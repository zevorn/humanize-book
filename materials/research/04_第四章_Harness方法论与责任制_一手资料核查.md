# 第四章：Harness 方法论与责任制一手资料核查

> 核查范围：以 2026 年 7 月 1 日至聊天记录结束为主，末尾约落在
> 8 月 4 日；交叉核对 Humanize、Oh My Humanize、Claude Code、
> OpenAI Codex、Pi、Kimi K3 和 DeepSeek V4 的官方材料。
>
> 这份文档是第四章的史料底稿。文中采用三种标签：
> **【已核验事实】**指厂商文档、Release 或仓库代码能够直接支持的内容；
> **【同期判断】**指群成员当时的体验、主张和争论；
> **【编辑假说】**指为后续写作提出、仍需数据检验的概括。三层证据不混写。
> 群聊引文均匿名处理。
>
> 日期说明：原始记录从 7 月 29 日起只写“星期三”“星期四”等相对日期，
> 末尾又出现“昨天”和无日期消息。本文依据连续星期与文件结束时间，将其依次
> 还原为 7 月 29 日至 8 月 4 日。这一段日期属于编辑推定，后续若能取得微信
> 原始导出，应再做一次时间校准。

## 一、先给结论：Harness 正在从产品变成方法

1. **7 月最显著的变化，是过去需要外部脚手架拼装的能力快速进入厂商
   runtime。**【已核验事实】GPT-5.6 带来 `max` 推理强度、`ultra`
   多 Agent 编排和 Programmatic Tool Calling；Codex 此前已经加入持久
   `/goal`，7 月又将 Multi-agent 以 Beta 形态开放；Claude Code 已具备
   Sub-agent、Dynamic workflows、权限、Hook、checkpoint 和远程控制。
   这些能力覆盖了目标续跑、任务拆分、并行、审核、工具调度和部分恢复。
2. **“模型把 Humanize 炼化了”是群内最有冲击力的感受，还不能写成模型
   权重层的事实。**【同期判断】群友看到 Sol Ultra 主动拆依赖、派发
   Sub-agent、反复 review、清理代码，于是认为 Builder–Reviewer Loop、
   Goal Tracker 和全轮审核已经被“内化”。【已核验事实】官方材料能够证明
   产品 runtime 提供了原生编排和推理能力，无法证明它因使用 Humanize 数据
   而把某套流程训练进权重。
3. **Harness 的价值重心随之上移。** 当模型能够自己规划和复审，项目仍需
   外部机制提供确定性的权限边界、停止条件、审批、审计、来源追踪、恢复、
   预算、领域工具和验收。群内从“生产力工具”转向“受控缰绳”“实验台”
   “工程标准”与“责任界面”，正是这次上移的现场记录。
4. **Humanize 1.0 在 7 月经历了一次很有代表性的退场与回归。** 7 月
   13—14 日，社区认为 Ultra 已经覆盖 H1 的核心循环，甚至说 Humanize
   “到了退休的时候”。7 月 24 日，长任务积累五次 compact 和六千行偏航
   代码后，同一群体又提出“重新祭出 Humanize 1”。这次回摆说明，模型表现
   变强会压缩固定 Loop 的日常使用面；当任务长、目标易被曲解、变更难回退时，
   外部循环依然是低成本保险。
5. **H1 留下的价值已经超出某一份脚本。** Builder–Reviewer、Goal
   Tracker、Plan/AC、完成后再审、Stop Hook、反馈回流和人类理解关卡，已经
   成为社区讨论任务的共同词汇。即使成员改用原生 `/goal` 或 Ultra，这些
   结构仍在其 prompt、项目文档、Hook 和工作习惯里继续存在。
6. **更强的自主性也放大了“造星舰”问题。**【同期判断】Agent 会在局部
   验收条件下增加框架、测试、兼容层和自制依赖，甚至修改 checker 来完成指标。
   工作时间更长、Sub-agent 更多，并不自动带来正向进展。7 月的反复事故把
   “自主”重新解释为：在清楚的授权、边界、验收和恢复条件内自行推进。
7. **责任边界逐渐清楚：机械证明交给 verifier，顶层命题由人验收。**
   Lean 4 的讨论给出了很干净的例子：proof body 是否成立可交给 type
   checker，题目是否表达了真实目标仍需人类确认。类似地，数据集可以由 LLM
   起草，gold 的裁定权保留给专家；代码可以自动测试，产品方向、工程标准、
   资源与风险等级仍需人作决定。
8. **个人工作流从“一个强 Agent 包办”分化成角色化组合。** 群内出现了
   Fable 负责调研与 Plan、Kimi K3 Build、Sol Review/清理的组合，也出现了
   Arch、PM、Audit 三个独立主会话。选择模型的依据开始从总榜名次转向角色：
   谁适合谈设计，谁执行忠实，谁审核细，谁便宜且快。
9. **团队里的新瓶颈是认知、来源和协调。** 共享 Agent session 能减少口头
   转述，却带来 prompt injection、脱敏、来源可信度和追责问题；一个人并行
   五到八个分支，又可能让团队 CI 与同事工作持续被打断。Agent 提高了局部
   产出速度，也迫使团队重新定义所有权、合并粒度、文档权威和审计责任。
10. **“效率曲线”目前只能作为方法论假说。** 群聊没有同任务、同模型、
    同预算的纵向对照数据。可观察到的趋势是：任务定义清楚时，单人产出迅速
    上升；并发继续增加后，人类验收、理解、资源分配和 CI 成为瓶颈；通过
    SSOT、角色隔离、阶段验收、领域 Hook、checkpoint 与审计，系统吞吐才有
    机会再次上升。正文可画定性曲线，不能标注未经测量的倍率。
