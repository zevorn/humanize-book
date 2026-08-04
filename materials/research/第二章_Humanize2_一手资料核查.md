# 第二章：Humanize 1.0 → 2.0 一手资料核查

> 核查范围：2026 年 4 月 10 日至 5 月 30 日的 Humanize 群聊、`PolyArch/humanize` 仓库，以及同期 Anthropic、OpenAI、Moonshot AI、OpenClaw 的官方公告或官方仓库。6 月材料只用于辨认后来形成的术语，不倒写成 4—5 月已经确定的设计。
>
> 这是一份供第二章写作使用的史料底稿，不是替代群聊的完整摘要。文中的“群内判断”只代表当时参与者的观察，不等于厂商或项目的正式结论。

## 一、先给结论：第二章可以成立的主线

Humanize 2.0 的起点，不是“再做一个更强的 RLCR”，而是对 Humanize 1.0 的两类问题同时作出回应：

1. **固定 Builder–Reviewer 循环已经证明有效，但出现了明显的长尾、震荡和上下文成本。** 群内先用“打地鼠”“二八定律”描述经验，随后借用反馈控制和 PID 语言解释循环为什么不易收敛。
2. **不同模型、CLI 和 Agent 工具快速更替，使硬编码 Claude Builder、Codex Reviewer 的实现越来越脆弱。** 因此 2.0 逐步被设想成模型可配置、CLI 可替换、机械部分脚本化的通用工作流执行层。
3. **H2 的设计语言在一周内迅速升级。** 4 月 20 日还是“删减、重写、压缩上下文”；4 月 22 日形成 `humz / hcc / hvm` 三层设想；4 月 23 日进一步用 ISA、编译器、类型系统、VM/runtime 来理解 Agent flow。
4. **5 月出现的 Codex `/goal` 改写了问题。** `/goal` 原生提供目标持久化和跨 turn 续跑，群内很快发现它比 H1 的重型循环更适合长程定向实现；Humanize 的价值开始收缩到 plan、独立 Review、历史记忆和渐进式对齐。
5. **5 月 28 日 Anthropic 正式推出 Dynamic workflows，再次改变了 H2 的位置。** 它把“模型生成 JavaScript 编排脚本、并行调度 subagents、在对话外保存协调状态”做进 Claude Code。群内很快从“这像 H3”修正为“它更像 H2 的静态工作流”；到 5 月 30 日，已经有人明确判断 H2 的独立存在空间被压缩。

这条主线不是单一因果链。更忠实的写法是：**H1 的实际痛点、H2 的抽象冲动、模型与 harness 的快速进步三股力量，在 4—5 月同时发生并相互校正。**

## 二、按日期还原：从 H1 的反馈问题到 H2 的平台化

### 2026-04-10—04-16：从“长尾打地鼠”到控制论隐喻

#### 4 月 10 日：Reviewer 被看作传感器

群内在讨论 Plan Mode、Review Mode 和 Auto Mode 时，第一次明确把 Reviewer 类比为控制系统里的传感器：

> “其实你把 reviewer 当做传感器往工程控制论里套，这个就是很自然的事情。”
>
> “系统达到稳态必须要有反馈。”
>
> “我最近真的在想怎么套 PID……让 loop 收敛得更快。”

史料位置：[聊天记录 7528—7548 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:7528)

此时 PID 还是讨论中的类比，不是 Humanize 已经实现的控制器，也没有稳定的 P/I/D 对应关系。

#### 4 月 11 日：长尾问题被量化成 20/80

群内把 H1 的主要方法学问题概括为“长尾打地鼠”：真正完成任务大约只占 20% 的时间，而修到 Codex 完全认可可能占 80%；每一轮修复又会暴露新的小问题。与此同时，异质模型既能带来不同视角，也会把“理解差异”误判成代码错误。

史料位置：[聊天记录 7617—7659 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:7617)

这段讨论是后来“便宜 Builder、昂贵 Reviewer”“多轮 Build、一轮 Review”“P2 即停”等策略的经验起点。

#### 4 月 14 日：B–R 二元震荡与 token 长尾

群内进一步提出：

> “RLCR 本身就是一个混沌动力学系统。”
>
> “B-R Loop 有点二元震荡的味道……单纯给 B-R 上 loop 是不对的，很容易局部震荡。”

同时有人提出让 Reviewer 查看前几轮 commit 和 Review 结果，为系统增加历史负反馈；另一个可复用的观察是：

> “前 20% 的时间 builder 花 80% 的 token；后 80% 的时间，builder 花 20% 的 token。”

史料位置：[聊天记录 8238—8317 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:8238)

这里还有一句需要谨慎处理的判断：“现在 RLCR 只有 P、D，没有 I；P 是 goal tracker，D 是 summary vs prompt”。这只是当日即兴映射。6 月 13 日的回顾又把 Goal Tracker 解释成 I、Codex Review 解释成 P，并称 H1 缺 D。两套映射相互矛盾，说明 PID 在群内是持续演化的思考工具，而不是正式规格。

#### 4 月 16 日：PID 被扩展成交易隐喻

