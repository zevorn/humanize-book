# Agent 发展史：一手资料核查与群聊证据索引

> 用途：为 Humanize Book 的按日期初筛、历史叙事和后续分析提供底稿。本文不试图把群聊整理成一条严格的因果链，而是把“当时群里看到了什么、成员怎样反应、外部事实能否被一手资料确认”分开记录。

## 一、资料边界与证据等级

本核查以《Humanize聊天记录_完整并行OCR_去重版》为群聊证据，以厂商公告、官方文档、GitHub 仓库和原始 X/Twitter 帖为外部证据。聊天记录从“3月18日”开始，结合其引用的 2026 年官方发布，可判断主体时段为 **2026 年 3 月至 8 月初**。7 月 28 日以后，OCR 文档只保留“星期日”“昨天”等相对日期，因此这一段不宜擅自还原成精确日期。

证据等级：

- **A：可直接核对的一手资料。** 官方公告、官方文档、GitHub 提交或 PR，可确认事件与日期。
- **B：群聊中有明确原话或链接，但外部页面无法完整复核。** 例如 X 页面无法抓取正文，或群友讲述的是个人经历。
- **C：回忆、推断或概念命名。** 可用于呈现社区感受，不能当作客观史实。

使用时应保留“外部事件”和“群体反应”之间的距离。群聊能证明社区在某个时点讨论了某件事，不一定能证明该时点就是技术首次出现，也不能自动证明前后事件存在因果关系。

## 二、群聊开始前的历史背景（2024—2025）

这部分不是群聊同期内容，而是理解 2026 年讨论所需的前史。

