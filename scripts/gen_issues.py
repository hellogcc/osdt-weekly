#!/usr/bin/env python3
"""把仓库里的 weekly-YYYY/*.md 转成 Hugo 内容。

用法：
    python3 scripts/gen_issues.py              # 生成/覆盖 website/content/issue 与 data/issues.yaml
    python3 scripts/gen_issues.py --check      # 只统计，不写文件

规则：
- 期号取自首行 H1 里的「第N期」；没有的（2019-07-10 首期）按时间顺序兜底为 1，并校验连续性。
- 首行 H1 由页面模板渲染，正文里删掉；其余 H1 降级为 H2（避免一页多个 H1）。
- 删掉「点击「查看原文」…」那段样板介绍及其后的裸 GitHub 链接（站点自己就是阅读入口）。
- images/ 复制到 website/static/images/，因为个别往期用 /images/xxx 绝对路径引图。
- 生成物不入库（.gitignore），CI 与 make 每次构建前重新生成。
"""
import glob
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_CONTENT = os.path.join(ROOT, "website", "content", "issue")
OUT_DATA = os.path.join(ROOT, "website", "data", "issues.yaml")
OUT_STATIC_IMG = os.path.join(ROOT, "website", "static", "images")

BOILER_MARK = "点击「查看原文」"
ISSUE_RE = re.compile(r"第\s*(\d+)\s*期")
WITHHELD_FILE = os.path.join(ROOT, "scripts", "withheld_issues.txt")


def load_withheld():
    """读取未发布（草稿）期号列表：一行一个，`#` 起注释。文件不存在即视为全部发布。"""
    if not os.path.exists(WITHHELD_FILE):
        return set()
    out = set()
    with open(WITHHELD_FILE, encoding="utf-8") as f:
        for line in f:
            s = line.split("#", 1)[0].strip()
            if s.isdigit():
                out.add(int(s))
    return out


def read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def strip_title_and_boiler(text):
    """返回 (body, h1_title)。"""
    lines = text.split("\n")
    h1 = ""
    body_lines = []
    i = 0
    # 首个非空行若是 H1，取出作为标题（模板会渲染）
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].startswith("# "):
        h1 = lines[i][2:].strip()
        i += 1
    lines = lines[i:]

    # 删除样板段：含标记的行起，连同紧随其后的、以 http 开头的裸链接行
    cleaned = []
    skip_next_url = False
    for line in lines:
        s = line.strip()
        if BOILER_MARK in s:
            skip_next_url = True
            continue
        if skip_next_url:
            if not s:
                continue
            if s.startswith(("http://", "https://")):
                skip_next_url = False
                continue
            skip_next_url = False
        cleaned.append(line)

    # 其余 H1 降级为 H2
    out = []
    for line in cleaned:
        if line.startswith("# ") and not line.startswith("## "):
            out.append("#" + line)
        else:
            out.append(line)

    body = "\n".join(out)
    # 原文里偶有裸域名链接（如 www.llvm.org/...），补上 https:// 才能点开
    body = re.sub(r"\]\((www\.[^)\s]+)\)", r"](https://\1)", body)
    return body.strip("\n"), h1


def summarize(body, limit=120):
    """取第一个有实际内容的段落，去掉 markdown 标记与 URL。"""
    for para in re.split(r"\n\s*\n", body):
        p = para.strip()
        if not p or p.startswith(("#", ">", "-", "*", "|", "```", "![")):
            continue
        p = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", p)
        p = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", p)
        p = re.sub(r"https?://\S+", "", p)
        p = re.sub(r"[*_`>#]", "", p)
        p = re.sub(r"\s+", " ", p).strip()
        if len(p) >= 20:
            return p[:limit].rstrip() + ("…" if len(p) > limit else "")
    return ""


