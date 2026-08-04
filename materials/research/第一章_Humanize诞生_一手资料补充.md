# 第一章「Humanize 诞生」一手资料补充核查

> 用途：给第一章写作提供可回查的史料底稿，不替正文下最终判断。核查截止于 2026-08-04。
>
> 状态说明：**已证实**＝厂商公告、官方文档、公开仓库或提交可直接核对；**群聊口述**＝聊天记录中有明确原话，但只能证明当时有人这样说；**作者亲历待核验**＝刘思皓或泽文以第一人称讲述自身经历，可信度高，但缺少完全对应的公开工程记录；**未确认**＝现有材料不足，不猜。

## 一、先给第一章的几项纠偏

1. **Humanize 的公开工程起点是 2026 年 1 月 12 日，思想起点则只能按刘思皓的回忆写到 2025 年 11 月。** 前者有首提交，后者是群聊亲历口述，二者不能写成同一种证据。
2. **公开证据不支持“Humanize 原本是内部项目”或“为 QEMU/Jimu 重构而生”。** 首版 README 明说它 derived from 公开的 GAAC；群聊说的是“给自己写代码方便的小工具”“为了加速器科研搞的 side project”。
3. **Anthropic 的编译器项目叫 CCC（Claude’s C Compiler），不是 CBNC。** 官方实验是 16 个 Agent、近 2,000 次 Claude Code 会话、两周、约 10 万行、近 2 万美元。群里另一个“22 个 Agent、3 小时、4.7 万行”的数字是成员自己的工程实践，不能移植到 CCC。
4. **Zevorn 的 `tcg-rs`、QEMU performance modeling、Cosim GPU 是不同工程线；Machina 是 `tcg-rs` 的后继。** 它们均晚于 Humanize v1，更适合写成 Humanize 出现后的工程验证窗口，而不是 Humanize 的起源。
5. **“Swarm mode”是群聊里的非正式叫法。** Anthropic 的正式名称是 Agent Teams；Subagents、Agent Teams、`/batch` 是三种不同机制。
6. **“Harness 工程就是控制论”是 Humanize 群的概括，不是 OpenAI 文章的原话。** 它很适合做思想史材料，但要把“官方事实”和“群内解释”并排呈现。
7. **OS3DC 与“《Primates》的作者”均未找到可靠对应。** 不建议为了让章节完整而补猜。

## 二、Humanize 的名字、作者与起源

### 2.1 刘思皓身份