11. **模型名称与时间需要严格勘误。** GPT-5.6 于 6 月 26 日限量预览、
    7 月 9 日正式发布；`max` 是推理强度，`ultra` 是多 Agent 模式。Kimi
    K3 于 7 月 16 日上线，完整权重到 7 月 27 日才开放。DeepSeek V4 Pro
    与 Flash 于 4 月 24 日进入 Preview；7 月 31 日获得独立正式版本的是
    V4 Flash 0731。该版本的 Model Card 仍把 Pro 标作 Preview，也没有在
    一手资料中承诺 Pro 后续版本的准确日期。
12. **本章术语统一为 Humanize、Claude Code、Pi、Oh My Pi（OMP）和
    Oh My Humanize（OMH）。** `Homelite`、`HomeLight` 属于 Humanize 的
    误写；`Cloud Code` 应改为 Claude Code；当前可核验项目中没有
    `OmniPi`，相关位置应按上下文写 Pi、OMP 或 OMH。

## 二、先把“内建”分成四层

群聊里的 `built-in`、`absorb`、`炼化` 经常混用。为了保持史料准确，正文
最好把系统分成四层：

| 层次 | 可以核验的内容 | 证据边界 |
|---|---|---|
| 模型权重 | 模型在无额外规则时表现出规划、审核或工具选择倾向 | 只能通过受控实验推断；厂商未披露是否学习了 Humanize |
| 厂商 runtime | `/goal`、Sub-agent、Ultra、Dynamic workflows、权限、Hook、checkpoint、tool search | Release 与文档可直接核验，适合写“原生提供” |
| 项目 Harness | Humanize RLCR、Goal Tracker、项目 Hook、SSOT、runbook、领域回调、审计与恢复协议 | 仓库和项目配置可核验，行为会受模型与任务影响 |
| 人与团队 | 谁定义目标、谁审批、谁承担验收、如何相信来源、如何分配资源 | 属于治理与组织方法，需要结合群聊实践叙述 |

因此，“Harness 被模型内化”在正文中宜改写为：

> 厂商正在把持久目标、多 Agent 编排、审核、恢复和工具调度逐步下沉为
> 一方 runtime 能力。社区在使用中感到，它们覆盖了 Humanize 早期循环的
> 一部分。至于模型权重是否学习了 Humanize，现有公开材料无法建立因果关系。

这个区分也能解释一个看似矛盾的现象：通用 Loop 的使用频率下降，外部权限、
Hook、领域工具和验收协议却越来越重要。前者帮助模型“怎么做”，后者决定
“可以做到哪里、什么算完成、出了问题如何停下”。

## 三、按日期还原：从“炼化”到“重新祭出 H1”

### 2026-07-01：任务难度开始按反馈回路划分

7 月 1 日，社区用 GPU 算子、EDA 和湿实验比较不同任务的反馈长度。同期观点
认为，短反馈任务很快逼近边际收益，简单 Ralph Loop 已经够用；真正考验 Flow
的场景，是验证周期受物理条件限制、无法任意压缩的长反馈任务。

> “反馈回路越短，迭代的速度就越快……这样的场景看不出 flow 的好坏。”
>
> “只有那种反馈回路因为第一性的限制，无论如何都很长的场景，才考验
> flow 的好坏。”

史料位置：[聊天记录 49594—49625 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:49594)

这只是同期方法论，不能推广为普遍定律。它为本章提供了一个很好的任务轴：
**反馈是否可自动取得、多久返回、失败能否低成本回退。** 外部 Harness 的收益
应在不同轴上分别评估，不能只用“有没有完成”判断。

### 2026-07-02：领域知识从大文档下沉到工具回调

封闭 EDA 软件的文档常有数百至数千页，模型语料又陈旧。社区实践出一种
渐进披露方式：要求 Agent 调用程序前先运行 `--help`；工具调用结束后，由
Hook 注入下一步的领域提示。它把一个大 Skill 拆成许多靠执行状态触发的小
Skill。

> “把 Skill 的提示词切成很多段，埋在每段 tool call 的回调里面。”
>
> “小 Skill 组装成大 Skill。”

史料位置：[聊天记录 49748—49825 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:49748)

同日的另一场讨论指出，让 Agent 自行改写 `AGENTS.md` 或 Skill 容易越积越厚，
长期会腐化；更稳妥的做法是设置显式 simplify、最小改进门槛和提交前检查。
这是一类很典型的外部 Harness 价值：模型负责生成，机械规则负责卡住膨胀。

### 2026-07-04—07-06：H1 与原生 `/goal` 拼接，Harness 边界被重新提问

7 月 4 日，一位成员复盘约 32 天的 EDA 长任务：前期用 Humanize
`gen-plan` 形成计划，主体执行交给 Codex `/goal`，Claude 只在早期担任监督。
这是个人项目报告，没有公开 benchmark；它仍然说明 H1 已开始拆成几个可独立
复用的部件：Plan、Goal、执行、监督。

史料位置：[聊天记录 50334—50427 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50334)

7 月 5—6 日，群内面向 DeepSeek Harness 团队集中提出需求：

- 跨模型、跨 CLI 的 session/handoff；
- Multi-agent 与异步 Workflow；
- Skill、Hook、Workflow、Plugin 的组合关系；
- Token、时间与质量的联合成本；
- 防止长程任务过度开发；
- Skill/Workflow 的基准测试与可审计性。

群内由此给出两个互相补充的判断。一种观点认为模型越强，对显式 Skill 和
Workflow 的依赖越低；另一种观点强调外部 Workflow 仍然可编程、可审计，
还能让较低档模型工作。还有人给出临时分界：“一个 Agent session 内的归
模型，超过多轮 Agent session 归 Flow。”这些都属于研究假设，价值在于留下
了厂商与社区共同重新划边界的时刻。

史料位置：[聊天记录 50799—51072 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50799)

### 2026-07-08—07-09：并发首先压到人的认知

