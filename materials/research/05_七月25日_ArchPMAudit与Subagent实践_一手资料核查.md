# 7 月 25 日前后：Arch—PM—Audit 与 Subagent 协作实践一手资料核查

> 核查范围：以 2026 年 7 月 25 日前后为中心，向前追溯到 3 月的
> Subagent、Batch、Worktree 和 Monitor 实践。主要证据来自原始群聊 OCR：
> [Humanize 聊天记录](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md)。
> 本文不把用户提供的流程图当作聊天原文；图中没有在 OCR 中出现的文件名和角色名，
> 均标为“图示化标签”或“编辑推断”。
>
> 证据等级：**A** = 原文明确写出角色、动作或数字；**B** = 原文明确写出相邻
> 事实，本文做了有限的结构化归纳；**C** = 只见于用户提供的图或需要进一步取得
> 原始运行记录才能确认。

## 一、先给结论

1. 附图所示的 Arch—PM—Audit 形态，聊天中最早完整出现于 **7 月 18 日
   02:19**，不是 7 月 25 日。当天的原话已经包含三个主 Session、会议记录、
   PM 切片派发、Audit 审查执行轨迹、3—10 个 Subagent，以及 Worktree 隔离。
   这部分是 **A 级证据**。
2. **7 月 25 日是一次角色路由的再确认。** 群里把 GPT 主 Session 限定为设计、
   协调、并发调度、合并和审查，把 Claude、Kimi 和 GLM 放在 Build；随后把这类
   工作称为 `graph engineering`。这与图中 PM、Reviewer、K3 Worker 的分层相符，
   但原文没有再次逐项写出 Arch—PM—Audit 全图，属于 **A 级角色证据 + B 级结构
   对齐**。
3. 图中“开会记录.md”可以追溯到聊天里的“会议记录”和“开会记录”；图中
   “工作审计.md”在 OCR 中没有原词，最接近的是 Audit 生成的“会议缺陷”文件，
   因此不能把“工作审计.md”当成群聊原始文件名。这个差异应在 README 图注或脚注中
   说明。
4. 图中 `PM + /goal`、`PM 的小弟 reviewer`、`K3 打工` 和底部再次出现的
   `PM + /goal` 是一张把多段实践压缩到一张图中的工作流示意。原文能直接支持
   “Sol Ultra /goal、K3 via Kimi Code、独立 Reviewer、Worktree、Audit”，但没有
   直接出现“PM 的小弟 reviewer”这一整句，也没有一条原文同时给出图中的所有箭头。
5. 这套方法并非突然出现。3 月 23—24 日已经形成了“主 Agent 分发、Subagent
   走文件、互不直接沟通、Worktree 隔离、主 Agent 汇总”的基本原则；7 月 15 日
   又加入 Manager—Worker—Reviewer 和定时监视；7 月 18 日才演变成 Arch—PM—Audit
   的组织化分工；7 月 25 日则进一步变成模型路由和图式工程。

## 二、附图与聊天证据的逐项对应

