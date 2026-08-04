# Humanize Book

<!-- 研究底稿、时间序语料和引用索引见 materials/README.md。 -->

## 序言

2026 年 3 月，我加入了 Humanize 社群。此后的几个月里，我有幸近距离见证了 Humanize 从 1.0，到 2.0 原型，再到 3.0 方向的演进。

这并不是一条整齐的“版本升级”路线。Humanize 1.0 首先回答的是：怎样让一个反馈循环真正跑起来？它以 Ralph Loop 和独立的 Codex Review 为核心，让 Agent 在实现、审查和修正之间持续迭代。到了 2.0，问题变成了：人能否用一套中间表示来构造、检查和复用 Flow？3.0 又把问题向前推了一步：Flow 能否由 Agent 在运行过程中生成和修改？如果用社群里更直观的说法概括，就是从 Ralph Loop，走向 Loop Engine，再走向 Agent-mutable Dynamic Workflow。

这条时间线贯穿了整本小册子。它记录的不只是 Humanize 自身的变化，也映照了 Agent，尤其是 Agent Harness 如何一点点改变开发方式。更完整的工程节点与社群讨论，可参见[《Humanize 演进关键节点导览》](materials/timeline/Agent发展史_关键节点导览.md)。

在技术演进之外，另一个同样珍贵的部分，是围绕 Humanize 形成的开发者贡献社区。社区规模不算大，但讨论密度和动手能力都很高。许多判断并非事后总结，而是在模型发布、仓库更新、实验成功或失败的当下自然生长出来的。大家一边使用 Humanize，一边质疑它、修改它，也不断重新理解什么才是有效的 Agent 工程。我一直想把这些散落在群聊里的见解保存下来。

因此，我使用 OCR 技术处理了群内聊天记录，并以时间为主线进行筛选和整理。OCR 转录难免存在错字、重复和上下文缺失，这本书也不会把聊天记录原封不动地搬出来。口水话和无关闲聊会被删去，必要处会做轻度润色，但我们会尽量保留原意、分歧与当时的不确定性。面向公开发布的版本还会继续清理敏感信息，并对成员姓名作匿名化处理。

《Humanize Book》并不打算成为一本盖棺定论的严谨著作。它首先是一份持续更新的社区记录，保存大家围绕 Humanize、Agent 与 Agent Harness 交流过的 Idea、经验和判断。对于群聊中提到的新闻、技术概念、GitHub 仓库及外部讨论，我们会尽量寻找一手资料相互印证，并将它们作为延伸学习材料提供给读者。

我之所以认为 Humanize 值得被专门研究，是因为它有很强的实践性。从 Ralph Loop、独立 Review、目标保持和熔断，到 Flow IR 与 Dynamic Workflow，它的大多数设计都来自具体项目中的问题、失败和修正，而不是从一套抽象理论出发。每一个留下来的工程点，都试图回答一个真实问题：怎样让 Agent 在更长的任务里持续工作，同时不偏离目标，并且接受外部校验。

