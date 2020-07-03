# LLVM + RISC-V 技术讨论会 2020-07-05

Title: LLVM + RISC-V Meetup July 5th 2020

Hi all,

OSDT社区组织的 LLVM + RISC-V 技术讨论会将在7月5日周日上午10点开始。本次讨论的议题已经确定，活动形式采用线上 Zoom 会议 + B站直播的形式，欢迎国内外的小伙伴参与。报告以中文为主。

The next OSDT Meetup will happen on July 5th, 2020. The location is webinar style, using Bilibili live streaming and Zoom Meeting. Topics cover RISC-V software porting / enhancement and LLVM toolchain family.

本次活动由OSDT开源开发工具社区（含HelloGCC、HelloLLVM）与 Shanghai RISC-V Group 联合组织。感谢中科院软件所智能软件研究中心（ISRC）提供 Zoom 会议赞助。

We thank Shanghai RISC-V Group for event organization and I.S.C.A.S. for Zoom sharing. This meetup is hold by OSDT community (formerly HelloGCC and HelloLLVM communities).

## 活动时间 Program

2020年7月5日 周日 10:00 AM - 12:00 AM

Sunday, July 5, 2020 at 10:00:00 am	CST	UTC+8 hours Shanghai

Saturday, July 4, 2020 at 7:00:00 pm	PDT	UTC-7 hours Las Vegas (USA - Nevada)

Sunday, July 5, 2020 at 02:00:00 Corresponding UTC (GMT)

## 活动议程 / Program

0. 开场介绍（吴伟 as MC）
0. Opening - Wei Wu (chair)
1. 蒙斌 - VxWorks on RISC-V: 切换 LLVM 编译器遇到的一些问题分享
1. Bin Meng - VxWorks on RISC-V: What we've learned about LLVM RISC-V toolchain
2. MaskRay - Clang 的 gcov 实现
2. MaskRay - GCov implementations in Clang
3. 王萌 - Spike模拟器Snapshot功能技术方案及实现分享
3. Meng Wang - implement snapshot feature for Spike RISC-V simulator
4. 陈影 - 基于LLVM实现RISC-V用户自定义指令支持——以玄铁C910处理器为例
4. Ying Chen - Custom ISA Support Using LLVM: XuanTie C910 as an example
5. 自由话题讨论
5. Free discussion

**蒙斌 - VxWorks on RISC-V: 切换 LLVM 编译器遇到的一些问题分享**

分享 VxWorks 操作系统在支持 RISC-V 架构从 GCC 编译器切换到 LLVM 过程中遇到的各种“坑”

演讲者蒙斌来自风河系统中国研发中心，VxWorks 产品部门高级研发经理。开源社区积极参与者和贡献者，RISC-V 坚定的推广者 :)

**MaskRay - Clang 的 gcov 实现**

GCC提供 gcov 用于实现code coverage。本次主题浅析clang对它的兼容实现和最近本人的一些改进。

MaskRay，一个活跃的LLVM开发者(LLD+binary utilities维护者，缓慢学习clang/middle-end/CodeGen)，退休的Algo/CTF/Student Cluster Competition选手/emacs-lsp维护者。ccls++🎉


**王萌：Spike模拟器snapshot功能技术方案及实现分享**

Spike 是用于验证RISC-V程序的模拟器，使用 C++ 编写，提供了模拟一个或多个 RISC-V hart 的功能模型。我们在spike的基础上进行开发，为其实现 snapshot 即快照功能，用于程序状态的保存及恢复。目前，我们已经完成了部分功能开发，本次报告将针对其技术方案和具体实现进行介绍。

王萌，武汉大学大二和大三之间，PLCT实验室模拟器分支LV3实习生。指导老师：PLCT实验室李威威主管。

**陈影：基于LLVM实现RISC-V用户自定义指令支持——以玄铁C910处理器为例**

基于LLVM框架，说明如何实现其中RISC-V后端的用户自定义指令的支持，并以玄铁C910处理器为例，具体说明如何在LLVM中添加其扩展指令集的支持。玄铁 C910的指令集架构是在RISC-V标准指令集架构的基础上，增加了部分自定义指令，以提高处理器性能，这部分扩展指令集主要包括有Cache指令子集，同步指令子集，算术运算指令子集，位操作指令子集以及存储指令子集。本次报告阐述的主要工作就是如何RISC-V后端实现这些扩展指令的支持。具体工作内容包括：为LLVM的RISCV后端添加一个C910命令行选项，实现llvm-mc汇编器的支持，使用TableGen语言编写全部扩展指令的汇编代码，能够将玄铁C910汇编指令汇编生成二进制文件，并编写测试用例，验证汇编指令编码的正确性。本项目对于在LLVM中添加用户自定义指令具有良好的指导意义，未来计划考虑添加对其他指令集架构的支持。

陈影，就读于合肥工业大学计算数学专业，研究生在读，目前在中科院软件所PLCT实验室实习。指导老师PLCT实验室邢明杰高级工程师。

## 直播观看（永久地址，可收藏）

https://live.bilibili.com/10339607

不需要报名，直接看。如果有B站账号，登陆之后可以进行弹幕提问。

Anyone who has internet access could watch this meetup using Bilibili live streaming.

Login users could post questions using DanMu feature.

## 通过 Zoom 参加

我们将在会议当天上午通过 HelloGCC 公众号（搜索 hellogcc2007）发布会议信息。请通过负责人微信或HelloGCC公众号与我们联系，获取Zoom会议室信息。没有微信的朋友请通过 lazyparser at gmail.com 跟我联系，请在邮件标题中体现本次活动信息以免被垃圾邮件过滤。

Please drop an email to Wei Wu (lazyparser at gmail.com) for Zoom ID (and passcode).

## 演讲报名

目前仍可以进行闪电演讲，请联系OSDT社区负责人吴伟报名。直接负责人微信报名或通过 lazyparser at gmail.com 后台留言。

Lightning talks are welcome. Please contact Wei Wu if you want to give a talk.

![](https://github.com/hellogcc/osdt-weekly/blob/master/images/hellogcc-wuwei.jpeg)
https://github.com/hellogcc/osdt-weekly/blob/master/images/hellogcc-wuwei.jpeg