| 图中元素 | 聊天中可以直接核对的内容 | 证据 | 需要保留的边界 |
| --- | --- | --- | --- |
| `Arch`（`gpt-5.6-sol max`） | Arch 只负责和人开会、Brainstorming、写开会记录；人绝大多数时间和 Arch 对话 | [L58924-L58929](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58924)、[L58945-L58960](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58945) | “Arch 使用 Sol Max”没有在同一段原文逐字写出；7 月 18 日主 Session 写的是 Sol Ultra，图中档位属于 **C/B 级图示信息** |
| `开会记录.md` | Arch 把设计讨论沉淀成“会议记录”；稍后又说专门用一个文件当“开会记录”，用来解耦设计和干活 | [L58270-L58272](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58270)、[L58893-L58895](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58893) | 扩展名 `.md` 是合理的文件形式，但 OCR 只给出文件名，不给出完整路径 |
| `PM + /goal`（`gpt-5.6-sol ultra`） | PM 只看会议记录、挑选清楚切片、派发 Subagent、合并 Worktree；7 月 18 日又说实际任务可由 Sol Ultra 派给 K3 via Kimi Code，并把这套工作放在 5.6 Goal 里 | [L58924-L58929](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58924)、[L58791-L58804](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58791) | “PM + /goal”是把两段文字合成一个图标节点；原文没有逐字出现这一节点名称 |
| `Audit`（`gpt-5.6-sol max`） | Audit 读取 PM 的 Session JSONL / Transcript，寻找 PM 跳过或误判的部分，对代码库进行审查，并生成“会议缺陷”；再把问题带回人和 Arch | [L58273-L58275](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58273)、[L58912-L58914](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58912) | Audit 的模型档位在图中给出，聊天段落只明确写“每个主 Session 都是 Sol Ultra”；档位应标注为图示配置 |
| `工作审计.md` | 没有检出这个确切文件名；原文中的对应物是 Audit 形成的“会议缺陷”文件，以及“审查 PM 的执行轨迹” | [L58273-L58275](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58273) | 建议图注写“工作审计（群聊原词：会议缺陷）”，不要声称文件原名就是 `工作审计.md` |
| `Contractor` | 7 月 18 日工作流描述中明确说“偶尔起一个 contractor 干一点急活” | [L58791-L58799](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58791) | 这是单点补位角色，原文没有给出它的固定模型、审批权或与 PM 的稳定上下游关系；图中箭头属于 **B/C 级结构化推断** |
| `PM 的小弟 reviewer` | 7 月 18 日写明每个 Arch/PM/Audit 主 Session 各带 3—10 个 Subagent；7 月 15 日也出现 Manager、Worker 与 Reviewer 的三层组合 | [L58269-L58277](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58269)、[L56289-L56297](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56289) | “PM 的小弟”是图示化称呼；不能据此断言所有 PM Subagent 都专职 Reviewer |
| `K3 打工` | Sol Ultra 被要求把实际任务派给 K3 via Kimi Code；同日另有“Codex Review + K3 Build”的直接体验 | [L58791-L58804](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58791)、[L58670-L58680](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58670) | 这是个人工作流经验，不代表 K3 在所有任务上都适合 Build |
| 底部再次出现 `PM + /goal` | 文字记录支持“PM 负责派发、合并；人回看 Audit，再回到 Arch 继续设计”，形成设计—执行—审计—再设计的闭环 | [L58912-L58929](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58912) | 原文没有画出底部节点；它是把反馈回流压缩成图的编辑表达 |

## 三、向前追溯：这条机制从哪里来

### 2026-03-23：先有“Subagent 不互聊，结果走文件”

3 月 23 日的讨论已经把今天图里的几个基本约束说得很清楚：有人主张
`agent-teams` 没有必要，Subagent 应由 Leader 统一调度；Subagent 必须走文件输出，
主 Agent 负责综合；真实并行最好控制在五个左右，并通过 Worktree 隔离修改。
同一段记录还写到一次性启动 22 个 Subagent，并明确担心 Leader 的 Context 和 I/O
被打爆，以及探索型任务不适合这种严格分工。

史料位置：[L950-L1003](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:950)、
[L1006-L1043](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1006)。

同日下午又把它压缩成“`harness {/batch {build-review}}`”：主 Agent 与 Builder
分离，批量任务走 Worktree，Subagent 不直接互相沟通，主 Agent 只负责合并和关键
提问。一次实践中，1 个 Master Plan 拆成 21 个小 Plan，每个约负责 1,000—3,000
行增量；启动后约 3.5 小时完成 4.7 万行代码。这里的数字是成员个人报告，不能
当作稳定吞吐率。

史料位置：[L1130-L1165](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1130)。

### 2026-03-24：把“批量子任务”写成可复用编排

