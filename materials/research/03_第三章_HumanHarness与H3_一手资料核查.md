# 第三章：Human Harness 与 Humanize 3.0 一手资料核查

> 核查范围：以 2026 年 5 月 12 日至 7 月 16 日的 Humanize 群聊为主，交叉核对 `PolyArch/humanize`、`PolyArch/oh-my-humanize`、`humanfia/oh-my-humanize`、`can1357/oh-my-pi`、`JerryLookupU/humanize-cgcr`、`SihaoLiu/skills`、KDA 仓库，以及 Anthropic、OpenAI、智谱、Moonshot AI 的官方材料。7 月中旬以后的仓库状态只用于回看实现边界，不倒写成 5—6 月已经稳定的能力。
>
> 这份文档是第三章的史料底稿。文中将材料分为三层：**仓库或厂商已经证实的事实**、**群内同期判断**、**后来为写作形成的概括**。三者不混写。群聊引文均以匿名形式呈现。

## 一、先给结论：这一阶段真正发生了什么

1. **Humanize 2.0 的 POC 与 Humanize 3.0 的定义几乎同时出现。** 5 月 16 日，群内公开说明 H2 已有 flow 原语、playground、触发式数据流执行器、Tool/Agent 接入与 GUI；同一段话第一次完整给出 H1、H2、H3 三代 Roadmap。仓库中的对应实现于北京时间 5 月 17 日进入 `h2-dev`。它是过渡分支上的 `0.1.0` 原型，还不是正式 Release。
2. **“Human Harness”先于本章后半段的认知负担讨论出现。** 5 月 12 日，社区在讨论 Plan 阶段如何让人跟上 Agent 时提出：“agent harness 让 AI 更强大，human harness 让人类更负责。”次日形成 Coach Mode 原型。它把理解检查插进 Plan 的每一层，而非只在最终 Plan 生成后让人点一次确认。
3. **“Human Awareness Cognitive Load”不是群聊中出现过的原词。** 全文与仓库均未检出这一英文短语。最接近的一手表述是 6 月 18 日的 `cognition overload`，此前还有“人类输出 token 的速度成为瓶颈”“每天的认知负担更大”，随后出现“现在 bottleneck 是人跟不上了”。本章可将这组现象概括为“人类认知同步负担”，但需要说明这是编辑性归纳。
4. **Pi、OMP 与 OMH 的名称和关系需要勘误。** 可核验的项目名是 Pi、Oh My Pi（OMP）和 Oh My Humanize（OMH），没有找到名为 “OmniPi” 的仓库或群聊术语。H2 的 HTML flow runtime 先独立成形；5 月 28 日才出现“把 H2 建在 OMP 上”的转向。6 月 1 日建立的 `PolyArch/oh-my-humanize` 才是 H3 在 OMP 脚手架上的具体实现。
5. **Anthropic 的正式产品名是 `Dynamic workflows`。** 官方于 5 月 28 日（北京时间 5 月 29 日）随 Claude Code 2.1.154 发布。Claude 会针对任务生成 JavaScript 编排脚本，再由独立 runtime 保存中间状态并协调大量 Sub-agent。这里的“动态”主要指按任务生成工作流；生成后的 JS 流程仍是静态程序。
6. **H3 对“动态”的探索经历了回摆。** 6 月 1 日的早期 OMH 代码确实允许 Agent 提案、Supervisor/Human 批准，并让调度器在运行中读取新 graph revision。到 6 月中旬，生产语义变得保守：运行中的 attempt 使用 immutable freeze；要改 flow，操作员先停止、checkpoint、批准改动、重新 freeze，再从 checkpoint 重启。正文若直接写“Agent 可以任意修改正在运行的 Workflow”，会遗漏这一轮重要的工程校正。
7. **Monitor Loop 是社区拼装出来的长程监督模式，已经有可执行实现，但尚未成为 H3 或厂商的内置标准。** 6 月 6 日，群内先用 Claude Code `/loop` 定时读取 Codex `/goal` 的 transcript、产物与 Git 变化，在必要时通知人并注入 steer prompt；6 月 10 日首次明确称为 `Monitor Loop`；6 月 17 日公开为 `monitor-codex-goal` Skill。它依赖厂商已经提供的定时调度、持久目标与远程控制能力，偏航判断、授权策略和 tmux 注入则来自社区。现有证据只支持“社区实现/原型”，不支持“Humanize 3.0 已内置”。
8. **6 月中旬更适合称为公开试用期，不宜写“内部测试”。** 6 月 3 日仓库已经开源，但还没有 Release，需要本地编译；6 月 15 日作者公开邀请群友试用。群聊当天称内置九种 flow，仓库快照也能对应到九个顶层示例目录。两天后，准入标准被提高到“本地跑十次、每次至少八小时”；6 月 16—18 日，多数未经验证的内置 flow 被移除。
9. **KDA 的公开证据支持“基于 Humanize 的算子优化工作流”，不支持“主要由 NVIDIA 内部使用”。** KDA 仓库属于 MIT HAN Lab，README 明确依赖 Humanize，并记录其用于 CUDA kernel 研究、实现、验证和迭代。另一个公开仓库记录了它在 MLSys 2026 Competition NVIDIA Track 三个 Full-Agent 赛道取得第 1、2、3 名。群里确有 NVIDIA 工程师参与和内部用户群的讨论，但目前没有 NVIDIA 官方材料证明 KDA 主要供其内部使用。
10. **“龙虾”在这份聊天记录里指 OpenClaw，不能写成 Humanize。** 群聊明确说“小龙虾也是基于 Pi”“Pi 是 OpenClaw 的 agent core”。关于“龙虾评鉴热度大幅下降”的说法，现有材料只能找到个别成员停止维护的自述，缺少可直接支持总体趋势的证据。
11. **模型时间线应写成错落推进。** GLM-5.2 于 6 月 16 日正式发布；GPT-5.6 于 6 月 26 日限量预览、7 月 9 日全面发布；Kimi K3 到 7 月 16 日才进入产品与 API，完整权重于 7 月 27 日开放。K3 不属于“6 月底或 7 月初”的同一节点，只适合放在章节尾声。

## 二、按日期还原：从 Human Harness 到 H3

### 2026-05-12—05-13：人开始跟不上，Human Harness 与 Coach Mode 出现

5 月 12 日晚，H2 的“人类介入”最初被设想成一套抽样、分层的考试机制，并保留 `--skip-quiz`。讨论很快把检查位置从“Plan 完成以后”提前到生成过程：

> “能不能做成在 gen-plan 的过程就考试，不要等到 plan 完全生成以后再考试？”
>
> “我想要的是 Plan-time Human Ver…”
>
> “agent harness 让 AI 更强大，human harness 让人类更负责。”

史料位置：[聊天记录 19874—19960 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19874)

这段话给“Human Harness”一个很朴素的起点：Agent 已经能在长程任务中持续生产，人类的职责开始从逐行实现转向理解设计、识别偏差并承担放行责任。社区当晚把问题分成三类：

1. **记忆（Memory）**：让人复述自己已经做出的设计，检验设计意图是否发生漂移；
2. **自检（Self-check）**：让人检查 AI 的设计是否符合目标，答不上或不同意可能意味着 AI 设计错了；
3. **教育（Education）**：先补齐必要背景，再依赖这个概念推进计划。

史料位置：[聊天记录 19974—19981 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19974)

5 月 13 日，群内给出了两个更准确的名字：`Plan-time Human Verification` 和 `Interactive Plan Comprehension Gate`，同时提出“老师模式”或 Coach Mode。史料位置：[聊天记录 20401—20429 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20401)

