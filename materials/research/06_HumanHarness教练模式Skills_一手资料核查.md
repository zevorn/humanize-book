# Human Harness：促进代码库理解与认知同步的 Skills 与工具

> 核查日期：2026-08-06（Asia/Shanghai）。
>
> 本稿服务于第三章关于 Humanize Coach Mode / Human Harness 的讨论。它只记录
> 仓库 README、SKILL.md、官方文档和 GitHub REST API 能够直接支持的事实；
> “适合接入 Humanize”属于基于这些事实的编辑建议，不把它写成项目作者的原话。

## 0. 名称勘误与范围

聊天记录和本次委托中出现了“understand anything”“matccpook / MCPook”“grill
me”“tech skill”等写法。

- `understand anything` 对应的官方仓库是
  [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)。
  README 说明它最初由 `Lum1104` 创建，现由 Egonex 维护，并把自己定位为
  “让人看懂代码”的开源项目。
- 在 GitHub 官方仓库搜索中没有找到名为 `MCPook` 或 `matccpook` 的对应项目。
  结合 `grill-me` 的官方来源，本稿按 **Matt Pocock** 及其
  [`mattpocock/skills`](https://github.com/mattpocock/skills) 处理。这里的
  `mattpocock` 很可能是聊天记录里“matccpook”的误写；若作者记得另一个具体
  仓库，后续可以替换本条。
- “tech skill”没有对应的唯一官方项目名称。本稿把它拆成两类：一类是
  Matt Pocock 仓库中的工程技能（`domain-modeling`、`code-review`、
  `improve-codebase-architecture`、`teach` 等），另一类是 GitHub 官方维护的
  `awesome-copilot` 技能集合。

GitHub Star 会随时间变化，下面的数量是 2026-08-06 通过官方 REST API 读取的
快照，作用是标记社区传播度，不代表质量、正确性或与 Humanize 的兼容性。

## 1. 先把 Human Harness 拆成三种能力

Humanize 的 Coach Mode 关心的核心问题是：Agent 运行得越远，人能否继续理解
它在做什么、为什么这样做、哪些决定仍然需要人承担。调研后可以把外部工具分
成三层：

1. **事实层（evidence）**：把代码、依赖、调用关系、变更影响和历史变成可追
   溯资料，减少“模型讲得像真的”造成的错觉。
2. **认知层（understanding）**：通过提问、预测、主动回忆、术语澄清和小步反
   馈，验证人是否真的理解，而非只看过一段总结。
3. **责任层（gates）**：在设计、计划、实现、测试、Review、发布之间设置人类
   可读的检查点，把“我同意了”变成“我能解释、能反驳、能承担”。

这三层正好对应 Humanize 2.0 的方向：Plan 前后不仅做一次理解测试，还要在
复杂任务的关键节点维持人类对产出的认知同步。

## 2. 重点项目与原始资料

### 2.1 Understand Anything：把整个仓库变成可探索的知识图

**项目**：[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)

**传播度快照**：77,671 stars、6,522 forks（[GitHub REST API 仓库元数据](https://api.github.com/repos/Egonex-AI/Understand-Anything)，2026-08-06）。

**官方实现和能力**：

- 它以 Claude Code Plugin 的形式运行多 Agent 分析流水线，提取文件、函数、
  类和依赖，生成可交互的知识图；原始 README 还提供 Codex、Cursor、Copilot、
  Gemini CLI 等平台的安装方式。
- Dashboard 支持结构图、业务域图、引导式 Tour、模糊/语义搜索、Diff Impact
  Analysis、按架构层分组，以及面向不同人群的 Persona-Adaptive UI。
- 通过 `/understand-chat`、`/understand-explain`、`/understand-diff`、
  `/understand-onboard`、`/understand-domain` 等入口，把“我不懂这个仓库”拆成
  可重复的提问、讲解、影响分析和入门流程。
- 首次 `/understand` 会分析整个代码库，官方明确提示大型项目可能消耗大量
  Token；后续默认增量分析，只重新处理变更文件。

以上内容见项目的
[README 能力和安装说明](https://github.com/Egonex-AI/Understand-Anything#readme)，
尤其是 Features、Quick Start、Keep learning 小节。

**与 Coach Mode 的契合点**：

- 在进入 `Candidate Plan` 之前，先生成一份可点击的架构地图，把教练模式的
  讨论对象从“模型认为的结构”拉回实际文件、符号和依赖。
- 在每个计划切片上调用 Diff Impact，让人回答“这个变更会影响哪些路径”，再
  进入 Build；这比单纯问“你理解了吗”更容易暴露理解缺口。
- 让人选择 Guided Tour 或业务域图作为 Plan 的阅读材料，再开始理解检查；这
  可以把 Coach Mode 从问答窗口扩展成可视化学习界面。

**限制与风险**：

- 初次全仓库分析成本很高，不能无条件放在每个 Stop Hook 上；应在仓库初次
  建图、重大结构变化或用户明确要求时运行，普通循环使用增量结果。
- 图中的摘要和关系解释仍然有模型生成部分；图是证据导航层，不是架构真相。
  Coach Mode 需要保留文件路径、符号和命令输出，让人可以回到源码复核。
- README 没有把“人必须批准才能继续”作为内建门槛，因此它更像认知基础设施，
  需要由 Humanize 的 Coach Loop 决定何时停下并要求人确认。

### 2.2 Matt Pocock / skills：把工程基本功包装成可调用的教练流程

**项目**：[mattpocock/skills](https://github.com/mattpocock/skills)

**传播度快照**：205,109 stars、17,711 forks（[GitHub REST API 仓库元数据](https://api.github.com/repos/mattpocock/skills)，2026-08-06）。

仓库 README 把它定义为“给真实工程师的 Skills”，并明确强调可组合、可修改，
目标是修复 Agent 与人之间的误解、上下文丢失、缺少反馈和代码腐化等问题。
README 的工程技能表见
[Skills for Real Engineers](https://github.com/mattpocock/skills#readme)。

#### `grill-me`：先把隐含决策说出来

[官方 SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)
只保留很薄的一层：调用 `/grilling`。详细的工作方式写在
[grill-me 文档](https://github.com/mattpocock/skills/blob/main/docs/productivity/grill-me.md)：

- 一次问一个问题，沿着决策树逐枝推进；前置决定没有解决，不进入后续问题。
- 问题如果可以由代码库回答，Agent 先去读代码，避免把事实问题丢给人猜。
- 每个问题带一个建议答案，让人针对具体方案反驳，而不是面对空白输入。
- `grill-me` 默认无状态，不写文件；结果是对话里变清楚了的理解。若希望留下
  记录，应使用 `grill-with-docs`。

**Coach Mode 用法**：把它放在 `First-pass Analysis` 和 `Candidate Plan` 之间，
只让它承担“暴露决策”的工作；每轮结束时由 Humanize 检查是否已经能解释关键
选择，再允许 Plan 继续。无状态是它的优点，也意味着 Humanize 必须另存摘要或
ADR，不能把这次理解当成已经沉淀的团队知识。

#### `grill-with-docs` 与 `domain-modeling`：把认知同步写进仓库

- [`grill-with-docs`](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md)
  的官方描述是：同样的持续追问，同时使用 `/domain-modeling`，在过程中创建
  ADR 和术语表。
- [`domain-modeling`](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md)
  要求主动挑战术语、设计边界场景、把解决的词义及时写入 `CONTEXT.md`，把难以
  逆转且存在权衡的决定写入 `docs/adr/`，并检查用户的描述是否与代码一致。

这对 Humanize 很有价值：`CONTEXT.md` 可以作为人和 Agent 的共享词典，ADR 可以
作为 Coach Mode 的长期记忆。计划反复执行时，教练不必每次从零解释“这个词在本
项目里是什么意思”，但仍然要在发现代码与叙述不一致时停下来让人裁决。

#### `teach`：把“理解”做成跨 Session 的训练

[`teach`](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md)
把当前目录当成教学工作区，用 `MISSION.md`、`RESOURCES.md`、`learning-records/`、
`lessons/` 和 `reference/` 保存学习状态。官方文档强调：知识需要高信任资料，
能力需要交互练习，长期记忆依靠检索、间隔和反馈；每一课都要对应一个具体学习
目标，并保留来源链接。

**Coach Mode 用法**：当复杂任务的认知负担超过一次 Plan 能承受的范围时，把
“理解整个仓库”切成短课：一课只讲一个数据流、一个模块或一个失败案例，下一课
先让人回忆上一课，再继续任务。这样 Human Harness 不只在阻止错误，也在积累人
的独立能力。

#### `improve-codebase-architecture` 与 `code-review`：把架构和交付质量外显

- [`improve-codebase-architecture`](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md)
  先根据近期变更、`CONTEXT.md` 和 ADR 探索代码库，再输出带 Before/After 图的
  HTML 报告，列出模块变浅、耦合泄漏、难测试等候选；用户选择一个候选后才进入
  `/grilling`。它可以充当 Coach Mode 的“架构观察阶段”，但不能让它自动把所有
  候选改掉。
- [`code-review`](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md)
  把 Review 分成 Standards 与 Spec 两条线，并用并行子 Agent 让一条线的结论
  不污染另一条线。Humanize 可以把这两份结果汇总给人，要求人回答“实现是否符
  合意图”和“代码是否符合工程约束”两个不同问题。

### 2.3 learn-codebase：最贴近“人要真的会解释”

**项目**：[ktaletsk/learn-codebase](https://github.com/ktaletsk/learn-codebase)

**传播度快照**：35 stars、1 fork（[GitHub REST API 仓库元数据](https://api.github.com/repos/ktaletsk/learn-codebase)，2026-08-06）。

它的 Star 远低于前面的项目，但和 Human Harness 的问题高度贴合，因此单独保留。
官方 README 将它称为“反 Vibe Coding 的技能”：

- 不马上给出代码，而是先让人预测行为，再展示答案；通过苏格拉底式提问和主
  动回忆，检查人是否能用自己的话追踪数据流。
- 记录概念掌握度、开放问题、间隔复习队列、Aha Moment 和 Session Log，写入
  `.claude/learning-journal.md`。
- 它的优化目标是形成心智模型，而非尽快完成任务；官方明确提醒，已经熟悉仓库
  且只想快速打补丁时，应回到普通 Agent 流程。

资料见 [项目 README 的 Why、How It Works 和 Learning Journal](https://github.com/ktaletsk/learn-codebase#readme)。

**与 Coach Mode 的契合点**：可以把“理解检查”从一次性选择题改成三步循环：
预测 → 读取证据 → 用自己的话复述。Humanize 只在复述与源码、测试和架构图吻合
时放行。它提供了认知同步的教学模型，适合作为 H2 Coach 的交互参考。

**限制**：官方只明确测试了 Claude Code，其他兼容 Agent 仍属未完全验证；它依赖
人认真回答问题，速度会低于直接让 Agent 总结；学习日志也需要纳入团队的隐私和
版本管理策略。

### 2.4 Superpowers：把人类批准放进完整开发流程

**项目**：[obra/superpowers](https://github.com/obra/superpowers)

**传播度快照**：267,348 stars、23,888 forks（[GitHub REST API 仓库元数据](https://api.github.com/repos/obra/superpowers)，2026-08-06）。

官方 README 把它定义为由可组合 Skills 组成的软件开发方法论。它的流程是：

1. Agent 先退一步追问用户真正想做什么；
2. 从对话中提炼规格，并以短块形式展示，让人有机会阅读和确认；
3. 人确认设计后，生成实现计划；
4. 用户说“go”后进入 Subagent-driven development，每个任务都检查和 Review，
   可以在计划内运行较长时间。

这些事实来自 [Superpowers README 的 How it works](https://github.com/obra/superpowers#how-it-works)。

**与 Humanize 的关系**：它可以作为 Coach Mode 的外部对照，尤其适合观察“设计
批准”“分片计划”“子 Agent 执行”“二次 Review”这几种门。Humanize 可以借鉴它
的节奏，但仍然保留自己的 RLCR 和 Coach 语义，不直接把完整方法论替换进来。

**限制**：Superpowers 的方法论很完整也很有主张，可能和已有 Humanize Flow、
团队目录结构或模型路由重叠；如果把所有门都打开，小改动也会承担较高的交互成本。
人仍然需要检查它是否真的读懂了仓库，而不能因为它生成了规格就视为理解完成。

### 2.5 gstack：把产品、架构、设计、Review 和 QA 分角色

**项目**：[garrytan/gstack](https://github.com/garrytan/gstack)

**传播度快照**：126,482 stars、19,023 forks（[GitHub REST API 仓库元数据](https://api.github.com/repos/garrytan/gstack)，2026-08-06）。

官方 README 把它描述为 23 个面向不同职责的工具：CEO、设计师、工程经理、
Review、QA 和发布角色等。它把流程明确写成
`Think → Plan → Build → Review → Test → Ship → Reflect`，并规定上游产物交给下游：
`/office-hours` 写设计文档，`/plan-ceo-review` 和 `/plan-eng-review` 继续挑战，
`/review` 查生产问题，`/qa` 做真实浏览器验证。[README 的流程表和快速开始](https://github.com/garrytan/gstack#the-sprint)
给出了这些关系。

`/office-hours` 的原始模板还要求围绕痛点、用户、替代方案和范围进行强制提问；
`/plan-eng-review` 关注数据流、状态机、错误路径和测试矩阵。见
[office-hours SKILL.md.tmpl](https://github.com/garrytan/gstack/blob/main/office-hours/SKILL.md.tmpl)。

**与 Human Harness 的契合点**：它展示了把“人类需要理解的事情”按职责拆开：
先确定是否值得做，再确认工程结构，再看设计，再做代码 Review 和 QA。Humanize
3.0 的 Dynamic Workflow 可以把这些角色当成可选 Flow，而 Coach Mode 负责在角色
切换点收集人类确认。

**限制**：它的默认体验高度围绕 Claude Code 和自身的命令目录，虽已提供 Codex、
Cursor、OpenCode 等安装目标，仍需要逐项检查宿主兼容性；23 个角色对小改动可能
过重，且角色输出不自动等于事实，需要保留源码和测试证据。

### 2.6 Addy Osmani / agent-skills：明确的 Define—Plan—Build—Verify—Review—Ship

**项目**：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

**传播度快照**：82,019 stars、8,826 forks（[GitHub REST API 仓库元数据](https://api.github.com/repos/addyosmani/agent-skills)，2026-08-06）。

官方 README 将 Skills 排成软件生命周期：`DEFINE → PLAN → BUILD → VERIFY →
REVIEW → SHIP`，并提供 `/spec`、`/plan`、`/build`、`/test`、`/review`、`/ship` 等
命令。[生命周期图和命令表](https://github.com/addyosmani/agent-skills#readme)还说明：
`/build auto` 可以在一次批准计划后连续执行，但每个任务仍然需要测试和提交，并
在失败或高风险步骤处暂停。

**与 Coach Mode 的契合点**：这提供了一个很清楚的“批准一次、验证多次”模型：人
主要批准 Spec/Plan，Agent 执行细节，系统在 Test/Review/风险步骤重新打断。这和
Humanize 想减少人被困在每个 Check 点的方向一致。

**限制**：它偏重生命周期自动化和质量门，对“人能否解释代码”没有
`learn-codebase` 那样的主动回忆机制；因此应把它放在认知检查之后，不能拿它替代
Coach Mode 的理解阶段。

### 2.7 codebase-memory-mcp：给教练提供结构化事实底座

**项目**：[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

**传播度快照**：37,630 stars、2,991 forks（[GitHub REST API 仓库元数据](https://api.github.com/repos/DeusData/codebase-memory-mcp)，2026-08-06）。

**官方实现和能力**：

- 用 Tree-sitter AST 和混合 LSP 类型解析建立持久知识图，覆盖 158 种语言，提供
  函数、类、调用链、HTTP 路由、跨服务链接等结构信息。
- 提供架构概览、ADR 管理、Git Diff Impact、调用图、死代码检测、语义搜索、
  结构搜索和 Cypher 查询等 MCP 工具；代码库索引和查询都在本地运行。
- README 报告了项目自测结果：在 31 个真实仓库上，结构化查询相对于逐文件探索
  声称可减少 Token 和工具调用。这里的数字是项目自己的基准，不能当成普遍保证。
- 它明确说明自身是结构分析后端，不内置 LLM，由已经在对话中的 Agent 把自然语言
  翻译成图查询，再把结构结果解释给人。

原始依据见 [README 的 Why、How It Works 与 Features](https://github.com/DeusData/codebase-memory-mcp#readme)。

**与 Coach Mode 的契合点**：让 Coach 在询问“你认为这次改动影响哪里”时，先调
用 `detect_changes`、`trace_path` 或 `get_architecture`，再把人回答和结构事实对
照。它适合作为 Understand Anything 的轻量、可查询底座，减少重复扫描和 Token 消耗。

**限制**：索引不是实时真相，必须确认项目是否重新索引；工具只给结构数据，意义
和责任仍需要人和 Agent 共同判断；安装程序会写入 Agent 配置，使用前要审查脚本、
版本和权限。

### 2.8 GitHub / awesome-copilot：可直接拼装的代码库理解技能

**项目**：[github/awesome-copilot](https://github.com/github/awesome-copilot)

**传播度快照**：37,489 stars、4,710 forks（[GitHub REST API 仓库元数据](https://api.github.com/repos/github/awesome-copilot)，2026-08-06）。

GitHub 官方仓库的 [Agent Skills 说明](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md)
明确了技能的形态：每个技能是带 `SKILL.md` 的自包含目录，可以附带脚本、模板和
参考资料，并按需加载（progressive disclosure）。其中几项特别适合作为 Human
Harness 的材料：

| Skill | 官方定义的主要工作 | 可放入 Coach Mode 的位置 |
| --- | --- | --- |
| [`acquire-codebase-knowledge`](https://github.com/github/awesome-copilot/blob/main/skills/acquire-codebase-knowledge/SKILL.md) | 读取本地仓库，生成 `STACK.md`、`STRUCTURE.md`、`ARCHITECTURE.md`、`CONVENTIONS.md`、`INTEGRATIONS.md`、`TESTING.md`、`CONCERNS.md`；每条结论要有证据，未知标 `[TODO]`，需要人决定的标 `[ASK USER]`。 | Coach 的事实底稿和首次认知同步，尤其适合新人或陌生仓库。 |
| [`doc-and-modernize`](https://github.com/github/awesome-copilot/blob/main/skills/doc-and-modernize/SKILL.md) | Documentation 模式从本地代码生成可引用的架构文档；Modernization 模式在此基础上生成分阶段、安全梯度计划。 | 把“先理解、后改造”变成显式 Flow；文档是 Plan 的证据基线。 |
| [`code-tour`](https://github.com/github/awesome-copilot/blob/main/skills/code-tour/SKILL.md) | 生成按角色定制的 `.tour`，每一步链接真实文件和行号，支持新人、架构师、PR Reviewer、安全 Reviewer 等角色。 | 把理解测试变成可复用的交互式导览，而不是一段长总结。 |
| [`repo-story-time`](https://github.com/github/awesome-copilot/blob/main/skills/repo-story-time/SKILL.md) | 从提交历史生成技术摘要和仓库演化故事。 | 让人理解“为什么变成今天这样”，补足只看当前代码的盲区。 |
| [`architecture-blueprint-generator`](https://github.com/github/awesome-copilot/blob/main/skills/architecture-blueprint-generator/SKILL.md) | 识别技术栈、架构模式、组件边界、数据流，并生成架构蓝图和图。 | 作为 Arch/Coach 的候选设计材料，但必须把理论模式和实际代码分开。 |
| [`review-and-refactor`](https://github.com/github/awesome-copilot/blob/main/skills/review-and-refactor/SKILL.md) | 按项目说明 Review 并重构代码。 | 放在 Builder—Reviewer 之后，要求人阅读分级问题和改动理由。 |
| [`security-review`](https://github.com/github/awesome-copilot/blob/main/skills/security-review/SKILL.md) | 追踪数据流和组件交互，检查注入、权限、密钥、依赖和业务逻辑风险。 | 给 Coach 增加“责任与信任”分支，避免只检查功能正确。 |

**限制**：这是一个社区集合，技能质量、维护状态和权限模型各不相同；不要因为
项目本身是 GitHub 官方组织就默认每个第三方技能都可信。安装前要阅读
`SKILL.md`、脚本和依赖，固定版本，并按最小权限运行。

## 3. 面向 Humanize Coach Mode 的组合方案

下面是一套可以在现有 Humanize 1.0 / 2.0 上逐步试验的组合，不代表任何单个项目
的官方推荐：

### 阶段 A：建立证据底稿

1. 新仓库或重大重构时运行 `Understand Anything`，或运行
   `acquire-codebase-knowledge` / `doc-and-modernize`。
2. 对关键模块补一份 `codebase-memory-mcp` 图查询结果和文件路径。
3. 把结构、业务流、依赖和未决事实保存到 Coach 的输入目录；明确标出
   `[TODO]`、`[ASK USER]` 和“需要源码复核”的内容。

### 阶段 B：验证人的心智模型

1. 对设计意图用 `grill-me`，一次只问一个决策；人可以说“不知道”，不能只点
   “同意”。
2. 对陌生仓库或关键数据流用 `learn-codebase` 的预测 → 证据 → 复述循环。
3. 对术语和边界用 `grill-with-docs` + `domain-modeling`，把达成共识的词写入
   `CONTEXT.md`，把真正的架构权衡写入 ADR。
4. Coach Mode 记录每轮：已确认的事实、仍不确定的事实、人做出的决定、下次需
   复习的概念。没有这四类记录，就不要把“问过问题”当成同步完成。

### 阶段 C：批准计划，放行 Agent

1. 人先批准结构和切片，再让 Builder/Subagent 实现；可借鉴 Superpowers 的
   规格分块和 Addy Osmani 的“一次批准、逐任务验证”。
2. 对大型改动，先用 `improve-codebase-architecture`、`gstack /plan-eng-review`
   或 `architecture-blueprint-generator` 产生候选和图，人选定要深入的一项。
3. 进入 Humanize RLCR 后，Builder 负责实现，Reviewer 负责代码和测试证据，
   Coach 负责认知同步；三者输出不要混成一份“看起来已经完成”的摘要。

### 阶段 D：完成后留下可复用记忆

1. 对重要改动保存 ADR、`CONTEXT.md`、CodeTour 或仓库故事，方便下一个人和下
   一个 Agent 从事实开始。
2. 对反复出现的误解，把它变成新的 Coach 检查题、`learn-codebase` 学习记录或
   GitHub Skill，而不是每次在对话中临时补一句提示。
3. 只有在测试、Review、影响分析和人类解释都通过后，才把任务标成“完成”。

## 4. 一个更贴近 Humanize 的 Coach 检查单

可以把下面的检查单嵌入 `gen-plan --coach` 或后续的 Coach Flow：

| 检查节点 | Coach 给人的任务 | 可调用资料 | 放行条件 |
| --- | --- | --- | --- |
| 进入 Plan 前 | 用自己的话说清目标、范围、非目标和当前仓库中的相关模块。 | Understand Anything、`acquire-codebase-knowledge`、CodeTour | 关键路径和未知项有文件证据。 |
| Candidate Plan | 逐项回答“为什么选这个方案、还可以怎样做、代价是什么”。 | `grill-me`、`grill-with-docs`、`domain-modeling` | 人能指出至少一个取舍和一个待确认问题。 |
| 进入 Build 前 | 预测变更会影响哪些调用方、数据流、测试和部署面。 | `codebase-memory-mcp`、Diff Impact、架构图 | 预测与工具结果对齐，偏差被记录。 |
| 长程执行中 | 只在目标漂移、事实冲突、风险升级或认知断层出现时打断。 | `teach`、`learn-codebase`、Monitor Loop | 人能看懂当前状态和下一步；不要求逐个检查 Agent 调用。 |
| Review | 分开回答“实现符合意图吗”和“代码质量与安全过关吗”。 | Matt 的 `code-review`、GitHub `security-review`、gstack `/review` | 两条 Review 线都有证据，人确认关键风险。 |
| 完成后 | 解释这次改动、记录术语和不可逆决定，留下下一次可复用的材料。 | ADR、`CONTEXT.md`、CodeTour、`repo-story-time` | 未来读者可以从文档回到源码，不依赖原始对话。 |

## 5. 编辑结论：高 Star 只是入口，Human Harness 的核心仍是责任分配

这些项目共同指向一个变化：Agent 的能力已经从“写一段代码”扩展到扫描仓库、
生成架构、拆分任务、调度子 Agent、运行测试和维护文档。Human Harness 需要保留
人的三项工作：

- **给事实定边界**：哪些是源码证据，哪些是模型推断，哪些还不知道；
- **给设计作选择**：在备选方案、约束和代价之间做出可以解释的决定；
- **给结果负责任**：即使 Agent 运行了很久、调用了很多子 Agent，最终交付仍然
  要有人能说明它为何正确、风险在哪里、发生问题由谁处理。

从这个角度看，`Understand Anything` 和 `codebase-memory-mcp` 解决的是“看见并
追溯”，`grill-me`、`learn-codebase`、`teach` 解决的是“真的理解”，Superpowers、
gstack、Addy Osmani 的 Skills 以及 GitHub `awesome-copilot` 解决的是“把理解和
质量门嵌入流程”。Humanize Coach Mode 可以把三类能力编排到同一条 Flow 中，保
持 Humanize 1.0 的 RLCR，又把 Humanize 2.0 所说的人类认知同步落实为可观察的
证据、问题、复述和批准记录。

## 6. 资料与安全提醒

- [GitHub：About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)：
  GitHub 对 Skills 的定义、目录位置、按需加载和安装方式。
- [Agent Skills specification](https://agentskills.io/specification)：技能目录、
  `SKILL.md` 和兼容性约定。
- Skills 可以附带脚本、资源和工具调用；安装 GitHub 上的技能前，应审查源码、
  脚本、网络访问、写文件行为和依赖来源，固定 commit 或 release，先在隔离仓库
  试运行。星数只能说明传播度，不能替代安全审查、测试和人工批准。
- 对 Token 预算尤其要注意：Understand Anything 的首次全仓库分析、知识图构建
  和教学型长对话都可能消耗很多 Token。Humanize 应使用增量索引、按模块切分、
  本地模型或缓存结果，并把“人类注意力成本”与 Token 成本一起记录。