群内有人把 Humanize 形容成“中频的 PID 套利算法”，在 Builder 和 Reviewer 之间抽取生产力，并顺势提出把量化交易的思路迁移到 harness flow。这个比喻很生动，但更适合做章节旁注，不宜当作技术定义。

史料位置：[聊天记录 8753—8764 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:8753)

同一天，Anthropic 正式发布 [Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)。群内几分钟内转发官方链接，并立刻把新模型挂上 Humanize 测试。第二天的反馈并不一致：有人认为它更少“流口水”，但离早期 Opus 高峰仍远；有人观察到它耗掉大量额度；也有人继续认为 Codex 更擅长修 bug，Claude 更适合早期铺开 MVP。

史料位置：[聊天记录 9019—9027 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9019)、[9511—9558 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9511)、[9905—9927 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9905)

### 2026-04-20—04-23：H2 从“删减重写”变成工作流语言

#### 4 月 20 日：简单性成为第一原则

讨论另一个多 Agent 编排项目时，H1 被反思为已经开始“功能冗杂”。群内列出的同类系统共同特征包括 Ralph、multi-model review、brainstorming、team/parallel 和持久化 bitter lesson。H2 最初的方向不是继续叠功能，而是：

- 让 flow 足够简单；
- 把可以机械执行的环节交给脚本；
- 尽量不占模型上下文；
- 把 Humanize 的上下文占用从超过 5% 的风险区压到约 1%；
- 彻底重写，而不是继续在 H1 上堆 ad hoc 补丁。

原话中甚至估计“本质的 Humanize flow 可能 1000 行以内代码就够了”。

史料位置：[聊天记录 11487—11524 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11487)

同日，社区也提出“轻量级 Humanize”：去掉逐级 Reviewer，只在结束时 Review，以降低启动和执行延迟。反方担心集中式 Review 会造成更大的震荡、隐藏问题，类似拿走 PID 调参过程只保留一次输出。

史料位置：[聊天记录 12127—12148 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12127)

#### 4 月 21—22 日：H1 的终点被提出，H2 转向模型无关

4 月 21 日群内明确说：

> “1.17.x 会是 Humanize 1.0 的最后一个版本。”
>
> “2.0 的 Humanize 就不绑定模型了，允许用户选择各类模型。”

史料位置：[聊天记录 12938—12959 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12938)

第二天对 Humanize 的定位也发生收缩：它不是一次性自动造物，而是通过多次失败帮助人打磨路径；理想状态下，plan 写完时设计已经完成，Humanize 只做“忠实的自然语言到编程语言的翻译器”。同一段里，H1 被称为进入“生命末期”，H2 被设想为彻底重写。

史料位置：[聊天记录 13162—13219 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13162)

这一天形成了 H2 最清晰的早期三层设想：

1. `humz`：描述 agentic flow 的“编程语言”；
2. `hcc`：把 flow 编译成实际 harness 的编译器，输出类似 Stop Hook 的脚本；
3. `hvm`：把编译结果与用户输入一起执行的 VM。

同时做出两个重要边界：远端 spawn、集群和沙盒属于 HVM 的基础设施能力，不等同于 flow 方法本身；机械功能应交给脚本，只有需要智力的部分才调用 LLM。

史料位置：[聊天记录 13249—13307 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13249)

