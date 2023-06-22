# 召唤「镖」之勇者！ 实习岗位：Porting DartVM to RISC-V

TL;DR: PLCT实验室2022年路线图中包含了移植DartVM到RISC-V架构，但是一直没有招募到合适的勇者（非常稀缺的LV4+实习生），所以一直在咕。但～是～！前不久，Google Dart Team 最新的版本中已经包含了初步的RISC-V支持！于是乎我们从躺平中惊坐起，觉得**难度大幅度降低，LV3+的实习生也可以开始参与了**！

PLCT实验室全称是程序语言与编译技术实验室，致力于成为编译技术领域的开源领导者，推进开源工具链及运行时系统等软件基础设施的技术革新，具备主导开发和维护重要基础设施的技术及管理能力。与此同时，努力成为编译领域培养尖端人才的黄埔军校，推动先进编译技术在国内的普及和发展。


## BJ32 Dart for RISC-V 开发实习生

工作内容：
- 就像将 V8 移植到 RISC-V 平台一样，将 Dart 移植到 RISC-V 平台。负责跟 Dart 上游交流，将移植工作 upstream。路线上先从 RV64GC 开始做。

入职要求：
- 这份工作目前没有正式员工在做，需要一位能力在LV3及以上的同学，与PLCT实验室的mentor和DartVM上游协作（默认mentor是 V8 RISC-V 的maintainer）。
- 学习了 Dart 语言（现学3天的水平即可）。
- 基本了解 DartVM 的内部实现（至少学了一周，看过文档、看过技术分享视频、看过源代码、编译运行起来了）。
- 熟悉语言虚拟机的内部实现（看过书，知道解释器、字节码、JIT、GC、锁、线程等等）
- 脸皮厚。能跟外国人直接英语对线。

## 我有兴趣！

第一步：按照入职要求准备；第二步：继续往下看，投简历～

## 如何正确的投递简历

在投递简历之前最好对我们有更多一点了解。以下是阅读材料：

- [极简项目管理](https://github.com/lazyparser/minimalist-team-leader) 是目前PLCT实验室的管理方式，实习生也在管理范围内。请先阅读。
- [我们如何进行实习生招聘](https://github.com/lazyparser/weloveinterns/blob/master/how-do-we-interview-interns.md)
- [我们如何对实习生进行能力评定和培养](https://github.com/lazyparser/weloveinterns/blob/master/how-do-we-rank-interns.md)
- [实习生生存手册](https://github.com/lazyparser/survivial-manual-for-interns) 目前还在断断续续的撰写中，欢迎围观和贡献PR (Pull Requests)

阅读之后，接下来就可以发邮件了。以下内容请认真阅读。不符合条件邮件不会收到回复。

有意者请投递简历至：
**吴伟 wuwei2016@iscas.ac.cn**

邮件标题请注明：
**岗位编号 - 姓名 - 手机号码 - 学校**

（兼职实习的伙伴可以用【兼职】取代【学校】）

邮件正文请:
**进行跟应聘职位相关的自我介绍**，不超过300字。

邮件必须附带简历。**没有PDF格式简历的邮件不保证会收到回复**。

## 所有实习生共性要求（技术类）

开放岗位的入职要求（教学助理等非技术类的同学只需要满足前两条）：

1. 良好的沟通理解能力、能够观察和感知他人的态度和观点。能够主动沟通、遇到计划外或坏消息能够大声的说出来。
2. 知道如何陈述bugs/issues以及向其他人求助，如何不浪费同事的时间，将复现bug需要的信息提供完整。
3. 能力值评定一般要求达到LV2级别及以上。参见：[我们如何面试实习生](https://github.com/lazyparser/weloveinterns/blob/master/how-do-we-interview-interns.md)，[我们如何给实习生评级](https://github.com/lazyparser/weloveinterns/blob/master/how-do-we-rank-interns.md)。
4. 热爱编程，经常写代码。C/C++/Java/JavaScript 任何一种常见语言都可以。
5. 熟练使用 Linux 命令行；会一点 Python/Bash 脚本进行自动化。
6. 熟练使用 Google 搜索引擎、流畅高清看油管。
7. 熟练使用 Git，能够自己 rebase 解决 conflicts。
8. （加分）自学了 RISC-V 指令集，包括 RV32GC 和 RV64GC。在自己的电脑上部署运行起来QEMU-RISCV64以及Spike模拟器。
9. （加分）对于网络知识有基本了解并熟练使用，例如SSH任意端口登陆、Port Forwarding、反向链接、ProxyCommand 等配置自行掌握。

（不确定是否合适？可以直接添加PLCT实验室负责人的微信 lazyparser 咨询。添加的时候请备注【BJ32】或其它实习岗位的编号方便通过。）