| 日期 | 外部事件与一手资料 | 可支持的历史判断 | 证据 |
| --- | --- | --- | --- |
| 2024-11-25 | Anthropic 发布 [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) | MCP 把模型连接数据源和工具的问题标准化，成为后续 Agent 基础设施的一条主线。 | A |
| 2025-02-24 | Anthropic 随 Claude 3.7 Sonnet 发布 [Claude Code 研究预览](https://www.anthropic.com/news/claude-3-7-sonnet) | Claude Code 从终端读取代码、改文件、跑测试、提交代码，较早把“模型”包装为可工作的 coding agent。 | A |
| 2025-05-16 | OpenAI 发布 [Codex 云端 coding agent 研究预览](https://openai.com/index/introducing-codex/)；公告同时说明 Codex CLI 已于此前一个月推出 | OpenAI 从 CLI 与云端异步任务两端追赶，并突出多任务并行、隔离环境和可验证结果。 | A |
| 2025-10-16 | Anthropic 发布 [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | Skills 把可复用知识、脚本与工作流程做成渐进加载的模块，后来频繁进入 Humanize 社群讨论。 | A |
| 2025-11-24 | Anthropic 发布 [Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5) | 厂商把“coding、agents、computer use”和长时间运行能力放在同一产品叙事中。 | A |
| 2025-11-26 | Anthropic 发布 [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | “初始化 Agent + 编码 Agent”、进度文件、Git 状态、上下文重置与增量推进，为后续 harness 讨论提供了明确方法。 | A |
| 2025-12-18 | OpenAI 发布 [GPT-5.2-Codex](https://openai.com/index/introducing-gpt-5-2-codex/) | 官方强调 compaction、长时任务、重构和迁移，coding agent 的竞争开始从单次生成转向长程执行。 | A |
| 2026-01-12 | [PolyArch/humanize](https://github.com/PolyArch/humanize) 建仓；首个提交 [Initial commit Humanize v1.0.0](https://github.com/PolyArch/humanize/commit/888451dbe0baf71b006f03961b7eb06939c100bf) | Humanize 1.0 有可核验的版本起点：Claude Code 负责 build、Codex 独立 review，外加目标跟踪、周期性全局对齐与熔断。 | A |

群聊中的回忆与这条前史大致吻合，但只能作为亲历者口述：成员说自己从上一年 11 月开始思考 Humanize、1 月做出来，希望把人主动放回 loop；另一段回顾则把 12 月到 2 月描述为长程 coding agent 快速跃迁期。[聊天记录 L19166–L19170](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19166) [聊天记录 L59811–L59818](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:59811)（B/C）

## 三、2026 年按月证据时间线

### 1—2 月：多 Agent 与 Harness 进入厂商主叙事

- **2 月 2 日，OpenAI 推出 Codex app。** 官方将其定义为同时管理多个 Agent 的“command center”，并整合 Skills 与 Automations；这说明 OpenAI 的追赶已经不只是模型分数，而是桌面工作台和多 Agent 调度。[官方公告](https://openai.com/index/introducing-the-codex-app/)（A）
- **2 月 5 日，Anthropic 发布 Opus 4.6 和 Agent Teams。** [Opus 4.6 公告](https://www.anthropic.com/news/claude-opus-4-6)强调更长的 agentic tasks、代码审查与调试，同时引入 Agent Teams。（A）
- 同日 Anthropic 披露“并行构建 C 编译器”实验：16 个 Agent、近 2,000 次会话、约 10 万行代码；其工程实现并非复杂群体智能，而是容器、Git、任务锁和极简循环，且官方明确列出失败与限制。[Building a C compiler with parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler)（A）
- **2 月 11 日，OpenAI 发布 Harness Engineering。** 其核心不是提示词技巧，而是把仓库作为事实源，令 AGENTS.md 充当地图，再用架构约束和 lint 把规则机械化；文中的团队实践是“人负责 steering，Agent 负责 execution”。[Harness engineering](https://openai.com/index/harness-engineering/)（A）

这些事件发生在聊天记录之前，但解释了为什么 3 月群里一开场就围绕 harness、Agent Teams、并行与 coding agent 争论，而不是从“什么是 Agent”讲起。

### 3 月：从模型惊艳转向 Harness、Agent Teams 与控制论

- **3 月 20 日，群内直接把 Harness Engineering 概括成“控制论”。** 成员同时讨论 Codex 的产出质量和如何控制执行过程。这是一条重要的社区语义变化：关注点从模型会不会写代码，转向怎样建立反馈、约束和可恢复的执行系统。[聊天记录 L656–L687](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:656)（B）
- **3 月 21 日，群内转发 OpenAI Harness Engineering 原文。** 这是“社区讨论—官方材料”可以闭环的明确节点。[聊天记录 L791](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:791)；[官方原文](https://openai.com/index/harness-engineering/)（A）
- **3 月 23 日，Agent Teams 引发密集质疑。** 群友一方面引用大规模并行项目的数字，另一方面质疑 peer communication 的价值，提出真正难点可能是“禁止通信”、隔离上下文和权限。不要把这段写成社区否定多 Agent；更忠实的说法是，大家开始区分“并发数量”与“有效协作结构”。[聊天记录 L949–L1203](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:949)（B）
- Anthropic 的多 Agent 指南也支持这种谨慎态度：多 Agent 往往被过度使用，成本可能是单 Agent 的 3—10 倍，真正适合的是上下文隔离、可并行工作和角色专业化。[Building multi-agent systems](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them)（A）
- **3 月 24 日，群内讨论 OpenClaw 的代码质量和适用场景。** 讨论重点并非 coding agent，而是常驻个人 Agent 的形态、记忆和工具组织；有成员明确觉得它对自己的 coding 工作不够必要。[聊天记录 L1543–L1588](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1543)（B）
- **3 月 26—30 日，Humanize 进入快速迭代与并行实践期。** 群中连续出现 PR #42、#47、#51、Anthropic harness 设计文章、多 Agent 指南，以及“并行开 10 个 Humanize”的实际尝试。[聊天记录 L2461–L2617](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:2461) [聊天记录 L3678–L3710](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3678)（A/B）
- 3 月 30 日转发 Boris Cherny 的 X 帖，群聊截图将其解释为 Claude Code 会话在云端与本地之间 teleport/remote control。[原始 X 链接](https://x.com/bcherny/status/2038454336355999749)目前无法稳定抓取正文，因此只宜把“群里在讨论远程接管”作为事实，不宜扩写产品能力。[聊天记录 L3698](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3698)（B）

### 4 月：Humanize 1 收束，Humanize 2 从“换模型”转向“流程平台/语言”

- **4 月 3 日，记忆架构成为议题。** 群内提出，不应在 Agent 之间直接共享完整 session history，而应共享经过筛选的知识。这与后来关于上下文隔离、知识工件和认知负担的讨论相连，但不必写成确定的技术因果。[聊天记录 L5992–L5994](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5992)（B）
- **4 月 17 日，Humanize 2 的第一层目标被明确为 model-independent。** 讨论同时涉及 Codex 作为默认 builder、hooks，以及 Claude/Codex 的能力差异。[聊天记录 L9072–L9150](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9072)（B）
- **4 月 20—23 日，H2 的设计迅速深化，也马上受到内部质疑。** 一条路线主张“less is more”：机械工作交给脚本，把系统控制在 1,000 行以内；随后又提出用 Rust 重写，以 `humz / hcc / hvm` 形成 flow language、compiler、VM，并用数据流图和形式化检查表达流程。群内也有人认为 DSL 可能过度设计。这组对话非常适合保留原始分歧，而不是替作者决定谁对谁错。[聊天记录 L11516–L11524](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11516) [聊天记录 L13190–L13320](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13190) [聊天记录 L13870–L14300](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13870)（B）
- **4 月 21 日，H1/H2 的分界被口头确认。** 1.17.x 被设想为 H1 最后版本；H2 要模型无关，但成员认为 Codex 的独立 review 仍是 H1 的关键价值，同时担忧国产模型尚缺少同等审查能力。[聊天记录 L12943–L13005](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12943)（B/C）
- **4 月 26—27 日，H2 进入“自举/内部测试”的叙述。** 群里称 H2 day-one bootstrap，并说 H1 即将成为历史；这反映当时预期，不等于 H2 已正式发布。[聊天记录 L15298–L15325](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:15298) [聊天记录 L15709–L15715](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:15709)（B）
- **4 月 30 日，Humanize 1.16 合并。** 群聊宣布合并，[PolyArch/humanize PR #51](https://github.com/PolyArch/humanize/pull/51) 的 GitHub 记录可确认其于 4 月 30 日合并。这是 H1 最清晰的正式里程碑之一。[聊天记录 L16978–L16982](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16978)（A）

同月也出现了社区对模型更替的即时体感：一位成员把 1 月至 4 月概括为 Gemini、Claude、GPT 的“朝代”轮换。它很有时代气息，但不是基准测试，适合作为口述史侧栏，不应升级为行业结论。[聊天记录 L15753–L15764](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:15753)（C）

### 5 月：H2 原型化，H3 被定义；厂商开始让 Agent 动态生成工作流

- **5 月 9 日，H2 被重新表述为“human awareness / cognitive load”问题。** 群内甚至提出通过 quiz 检验人是否真正理解 Agent 的进展。这说明 Humanize 的“human-in-the-loop”不只是审批按钮，而是保持人的认知同步。[聊天记录 L18931–L18975](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18931)（B）
- **5 月 16—17 日，H2 有了可核验的代码原型。** `h2-dev` 分支中的 [Apply Humanize2 platform onto h2-dev](https://github.com/PolyArch/humanize/commit/3fccb60c11332fb322a295db0583432416c7cf07) 提交可确认 H2 平台进入仓库；群聊也直接贴出 `h2-dev` 分支。[聊天记录 L22099](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22099)（A）
- **5 月 16 日，群内给出最清楚的三阶段定义：** “H1: a flow that works；H2: a platform/language that human build/test flow；H3: an automation system that let agents builds its own flow”。这是理解 Humanize 1/2/3 的核心原话，但它是路线图式概念，不是三个正式 release。[聊天记录 L21910–L21912](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21910)（B）
- 同日群内分享 Codex hooks。当前官方文档把 hooks 定义为在生命周期事件触发的确定性脚本，包括 Stop、SubagentStop 等；但文档已迁移，不能据此确认功能首次发布时间。[Codex hooks 文档](https://learn.chatgpt.com/docs/hooks) [聊天记录 L21703](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21703)（A/B）
- **5 月 28 日，Claude Opus 4.8 与 Dynamic Workflows 发布。** 官方称 Claude 可自己编写 orchestration scripts，调度数十乃至数百个并行 subagents，并让验证由独立 Agent 完成。[Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) [Dynamic workflows](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)（A）
- 群内于 5 月 29 日转发 Opus 4.8；6 月 18 日再次转发 Dynamic Workflows 并讨论它与 H2/H3 的区别。[聊天记录 L28740](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:28740) [聊天记录 L45722](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45722)（A/B）

这里形成了一个值得观察、但不宜强行写成因果的“同向演进”：Humanize 内部在定义“Agent 自己构建流程”，Anthropic 同期也在把动态生成调度脚本产品化。

### 6 月：H3/oh-my-humanize 形成项目，国产与开源 Agent 进入密集讨论

- **6 月 2 日，oh-my-humanize 被明确介绍为 Humanize 3。** 它建立在 OMP 上，关键增量被描述为“Agent 可以修改正在运行的 workflow”，群内据此区分静态流程、动态选择流程和运行中自修改流程。[聊天记录 L32248–L32335](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32248)（B）
- GitHub 可确认 [PolyArch/oh-my-humanize](https://github.com/PolyArch/oh-my-humanize) 于 6 月 1 日建立，后通过 [迁移提交](https://github.com/PolyArch/oh-my-humanize/commit/04e0229d474b7258f8bf36efd0d86f6036857456) 转到 [humanfia/oh-my-humanize](https://github.com/humanfia/oh-my-humanize)。群公告也于 6 月 20 日同步了迁移，并把旧项目标成 “Humanize (1.0)”。[聊天记录 L46655–L46761](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46655)（A）
- **6 月 15 日，群内公开邀请试用 OMH。** 当时称内置九种 flow，包括 Humanize 1 和 KDA；讨论者同时怀疑 progressive workflow 是否真的优于更简单的方案。这仍是实验陈述，不应改写成经过验证的性能结论。[聊天记录 L42888–L42916](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42888)（B）
- **6 月 15 日，对“龙虾”的实践评价发生收缩。** 有成员认为用 OpenClaw 做 research/browser 消耗 token 太多，自己已经回到 coding CLI。这比“OpenClaw 不适合 coding agent”更准确：原话比较的是常驻通用 Agent 与 coding CLI 的工作适配，而不是一项系统评测。[聊天记录 L43345–L43361](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:43345)（B）
- **6 月 26 日，OpenAI 预览 GPT-5.6 Sol。** 官方将 Sol/Terra/Luna 组成新系列，并在 ultra reasoning 中加入 subagents；7 月 9 日 GPT-5.6 正式发布，`ultra` 被描述为协调多个 Agent。[Sol 预览](https://openai.com/index/previewing-gpt-5-6-sol/) [GPT-5.6](https://openai.com/index/gpt-5-6/)（A）
- 这对应群内 6 月 26 日与 7 月 10 日的即时转发，说明社区关注点从“OpenAI 是否追上 Claude”继续转向模型是否原生吸收 harness、多 Agent 和长程执行能力。[聊天记录 L48963](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48963) [聊天记录 L52252](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52252)（A/B）
- **国产与开源路线并非单一事件，而是连续进入视野。** GLM-5.2 官方于 6 月 16 日发布，强调 1M context、长程 agentic work、MIT 权重与 agentic RL；群聊在标作 6 月 14 日的位置已讨论 GLM-5.2，存在提前获知、OCR 日期错位或后期拼接的可能，必须保留疑点。[GLM-5.2 官方公告](https://z.ai/blog/glm-5.2) [聊天记录 L42075–L42140](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42075)（A/C）

### 7 月至 8 月初：模型吸收 Harness，H1 被重新估值，Flow 成为新的抽象层

- **7 月 6 日，群内分享 DeepSeek 的 DeepCode 集成。** 官方页面把 Deep Code CLI 列为第三方 Agent 工具，支持 Agent Skills，但也明确提示其效果和安全性由第三方承担；因此不能把它写成 DeepSeek 自研 coding agent 正式发布。[官方文档](https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/deepcode/) [聊天记录 L51319](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:51319)（A）
- **7 月 9—10 日，群内出现“模型正在吸收 harness”的判断。** 它表达了一个当时的社区问题：当模型自身拥有 compaction、subagents、工具调用和流程规划，外部 harness 还剩什么价值？这应作为开放问题呈现，而非结论。[聊天记录 L51947](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:51947)（B/C）
- **7 月 16—17 日，Kimi K3 发布并进入群聊。** Kimi 官方历史页可核对 K2、OK Computer、K2.5、Kimi Claw、开源 K2.6、K3 的连续产品线；K3 公告强调长程任务和 1M context，并于 7 月 27 日开放权重。[Kimi Agent 产品历史](https://www.kimi.com/help/agent/agent-overview) [Kimi K3](https://www.kimi.com/blog/kimi-k3) [聊天记录 L57747](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:57747)（A）
- Kimi K2.5/K2.6 的官方文章分别展示最多 100 个 Agent、1,500 次调用，以及 300 Agent、4,000 步的并行/长程实验。这些数字来自厂商自报，只能说明产品方向和公开主张，不能作为跨模型独立排名。[Kimi K2.5](https://www.kimi.com/blog/kimi-k2-5) [Kimi K2.6](https://www.kimi.com/blog/kimi-k2-6)（A，厂商口径）
- **7 月 24—25 日，Claude Opus 5 发布并被群内转发。** 官方重点仍是验证、迭代和 agentic work，说明 Claude 的“领先”叙事继续围绕整个执行系统而非纯模型能力。[Opus 5](https://www.anthropic.com/news/claude-opus-5) [聊天记录 L62592](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62592)（A）
- **7 月 24 日，群内重新肯定 Humanize 1。** 观点是，即便 autonomous agents 更强，仍需要 harness；这与 4 月“让 H1 进入历史”的乐观判断形成自然张力。[聊天记录 L62245–L62256](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62245)（B）
- **7 月 25 日，群内把 `flowjanus` 称为“最小 H2”。** 但 `humanfia/flowjanus` 当前无法通过公开 GitHub API 访问，可能已私有、删除或改名。应保留群聊原链和描述，同时标为未核验，不能据此写正式发布史。[聊天记录 L62917–L62929](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62917)（B/C）
- **7 月 28 日后的相对日期段，讨论又回到 H1 的认识论。** 有成员说“H1 把 LLM 当 compiler”，并把第一次 Humanize loop 和后来的 `/goal` 视为两次 harness 震动。这是最有价值的亲历者总结之一，但属于思想史口述。[聊天记录 L64427](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:64427) [聊天记录 L68207–L68218](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68207)（B/C）
- 随后群内分享 [tastynoob/Agent-Flow-Language](https://github.com/tastynoob/Agent-Flow-Language)，把 workflow 表达成可编译 IR，并讨论 Skills、MCP、安全和 RAG 的边界；GitHub 显示仓库创建于 2026 年 8 月 2 日。由于群聊只写相对日期，建议排版为“7 月 28 日后 / 8 月初”，不要精确到某一天。[聊天记录 L68606–L68615](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68606)（A/B）

## 四、Humanize 1.0、2.0、3.0 的证据对照

| 阶段 | 群内定义与思想变化 | 可核验工程事实 | 出版时应怎样称呼 |
| --- | --- | --- | --- |
| **Humanize 1 / H1** | “A flow that works”；Claude build + Codex review，人负责架构和介入，靠循环、全局对齐、目标和熔断维持长程执行。 | 2026-01-12 建仓和 `v1.0.0` 首提交；1.16 的 PR #51 于 4 月 30 日合并。 | 可以称正式项目与版本线。 |
| **Humanize 2 / H2** | 从模型无关，逐步扩展到“人构建和测试 flow 的 platform/language”；曾探索 Rust、compiler/VM、DFG、形式化检查和认知同步。 | `h2-dev` 分支及 5 月 16 日平台提交存在；未找到与 H1 同等级的独立正式 2.0 release/tag。 | 宜称“路线、设计与原型”，不要写成已完整发布的 2.0 产品。 |
| **Humanize 3 / H3** | “Agent builds its own flow”；重点由人预先写 flow 转向 Agent 在运行中创建、选择和修改 flow。 | `oh-my-humanize` 6 月 1 日建仓，6 月 19—20 日迁移至 humanfia；群聊明确把它称为 H3。 | 可称“H3 方向 / oh-my-humanize 项目”，并注明这是群内命名。 |

当前 [oh-my-humanize workflow 文档](https://github.com/humanfia/oh-my-humanize/blob/main/docs/workflows.md) 强调可变、可审计的 flow artifacts，以及进入生产尝试前的 immutable freeze；但仓库内容在群聊之后仍会演进，不应拿今天的 README 倒推 6 月当时已经具备全部能力。

最忠实的历史叙事不是“H1 被 H2 淘汰、H2 又被 H3 淘汰”，而是三条问题意识相互覆盖：

1. H1 解决“怎样让一个可工作的反馈循环跑起来”；
2. H2 追问“怎样让人能够表达、检查和复用流程”；
3. H3 追问“当 Agent 变强后，流程能否在运行中由 Agent 自己生成和修正”；
4. 到 7 月，社区又重新发现 H1 的简洁与外部约束仍有价值。

## 五、“龙虾”必须单独校正：OpenClaw 不是 AutoGPT

对聊天全文检索，没有发现 **AutoGPT / Auto-GPT** 的明确提及。相反，“小龙虾”“龙虾”在可定位上下文中明确指向 **OpenClaw**：群里直接说“OpenClaw 背后核心框架 Pi”，后文又说“pi 是 openclaw 的 agent core”。[聊天记录 L38238–L38248](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:38238) [聊天记录 L54440–L54450](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:54440)（B）

- [OpenClaw 仓库](https://github.com/openclaw/openclaw)创建于 2025 年 11 月，定位是本地运行、跨消息渠道、可扩展 Skills 的个人助手；这与群聊对常驻 Agent、记忆和 browser/research 的讨论一致。（A）
- [AutoGPT 仓库](https://github.com/Significant-Gravitas/AutoGPT)创建于 2023 年 3 月，是更早一轮 autonomous agent 热潮的代表；当前仓库已演进成平台，原来的 Classic 仍保留其中。（A）
- 因此，如果小册子要把 AutoGPT 写进大历史，应把它放在 **2023 年行业前史**，并明确“这是编辑补充的外部背景，不是本群聊中的‘龙虾’”。若要叙述群友后来发现“龙虾不适合 coding agent”，正确主语应是 OpenClaw，而且原话更接近“通用常驻 Agent 在 research/browser 上 token 成本高，实际工作回到 coding CLI”。

## 六、Agent Teams、Subagents、MCP、Skills 与 Harness 的概念分工

为了避免小册子把同期热词写成同义词，可用以下朴素分工：

| 概念 | 在历史中的功能 | 一手资料 |
| --- | --- | --- |
| **MCP** | 连接模型与外部数据/工具的开放协议，解决“怎么接”。 | [Anthropic MCP 公告](https://www.anthropic.com/news/model-context-protocol) |
| **Skills** | 可渐进加载的知识、指令和脚本包，解决“怎样复用某类能力”。 | [Anthropic Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) |
| **Subagents** | 隔离上下文、分派专门工作，可前台或后台运行，解决“怎样拆任务与隔离上下文”。 | [Claude Code subagents 文档](https://code.claude.com/docs/en/sub-agents) |
| **Agent Teams** | 多个独立上下文的 Agent 可相互通信，需要额外 token 与协调，适合真正并行、专业化任务。 | [Claude Code Agent Teams 文档](https://code.claude.com/docs/en/agent-teams) |
| **Harness** | 包围模型的任务分解、状态、反馈、校验、权限、恢复、上下文管理和工程约束，解决“怎样稳定地做完”。 | [OpenAI Harness Engineering](https://openai.com/index/harness-engineering/)；[Anthropic long-running harness](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) |
| **Dynamic workflow / Agent-built flow** | 让 Agent 根据任务生成或修改编排逻辑，解决“流程由谁、在什么时候决定”。 | [Claude Dynamic Workflows](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)；Humanize H3 群聊原话 |

群聊中的关键洞察，是这些层次不能互相替代：增加 subagent 数量不等于拥有好的 harness；MCP 接入更多工具不等于知道何时调用；Skills 提供知识不等于状态恢复；模型能动态编排也不等于外部校验和权限约束已经无用。

## 七、X/Twitter 与聊天引用的处理建议

以下 X 链接出现在聊天记录中，但当前无法稳定取得原帖正文。它们仍可作为历史书签，内容只能按群聊截图和转述描述，证据等级为 B：

- Boris Cherny 关于会话 teleport/remote control：[原帖](https://x.com/bcherny/status/2038454336355999749)；[聊天记录 L3698](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3698)。
- Cursor 官方关于模型路由：[原帖](https://x.com/cursor_ai/status/2049901436918436249)；[聊天记录 L17076](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17076)。
- Cursor 官方被群内概括为 PDBR（plan-delegate-build-review）：[原帖](https://x.com/cursor_ai/status/2052432778743210127)；[聊天记录 L18503](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18503)。
- `trq212` 的“Six Workflow Patterns”讨论：[原帖](https://x.com/trq212/status/2061907337154367865)；[聊天记录 L33828](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33828)。
- `_can1357` 分享 snapcompact：[原帖](https://x.com/_can1357/status/2065284468311461895)；[聊天记录 L40628](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40628)。

出版前如需引用具体措辞，应人工登录 X 复核原帖或使用作者保存的截图；在未复核前，不要把群聊 OCR 中的摘要放进引号。

## 八、仍未解决的疑点与编辑红线

1. **精确年份和相对日期。** 2026 年可由大量官方链接交叉确认，但 7 月 28 日以后只能写“7 月底至 8 月初”。
2. **OCR 顺序和归属。** 文档名虽为“去重版”，仍可能有截图、转发、昵称和消息顺序错位；涉及重大结论时应回看原始群聊截图。
3. **H2、H3 不是等同 H1 的正式版本发布。** H2 有分支原型，H3 有 oh-my-humanize 项目与群内命名；不要虚构 2.0/3.0 release date。
4. **`humanfia/flowjanus` 暂不可核验。** 只保留群聊原始描述，不补写技术能力。
5. **GLM-5.2 日期冲突。** 群聊段落标 6 月 14 日，官方公告为 6 月 16 日；在原始导出未复核前，不能断言群里提前两天获得发布信息。
6. **厂商 benchmark 是历史材料，不是独立结论。** Anthropic、OpenAI、Kimi、智谱的 Agent 数、步数和榜单可以说明它们如何定义竞争，不宜直接横向比较。
7. **“Claude 领跑、OpenAI 紧追”是社区体验框架。** 可以由产品发布时间和群友即时反应支撑，但“领跑”需注明评价维度，例如 coding agent 可用性、长程任务、并行调度或工具生态，不能写成无条件事实。
8. **AutoGPT 与 OpenClaw 不得混称。** AutoGPT 可作为 2023 年前史；本群聊中的“龙虾”应按证据写 OpenClaw。

## 九、可直接用于小册子的历史主线（保守版本）

综合群聊和一手资料，可用四条并行方向组织材料，而不强行制造单线因果：

- **模型与产品竞争：** Claude Code 较早建立 coding agent 的产品心智；OpenAI 通过 Codex CLI、云端 Codex、Codex app 和 GPT-5.x 系列持续追赶；国产与开源模型随后在长上下文、并行 Agent、coding CLI 和开放权重上密集出现。
- **从“模型能力”到“系统能力”：** 社区逐渐把可靠性归因于上下文、状态、反馈、独立 review、权限、Git 和机械约束，即 Agent Harness，而非只靠更长 prompt 或更强模型。
- **从单 Agent 到多 Agent，再回到协作成本：** Agent Teams 和数十/数百 Agent 的实验制造了冲击，但群内很快讨论 token 成本、通信污染、任务边界和共享状态，说明“并行”本身并不是答案。
- **Humanize 自身的三次抽象：** H1 是可工作的 RLCR loop；H2 把 flow 变成人可构建、检查的语言/平台；H3/OMH 探索由 Agent 在运行中创建和修改 flow。到 7 月，社区又重新评价 H1，显示这不是简单的版本替代史，而是围绕“人、Agent 与流程谁控制谁”的往复探索。

这四条主线与月度原始材料并置，既能保留历史感，也允许后续作者自己判断哪些是真正的转折点。