3 月 24 日，有成员总结出一套可稳定复现的流程：一次启动 10 个以上 Agent，
每小时稳定输出约 1 万行可用代码，核心是 predefined harnessed orchestration
flow with batched Subagents that cannot talk；随后又报告写了近 6 万行代码，期间
没有发生上下文压缩。紧接着的复盘明确区分安全 Subagent 模式与不可见的 Agent-to-
Agent 直连：前者各自完成任务后向 Manager 汇报，后者应避免；隔离应通过工具权限
和 Worktree 实施，而非只靠 Prompt。

史料位置：[L1249-L1275](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1249)、
[L1276-L1292](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1276)。

这段历史说明：7 月的 Arch—PM—Audit 不是从零发明的模式，它把 3 月已经出现的
“主控—批量执行—汇总—隔离—复核”原则，换成了更接近真实项目管理的岗位名称。

### 2026-07-04：`gen-plan + /goal` 先验证了长程执行

7 月 4 日，群里记录了一次持续 32 天的 Goal：起点是 Humanize `gen-plan` 生成的
计划，执行交给 Codex `/goal`，Claude 只在早期监督约一周；前两周大部分实现完成，
后两周主要做性能调优。报告者强调，任务最后能够停机，说明“持续很久”和“最终
能够完成”可以同时成立；但他同时说尚未评价工作是否真的有效，也没有给出可复现的
Token 总量。

史料位置：[L50334-L50360](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50334)、
[L50371-L50427](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50371)。

同一夜还出现一个被遗忘、运行了 12 天的 Goal，以及一个运行 20 天、抓取多国历史
教材并建立数据库的任务。它们只能说明当时社区已经在尝试超长程任务，不能证明执行
质量或成本。

史料位置：[L50428-L50460](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50428)。

### 2026-07-15：加入定时 Reviewer、Monitor 和 DAG Worktree

7 月 15 日，一种三层工作流被直接写出：Manager、Worker、Reviewer；Reviewer
使用 Codex，通常通过 Loop 定时检测 Manager。它是 7 月 18 日 Audit 角色的前置
版本：先有一个外部角色观察执行者，后来才把观察对象扩大为 PM 的完整 Transcript
和 Worktree 结果。

史料位置：[L56282-L56301](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56282)。

同日另一位成员让 Sol 分析依赖图、并行走 Worktree 并负责合并；实践中一个小报告
跑了约 1.5 小时，模型曾展开 4—5 层 Subagent，反复验证、修复和循环，迟迟不能
收敛。随后有人把任务拆成约 500 行工作量建立 DAG，并在 DAG 上增加检查点。

史料位置：[L56461-L56501](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56461)。

这段记录同时暴露了机制的限制：并发不等于吞吐，模型可能用更多层级重复验证；
Reviewer 也可能变成新的上下文和延迟瓶颈。

### 2026-07-18：Arch—PM—Audit 作为组织化方法出现

7 月 18 日 02:19 的记录是本次附图最重要的一手来源。它明确给出：

- 启动三个主 Session：Arch、PM、Audit，每个主 Session 使用 Sol Ultra；
- 人与 Arch 讨论和问答，形成“会议记录”；
- PM 只挑选会议记录中设计完善、合理的切片进行实现，不合理时可以跳过；
- Audit 审查 PM 的 Session JSONL，找出 PM 认为不合理或跳过的部分，形成“会议缺陷”；
- 人每天回看 Audit 的缺陷，再回到 Arch 继续讨论；
- 每个主 Session 带 3—10 个 Subagent，设计、实现和审查通过 Worktree 并行。

史料位置：[L58269-L58289](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58269)。

当天 12:06 的补充把模型路由和职责写得更具体：Sol Ultra 负责持续与 Arch 开会，
实际任务通过 Kimi Code 派给 K3；必要时另外启动 Contractor 处理急活；体验上
“Codex Review + K3 Build”很顺手。这里的“会议—派发—Build—Review”已经接近
附图的上下游箭头。

