# Humanize 社群 Agent 发展史：关键节点导览

这份导览服务于《Humanize 聊天记录：Agent 相关内容时间序初筛版》。它只标出值得继续分析的时间节点，不替群聊补写一条完整、必然的因果链。

## 阅读边界

- 原始群聊从 3 月 18 日开始。关于此前“去年 11 月至今年 1 月”的内容，来自群友在 5—7 月的回顾，不是同期聊天记录。

- 源文件标题没有标明年份；聊天截图和外部链接多次出现 2026。具体年份、产品发布日期和版本号，另由一手资料核查表确认。

- 群内所说的 Humanize `h1 / h2 / h3`，与仓库正式版本号 `1.x / 2.x / 3.x` 不宜未经核对直接画等号。记录中最清楚的一次定义是：h1 是能工作的 Flow，h2 是人构建与测试 Flow 的平台或语言，h3 是 Agent 构建或修改 Flow 的自动化系统。

- 原文没有出现 `AutoGPT` 这个名称；“龙虾”“小龙虾”“虾”主要指向 `OpenClaw`，后续又讨论了其 Agent Core `Pi`。二者与 AutoGPT 的历史关系需要分开核查。

## 外部历史坐标｜不是群聊同期内容

下面只列帮助理解群聊起点的一手资料。它们是行业背景，不代表 Humanize 社群当时已经讨论或接受了相关结论。

