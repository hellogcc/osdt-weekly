# OSDT 线上技术交流会 2020-07-26

视频回放：

https://www.bilibili.com/video/BV12a4y1a7Xu

OSDT 社区组织的线上技术讨论会将在7月26日周日上午10点开始。本次依然采用线上形式。欢迎大家报名演讲。

话题范围：围绕开源开发工具，以及基于LLVM等开源系统做的二次开发工作。尤其欢迎 RISC-V 的软硬件开源爱好者、开源 EDA 工具的从业者分享自己的经验。

## 活动时间 / Time

- 2020年7月26日 周日上午10点
- 美国西海岸25日晚上7点

## 活动议程 / Program

- Wei Wu (chair) - 开场介绍
- Mohanson - 如何通过 LLVM-9 将 WebAssembly WASI 程序翻译到 x86/RISC-V ELF 程序(AOT)
- MaskRay - 讨论 RISC-V Linker Relaxation 的弊端（狗头）
- 闪电：廖春玉 - clang中实现forstmt转换
- 闪电：陆旭凡 - 在LLVM指令选择中如何一条指令有多个寄存器类
- 闪电：陆旭凡 - 展示下最近对llvm栈分配的学习
- Free discussion

**Mohanson - 如何通过 LLVM-9 将 WebAssembly WASI 程序翻译到 x86/RISC-V ELF 程序(AOT)**

与大多数采用 WebAssembly 的公链不同(以太坊 2.0, EOS ... ), Nervos CKB 是使用 RISC-V 指令集的公链. 在过去的一段时间, 得益于 GCC 与 LLVM 对 RISC-V 的支持, 我们证明可以通过一些技术手段, 将 WebAssembly 程序在没有大的性能损失的前提下翻译为 RISC-V 程序。 WASC 便是这个解决方案的实践. 我将分享介绍 WASC 实现的原理, 在实现过程遇到的问题及解决方式, 以及最后对 WebAssembly 指令集与 RISC-V 指令集的反思。

Mohanson, cryptape 高级工程师. 2014年毕业于安徽大学通信工程, 早年任职于科大讯飞与又拍云从事数字图像处理与 Deep Learning 相关工作; 2017年后开始在区块链虚拟机, 智能合约编程语言与编译器方向发展. 曾主导/参与过一些开源项目，包括 CITA-WM、minits、gameboy模拟器、pywasm 等。

博客主页: http://accu.cc

Github 主页: https://github.com/mohanson

我主导的一些项目(公司项目, 均已开源):

- CITA-VM: CITA 是国内知名的联盟链解决方案, CITA-VM 则是 CITA 的虚拟机模块, 采用 EVM 指令集.

- minits: TypeScript 的静态编译方案, 底层使用 LLVM, 可以将 ts 的一个语法子集编译到 RISC-V, x86 和 WebAssembly. 在去年的中国开源年会(11月 02-03日, 华东师范大学), 我做了关于 minits 的主题演讲.

我的一些个人项目:

- gameboy 模拟器. github 上 star 数量相对靠前的一个 gb 模拟器实现, 我的博客上有关于模拟器技术的教程, 约 30 来万字, 本来是准备出版的, 不过收到了任天堂的律师函警告只能作罢.

- pywasm: 纯 python 实现的 webassembly 解释器, python 社区曾有 pypi 核心开发者提议将 wasm 写入 python 标准库, 提议人的初版实现便是使用的 pywasm. 国外有个大学(可能是印度)也使用了它来进行计算机实验课教学, 几年前发过邮件征求过我意见, 不过具体忘记是哪个学校了.

**MaskRay - 讨论 RISC-V Linker Relaxation 的弊端（狗头）**

与多数RISC架构不同，RISC-V采用支援指令删除的linker relaxation实现长距离的跳转/内存存取。本主题和大家探讨一下linker relaxation给工具链造成的困难，以及特别地，在LLD中实现R_RISCV_ALIGN/R_RISCV_RELAX的困难。

TODO brief introduction for this talk

MaskRay，一个活跃的LLVM开发者 (LLD+binary utilities 维护者，缓慢学习 clang/middle-end/CodeGen)，退休的Algo/CTF/Student Cluster Competition 选手 / emacs-lsp 维护者。ccls++🎉

MaskRay is an active LLVM developer (maintains LLD + Binary Utilities, learning clang/middle-end/codegen slowly), a retired Algo / CTF / Student Cluster Competition athlete / emacs-lsp maintainer. ccls++🎉


**闪电：廖春玉 - clang中实现forstmt转换**

廖春玉，PLCT Lab 员工。长期做 Clang/LLVM 的开发工作。

**闪电：陆旭凡 - 在LLVM指令选择中如何一条指令有多个寄存器类**

陆旭凡，人海中一名普普通通的大学生。最近在 PLCT Lab 实习，开始在 LLVM 社区围绕 RISC-V 后端贡献代码。

**闪电：陆旭凡 - 展示下最近对llvm栈分配的学习**

跟上边是同一个同学。

## 直播观看（永久地址，可收藏）

https://live.bilibili.com/10339607

不需要报名，直接看。如果有B站账号，登陆之后可以进行弹幕提问。

## 通过 Zoom 参加

本次Zoom会议由RISC-V基金会提供，需要填写一下邮箱地址，之后会得到一个自己唯一的URL，记住这个URL，到时候在浏览器中输入，按照提示安装插件或客户端进入。点击【查看原文】可以进入zooom页面。

https://zoom.us/webinar/register/WN_UYtzSRPwQ0K6w3kGsEBjbQ

## 演讲报名

目前仍可以进行闪电演讲，请联系OSDT社区负责人吴伟报名。直接负责人微信报名或通过 lazyparser at gmail.com 后台留言。

![](https://github.com/hellogcc/osdt-weekly/blob/master/images/hellogcc-wuwei.jpeg)

https://github.com/hellogcc/osdt-weekly/blob/master/images/hellogcc-wuwei.jpeg
