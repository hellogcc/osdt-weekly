# OSDT Weekly

## 简介

开源开发工具周报（OSDT Weekly）是由HelloGCC及HelloLLVM社区发起和维护的摘要类周刊。内容覆盖GCC、LLVM、GDB、Binutils、TVM、QEMU等开发人员常用的开源项目。每周三晚上发布。内容通过Git仓库托管在HelloGCC的GitHub账号里，欢迎提交PR :-)

仓库地址： https://github.com/hellogcc/osdt-weekly/

## 周报列表

- [2026](weekly-2026/)
- [2025](weekly-2025/)
- [2024](weekly-2024/)
- [2023](weekly-2023/)
- [2022](weekly-2022/)
- [2021](weekly-2021/)
- [2020](weekly-2020/)
- [2019](weekly-2019/)

## 网站（osdtweekly.com）

线上站点 <https://osdtweekly.com/>，Hugo 构建，源码全部在本仓库 `website/` 目录。

每期一个地址：`https://osdtweekly.com/issue/382/`；全部往期在 `/archive/`；订阅方式有两种：

- **RSS**：<https://osdtweekly.com/rss.xml>
- **邮件订阅**：页面上的表单已就位但**当前禁用**（订阅服务尚未选定）。开通时把 `website/hugo.toml` 里 `subscribeEnabled` 改成 `true`，并补上服务商所需的表单字段即可。

### 内容怎么来的

`website/content/issue/`、`website/data/issues.yaml`、`website/static/images/` 都是 `scripts/gen_issues.py` 生成物，**不入库**。脚本做的事：

1. 扫描 `weekly-<年份>/YYYY-MM-DD.md`，从首行 H1 的「第 N 期」取期号（首期 2019-07-10 没有期号，按时间顺序兜底为第 1 期）；
2. 删掉首行 H1（由页面渲染）与「点击「查看原文」…」那段样板说明（站点本身就是阅读入口）；
3. 其余 H1 降级为 H2，裸域名链接（`www.example.com/...`）补上 `https://`；
4. 生成 `/issue/N/` 页面、首页/归档用的索引数据，并把 `images/` 复制到站点静态目录。

所以**每周新增一期只需加一个 md 文件**，站点内容会自动跟着变。

### 草稿期号（暂不上站）

有些期写在仓库里但还没到发布时间。把期号一行一个写进 `scripts/withheld_issues.txt`，这些期就**不会生成 `/issue/N/` 页面**，也不进首页、归档、RSS 与上下期导航（`#` 之后是注释）。要放出来，删掉或注释掉那一行，重新构建即可。

当前草稿：第 382、383 期。

### 本地构建与自检

```sh
make site          # 生成期号页面 + 构建到 website/public
make site-serve    # 本地预览 http://localhost:1313/
make site-check    # 构建后自检：站内链接、期号连续性、RSS
```

依赖：Python 3（仅标准库）+ Hugo **0.147.9 extended**。

### 部署

`.github/workflows/pages.yml` 在 `master` / `main` 分支推送时触发（改 `weekly-*/*.md`、`website/**`、`scripts/**`、`images/**` 也会触发），构建并部署到 GitHub Pages。

首次启用需要：

1. 把本仓库同步到 GitHub；
2. Settings → Pages → Source 选 **GitHub Actions**；
3. Settings → Pages → Custom domain 填 `osdtweekly.com`（DNS 侧配 CNAME 指向 `<用户名>.github.io`），勾选 Enforce HTTPS。

未配域名前，站点会部署在 `https://<用户名>.github.io/<仓库名>/`，`baseURL` 由 `configure-pages` 自动适配，无需改配置。

### 站点素材

页面上没有第三方图片、图标与网络字体：favicon 与 RSS 图标是自绘 SVG，字体使用系统字体栈。往期正文里引用的外部图片链接保持原样，版权归各原作者。