群内在这里推荐了 [OpenClaw/acpx](https://github.com/openclaw/acpx)，理由是它通过 Agent Client Protocol 为多种 coding agent 提供结构化兼容层，也比 PTY/Hook 拼接更容易观察中间状态。需要注意：**H2 仓库后来没有把 `acpx` 加为依赖，而是自己实现了 Codex/Claude backend。** 因此 `acpx` 是同期参照物，不是已采用的底层组件。

#### 4 月 23 日：ISA、类型系统、VM/runtime

4 月 23 日的讨论把前一天的三层结构继续抽象：

> `codebase = variable`
>
> `context = hidden-value`
>
> `prompt = predicate`
>
> `state = control-tag`
>
> `Agent = Model x Tool x Action x Permission`

随后把 Agent 称为“指令系统”，把这些约束称为“类型系统”。

史料位置：[聊天记录 14145—14159 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14145)

接下来的关键原话包括：

- agentic workflow 不是自然语言 Markdown，而是一套“编译器基础设施”；
- 程序员从“写代码描述程序功能”转向“写代码描述一个程序被生成出来的过程”，即 `meta code`；
- “LLM is the new processor/interpreter; Agent flow is the new code”；
- flow 可能只需要约十种指令，却能描述大量 workflow；
- 它不是 prompt/skill 编程语言，而是 workflow 编程语言；
- 形式化检查的目标是减少 flow 的腐烂、漂移和体积膨胀。

史料位置：[聊天记录 14162—14205 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14162)

H2 的原始动机也在当天被明确说明：先想给 Humanize 建 CI/benchmark，再想到从全量 flow 中抽取共性操作做 microbench；共性操作进一步成为 flow ISA；有了 ISA，问题自然被理解成 PL 问题。

对于 runtime，原话更克制：它是当前 flow 的“执行跟踪机器”，不需要高性能，因为每个操作本身要运行数分钟或数小时；它主要负责机械执行、监控和输出审计。讨论还明确说 `workflow as PL` 只是思维模型，实际实现会选择最快、最稳定的方式，不会为了类比而强行复用 LLVM/MLIR。

史料位置：[聊天记录 14228—14317 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14228)

### 2026-04-24—04-30：模型跃迁与 H1 正式主线的终点

#### 4 月 23/24 日：GPT-5.5 进入 Codex

OpenAI 于 4 月 23 日发布 [GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)，并在 4 月 24 日更新 API 可用性。官方把提升重点放在 agentic coding、computer use、跨工具持续执行以及更少 token 完成任务。

北京时间 4 月 24 日凌晨，群内开始试用，第一反应不是 benchmark，而是“说人话了一些”“不知道和 Humanize 配合起来怎么样”。当天晚些时候，讨论迅速落到更现实的分工：把 GPT-5.5 设为 RLCR Reviewer、比较其 debug/review 深度，并继续观察它与 Opus 的角色差异。

史料位置：[聊天记录 14480—14500 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14480)、[14769—14852 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14769)

这里值得保留的历史观察是：新模型并没有立刻让 harness 消失，反而马上被嵌入 Humanize 的角色系统中，重新定义 Builder 与 Reviewer 的模型选择。

#### 4 月 21—24 日：Kimi K2.6 与国产开源模型冲击

群内在 4 月 21—22 日开始转发 Kimi K2.6 的“300 个 Agent、4000 步”材料，第一反应是“看起来可以成为平替”。Moonshot AI 的[官方技术页](https://www.kimi.com/blog/kimi-k2-6)确认 K2.6 是开源模型，重点包括长程编码、Agent Swarm、最多 300 个 subagents 和约 4000 个协调步骤；[官方 Hugging Face 模型仓库](https://huggingface.co/moonshotai/Kimi-K2.6)也构成开源实物证据。

史料位置：[聊天记录 12832—12848 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12832)、[13229—13239 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13229)

需要保留一个证据边界：Kimi 当前官方技术页没有展示文章发布日期，Hugging Face API 只显示模型仓库于 4 月 14 日创建，不能据此确定公开发布的精确小时。因此正文宜写“4 月 21—22 日群内开始传播和试用”，不要把某个媒体发布时间直接写成官方首发时刻。

到 5 月 16 日，社区对国产模型的评价已经分化：有人认为 Kimi Review 接近 GPT，有人认为 Kimi/GLM 仍明显弱于 Opus；相对稳定的共识仍是 Codex Review 独一档。史料位置：[聊天记录 21714—21780 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21714)

#### 4 月 27 日：H2 的“流程图 + 自然语言”表达与第一轮质疑

群内提出未来可能只剩两种编程语言：“流程图”和“自然语言”。H2 的卖点被归纳为：容易构建各种 flow、容易换模型、HCC 能在运行前静态检查结构缺陷。立即有人提出反对意见：这种路线是否让 Humanize “less sexy”，因为工作流 Agent 系统两年前就已经很多。

史料位置：[聊天记录 15587—15625 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:15587)

这段异议应保留。它说明 H2 从一开始就存在一个尚未解决的问题：**它的独特性究竟是“有一个工作流系统”，还是“找到 Agent flow 的最小原语、验证方法和可演化载体”。**

#### 4 月 30 日：H1 的正式主线停在 1.16，不是 1.17 Release

群内当晚宣布 [PR #51](https://github.com/PolyArch/humanize/pull/51) 合并，并称“Humanize 1.16 正式合并了”。对应 `main` 的 merge commit 是 [`0ec921a`](https://github.com/PolyArch/humanize/commit/0ec921a36b4365df503511c5567bbd3e02db0df5)，提交时间为 2026-04-30 08:11 PDT。

史料位置：[聊天记录 16970—16982 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16970)

版本核查的准确结论是：

- 4 月 21 日，“1.17.x 会是 H1 最后版本”是**路线声明**；
- 5 月 1 日，`dev` 分支出现 [`f4e5721`](https://github.com/PolyArch/humanize/commit/f4e5721e344ef602a77cfb3511ec51b74e387120)，把插件版本号升到 `1.17.0`；
- 但仓库没有任何公开 [GitHub Releases](https://github.com/PolyArch/humanize/releases) 或 [tags](https://github.com/PolyArch/humanize/tags)，`1.17.0` 也没有合入 `main`；
- 因而不能写“Humanize 1.17 于 5 月 1 日正式发布”。更严谨的表述是：**1.17.x 被规划为 H1 最后一条版本线，并在开发分支落地；公开默认主线的最后一个明确合并里程碑是 1.16。**

### 2026-04-30—05-16：`/goal` 出现，H2 从想法落成过渡分支

#### 4 月 30 日 / 5 月 1 日：Codex `/goal` 首发与群内首次出现

OpenAI 在 Codex CLI [0.128.0 Release](https://github.com/openai/codex/releases/tag/rust-v0.128.0) 中首次把持久化 `/goal` 列为 New Feature。GitHub 显示发布时间为 4 月 30 日 16:40 UTC，即北京时间 5 月 1 日 00:40。Goal 的五段式实现 PR 从 4 月 16 日开始公开，TUI PR [#18077](https://github.com/openai/codex/pull/18077) 于 4 月 25 日合并。

5 月 1 日 13:39，群内第一次转发 `/goal`：先在 `/experimental` 中开启 Goals，再用 `/goal` 设定目标；转发文字把它描述成“keep a goal alive across turns”。

史料位置：[聊天记录 17231—17246 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17231)

初版 `/goal` 的官方边界是：

- 将长期目标持久化到当前 thread；
- 在 turn 结束、session 空闲时自动决定是否继续；
- 支持创建/替换、查看、暂停、恢复、清除；
- 状态包括 active、paused、budget-limited、complete；
- 人类输入和 mailbox 优先，某次续跑没有调用工具时会抑制继续空转；
- token budget 是 soft stop；初版 slash command 不公开预算参数；
- 模型不能把普通任务擅自升级成 goal，`create_goal` 只应在用户明确要求时调用。

官方实现证据：[持久化基础 #18073](https://github.com/openai/codex/pull/18073)、[模型工具 #18075](https://github.com/openai/codex/pull/18075)、[运行时 #18076](https://github.com/openai/codex/pull/18076)、[TUI #18077](https://github.com/openai/codex/pull/18077)。

因此，`/goal` 可以被解释为 Codex 对 Ralph Loop 的一种原生化，但不能直接等同于 Humanize：它初版没有独立 Reviewer、不可变全局 plan 或强制大规模回退。`Dynamic Progressive Planning` 也不是 OpenAI 的正式架构名，而是 Humanize 群对体验的二次抽象。

#### 5 月 3—6 日：从惊喜到“Humanize plan + `/goal` 执行”

5 月 3 日出现首个简短实测反馈：“codex 的 `/goal` 没想到效果还挺好的。”

史料位置：[聊天记录 17396—17400 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17396)

到 5 月 6 日，群内根据 request trace 观察到 `/goal` 似乎把 build、test、review 融在一起，而不是严格切成 H1 的两个阶段；同时形成了直接把 Humanize 产出的 `plan.md` 喂给 `/goal` 的实践。群内也马上补上限制：长程任务无论直接许愿还是给 plan 都不尽如人意，仍需要小步推进。

史料位置：[聊天记录 17817—17849 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17817)

“Build/Test/Review 融为一体”是群内对 trace 的解释，不是 `/goal` runtime 硬编码的三阶段结构，正文应标成观察。

#### 5 月 16/17 日：H2 首个公开可审计实现

5 月 16 日 14:38，群内宣布 H2 已进入愿意公开展示的阶段，并说明这一版并没有更新 H1 方法学，而是：

- 规范一套 flow 原语；
- 提供 flow playground；
- 提供触发式数据流执行器；
- 支持层级化 flow、Tool/Agent 和 GUI；
- 5 月保持高频开发，6 月再进入 beta；
- H3 的路线是 “Agents create Agentic Flow”。

紧接着给出三代定位：

> H1: A flow that works.
>
> H2: A platform/language that human build/test flow.
>
> H3: An automation system that let agents builds its own flow.

史料位置：[聊天记录 21885—21915 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21885)

仓库中最关键的对应提交是 [`3fccb60`](https://github.com/PolyArch/humanize/commit/3fccb60c11332fb322a295db0583432416c7cf07)，作者时间为 2026-05-16 15:57 PDT，即北京时间 5 月 17 日 06:57。提交说明明确把 H2 的 MCP server hub、HTML workflow runtime、agent backends、dashboard 和第一方 flow cartridges 放入 `h2-dev`，与 H1 RLCR 并存。

这不是 H2 正式 Release。提交时 README 明确把 `h2-dev` 称为 **transitional branch**；`package.json` 中 H2 包版本是 `0.1.0`，而 README 顶部的 `1.17.0` 指并存的 H1 插件表面。

### 2026-05-21—05-30：H1 退到收口工具，H2 被 `/goal` 与 Dynamic workflows 重新定义

#### 5 月 21 日：长尾的实际停止规则

面对 H1 长尾，群内给出的实际策略不是理论上修完所有问题，而是当 Codex 找到的都只剩 P2/P3 时人工终止；也有人建议“如果连续三轮全是 P2 就停止”。

史料位置：[聊天记录 24527—24536 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:24527)

同一天，工作流逐渐稳定为“Humanize 生成 plan，Codex `/goal` 执行”，但社区立即指出它缺少隔离 Review。

史料位置：[聊天记录 24624—24645 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:24624)

#### 5 月 23—27 日：H1“完成历史使命”与 H2 的新任务

5 月 23 日有人认为 Codex Plan + Goal 已经很接近 Humanize 1。5 月 24 日进一步形成激进判断：H1 在长程任务的定向实现上完成了历史使命，但 `/goal` 仍缺少几块 Humanize 经验：

- 便宜的 Builder、昂贵的 Reviewer；
- 多轮 Build、一轮 Review；
- 项目历史记忆（bitter lesson）；
- 渐进式对齐。

史料位置：[聊天记录 25648—25809 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25648)

5 月 26 日，群内把长程执行所需组件概括成 `dynamic progressive planning`、`slice verifier`、`goal tracker`；与此同时也出现反向评价：“`/goal` 很像 Humanize 青春版，但是太容易跑偏了。”

史料位置：[聊天记录 26366—26440 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:26366)、[26960—26976 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:26960)

5 月 27 日，H2 的目标被重新写成两项：吸收 `/goal` 已经证明有效的 `dynamic progressive planning`；补上 H1 和 `/goal` 都没有解决好的 `dynamic progressive review`。群内定义中，progressive 指随轮次变化，dynamic 指不必每一轮都发生；H1 的 plan 被批评为“全局不动点”，而 `/goal` 的 Review 被批评为静态且过弱。

史料位置：[聊天记录 27624—27666 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27624)

这些是 Humanize 群的设计语言，不是 OpenAI `/goal` 的官方术语。

#### 5 月 28/29 日：Claude Code Dynamic workflows

Anthropic 于 5 月 28 日正式发布 [Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)，并在 Claude Code `v2.1.154` 中推出 [Dynamic workflows](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)。北京时间约为 5 月 29 日凌晨，正好对应群内第一次集中讨论。

正式名称核查结论：

- 功能正式名是 **Dynamic workflows**；
- 不是 `Auto Work`、`Auto Code` 或 `ultrawork`；
- `auto mode` 是官方建议配合使用的权限/执行模式，不是功能名称；
- `ultracode` 是把 xhigh effort 与自动 workflow orchestration 结合的设置，也不是功能名称；
- 官方最低支持版本是 [Claude Code v2.1.154](https://github.com/anthropics/claude-code/releases/tag/v2.1.154)，发布时间为 2026-05-28 18:00 UTC；
- 前一天的 [v2.1.152](https://github.com/anthropics/claude-code/releases/tag/v2.1.152) 已有 Workflow tool 和 background workflow 的公开实现痕迹，但不是正式 introduction。

官方机制是：Claude 根据任务生成 JavaScript orchestration script，在独立 runtime 中保存循环、分支和中间结果，并调度数十到数百个并行 subagents；结果经独立角度检查后再汇总。这里的“动态”首先指**工作流由模型按任务即时生成**，不等同于 Agent 在运行中持续修改正在执行的 workflow。

群内最初把它理解成“H2/H3 已经被 Claude Code 做了”，并立即感叹迭代速度；有人说 H2 是强契约静态工作流、H3 是 Agent 自动更新的动态工作流。几天后，讨论修正为：Claude Dynamic workflows 更接近静态 JS flow，动态的是被调度的 agents；Humanize 3 想增加的是 Agent 修改运行中 flow 的能力。

史料位置：[聊天记录 28738—28805 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:28738)、[32248—32301 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32248)

#### 5 月 30 日：H2 的存在空间被重新评估

有人询问 Dynamic workflows 是否可以与 Humanize 兼容、是否相当于在 Claude 原生 workflow 后加 Codex Review。回答是正在转向 H3，并直言：“dynamic workflow 出来之后，H2 其实没有很大的存在必要”；一种更轻的组合是直接在 Dynamic workflows 的某个节点加入 `codex-rescue / codex-review`。

史料位置：[聊天记录 30351—30361 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:30351)

同日对 `/goal` 的长时间观察也变得更具体：静态弱 Review、依靠局部搜索而不是全局 roadmap 保持 Big Picture、缺乏大规模回退机制。发言者明确说后两点仍在观察，证据不足，不能写成已经证实的 Codex 架构缺陷。

史料位置：[聊天记录 30865—30916 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:30865)

## 三、H2 仓库实物：哪些愿景真的实现了

以下均以 5 月 16 日的 [`3fccb60`](https://github.com/PolyArch/humanize/commit/3fccb60c11332fb322a295db0583432416c7cf07) 为准，而不是用后来分支状态倒推。

### 已实现

- **本地 MCP server hub**：作为 Agent CLI 之下的共享调度层。
- **HTML workflow runtime**：从 HTML cartridge 读取 flow、board、artifact、event、view 等定义。
- **Workflow coordinator、存储、恢复、projection、dashboard**：使执行轨迹可观察、可恢复。
- **第一方 cartridges**：`rlcr`、`gen-idea`、`gen-plan`、`refine-plan` 以及实验 flow。
- **Agent 调用与父子运行**：`agent_run`、`agent_spawn_child`、`agent_send_message`、`agent_wait` 等。
- **13 种 workflow node**：`sequence`、`parallel`、`loop`、`script`、`check`、`agent`、`message`、`sleep`、`await`、`branch`、`human`、`transform`、`end`。这与 4 月 23 日“约十种指令”的愿景大体同方向，但并非一一对应的正式 ISA。
- **typed artifacts / boards / expectations**：Agent 节点可声明输入 artifact/board 和预期输出，runtime 记录 schema 与 validation status。
- **Sandbox 与 Permission 配置**：`AgentRequest` 已包含 `sandbox` 和 `permissionMode`；权限枚举包括 `acceptEdits`、`auto`、`bypassPermissions`、`default`、`dontAsk`、`plan`。

代码证据：[README at 3fccb60](https://github.com/PolyArch/humanize/blob/3fccb60c11332fb322a295db0583432416c7cf07/README.md)、[`src/workflows/types.ts`](https://github.com/PolyArch/humanize/blob/3fccb60c11332fb322a295db0583432416c7cf07/src/workflows/types.ts)、[`src/agents/types.ts`](https://github.com/PolyArch/humanize/blob/3fccb60c11332fb322a295db0583432416c7cf07/src/agents/types.ts)。

### 愿景与实现之间的边界

- 群聊说“任意 Tool/Agent”，但 5 月 16 日代码里的 `AgentId` 只有 `codex | claude`；README 提到 Gemini、Zed 等熟悉 CLI，并不等于 backend 已全部实现。
- 群聊早期说 `humz / hcc / hvm`，仓库实际产品形态是 TypeScript MCP hub + HTML workflow runtime，并没有三个独立发布的编译工具链。
- 群聊的 `Agent = Model x Tool x Action x Permission` 是概念公式。仓库确实把 model、sandbox、permissionMode 放进 AgentRequest，也有 workflow node/action，但没有一个同名的四元组类型或完整静态类型系统。
- 群聊推荐 `acpx`，但 `package.json` 的运行依赖只有 MCP SDK、`parse5` 和 `zod`；H2 没有直接依赖 `acpx`。
- H2 是过渡分支的 `0.1.0` 平台实现，没有正式 tag/Release，也不应写成 2.0 GA。

## 四、术语核查：不要把后来的名称倒灌回 4 月

| 术语 | 最早可确认的群聊位置 | 当时准确含义 | 仓库对应 | 写作建议 |
|---|---|---|---|---|
| PID / 控制论 | 4 月 10 日 | Reviewer 是传感器，反馈帮助 loop 收敛 | H1 没有正式 PID 控制器 | 写成解释框架，不写成已实现算法 |
| B–R token 长尾 | 4 月 11、14 日 | 前期 Builder 高 token，后期大量时间消耗在小修与 Review | H1 RLCR 的实际运行现象 | 可作为 H2 出现的核心压力 |
| `Agent = Model x Tool x Action x Permission` | 4 月 23 日 | Agent 的概念分解与类型系统类比 | `AgentRequest` 有 model、sandbox、permissionMode；workflow 有 node/action | 标明是群聊公式，不是仓库 API 名称 |
| `hvm` / VM-runtime | 4 月 22—23 日 | 执行编译后 harness、跟踪并审计 flow 的机械 runtime | HTML workflow runtime、coordinator、recovery | “Agent VM”只能作为编辑性简称，原文没有这个正式产品名 |
| flow ISA | 4 月 23 日 | 从共性操作抽取原子编排动作，支持 microbench 与静态检查 | 5 月仓库有 13 种 node | 可写“从 ISA 设想到 node grammar”，不要声称严格实现同一 ISA |
| Flow IR | 6 月 16 日 | 对 H2 的后见性总结：“An IR that builds flows; enabling flows to call flows” | typed artifacts、boards、HTML flow、触发执行器 | 不能写成 4 月已经使用的术语 |
| Loop Engine | 6 月 6 日 | 对 H1 RLCR 的后见性称呼，且被评价为 PR 级“重卡” | H1 Stop Hook / RLCR loop；H2 模块叫 workflow runtime/coordinator | 不应称 H2 的正式模块名 |
| Dynamic Progressive Planning / Review | 5 月 26—27 日 | 群内从 `/goal` 与 H1 对比中形成的设计抽象 | H2 初始提交早于这轮表述 | 是后续 H2 方向，不是 5 月 16 日初始仓库规格 |

### 6 月回顾能说明什么

6 月 6 日，群内把 H1 loop 称为适合 PR 级增量改进的“重卡”，把 Codex `/goal` 称为“跑车”，并观察到 `/goal` 每 2—3 小时可能开始跑偏，需要 Claude 外部监督。

史料位置：[聊天记录 35007—35052 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35007)

6 月 13 日，`loop engineering` 被重新解释为过程控制和系统理论：H1 Goal Tracker 被看作积分器 I，Codex Review 被看作 P，`/goal` 的 progressive planning 被看作 H1 所缺少的 D。它与 4 月 14 日的 P/I/D 映射不一致，恰好证明这是逐步形成的解释，不是从一开始就固定的设计。

史料位置：[聊天记录 40794—40808 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40794)

6 月 16 日才第一次出现对 H2 的 `Flow IR` 式总结；同日又公开反思“用 HTML 当 flow language”是错误教训，转而学习 Claude Code Dynamic workflows，在 YAML/AST 外直接嵌入 JS/TS。这说明 H2 应被写成一次重要探索和中间态，而不是已经稳定的终局架构。

史料位置：[聊天记录 43776—43825 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:43776)

## 五、4—5 月值得进入正文的外部一手节点

只保留直接改变 Humanize 讨论方向的节点：

| 日期 | 外部节点 | 官方事实 | 群内意义 |
|---|---|---|---|
| 2026-04-16 | [Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) | 强调长程软件工程、复杂任务、指令遵循和自我验证 | 群内立即挂上 Humanize；但很快形成“更耗 token、修 bug 仍不如 Codex、适合早期铺开”的混合评价 |
| 2026-04-23 | [GPT-5.5](https://openai.com/index/introducing-gpt-5-5/) | 面向 agentic coding、跨工具行动、长任务和 token 效率；4 月 24 日进入 API | 群内迅速把它放入 Reviewer 位置，OpenAI 从“追赶”变成重新定义 Builder/Reviewer 分工 |
| 2026-04-21—22（群内传播） | [Kimi K2.6](https://www.kimi.com/blog/kimi-k2-6) / [官方开源权重](https://huggingface.co/moonshotai/Kimi-K2.6) | 开源、长程编码、Agent Swarm、最多 300 subagents / 4000 steps | 让“模型可替换”和国产/开源模型进入 H2 设计；实测评价随后分化 |
| 2026-04-25 / 04-30 | Codex [`/goal` PR #18077](https://github.com/openai/codex/pull/18077) / [CLI 0.128.0](https://github.com/openai/codex/releases/tag/rust-v0.128.0) | thread 级持久目标、跨 turn continuation、暂停/恢复/清除 | 最直接改变 H1/H2 叙事的工具节点：H1 的长程循环能力被 Codex 原生吸收一部分 |
| 2026-04-25 | [acpx 0.6.0](https://github.com/openclaw/acpx/releases/tag/v0.6.0) | 结构化 ACP session、adapter、模型与权限控制继续成熟 | 群内把它视作多 coding agent 兼容层和可观察调度参考，但 H2 未直接依赖 |
| 2026-05-16/17 | [Humanize H2 初始公开提交](https://github.com/PolyArch/humanize/commit/3fccb60c11332fb322a295db0583432416c7cf07) | MCP hub、HTML runtime、agent backends、dashboard、cartridges | H2 从聊天中的 PL/VM 类比落成可审计的过渡实现 |
| 2026-05-28 | [Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) + [Dynamic workflows](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) | Claude 动态生成 JS 编排脚本，调度大量并行 subagents，并在对话外保存协调状态 | H2/H3 位置被迫重估；两天后群内已提出直接在原生 workflow 节点加入 Codex Review |

## 六、可直接用于正文的匿名社区反应

以下均已去掉姓名，只保留日期与原意。引号中的轻微标点和英文大小写做了清理，不改变语义。

### 对 H1 长尾和反馈循环

- **4 月 11 日**：“干活只需要 20% 的时间，但是修到一个 Codex 能完全认可的状态，需要 80% 的时间。”
- **4 月 14 日**：“B-R Loop 有点二元震荡的味道……很容易局部震荡。”
- **4 月 14 日**：“前 20% 的时间 Builder 花 80% 的 token；后 80% 的时间，Builder 花 20% 的 token。”
- **4 月 20 日**：“Humanize 的启动和执行还是太慢了。”
- **5 月 21 日**：“看到它找出的 bug 都是 P2 的时候，我就直接终止了。”

### 对 H2 的期待与质疑

- **4 月 20 日**：“大道至简，重的 harness 感觉始终会被模型能力给吃掉。”
- **4 月 22 日**：“所有硬编码都会转瞬即逝。”
- **4 月 22 日**：“机械的功能就应该交给脚本，需要智力的地方才交给 LLM。”
- **4 月 23 日**：“有种被灌顶的感觉了。”
- **4 月 23 日**：“我们为什么还要搞一个 DSL？”
- **4 月 27 日**：“这是不是把 Humanize 变得 less sexy 了？市面上做 workflow 的 Agent system 两年前就有好多了。”
- **5 月 16 日**：“真正的 vision。”

### 对模型与角色分工

- **4 月 17 日**：“Claude 代码写得好看，Codex 任务做得更到位。”
- **4 月 17 日**：“Claude 适合早期铺开、快速搭 MVP，后续应该全部 Codex。”
- **4 月 24 日**：“GPT 说人话了，Opus 不说人话了。”
- **5 月 16 日**：“Review 我开 Codex xhigh，感觉比其他的都领先一个级别。”
- **5 月 16 日**：“Kimi Review 能赶上 Codex 这件事，我倾向于让子弹飞一会儿。”

### 对 `/goal` 的双向评价

- **5 月 3 日**：“Codex 的 `/goal` 没想到效果还挺好的。”
- **5 月 6 日**：“它似乎神奇地把 Build/Test/Review 结合在一起了，所以感觉快很多。”
- **5 月 21 日**：“Humanize plan 做好，然后只使用 Codex `/goal` 执行。”
- **5 月 21 日**：“就是没有隔离 Review 的感觉。”
- **5 月 24 日**：“Humanize 1 已经完成了它的历史使命。”
- **5 月 26 日**：“`/goal` 很像 Humanize 青春版，但是太容易跑偏了。”

### 对 Dynamic workflows 的冲击

- **5 月 29 日**：“所以 ultrawork 是 H2，Dynamic workflow 是 H3 吗？”
- **5 月 29 日**：“最怕的就是大家都太快了。”
- **5 月 29 日**：“先实际用一下吧，看看它效果怎么样。”
- **5 月 30 日**：“Dynamic workflow 出来之后，H2 其实没有很大的存在必要。”
- **6 月 2 日（修正理解）**：“Dynamic workflow 并不是 dynamic 的，工作流本身是静态的。”

## 七、第二章最需要避免的误写

1. **不要写“v1.17 是 Humanize 1.0 的正式最终版”。** 准确说法是：它被规划为最后版本线，并在 `dev` 分支做过 1.17.0 版本更新；没有 tag、Release，也未合入 `main`。
2. **不要把 PID 当作 H1 已实现算法。** 它是群内用来理解震荡、长尾和反馈的类比，而且 P/I/D 对应关系后来发生过变化。
3. **不要把 `Agent = Model x Tool x Action x Permission` 写成 H2 的正式 API。** 它是 4 月 23 日的概念公式；仓库只实现了其中一部分可配置字段。
4. **不要把 `Agent VM`、`Flow IR`、`Loop Engine` 并列成 4 月已经确定的 H2 三个模块。** 原始称呼是 `hvm / VM-runtime`；`Loop Engine` 和 `Flow IR` 分别到 6 月才出现。
5. **不要把 `/goal` 写成完整 Humanize 内置版。** 它提供目标持久化和跨 turn 续跑，但没有 H1 的独立异质 Reviewer、固定全局 plan 和 Review 收口结构。
6. **不要把 `Dynamic Progressive Planning` 写成 OpenAI 官方名。** 这是 Humanize 群在 5 月下旬形成的解释。
7. **不要把 Anthropic 功能称为 Auto Work、Auto Code 或 ultrawork。** 正式名称是 **Dynamic workflows**；`ultracode` 是设置，Auto mode 是配套执行模式。
8. **不要把 Dynamic workflows 直接等同于 H3 的自修改 flow。** 官方所说的动态，首先是 Claude 按任务生成脚本；脚本执行阶段仍由确定的 JS 控制。
9. **不要把 H2 的 5 月提交写成正式 2.0 发布。** 它是 `h2-dev` transitional branch 上的 `0.1.0` 平台实现，与 H1 1.17 表面并存。
10. **不要删除群内异议。** “DSL 是否必要”“工作流系统是否早已存在”“轻量 Humanize 是否更好”等反对意见，是理解 H2 为什么继续转向的重要史料。

## 八、核心一手资料索引

### Humanize

- [PolyArch/humanize](https://github.com/PolyArch/humanize)
- [H1.16 合并 PR #51](https://github.com/PolyArch/humanize/pull/51)
- [H1.16 main merge commit](https://github.com/PolyArch/humanize/commit/0ec921a36b4365df503511c5567bbd3e02db0df5)
- [dev 分支 v1.17.0 版本更新](https://github.com/PolyArch/humanize/commit/f4e5721e344ef602a77cfb3511ec51b74e387120)
- [H2 初始公开实现 3fccb60](https://github.com/PolyArch/humanize/commit/3fccb60c11332fb322a295db0583432416c7cf07)

### OpenAI / Codex

- [GPT-5.5 官方公告](https://openai.com/index/introducing-gpt-5-5/)
- [Codex CLI 0.128.0 Release](https://github.com/openai/codex/releases/tag/rust-v0.128.0)
- [`/goal` 持久化基础 #18073](https://github.com/openai/codex/pull/18073)
- [`/goal` 模型工具 #18075](https://github.com/openai/codex/pull/18075)
- [`/goal` 运行时 #18076](https://github.com/openai/codex/pull/18076)
- [`/goal` TUI #18077](https://github.com/openai/codex/pull/18077)
- [Codex from Claude Code 官方插件](https://github.com/openai/codex-plugin-cc)

### Anthropic / Claude Code

- [Claude Opus 4.7 官方公告](https://www.anthropic.com/news/claude-opus-4-7)
- [Claude Opus 4.8 官方公告](https://www.anthropic.com/news/claude-opus-4-8)
- [Dynamic workflows 官方公告](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)
- [Dynamic workflows 官方文档](https://code.claude.com/docs/en/workflows)
- [Claude Code v2.1.154 Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.154)

### 国产与开源生态

- [Kimi K2.6 官方技术页](https://www.kimi.com/blog/kimi-k2-6)
- [Kimi K2.6 官方 Hugging Face 仓库](https://huggingface.co/moonshotai/Kimi-K2.6)
- [OpenClaw/acpx](https://github.com/openclaw/acpx)
- [acpx v0.6.0](https://github.com/openclaw/acpx/releases/tag/v0.6.0)

