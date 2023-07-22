# 周日：南京线下聚会议程更新

周日下午2点见！记得点击左下角【查看原文】进行报名～

## 时间和地点

2023年7月23日（周日）下午 14:00 - 18:00

大体上的时间安排如下：

- 14:00 - 15:30 RISC-V 社区最近的好玩的事情
- 15:30 - 17:00 编译器主题（HelloGCC、HelloLLVM）
- 17:00 - 18:00 闪电演讲、自由讨论

具体的议程：

- Sipeed RISC-V Laptop 原型机：现场上手体验！ by 泽畔
- 基于 BuildStream 及 Freedesktop SDK 构建哪吒系统镜像 by 李瑞彬
- 基于 Buddy Compiler 的深度学习编译优化 by 周旭林
- 国内开源社区现状讨论及八卦交流分享 by 吴伟

**Sipeed RISC-V Laptop 原型机：现场上手体验！ by 泽畔**

The title tells it all.
没有介绍。直接现场上手。

**基于 BuildStream 及 Freedesktop SDK 构建哪吒系统镜像**

大家好我是广州的开源软件爱好者和 Linux 系统软件开发从业者，名叫李瑞彬，英文名 Robin
Lee。开源社区方面主要参与 Fedora 和 Freedesktop SDK 等项目。

下面是演讲内容的提纲：

1. Freedesktop SDK 简介
2. BuildStream 简介
    1. 若干 element 代码结构展示
    2. 使用 cache key 索引构建产物、日志、失败状态
    3. source track
3. Freedesktop SDK 构建主要环节
    1. live-bootstrap 项目简介
    2. bootstrap 及构建整体流程
    3. 使用 genimage 工具生成磁盘镜像
4. 演示——在干净环境用容器启动 Freedesktop SDK 构建
5. 演示——构建完成后提取系统镜像
6. 未来畅想
    1. 支持 loongarch64，建立其 flatpak 基础运行环境和工具链
    2. 支持更多 RISC-V 开发板
    3. GNOME OS (Wayland) on RISC-V boards
    4. Bootstrap Gentoo stage1 based on  Freedesktop SDK，将 Freedesktop
SDK 的 bootstrap 流程延伸到主流发行版
    5. Freedesktop-SDK-based Kairos 镜像，自主可控的 K3s 基础操作系统

下面是关于 BuildStream 及 Freedesktop SDK 的简要介绍：

Freedesktop SDK 是一个开源项目，官网是 https://freedesktop-sdk.io/ , 源码库为
https://gitlab.com/freedesktop-sdk/freedesktop-sdk 。它是一个 BuildStream
project。与 Yocto/Buildroot 等项目比较相似。它内部包含了一个以 Live-bootstrap
项目(https://github.com/fosslinux/live-bootstrap)为起点的 bootstrap 流程，并以
Reproducible build 为其主要追求。但可能更可能为人了解的方面，是 Freedesktop SDK 为 Flatpak
生态系统提供 SDK 和 runtime。几乎所有 Flathub 上的 flatpak 均运行在 Freedesktop SDK 的
runtime 或其扩展 runtime 之上。

BuildStream 是一个自动化构建工作，官网是 https://buildstream.build/ ，源码库为
https://github.com/apache/buildstream ，托管于 Apache 基金会之下。它通过 YAML
文件描述各个软件组件及转化步骤的构建流程，每个 YAML 文件称为一个 element。BuildStream 会为每个 element
根据影响该 element 构建结果的所有条件因子计算一个 hash 值作为 cache key，从而可以快速从 cache
中提取构建产物、日志、失败状态等。

Freedesktop SDK 当前已支持 RISC-V 架构，并支持少量开发板。我个人 RISC-V 相关的工作是基于
Freedesktop SDK 初步实现了哪吒开发板的系统镜像构建。


**基于 Buddy Compiler 的深度学习编译优化**

本次分享时长为5分钟左右，主要介绍 Buddy Compiler 中深度学习模型的端到端推理支持情况与关键算子的优化成果。希望能借助这个机会宣传我们 Buddy Compiler 社区，推广开源之夏2023中深度学习模型编译优化的相关工作，吸引更多志同道合的小伙伴一起交流。期待能在广州见到大家！

大家好我是周旭林，最开始在中科院软件所PLCT实验室 MLIR 小队跟随张洪滨 mentor 实习，负责 RISC-V 向量拓展指令集和深度学习编译优化的相关工作，至今已有半年。目前我在**开源之夏2023**中担任 Buddy Compiler 社区相关项目的导师，并将于今年九月份正式成为中科院软件所的研究生。希望能将目前的实践经验与日后的科研课题联系起来，继续跟给力的小伙伴一起合作探索有趣的事情。

## 线下聚会报名形式

请点击下方链接或微信文章左下角【查看原文】进行报名：

https://www.wenjuan.com/s/VbArMj/

聚会地点：广州易尚国泰大酒店18楼2号会议室（暂定）

广州市越秀区环市东路376号,距离地铁5号线淘金站183米

感谢 **杭州全橙智能软件有限公司** 提供场地赞助！

## 线上 Zoom 参会

- 7月23日 14:00
- Topic: 广州线下聚会（RISC-V and 编译技术）
- 参会链接： https://us02web.zoom.us/j/85944440554?pwd=Vy8xMDkrbUx1NnZWNU9UMDcyQVNPQT09
- Meeting ID: 859 4444 0554
- Passcode: 789621

## 活动形式

松散的线下聚会形式。现场有投影仪，可能会有几个非正式的技术分享。大家一起聊聊天，八卦八卦。

## 技术分享（演讲）的内容和形式要求

- 演讲内容可以是自己近期在做的 patch、开发的心得体会、社区的八卦等。内容和工具链、模拟器、虚拟机、内核、RISC-V等有一项相关即可。同时也欢迎介绍新技术领域的进展。
- 演讲时长没有严格要求，可以是5分钟的闪电演讲，也可以是25分钟的长演讲。欢迎新语言、新工具的 Tutorial。

## 关注公众号获取大会后续信息

**HelloGCC**

- 社区博客： https://hellogcc.org
- 微信公众号：hellogcc2007
- 邮件列表： hellogcc@freelists.org

**HelloLLVM**

- 社区博客： https://hellollvm.org
- 邮件列表： hellollvm@freelists.org

**CNRV**
- 社区博客： https://cnrv.io
- 微信公众号：risc-v