史料位置：[L58791-L58816](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58791)。

12:47—13:06 的后续讨论进一步规定了岗位边界：PM 只做 Delegation，派发到
Worktree 并合并；PM 判断不了的点由 Audit 从 Transcript 中找出，再回到人和 Arch；
三栏 tmux 分别放 Audit、Arch、PM，人约 95% 的时间与 Arch 对话。这个“角色隔离”
比“让一个 Agent 从头包办”更接近真实项目管理，但它仍是个人工作流，不是 Humanize
仓库的正式功能。

史料位置：[L58901-L58966](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58901)。

## 四、2026-07-25：从角色分工走向模型路由与 Graph Engineering

### 1. GPT 负责设计、协调、审查；Claude/Kimi/GLM 负责 Build

7 月 25 日 07:57 的消息把前几天的经验压缩成一句可执行规则：GPT 只做设计、
协调和审查，Claude 与 Kimi 做 Build，GLM 也可以承担高效的 Build。随后又补充，
主 Session 使用 Codex + GPT，只做交互式设计、并发调度、合并和审查，**不做
Build**；原生 Harness 优先，缺少原生入口时才走 Claude Code。

史料位置：[L62901-L62915](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62901)、
[L62973-L62989](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62973)。

这正是附图里“主控/审计模型”和“K3 打工/Builder”分开的现实依据。需要注意，
这是个人对模型性格和成本的经验判断，不是模型能力的独立 Benchmark。

### 2. `graph engineering` 与最简 H2 抽象层

