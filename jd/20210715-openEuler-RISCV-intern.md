# 笑死，一个实习生都没有就敢开始做 openEuler RISC-V 的移植

（没错，就是那个[最近在开源之夏2021活动](https://mp.weixin.qq.com/s/-VRBfZpfedKZDSf6ojjU1w)中[火爆到不要不要的](https://mp.weixin.qq.com/s/qy3r8wE-LR4GtzF4tBYGVw) openEuler。）

openEuler 是国内的 yet another Linux Distribution （Linux 发行版）。起初由 华为 发起，中科院软件所是最早一批和目前（可能）最活跃的社区贡献单位（由软件所的OS团队贡献）。2021年7月开始，PLCT实验室开始与华为的工程师一起负责 RISC-V 平台上的 oE 的构建和维护工作。

目前老板和资金已经到位，项目经理已经就绪，测试团队已经组建，CI基础设施订单已下。软硬件环境都已经准备好，就差你来干活了（bushi）。

好了说正经的，上JD～

（[全职请点这里](https://mp.weixin.qq.com/s/wXj-w5QCfRCLZ8eko1ysxQ)；其它实习岗位点[这里](https://mp.weixin.qq.com/s/p3drKlnvhkMB9IyEH3NlBA)）

### NJ53 openEuler RISC-V 开发实习生

工作内容：
从事 Linux 发行版的软件包构建、测试、分析工作。

要求：
- 自我感觉达到LV2即可；喜欢倒腾新技术、喜欢编译尝试开源软件的同学们优先。
- 需要先去 gitee 上逛逛 oE RISC-V 的有关信息，看看会议纪要，构建的状态等。
  构建状态 https://build.openeuler.org/project/show/openEuler:Mainline:RISC-V
  会议纪要 https://etherpad.openeuler.org/p/sig-RISC-V-meetings

不管是否决定来实习，都欢迎加老板微信 lazyparser 先拉你到 oE RISC-V SIG 的群里。每两周开会，各种讨论事项都很公开。来感受下业界的脉搏，说不定以后毕业未来的面试官/老板就在群里😄

## 如何正确的投递简历

在投递简历之前最好对我们有更多一点了解。以下是阅读材料：

- [极简项目管理](https://github.com/lazyparser/minimalist-team-leader) 是目前PLCT实验室的管理方式，实习生也在管理范围内。请先阅读。
- [我们如何进行实习生招聘](https://github.com/lazyparser/weloveinterns/blob/master/how-do-we-interview-interns.md)
- [我们如何对实习生进行能力评定和培养](https://github.com/lazyparser/weloveinterns/blob/master/how-do-we-rank-interns.md)
- [实习生生存手册](https://github.com/lazyparser/survivial-manual-for-interns) 目前还在断断续续的撰写中，欢迎围观和贡献PR (Pull Requests)

阅读之后，接下来就可以发邮件了。以下内容请认真阅读。不符合条件邮件不会收到回复。

有意者请投递简历至：
**吴老师 wuwei2016@iscas.ac.cn**

邮件标题请注明：
**岗位编号 - 姓名 - 手机号码 - 学校**

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
6. 熟练使用 Google 搜索引擎。
7. 熟练使用 Git，能够自己 rebase 解决 conflicts。
8. （加分）自学了 RISC-V 指令集，包括 RV32GC 和 RV64GC。在自己的电脑上部署运行起来QEMU-RISCV64以及Spike模拟器。
9. （加分）对于网络知识有基本了解并熟练使用，例如SSH任意端口登陆、Port Forwarding、反向链接、ProxyCommand 等配置自行掌握。

## PLCT Lab

PLCT全称是程序语言与编译技术实验室，隶属于中科院软件所智能软件研究中心（ISRC），致力于成为编译技术领域的开源领导者，推进开源工具链及运行时系统
等软件基础设施的技术革新，具备主导开发和维护重要基础设施的技术及管理能力。与此同时，努力成为编译领域培养尖端人才的黄埔军校，推动先进编译技术在国
内的普及和发展。
