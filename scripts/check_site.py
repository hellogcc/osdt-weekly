#!/usr/bin/env python3
"""构建产物自检：站内链接可达性 + 期号完整性 + RSS 校验。

用法：
    python3 scripts/check_site.py                  # 检查 website/public
    python3 scripts/check_site.py --dir some/dir
"""
import argparse
import os
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, unquote

# 注意：hugo --minify 会去掉属性引号（href=/issue/1/），两种形态都要覆盖
HREF_RE = re.compile(r'(?:href|src)=(?:"([^"]+)"|([^\s>]+))')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="website/public")
    args = ap.parse_args()
    root = os.path.abspath(args.dir)
    if not os.path.isdir(root):
        sys.exit(f"找不到构建目录 {root}，先跑 hugo")

    htmls = []
    for dirpath, _, files in os.walk(root):
        for f in files:
            if f.endswith(".html"):
                htmls.append(os.path.join(dirpath, f))
    htmls.sort()

    broken, checked = [], 0
    for path in htmls:
        with open(path, encoding="utf-8", errors="replace") as fh:
            html = fh.read()
        for m in HREF_RE.finditer(html):
            href = (m.group(1) or m.group(2) or "").strip()
            if href.startswith(("mailto:", "javascript:", "#", "data:")):
                continue
            u = urlparse(href)
            if u.scheme in ("http", "https"):
                continue  # 外链不在静态可达性检查范围内
            target = unquote(u.path)
            if not target:
                continue
            tpath = os.path.normpath(os.path.join(root, target.lstrip("/")))
            candidates = [tpath, os.path.join(tpath, "index.html")]
            checked += 1
            if not any(os.path.exists(c) for c in candidates):
                broken.append((os.path.relpath(path, root), href))

    # 未发布期号：不应有页面，也不该出现在首页与 RSS 里
    withheld = set()
    wf = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      "scripts", "withheld_issues.txt")
    if os.path.exists(wf):
        with open(wf, encoding="utf-8") as fh:
            for line in fh:
                s = line.split("#", 1)[0].strip()
                if s.isdigit():
                    withheld.add(int(s))
    leaked = []
    for n in sorted(withheld):
        if os.path.exists(os.path.join(root, "issue", str(n), "index.html")):
            leaked.append(f"/issue/{n}/ 页面存在")
        for f in ("index.html", "rss.xml"):
            p = os.path.join(root, f)
            if os.path.exists(p):
                with open(p, encoding="utf-8", errors="replace") as fh:
                    if f"/issue/{n}/" in fh.read():
                        leaked.append(f"{f} 里出现 /issue/{n}/")

    # 期号完整性
    issues = sorted(int(d) for d in os.listdir(os.path.join(root, "issue"))
                    if d.isdigit() and os.path.isdir(os.path.join(root, "issue", d))) \
        if os.path.isdir(os.path.join(root, "issue")) else []
    gaps = sorted(set(range(1, issues[-1] + 1)) - set(issues) - withheld) if issues else []

    # RSS
    rss_ok, rss_items, rss_err = False, 0, ""
    rss_path = os.path.join(root, "rss.xml")
    if os.path.exists(rss_path):
        try:
            tree = ET.parse(rss_path)
            items = tree.getroot().findall("./channel/item")
            rss_items = len(items)
            rss_ok = rss_items > 0 and all(
                i.findtext("link") and i.findtext("guid") for i in items)
            if not rss_ok:
                rss_err = "有条目缺 link 或 guid"
        except ET.ParseError as e:
            rss_err = f"XML 解析失败: {e}"
    else:
        rss_err = "rss.xml 不存在"

    print(f"HTML 页面: {len(htmls)}")
    print(f"站内链接检查: {checked} 个，坏链 {len(broken)} 个")
    for page, href in broken[:20]:
        print(f"  ✗ {page} → {href}")
    print(f"期号页面: {len(issues)} 个，范围 {issues[0] if issues else '-'}-{issues[-1] if issues else '-'}"
          + (f"，缺号 {gaps[:10]}" if gaps else "，无缺号"))
    if withheld:
        print(f"未发布（草稿）: {sorted(withheld)}，泄漏 {len(leaked)} 处")
        for item in leaked[:10]:
            print(f"  ✗ {item}")
    print(f"RSS: {'正常' if rss_ok else '异常'}，{rss_items} 条" + (f"（{rss_err}）" if rss_err else ""))

    if broken or gaps or leaked or not rss_ok:
        sys.exit(1)
    print("全部通过")


if __name__ == "__main__":
    main()