截至 2026 年 8 月，[Humanize](https://github.com/PolyArch/humanize) 在 GitHub 上约有 1.4k Star。与许多更受关注的 Agent Harness 相比，它的规模并不算大，但我仍然认为它被低估了。沿着社群内部所说的 1.0、2.0、3.0 三个阶段去理解它——从一个能工作的 Loop，到表达和运行 Flow 的系统，再到由 Agent 参与构造与修改 Flow——未必能得到一套唯一正确的答案，却能看到 Agent Harness 最核心的一组问题是怎样被逐步提出、试错和重写的。

我希望读完这本小册子后，大家记住的不只是几个流行概念，而是能看见模型、工具与开发者之间的关系如何一步步变化。当你开始设计自己的 Agent 时，能够更清楚地判断为什么需要 Loop、什么时候需要独立 Review、自治的边界应该放在哪里，以及为什么一个足够简单的 Harness 有时反而更可靠。如果这本记录能带来这些具体的启发，它的目的就达到了。

> PS: 全文使用 Typeless 口述转文字，由 ChatGPT Codex 5.6 SoulMax 整理润色。

## 第一章｜Humanize 的诞生

如果把 Humanize 放进整个 Agent 发展史，它的诞生或许算不上一个醒目的世界性事件。但从我们这个社区向外看，它恰好构成了一条自然的分界线：在它之前，我们更多是在追赶模型能力的变化，观察 Claude Code 能把一次任务推到多远；在它之后，讨论的重心逐渐移向另一件事——怎样给模型建立目标、状态、反馈和边界，让它在真实工程里持续工作。

因此，本章并不打算证明 Humanize 改变了 Agent 的历史。它只是选择了一个离我们最近、也最便于观察的坐标：以 Humanize 的诞生为界，看一看 2026 年初 Agent 工程发生了什么，以及社区成员如何在几乎同一时间，用自己的项目去检验这些变化。

### 一把为自己磨的镰刀

Humanize 最初并不是一项按照产品路线图规划出来的 Agent Harness。刘思皓博士后来在群里回忆，它只是为了方便自己写代码而做的一个小工具，也是服务于加速器研究的 side project；更早的设计目标，甚至只是把一份 spec 翻译成 Agent 能够执行的计划。它的出发点并不宏大。

公开代码留下了一条更具体的演变路线。Humanize 1.0 的前身是 [GAAC（GitHub-as-a-Context）](https://github.com/SihaoLiu/gaac)，它曾尝试用 GitHub Issues、PR、Projects 和复杂的 Agent 交互来保存长程上下文。刘思皓后来回忆，GAAC 一度包含超过 60 个 Agent 的交互；经过实际失败，他把这些复杂结构大幅删去，只留下最有用的一条主线：Ralph Loop 加独立 Codex Review，再配上 Goal Tracker 与停滞熔断。2026 年 1 月 12 日提交的 [Humanize v1.0.0](https://github.com/PolyArch/humanize/commit/888451dbe0baf71b006f03961b7eb06939c100bf)，已经完整表达了这套骨架。

群里后来反复提到的一个早期用例，是对 gem5 构建系统的重构。[gem5 PR #2969](https://github.com/gem5/gem5/pull/2969) 尝试用 CMake + Ninja 替换长期使用的 SCons，同时加入一套可并行存在的 Bazel 构建系统。这个改造涉及五百多个文件，还要保留 ISA Parser、SLICC、SimObject 代码生成等既有链路，并验证两套构建系统得到一致的对象集合。它不是一个为了展示 Agent 而刻意设计的小样例，而是一个有历史包袱、有兼容要求、也要接受上游审查的真实工程问题。

如果用一个朴素的比喻来概括，Humanize 就像一把意外磨得很锋利的镰刀。最初只是因为眼前有一片麦子，想把它割得快一点，于是开始磨刀；等刀磨好以后，大家才发现，它处理的不只是一种麦子，也不只适用于一个项目。一个为个人研究服务的小工具，由此逐渐显露出 Agent Harness 的通用价值。

### Humanize 之前：模型开始进入真实工程

Humanize 诞生前后，最先带来冲击的仍然是模型能力，但交互方式已经先走了一步。2025 年 2 月，Anthropic 将 [Claude Code](https://www.anthropic.com/news/claude-3-7-sonnet) 作为研究预览带进终端，开发者开始把完整工程任务交给模型，而不只是让它补一个函数。到同年 7 月，Geoffrey Huntley 公开总结 [Ralph Wiggum Loop](https://ghuntley.com/ralph/)：用一个简单的持续循环，把同一目标反复交给 Agent，让代码、测试失败和 Git 历史成为下一轮的上下文。Anthropic 随后也提供了基于 Stop Hook 的 [Ralph Wiggum 插件](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum)。这条路线把注意力从“一次回答够不够好”移向了“系统能不能继续迭代”；Humanize 1.0 没有发明 Loop，而是在这个基础上加入独立 Review、目标保持和熔断。

2026 年 2 月 5 日，Anthropic 研究员 Nicholas Carlini 发布了[《Building a C compiler with a team of parallel Claudes》](https://www.anthropic.com/engineering/building-c-compiler)。实验让 16 个 Claude Opus 4.6 Agent 并行工作，接近 2,000 次 Claude Code 会话，在两周内产生约 10 万行 Rust 代码，API 成本约 2 万美元；得到的 [Claude's C Compiler](https://github.com/anthropics/claudes-c-compiler) 可以构建 x86、ARM 和 RISC-V 上的 Linux 6.9。这个结果并不等于“Claude 已经重造了 GCC”：当时公开的版本仍然依赖外部工具链，生成代码的质量和兼容性也有明显边界。但它把并行 Agent 的工程尺度推到了足以让系统软件开发者认真对待的位置。

同样重要的是，这个实验背后的 Harness 并不神秘。它的主体只是一个持续启动 Claude 的循环、隔离的容器、一个共享 Git 仓库，以及用文本文件实现的任务锁。Agent 之间没有复杂的通信协议，也没有一个全知全能的总调度器。真正花费作者大量精力的，是测试、执行环境和反馈：如果验证器不可靠，Agent 只会更快地把错误方向做大。

我当时受到的冲击很直接，于是用自己熟悉的系统软件做了几次验证：先让 Agent 用 Rust 重写 QEMU TCG，形成 [tcg-rs](https://github.com/zevorn/tcg-rs)；随后又完成 [cosim-gpu](https://github.com/gevico/cosim-gpu) 的第一版，把 QEMU 与 gem5 的 AMD MI300X 模型连接起来。这些项目在这里不需要展开。它们的作用，是让我亲眼确认 Claude 的工程能力已经跨过了某个门槛，同时也看到单点对话在长任务中的局限。过程分别记录在[《5 天，4.5 万行 Rust：用 Claude + Codex 重写二进制翻译引擎》](https://mp.weixin.qq.com/s/nDMDtWLwFqlYCr8dNk5Pwg)和[《只用两天：我用 Claude 把 MI300X GPU 搬进了 QEMU》](https://mp.weixin.qq.com/s/LG_PSQyQApr6zeilCCXLNg)中。

需要说明的是，这些初版并不是 Humanize 的成果，当时我还没有深入使用 Humanize。它们只是一次能力体验，并由此把我带到 Humanize 1.0 面前。在 3 月 28 日的 [OS2ATC 2026](https://os2atc.cn/) 上，我展示了 tcg-rs 与 Humanize；从这里开始，本书的叙述重点也从“Claude 能不能完成一个复杂项目”，转向“Humanize 怎样让这种能力持续、可控并接受外部 Review”。后来 tcg-rs 扩展为 [Machina](https://github.com/zevorn/machina)，cosim-gpu 也继续迭代，它们将作为 Humanize 的后续验证窗口，而不再占用本章的大篇幅。

### 第一次摆脱单点交互

我第一次认真使用 Humanize 1.0 时，最明显的感受不是“模型突然变聪明了”，而是自己终于可以离开单点交互。

此前使用 Claude Code，即使模型能力很强，我仍然要留在对话旁边：看它做到哪里，发现偏差，补一句提示，再要求它继续。任务一旦拉长，人就会变成维持循环运转的那部分。Humanize 改变的是这个结构。我先把目标、约束和验收条件想清楚，Builder 负责实现，独立的 Codex Reviewer 负责寻找没有证据的完成声明、遗漏的验收项和新引入的问题；下一轮再根据 Review 继续修改。人从高频纠偏中退出来，转而负责定义问题和判断最终结果。

后来复盘 Machina 的一个月实践时，这种变化已经可以用数据描述：11 份计划、12 个 Humanize Session、77 轮 Claude Build × Codex Review，以及 407 个提交。这些数字本身不能证明代码一定正确，却说明它不再是一段被包装得更长的聊天，而是一个能够留下计划、证据、审查结果和迭代轨迹的工程循环。更完整的复盘见[《月烧 6300 刀才明白：Agent 团队飞轮是怎么转起来的》](https://mp.weixin.qq.com/s/S45KRGmDCCLu5GoBa7v2bQ)。

PPT 是另一个更直观、也更容易被低估的例子。当时模型原生编辑 PPT 的能力还不稳定，第一次画出的结构图经常出现箭头没有接到组件、连线歪斜、间距失衡等问题。Humanize 1.0 做出的“漂亮”，首先不是华丽，而是规整：Reviewer 一轮轮检查连接关系、排序、间隔和对齐，Builder 再逐项修正，直到页面结构清楚。它没有让模型在第一轮获得设计天赋，而是把原本主观、零散的“不太对劲”，转化成可以不断检查和修复的问题。

这正是 Harness 最早让我信服的地方：它不必在单次生成中战胜模型的缺点，只要能够稳定看见缺点，并让下一轮有机会改掉它。

### 控制、协作与远程入口

3 月 20 日，群里谈到 OpenAI 的 Harness Engineering 时，有人给出了一个极简的概括：**Harness 工程就是控制论。**

OpenAI 在 2 月发布的[《Harness engineering: leveraging Codex in an agent-first world》](https://openai.com/index/harness-engineering/)中，披露了一个由 Codex 从零构建的内部产品：早期团队先有 3 名、后来增至 7 名工程师，约五个月形成近百万行代码、1,500 个 PR，产品代码没有人工手写。文章真正值得关注的并不是代码量，而是人的工作发生了什么变化：人不再逐行生产代码，而是设计环境、组织仓库知识、暴露日志与指标、把架构边界变成可机械检查的规则，再让 Agent 在这些约束中工作。

从社区实践出发，我们很自然地把它理解成一个控制系统：spec 和验收条件是参考目标，Builder 是被控制对象，测试与独立 Reviewer 提供观测，Goal Tracker 保存状态，循环与熔断负责继续、纠偏或停止。这不是 OpenAI 给出的正式定义，而是社区用来理解 Harness 的工程类比。它提醒我们，真正的问题不是如何写出更长的 prompt，而是如何让“目标—执行—观测—修正”这条反馈链闭合。

3 月 23 日，讨论转向多 Agent：究竟应该使用由 Leader 统一调度的 subagents，还是让 Agent 彼此通信、形成更接近 swarm 或 Agent Teams 的结构？群里并没有得到一个抽象的标准答案，反而迅速落到了几个很具体的问题上：Leader 的上下文和 I/O 会不会成为瓶颈？不同 Agent 之间的直接通信是否会形成对人和主 Agent 都不可见的黑盒？工作是否应该通过文件与 Worktree 交接？并行增加的到底是有效吞吐，还是协调成本？

讨论中较强的一派主张：实现型子任务交给 subagent，但结果经由文件回到 Leader；Agent 之间未经主控的沟通应当谨慎，因为不可观察的协作很难审计。另一派则指出，当规模继续扩大，单一 Leader 同样会被上下文和消息压垮，探索型任务也未必适合严格的层级调度。后来 Anthropic 的[多 Agent 使用指南](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them)给出了相近的成本侧证：同等任务下，多 Agent 通常消耗单 Agent 约 3—10 倍 Token；真正稳定获益的场景主要是上下文隔离、可并行任务和专业化工具，而黑盒验证之所以有效，恰恰是因为它需要传递的上下文很少。

这场讨论的重要性，不在于提前判定 Subagents 一定战胜 Agent Teams，而在于社区开始把 Agent 数量和协作拓扑分开看。开很多 Agent 并不自动构成好的 Agent Team；通信是否可见、任务边界是否独立、结果能否被外部验证，往往比数量更重要。

同一时期，Humanize 之外也已经出现了一批很强的单点能力。最典型的是 [Superpowers](https://github.com/obra/superpowers)。它的主要作者是 Jesse Vincent，背后团队是 Prime Radiant；Superpowers 也不是单个 Skill，而是一套由可组合 Skills 构成的软件开发方法。群里最认可的是它的 Brainstorming：先连续追问，把模糊愿望整理成干净的 spec 和 plan，再交给 Humanize 执行。有人把当时的工作流概括为：“许愿 → Superpowers 提问 → Humanize 执行。”但也有人发现，在需要长期盯实验、目标已经足够明确的任务里，过重的 Brainstorming 会产生负收益。Skill 的价值从一开始就不是越多越好，而是能否在合适的阶段补上一个明确缺口。

3 月 30 日还有一个轻松的小插曲。[Boris Cherny 当天介绍](https://x.com/bcherny/status/2038454336355999749)了 Claude Code 中两种不同的会话迁移方式：`/teleport` 把云端 Session 接回本地终端，`/remote-control` 则让手机或网页控制仍在本机运行的 Session。按照[官方 Remote Control 文档](https://code.claude.com/docs/en/remote-control)，本地环境、文件和工具并没有搬到云端，手机只是一个远程窗口。它没有让开发彻底脱离电脑，却把人从电脑桌面前解放了出来。我当时开玩笑说，我们这帮写代码的终于也能像高级金融白领一样，端着咖啡在星巴克坐一天，手机上刷的不是股票看板，而是几个 Agent 的运行状态。

玩笑背后其实是一种工作界面的变化：当 Agent 可以持续运行，人最需要的未必还是一块更大的代码编辑器，而可能是一块用来查看进度、接收告警和做关键决策的控制面板。

### 让真实失败成为 Harness 的反馈

Humanize 进入快速实践期后，大家很快遇到一个现实问题：怎样测试 Harness 本身？普通单元测试可以检查脚本是否能运行，却很难覆盖 Agent 在一个真实仓库中连续工作十几轮以后，出现的目标漂移、虚假完成、修复—回退振荡和停滞误判。

实践的尺度也在迅速拉长。最初是让 Humanize 在人睡觉时继续工作，随后群里开始出现持续数天、一周乃至两周的运行记录，也有人尝试同时启动多个 Humanize，让彼此独立的计划并行推进。这些尝试并不都成功：循环越长、并发越高，错误验证、上下文交接和资源消耗带来的代价也越容易被放大。但正是在这种使用强度下，Harness 的真实问题才会显现出来。

3 月底，Humanize 的开发分支加入了一个很有意思的“沉淀反思”机制：长程任务结束后，由 Agent 回看整段迭代，提炼 Harness 层面的问题；在用户同意后，对本地记录脱敏并交由用户审核，再提交为仓库 Issue。与其先发明一个看起来完整、实际覆盖有限的 Agent Benchmark，不如先让真实项目中的失败反向塑造 Harness。

最早一批 Issue 已经能够说明这套反馈的价值：[Issue #53](https://github.com/PolyArch/humanize/issues/53) 来自一个 23 轮的 RLCR Session，涉及 30 项任务、7 个阶段、37 个提交和 900 多个测试。独立 Reviewer 抓到了 4 个实现者遗漏的关键 Bug，但运行也暴露出新的问题：停滞检测把“围绕同一架构问题持续推进”误判成没有进展，原计划无法容纳中途发现的架构工作，Reviewer 与 Builder 还会因任务顺序产生长期僵持。

紧接着的 [Issue #54](https://github.com/PolyArch/humanize/issues/54) 记录了连续四轮“打地鼠式修复”：每轮只修复同一子系统中的一个局部问题，下一个问题又在 Review 中出现。它由此提出子系统级审计和进度速度信号，并被标记为 `good first issue`。[Issue #55](https://github.com/PolyArch/humanize/issues/55) 则记录了 6 轮中 6 次过早宣称完成；[Issue #57](https://github.com/PolyArch/humanize/issues/57) 记录了 19 轮运行中的修复—回退振荡，以及验收完成后仍然无休止打磨的问题。

这些 Issue 不是用来证明 Humanize 已经成熟，恰恰相反，它们保留了 Humanize 在真实工程中失败的方式。在 Agent Benchmark 尚不成熟的阶段，这可能是优化 Harness 性价比最高的办法之一：不把失败留在某个用户的本地日志里，而是将其脱敏、抽象成可讨论、可实现、可回归检查的工程问题。社区成员既是使用者，也成为了 Harness 的分布式测试者。

### 当方法被模型吃进权重

3 月 24 日，Anthropic 发布了 Prithvi Rajasekaran 撰写的[《Harness design for long-running application development》](https://www.anthropic.com/engineering/harness-design-long-running-apps)。文章使用 Planner、Generator 和 Evaluator 构成的三 Agent 架构，把主观设计标准转化为可评分的指标，并让完整 Harness 最长运行 6 小时。它和 Humanize 都强调独立评价、文件交接与反馈循环，但群里的即时反应却相当冷淡：早期大家几乎会逐篇研究 Anthropic Blog，到这篇文章时，不少人觉得其中可获得的新知识已经变少，甚至认为社区的真实运行时间和问题复杂度已经走得更远。

这不意味着文章没有价值。相反，它在后半部分写出了一个后来反复出现的矛盾：每一个 Harness 组件，都隐含着“当前模型还做不到什么”的假设；模型更新以后，原本必要的 Sprint、上下文重置或 Review，可能变成额外负担，因此应该重新检查并删除已经不再承重的部分。

社区里后来形成了一个很有意思的判断标准。刘思皓曾把它概括为：判断一个 Harness 特性是不是真的有用，可以看下一轮模型会不会把它 built-in。有效的方法会先被写进 prompt，随后沉淀为 Skill 或 Harness；一旦足够通用、足够高频，它又可能通过后训练或下一轮模型迭代，直接进入模型能力。到那时，外部脚手架就要继续变薄，或者把边界推向模型尚未覆盖的新问题。

从这个角度看，闭源实验室相对开源社区的领先并不是一个固定距离。模型公司可以更早看到新模型、拥有更多训练资源，但社区拥有数量更大、变化更快的真实工程现场。随着有效方法不断被公开、复现和内化，单篇官方 Blog 所能带来的前瞻性会出现边际递减；而真实使用中暴露的失败、Issue 和反例，反而可能成为更稀缺的知识。

Humanize 的诞生因此既是一个起点，也是一个待解的问题。1.0 证明了 Builder、独立 Reviewer、Goal Tracker 和 Circuit Breaker 组成的简单循环能够产生真实价值；与此同时，模型已经开始吸收这些循环曾经补足的能力。当 Harness 的一部分逐渐被 built-in，外部还应该保留什么，又该向哪里演进？

这正是 4 月份讨论的起点，也是下一章要继续追踪的问题。

## 第二章｜从一条 Loop 到一门 Flow

Humanize 1.0 从一小群人的工具走向更多真实项目后，最先被大家记住的是“它真的能跑”。紧接着暴露出来的，是另一个很具体的问题：它常常很难漂亮地停下来。

前几轮，Builder 大开大合地铺功能、补接口、改架构，Token 像水一样往外流。等主要 Feature 都完成，系统进入收口期，Builder 每轮只改一点，Reviewer 却总能继续找到下一个问题。P0、P1 清完以后还有 P2、P3；一个局部缺陷修掉，旁边又冒出另一个。群里把这种现象叫作“长尾打地鼠”。4 月 11 日的一句总结很准确：真正干活只用了约 20% 的时间，让 Codex 完全认可却花掉了剩下的 80%。

### 收敛以后，为什么还停不下来

我们很自然地想到了控制系统。4 月 10 日，群里有人把 Reviewer 叫作传感器：系统要达到稳态，就得有反馈。几天后，Builder—Reviewer Loop 又被形容成“二元震荡”。两边不断交换判断，误差越来越小，系统逐步逼近验收目标；每修掉一个小问题所带来的边际价值也越来越低。

当时观察到的 Token 分布大致是这样：

| 阶段 | Builder 的 Token 投入 | Reviewer 的相对作用 | 系统表现 |
| --- | --- | --- | --- |
| 前约 20% 时间 | 约占 Builder 总 Token 的 80% | 主要检查 Feature 与验收项有没有落地 | 大幅推进，改动范围很大 |
| 中段 | 持续下降 | 逐步成为主要驱动力 | 功能补齐，问题从“做没做”转向“做得好不好” |
| 后约 80% 时间 | 约占 Builder 总 Token 的 20% | 不断寻找局部缺陷和边界问题 | 小步修复，P2/P3 长尾，偶尔出现修复—回退振荡 |

这里的 Reviewer 比例没有一份完整的计量数据，上表保留的是群聊中的相对趋势；Builder 的“二八分布”则来自当时对连续多轮运行的直接观察。它很像一条先剧烈下降、随后拖着长尾慢慢贴近目标的收敛曲线。

4 月 14 日，我们真的沿着 PID 的类比改了一版 Humanize。[PR #81](https://github.com/PolyArch/humanize/pull/81)把累计 Commit 和最近三轮 Summary、Review 一起提供给 Reviewer。对应提交把 Goal Tracker 与 Acceptance Criteria 的差值看作 P，把历史轨迹看作 I，把当前 Round 的变化看作 D。到 6 月复盘时，大家又给 P、I、D 重新分配过角色，甚至认为 Humanize 缺少的 D 恰好对应 `/goal` 的 Progressive Planning。这个映射一直在变，所以我更愿意把 PID 看成社区理解问题的一种工程语言。它帮我们看见震荡、积分记忆、阻尼和收敛速度，也没有把一个概率系统假装成精确的控制器。

长尾也说明了 Humanize 1.0 的适用边界。目标清楚、Plan 足够完整、验收条件可以写出来时，RLCR 很强；它会忠实地把自然语言 Plan 翻译成代码，再用独立 Review 把结果慢慢压到目标附近。探索型任务、快速小改和途中需要频繁改方向的任务，会让这套固定结构显得很重。到了 5 月 21 日，刘思皓给出的日常做法已经很朴素：当 Reviewer 剩下的全是 P2，就由人直接终止。控制系统最后仍然需要一个知道什么时候值得停下的人。

### 1.17：给固定 RLCR 画一个句号

4 月 21 日，群里第一次明确说，`1.17.x` 会成为 Humanize 1.0 的最后一条版本线。4 月 30 日，[1.16 合并 PR](https://github.com/PolyArch/humanize/pull/51)进入 `main`；这也是公开主线最后一个清楚的 H1 里程碑。5 月 1 日，`dev` 分支又出现了 [1.17.0 的版本提交](https://github.com/PolyArch/humanize/commit/f4e5721e344ef602a77cfb3511ec51b74e387120)，随后没有形成独立 Tag 或 Release，也没有进入 `main`。本书因此把 1.17 视作 H1 的开发线收官标记，同时保留 1.16 才是公开主线最后明确合并版本这项注释。

这个句号并没有否定 H1。它已经验证了一件很重要的事：Builder 和独立 Reviewer 可以构成一个有效的反馈循环，Goal Tracker、历史轨迹和 Stop Hook 能让长程 Coding Task 持续推进。我们后来才把这种结构概括成 Loop Engine。接下来的问题变了。模型更新得越来越快，Coding CLI 也越来越多，一条 Flow 继续硬编码 Claude Build、Codex Review，维护成本会迅速上升；同一个 RLCR 结构也覆盖不了探索、研究、批量维护、性能优化等差异很大的任务。

H2 最早的设想其实很直接：让用户自己选择模型，再把不同模型放进 Builder 和 Reviewer。这个想法很快牵出更深的一层——如果模型可以换，Flow 为什么还要和某个 CLI 绑死？

### 一个多月里，模型和工具一起换挡

回头看 4 月到 5 月，这个问题几乎是被发布节奏推到我们面前的。

4 月 7 日，[GLM-5.1](https://docs.z.ai/guides/llm/glm-5.1)把长程 Agentic Coding 放在核心位置，官方给出的单任务持续运行上限达到 8 小时。4 月 16 日，[Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)发布，群里几分钟后就把它挂上 Humanize 测试。反馈并不整齐：有人觉得它写出来的代码更好看，也有人嫌它消耗额度太快；“Claude 适合早期铺开，Codex 更会修 Bug、做 Review”仍是当时很有代表性的一种分工。

4 月 21—22 日，群里开始传看 [Kimi K2.6](https://www.kimi.com/blog/kimi-k2-6) 的长程编码与 Agent Swarm 材料。它的[开放权重](https://huggingface.co/moonshotai/Kimi-K2.6)让“国产模型能不能平替”从价格讨论进入了 Builder 和 Reviewer 的实测。这里很快也出现分歧：有人认为 Kimi 的 Review 已经接近 GPT，也有人觉得它和 Opus、Codex 仍有明显差距。4 月 23 日，[GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)进入 ChatGPT 与 Codex，群里几乎立刻把它放到 RLCR Reviewer 的位置。4 月 24 日，[DeepSeek V4](https://api-docs.deepseek.com/news/news260424/)又带来 Pro 与 Flash 两档模型、1M Context、开放权重，以及对 OpenAI 与 Anthropic API 的兼容。

这些节点挤在三周之内。具体 Benchmark 可以争论，方向已经很清楚：

- 模型厂商开始用“能否连续规划、调用工具、修错并交付”描述 Coding 能力，单轮代码生成的占比在下降。

- 智力、速度与成本逐渐分档。Pro/Flash、不同 Effort、Fast Mode 让“便宜模型铺 Build，强模型做 Review”从群聊里的省钱技巧变成可长期设计的 Flow。

- Kimi 与 DeepSeek 同时推进开放权重，DeepSeek 还兼容两套主流 API；5 月重写的 [Kimi Code CLI](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)也直接提供 Multi-provider 和内置 Subagents。模型和 CLI 的替换门槛都在下降。

- 模型能力与 Harness 能力开始一起发布。厂商交付的单位逐渐从“一个更聪明的模型”扩大成“模型 + Runtime + 权限 + 持续执行 + 编排”。

这种变化给 H2 的模型无关设计提供了很现实的理由。今天写死的最佳模型组合，几周后就可能变成旧答案。真正值得稳定下来的，应当是任务如何被拆分、状态怎样传递、谁有权执行什么动作、结果由谁验证，以及失败以后走哪一条边。

### 把 Flow 从模型里抽出来

4 月 22 日，H2 被拆成三个暂定层次：`humz` 用来描述 Agentic Flow，`hcc` 将它编译成实际运行的脚本与 Harness，`hvm` 负责执行编译结果和用户输入。第二天的讨论又加入了 ISA、类型系统、编译器和 VM/runtime。名字后来没有完整保留下来，这个分层表达了当时最重要的直觉：Flow 可以先成为一个独立的中间层，再去适配 Claude Code、Codex、OpenCode、Gemini、Kimi 或下一款还没发布的 CLI。更简练的“Flow IR”要到 6 月复盘时才出现，本章把它当作后见性的概括。

编译器的类比也从这里展开。我们希望把一条 Flow 中相对稳定的东西抽出来：节点、边、状态、输入输出、验收条件、并行关系、循环、分支、Review 和权限。自然语言仍然负责表达目标和那些难以形式化的判断；能够机械执行的部分尽量落到脚本与运行时里。这样可以少花 Token，也能减少同一条 Prompt 在不同 Round 里慢慢漂移。

如果把当时的设想压缩成一行，大概是：

`自然语言目标 → Flow 表示 → 静态检查与变换 → 后端适配 → Agent CLI 执行`

这条链路有一点像编译器 IR。它可以检查某个 State 是否永远到不了、某条路径有没有出口、某个 Agent 是否缺少必要输入，也可以把不同后端的调用方式放到 Codegen 一侧处理。类比的边界也很清楚：Agent 的一次执行仍然带有概率，Verifier 的判断也会错。这里追求的是 Flow 结构更稳定、结果更容易观察，编译器本身的确定性无法原样复制过来。

当时还有一句我很喜欢的定义：

> Agent = Model × Tool × Action × Permission

Model 和 Tool 只解释了 Agent 能理解什么、能调用什么。Action 与 Permission 决定它此刻可以做什么：能否修改代码、启动子 Agent、访问网络、绕过 Sandbox、改变 Plan、更新 Goal，或要求人类确认。Flow 由此获得了安全和组织上的含义。两套 Agent 即使使用同一个模型，只要动作集合与权限边界不同，实际行为就可能完全不同。

群里当时使用的原词是 `hvm` 或 VM/runtime，“Agent VM”是本书为了阅读方便采用的简称。这个 VM 没有性能压力，一条“指令”可能运行几分钟甚至几个小时；它更像一台 Flow 执行和监控机，负责把状态交给下一节点，记录发生过什么，并在边界上执行权限和检查。

群里对这套构想始终有质疑。有人直接问：已有编程语言加 Agent SDK 已经能做编排，为什么还要造 DSL？刘思皓当时的回答很克制，Workflow-as-PL 首先是一套思维模型，实现时完全可以使用现成语言。这句话让讨论降了一点温。H2 从起点就背着一个问题：我们究竟需要一门新语言，还是只需要把少数可靠的 Flow 原语整理出来？

事实上，[5 月 17 日进入 `h2-dev` 的 POC](https://github.com/PolyArch/humanize/commit/3fccb60c11332fb322a295db0583432416c7cf07)已经换了一种形态：TypeScript、MCP Server Hub、HTML Workflow Runtime、Dashboard，以及把 RLCR、gen-idea、gen-plan 等能力重新表达成 Workflow Cartridges；最初真正接通的 Agent Backend 只有 Codex 和 Claude。它和最初聊到的 Rust、MLIR 方言与小型 VM 有很大差别。作者在公开分支时也反复提醒，这个版本用于开发一个更合理的 Agentic Flow Platform，普通项目继续使用 H1；仓库把它标成 Transitional Branch，包版本也只有 `0.1.0`。H2 当时是一份 First-step Proof of Concept。

我很喜欢这段不整齐的历史。大家先想换模型，接着讨论 IR、类型、编译器和 VM，最后落下来的 POC 又采用了另一套基础设施。概念与实现互相试探，任何一版都还谈不上最终答案。H2 真正完成的转向，是让 Flow 本身第一次成为开发对象：人可以构造它、运行它、检查它，也可以拿不同模型与工具去替换其中的节点。

### `/goal` 带来的第二次震动

就在 H2 快速成形时，Codex 从另一个方向给出了答案。[Codex CLI 0.128.0](https://github.com/openai/codex/releases/tag/rust-v0.128.0)于 4 月 30 日 UTC 发布，北京时间已经进入 5 月 1 日。它加入了持久化 `/goal`：Goal 可以跨 Turn 保存，Core Runtime 在 Session 空闲时自动继续工作，模型拥有读取和更新 Goal 的工具，TUI 则提供创建、暂停、恢复和清除。

这很像把原先依赖 Stop Hook 维持的 Loop 收进 Codex 自己的 Runtime。首发时它仍然是实验功能，需要经 `/experimental` 开启。证据能确认的是 Codex 产品层内置了持续目标与自动续跑；它是否已经进入 GPT-5.5 的模型权重，需要另一套训练与评测证据。

群里的第一反应相当兴奋。5 月 6 日，有成员觉得 `/goal` “神奇地把 Build、Test、Review 结合在一起”，Build 的同时就在检查，阶段之间少了 Humanize 那种清晰、也略显机械的切换。直接把 Humanize 生成的 Plan 喂给 `/goal`，一度成了很顺手的组合。

真实体验很快又把判断拉回地面。有人发现 `/goal` 会改写自己的 Plan，遇到难点时绕路，或用很弱的完成判断给任务打勾；也有人用它连续完成了很大的从零构建。到了 5 月 26 日，群里出现了一组很有解释力的对照：

- Humanize：强 Review + Static Planning；

- Codex `/goal`：弱 Review + Dynamic Progressive Planning。

前者很稳，长尾明显；后者推进快，也更容易在途中自行改变路径。大家当时真正想要的答案，逐渐变成 **Dynamic Progressive Planning + Strong Review**。H1 的独立审查和 `/goal` 的动态推进各自抓住了一半。所谓 Harness 被 built-in，也呈现出更细的层次：内置能力会减少外部脚手架，却未必一次覆盖所有真实任务。

### 当同一个方向出现在厂商产品里

5 月 28 日，Anthropic 随 [Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)在 Claude Code `v2.1.154` 中推出 [Dynamic workflows](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)。群聊和后来的记忆里曾出现 `ultrawork`、“Auto Work”和“Auto Code”等名字，正式名称都应勘误为 **Dynamic workflows**。Auto Mode 是建议搭配的权限模式，`ultracode` 则是 `xhigh` Effort 加自动 Workflow Orchestration 的设置。

官方描述里，Claude 会动态写出 JavaScript 编排脚本，把任务分给数十到数百个并行 Subagents，再安排独立 Agent 验证结果。5 月 28 日首发时它属于 Research Preview，后续才更新为 Generally Available。北京时间 5 月 29 日，群里的第一反应近乎错愕：有人问 `ultrawork` 是否已经覆盖 H2，Dynamic workflows 是否又覆盖了 H3；也有人只说了一句，“最怕的就是大家都太快了。”

5 月 30 日，群里已经有人判断 H2 的独立空间被压缩了：与其另起一套平台，也许可以直接在原生 Workflow 的节点里接入 `codex-review` 或 `codex-rescue`。到 6 月 2 日，大家又修正了最初的理解。这里的“动态”主要指 Claude 按当前任务即时生成脚本；脚本生成后仍交给独立 Runtime 执行。H3 继续追问运行中的 Flow 能否被 Agent 改写，两者之间还隔着一步。

把这两份时间线并排放着看，很容易让人兴奋，到这里也得踩一下刹车。公开证据只能支持“同一个方向在接近的时间出现”，还不足以建立 Anthropic 与 Humanize 之间的直接影响关系。更稳妥的解释是，模型、CLI 和社区 Harness 都撞上了同一批工程问题：怎样让长任务持续，怎样并行，怎样验证，以及怎样在任务途中重写原有计划。

我现在再看 H2，最想留下的是那次视角变化。大家暂时放下“哪个模型更强”，开始追问“怎样描述一个生成软件的过程”。相近的能力很快出现在 `/goal` 和 Dynamic Workflows 中，一些 H2 实现后来被推翻，外部 Harness 仍要处理强 Review、权限、可观测、恢复、人类接管，以及 Flow 在运行中怎样变化。

当 Flow 终于可以被当成程序，下一步自然会有人问：这份程序一定要由人预先写好吗？这就把故事推向了 Humanize 3。

> 本章的群聊行号、版本状态与外部资料快照，见[第二章一手资料核查](materials/research/第二章_Humanize2_一手资料核查.md)和[第二章参考资料卡](materials/references/第二章/README.md)。