- **已证实｜长期有效资料**：[Sihao Liu 的 UCLA 个人主页](https://web.cs.ucla.edu/~sihao/)明确写道英文名为 Sihao Liu，中文名为“思皓”，研究方向包括领域专用加速器、RISC-V、FPGA 原型与 VLSI。其 [GitHub 账号](https://github.com/SihaoLiu)与 Humanize、GAAC 提交中的作者身份一致。
- **群聊口述｜2026-03 至 07**：聊天记录稳定使用“刘思皓”这一群昵称。OCR 偶尔把名字识别成“刘诗楠”等，引用时应按上下文校正，不要照抄 OCR 错字。
- **出版建议**：可写“Humanize 的主要发起者刘思皓（Sihao Liu）”；不宜仅凭旧插件 metadata 中的组织名 `humania-org` 判断个人作者。

### 2.2 “Humanize”这个名称能确认到什么程度

- **已证实｜2026-01-12**：[Humanize v1.0.0 首提交](https://github.com/PolyArch/humanize/commit/888451dbe0baf71b006f03961b7eb06939c100bf)已经使用 Humanize 名称，并将系统定义为 RLCR（Ralph-Loop with Codex Review）。
- **群聊口述｜2026-03-22**：刘思皓只留下了一句“我懂了 humanize 败在了名字上”，没有解释名称的词源或命名过程。[聊天记录 L928–L935](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:928)
- **未确认**：现有仓库、群聊与个人主页都没有找到“为什么取名 Humanize”的正式说明。可以解释它后来承载了 human-in-the-loop 的思想，但不能倒推这就是最初命名理由。

### 2.3 起源：能证实的链条是 GAAC → Humanize

- **已证实｜2025-12-22 / 2026-01-05**：[GAAC 仓库](https://github.com/SihaoLiu/gaac)创建于 2025-12-22；最早公开提交是 2026-01-05 的 [`initial commit`](https://github.com/SihaoLiu/gaac/commit/f99231886420996358769a89a34a729d2c8d0507)。GAAC 的全称是 GitHub-as-a-Context，重点是把 GitHub Issues、PR 与 Projects 作为 Agent 的持久上下文。
- **已证实｜2026-01-08 至 01-11**：GAAC 依次加入 [`ralph-loop-with-codex-review`](https://github.com/SihaoLiu/gaac/commit/e577cf6c7c3895e503ee42dcf565c2e3e09cc28d)、[Goal Tracker](https://github.com/SihaoLiu/gaac/commit/40425a9014bcc5a10d4a215d503eaf058c330416)和[停滞熔断器](https://github.com/SihaoLiu/gaac/commit/a6d18129a342fe3d086cb7014581faf5ac4c676e)。这三项随后成为 H1 的骨架。
- **已证实｜2026-01-12**：[Humanize 初版 README](https://github.com/PolyArch/humanize/blob/888451dbe0baf71b006f03961b7eb06939c100bf/README.md)明确写着 “Derived from GAAC”，并把系统收束为 Claude 实现、Codex 独立 review、Goal Tracker、Full Alignment Check 与 Circuit Breaker。
- **已证实｜2026-01-14**：GAAC 的[弃用提交](https://github.com/SihaoLiu/gaac/commit/ae5d075050a4c56d4c63dcf54b7a7a95705d93f5)把用户指向 Humanize，公开迁移关系闭环。
- **群聊口述｜2026-04-02 至 04-03**：刘思皓回顾，GAAC 曾包含超过 60 个 Agent 的复杂交互；经历失败后“全部删掉”，只保留 Ralph loop with Codex Review，并直说“gaac -> humanize 就是这么来的”。[聊天记录 L5859–L5867](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5859)

### 2.4 “内部项目、QEMU、Jimu”核查

| 命题 | 状态 | 核查结论与证据 |
| --- | --- | --- |
| Humanize 最初是公司/实验室内部项目 | **未确认** | 公开仓库链条是 GAAC → Humanize；群聊称“给自己写代码方便造的小工具”“一个 side project”，没有“内部项目”原话。[L5231–L5235](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5231) |
| Humanize 为 QEMU 重构而生 | **不支持** | Humanize v1 首提交为 2026-01-12，Zevorn 的 `tcg-rs` 创建于 2026-02-08，后续 QEMU performance modeling 又在 3—4 月出现；时间顺序相反。|
| Humanize 用于重写刘思皓读博项目 | **作者亲历待核验｜2026-04-02** | 刘思皓说自己开了 5 个 RLCR，把读博期间的项目转成 Rust 重写，并称 Humanize 是“为了做加速器科研搞的小工具”。未找到能与这句话唯一对应的公开仓库。[L5263–L5271](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5263) |
| Humanize 用于 Zevorn 的 QEMU 工程 | **作者亲历待核验，部分有公开痕迹** | 3 月 31 日泽文说“让 Humanize 规划并 fork 了 QEMU”；4 月 21 日又描述 QEMU 性能模拟与最长四天的 Humanize run。[L4470–L4484](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4470) [L12908–L12935](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12908) |
| Jimu 与 Humanize 起源有关 | **未确认** | 聊天全文及当前项目资料未找到 `Jimu` 的可靠命中。可能是项目别名、OCR 误差或未公开项目；暂不写入事实叙述。|

## 三、Humanize 1（H1）的可核验时间轴

| 日期 | 事件 | 状态 | 适合支持的叙述 |
| --- | --- | --- | --- |
| 2025-11 | 刘思皓称“去年 11 月份开始搞 Humanize” | **作者亲历待核验** | 可作为思想起点的口述，不可写成公开发布日期。[L19166–L19170](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19166) |
| 2025-12-22 | GAAC 建仓 | **已证实** | Humanize 的公开前身出现。|
| 2026-01-05 | GAAC 首提交 | **已证实** | GitHub-as-a-Context 进入公开工程历史。|
| 2026-01-08 | GAAC 加入 Ralph Loop with Codex Review | **已证实** | Claude build / Codex review 的核心回路出现。|
| 2026-01-10（UTC） | Goal Tracker 提交 | **已证实** | 用 immutable goal/AC 与 mutable tasks/evolution 防止长程漂移。|
| 2026-01-11（UTC） | Circuit Breaker 提交 | **已证实** | 以周期性全局审查检测停滞并终止循环。|
| 2026-01-12 | Humanize v1.0.0 首提交 | **已证实** | H1 正式公开起点；仓库创建时间为同日。|
| 2026-01-14 | GAAC 标记弃用，转向 Humanize | **已证实** | 前身到新项目的迁移完成。|
| 2026-03-12（美西）/ 03-13（UTC） | 加入 methodology analysis | **已证实** | Humanize 开始在循环退出时反思自身方法论，并在用户同意后提交脱敏 issue。[提交](https://github.com/PolyArch/humanize/commit/29a528fbd6b8ff97be5c60443047d5d2d193f89f) |
| 2026-03-26 | 群里用“群友就是 CI”概括真实项目反馈 | **群聊口述** | H1 的评测路径不是传统单元测试，而是从真实 run 收集失败模式。[L2453–L2467](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:2453) |
| 2026-03-30 至 04-01 | issues #53—#60 集中出现 | **已证实 + 群聊口述** | 方法论反馈飞轮开始实际运转。|
| 2026-04-14 | 群里确认组织从 `humania-org` 换到 `PolyArch` | **群聊口述** | 可解释旧链接为什么跳转；理由“免得老板不开心”只宜保留为口述。[L8323–L8335](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:8323) |
| 2026-04-20 | 刘思皓提出重写 H2，强调上下文压缩、脚本机械化、less is more | **群聊口述** | H1 的成功同时暴露了过重、占上下文、会被模型吸收的问题。[L11498–L11524](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11498) |
| 2026-04-30 | [PR #51](https://github.com/PolyArch/humanize/pull/51) 合并 v1.16.0 开发线 | **已证实** | H1 后期最清晰的正式里程碑之一。|

第一章若只写“某天灵光一现做出 Humanize”，会遗漏真正重要的变化：公开提交显示，H1 是从 GAAC 的复杂流程中持续做减法，最后留下跨模型 review、目标锚定、周期性全局对齐和熔断；3 月以后又把真实 run 的失败反过来变成方法论数据。

## 四、Anthropic C 编译器实验：CCC，不是 CBNC

### 4.1 官方实验数据

- **已证实｜2026-02-05**：官方文章的准确标题是 [Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler)，作者 Nicholas Carlini；仓库名为 [CCC — Claude’s C Compiler](https://github.com/anthropics/claudes-c-compiler)。没有找到 CBNC 这一官方名称。
- **已证实**：实验使用 Opus 4.6 与 Agent Teams；16 个 Agent 从头构建 Rust C 编译器，近 2,000 次 Claude Code 会话、两周、20 亿 input tokens、1.4 亿 output tokens、成本略低于 2 万美元，产出约 10 万行。
- **已证实**：文章发布时，它能构建 Linux 6.9（x86、ARM、RISC-V），也能编译 QEMU、FFmpeg、SQLite、Postgres、Redis，并通过多数编译器测试集的 99%。这些是 Anthropic 自报实验结果，不是独立 benchmark。
- **已证实**：并行实现很朴素——每个 Agent 在独立容器和工作区运行，通过共享 bare Git repo、task lock 文件、pull/merge/push 协作；作者明确说没有额外通信机制，也没有高层 orchestration agent。
- **已证实**：官方同时承认限制：16-bit x86 阶段仍调用 GCC；文章发布时自有 assembler/linker 仍有 bug；不是 drop-in compiler；生成代码甚至弱于 GCC `-O0`；Rust 代码质量不及专家。当前仓库后来继续演进，不能把今天 README 的能力倒填到 2 月 5 日。

### 4.2 群聊怎样读错、再修正这个实验

- **群聊口述｜2026-03-23**：刘思皓说“CCC 走 Agent Teams 的实验有点把我带偏了”，随后质疑其真实有效部分可能更接近 `/batch`，并主张实现小兵不直接通信、由 leader 汇总。[L1023–L1069](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1023)
- **群聊口述｜同日**：“22 个 agents、3 小时、纯增量 47,000 行、一次性编译正确”是群成员自己的工程实践。[L1029–L1058](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1029) 它不是 CCC 的官方数据。
- **群聊口述｜同日**：讨论没有简单否定并行，而是把问题改写成：是让 peers 互相通信，还是用主 Agent 拆分任务、worktree 隔离与 Git 合并？刘思皓甚至承认自己有 Humanize + Agent Teams 的成功反例，只是 `/batch` 的规模和体验更好。[L1089–L1119](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1089)

这一段适合写成“社区从宣传数字退回到编排机制”：震动并非来自 16 或 22 这个数量，而是大家开始追问并行究竟靠通信、隔离、验证还是任务分解获得收益。

## 五、Zevorn 的工程线：五条相邻但不能合并的证据

| 工程线 | 状态与日期 | 可确认事实 | 与 Humanize 的关系 |
| --- | --- | --- | --- |
| [`tcg-rs`](https://github.com/zevorn/tcg-rs) | **已证实｜2026-02-08** | [初始提交](https://github.com/zevorn/tcg-rs/commit/cd9a5f17e44bf7e78fd580484708a6df8855183d)明确是 QEMU TCG 的 Rust reimplementation，含 core IR、x86-64 backend 与 88 tests；署名 Chao Liu，并有 Claude Opus 4.6 co-author。 | 公开提交能确认 Claude 辅助，不能确认初始阶段使用 Humanize。不要写“Humanize 重写了 TCG”。|
| QEMU performance modeling | **作者亲历待核验｜2026-03-31、04-18、04-21** | 泽文描述在 accel 层增加新模式、从 TCG 取 trace、送到 Sparta，尽量复用 QEMU 功能模型，并以香山 gem5 为参考，目标误差 20% 内。 | 群聊明确称用 Humanize，最长单次 run 约四天、整体约一周基本跑通。[L10498–L10529](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:10498) [L12908–L12935](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12908) |
| [`Cosim GPU`](https://github.com/gevico/cosim-gpu) | **已证实仓库 / 群聊对应待核验｜2026-03-08** | [初始提交](https://github.com/gevico/cosim-gpu/commit/878e6aa3e8ad9013318ab3663e3cb177019e9f69)定义 QEMU + gem5 的 AMD MI300X co-simulation：QEMU/KVM 跑 host CPU/system，gem5 提供 cycle-accurate GPU model，以 Unix socket/shared memory 连接。 | [3 月 18 日提交](https://github.com/gevico/cosim-gpu/commit/28fe46f74be50fd6ec316ca9f4da123f3528bb56)把 `.humanize` 加入 `.gitignore`，可证实使用过 Humanize 工作目录。群聊“cosir + MI300X”大概率是 OCR 后的该项目，但原 URL 截断，只能标待核验。[L22–L29](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22) |
| [`Machina`](https://github.com/gevico/machina) | **已证实｜2026-03-30** | [改名提交](https://github.com/gevico/machina/commit/2edec5f9962540b7faf70a0dd90cac2ff0b02de9)明确写 `tcg-rs` 改名为 Machina，并扩展为 Rust full-system emulator。 | [4 月 4 日提交](https://github.com/gevico/machina/commit/2970d5c5cb0010ec590b012fe26ffe635d2f3730)提到计划被移入 `.humanize/plans/`，证明最迟此时在使用 Humanize 产物；不能证明 Humanize 是项目起源。|
| [`Oh My QEMU`](https://github.com/processmission/oh-my-qemu) | **已证实｜仓库 2026-06-01，文章 06-25** | QEMU hardware modeling 的 Agent skills / workflow 项目。 | Zevorn 原文 [Implementing Oh My QEMU with Humanize ideas](https://processmission.github.io/oh-my-qemu/blog/humanize-workflow-oh-my-qemu/)明确说设计 heavily influenced by Humanize，并将 loop、review、memory、checkpoints 与 dynamic flow 用于 QEMU modeling。这是最强的 Humanize → QEMU 下游影响证据。|

补充背景资料：Zevorn 2024 年文章 [The Development and Current State of Rust in QEMU](https://zevorn.cn/posts/23/)是 Rust 进入上游 QEMU 的技术前史，不是 `tcg-rs` 的发布文；2025 年文章 [Simulating MI300X with gem5 and Saving 100k?](https://zevorn.cn/posts/32/)是 MI300X/gem5 的实践前史，也不是 2026 年 `cosim-gpu` 的发布文。

**结论**：这些项目均晚于 Humanize v1.0.0。最稳妥的历史写法是：Humanize 先出现，随后进入 TCG、QEMU 性能建模、GPU 联仿和模拟器等真实 systems workload；这些 workload 又把长程任务、验证、环境阻塞与方法论反馈问题带回 Humanize 社群。

## 六、2026 年 3 月前后的外部一手坐标

### 6.1 Superpowers

- **已证实｜2025-10-09**：[obra/superpowers](https://github.com/obra/superpowers)建仓，定位是 Agent skills framework 与软件开发方法论。
- **已证实｜2026-03-12**：[v5.0.2 对应提交](https://github.com/obra/superpowers/commit/3188953b0c94f76716d862632ee9737a97204f1a)强调 subagent context isolation：派发者应重新构造最小 review context，而不是把父 session 历史整个传给 reviewer。
- **已证实｜2026-03-17**：[v5.0.4](https://github.com/obra/superpowers/releases/tag/v5.0.4)把 spec/plan review 改为一次 whole-plan review，最多三轮，并提高 blocking issue 门槛。
- **已证实｜2026-03-25**：[v5.0.6](https://github.com/obra/superpowers/releases/tag/v5.0.6)又撤掉 subagent review loops。作者称跨 5 个版本、每版 5 次回归测试中，额外 reviewer 带来约 25 分钟开销，却没有可测的计划质量提升，因此改用约 30 秒的 inline self-review。这个反转本身是很好的历史证据：当时大家仍在快速试错，并无固定“最佳实践”。
- **群聊口述｜2026-03-23 至 03-24**：群友观察到 Superpowers 新增“确定 spec 细节 + quiz + review”，随后高度评价 brainstorming 能把模糊想法问成干净 spec 和 plan，再交给 Humanize 执行。[L1235–L1248](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1235) [L1330–L1345](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1330)

### 6.2 Claude Code Remote Control 与 Teleport

- **已证实｜2026-02-24**：[Claude Code v2.1.51](https://github.com/anthropics/claude-code/releases/tag/v2.1.51)加入 `claude remote-control`，使用户能从外部设备控制本地运行、使用本地环境的 Claude Code session。
- **已证实｜当前机制说明**：[Remote Control 文档](https://code.claude.com/docs/en/remote-control)说明文件访问、命令执行与 MCP 仍发生在本机；本地 session 通过 Anthropic API 与 Web/移动端同步。它不是把本地执行环境搬到云端。
- **群聊口述｜2026-03-30**：群里转发 Boris Cherny 的 [X 帖](https://x.com/bcherny/status/2038454336355999749)，截图同时提到 `--teleport`（把 cloud session 接回本机）与 `/remote-control`（远程控制本地 session）。[L3698–L3718](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3698) 书中应把两者分开，不写成同一个“远程接管”功能。

### 6.3 Agent Teams、Subagents、Swarm 与 `/batch`

- **已证实｜2026-02-05**：Anthropic 随 [Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)推出 Agent Teams；[Claude Code v2.1.32](https://github.com/anthropics/claude-code/releases/tag/v2.1.32)明确称其为 research preview、token-intensive，并要求环境变量 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`。
- **已证实**：[Agent Teams 官方文档](https://code.claude.com/docs/en/agent-teams)定义 team lead、独立 teammate sessions、共享 task list 与 mailbox；teammates 可以直接通信，任务通过文件锁避免重复 claim。
- **已证实｜至少 2026-01-20 已存在**：[Claude Code v2.1.14](https://github.com/anthropics/claude-code/releases/tag/v2.1.14)已经修复 parallel subagents 问题。它只能证明此时已有 Subagents，不等于首次发布日期；当前定义见 [Subagents 文档](https://code.claude.com/docs/en/sub-agents)。
- **已证实｜2026-02-28**：[Claude Code v2.1.63](https://github.com/anthropics/claude-code/releases/tag/v2.1.63)加入 `/batch` bundled slash command。
- **群聊口述｜2026-03-23**：群内把能直接互相通信的 teammates 非正式叫“swarm team mode”，并把它与只向 leader 汇报的 subagents 对比。[L1089–L1108](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1089) **未找到 Anthropic 将产品正式命名为 Claude Swarm 的证据。**

## 七、OpenAI Harness Engineering 与群内“控制论”

### 7.1 OpenAI 官方文章能支持什么

- **已证实｜2026-02-11**：OpenAI 发布 [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)。作者 Ryan Lopopolo。
- **已证实**：文章描述的团队从空仓库开始，用 Codex 构建内部 beta；五个月后约百万行代码、约 1,500 个 PR，宣称 0 行人工手写代码、约为手写所需时间的十分之一。这是 OpenAI 团队的自报案例。
- **已证实**：文章核心措辞是 “Humans steer. Agents execute.” 人类的工作转向设计环境、表达意图与建立 feedback loops。
- **已证实**：重要机制包括：把仓库知识当 system of record；让短 AGENTS.md 做目录而不是千页手册；把计划、架构、技术债版本化；让 Agent 可读 UI、logs、metrics、traces；用 linters、CI 与结构测试机械执行架构原则；周期性运行清理 drift 的 Codex tasks。

### 7.2 Humanize 群如何把它翻译成“控制论”

- **群聊口述｜2026-03-20**：面对 Codex 产出“能跑就行”的代码，成员提出观测、验证、测评，而不是人亲自下场修；随后直接说“Harness 工程就是控制论”。[L656–L686](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:656)
- **群聊口述｜2026-03-21**：群内贴出 OpenAI 原文关于 code drift、每周清理 AI slop，以及把“golden principles”写成机械规则的段落。[L789–L813](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:789)
- **编辑判断**：“控制论”在这里不是严格数学模型，而是群体用来组织实践的隐喻：Agent 是有概率误差的被控对象；tests、review、metrics 与 verifier 提供观测和反馈；hooks、权限、熔断与结构 lint 形成控制输入和边界。可以写成 Humanize 社群的概念创造，不要加引号冒充 OpenAI 原话。

## 八、Humanize 的脱敏方法论反馈机制

### 8.1 机制与时间

- **已证实｜2026-03-12**：[methodology analysis 提交](https://github.com/PolyArch/humanize/commit/29a528fbd6b8ff97be5c60443047d5d2d193f89f)加入退出前方法论分析：Opus 阅读开发记录，生成 sanitized report；用户同意后可协助创建 GitHub issue；`--privacy` 可关闭该功能。
- **已证实｜当前代码**：[methodology-analysis-prompt.md](https://github.com/PolyArch/humanize/blob/main/prompt-template/claude/methodology-analysis-prompt.md)要求只分析可泛化的方法论，不分析具体项目；用户可见 issue 内容只从 sanitized report 派生，并在 `gh issue create` 前征求同意。[loop-read-validator.sh](https://github.com/PolyArch/humanize/blob/main/hooks/loop-read-validator.sh)限制 methodology analysis 阶段可读取的工件。
- **准确表述边界**：这些代码能证明项目意图和访问限制，不能独立证明历史上每一份公开 issue 都绝无重识别风险。正文宜写“按模板与 validator 做脱敏”，不写“绝对保证不会泄漏”。
- **群聊口述｜2026-03-31 至 04-01**：刘思皓把它描述为“你愿意帮助改进 Humanize 吗？”；泽文说此前会让 Claude 手动总结提交。次日群里出现 #54，并强调只研究方法论、用户同意后开 issue，把它称为“方法论的自我迭代”和数据飞轮。[L4454–L4477](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4454) [L4805–L4867](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4805)

### 8.2 五个典型 issue

| Issue | 日期 / 状态 | 真实 run 暴露的问题 | 方法论价值 |
| --- | --- | --- | --- |
| [#53：23-round large-plan](https://github.com/PolyArch/humanize/issues/53) | **已证实｜2026-03-30** | 30 tasks / 7 phases，23 轮、37 commits、约 13.7K 新增行、900+ tests；reviewer 抓到 4 个 critical bugs，但 scope/milestone 不匹配、停滞误报、执行顺序死锁和 emergent architecture 消耗大量轮次。 | 说明 Goal Tracker 能防任务遗忘，却不能自动解决任务粒度、里程碑和动态依赖。|
| [#54：whack-a-mole](https://github.com/PolyArch/humanize/issues/54) | **已证实｜2026-04-01** | 7 轮续跑（此前 18 轮）；第 3—6 轮都在同一子系统逐个修局部问题，耗费 57% implementation rounds，只贡献约 15% value。 | 提议遇到局部缺陷后做 subsystem audit，并引入 velocity signal，而不只看 advanced/stalled 二值判断。|
| [#55：over-claiming](https://github.com/PolyArch/humanize/issues/55) | **已证实｜2026-04-01** | 6/6 轮 implementer 都过度宣称 AC 已完成，reviewer 需靠 build、runtime、reboot 与 scheduling tests 逐次推翻。 | AC closure 应先提交原始测试证据，区分 blocking findings 与 improvement findings。|
| [#57：fix-revert oscillation](https://github.com/PolyArch/humanize/issues/57) | **已证实｜2026-04-01** | 19 轮中，前 4 轮完成 AC，后 15 轮没有新增 AC；同一资源生命周期出现 8 轮 fix-revert，边际价值快速下降。 | 应检测 oscillation、区分 acceptance convergence 与 polishing，并允许持久化 accepted risk。|
| [#60：environment deadlock](https://github.com/PolyArch/humanize/issues/60) | **已证实｜2026-04-01** | 10 轮中外部硬件环境阻塞重复 7 轮；error-handling 缺陷又出现逐层“剥洋葱”。 | 外部阻塞应升级为 human decision request；一次发现调用链问题时应端到端追踪，而非每轮只修一层。|

这些 issue 的史料价值不只是“Humanize 有哪些 bug”，而是保存了早期 coding-agent harness 的失败剖面：虚假完成、局部修复、审查范围膨胀、停滞误判、环境不可验证、长尾质量打磨和任务图失真。

## 九、“好 harness 会被下一代模型 built-in”假说的原话轨迹

这不是一次性提出的口号，而是从 3 月到 7 月不断加强、又被现实反驳的假说。

| 日期 | 群聊原话/观点 | 状态与解释 |
| --- | --- | --- |
| 2026-03-23 | “人类学会把一切有效的东西快速 Builtin”；先做 Skills，常用后进入 built-in，再进 post-train / mid-train。 | **群聊口述**。这是最早清晰版本。[L1096–L1107](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1096) |
| 2026-04-20 | “重的 harness 感觉始终会被模型能力给吃掉”；能机械化走脚本的不要走 LLM。 | **群聊口述**。同时导向 H2 的“少、轻、低上下文”设计。[L11504–L11523](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11504) |
| 2026-05-26 至 05-27 | “很多 harness 技巧都会逐渐被内化”；衡量 flow 的指标是能否在 2—3 个月内被官方选项覆盖。能，说明做对了但要继续演进；不能，可能做错了。 | **群聊口述**。[L26389–L26400](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:26389) [L27542–L27552](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27542) |
| 2026-05-29 / 06-03 | “不被官方内化的 harness flow 没有存在意义”；“不被内化的 skill/harness/workflows，没有存在的意义”。 | **群聊口述**。这是观点最强硬的阶段。[L29640–L29656](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29640) [L33534–L33546](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33534) |
| 2026-07-09 至 07-10 | 模型厂“又给内置了”；“好东西才会被 absorb”；第三方 harness 的必要性是被官方蒸馏；随后观察 GPT-5.6 Sol 主动发起 adversarial review，称模型把 harness 内化了。 | **群聊口述**。[L51965–L51975](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:51965) [L53043–L53050](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:53043) |
| 2026-07-24 | “果然得重新祭出 humanize1 了；说好的不需要 harness 的时代呢。” | **群聊口述**。这是一条重要反证：模型原生 verifier 仍可能不可靠，外部循环重新获得价值。[L62252–L62258](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62252) |

出版时不宜把它写成已经证明的规律。更忠实的表述是：Humanize 社群形成了一套“copy rate / absorb rate”评价观——有效的外部模式会被厂商做成内置能力；但 7 月的回摆表明，内置不等于稳定替代，外部 harness 仍可能在新模型退化、验证不可靠或任务特殊时重新成为必要层。

## 十、Anthropic Blog 的“边际价值递减”：保留反复，不要写成单线失望史

- **群聊口述｜2026-03-26**：群内转发 3 月 24 日发布的 [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)，刘思皓说这是自己读过“收获最少”的 Anthropic 文章，“居然没有收获一点东西”“被 Humanize 完爆”，并对官方最长约 6 小时 run 与群友睡觉编程作比较。[L2468–L2493](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:2468)
- **群聊口述｜2026-04-17**：看到 Boris 的 4.7 best-practice tweet 后评价“没啥用”“人类学最近博客越来越水了”。[L9382–L9388](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9382)
- **群聊口述｜2026-04-19**：两天后又说当前 AI 方法论优质来源第一是 Boris Twitter 与 Anthropic Blog，第二是朋友口口相传的经验。[L11389–L11394](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11389)
- **群聊口述｜2026-05-09**：“半年前人类学每发一篇博客我都熟读并背诵，最近的博客质量越来越低。”[L18813–L18818](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18813)
- **群聊口述｜2026-06-15**：又认可 Anthropic Blog 的建议：新模型到来时重新检查 harness，删去已不再承重的部分，再加入过去不可能的能力，并用 Occam’s razor 控制复杂度。[L43312–L43320](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:43312)

这组记录更像“读者位置变化”而非单纯博客降质：当社区实践跑到多日、多轮、真实系统项目后，官方文章里曾经新鲜的 initializer、handoff、planner/generator/evaluator 对他们的边际信息量下降；但只要文章提出与当下问题吻合的新原则，他们仍会吸收。因此可写“边际价值递减与选择性吸收”，不要写“从此不看 Anthropic Blog”。

## 十一、OS3DC 与“《Primates》的作者”：未确认清单

### 11.1 OS3DC

- **未确认**：聊天全文、humanize-book 当前材料、Zevorn 的公开 GitHub 与博客均未找到 `OS3DC` 命中。
- **已排除的同名项**：公开网络能搜到的 OS3DC 主要是德国旧的 Open Source 3D Printer Convention，与 Zevorn、Humanize、Agent 或 QEMU 没有连接。
- **高可信勘误候选，但仍需回看原稿**：如果这里指泽文在 2026 年 3 月 28 日参加的开源操作系统会议，准确缩写应是 [OS2ATC](https://os2atc.cn/)（Open Source Operating System Annual Technical Conference），不是 OS3DC。官方[奖项页](https://os2atc.cn/award.html)可核对活动日期为 2026-03-28，并列出“刘超（泽文）”获得 OpenCamp 训练营特别贡献奖。它能证实人、会与日期，尚不能单独证实当天展示内容。
- **建议**：原稿上下文若是 3 月 28 日会议，优先改作 OS2ATC；若不是，则仍按 OCR、简称或未公开项目处理，不收录事实性叙述。

### 11.2 “《Primates》的作者”

- **未确认**：聊天全文对 `Primates`、`Primate`、`灵长`均无命中，无法还原所谓原话。
- **否证性线索**：当前唯一语境完整的“作者在群里”出现在 5 月 15 日，前文是《Humanize 带来的 Codex 使用范式变化，解锁 Agent 优化 kernel 上限》，随后有人说“作者在群里吧 @BBuf”。它与 Primates 无关。[L21430–L21443](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21430)
- **高可信勘误候选，但不倒推原话**：如果 `Primates` 实际想记录的是 Superpowers 的作者/团队，官方 [Superpowers README](https://github.com/obra/superpowers#community)写的是 “built by Jesse Vincent and the rest of the folks at Prime Radiant”。正确专名是 **Prime Radiant**，主要作者是 **Jesse Vincent**；这是一条仓库事实，但聊天中没有 `Primates → Prime Radiant` 的文本连接。
- **无关同名候选**：Macmillan 的图像小说 [Primates](https://us.macmillan.com/books/9781250062932/primates/)作者为 Jim Ottaviani、绘者 Maris Wicks，主题是 Goodall、Fossey 与 Galdikas；没有任何文本证据把它与 Humanize 群联系起来。
- **结论**：不猜作者。优先回到未 OCR 的原始导出或截图，检查是否其实是 `Primitives`、某个项目名或文章标题。

## 十二、第一章可直接采用的保守叙述骨架

如果第一章要讲“Humanize 的诞生”，一条证据上站得住、又保留历史感的骨架是：

1. 2025 年底，刘思皓先做 GAAC，尝试用 GitHub 工件和复杂 Agent 交互组织长程开发；公开仓库从 12 月建仓、1 月初密集提交开始留下痕迹。
2. 多次失败以后，他把系统做减法，抽出 Ralph loop + Codex independent review，再加 Goal Tracker、Full Alignment 与 Circuit Breaker。2026 年 1 月 12 日，Humanize v1.0.0 公开。
3. Humanize 不是在真空中被“设计完成”的。3—4 月，群友把它用于 QEMU、GPU modeling、模拟器、编译器和大规模重构；多日 run 暴露了虚假完成、打地鼠、fix-revert、停滞误判和环境死锁。
4. 这些失败通过脱敏 methodology issue 反哺项目，令社区把 harness 理解为观测、验证、反馈、熔断和人的主动介入——也就是他们口中的“控制论”。
5. 同期 CCC、Agent Teams、`/batch`、Superpowers 与 OpenAI Harness Engineering 提供了外部参照。社区不是简单追随厂商，而是不断用自己的工程数据质疑 peers 是否需要通信、review 是否值得成本，以及哪些 flow 会被下一代模型内化。
6. 到 4 月下旬，H1 的成功已经孕育了对 H2 的需求：更轻、更少上下文、更机械化、模型无关。但 7 月“重新祭出 Humanize 1”的反转提醒我们，这不是旧版本被新版本淘汰的直线历史，而是模型能力与外部约束不断重新分工的过程。

这套骨架刻意不写“QEMU/Jimu 催生 Humanize”、不把 CCC 与群友的 22-Agent 实验混在一起，也不把“harness 被内化”写成已证实定律。它允许正文保留故事性，同时让每个关键转折都能回到仓库、文章或群聊原行。
