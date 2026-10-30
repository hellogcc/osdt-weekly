---
title: 关于
description: OSDT Weekly（开源开发工具周报）的来由、更新节奏、投稿与引用方式。
---

## 这是什么

**OSDT Weekly**（开源开发工具周报）是由 HelloGCC 与 HelloLLVM 社区发起和维护的摘要类周刊，内容覆盖 GCC、LLVM/Clang/LLDB/LLD、GDB、Binutils、glibc、QEMU、TVM、RISC-V 等开源开发工具与社区的一周动态。

每期通常包含：

- **近期活动预告** —— 编译器与工具链相关的会议、聚会、征稿（CfP）；
- **编译社区的八卦信息** —— GCC、BINUTILS、GDB、GLIBC、LLVM/Clang、QEMU、RISC-V in China、RT-Thread、AI Compilers 等分节，摘录邮件列表、代码评审与社区讨论的要点；
- **本周工具链岗位** —— 与编译器、工具链相关的社招与实习岗位。

## 发布节奏

每周三晚上发布一期，期号连续递增。当前站点共 {{< issue-count >}} 期，最早一期为 2019 年 7 月。

## 内容怎么维护

周报正文以 Markdown 保存在仓库 {{< param "github" >}} 的 `weekly-<年份>/` 目录下，文件名是当期日期（如 `weekly-2026/2026-11-04.md`）。欢迎提 Issue 或 PR 补充线索、纠正描述。

站点由仓库内的 `website/` 目录构建：`scripts/gen_issues.py` 会读取全部 `weekly-*/YYYY-MM-DD.md`，按标题里的「第 N 期」生成 `/issue/N/` 页面与索引数据，因此新增一期只需要往仓库里加一个 md 文件。

## 订阅

- **RSS**：订阅地址是 `{{< abs-url path="rss.xml" >}}`（推荐，无需邮箱）
- **邮件订阅**：服务选型中，页面上的输入框暂时禁用；开通后会在此处与页头同步告知。

## 引用与转载

转载请注明「来源：OSDT Weekly 第 N 期」并附上对应期号的链接。文中引用的原文链接归各原作者所有。

## 联系

- 仓库 Issue 与 PR：{{< param "github" >}}/issues
- 社区：HelloGCC / HelloLLVM