这一想法当天就进入代码。Humanize [PR #159](https://github.com/PolyArch/humanize/pull/159) 于 5 月 13 日创建，首个实现提交是 [`e69b239`](https://github.com/PolyArch/humanize/commit/e69b239770df68141939721f07526ee82ada7c5f)。代码里的 `--coach` 不是最终确认框，它规定了四道关卡：

- 首轮分析之后、候选 Plan 之前；
- 候选 Plan 之后、继续收敛之前；
- 每一轮收敛之后；
- 写入最终 Plan 之前的总体验收。

每道关卡先用 3—5 个要点解释当前状态，再要求用户用自己的话回答。选择题、是/否和“继续”不能代替理解检查。Memory 不一致会被当作设计意图可能漂移；Self-check 否决会触发 AI 方案修订；Education 缺口会先补背景。人类未对齐时，流程停在当前层，不继续扩张计划。

需要保留时间边界：这个功能 5 月 13 日已经写出，但 PR 直到 6 月 13 日才合入 `dev`。因此可以写“5 月形成并完成首版实现，6 月进入开发主线”，不要写成“5 月已经正式发布”。

### 2026-05-16—05-17：H2 POC 公开，H3 被第一次完整定义

5 月 16 日，Humanize 2.0 首次被公开描述为一套可供社区研究的 POC：

- 规范 flow 原语；
- 提供 flow playground；
- 用触发式数据流执行 flow；
- 支持任意层级的 flow、Tool/Agent 与 GUI；
- 5 月继续高频开发，原计划 6 月进入 beta；
- H3 的核心精神是 `Agents create Agentic Flow.`

同一段群聊留下三代 Roadmap 的原始版本：

> `h1: A flow that works`
>
> `h2: A platform/language that human build/test flow`
>
> `h3: An automation system that let agents builds its own flow`

史料位置：[聊天记录 21885—21915 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21885)

5 月 21 日的中文复述更容易理解：H1 是“一个能干活的 flow——RLCR”，H2 是“一个搭 flow 的平台和强类型流程语言”，H3 要“搞清楚怎么让 AI 自己搭 flow”。史料位置：[聊天记录 24224—24236 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:24224)

仓库中的实物证据是 [`3fccb60`](https://github.com/PolyArch/humanize/commit/3fccb60c11332fb322a295db0583432416c7cf07)。它于北京时间 5 月 17 日 06:57 提交到 `h2-dev`，一次加入约 2.2 万行实现，包括：

- MCP server hub 与 Agent session 管理；
- HTML workflow runtime；
- workflow graph、parser、coordinator、recovery；
- typed artifacts/boards 与 schema registry；
- Codex、Claude、fake backend；
- dashboard 与 H1 的第一方 flow cartridges。

README 将 `h2-dev` 明确写作 transitional branch，包版本为 `0.1.0`。这足以支持“H2 POC 已诞生”，尚不足以支持“H2 已稳定发布”。

Roadmap 原文有语法问题。正文若要保留三句式，建议润色为：

> **Humanize 1.0: A flow that works.**
>
> **Humanize 2.0: A platform and language for humans to build and test flows.**
>
> **Humanize 3.0: An automation system that lets agents build and evolve their own flows.**

其中 `evolve` 是结合 6 月“progressive / mutable workflow”形成的编辑补充。若要逐字忠于 5 月 16 日的定义，可删去 `and evolve`，写成 `lets agents build their own flows`。

### 2026-05-22—05-28：从 H2 自研脚手架转向 Pi 与 OMP

5 月 22 日，群内开始推荐 `oh-my-pi`，并把它作为 Coding CLI 讨论。与此同时，已有成员把自己的常用组合描述为 `humanize gen-plan + codex /goal`，并直言很少再用 RLCR 本体。史料位置：[聊天记录 24990—25030 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:24990)

5 月 28 日，转向变得明确：

> “omp is soooooo good.”
>
> “I need to build h2 on omp.”
>
> “humanize2 不在 omp 里面构建是完全不合理的，它把脚手架全部都搭完了。”

史料位置：[聊天记录 27882—27908 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27882)

稍后的讨论把当时的构想压缩成一句话：“把 OMP 的 orchestration 从 YAML 改成强类型的契约模式。”这仍是社区对 H2 迁移方式的设想，不能当作已经落地的架构。史料位置：[聊天记录 27970—27980 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27970)

这里需要把三个项目分清：

| 名称 | 可核验项目 | 在这段历史中的位置 |
|---|---|---|
| Pi | [earendil-works/pi](https://github.com/earendil-works/pi) | 轻量 Agent toolkit，提供统一 LLM API、Agent loop、TUI 与 Coding Agent CLI；仓库后来由原 `badlogic/pi-mono` 迁移而来 |
| OMP | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | 在 Pi 上扩展的终端 Coding Agent，提供供应商、工具、Sub-agent、TUI 等完整脚手架 |
| OMH | [humanfia/oh-my-humanize](https://github.com/humanfia/oh-my-humanize) | 6 月初从 OMP fork 起步，把 H2/H3 的 workflow 语言与运行设施落到 OMP 之上 |

“OmniPi”没有出现在群聊或上述官方仓库中，大概率是对 OMP / Oh My Pi 的误记。正文应统一写 **Oh My Pi（OMP）**。

还要修正“Humanize 2.0 主要基于 HTML 实现 OMP 接入”这一说法。时间顺序正好相反：H2 的 HTML runtime 已在 5 月 17 日 POC 中存在，5 月 28 日才决定向 OMP 转移；真正形成 OMP fork 的项目是后来的 OMH/H3。6 月 16 日，作者还公开复盘“拿 HTML 当 flow language”是一次教训，转而用 YAML 作为可解码的 AST、用 JS/TS 表达机械程序。史料位置：[聊天记录 43776—43825 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:43776)

### 2026-05-28—05-30：Anthropic 发布 Dynamic workflows，社区迅速校正 H2/H3 的位置

Anthropic 于 5 月 28 日发布 [Introducing Dynamic workflows in Claude Code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)，对应 [Claude Code 2.1.154](https://github.com/anthropics/claude-code/releases/tag/v2.1.154)。换算到北京时间，群内集中讨论发生在 5 月 29 日凌晨。

官方机制可以概括为：Claude 针对任务现场生成一段 JavaScript 编排脚本；脚本在独立 runtime 中运行，保存循环、分支和中间状态，按需生成并协调数十乃至数百个 Sub-agent，并允许独立验证。这样，协调状态不必全部挤在主对话上下文中。

群内第一反应是“这就是 H3 想做的东西”，并一度把 `ultrawork` 对应 H2、Dynamic workflow 对应 H3。史料位置：[聊天记录 28725—28805 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:28725)

一天后，判断已经变得更具体：既然 Claude Code 能生成 JS flow，H2 作为独立平台的空间被压缩；Humanize 可以在某个节点插入 Codex Review/Rescue。史料位置：[聊天记录 30335—30366 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:30335)

随后，社区进一步修正了“Dynamic”的含义：Claude 的 workflow 是按任务动态生成的，运行时脚本本身仍然静态；H3 试图让 Agent 或人根据运行反馈继续调整 flow。这一区分在 6 月 2 日被明确说出。史料位置：[聊天记录 32248—32301 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32248)

因此，本章可以把三种流程放在同一条光谱上：

| 层次 | 流程何时变化 | 同期代表 | 证据边界 |
|---|---|---|---|
| 预先定义的静态流程 | 开始运行前由人写好 | H1 RLCR、普通脚本 flow | 运行中主要改变状态，不改变图结构 |
| 按任务生成的流程 | Agent 在启动时生成一份任务专用程序 | Claude Code Dynamic workflows | JS 生成以后作为协调程序运行；“动态”不等于自修改 |
| 运行反馈驱动的渐进流程 | 执行期间提出 graph change | H3 / OMH 早期 prototype | 6 月初支持 live revision；随后加入审批与冻结边界 |
| 受控演化的生产流程 | stop → checkpoint → approve → freeze → restart | 6 月中旬 OMH | 生产 attempt 保持 immutable，变化通过新 revision 生效 |

这条演进很重要。H3 的价值逐渐从“能否热改一张图”转向“谁能提出改动、谁批准、如何保留状态、如何审计和回退”。

### 2026-06-01—06-03：Oh My Humanize 出现，H3 进入可审计原型

5 月 31 日，群内明确说“我打算 H3 直接在 OMP 上面开发”，理由是 OMP 已经省去大量脚手架。史料位置：[聊天记录 31376—31408 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:31376)

6 月 1 日，GitHub 上创建 [PolyArch/oh-my-humanize](https://github.com/PolyArch/oh-my-humanize)，它当时还是 [Oh My Pi](https://github.com/can1357/oh-my-pi) 的 fork。最早的一组提交清楚显示 H3 从概念进入代码：

- [`6d6bd85`](https://github.com/humanfia/oh-my-humanize/commit/6d6bd85ef5c3eecf69f1711e653a285975d1481c)：加入 workflow definition 与 condition DSL；
- [`26b082f`](https://github.com/humanfia/oh-my-humanize/commit/26b082f580f6942492b89f26650d1d67bc6d9e22)：加入 workflow graph patch API；
- [`fccda30`](https://github.com/humanfia/oh-my-humanize/commit/fccda309629d02ee033f06819a2554d8b6a8ca22)：让 scheduler 在每次 activation 与 transition 时读取当前 definition 和 graph revision。

早期 API 已经包含 `agent`、`supervisor`、`human` 三类 actor。Agent 可以提出 patch，真正 apply 要求 Supervisor 或 Human 批准。应用后，run 的 `currentGraphRevisionId`、definition、revision history 和 applied patch history 会一并更新。这构成“Agent mutable workflows”的实物证据，也显示它从起点就带有权限与审计意识。

6 月 2 日，群里把项目写成：

> “h3 (oh-my-humanize) 的核心增量特性是：允许 agent 改动正在运行中的工作流。”
>
> “h3 = oh-my-humanize = agent mutable workflows.”

史料位置：[聊天记录 32248—32301 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32248)、[33111—33118 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33111)

6 月 3 日，有人问 H3 何时推出，回答是“已经开源”；紧接着又说明“现在还没有 release，要自己本地编译”。史料位置：[聊天记录 33597—33620 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33597)

所以这一节点适合写成：**H3 的开源原型已经出现，尚未形成正式发布和稳定使用面。**

### 2026-06-06—06-25：Monitor Loop 从“监工”想法变成可运行的监督层

Monitor Loop 出现以前，`monitor` 在 Humanize 中已经有一层较早的含义。H1 的 Goal Tracker 保存 Ultimate Goal、验收条件、当前任务和演进记录；`humanize monitor rlcr-loop` 则把轮次、日志和 Goal Tracker 摘要展示在状态面板上。这是一套 **ledger + dashboard**：它帮助人查看循环状态，却不会自己理解任务语义、判断偏航或向工作会话注入纠偏指令。6 月形成的 Monitor Loop 多了一层独立 Agent 监督，两者需要分开。

这套实践所需的三个厂商底座当时已经陆续到位：

- Claude Code [2.1.51](https://github.com/anthropics/claude-code/releases/tag/v2.1.51) 于北京时间 2 月 24 日加入 Remote Control，让本地会话可以从 Web 或手机继续控制；官方命令是 `/remote-control` 或 `/rc`，群聊里的 `/remote` 更可能是口语或 OCR 简写；[2.1.110](https://github.com/anthropics/claude-code/releases/tag/v2.1.110) 又于北京时间 4 月 16 日加入 Push tool，用于任务完成或需要决策时通知人；
- Claude Code [2.1.71](https://github.com/anthropics/claude-code/releases/tag/v2.1.71) 于北京时间 3 月 7 日加入 `/loop` 和 cron scheduling tools；`/loop` 只负责在同一会话里定时重复 prompt，本身没有偏航判断逻辑；
- Codex [0.128.0](https://github.com/openai/codex/releases/tag/rust-v0.128.0) 于北京时间 5 月 1 日加入持久化 `/goal`、暂停/恢复/清除与空闲续跑。它让长程目标能跨 turn 保持运行，但不等同于 Humanize Goal Tracker 的完整 AC、任务和 evolution ledger，也没有自带独立监督者。

6 月 6 日 07:40，群内第一次把三者组合成一个可操作的方法：开一个 Claude Code `/loop`，将另一个正在运行的 Codex `/goal` session id 交给它；Claude 定时分析目标会话的 transcript、仓库和产物，如果发现工作进入死胡同或偏离主线，就通过 Remote Control 通知手机。同期原话还特意区分：“之前 Humanize 是做代码审查的监工”，这一次找的是第三方“进度”的监工。史料位置：[聊天记录 34718—34749 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:34718)

当时给出的角色分工很清楚：

> `Claude + 我 => 写给 Codex /goal 的 prompt`
>
> `Codex + /goal + subagent => 干活`
>
> `Claude + subagent => 监控 Codex /goal 的进度`

史料位置：[聊天记录 34981—35005 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:34981)

这里最有价值的观察是“时间流逝”成为监督信号。Worker 的上下文会不断压缩，容易把长时间钻研某个细节合理化；独立 monitor 每隔一小时醒来，能从连续 tick 中看到三小时、五小时仍未推进主线的差别。6 月 7 日，实践者把它称为近期提升开发体感最大的变化，并自报约十到十二小时出现一次 Claude 所判断的偏航。这个比例只是一次个人工作流观察，不能写成 benchmark。群内列出的典型偏航是“钻牛角尖、深挖细节、不推进主线”，monitor 主要扫描 transcript，也会抓取 tmux pane。史料位置：[聊天记录 35443—35515 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35443)

6 月 6—8 日，这个想法已经进入原型。社区仓库 [JerryLookupU/humanize-cgcr](https://github.com/JerryLookupU/humanize-cgcr) 的首个实现提交 [`6de5eb1`](https://github.com/JerryLookupU/humanize-cgcr/commit/6de5eb16c9ae5e59e8f78900d4de3c90a63166b2) 在北京时间 6 月 6 日 23:46 落地，名称是 `Codex goal with Claude review`。它用 tmux 启动两个窗口，并将纠偏分成复述提醒、增加约束、强约束和奥卡姆约束四级。群内于 6 月 8 日分享该仓库。史料位置：[聊天记录 36080—36094 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36080)

相应的 Humanize [PR #205](https://github.com/PolyArch/humanize/pull/205) 于 6 月 8 日创建，试图增加 Codex 执行、Claude 只读监督的反向 workflow；截至 2026 年 8 月 5 日仍未合并。随后 [Issue #213](https://github.com/PolyArch/humanize/issues/213) 又提出 `monitor-claude-goal`，同样停留在开放提案状态。这说明 CGCR 已经是可运行的社区原型，还没有进入 Humanize 主线。

6 月 8 日，实践规模被描述为十个 Claude 监控 loop 对齐十个 Codex `/goal`，并为少数情况设置 auto-inject 白名单。同期也强调：不审批时就退化为普通 `/goal`，人类只在几个关键点提供锚定；当时个人版本仍主要依靠提示词，并未整理成 Skill。史料位置：[聊天记录 36338—36400 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36338)

6 月 10 日 12:00，群聊第一次明确检出大写术语 **Monitor Loop**。同期表述是让 Agent Loop 推进各个 flow 环节，再引入 Monitor Loop 并行观察，只在有限的关键节点让 Human 介入。OCR 在 AC 相关句子上有截断，因此正文适合概述，不宜把残句逐字引用。史料位置：[聊天记录 37862—37870 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:37862)

两天后，社区把长程系统概括成三条循环：

> “带验证的长程循环，有固化的 workflow 做流程锚定，带全局视野的监控循环。”
>
> “构建循环 + 监控循环 + 审计循环，三驾马车。”

史料位置：[聊天记录 39384—39393 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:39384)

Monitor Loop 并不意味着持续给 Worker 发指令。6 月 12 日的实践总结是“monitor 大部分时候都是零注入，但是它总结汇报的功能非常好”。6 月 13 日又把监督输入压缩成三类：transcript、产物变动、Git commit；作用是感受真实时间、保持大方向、帮助内部 loop 跳出局部最优。群内明确称它是进度监控，不是代码审查或 building loop，并有人提出应关掉 monitor 偶尔自行复审代码的倾向。它也不只适用于 `/goal`：同期原话是“任何指令都可以监控”，`/goal` 只是这一阶段最常见的长程 Worker。史料位置：[聊天记录 39957—39960 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:39957)、[40381—40400 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40381)

6 月 17 日，这套方法有了公开、可执行的 Skill。[`SihaoLiu/skills`](https://github.com/SihaoLiu/skills) 的初始提交 [`ec9cd9e`](https://github.com/SihaoLiu/skills/commit/ec9cd9e2733f28d93bbf66c37ef58722cf6390ce) 于北京时间 13:42 写入 `monitor-codex-goal`，仓库三分钟后公开，13:46 分享到群内。首版已经包含：

- 独立 Claude Code 会话与默认一小时 cadence；
- 按 session id 和 tmux pane 定位目标；
- 读取 transcript、Git 变化和产物，派发只读 Explore Agent；
- Remote Control 的启动检查、heartbeat 和手机通知；
- 经过目标校验、粘贴确认和有限重试的 tmux steer 注入脚本；
- 人类授权门：多数纠偏先请求批准，只有既定原则的重申或严重完整性风险进入自动注入白名单；`--notify-only` 可彻底关闭自动注入。

这已达到“公开实现”的层级，归属仍是个人 Skill 仓库，未合入 `PolyArch/humanize` 或 OMH。正文可以写“社区把 Monitor Loop 代码化”，不要写“Humanize 3.0 已内置 Monitor Loop”。

同一天的本地 H3 实验给出了五层传导链：人类 → Claude Code `/loop` → Codex `/goal` → Codex Sub-agent → 运行 workflow 的 OMH。tmux 同时承担“终端操作手”和“录屏器”，一层监督也被理解为一层 context 压缩，只有更本质的问题逐层上浮到人。史料位置：[聊天记录 44535—44618 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44535)、[44694—44778 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44694)

6 月 18 日，有成员询问能否用 Monitor Loop 监督一个 flow test case 是否沿预期 path 运行，回答是“我已经这么做了”，并指向五层链中第 4 层对第 5 层的监控。这能证明 Monitor Loop 已经用于本地 H3 flow 测试，仍不足以证明它成为 OMH 的正式 built-in。史料位置：[聊天记录 45970—45989 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45970)

6 月 23 日又补出一个更机械的兜底脚本 [`watch-codex-goal`](https://github.com/SihaoLiu/skills/commit/671516c91d41417aeefd24b097368412f6a5205b)：扫描 tmux pane，如果 `/goal` 因 429 或 5xx 长时间 blocked，就发送 `/goal resume`。群内将两层关系说得很直白：“主 Claude `/loop` 监控 Codex goal，脚本保底。”前者做语义进度判断，后者只管 liveness；需要人回答的问题可另行通过 Telegram 通知。史料位置：[聊天记录 47893—47924 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47893)

到 6 月 24—25 日，实践边界也暴露出来：一个人每天大约只能认真观测十组 loop + goal，人依旧会成为系统瓶颈；注入式 monitor 并非每个人都运行顺畅；短任务增益有限；monitor 与 review 同时存在还可能引发 hook 冲突。社区于是区分定时或阶段触发的主动监控、遇到决策再升级的被动监控，并提出把运行数据留给事后 meta optimizer。史料位置：[聊天记录 48276—48295 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48276)、[48773—48814 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48773)

这段演进可以按成熟度分成四层：

| 时间 | 成熟度 | 证据支持的表述 |
|---|---|---|
| 6 月 6 日以前 | 前置想法与基础设施 | Goal Tracker、状态面板、完成通知、第二个 AI 做监工等想法陆续出现 |
| 6 月 6—8 日 | 可复用实践与原型 | `/loop` 监督 `/goal` 已实际运行；CGCR 仓库把它包装成 tmux workflow |
| 6 月 10—13 日 | 命名与操作定义 | `Monitor Loop` 成为明确术语，并与 Build/Review 区分 |
| 6 月 17 日以后 | 公开社区实现 | `monitor-codex-goal` Skill 可执行，并用于本地 H3 flow 测试；尚未进入 Humanize/OMH 主线 |

与几个相近概念的关系也应固定下来：

| 相近概念 | 与 Monitor Loop 的关系 |
|---|---|
| Humanize Goal Tracker | 保存目标、AC、任务和演进的内部账本；可供 dashboard 展示，没有证据表明 6 月 Monitor Loop 必须读取 `goal-tracker.md` |
| Codex `/goal` | 被监督的长程执行引擎；持久目标与续跑是官方能力，外部监督不是 `/goal` 自带行为 |
| Claude `/loop` | 定时唤醒监督 prompt 的调度器；Monitor Loop 的判断标准、读哪些材料和何时纠偏由社区补上 |
| Remote Control / Push | 手机与本地会话之间的通信、控制和通知通道；不会自己识别偏航 |
| Code Review | 检查实现正确性；Monitor Loop 主要看时间、进度与主线偏移，群聊明确要求减少越界复审 |
| H1 feedback issue | 长程任务结束后把脱敏反馈沉淀为 Issue；Monitor Loop 的 steer 是运行时反馈，两者处在不同阶段 |
| tmux 注入 | 将批准后的 steer prompt 送进 Worker TUI 的执行通道；并不等于监控判断本身 |

最稳妥的一句话结论是：**Monitor Loop 把官方已有的定时调度、持久目标和远程控制拼成一层社区监督协议，让独立 Agent 对长程任务做低频、全局、可升级的进度检查。它已经从经验走到公开实现，仍处于多种工具组合的实验期。**

### 2026-06-06—06-18：从效率增长转向“人类认知同步负担”

“Human Awareness Cognitive Load”虽然不是原始术语，它所指向的现象在群聊里有一条连续证据链。

5 月 24 日，讨论先从输入带宽开始：

> “人类输出 token 的速度已经成为了核心的 bottleneck。”
>
> “唯一能稍微解决问题的方法就是 multiple-human in the loop。”
>
> “‘我’才是系统的瓶颈。”

同一晚还有一段很值得保留的自省：许愿式 workflow 用得太多，会让人失去 intuition，作为 reward model 变得迟钝。史料位置：[聊天记录 26005—26049 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:26005)

6 月 6 日，问题从输入速度扩展到认知密度：

> “AI 只是把 Implementation 的心智负担切分到 Arch 和 DV 上了。”
>
> “人类心智消耗的需求并没有减少，反而密度更高了。”
>
> “每天的认知负担更大，工作时间更长。”

讨论最后承认效率确实提高，但可做的工作近乎无限，效率提升不会自动换来休息。史料位置：[聊天记录 34672—34708 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:34672)

6 月 18 日，`cognition overload` 第一次以可检索的英文短语出现。起因是长程任务已经写下十个条件，仍可能遗漏二三十个隐性条件；用户必须确认的细节越来越多：

> “所以其实还是一个 cognition overload 的问题？必须确保里面的每个细节都自己确定好了之后，才能执行。”

群内紧接着追问：这些细节是否可以让 Agent 自己决定，还是必须等待人类输入；另一个回答是“所以才有 grill-me 呀”。史料位置：[聊天记录 45831—45866 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45831)

到 7 月 10 日，群里用一句更直接的话收束：“现在 bottleneck 是人跟不上了。”史料位置：[聊天记录 52820—52845 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52820)

结合 Coach Mode，这组讨论可以形成第三章的一个核心判断：**当 Agent 能持续完成复杂长程任务，Humanize 的反馈环也要承担认知同步。人需要在关键设计节点理解“当前做到了哪里、为什么这样做、哪些约束已经改变”，才能给出有效判断。** 这是从一手材料抽出的编辑性结论，不是群内某一天已经写成的正式定义。

英文术语建议：

- 正文中文优先使用：**人类认知同步负担**；
- 如需英文：`human cognitive synchronization load`；
- 也可使用更自然的：`the cognitive load of keeping humans in sync`；
- 保留历史原话时写：`cognition overload`；
- 避免把 `Human Awareness Cognitive Load` 当成已经确立的学术或社区术语。

### 2026-06-12—06-18：KDA、九个内置 Flow 与一次迅速的回退

6 月 12 日，群内首次集中解释 KDA，并链接 [mit-han-lab/kernel-design-agents](https://github.com/mit-han-lab/kernel-design-agents)。史料位置：[聊天记录 40075—40102 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40075)

KDA README 将它定义为：使用 Coding Agent 研究、实现、验证并迭代性能敏感 CUDA kernel 的 Agent-centric workflow。最小流程要求先写任务契约，再形成 Plan，随后小步实现、验证、记录候选与性能证据；README 明确将 Humanize 列为 Plan 生成工具和 Claude Code 插件依赖。这足以支持“它是从 H1/RLCR 演化出来的算子优化工作流”。

6 月 15 日，OMH 进入公开邀请试用阶段。群内原话是：

> “oh-my-humanize 到了一个我愿意公开地请大家一起试一试的地步了。”
>
> “里面内置了 9 种不同 flow。”
>
> “而且里面内置了 humanize 1.0 和 kda。”

史料位置：[聊天记录 42888—42922 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42888)

仓库快照可以和“九种”对上。在当时公开试用对应的 [`39de077`](https://github.com/PolyArch/oh-my-humanize/tree/39de07716d255a0de489d222afdbcc84240520bb/packages/coding-agent/examples/workflows) 快照中，README 明列九个顶层可调用 built-in；其加入过程可追溯到 [`45eece0`](https://github.com/humanfia/oh-my-humanize/commit/45eece01b8709184906474dec9477493c6da394c)。`packages/coding-agent/examples/workflows` 下有九个顶层目录：

- `humanize-rlcr`
- `kda-humanize-reference`
- `agent-build-review-loop`
- `human-interactive-dev`
- `parallel-weak-implementation`
- `recflow-audit-events-cockpit`
- `branch-conditional`
- `loop-until-done`
- `parallel-join`

其中部分目录还包含 Sub-flow，因此简单统计 `.omhflow` 文件会得到十一，而不是九。这也是后续核对数量时容易出现差异的原因。

同日，群内还描述了 import 设想：`kda.omhflow` 可直接 import `humanize.rlcr`，未来 flow 也可组合 `codex.goal`、`claude.loop` 与 `humanize.rlcr`。这是“flow 调用 flow”与复用算子的直接表达。史料位置：[聊天记录 42797—42815 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42797)

但公开试用没有被包装成一帆风顺的发布。6 月 17 日，内置资格被提高为“本地跑十次、每次至少八小时”；同一段对运行中改流的回答也已经变成：需要专门的审核门控和人类介入，不能直接边跑边改。史料位置：[聊天记录 44096—44120 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44096)

仓库提交 [`21e56a0`](https://github.com/humanfia/oh-my-humanize/commit/21e56a0892beeffdab258157860ec9d94f25e378) 的标题就是 `demote unverified built-in flows`，一次移除了 Humanize RLCR、KDA、并行实现等未经充分验证的内置 artifact。6 月 18 日，群内解释此前九个 flow 中有一两个暴露 bug，于是整体 rollback；本地连续运行 80 小时确认后再升格，Humanize RLCR 与 KDA 当时仍被认为可用。史料位置：[聊天记录 45897—45918 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45897)

这次回退应写进历史。它显示 H3 很快从“能生成很多 flow”走向“什么 flow 有资格被社区当成内置能力”，验证成本开始成为基础设施的一部分。

### 2026-06-14—06-19：Live mutation 收紧为可审批、可冻结、可恢复的演化

6 月 12 日的 [`eea3778`](https://github.com/humanfia/oh-my-humanize/commit/eea3778e2e5ba7fa38f90eae6da4d9d9461a1474) 以 `add mutable workflow runtime` 为题，对 lifecycle、freeze、patch、checkpoint、session runtime、TUI 和测试进行了一次大规模重构。6 月 13 日的 [`eb78a8e`](https://github.com/PolyArch/oh-my-humanize/commit/eb78a8eacc905434dd340f01a0f1ea8fa5d90276) 随即改变安全策略，拒绝直接向 active run 提交 graph patch，要求改走 workflow change request。代码错误信息很直接：`workflow graph patches cannot be proposed on an active run; use a workflow change request instead`。

到 6 月 14 日的 [`aaf4642`](https://github.com/humanfia/oh-my-humanize/commit/aaf46428db15a2cfe2b18f9eae9a61827f47d1c1)，`docs/workflows.md` 已经把生产语义写得非常明确：

> A workflow can be edited while it is in development, but a production attempt runs against an immutable freeze. If the flow must change, the operator stops the attempt, checkpoints it, applies an approved change, freezes the new graph, and restarts from the checkpoint.

这段话给 H3 的“动态”加上四个工程约束：

1. 开发态可以编辑，生产 attempt 绑定不可变快照；
2. 变更需要授权；
3. 运行状态通过 checkpoint 保留；
4. 新图形成新 freeze，再从 checkpoint 重启。

所以 H3 的成熟表达更适合用 **progressive workflow** 或 **controlled workflow evolution**。它仍允许 Agent 参与改变 flow，却不让一个正在生产执行的图在无人知情时随意变形。

6 月 19 日，作者描述了一组尚未公开成 benchmark 的本地实验：每天启动约 150 个 run，让 Agent 自己选择十万行以上的开源项目、设计 flow、设计与 flow 匹配的任务，最后只沉淀 flow；失败或终止后，再由 GPT-5.5 xhigh 审查轨迹。相比 H1 一天不到一条反馈，这套本地“Humanize 社区”自称能获得约 150 条反馈。史料位置：[聊天记录 46235—46335 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46235)

这些数字适合写成**作者自报的实验规模**，不能写成 OMH 的公开 benchmark 成绩。它们仍有历史价值：H3 的开发方法本身已经从手工设计 flow 转向批量生成、运行、审查和筛选 flow。

同日，项目通过迁移提交 [`04e0229`](https://github.com/PolyArch/oh-my-humanize/commit/04e0229d474b7258f8bf36efd0d86f6036857456) 从 fork 仓库迁移为独立的 [humanfia/oh-my-humanize](https://github.com/humanfia/oh-my-humanize)。旧的 `PolyArch/oh-my-humanize` 保留了 fork 身份，后续公开维护面以 `humanfia` 为准。

## 三、KDA、NVIDIA 与“算子榜单”的证据边界

关于 KDA，正文可以确认以下内容：

- [KDA 仓库](https://github.com/mit-han-lab/kernel-design-agents) 属于 MIT HAN Lab；
- 它定位为 CUDA kernel 的研究、实现、验证、迭代工作流；
- README 明确要求或推荐 Humanize，用它把 draft 转成可执行 Plan，并在小步实现中保留证据；
- [MLSys 2026 FlashInfer Contest 开源材料](https://github.com/mit-han-lab/mlsys2026-flashinfer-contest) 说明其 Full-Agent workflow 由 KDA 驱动，Humanize、KernelWiki 和 NCU Report Skill 是核心组成；
- 该仓库记录 HAN Lab Kernel Mafia 在 MLSys 2026 Competition NVIDIA Track 的 MoE、DSA、GDN 三个赛道分别取得第 1、2、3 名。

需要降格处理的说法：

1. **“KDA 主要由 NVIDIA 内部使用”**：目前缺少 NVIDIA 官方仓库、公告或内部使用统计。群聊中出现 NVIDIA 成员、私有 Slack 群与 “Nvidians” 用户群，只能证明社区与 NVIDIA 工程师有交集。
2. **“KDA 在 SOL-Bench 全面击败 Recursive”**：6 月 18 日群聊确有“在 sol-bench 上把 Recursive 挨个打过去”的自述，史料位置：[聊天记录 45990—46035 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45990)。目前没有找到对应的公开榜单快照或可复现实验，正文只能写“群内自报”。
3. **“算子榜单”**：能够公开核对的是 FlashInfer Competition 的三个赛道名次；SOL-Bench、KernelBench、SOL-ExecBench 等出现在群聊中时，应分别链接各自 benchmark，不宜合称成一个权威总榜。

一段可直接用于正文的安全表述是：

> KDA 把 Humanize 的 Plan 与 RLCR 引入 CUDA kernel 优化，并补上 KernelWiki、NCU 分析和性能证据记录。MIT HAN Lab 后来公开的 MLSys 2026 FlashInfer Competition 材料显示，这套 Full-Agent workflow 在 NVIDIA Track 的三个赛道分别取得第一、第二和第三。群内还分享过 SOL-Bench 上的领先进展，但当时没有同步公开可复现的榜单快照。

## 四、“龙虾”、OpenClaw 与 CLI 回归：必须做的名词校正

在这份聊天记录里，“龙虾”与“小龙虾”指向 OpenClaw：

- 5 月 22 日，有成员说“上一次用 Pi 还是修龙虾的时候，后来不修了我就没用 Pi 了”；史料位置：[聊天记录 25004—25018 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25004)
- 6 月 10 日，群内说 OMP 建在 Pi 上，“小龙虾也是的”，随后分享“OpenClaw 背后核心框架 Pi”；史料位置：[聊天记录 38238—38258 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:38238)
- 7 月 12 日再次明确：“Pi 是 OpenClaw 的 agent core”；史料位置：[聊天记录 54430—54455 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:54430)

因此，以下写法需要改：

> 到这个阶段，社区对“龙虾”（Humanize）的关注度大幅降低。

更忠实的写法可以是：

> 到这个阶段，OpenClaw 仍偶尔作为 Pi 的历史入口被提起，群内的实践重心已经明显转向 Coding CLI、OMP/OMH、Codex 与 Claude Code 的长程工作流。

“明显转向”是基于主题分布的编辑观察，并非群内做过量化统计。若正文要使用“大幅降低”，建议先按月份统计 OpenClaw/龙虾相关消息量；现有单条“后来不修了”的自述不足以代表整个社区。

## 五、同期模型变化：应怎样嵌入 H3 的历史

### 2026-06-16：GLM-5.2 正式发布

智谱于 6 月 16 日发布 [GLM-5.2](https://z.ai/blog/glm-5.2)。官方材料和[模型卡](https://huggingface.co/zai-org/GLM-5.2)支持以下特征：

- 稳定的 1M Context；
- 面向长程 Agentic Work 的训练与评估；
- Flexible Effort；
- 在 1M 长上下文下通过 IndexShare 降低每 token 计算量；
- 开放权重采用 MIT License。

对应发布提交是 [`0e29acc`](https://github.com/zai-org/GLM-5/commit/0e29acc8884b689ce2ec0e1abafecb160defb469)。群里在 6 月 13—14 日已经出现“GLM-5.2 出来了”和早期试用反馈，时间早于正式公告，应写成提前流传、灰度或早期可用。史料位置：[聊天记录 41845—41885 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:41845)、[42085—42125 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42085)

群内评价没有形成单一结论：有人认为它已经是国产模型第一梯队、接近 Opus；也有人反馈速度慢、容量难抢、幻觉仍多，或者实际体验像蒸馏模型。6 月 22 日出现“GLM-5.2 在 Claude Code 里主动调用 ask-codex Review，于是 H1 被炼化”的判断。史料位置：[聊天记录 47285—47320 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47285)

这条反馈能证明**模型与 Harness 组合后出现了主动 Review 行为**，不能单凭一次 trace 断言该 flow 已训练进 GLM-5.2 权重。

### 2026-06-26 / 07-09：GPT-5.6 从限量预览到 GA

OpenAI 于 6 月 26 日发布 [GPT-5.6 limited preview](https://openai.com/index/previewing-gpt-5-6-sol/)，推出 Sol、Terra、Luna 三个层次；7 月 9 日通过 [GPT-5.6 正式公告](https://openai.com/index/gpt-5-6/) 全面开放。群聊中的集中转发因时区出现在 6 月 27 日和 7 月 10 日。

预览期，社区的第一反应集中在安全评估、METR 所说的作弊倾向、reward hacking 与 token efficiency。史料位置：[聊天记录 48980—49050 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48980)

GA 后，`Ultra` 的自动任务委派、拆解依赖、Sub-agent 与 Review 最受关注。群内有人将它概括为 “Fable + Delegation Mode + Subagents Team”，并据此提出 Harness 正在被模型或产品层内化。与此同时，负面反馈也没有消失：复杂逻辑 one/few-shot 仍会错，额度消耗很快，也出现 CLI 版本和可用性问题。史料位置：[聊天记录 52245—52305 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52245)、[52930—53018 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52930)

官方可以确认 `Ultra` 会自动委派给多个 Sub-agent；群内“数十或上百个 Agent”的运行记录属于个人数据点，不应扩写成官方固定规模。

### 2026-07-16 / 07-27：Kimi K3 作为章节尾声

Kimi K3 于 7 月 16 日进入产品、API 和 Kimi Code，[Kimi Code 更新记录](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)可核对该日期；7 月 27 日，[完整权重仓库](https://github.com/MoonshotAI/Kimi-K3)开放。官方[技术博客](https://www.kimi.com/blog/kimi-k3)给出的要点包括 2.8T 参数、KDA + AttnRes、原生视觉、1M Context 和长程 Coding。

群内从 7 月 16 日晚开始集中试用。早期反应很兴奋，也立刻出现反例：有人称 K3 可与一线闭源模型竞争，也有人提醒 K2.6/K2.7 的宣传与体感曾有落差，Kimi Code 本身仍难用。史料位置：[聊天记录 56880—56960 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56880)

K3 的时间晚于本章主要叙事，可以作为尾声说明：H3 形成后，社区很快进入“不同模型分别承担 Plan、Build、Review，再由开放 Harness 组合”的阶段。它不应被提前塞进“6 月底模型交替发布”的同一天线。

## 六、可以直接引用的匿名化群聊片段

以下原话经过最小清理，只去除 OCR 断行、姓名和无关上下文：

### Human Harness

> “agent harness 让 AI 更强大，human harness 让人类更负责。”
>
> ——群友，2026-05-12

来源：[聊天记录 19945—19960 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19945)

### Coach Mode

> “我想要的是 Plan-time Human Verification，或者 Interactive Plan Comprehension Gate。”
>
> ——群友，2026-05-13

来源：[聊天记录 20410—20429 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20410)

### 三代 Roadmap

> “H1: A flow that works. H2: A platform/language that human build/test flow. H3: An automation system that let agents builds its own flow.”
>
> ——群友，2026-05-16

来源：[聊天记录 21885—21915 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21885)

### 人类成为系统瓶颈

> “人类输出 token 的速度已经成为了核心 bottleneck。”
>
> “‘我’才是系统的瓶颈。”
>
> ——群友，2026-05-24

来源：[聊天记录 26005—26049 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:26005)

### 心智负担的迁移

> “AI 只是把 Implementation 的心智负担切分到 Arch 和 DV 上了。人类心智消耗的需求并没有减少，反而密度更高了。”
>
> ——群友，2026-06-06

来源：[聊天记录 34672—34708 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:34672)

### Monitor Loop 的起点

> “之前 Humanize 是做代码审查的监工，现在说的是找一个第三方工具做‘进度’的监工。”
>
> “Worker context 是一直在压缩的，监工没在压缩。”
>
> ——群友，2026-06-06

来源：[聊天记录 34718—34749 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:34718)

### 构建、监控与审计

> “带验证的长程循环，有固化的 workflow 做流程锚定，带全局视野的监控循环。”
>
> “构建循环 + 监控循环 + 审计循环，三驾马车。”
>
> ——群友，2026-06-12

来源：[聊天记录 39384—39393 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:39384)

### Monitor 的职责边界

> “它是个进度监控，不是个代码审查，也不是 building loop。”
>
> “它本质的作用是：感受时间流逝，在大方向上保持正轨，帮助内部 loop 跳出局部最优。”
>
> ——群友，2026-06-13

来源：[聊天记录 40381—40400 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40381)

### H3 与 mutable workflow

> “Dynamic workflow 的意思是：我拿 JS 固化一个流程，跑在上面的 agents 是动态的；流程是静态的。”
>
> “H3 的核心增量特性是：允许 Agent 改动正在运行中的工作流。”
>
> ——群友，2026-06-02

来源：[聊天记录 32248—32301 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32248)

### 认知过载

> “所以其实还是一个 cognition overload 的问题？必须确保里面的每个细节都自己确定好了之后，才能执行。”
>
> ——群友，2026-06-18

来源：[聊天记录 45831—45866 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45831)

### Flow 的准入标准

> “我曾经放了 9 个 OMH 内置的 flow，但是发现里面有一两个 flow 似乎有点 bug，然后我就一波全部 rollback 了。我本地需要连续运行 80 小时确定无问题，再升格为 OMH 内置 flow。”
>
> ——群友，2026-06-18

来源：[聊天记录 45897—45918 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45897)

## 七、第三章写作时应统一的勘误表

| 草稿中的说法 | 核查后的建议 |
|---|---|
| Human Awareness Cognitive Load | 群聊未出现；正文写“人类认知同步负担”，并注明来自 `cognition overload` 等讨论的编辑归纳 |
| OmniPi | 改为 Oh My Pi（OMP） |
| H2 基于 HTML 接入 OmniPi | H2 先有 HTML runtime；随后 H2/H3 思路迁入 OMP，形成 Oh My Humanize |
| Anthropic 在 5 月 28 日把 Dynamic Workflow 集成到 Cloud | 改为“Anthropic 于 5 月 28 日发布 Claude Code Dynamic workflows；北京时间为 5 月 29 日” |
| Dynamic workflows 会在运行中自我修改 | 官方机制是按任务生成 JS workflow；生成后的流程本身静态 |
| H3 允许 Agent 任意修改正在运行的 workflow | 早期原型支持 live graph revision；6 月中旬生产语义收紧为审批、停止、checkpoint、freeze、restart |
| Monitor Loop 就是 H1 的 `humanize monitor` | H1 monitor 是 Goal Tracker/日志状态面板；6 月的 Monitor Loop 是独立 Agent 对长程任务做语义进度监督 |
| Claude `/loop` 自带 Agent 监工能力 | `/loop` 只提供会话内定时重复 prompt；偏航判断、取证、授权和 steer 策略来自社区实现 |
| 群聊中的 `/remote` 是官方命令 | 官方命令是 `/remote-control` 或 `/rc`；`/remote` 应视为口语或 OCR 简写 |
| Monitor Loop 已内置于 Humanize 3.0 / OMH | 6 月 17 日已有独立可执行 Skill，并用于本地 H3 flow 测试；未找到进入 Humanize 或 OMH 主线的证据 |
| Monitor Loop 会持续向 Worker 注入反馈 | 同期实践大部分 tick 为零注入，以汇报为主；多数 steer 需要人批准，自动注入仅限白名单 |
| Monitor Loop 等同于 Code Review | 群聊明确将其定义为进度监督；它关注时间、主线与局部最优，代码审查是另一条循环 |
| 6 月中旬 H3 开启内测 | 改为“开源原型进入公开试用；尚无正式 Release” |
| H3 一直内置 9 个 flow | 6 月 15 日快照确有九个顶层示例；6 月 16 日起未经验证的 flow 被 demote/rollback |
| KDA 主要由 NVIDIA 内部使用 | 未获官方证据；可写 MIT HAN Lab 的 KDA 用于 NVIDIA Track kernel contest，并有 NVIDIA 工程师参与社区 |
| KDA 已有公开 SOL-Bench 全面领先榜单 | 群内自报，尚未找到公开快照；公开可核对的是 FlashInfer Competition 三个赛道第 1/2/3 名 |
| 龙虾（Humanize） | 龙虾/小龙虾在本文语境中指 OpenClaw |
| 6 月底 GPT-5.6 预览 | 准确日期为 6 月 26 日限量预览，7 月 9 日 GA |
| 6 月 16 日 GLM-5.2，支持 1M Context | 基本准确；群内 6 月 13—14 日属于提前传播或灰度体验 |
| 随后 Kimi K3 | 补日期：7 月 16 日产品/API，7 月 27 日完整权重；放章节尾声更合适 |

## 八、一手资料索引

### Humanize / H2 / Coach

- [PolyArch/humanize](https://github.com/PolyArch/humanize)
- [H2 POC 提交 `3fccb60`](https://github.com/PolyArch/humanize/commit/3fccb60c11332fb322a295db0583432416c7cf07)
- [Coach Mode PR #159](https://github.com/PolyArch/humanize/pull/159)
- [Coach Mode 首个实现 `e69b239`](https://github.com/PolyArch/humanize/commit/e69b239770df68141939721f07526ee82ada7c5f)

### Pi / OMP / OMH / H3

- [Pi](https://github.com/earendil-works/pi)
- [Oh My Pi](https://github.com/can1357/oh-my-pi)
- [Oh My Humanize 当前仓库](https://github.com/humanfia/oh-my-humanize)
- [Oh My Humanize 最初的 PolyArch fork](https://github.com/PolyArch/oh-my-humanize)
- [Workflow graph patch API](https://github.com/humanfia/oh-my-humanize/commit/26b082f580f6942492b89f26650d1d67bc6d9e22)
- [Live graph revision scheduler](https://github.com/humanfia/oh-my-humanize/commit/fccda309629d02ee033f06819a2554d8b6a8ca22)
- [Mutable workflow runtime](https://github.com/humanfia/oh-my-humanize/commit/eea3778e2e5ba7fa38f90eae6da4d9d9461a1474)
- [拒绝 active-run patch，转向 change request](https://github.com/PolyArch/oh-my-humanize/commit/eb78a8eacc905434dd340f01a0f1ea8fa5d90276)
- [Practical built-ins](https://github.com/humanfia/oh-my-humanize/commit/aaf46428db15a2cfe2b18f9eae9a61827f47d1c1)
- [Primitive built-ins / 九个顶层 flow 快照](https://github.com/humanfia/oh-my-humanize/commit/45eece01b8709184906474dec9477493c6da394c)
- [6 月 15 日公开试用快照](https://github.com/PolyArch/oh-my-humanize/tree/39de07716d255a0de489d222afdbcc84240520bb)
- [Demote unverified built-in flows](https://github.com/humanfia/oh-my-humanize/commit/21e56a0892beeffdab258157860ec9d94f25e378)
- [迁移到 humanfia](https://github.com/PolyArch/oh-my-humanize/commit/04e0229d474b7258f8bf36efd0d86f6036857456)

### Dynamic workflows

- [Anthropic：Introducing Dynamic workflows in Claude Code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)
- [Claude Code 2.1.154](https://github.com/anthropics/claude-code/releases/tag/v2.1.154)

### Monitor Loop / 长程监督

- [Claude Code 2.1.51：Remote Control](https://github.com/anthropics/claude-code/releases/tag/v2.1.51)
- [Claude Code Remote Control 官方文档](https://code.claude.com/docs/en/remote-control)
- [Claude Code 2.1.110：Push tool](https://github.com/anthropics/claude-code/releases/tag/v2.1.110)
- [Claude Code 2.1.71：`/loop` 与 cron scheduling](https://github.com/anthropics/claude-code/releases/tag/v2.1.71)
- [Claude Code scheduled tasks 官方文档](https://code.claude.com/docs/en/scheduled-tasks)
- [Codex 0.128.0：持久化 `/goal`](https://github.com/openai/codex/releases/tag/rust-v0.128.0)
- [H1 Goal Tracker 定义快照](https://github.com/PolyArch/humanize/blob/0ec921a36b4365df503511c5567bbd3e02db0df5/commands/start-rlcr-loop.md)
- [H1 `humanize monitor` 实现快照](https://github.com/PolyArch/humanize/blob/0ec921a36b4365df503511c5567bbd3e02db0df5/scripts/humanize.sh)
- [CGCR 社区原型](https://github.com/JerryLookupU/humanize-cgcr)
- [CGCR 首个实现 `6de5eb1`](https://github.com/JerryLookupU/humanize-cgcr/commit/6de5eb16c9ae5e59e8f78900d4de3c90a63166b2)
- [Humanize CGCR PR #205（未合并）](https://github.com/PolyArch/humanize/pull/205)
- [Humanize `monitor-claude-goal` Issue #213](https://github.com/PolyArch/humanize/issues/213)
- [`monitor-codex-goal` 首个公开实现 `ec9cd9e`](https://github.com/SihaoLiu/skills/commit/ec9cd9e2733f28d93bbf66c37ef58722cf6390ce)
- [`monitor-codex-goal` Skill 原始快照](https://github.com/SihaoLiu/skills/blob/ec9cd9e2733f28d93bbf66c37ef58722cf6390ce/monitor-codex-goal/SKILL.md)
- [`watch-codex-goal` liveness 兜底 `671516c`](https://github.com/SihaoLiu/skills/commit/671516c91d41417aeefd24b097368412f6a5205b)

### KDA

- [MIT HAN Lab：Kernel Design Agents](https://github.com/mit-han-lab/kernel-design-agents)
- [MLSys 2026 FlashInfer Contest 开源材料](https://github.com/mit-han-lab/mlsys2026-flashinfer-contest)
- [MLSys 2026 FlashInfer Contest 最终方案快照](https://github.com/mit-han-lab/mlsys2026-flashinfer-contest-solution)

### 同期模型

- [智谱：GLM-5.2](https://z.ai/blog/glm-5.2)
- [GLM-5.2 模型卡](https://huggingface.co/zai-org/GLM-5.2)
- [GLM-5.2 发布提交](https://github.com/zai-org/GLM-5/commit/0e29acc8884b689ce2ec0e1abafecb160defb469)
- [OpenAI：GPT-5.6 limited preview](https://openai.com/index/previewing-gpt-5-6-sol/)
- [OpenAI：GPT-5.6](https://openai.com/index/gpt-5-6/)
- [Moonshot AI：Kimi K3](https://www.kimi.com/blog/kimi-k3)
- [Kimi Code 更新记录](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)
- [Kimi K3 完整权重](https://github.com/MoonshotAI/Kimi-K3)

## 九、建议第三章采用的叙事边界

这一章可以把 Humanize 3.0 写成一次连续的重心移动：H1 已经给出能工作的 RLCR；H2 把经验拆成可组合的 flow 原语和执行平台；模型厂商随后把任务级工作流生成做进产品；H3 继续追问，运行反馈能否反过来改变 flow，以及这种变化怎样获得人类批准、保留状态、接受验证。

Monitor Loop 正好位于这条演进的中间。它没有先等待一个完整平台出现，而是把 `/loop`、`/goal`、Remote Control、transcript 和 tmux 组合起来，让独立 Agent 从长时间尺度观察另一个 Agent。6 月的实践已经证明这种监督层可以运行，也很快暴露了人的注意力上限、误判、hook 冲突和审批成本。它更适合写成 H3 形成期的一项社区实践，以及 Human Harness 如何承担信息压缩和认知同步的具体例子。

与这条技术线并行的，是人的位置发生变化。Coach Mode 在 Plan 生成过程中建立理解关卡，6 月的讨论又把输入带宽、心智密度、隐性条件和“人跟不上”连成同一个问题。由此提出 Human Harness 很自然：它让人保有理解、判断和否决能力，也让 Agent 的高吞吐产出能够被人类真正接住。

需要避免把这段历史写成线性胜利。H2 的 HTML flow language 很快被自己否定；H3 的 live mutation 很快加上冻结和重启；九个内置 flow 很快又被回退。恰恰是这些来回校正，让 Humanize 3.0 的轮廓变得清楚：Agent 可以参与创造 workflow，生产系统仍要通过权限、证据、checkpoint 与人工认知同步来守住边界。