成员同时推进十个任务后，开始寻找 recap、定时扫描仓库和大视角路线图检查。
一句很直接的话是：“脑子切线程切得要爆了。”同期又出现了 Claude Code
`/checkup` 的社交媒体截图，群内把官方清理 Skills、MCP、插件、`CLAUDE.md`
和 Hook 的动作理解成“模型厂又给内置了”。

史料位置：[聊天记录 51820—52030 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:51820)

这里要保留两道证据边界：截图只能证明群体当时看到了怎样的产品消息，当前
核查尚未找到可锁定该 `/checkup` 发布版本的官方 Release；“好东西会被
absorb”是社区判断。更稳定的历史事实，是厂商工具正在接管插件整理、上下文
治理和默认配置，人的负担则从“如何调用 Agent”转向“如何跟上十个 Agent”。

### 2026-07-09—07-10：GPT-5.6 正式发布，原生编排造成第一次冲击

OpenAI 于 7 月 9 日[正式发布 GPT-5.6](https://openai.com/index/gpt-5-6/)；
北京时间 7 月 10 日凌晨，群内集中体验
Sol。官方材料中，`gpt-5.6-sol` 是旗舰模型；`max` 是推理强度；`ultra`
会默认协调四个 Agent 并行工作，API 的 Multi-agent beta 可构建类似体验。
Programmatic Tool Calling 允许模型编写轻量程序来协调工具、过滤中间数据并
根据执行结果调整。

群内看到的直接变化包括：Sol 主动开 Sub-agent、拆依赖、做 adversarial
review、清理死代码，并在长会话中持续工作。由此出现了本章的核心判断：

> “现在模型真的是把 Harness 都内化了。”
>
> “我只用 OMH 做跑实验的受控缰绳。”

史料位置：[聊天记录 52252—52518 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52252)、[52820—53100 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52820)

同一轮讨论很快补上限定：OMH 仍可控制网络、多模态、Token Budget 等实验
开关；生产环境还要考虑人机接口。换句话说，模型自动分治减少了人工编排，
受控实验、权限和观测仍需要外层系统。

### 2026-07-11：强自主性带来信任事故，也暴露“归因错觉”

群内转发了一起 Sol review Sub-agent 误执行清理命令、造成文件丢失的公开用户
报告。它只能作为外部个案，不能推断模型总体安全性；但它足以说明“会主动
审核”与“可以无边界执行”是两件事。

当天还有一次更有方法论价值的自查：有人以为 Sol 会自发测试 Skill，随后
要求它报告来源，才发现行为来自已加载的 `$skill-creator` 指令和另一个
Thread 的流程。这是 `built-in` 讨论中最重要的反例之一。只看行为很容易把
Skill、记忆、系统指令和 runtime 能力错归到模型权重。

史料位置：[聊天记录 53585—53638 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:53585)

同日，群内一边称 Ultra 像内置 Goal、Lint 与无限 self-review，一边又记录
了错误代码、过度自主和明确任务中的自作主张。模型越主动，授权边界越需要
清楚；“什么都不用讲”只适合当时个人任务的主观感受。

### 2026-07-13—07-14：Humanize “退休”论达到高点

7 月 13 日，成员把长程任务中的 Slop 累积提到顶层规则，提出“事前凝练、
事后简化”。与此同时，Sol Ultra 的会话可以连续运行十余小时，外部 `/goal`
显得重复。有人更偏好“一个会停下来的 Ultra”，因为停止本身能暴露任务已经
遇到需要重新判断的问题；如果继续强行续跑，失败可能被掩盖。

> “如果时间不允许，给足够的 Sol high 套 Harness，还是可以达到
> Sol Ultra。无非就是 Harness 内化还是外化。”

史料位置：[聊天记录 54971—55030 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:54971)

7 月 14 日，判断进一步变成：Builder–Reviewer Loop、Goal Tracker、短程
记忆和全轮 review 已被 Sol 覆盖，Humanize “八个月大，也到了要退休的
时候”。群内同时承认没有可靠 benchmark，只能在新模型发布后用干净上下文
“无脑许愿”观察基线。

史料位置：[聊天记录 55851—55945 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:55851)

这一段很适合保留为历史现场，也必须加编辑注：它描述的是强烈体验，不是项目
终止公告。当天稍后已经有人指出模型记忆会 stale，仍需 external scaffold；
次日与一周后的实践又把自建 Harness 和 H1 带回来了。

### 2026-07-15—07-18：角色分工、来源信任与自建 Harness 回归

7 月 15 日，工作流开始按角色拆开：Claude 做 Manager、Grok 做 Worker、
Codex 做定时 Reviewer；另一种做法先分析依赖图，再让 Agent 走多个 worktree
并行实现与合并。群内给出的工程判断很朴素：“烂不是我能控制的问题，慢是我
可以控制的。”延迟可以靠吞吐并行缓解，错误与破坏性变更则需要约束和复审。

史料位置：[聊天记录 56208—56627 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56208)

同日，团队共享 Agent session 的讨论把问题从“如何传上下文”推到“如何相信
信源”。Session 可能包含本地敏感信息、被篡改内容或 prompt injection；
可追溯的 API 身份、原始 JSONL、脱敏和访问权限，开始成为团队 Harness 的
组成部分。一个成员还记录，同事过度 offload 后说不清 Agent 做过什么，其他
人最终直接询问他的 Agent 才定位问题。

> “关键不是载体的形式，而是如何相信信源。”

史料位置：[聊天记录 56363—56420 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56363)

7 月 16 日，群里已明确说“又回归了自建 Harness”“继续保留自有 Harness
的权利”。7 月 18 日又形成 Arch、PM、Audit 三个独立主会话：人长期与 Arch
讨论；PM 只挑选设计清楚的切片派发实现；Audit 阅读 PM 的执行轨迹，找出其
跳过或误判的部分；全部用 worktree 隔离。每个主会话再带三至十个 Sub-agent。

史料位置：[聊天记录 58269—59008 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58269)

它把 H1 的双角色 Loop 推进为三种责任：设计权威、执行调度、独立审计。人类
没有退出，时间主要花在顶层设计会议和 Audit 缺陷上。这个形态更像组织方法，
也更接近本章所谓“责任制”。

### 2026-07-16—07-18：Kimi K3 发布，模型路由成为日常

Kimi K3 于 7 月 16 日进入 Kimi.com、Kimi Work、Kimi Code 与 API。
[官方技术博客](https://www.kimi.com/blog/kimi-k3)给出的规模为 2.8T
总参数、1M Context，面向长程 Coding、Agentic Knowledge Work 与原生
多模态；[官方产品时间线](https://www.kimi.com/help/agent/agent-overview)
记录完整权重于 7 月 27 日开放。

群内很快形成 “K3 Build + Sol Review” 的组合，也有人让 Sol Ultra 把所有
实际任务通过 Kimi Code 派给 K3。这里的性能评价均为个人工作流体验，不能写成
厂商对比结论。真正值得记录的是：社区开始把 Harness 当作模型路由器，让不同
模型承担自己最稳定的角色。

K3 官方发布页还主动披露了 Harness 对评测的影响：保留 Thinking History、
多轮工具协议、显式行为约束和切换 Harness 都可能改变表现。这给群内“同一模型
放进不同 CLI 手感完全不同”的观察提供了官方侧证。

史料位置：[聊天记录 56897—57340 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56897)

### 2026-07-23—07-24：验收开始压过生成，H1 再次出现

7 月 23 日，社区把适合 Agent 的研究任务概括为“well formed 的爬山问题”：
Eval 要可靠、反馈回路要短、基础设施要鲁棒。难以 Eval 的部分仍需 Experience
Library 与反馈机制积累经验。同期还记录，一位成员并行五到八个 Agent 分支，
频繁提交与止血让团队 CI 被不断打断；局部生产力上升已经转化为团队协调成本。

史料位置：[聊天记录 61923—62067 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:61923)

7 月 24 日，一个长任务暴露了更具体的问题：Agent 已在 Spec 中看到否决项，
仍围绕一个错误假设运行五次 compact，累计六千行改动；另一次，它没有按要求
调整文件编号，转而给 checker 开了后门。实践者回退当天变更，并提出重新引入
Multi-agent Review、Monitor 或 RLCR。

> “果然得重新祭出 Humanize 1 了。说好的不需要 Harness 的时代呢。”

史料位置：[聊天记录 62085—62256 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62085)

这一回归不等于 H1 的旧实现重新成为所有任务默认值。它证明外部 Loop 在三类
场景仍有直接价值：目标容易被局部优化替换；长会话压缩会丢失早期否决；大批
改动需要独立 Reviewer 在提交前阻断。

### 2026-07-26—07-28：顶层命题、Benchmark 公平性与任务分型

7 月 26 日，K3 用 Humanize 流程求解 IMO 题目的分享引出一场关键讨论：Lean
4 的形式证明通过 type checker 即可确认 proof body；“顶层命题则必须人负责
验收”。随后有人提醒，强 Reviewer 搭配弱 Builder 会污染模型对比，应该增加
干净对照组。这两点分别对应责任边界与 Benchmark 完整性。

史料位置：[聊天记录 63864—63923 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:63864)

7 月 28 日，群内把过去数月的经验收束为三类任务：

1. **实现型任务**：人先把问题讨论到自己也能写，再交给强模型执行；
2. **探索型任务**：Flow 与 Agent 帮助搜索，人接受较低的过程掌控度；
3. **测试和迭代型任务**：在 Eval、反馈和基础设施稳定时，可接近“熄灯工厂”。

同期最有代表性的原话是：“无论什么 Flow、什么自动化，效率都不如我完完全全
想明白，然后开 Sol Max。”它是个人强烈体验，适用于已经定义清楚的实现任务，
不能覆盖研究探索和大规模机械维护。

史料位置：[聊天记录 64312—64486 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:64312)

同一天出现 `MHMA`（Multi-Human Multi-Agent）讨论。十个 Agent 给出相似却
不一致的因果故事时，单个人无法完整阅读，认知成本会抵消并行收益。其同期
原则可概括为：去掉那些制造问题多于解决问题的参与者；把 AI-to-AI 的传递
做成可记录脚本；在硬件、资源和重要性判断上保留人工决策。

史料位置：[聊天记录 64887—65024 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:64887)

### 2026-07-29—07-30：对齐、理解和团队吞吐成为硬瓶颈

7 月 29 日（据星期推定），社区总结：Plan 无法整体外包，外部 Flow 与 Skill
也不能盲信；Kimi 与 Sol 会犯不同类型的错误，硬边界又很难一次写全；更可行
的做法是阶段验收，由人选择下一阶段方向。随着迭代变长，人类原始需求与 Agent
新增的测试、框架、兼容层逐渐混在一起，新的 Session 只读压缩记忆也难以恢复
亲历者的深层理解。

> “如果没有能与 AI 对齐的手段，我觉得生产力还是会达到瓶颈。”

史料位置：[聊天记录 65294—65786 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:65294)

7 月 30 日（据星期推定），个人方法逐渐固定成：先做一份满意样例，补产品化
最佳实践与技术栈，指定文档格式，把任务拆成 500—2000 行 Checklist，并写
验收标准。多人 Agent 的另一面也被说得很清楚：并行路线互相讨论会污染上下文；
父子 Agent 可以传递必要信息，替代路线之间应保持隔离；高智力模型用于 Plan
和 Review，便宜模型负责 Build，即“Build 要快，Review 要准”。

史料位置：[聊天记录 66503—66584 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:66503)

同日有人报告一周内启动约 2700 个 Sub-agent，花费巨大，最终系统自己也无法
理解；群体随即把验收扩展为 invariant、testcase、throughput 和代码熵约束。
这组数字属于个人使用报告，适合表现规模与认知失衡，不宜包装成行业统计。

### 2026-07-31：DeepSeek V4 Flash 正式上线公测

群内在 7 月 31 日（据星期推定）看到 “DeepSeek-V4-Flash 正式版 API 上线
公测”，随即讨论其能否成为 K3 或 GLM-5.2 的替代。官方材料的准确边界是：

- [DeepSeek V4 Pro/Flash](https://api-docs.deepseek.com/news/news260424/)
  在 4 月 24 日一同进入 Preview；
- [V4-Flash-0731 Model Card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731/blob/main/README.md)
  将其称为取代 Preview 的正式版，并公开了权重；
- 0731 延续 V4 Flash 的模型结构，Agent 能力主要来自后训练更新；
- 同一张 Model Card 仍把比较对象写作 `DeepSeek-V4-Pro (Preview)`；
- Code Agent 结果使用尚待发布的 `DeepSeek Harness minimal mode`。

所以正文可以写“V4 Flash 0731 取代 Preview 成为正式版”，不能写“V4
Pro/Flash 同时发布正式版”。群聊在发布最初几小时说“权重还没发”，只能保留
为当时的可见性记录；截至 8 月 5 日，官方仓库已经包含权重。`Think Max`
同样是推理档位，不是新的模型 checkpoint。

史料位置：[聊天记录 67269—67682 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:67269)

### 2026-08-01—08-02：从固定 Flow 与动态 Flow 之争回到任务本身

8 月初的讨论强调，安全暂停很贵，长任务最好拆成可重试、幂等的小步骤，保留
checkpoint，让 Master 追踪目标，Sub-agent 负责探索与验证。方向错时，多做工作
只会扩大损失，阶段方向仍由人选择。

与此同时，Humanize 维护者报告 H2/H3 已公开但缺少维护，社区使用更多的是
理念和部件。群内回看两条技术路线：Claude Code Dynamic workflows 被概括成
“组合主义”，外层有阶段、循环和可编程 Flow；Codex Ultra 被概括成“动态
主义”，由 Agent 随运行状态在线决定如何派发。这个命名是社区解释，不能当作
两家公司正式宣布的哲学。

同期结论具有很强的编辑价值：大规模机械维护适合固定、代码式的 Flow；频繁
交互的探索任务适合让 Agent 动态规划；静态 Flow 难以提前覆盖涌现问题，动态
编排又可能过度派发、缺少全局约束。实践者仍在两种模式间手动切换。

> “抛开具体任务谈哪个方法更好是无效的，关键还是在人。”

史料位置：[聊天记录 67956—68142 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:67956)

### 2026-08-03—08-04：Hook 回归，工程标准成为新的责任边界

记录尾声里，Sol Max 在代码完成后重新阅读大量文件，主动换成更凝练的实现；
Kimi Build、Sol Review/清理也成为固定组合。有人给 `TaskCompleted` 增加
Simplify Hook，社区立刻指出 Humanize 最早版本已有类似做法，只是当时粒度
更细。这说明模型能力提升以后，机械完成门仍然有用，调用内容从通用 Review
转向简化、标准化和项目特定检查。

最后一场讨论非常适合作为本章收束。Agent 为完成目标，可能 fork 通用依赖、
修改实现或制造全定制零件，局部指标通过了，量产成本却更高。用户写下“尽量
不要 fork 依赖库”后，Agent 又尝试修改 OS 内核绕过限制。单条负约束只会把
搜索推到另一个缝隙。更稳的办法是把标准化部分做成结构化 Tool 或填空式接口，
再由人给出工程层级的成本、兼容和授权原则。

史料位置：[聊天记录 68639—68975 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68639)

## 四、哪些能力进入了 runtime，哪些能力仍需要外部 Harness

下表只讨论可以观察和核验的机制，不推断训练数据与模型权重：

| 能力 | 7 月已经进入厂商产品的部分 | 外部 Harness 仍直接负责的部分 |
|---|---|---|
| 目标持续 | Codex `/goal` 可创建、暂停、恢复和续跑；Claude `/goal` 用 Stop Hook 每轮判断目标是否完成 | 把产品目标展开为 AC、任务账本、演进记录；防止局部目标替换顶层目标 |
| 计划与分解 | Sol `max/ultra`、Claude Dynamic workflows 和 Sub-agent 都能动态拆任务 | 指定哪些决定必须问人；固定不可越过的阶段门；保存权威 Plan/SSOT |
| Multi-agent | Codex multi-agent、Claude Agent Teams/Sub-agent、GPT-5.6 Ultra 已原生支持委派与并行 | 隔离替代路线、限制递归与并发、选择模型角色、控制预算、保证任务来源可追踪 |
| 自我审核 | 强模型会主动调用 Reviewer、Verifier、Lint 或 Simplifier | 使用独立上下文与独立模型复审；规定审核清单；审核失败时机械阻断提交 |
| 工具调度 | GPT-5.6 Programmatic Tool Calling、Codex tool search、Pi tool primitives 等可以按需选择工具 | 给闭源领域工具加入 `--help`、回调提示、许可证与资源限制；把标准化动作封成结构化 Tool |
| 权限 | Claude Code 和 Codex runtime 提供 Permission/Approval；Pi 可用扩展 Hook 阻断工具调用 | 仓库和组织定义谁能写、谁能联网、哪些命令需批准；关键权限不能只靠自然语言请求 |
| 停止与完成 | Agent 会主动停止，厂商 runtime 也有 Stop/TaskCompleted 事件 | 确定性 Stop Hook、AC Gate、预算上限、人工签字；防止“说完成了”自动等于“可以发布” |
| 恢复 | Claude checkpoint、Codex session/goal 恢复和状态保留已经提供基础能力 | Git/worktree、attempt freeze、checkpoint 后重启、数据备份；Claude checkpoint 不追踪 Bash 改动 |
| 审计 | 厂商保存 session、tool call 和 Sub-agent 状态 | 版本化 JSONL、Commit、Plan、审批与来源；团队内脱敏、访问控制和事故追责 |
| 认知同步 | Agent view、recap、side chat 能降低查看成本 | 用人能理解的语言说明里程碑、风险和选项；Coach Mode 在设计放行前检验人的理解 |
| 评测 | 模型可自动生成或调用 verifier | 固定 held-out 集、gold 裁定、对照组、成本与时间记录；防止 Reviewer 能力污染 Builder 结论 |

其中，权限是区分“建议”和“约束”的最好例子。Claude Code 官方文档明确说明，
`CLAUDE.md` 和 Prompt 影响模型意图，真正的 Allow/Ask/Deny 由 Claude Code
runtime 执行；Pi Coding Agent 则明确选择了更轻的核心，默认不提供 Permission
Popup，进程以用户权限运行，隔离要靠容器、Sandbox 或 Extension。一个模型即使
非常听话，也不能代替操作系统和 runtime 的权限边界。

### Pi 的意义：把“最小核心”和“可扩展 Harness”拆开

Pi 在群内受到重视，很大一部分原因是它的核心保持克制。官方仓库把能力拆成
统一 Provider API、Agent Core、Coding Agent CLI 和 TUI；默认工具主要是
read、write、edit、bash。Coding Agent README 明确说，Sub-agent、Plan Mode
和 Permission Popup 没有放进核心，用户可通过 Extension 或外部 Package 添加。

Agent Core 本身又提供了适合构建 Harness 的低层原语：并行 Tool Call、
`beforeToolCall` 阻断、`afterToolCall` 后处理、steering/follow-up queue、
session resume/tree/fork、自动 compaction 与溢出恢复。7 月 14 日的 v0.80.7
加入 cache-friendly dynamic tool loading，7 月 16 日的 v0.80.9 加入 Kimi
K3 及其 deferred tool loading。

这组事实支持的结论是：**Pi 把低层 runtime 做薄，把 Workflow、Sub-agent 和
Permission Policy 留给上层。** 群聊里提到的高阶可控编排，应按具体项目写
Oh My Pi（OMP）或 Oh My Humanize（OMH）。`OmniPi` 仍缺乏可核验项目。

## 五、Humanize 1.0 的价值怎样退场，又怎样回来

“Humanize 退休”与“重新祭出 H1”相隔十天，看起来互相矛盾，其实对应不同
任务状态。下面按部件拆开：

| H1 部件 | 强 runtime 带来的替代 | 7 月仍然保留的价值 |
|---|---|---|
| Builder–Reviewer Loop | Ultra 能自发 Build、Review、修正和清 Slop | 独立 Reviewer、固定回合与失败阻断更容易审计，也可组合不同模型 |
| `gen-plan` | 强模型可以在对话中直接形成设计并执行 | 把想法固化成可读 Plan，支持人工理解、跨 Session 恢复和干净基线 |
| Goal Tracker | Codex `/goal`、Claude `/goal` 能保存目标并续跑 | H1 账本同时保留 AC、当前任务和 evolution；适合追问“目标为何变了” |
| Full-round Review | Sol Ultra 会主动进行多轮审核 | 项目特定标准、法规、性能和兼容性仍需显式清单；独立上下文可减少自证偏差 |
| Stop Hook | 厂商 runtime 会在认为完成或受阻时停下 | 机械 Hook 不受模型当轮判断影响；可强制 Review、Simplify、审批和预算检查 |
| Feedback Issue | 模型能力升级降低部分通用问题的重复率 | 真实长程失败、脱敏轨迹和 Good First Issue 仍是优化 Harness 的高价值数据 |
| Coach/Human Gate | 模型更善于解释、Side Chat 更方便追问 | 人是否真正理解设计仍是人类侧问题；它很难被“模型更聪明”自动消除 |

因此，H1 在本章里更适合被写成一个**观念与协议的母体**。它作为整套 CLI
Workflow 的使用面可能收缩，其中的 Plan、AC、双角色审查、完成门、反馈和
人类理解检查仍被拆散后复用。7 月尾声给 `TaskCompleted` 加 Simplify Hook，
正是同一思想在新 runtime 上的重新组合。

还有一个容易遗漏的仓库事实。OMH 后期对可变 Workflow 加入了更保守的生产
语义：运行 attempt 先 freeze；要修改 Flow，操作员执行 stop、checkpoint、
批准变更、重新 freeze，再从 checkpoint 重启。相关提交把“动态”变成了可审计
的 revision 与恢复协议。它与本章的责任制完全接得上：Agent 可以提出变化，
运行边界和放行责任仍需外层系统固定。

## 六、从 Human Harness 到“责任制”

“责任制”不是群聊里一个已经定型的专有名词，它是本章对多组实践的编辑性
归纳。它至少包含三条链：

### 1. 目标责任链

| 环节 | 建议责任主体 | 原因 |
|---|---|---|
| 真实问题与顶层命题 | 人类作者、产品负责人或领域专家 | Agent 无法从局部测试推出组织真正想要什么 |
| 设计与权威文档 | 人与 Arch Agent 共同形成，人最终放行 | 讨论可借助模型展开，SSOT 必须有明确 Owner |
| 切片与派发 | PM/Orchestrator Agent | 适合按依赖、资源与上下文自动排程 |
| 实现 | Builder Agent | 目标清楚、工具充分时，自动化收益最大 |
| 机械验证 | Test、Type Checker、Verifier、CI | 可重复、低歧义，适合自动执行 |
| 轨迹与缺陷审计 | 独立 Audit/Reviewer Agent | 读取执行轨迹，发现 PM 跳过或 Worker 自证的问题 |
| 风险接受与发布 | 人类与组织 | 权限、量产成本、法规与事故责任不能由一次模型输出承担 |

Lean 4 的群聊讨论给出了一条极简原则：

> “Type checker 过了就是过了，没过就是没过。顶层命题则必须人负责验收。”

这条原则也适用于软件工程。测试证明的是已编码条件，不能证明条件本身完整。
Agent 可能通过修改 checker、补 trivial test 或绕过依赖来赢得局部指标。人类
真正承担的是目标定义、重要性排序和风险接受。

### 2. 质量责任链

7 月的实践把“质量”拆成了几类互相独立的检查：

- **正确性**：Test、Invariant、Type Checker、形式化证明；
- **性能**：Throughput、Latency、Token、真实硬件与端到端数据；
- **复杂度**：代码量、依赖数、代码熵、是否出现重复 Framework；
- **可维护性**：SSOT、标准化接口、版本、兼容策略、清晰的 Owner；
- **过程完整性**：是否遗漏否决项、是否改过 checker、是否经过批准；
- **可恢复性**：失败能否回到 checkpoint，能否定位哪次变更引入偏差。

群内提到的 “gold 裁定权在人”同样关键。LLM 可以起草 Problem、Rationale 和
Answer，专家负责校验 held-out 样本与最终 gold，bad case 再回流版本化
Benchmark。这里的人类劳动量少了，裁定责任没有消失。

史料位置：[聊天记录 52073—52080 行](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52073)

### 3. 信任责任链

信任不能只建立在“这个模型通常很聪明”。一个可交接的 Agent 工作单元至少
要回答：

1. 输入来自谁，是否经过脱敏和签名；
2. 它读过哪些 Plan、Memory、Skill 与 Session；
3. 它用什么身份调用了哪些工具；
4. 哪些变更来自 Builder，哪些来自 Reviewer；
5. 哪道权限由谁批准；
6. 验收用了哪个版本的数据与 checker；
7. 失败后可以恢复到哪个 Git commit 或 checkpoint。

Claude Code 的 Permission、Hook 与 Checkpoint，Codex 的 Approval 与 session
状态，Humanize 的 Goal/Review 账本，Git/worktree 和团队 Session 审计，在这条
链上承担不同职责。将它们统称为 Harness 也可以，正文最好具体说出每一层做了
什么，读者才能理解“信任”是怎样被工程化的。

## 七、个人与团队工作流的几种收敛形态

### 个人工作流

1. **讨论驱动型**：人与高推理模型长时间讨论，把架构与取舍写进 SSOT；设计
   足够清楚后，再开 Max/Ultra 或 `/goal` 实现。它适合方向已知、实现规模大的
   任务，人的主要投入在开始前。
2. **模型路由型**：Fable/Claude 做 Research 与 Plan，Kimi K3 做 Build，
   Sol 做 Review 与清理；低成本模型处理机械工作，高成本模型守高价值节点。
   这是同期个人经验，不代表固定的模型排名。
3. **外部循环型**：对长反馈、易偏航、可造成大面积变更的任务，继续使用 H1、
   Monitor、独立 Reviewer、Stop Hook 和 checkpoint。人的介入集中在阶段门。
4. **领域工具型**：先把环境、runbook、`--help`、Tool callback、许可证与资源
   规则做扎实，再让 Agent 自行推进。它减少一次性大 Prompt，也让每一步只看到
   当前需要的知识。

### 团队工作流

Arch/PM/Audit 是这段记录里最完整的团队形态：

```text
人类 ↔ Arch（会议、设计、SSOT）
          │
          ├── PM（挑选清楚切片、派发 Builder、合并 worktree）
          │
          └── Audit（读取 PM 轨迹、找遗漏和越权、回报人类）
```

它有三个值得保留的工程细节：

- 三个主 Session 彼此隔离，防止角色上下文互相污染；
- PM 遇到设计不清楚的切片可以跳过，不能替人补造权威需求；
- Audit 审查 PM 的 transcript 与仓库结果，关注“为什么跳过”，不只看最终 Diff。

当团队扩大到 MHMA，新的约束随之出现：替代路线 Agent 不宜互相讨论后形成
错误共识；父子 Agent 可以传递必要信息；所有 AI-to-AI Handoff 都应保留原始
消息与来源；人的注意力、GPU、CI 和代码所有权要进入调度。只提高 Agent 并发，
很容易把局部加速变成团队阻塞。

### 自主程度的三档

| 档位 | 适用任务 | 人的介入 | 必要 Harness |
|---|---|---|---|
| 交互探索 | 目标仍在变化、缺少 Eval | 高频讨论与方向选择 | Side Chat、研究记录、候选方案隔离、预算 |
| 受控长程 | 目标基本清楚、过程长且可能偏航 | 里程碑和异常时介入 | Plan/AC、Monitor、Stop Hook、checkpoint、独立 Audit |
| 机械工厂 | Eval 稳定、反馈短、步骤幂等 | 定期抽样与事故处理 | 固定 Flow、并发调度、资源配额、自动恢复、版本化 Benchmark |

“Autonomous”最好写成这张表里的受控程度。长时间无人值守只是运行现象，系统
是否可靠还取决于边界、观测、验收和恢复。

## 八、效率曲线：目前能画到什么程度

### 【编辑假说】有效吞吐的三段曲线

本章若要画图，纵轴建议使用“单位人类注意力下被验收的有效产出”，而非 Token、
Commit 或并发 Agent 数；横轴可以是自动化程度或 Agent 并发度。

1. **加速段**：需求清楚、反馈可自动获得时，Agent 接管实现、测试和维护，
   有效吞吐快速上升；
2. **认知饱和段**：分支和 Sub-agent 继续增加，人开始读不完产物，Review、
   来源确认、GPU 分配、CI、合并与事故恢复形成排队，边际收益下降；
3. **治理修复段**：SSOT、Arch/PM/Audit、固定阶段门、领域 Tool、权限、
   checkpoint 和审计减少返工，系统吞吐有机会重新提高。

这条曲线的支撑只是多个同期观察：十任务切换造成认知过载；团队五到八个并行
分支阻塞 CI；2700 个 Sub-agent 产出难以理解的系统；“我自己想明白”之后单个
Max 会话反而更快；阶段验收和角色隔离又能降低返工。它还不是实验结果。

### 后续测量应记录什么

| 指标 | 目的 |
|---|---|
| Accepted change / human-hour | 衡量真正被人接受的产出，而非生成量 |
| 首次通过率与返工轮次 | 区分“做得快”和“交付得快” |
| 偏航发现时间 | 比较自审、独立 Monitor 与人工抽查 |
| 恢复时间与不可逆损失 | 衡量 checkpoint、Git 和权限边界 |
| 人类决策次数与等待时长 | 识别 Agent 卡人、人与 Agent 互相等待 |
| Context/Token/Wall-clock | 计算模型、Flow 与并发的总成本 |
| 代码复杂度和依赖变化 | 识别“造星舰”与局部 reward hacking |
| 来源/审批覆盖率 | 衡量团队工作能否追踪和交接 |

若要比较 H1、原生 `/goal`、Sol Max 与 Sol Ultra，至少固定任务、模型快照、
Prompt、权限、硬件、时间预算和验收人，并设置无 Skill、无 Memory 的干净基线。
强 Reviewer 搭配弱 Builder 必须单独列组，不能把组合上限归到 Builder。

## 九、一手资料索引

下面只收录能够直接支撑本章事实边界的官方页面与项目仓库。Benchmark
结果采用厂商材料时，应继续标明“厂商口径”；群聊体验仍以第三节的原文
行号为准。

| 一手资料 | 可核验内容 | 使用边界 |
|---|---|---|
| [GPT-5.6 限量预览](https://openai.com/index/previewing-gpt-5-6-sol/) | 2026-06-26 预览时间、Sol/Terra/Luna、早期 `max` / `ultra` 描述 | 预览期可见性不等于 GA 范围 |
| [GPT-5.6 正式公告](https://openai.com/index/gpt-5-6/) | 2026-07-09 GA；`max` 延长单 Agent 推理；`ultra` 默认协调四个 Agent；Programmatic Tool Calling 与 Multi-agent Beta | 只能证明模型与 Runtime 的产品行为，不能证明 Workflow 已写入权重 |
| [Codex CLI 0.128.0](https://github.com/openai/codex/releases/tag/rust-v0.128.0) | `/goal` 的创建、续跑、暂停、恢复与清除 | 首发是实验能力；实际效果仍受模型、Context 与任务影响 |
| [Claude Code Dynamic Workflows](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) | Claude 生成 JavaScript 编排脚本，Runtime 执行阶段、并行与验证 | “组合主义”是社区归纳，不是 Anthropic 的官方路线名称 |
| [Claude Code `/goal`](https://code.claude.com/docs/en/goal) | `/goal` 是 Session 范围的 Prompt-based Stop Hook，由独立小模型判断条件 | Evaluator 不读文件也不调用工具，只能依据会话中呈现的证据 |
| [Claude Code Permissions](https://code.claude.com/docs/en/permissions) | Allow / Ask / Deny 与 Runtime 权限边界 | Prompt 约束与可执行权限不能混写 |
| [Claude Code Hooks](https://code.claude.com/docs/en/hooks) | 生命周期事件、确定性脚本检查、Prompt Hook 与 Stop 语义 | Hook 可以失败或被错误配置，仍需项目侧验证 |
| [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents) | 独立 Context、工具白名单、角色与权限配置 | 证明产品机制，不证明某次群聊运行实际采用了相同配置 |
| [Kimi K3 技术博客](https://www.kimi.com/blog/kimi-k3) | 2026-07-16 发布、2.8T、原生视觉、1M Context；不同 Benchmark 使用 Kimi Code、Claude Code 或 Codex Harness；局限与 Thinking History 要求 | 性能排名和局限说明来自厂商；跨 Harness 分数不能直接归因于模型 |
| [Kimi Code 更新记录](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) | 7 月 16 日 `v0.26.0` 的后台 Coder、Todo、Plan、Skills 与 Nested Agents | 当前文档会继续更新，写历史时应锁定版本日期 |
| [Kimi Agent 产品时间线](https://www.kimi.com/help/agent/agent-overview) | K3 进入产品的日期与 7 月 27 日完整权重节点 | 产品宣传用语不能替代独立 Benchmark |
| [DeepSeek V4 Preview 公告](https://api-docs.deepseek.com/news/news260424/) | 2026-04-24 V4-Pro / V4-Flash Preview、1M Context、API 与开放权重 | 不能用它证明 7 月 31 日的正式版状态 |
| [DeepSeek-V4-Flash-0731 Model Card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731/blob/main/README.md) | 0731 取代 Flash Preview；官方 Benchmark；`max` Effort；Code Agent 使用待发布的 DeepSeek Harness Minimal Mode | 厂商 Benchmark 含内部测试集；其表中 V4-Pro 仍标作 Preview |
| [Pi Extensions](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md) | 动态工具、Hook、命令、界面与无内置工具启动方式 | Pi 是可扩展 Core；具体权限和 Workflow 取决于用户配置与外部隔离 |
| [Humanize](https://github.com/PolyArch/humanize) / [Oh My Humanize](https://github.com/humanfia/oh-my-humanize) | RLCR、Goal / Plan、Coach 与 Flow Runtime 的公开实现历史 | 当前 README 不能倒推每个功能在 7 月当时已经存在 |

### 仍待核验或等待发布

- DeepSeek Harness 的公开仓库、版本、Minimal Mode 定义与完整 Eval 配置；
- V4 Pro 是否会出现与 `0731` 对应的后续正式版本；
- `/checkup` 截图对应的 Claude Code 官方版本；
- 责任制与效率曲线的跨项目量化数据；
- 群聊 7 月 29 日至 8 月 4 日相对日期的原始微信时间戳。