7 月 25 日 08:20—08:21，群里分享了 [humanfia/flowjanus](https://github.com/humanfia/flowjanus)：
作者称其炼化 Oh My Humanize 的核心，做成一个 H2 最简实现，当前只是 Agent 抽象层，
后续准备加入 Flow Call Flow。几小时后，原作者把这类工作称为 `graph engineering`，
并继续说明 K3 打工并不只使用 K3，而是按可用量在 Kimi、Claude、GLM 之间路由。

史料位置：[L62916-L62922](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62916)、
[L62995-L63007](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62995)。

同一早晨还分享了 [SihaoLiu/skills/ask](https://github.com/SihaoLiu/skills/tree/main/ask)，
包含 `ask-{claude,codex,kimi,glm}` 入口。它可以被理解为“没有原生 Harness 时，
让主控统一调用不同模型”的轻量路由层，但仓库和运行示例仍需独立确认，正文不宜
把这段聊天直接写成稳定产品能力。

### 3. 路由的依据：审查质量、Build 质量和成本分开看

7 月 25 日 02:38 的个人总结是：GPT 仍是 Reviewer 和 Gatekeeper；Claude 只比
Kimi 略好；Kimi 更省成本；GLM 可用但不如 Kimi K3。此前的 API Cost 截图和文字
又给出一个个人几日快照：Claude 占 16% Token、20% 费用；Kimi 占 8% Token、4%
费用。这个快照由群友自写的 `ai-usage` 工具统计，不能外推到其他账户或模型版本。

史料位置：[L62823-L62860](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62823)、
[L62861-L62866](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62861)。

### 4. 为什么要把图画成“多层回路”

把上述记录放在一起，图中的回路可以用下面这条**编辑模型**解释：

```text
人类 ↔ Arch：把模糊意图讨论成可执行的会议记录 / SSOT
         ↓
PM + /goal：读取记录，选择清楚切片，派发到隔离 Worktree
         ↓
Subagent / K3 Worker：实现局部任务，结果回到 Worktree 或文件
         ↓
PM：合并、整理、提交阶段结果
         ↓
Audit：读取 PM Transcript、JSONL 和仓库变化，记录被跳过的风险
         ↓
人类 ↔ Arch：处理缺陷、改写设计，再生成下一批切片
```

这条图式把 3 月的 Batch/Subagent 原则、7 月 15 日的 Monitor/Reviewer 和
7 月 18—25 日的角色路由放在一个连续框架里。它是用于读图的编辑性抽象，不能
反过来当作一个已经发布的统一工具协议。

## 五、可作为册后参考的数据点

下表专门区分“原文数字”和“编辑计算”。所有数字均来自个人实践或群聊快照，
没有同任务、同模型、同预算的对照实验。

### 5.1 Token 与费用：能计算的只有相对指标

用户提供的流程图没有 Token、费用、调用次数或运行时长字段，无法从图里的
Arch、PM、Audit、Contractor、Reviewer 和 K3 Worker 节点推导逐角色消耗。
能计算的部分来自群聊中的个人统计：7 月 25 日，一张 `ai-usage` 面板显示
Claude 占 16% Token、20% 费用，Kimi 占 8% Token、4% 费用；GPT 40% 和
其余各家各 20% 是当时对个人未来分布的预估。[L62823-L62866](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62823)

将这张面板的总 Token 和总费用各自归一为 100，得到 Claude 的相对成本密度
`20 / 16 = 1.25`，Kimi 为 `4 / 8 = 0.50`。在同一个人的任务组合和价格
口径下，Kimi 的相对成本密度约为 Claude 的 40%。这可以解释“GPT 做
Reviewer/Gatekeeper、Kimi 做 Build”的个人路由，但不能替代官方价格，也不
能外推到其他账户、模型版本或任务类型。

在更早的记录里，一位成员留下过 `codex:omh:claude = 71:16:13`，并预估
之后会变成 `omh:codex:claude = 80:10:10`。[L45435-L45450](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45435)
这说明 Token 分布会随 Harness 入口和任务角色变化，单看模型名很难解释账单。

几条套餐口述进一步给出了“消耗速度”的量级：7 月 17—18 日有人报告
`¥699` 套餐一天消耗 25% 周额度、5% 月额度，也有人说 K3 Swarm 一天用完
`¥199`，一个 36 分钟的 `/goal` 用掉 3% 周额度；7 月 19 日一次错误的 Sol
任务在三个小时内消耗 30% Codex 周额度和 20% Kimi 周额度；7 月 21—24 日
又出现高强度 K3 用掉 `$100 + $200`、每周约 `1.5 × $200`、一小时用掉
10% Codex 额度等记录。[L58095-L58124](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58095)、
[L59329-L59330](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:59329)、
[L60061-L60408](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:60061)、
[L60807-L60828](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:60807)、
[L62242-L62264](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62242)。这些样本的套餐、地区、模型、统计周期都不同，不能相加，适合用来观察预算压力和错误路径的代价。

后续若要把“大家各自烧了多少”做成真正可比的附表，至少需要统一记录：统计
窗口、模型、角色（设计/Build/Review）、输入/输出/缓存 Token、费用、任务是否
通过验收、返工轮次和人类介入时间。这样才能比较“可接受产出 / 成本”和
“可接受产出 / 人类时间”，避免把高产出高消耗与低产出空转混在一起。

| 数据点 | 原始记录 | 证据等级与用法 |
| --- | --- | --- |
| 32 天 Goal；前两周完成大部分实现，后两周性能调优 | [L50334-L50381](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50334) | **A**：可写“单次个人长程实践”；没有 Token、质量和硬件数据，不能写成 Benchmark |
| Claude 监督约一周；报告者尚不能判断 32 天产物是否有效 | [L50402-L50427](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50402) | **A**：说明监督强度和结论都有限；不要把“成功停机”写成“成功交付” |
| 另一个 Goal 被遗忘运行 12 天；历史数据库任务运行 20 天、完成七个国家 | [L50428-L50460](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50428) | **A**：仅能作为运行时长样本；质量和成本未知 |
| 1 个 Master Plan、21 个小 Plan；约 3.5 小时写入 4.7 万行 | [L1130-L1165](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1130) | **A**：3 月个人 Batch 记录；适合说明并行规模，不适合外推每小时产能 |
| 10+ Agent、约 1 万行/小时；随后近 6 万行且未发生 Context 压缩 | [L1249-L1270](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1249) | **A**：3 月个人报告；“可用代码”是作者自评，需注明口径 |
| Arch、PM、Audit 各带 3—10 个 Subagent | [L58269-L58277](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58269) | **A**：原文直接数字；三主 Session 合计 9—30 是简单乘法推导，属于 **B**，且不代表同时活跃数 |
| Manager—Worker—Reviewer 小报告运行约 1.5 小时；Subagent 展开 4—5 层 | [L56461-L56482](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56461) | **A**：个人体验；可用于说明并发和递归会增加延迟与不收敛风险 |
| K3 + Kimi Code “一个回车跑 12 小时” | [L58670-L58680](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58670) | **A**：个人能力感受；没有交付质量和总 Token，不宜写成稳定保证 |
| Claude 占 16% Token / 20% 费用；Kimi 占 8% Token / 4% 费用 | [L62823-L62830](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62823) | **A**：个人 `ai-usage` 快照；统计窗口、任务集合和价格口径不完整，不能外推 |
| 非 GPT 模型日均“1B 多一点 / 不到 2B” | [L62930-L62940](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62930) | **B**：OCR 中提问、回答和时间标签粘连，具体对应谁的账户需回原截图确认 |
| “95% 时间和 Arch 对话” | [L58942-L58966](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58942) | **A**：个人时间分配感受；不是系统级人类介入比例 |

### 建议的引用写法

正文或附录可以写成：

> 群里有人曾把一个由 Humanize `gen-plan` 启动、交给 Codex `/goal` 执行的任务
> 跑了 32 天；前两周完成主体实现，后两周主要做性能调优。这个记录证明的是
> 长程运行曾经发生过，不证明产出已经达到预设目标。几周后，另一套角色化实践
> 把设计、派发、执行和审计拆到 Arch、PM、Audit 三个主 Session，每个主 Session
> 再带 3—10 个 Subagent，并用 Worktree 隔离。到 7 月 25 日，实践者进一步把
> GPT 放在设计、协调、审查位置，把 Claude、Kimi 和 GLM 放到 Build，形成了按
> 角色而不是按单一模型排名选择工具的工作流。

这段写法保留了日期、数字和证据边界，也避免把截图中的“工作审计.md”或
“PM 小弟 reviewer”误当成群聊逐字记录。

## 六、仍待补证的项目

- 用户提供的图片没有随 OCR 一起出现，无法从聊天文本确认它的生成时间、制图者、
  原始 Prompt 或实际运行配置。当前只能以 7 月 18 日文字和 7 月 25 日路由实践
  作为“图示所依据的聊天材料”。
- `工作审计.md`、`PM 的小弟 reviewer`、图中每个模型档位以及底部回流箭头都应
  标注为图示化表达；如果能拿到制图当天的原始消息或项目文件，再升级证据等级。
- 7 月 25 日 `ai-usage` 的 API Cost 截图只在 OCR 中留下表头和两个百分比，缺少
  统计起止时间、总 Token、价格、任务构成和模型路由规则。它适合放在“个人观测
  数据”附录，不适合做跨模型结论。
- 3 月的行号来自高召回 OCR，包含重复消息和 OCR 粘连；所有数字引用写入正文前，
  最好回看原始截图或导出，特别是“4.7 万行”“6 万行”和“1 万行/小时”。
- `flowjanus`、`SihaoLiu/skills/ask` 和个人 `ai-usage` 属于社区或个人项目，
  应与 Humanize 官方仓库分开列为参考资料；它们说明实践扩散，不证明已进入
  Humanize 主线。