| 日期 | 外部事件 | 放进材料中的用途 |
| --- | --- | --- |
| 2023-03 | [AutoGPT 仓库](https://github.com/Significant-Gravitas/AutoGPT)出现 | 只能作为早期 autonomous agent 热潮的前史；不是本群所说的“龙虾” |
| 2024-11-25 | Anthropic 发布 [MCP](https://www.anthropic.com/news/model-context-protocol) | 解释后续“工具怎样接入 Agent”的基础设施背景 |
| 2025-02-24 | Anthropic 随 Claude 3.7 Sonnet 发布 [Claude Code 研究预览](https://www.anthropic.com/news/claude-3-7-sonnet) | Claude 较早建立终端 Coding Agent 的产品心智 |
| 2025-05-16 | OpenAI 发布 [Codex 云端 Coding Agent](https://openai.com/index/introducing-codex/)；公告同时回顾此前一个月发布的 Codex CLI | OpenAI 的追赶同时发生在模型、CLI、云端任务与隔离执行层 |
| 2025-10-16 | Anthropic 发布 [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | 解释后续 Skill、渐进加载和长期记忆讨论 |
| 2025-11 | [OpenClaw 仓库](https://github.com/openclaw/openclaw)建立 | 本群“龙虾”线索的项目背景；它定位为本地、跨消息渠道的个人 Agent，不等同 AutoGPT |
| 2025-11-24 / 11-26 | [Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5) 与 [长程 Agent Harness](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | 模型能力与进度文件、Git、上下文重置、增量推进被放进同一长程任务叙事 |
| 2025-12-18 | OpenAI 发布 [GPT-5.2-Codex](https://openai.com/index/introducing-gpt-5-2-codex/) | 对应群友后来反复提到的“12 月长程能力转折” |
| 2026-01-12 | [PolyArch/humanize](https://github.com/PolyArch/humanize) 建仓并提交 [Humanize v1.0.0](https://github.com/PolyArch/humanize/commit/888451dbe0baf71b006f03961b7eb06939c100bf) | Humanize 1.0 可核验的工程起点 |
| 2026-02-02 | OpenAI 发布 [Codex app](https://openai.com/index/introducing-the-codex-app/) | 多 Agent 工作台、Skills 与 Automations 进入官方产品 |
| 2026-02-05 | Anthropic 发布 [Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)、Agent Teams 与 [并行构建 C 编译器](https://www.anthropic.com/engineering/building-c-compiler) 实验 | 解释 3 月一开场就出现的 Agent Teams、并行与协调成本争论 |
| 2026-02-11 | OpenAI 发布 [Harness Engineering](https://openai.com/index/harness-engineering/) | 解释 3 月群内为何迅速把 Harness 与控制、机械规则和仓库约束联系起来 |

详细的来源日期、证据等级和疑点见[一手资料核查](../research/00_Agent发展史_一手资料核查.md)。

## 前史｜来自后期聊天的回顾

### 去年 11 月至今年 1 月：Humanize 第一阶段的形成

- 群友回顾“去年 11 月份开始搞 Humanize，1 月份搞出来”，同时承认最初视野仍集中在 Ralph Loop，还没有后来关于长程任务、Flow 和多人多 Agent 的完整设想。[原文 L19152](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19152)

- 另一段回顾把去年 11 月视为 Humanize 最早阶段，并说“当时只有 Ralph”。同段把 12 月 18 日的 GPT-5.2 视作模型长程能力的一个个人转折点。这是参与者的事后判断，应与官方发布日期和真实模型能力评测分开看。[原文 L47318](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47318)

- 7 月的再次回顾把 Opus 4.6 与 GPT-5.2 并列为个人工作方式的转折点，并提到 12 月的长程 Coding 个案、1—2 月的单 Prompt 项目，以及模型升级怎样迅速淘汰一批外部 Loop、Skill 和脚手架。[原文 L59770](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:59770)

## 3 月｜从模型搭配、长程 Loop 到多 Agent 拓扑

### 3 月 19 日：Claude 做 Build、Codex 做 Review；上下文成为显性问题

- 当时有人把 `B=Opus, R=Codex` 称作自己的 SOTA 组合。与此同时，群里已经在比较 Claude 与 Codex 阅读大型代码库、调试和长上下文压缩的差异。[原文 L112](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:112)

- Humanize 被用于把白天积累的 Plan 交给 Agent 过夜执行；但同一天也有人批评 Loop 只是“堆超级力工”，无法自动补上全局洞察。[原文 L112](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:112) [原文 L186](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:186)

- 在 Prompt、Spec 和自然语言歧义的讨论里，重点逐渐从“怎样问得更好”转向“怎样把需求、取舍和验收写成可追溯的文档”。[原文 L236](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:236)

### 3 月 20—21 日：Harness 被理解为控制系统

- 群内从“怎样 Review 一周生成的代码”推进到观测、验证、独立 Agent 审查，并提出“Harness 工程就是控制论”。[原文 L630](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:630)

- 同期转发 OpenAI 的 Harness Engineering 文章，重点讨论把工程原则编码成机械规则、后台扫描和可快速审查的改动，而不是让人持续清理 AI Slop。[原文 L789](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:789)

- 为减少初始计划的路径偏置，出现“Claude 与 Codex 独立产出计划，再合并后进入 gen-plan Loop”的实践。[原文 L821](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:821)

### 3 月 23—24 日：Agent Teams 与 Sub-agent 之争

- 群里围绕 Agent Teams、Sub-agent、Leader Context 瓶颈和探索任务展开长讨论。一次 22 个 Agent、约 3.5 小时、4.7 万行增量的个人案例，把注意力推向 `/batch`、Worktree 和集中汇总。[原文 L949](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:949)

- 判断从“怎样让 Agent 沟通”转向“怎样禁止不必要的通信”：Plan 不写实现代码、Worker 不自由聊天，边界应由 Tool Permission 实施，而不只依赖 Prompt。[原文 L1153](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1153)

- 次日继续讨论 Expert—Manager 拓扑、Worktree 隔离和 Review 粒度，并开始考虑把这套批处理并行移入 Humanize。[原文 L1249](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1249)

- 同期对 OpenClaw 的态度很分裂：它有很高热度，但有人直言代码质量差、看不出用途；相比之下，Humanize 被描述为能让人放心睡觉的 Coding Flow。[原文 L1520](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1520)

### 3 月 26 日以后：官方 Harness 与多 Agent 资料进入讨论

- Anthropic 的长程 Agent Harness 文章、Multi-agent 文章，以及 Humanize 的 PR/Issue 开始成为群内直接参考资料。讨论不再只靠经验口述，而开始对照产品实现和仓库变更。[原文 L2440](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:2440)

## 4 月｜Humanize 1.0 做减法，h2 转向 Flow 语言

### 4 月 2—3 日：PDBR 与最小工作流

- PDBR 把 Humanize 拆成 Plan、Delegate、Build、Review，并给出 `P - /loop { D - /batch { B - R } }`。[原文 L5700](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5700)

- Humanize 作者回顾曾设计超过 60 个 Agent 的复杂交互系统，失败后大量删除，只留下 Ralph Loop 和独立 Review。Zero Shared Session History、Curated Knowledge 与 Less is more 在这一时期被明确化。[原文 L5855](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5855)

### 4 月 10—16 日：长尾、二元震荡与 PID

- 群内先把 Reviewer 类比为控制系统中的传感器，随后观察到 Builder—Reviewer 的局部震荡与“长尾打地鼠”：约 20% 时间完成主体工作，剩余约 80% 时间用于让 Codex 完全认可；Builder 自身也呈现“前 20% 时间消耗约 80% Token”的分布。[原文 L7528](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:7528) [原文 L7618](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:7618) [原文 L8280](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:8280)

- 4 月 14 日，[PR #81](https://github.com/PolyArch/humanize/pull/81)把累计 Commit 与最近三轮记录加入 Reviewer 上下文，提交说明以 P/I/D 映射解释这次修改。后期群聊又重新解释过 P/I/D 的角色，因此正文应把 PID 保留为社区工程类比，不写成严格的控制算法实现。

### 4 月中旬：模型更替推动“模型无关”的 Humanize 2.0 设想

- 群里一边经历 Claude Opus 4.7、Codex 和国内模型的密集更新，一边讨论让 Humanize 摆脱对某个 CLI 或模型的绑定。1.17.x 被说成 Humanize 1.0 的最后一组版本，2.0 计划允许用户选择不同模型。[原文 L8990](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:8990) [原文 L12940](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12940)

- 国内模型开始被放进 Builder / Reviewer 组合中试用。讨论重点不是简单问“谁跑分高”，而是 Build、Review、长程收敛、价格和 Tool Calling 各自能否替换。[原文 L6970](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:6970) [原文 L12820](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12820)

- 外部发布节奏提供了清楚的时代坐标：[GLM-5.1](https://docs.z.ai/guides/llm/glm-5.1)（4 月 7 日）、[Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)（4 月 16 日）、[Kimi K2.6](https://www.kimi.com/blog/kimi-k2-6)（群内 4 月 21—22 日开始传播）、[GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)（4 月 23 日）和 [DeepSeek V4](https://api-docs.deepseek.com/news/news260424/)（4 月 24 日）在三周内接连进入视野。它们共同强化长程 Coding、工具调用和 Agent 能力，同时出现 Effort / Fast / Pro / Flash 分档、开放权重与 OpenAI/Anthropic API 兼容。这些特征直接提高了异构 Builder—Reviewer 与模型无关 Flow 的现实价值。

- 版本史需要分开记：4 月 21 日的 `1.17.x` 是 H1 最后版本线的路线声明；4 月 30 日 [1.16 合入 `main`](https://github.com/PolyArch/humanize/pull/51)；5 月 1 日 `dev` 分支更新到 1.17.0，后来没有形成 Tag、Release 或 `main` 合并。[版本提交](https://github.com/PolyArch/humanize/commit/f4e5721e344ef602a77cfb3511ec51b74e387120)

### 4 月 22—30 日：从 Prompt/Flow 转向语言、编译器和运行时

- `humz / hcc / hvm` 被提出：分别描述 Agentic Flow、把它编译为脚本与 Harness、再放入基础设施执行。[原文 L13255](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13255)

- 随后的讨论把 Codebase、Context、Prompt、State 和 Agent 节点放进 Development Flow Graph，提出类型、死 Agent、Goal Drift 和静态检查。[原文 L13960](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13960)

- `Agent = Model × Tool × Action × Permission` 与“LLM is the new processor / Agent Flow is the new code”在这一阶段出现。[原文 L14145](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14145)

- h2 被描述成 AgentVM 与 Flow 编程语言，但群里同时质疑 DSL、形式化和过度基础设施化。月底已有 MVP，却仍多次更换实现基础设施。[原文 L15438](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:15438) [原文 L16790](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16790)

## 5 月｜从 h2 到 h3，从自动化扩张转向人的掌控

### 5 月 1—6 日：Codex 把持续目标收进 Runtime

- [Codex CLI 0.128.0](https://github.com/openai/codex/releases/tag/rust-v0.128.0)于 4 月 30 日 UTC、北京时间 5 月 1 日发布 `/goal`，支持持久化 Goal、模型工具、Runtime 续跑以及暂停、恢复和清除。首发仍属于实验功能。[原文 L17231](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17231)

- 5 月 6 日，群友根据使用 Trace 认为 `/goal` 把 Build、Test、Review 融在连续推进里，并尝试直接输入 Humanize 生成的 Plan。这个结论属于社区体验；官方 Runtime 没有写死三个阶段。[原文 L17817](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17817)

### 5 月上旬：Build / Explore 分流，Memory 与 Worktree 暴露代价

- Agent 被类比为约束求解器；构建、维护和探索被认为需要不同的 Flow。[原文 L17524](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17524)

- Worktree 被发现不是完整隔离：长 Session 可能进入其他 Worktree，冲突和管理成本会吞掉并行收益。[原文 L17742](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17742)

- Auto-memory、GraphRAG 和高优先级规则投毒引发争论。群友开始强调短期事实、文件检索、SSOT 与记忆衰减，而不是默认保存所有历史。[原文 L18295](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18295)

### 5 月 9—13 日：Codex 接管更多开发，人类掌控成为新问题

- 有参与者说“cx 全面接盘”“重回古法”；模型切换不再只是选 Builder，而开始改变整个计划、执行与 Review 结构。[原文 L18790](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18790)

- h2 的困难从“能否起更多 Agent”转向“人是否还能理解超过 15 个 Agent 构建的代码库”。讨论由“保证人类知情”、Observability、Human in the Loop 推进到 Human Harness；`Human Awareness Cognitive Load` 是本书的回顾性标签，不是当时已经确定的正式术语。[原文 L18913](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18913) [原文 L19090](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19090)

- “抽样层级考试”把检查分成记忆、自检和教育，并要求在 Plan 逐层生成时确认理解。5 月 13 日创建的 [Coach Mode PR #159](https://github.com/PolyArch/humanize/pull/159)到 6 月 13 日才合入；要分开记录概念出现与代码落地。[原文 L19874](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19874) [原文 L20401](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20401)

- HAD（Human Aided Design）提出把人的有限带宽放在 Flow 挑选出的关键确认点上，并用“带着人类往前跑”概括 Human Harness。[原文 L20651](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20651)

### 5 月 16—21 日：h1 / h2 / h3 被明确区分

- h1、h2、h3 被定义为：能工作的 Flow；人构建和测试 Flow 的平台/语言；Agent 构建自身 Flow 的自动化系统。[原文 L21886](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21886)

- `h2-dev` 分支于北京时间 5 月 17 日公开为 POC；[对应提交](https://github.com/PolyArch/humanize/commit/3fccb60c11332fb322a295db0583432416c7cf07)落地 TypeScript MCP Hub、HTML Workflow Runtime、Agent Backends、Dashboard 与 Flow Cartridges。群里一方面开始试用、提 Issue、做 Profiling，另一方面持续提醒它不是用于直接提高普通项目生产力的稳定 Flow。[原文 L22098](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22098)

- 同期有人完成从 Claude 到 Codex 的主力迁移，并继续把 Codex Review 视为难替代能力。这里是个人工作流转向，不代表社区全体同步迁移。[原文 L24737](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:24737)

### 5 月下旬：以产物为中心、动态 Flow 与“被产品内化”

- 5 月 22 日，群里开始推荐 [Oh My Pi](https://github.com/can1357/oh-my-pi)；5 月 28 日，H2 作者明确提出在 OMP 上重建 H2。`OmniPi` 是误记，HTML H2 POC 与后来的 OMP 路线也要分开。[原文 L25004](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25004) [原文 L27882](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27882)

- h2 的对话中心设计开始被批评，Artifact-centered 逐渐成为新的组织方向。[原文 L25994](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25994)

- Codex `/goal` 被理解为 Progressive Planning 与较弱 Review 的组合，并与 h2 的强契约静态 Flow 对照。[原文 L26500](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:26500)

- 5 月 28 日，Anthropic 随 [Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)在 Claude Code v2.1.154 中正式推出 [Dynamic Workflows](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)。这里的“动态”首先指 Claude 按任务即时生成 JavaScript 编排脚本；生成后的脚本由独立 Runtime 执行。它与 H3 所设想的运行中改写 Flow 仍有差别。[原文 L28740](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:28740)

- 对 Humanize 未来的一种判断是：有效 Flow 的最好归宿，是在几个月内被 Claude Code、Codex 等产品吸收。外部 Harness 的角色因而开始从日常编排转向实验、控制和可观测。[原文 L25750](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25750) [原文 L29630](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29630)

- “没有例证的 Flow 站不住脚”把讨论拉回真实项目、第三方案例、成本与质量，而不是只看架构图和 Token 量。[原文 L31195](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:31195)

## 6 月｜Humanize 3、动态工作流、Monitor 与模型吸收 Harness

### 6 月 2—7 日：h3 / oh-my-humanize 与 Monitor

- h3 被实现为 `oh-my-humanize` 的早期形态，核心增量是允许 Agent 修改正在运行的工作流，但修改权、触发方式和人类审批仍在实验。仓库于 6 月 1 日 UTC（北京时间 6 月 2 日）加入 Workflow Runtime，[随后数小时的提交](https://github.com/PolyArch/oh-my-humanize/commit/fccda309629d02ee033f06819a2554d8b6a8ca22)已经支持实时 Graph Revision。[原文 L32220](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32220)

- 长程 `/goal` 任务催生“Claude 监控 Codex”的第三方 Monitor。典型组合是 Codex `/goal` 执行，Claude Code `/loop` 每小时读取代码库与完整 Transcript，识别低效深挖、死胡同和事实问题；发现异常后，通过 Remote Control 通知 Human，获批后再用 tmux 注入 Steer Prompt。[原文 L34718](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:34718) [原文 L35444](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35444)

### 6 月 8—10 日：Monitor Loop、动态主义、错题本失败与 Pi

- 6 月 8 日，作者自报已在手机上运行十个监控 Loop，并为既有原则设置少量 Auto-inject 白名单；6 月 10 日，群聊直接使用 `Monitor Loop` 这一名称，把 Human 放在有限的关键 Check Point 上。[原文 L36338](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36338) [原文 L37862](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:37862)

- 动态主义与组合主义被作为两条路线讨论：是让 Agent 在巨大 Flow 空间中动态选择，还是组合少量已经验证的 Flow。[原文 L36555](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36555)

- 优化 Flow 的“错题本”实验被删除，因为失败记录会把仍有潜力的邻近方向一起剪掉。Evidence Score、Decay Rate 和记忆的路径依赖进入讨论。[原文 L37904](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:37904)

- 群友重新注意到 OpenClaw 背后的 Pi：OpenClaw 本体未必适合 Coding，但极简 Agent Core 被认为可能更适合让用户自己搭 Coding Harness。群聊中的“龙虾”指 OpenClaw，不指 Humanize。[原文 L38240](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:38240)

### 6 月 13—18 日：Humanize 3 进入公开试用，Flow 验证成为瓶颈

- Humanize 3 被描述为 Agent-mutable Dynamic Workflow；[6 月 12 日的提交](https://github.com/PolyArch/oh-my-humanize/commit/eea3778e2e5ba7fa38f90eae6da4d9d9461a1474)集中落地 Mutable Runtime。围绕 FlowBench、Flow Factory、Flow 修改门控和 Flow-aware Inference 的讨论密集出现。[原文 L40620](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40620) [原文 L44115](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44115)

- 这套实现随即发生工程回摆。[6 月 13 日的提交](https://github.com/PolyArch/oh-my-humanize/commit/eb78a8eacc905434dd340f01a0f1ea8fa5d90276)拒绝向 Active Run 直接提交 Graph Patch；生产 Attempt 后来绑定 Immutable Freeze，改 Flow 需经过停止、Checkpoint、审批、重新冻结与重启。H3 的“动态”由 Live Mutation 收紧为受控演化。

- 群里给出一组相对正式的 1.0 / 2.0 / 3.0 描述：单一硬编码 RLCR Flow；构建 Flow 的 IR；让 Flow 生成 Flow 的平台。[原文 L43776](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:43776)

- 6 月 15 日，`oh-my-humanize` 公开邀请社区试用，短暂内置九种 Flow，包括 H1 RLCR 与 KDA；发现一两个 Bug 后整批回滚，未充分验证的 Built-in 于 6 月 16 日被降级。作者随后提出先在本地连续验证 80 小时再升格。[原文 L42888](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42888) [原文 L45897](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45897)

- [KDA](https://github.com/mit-han-lab/kernel-design-agents)把 Humanize Plan/RLCR 用到 CUDA Kernel 优化；[公开复现仓库](https://github.com/mit-han-lab/mlsys2026-flashinfer-contest)记录了 MLSys 2026 Competition NVIDIA Track 的第 1、2、3 名。公开归属是 MIT HAN Lab，不能据赛道名写成 NVIDIA 官方内部系统。

- 群聊把长程任务中漏掉隐含条件的问题称为 `cognition overload`，再次接上 5 月的“保证人类知情”与 Human Harness 讨论。[原文 L45831](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45831)

- 6 月 17 日公开的 [`monitor-codex-goal` Skill](https://github.com/SihaoLiu/skills/tree/ec9cd9e2733f28d93bbf66c37ef58722cf6390ce/monitor-codex-goal)把 Monitor Loop 固化为只读审计、手机通知、人工审批和受控注入；次日，社区又用它监控 Flow Test Case 的执行路径。[首次提交](https://github.com/SihaoLiu/skills/commit/ec9cd9e) [原文 L45971](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45971)

- 回看 Claude Code Dynamic Workflows 后，群里反思 h2-dev 使用 HTML/专用语法是否过度设计，转向 YAML AST 与 JS/TS 等更直接的表达。[原文 L43811](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:43811)

- [GLM-5.2](https://z.ai/blog/glm-5.2)于 6 月 16 日正式发布，强调 1M Context、长程 Agentic Work、Flexible Effort 与开放权重；群里 6 月 13—14 日已出现提前传播和实测，评价同时包含“自然使用 Workflow”与速度慢、容量紧、幻觉。[原文 L41848](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:41848)

### 6 月 20—26 日：项目重组、Humanize 1.0 被“炼化”、GPT-5.6 预览

- 群公告集中列出当时的 `oh-my-humanize`、Humanize 1.0、Multi-Agent Wiki、Slides 和社区文章，可视为阶段性的项目资料快照。[原文 L46720](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46720)

- 群里观察到 GLM 等模型会主动调用 Codex 做 Review，称“Humanize 1.0 已经被彻底炼化”；这只是对外部行为的社区解释，不是模型训练事实。[原文 L47290](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47290)

- 国内模型讨论从“是否能平替 Claude”推进到 Builder、Reviewer、长程 Agent、价格与蒸馏周期的细分比较。Humanize 开始更像比较这些角色能力的试验场，而不是绑定单一模型的工具。[原文 L47370](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47370)

- Monitor 被重新限定：多 Flow、长任务可能有价值，一两个短任务未必需要；主动监控与被动观察也不等价。[原文 L48765](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48765)

- 6 月 26 日，OpenAI 开启 [GPT-5.6 限量预览](https://openai.com/index/previewing-gpt-5-6-sol/)，发布 Sol、Terra、Luna，并用 `max` 表达更深单 Agent 推理、用 `ultra` 调度 Subagent。群聊随即转向 Token Efficiency 与长程 Reward Hacking。[原文 L48962](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48962)

## 7 月与记录末段｜自动子 Agent、国产模型、轻 Harness 与多人协作

### 7 月 2—10 日：Codex 成为主力，GPT-5.6 GA 与自动子 Agent

- 有参与者明确建议连续使用 Codex + GPT 三周，并回顾自己曾在 4 月大量使用 Claude。这代表一条个人迁移轨迹，也呼应了 5 月以来对 Codex `/goal` 与 Review 的持续评价。[原文 L49830](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:49830)

- 超长程任务把隔离从 Worktree 推向可 Snapshot 的 Sandbox、容器、SSH、VNC 与 Computer Use；目标是隔离进程状态和外部副作用，并允许从快照重新分叉。[原文 L51128](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:51128)

- GPT-5.6 于 [7 月 9 日全面发布](https://openai.com/index/gpt-5-6/)，其自动 Sub-agent 能力引发密集试用。10、70、101 个子 Agent 是群友的个人报告，并非官方承诺的固定规模；递归、预算、生命周期和 UI 问题同时出现。[原文 L52166](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52166) [原文 L53933](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:53933)

- 群里再次提出“模型已经把 Builder—Reviewer、任务追踪和主动分解炼化进去”。外部 Humanize 因而转向实验控制、多人协作和高风险边界。[原文 L53013](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:53013)

### 7 月 12—20 日：Pi、Kimi K3、Arch / PM / Audit 与模型迁移回顾

- Pi 被描述为 OpenClaw 的 Agent Core，也是一个非常精简的 Harness；支持者认为模型越强，Pi 的优势越明显。[原文 L54420](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:54420)

- Kimi K3 于 [7 月 16 日发布](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)，完整权重在 7 月 27 日开放。群内快速把它放进长程 Build、Codex Review 和不同订阅/API 成本中试用，并提出 `K3 Build + Sol Review`；对 K3、Sol、Fable 的排序始终有分歧。[原文 L56900](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56900) [原文 L57440](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:57440)

- 另一条路线建立 Arch / PM / Audit 三个窄职责主 Session，每个再带多个子 Agent；角色之间通过会议记录、执行轨迹和缺陷文件交接。[原文 L58269](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58269)

- 7 月 20 日的长段回顾把个人迁移轨迹写得最清楚：Claude/Opus 的早期领先，GPT-5.2 长程能力的转折，Codex `/goal` 与 Review 的接管，以及 Kimi K3 带来的新一轮迁移意愿。[原文 L59770](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:59770)

### 7 月 24—29 日：H1 回归、Context Engineering、Bare Pi 与 MHMA

- 7 月 24 日，一次 Sol 长程重构经历五次 Context Compaction、产生六千多行改动后，重新采用了人类已经否决的设计。社区随即建议接回 Monitor / RLCR，并留下“说好的不需要 Harness 的时代呢”这句反问。它是一次个案，说明自动规划出现以后，持久约束和独立验证仍有用武之地。[原文 L62193](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62193) [原文 L62245](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62245)

- Opus 5 和面向 Claude 5 的 Context Engineering 资料进入群聊，模型/Harness 的边界再次变化；同一时期也出现 Skill Dropout，防止过多规则把 Agent 锁死在旧路径上。[原文 L62566](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62566) [原文 L59908](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:59908)

- 7 月 26 日，群友报告 `ultra` 在多次压缩后丢失深层 Subagent 生命周期和职责状态，阶段性停止并与人对齐被称作 `human as memory`。[原文 L63768](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:63768)

- 7 月 28—29 日的实践转向 Bare Pi、极短 System Prompt、Bash 与 Sub-agent，并讨论多人多 Agent（MHMA）的文件/脚本交接。这里把复杂编排更多交给强模型现场生成，同时继续保留工具面与交接方式的外部设计。[原文 L64473](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:64473) [原文 L64926](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:64926) [原文 L65151](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:65151)

- 同期讨论把人的瓶颈从代码输入推进到 Plan、认知同步和责任：模型构建能力继续提高，人与模型的交互带宽却没有同步增长；连续 `approve` 会累积难以维护的系统。[原文 L65288](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:65288) [原文 L65363](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:65363)

### 记录末段：基础设施追赶模型，简化成为能力

- 数百个子 Agent 带来 UI、进程管理、递归深度和任务状态问题；模型派发能力开始超过现有基础设施的承载能力。[原文 L67657](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:67657)

- 7 月 31 日，[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731/blob/main/README.md)作为取代 Preview 的正式版本发布。官方 Code Agent 成绩使用尚未公开的 DeepSeek Harness Minimal Mode；群里也立即从模型排名转向 Harness、Reasoning Effort 和实际 CLI 组合。[原文 L67269](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:67269)

- 动态主义与组合主义最终没有分出胜负：机械维护适合代码化 Flow，探索任务适合动态决策，自动平衡机制仍未知。[原文 L68085](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68085)

- Agent-Flow-Language 发布早期版本；同时，模型主动重写、删除和 Simplify 代码成为新的观察点。社群的关注从“怎样让 Agent 多做”又转向“怎样让 Agent 正确地少做”。[原文 L68605](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68605) [原文 L68773](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68773)

- 最后一段标准化讨论指出，Agent 为完成 Goal 可能 Fork 通用依赖或定制全部零件，短期达标却抬高量产和维护成本。把稳定部分做成 Tool、表单与可校验接口，被概括成“不要写作文，要搞成填空题”。[原文 L68953](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68953)

## 暂时可见的几条演进方向

这些只是材料导航，不是最终结论：

1. **模型角色变化**：Claude/Opus 早期承担主要 Build，Codex 先以 Review 和 Debug 见长，随后 `/goal`、长程能力与自动 Sub-agent 让 Codex 接管更多主任务；国产模型又从低价 Worker 进入长程 Build 与 Review 候选。

2. **Agent 形态变化**：Ralph Loop → Builder—Reviewer → Batch/Worktree → h2 静态 Flow → h3 动态可变 Flow → 模型原生编排与 Bare Pi。

3. **Harness 位置变化**：Prompt 规则 → Tool Permission / Hook / Script → IR 与 Runtime → 实验控制、Sandbox、审计与多人交接。

4. **人的位置变化**：写代码 → 写 Plan/Spec → 选择 Review 点 → 维护 Human Harness → 管理认知债、风险与责任。

5. **OpenClaw/Pi 线索**：OpenClaw 的热度、泛用性和工程质量被质疑，但其底层 Pi 在强模型时代被重新发现为轻量 Coding Agent Core。这个反差值得单独成章，不能简单写成“龙虾失败”。

6. **持续未决的问题**：固定还是动态、共享记忆还是独立探索、自由沟通还是产物交接、重 Harness 还是轻 Harness、真实项目还是 Micro-benchmark。