def sections_of(body, limit=10):
    """提取正文里的小节标题（H3 优先，退化为 H2），用于列表展示。"""
    h3 = re.findall(r"(?m)^###\s+(.+?)\s*$", body)
    h2 = re.findall(r"(?m)^##\s+(.+?)\s*$", body)
    picks = h3 or h2
    seen, out = set(), []
    for s in picks:
        s = re.sub(r"[*_`]", "", s).strip()
        if s and s not in seen:
            seen.add(s)
            out.append(s)
        if len(out) >= limit:
            break
    return " · ".join(out)


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main():
    check_only = "--check" in sys.argv
    files = sorted(glob.glob(os.path.join(ROOT, "weekly-*", "[0-9]*.md")))
    if not files:
        sys.exit("没有找到任何 weekly-*/YYYY-MM-DD.md")

    records = []
    for path in files:
        rel = os.path.relpath(path, ROOT)
        date = os.path.basename(path)[:-3]
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            print(f"  跳过（文件名不是日期）: {rel}")
            continue
        text = read(path)
        body, h1 = strip_title_and_boiler(text)
        m = ISSUE_RE.search(h1)
        r_issue = int(m.group(1)) if m else "?"
        records.append({
            "date": date,
            "year": date[:4],
            "path": rel,
            "h1": h1,
            "issue": int(m.group(1)) if m else None,
            "body": body,
            "desc": f"OSDT Weekly 第{r_issue}期（{date}）：GCC、LLVM、GDB、Binutils、QEMU 等开源开发工具社区的一周摘要。",
            "sections": sections_of(body),
        })

    records.sort(key=lambda r: r["date"])

    # 兜底与校验：缺号按时间序补齐，并确认无重复
    next_guess = 1
    for r in records:
        if r["issue"] is None:
            r["issue"] = next_guess
        next_guess = r["issue"] + 1
    nums = [r["issue"] for r in records]
    dup = {n for n in nums if nums.count(n) > 1}
    if dup:
        sys.exit(f"期号重复，需人工确认: {sorted(dup)}")
    missing = sorted(set(range(1, max(nums) + 1)) - set(nums))
    if missing:
        print(f"  注意：期号不连续，缺 {len(missing)} 个: {missing[:10]}")

    # 草稿期号：不生成页面、不进索引，首页/归档/RSS/上下期导航都会跳过
    withheld = load_withheld()
    if withheld:
        held = sorted(set(nums) & withheld)
        unknown = sorted(withheld - set(nums))
        records = [r for r in records if r["issue"] not in withheld]
        print(f"未发布（草稿）跳过 {len(held)} 期: {held or '无命中'}")
        if unknown:
            print(f"  注意：withheld_issues.txt 里有源文件不存在的期号: {unknown}")

    print(f"期数: {len(records)} | 期号范围: {min(r['issue'] for r in records)}-{max(r['issue'] for r in records)} | 年份: "
          f"{min(r['year'] for r in records)}-{max(r['year'] for r in records)}")
    print(f"带样板段被清理: {sum(1 for r in records if BOILER_MARK in read(os.path.join(ROOT, r['path'])))}")
    if check_only:
        return

    # 写内容
    if os.path.isdir(OUT_CONTENT):
        shutil.rmtree(OUT_CONTENT)
    os.makedirs(OUT_CONTENT, exist_ok=True)
    for r in records:
        fm = [
            "---",
            f"title: {yaml_str('OSDT Weekly 第' + str(r['issue']) + '期')}",
            f"issue: {r['issue']}",
            f"date: {r['date']}T00:00:00+08:00",
            f"description: {yaml_str(r['desc'] or ('OSDT Weekly 第' + str(r['issue']) + '期（' + r['date'] + '）'))}",
            f"source: {yaml_str(r['path'])}",
            f"sections: {yaml_str(r['sections'])}",
            "layout: issue",
            "---",
            "",
            r["body"],
            "",
        ]
        with open(os.path.join(OUT_CONTENT, f"{r['issue']}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(fm))

    # 写索引数据（首页/归档/年份页都用它）
    os.makedirs(os.path.dirname(OUT_DATA), exist_ok=True)
    lines = ["# 由 scripts/gen_issues.py 生成，请勿手工编辑", "issues:"]
    for r in sorted(records, key=lambda x: -x["issue"]):
        lines += [
            f"  - issue: {r['issue']}",
            f"    date: {yaml_str(r['date'])}",
            f"    year: {yaml_str(r['year'])}",
            f"    title: {yaml_str('第' + str(r['issue']) + '期')}",
            f"    sections: {yaml_str(r['sections'])}",
        ]
    with open(OUT_DATA, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    # 复制 images/（个别往期用 /images/xxx 绝对路径）
    src_img = os.path.join(ROOT, "images")
    if os.path.isdir(src_img):
        if os.path.isdir(OUT_STATIC_IMG):
            shutil.rmtree(OUT_STATIC_IMG)
        shutil.copytree(src_img, OUT_STATIC_IMG)
        print(f"图片: {len(os.listdir(OUT_STATIC_IMG))} 个已复制到 website/static/images/")

    print(f"已生成 {len(records)} 期 → {os.path.relpath(OUT_CONTENT, ROOT)}/")
    print(f"索引数据 → {os.path.relpath(OUT_DATA, ROOT)}")


if __name__ == "__main__":
    main()
