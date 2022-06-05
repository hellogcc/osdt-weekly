# BJ61 蝉语团队Cicada语言设计实习生招募（联合PLCT实验室）

本岗位为PLCT实验室与蝉语社区联合招聘岗位，实习关系在PLCT，mentor来自蝉语社区，工作内容是向蝉语社区的开源程序语言 Cicada 贡献代码。岗位信息来自 [cicada-internships](https://github.com/cicada-lang/cicada-internships)

## 来自蝉语社区的岗位介绍

**BJ61 蝉语实习生 / Cicada Internships**

[蝉语](https://github.com/cicada-lang) 是一个开源程序语言设计团队。

主要项目 [Cicada](https://github.com/cicada-lang/cicada)
是一个 Dependently Typed 程序语言（类似 Coq、Agda、Idris 和 Lean），
可以用来辅助证明数学定理，并却作为形式化的数学基础。

想要设计一个实用的计算机辅助证明系统的同时，这个语言也是大家学习与尝试新想法的基础。

程序语言设计就像 Web App 的设计一样，也分为 _前端_ 与 _后端_，
前端包括语法设计与类型系统设计，后端主要在于代码生成与编译器优化。
我们的工作偏重于程序语言设计的前端。

工作内容：

- 维护 [Cicada](https://github.com/cicada-lang/cicada) 的代码。
  - 由 TypeScript 实现，OOP 编程风格。
- 编写文档来介绍我们的语言，以普及 _机器辅助证明_ 与 _形式化数学基础_ 相关的知识。
  - 当前的文档在：https://cicada-lang.org/docs
- 探索类型系统的功能与实现方式。
  - 例如 Inductive datatype、递归函数、子类型关系等等。
  - 我们读类型论相关的书籍与论文，然后以研讨会和博客的形式分享。
  - 中文 Telegram 讨论群：https://t.me/CicadaLanguageCN

入职要求：

- 能读英文。
- 对 _程序语言设计_ 与 _类型系统设计_ 感兴趣。

说明：

- 目前 [Cicada](https://github.com/cicada-lang/cicada)
  的代码有 10000 行左右（包括 REPL，以及模块系统）。
  良好的代码结构在于容易理解（因而容易修改），
  我们努力注意保持良好的代码结构，
  但是代码中还是有很多有待改进的地方。
  也许通过讲解与讨论实现方式，
  我们能获得清晰的理解与更好的代码结构。


## 来自PLCT实验室的介绍

PLCT全称是程序语言与编译技术实验室，隶属于中科院软件所智能软件研究中心（ISRC），致力于成为编译技术领域的开源领导者，推进开源工具链及运行时系统等软件基础设施的技术革新，具备主导开发和维护重要基础设施的技术及管理能力。与此同时，努力成为编译领域培养尖端人才的黄埔军校，推动先进编译技术在国内的普及和发展。

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

（兼职实习的伙伴可以用【兼职】取代【学校】）

邮件正文请:
**进行跟应聘职位相关的自我介绍**，不超过300字。

邮件必须附带简历。**没有PDF格式简历的邮件不保证会收到回复**。
