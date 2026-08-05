# Humanize Book「Agent 篇」素材索引

这份文件用于核对《当 Agent 开始组成团队》的事实边界、时间顺序和原始上下文，不建议原样放入公开版小册子。

## 一、原始材料与整理边界

- 原始记录：`/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md`

- 文件规模：68,975 行，约 2.75 MB；正文头部说明其由 7,481 张截图 OCR、像素去重、文本片段去重后按时间合并。

- SHA-256：`349efc7f1c242078b6b6323b321e9a4c8b1711479fa05629fb2eff7aeaefd429`

- 时间范围：记录从 3 月中旬延伸到 7 月 28 日之后。后段日期标记由“7 月 28 日”切换为“星期三”“昨天”等相对时间，因此正文只写“记录后段”，不擅自换算成确定日期。

- 选材范围：保留与 Agent 架构、并行、委派、Review、Harness、Flow、Memory、评估、人类在环、可观测性、权限和多人协作直接相关的内容。纯模型品鉴、价格与额度、水群、招聘和与方法论无关的产品新闻没有进入正文。

- 署名策略：OCR 会把引用者、被引用者和截图文字粘连。正文默认匿名转述；如公开署名，必须回到对应截图核对，并征得社区成员同意。

## 二、证据标签

素材可按四类阅读：

- **原话/定义**：记录中明确提出的公式、术语或原则。

- **个人案例**：参与者报告自己项目中的结果，只能证明该案例发生过，不能当普遍 Benchmark。

- **提案**：尚未充分验证的架构设想、产品设计或研究方向。

- **反例/保留意见**：用于阻止正文把争论写成共识。

## 三、主题索引

条目按主题组织，日期按原记录标注；主题内部不严格按时间排序。正文末尾另附有时间线。

### A. Harness、计划与独立审查

**A01｜3 月 20 日：Harness 是控制系统**  
[L656–687：观测、验证、每次编辑后拉起另一个 Agent 审查；“Harness 工程就是控制论”](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:656)

- 原话/定义：人维护接口和评价机制，Agent 负责实现；重点从手改代码转向观测与验证。

- 保留意见：群友也指出再好的控制都可能有漏洞，不能把“控制论”写成形式保证。

**A02｜3 月 21 日：把原则编码成机械规则**  
[L789–813：群内转发的 Harness Engineering 片段，涉及代码漂移、清理 AI Slop、黄金原则和后台扫描](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:789)

- 这是聊天记录中转引的外部材料，正文只吸收了“机械规则比反复提醒稳定”的思想，没有把其中数字当作本文独立验证的事实。

**A03｜3 月 21 日：两个 Agent 独立出计划，再合并**  
[L821–842：并行独立规划用于缓解初始 Plan 的路径偏置](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:821)

**A04｜4 月 2 日：PDBR**  
[L5700–5799：P、D、B、R 的含义，以及 `P-/loop{D-/batch{B-R}}`](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5700)

- P 承载人的意志与目的；D 影响一次能完成的任务大小；B 影响收敛速度；R 影响收敛质量。

- 原始表达中的公式没有空格，正文为可读性加入了空格。

**A05｜4 月 3 日：Humanize 从复杂系统做减法**  
[L5855–5964：超过 60 个 Agent 的复杂系统失败后，只保留 Ralph Loop 与 Codex Review；独立 Context 与 Less is more](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5855)

- 个人回顾，不是对所有复杂系统的否定。

- 同段给出四点解释：多步优于一次、构建与审查分离、迭代与并行、以终为始。

**A06｜4 月 3 日：Plan 在执行期间是否可修改**  
[L6022–6030：重新规划可以发生，但 `plan.md` 不应在任务执行中被随意修改](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:6022)

- 后续动态 Flow 对这一原则提出修正，因此正文把它写成历史阶段中的选择，而不是永久规则。

### B. Agent Teams、Sub-agent 与通信拓扑

**B01｜3 月 23 日：76% 的 Agent Teams 质疑**  
[L950–1004：Teams 与 Sub-agent 争论，Leader Context/I/O 瓶颈，构建与探索的差别](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:950)

- 原话：“干活的小兵并不需要沟通。”

- 保留意见：探索型任务可能不适合只做封闭 Sub-agent；也有人提出 Teams 与 Sub-agent 都未必是最终答案。

**B02｜3 月 23 日：22 个 Agent 的个人案例**  
[L1029–1119：22 个 Agent、3 小时、约 4.7 万行增量；Teams 反例与 Batch 对比](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1029)

- 个人案例：第一次编译通过、关键点检查正确等为发言者报告，没有统一复现。

- 反例：同一参与者的 gem5 CMake/Bazel 工作曾使用 Humanize + Agent Teams 完成。

**B03｜3 月 23 日：Batch、Worktree 与集中汇总**  
[L1153–1180：`harness {/batch {build-review}}`；MVP 后从 1 到 100 的扩展实践](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1153)

- 关键前提：先交互式完成 MVP；21 个小 Plan 经人阅读；Master Plan 只描述并行度与依赖。

**B04｜3 月 23 日：难的是禁止沟通**  
[L1171–1232：禁止沟通、Plan 禁止写 Code、通过剥夺工具实施权限边界](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1171)

- 原话：“这个不应该靠 Prompt，而应该直接剥夺 Agent 的 Tool。”

**B05｜3 月 24 日：安全拓扑与动态 Review 粒度**  
[L1250–1293：十个以上 Agent、文件/Manager 中转、Worktree 隔离、Review 放置位置](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1250)

- 安全模式：独立 Expert → Manager → 综合。

- Review 太细会过早打磨；太粗会因规模过大而漏检。

**B06｜4 月 3 日：Zero Shared Session History**  
[L5983–5994：Sub-agent 不共享完整 Session History，但可共享 Curated Knowledge](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5983)

**B07｜4 月中旬：构建与探索对通信的不同需求**  
[L9770–9855：Teammate 禁止沟通的反直觉经验，以及“构建型/探索型 Humanize”](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9770)

**B08｜5 月下旬：从对话中心转为产物中心**  
[L23353–23375：会话、资源权限与“以产物为中心”的提出](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:23353)  
[L25994–26012：h2 以对话为中心被认为是问题；对话带宽低，多人介入](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25994)

**B09｜5 月 29 日：Agent 只对产物做变换**  
[L29630–29654：Agent 之间不沟通，围绕产物做变换；Harness 是否会在数月内被官方内化](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29630)

**B10｜5 月 6 日：Worktree 不等于完整隔离**  
[L17742–17797：长 Session 走入其他 Worktree、合并冲突、独立 Session 与人工维护](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17742)

### C. Flow 作为程序、语言与运行时

**C01｜4 月 22 日：`humz / hcc / hvm` 三层**  
[L13255–13307：Flow 语言、编译成脚本的 hcc、执行环境 hvm；工作流与基础设施分离](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13255)

- 原话：“机械化的 Harness 不应该交给 Agent 做——浪费 Token，而且还容易漂移。”

**C02｜4 月 23 日：Development Flow Graph 与类型系统**  
[L13960–14020：Codebase、Context、Prompt、State 四类输入输出；Agent 节点与 DFG](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13960)

**C03｜4 月 23 日：Agent 公式与新处理器类比**  
[L14145–14315：`Agent = Model × Tool × Action × Permission`、Token 功耗类比、Flow as Code、结果稳定性](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14145)

- 保留意见：讨论明确说 Workflow as PL 可以只是思维模型，实际实现不必复用 MLIR/LLVM 或专用 DSL。

**C04｜4 月 24 日：静态检查**  
[L14575–14595：组合逻辑回环对应 Goal Drift；死代码对应永远不会触发的 Agent](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14575)

**C05｜4 月 27 日：h2 能做什么、不能做什么**  
[L15605–15655：构建 Flow、换模型、静态检查；h2 不能自动配置最优 Flow](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:15605)

**C06｜4 月 30 日：AgentVM + Flow 编程语言**  
[L16813–16830：MVP 尚不稳定；AgentVM、后端适配、编译警告](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16813)

**C07｜5 月 5 日：Agent 作为约束求解器**  
[L17524–17570：Constraint、Optimization Target、Heuristics；构建、维护与探索任务](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17524)

- 反例/保留：Constraint Solver 只覆盖 Build；开放目标仍需探索。

**C08｜5 月 16 日：h1、h2、h3**  
[L21910–21930：h1 是能工作的 Flow；h2 是人构建/测试 Flow 的平台或语言；h3 是 Agent 构建 Flow 的自动化系统](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21910)

**C09｜6 月初：运行中修改 Flow**  
[L32255–32345：h3 允许 Agent/人按阶段动态调整 Flow，Agent 改 Flow 需要人类审批](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32255)

**C10｜6 月 9 日：动态主义与组合主义**  
[L36555–36587：无限 Flow 空间中的动态调整，或少量有效 Flow 的重复组合；个人判断 45/55](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36555)

- 个人概率只是当时判断，不应写成投票结果。

**C11｜6 月 15–17 日：处在 Flow 内部的 Agent 难以意识到要改 Flow**  
[L42496–42512：Progressive Flow 接口存在但不易触发](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42496)  
[L44115–44148：改 Flow 的审核门控、接口尚不稳定、FlowBench 设想](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44115)

**C12｜6 月 19 日：Flow 光谱与软硬分工**  
[L46155–46189：从自由 Skill 到机械 Hook；确定性规则交给程序，不确定判断交给 Agent](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46155)

**C13｜5 月 24 日：把 Flow 优化者与任务执行者分开**  
[L25674–25718：AI1 只改 Workflow、跑实验和记日志；AI2 严格执行；脚本化约束与自然语言服从问题](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25674)

**C14｜6 月中旬：Flow-aware Inference**  
[L44147–44236：Loop 结构映射到 Serving 优化、长程 Flow 与推理框架连调](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44147)  
[L45028–45048：并发结构作为预加载和调度信号](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45028)

- 主要是研究设想，正文没有把它写成已验证收益。

**C15｜记录末段：Agent-Flow-Language**  
[L68499–68535：Pi Agent、Agent Flow Language IR、Python 作为前端/Generator](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68499)  
[L68605–68615：发布早期仓库，说明 Skill、MCP、安全、RAG 支持仍有限](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68605)

### D. 构建、探索与评估

**D01｜3 月 23 日：先构建探索工具**  
[L991–1004：Sub-agent 擅长明确任务；探索工作应先构建探索工具，而非边探索边建系统](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:991)

**D02｜5 月下旬：Build Flow 与 Exploration Flow**  
[L27995–28050：强 Review/强约束与强发散的区分；`build an exploration tool, not build tool while exploring`](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27995)

**D03｜5 月 31 日：没有例证的 Flow 站不住脚**  
[L31195–31235：真实第三方项目、实际效果与例证标准](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:31195)

**D04｜4 月 23 日起：Flow Benchmark 与 Micro-benchmark**  
[L14198–14240：Agentic Workflow Benchmark 困难；从原语与 ISA 构建 Micro-benchmark](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14198)

**D05｜6 月 14 日：同任务同模型，换 Harness，轨迹改变**  
[L42410–42449：Trace、Eval、样本成本与随机波动争论](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42410)

**D06｜6 月 25 日：Monitor 的适用范围**  
[L48765–48814：多 Flow/长任务时 Monitor 更有价值；短任务不一定需要；主动与被动监控](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48765)

**D07｜6 月 7 日：第三方 Monitor 的个人实践**  
[L35444–35508：每小时扫 Transcript；发言者报告约每 10–12 小时一次偏离，等待三轮后介入；从三条任务扩到十个 Loop](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35444)

- 个人工作流中的经验，不代表通用偏离概率。

**D08｜记录末段：组合主义与动态主义按任务分流**  
[L68085–68142：机械维护任务用代码化 Flow，交互探索用动态管理；两者缺点与未决平衡](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68085)

### E. Memory、Skill 与路径依赖

**E01｜5 月 8 日：自动 Memory、GraphRAG 与文件检索**  
[L18295–18410：Auto-memory 膨胀、高优先级规则投毒、GraphRAG/ClaudeMem 个人体验、长短时记忆](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18295)

- 个人案例：“最后发现不如 planning-with-files”“最后都是瞬时 grep/rg”。不能外推为对所有图检索方案的否定。

**E02｜5 月 17 日：好的记忆也会有毒**  
[L22423–22436：Coding Memory 被认为常是负收益；低频触发；只保留特别坏的记忆；成功路径抑制探索](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22423)

**E03｜5 月下旬：Memory 是共享事实还是污染源**  
[L26875–27015：对话/产物/Flow 三种中心，错误经验在多 Agent 间传播，环境事实与共享 Artifact](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:26875)

**E04｜6 月 10 日：错题本失败**  
[L37904–38108：失败路径记录造成剪枝；Evidence Score、Decay Rate、Leaky Integrator；最终删除错题本](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:37904)

- 原话：“巨量的性能提升，往往就在错误尝试旁边。”

**E05｜7 月 10 日：Auto-subagent 被视为 Memory 的前提**  
[L52530–52560：多个 Explorer 对比后才知道什么重要；Transcript、Spec、文件 Checkpoint 的信息损失争论](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52530)

**E06｜7 月 20 日：Skill Dropout**  
[L59908–59940：领域 Skill 太多会造成路径依赖；随机禁用或渐进加载](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:59908)

**E07｜7 月 28 日：不使用长期 Memory，重读项目 Spec**  
[L64665–64672：约五万 Token 的固定开销换取简单；单人可行，多人协作存在问题](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:64665)

### F. 人类掌控、认知债与 Human Harness

**F01｜5 月 12 日：生产力增长与掌控度不匹配**  
[L19472–19554：h2 的障碍是人类掌控；人脑固定；抽样考试；未被理解的代码类比未测试代码](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19472)

**F02｜5 月 12–13 日：Quiz 与 Human Harness**  
[L19880–19981：抽样考试、Plan-time Human Verification、“Human Harness 让人类更负责”、记忆/自检/教育](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19880)

**F03｜5 月 13 日：HAD**  
[L20651–20695：让 Agent 带着人往前跑；把人的带宽放到确认点；Human Aided Design](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20651)

**F04｜6 月 24 日：人的注意力上限**  
[L48276–48294：最多监控约十个 Loop 的个人实践；每天少于一次观察被认为难以负责](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48276)

**F05｜7 月 18 日：Arch / PM / Audit**  
[L58269–58305：三个主 Session、每个三到十个子 Agent、会议记录与会议缺陷、Worktree 隔离](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58269)  
[L58894–58966：角色的窄职责、设计与执行解耦、Audit 阅读 PM 轨迹](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58894)

**F06｜7 月 28 日后：长程 Agent 主动考试人与认知债**  
[L66085–66187：反向 BTW Quiz、层级抽样测试、安慰剂批评、可读文档、按 Profit/Loss 决定理解深度](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:66085)

**F07｜7 月 28 日：MHMA**  
[L64926–65024：单人/多人、单 Agent/多 Agent 分类；一键脚本交接；多人硬件开发的价值与认知成本](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:64926)

### G. 模型内化 Harness、自动子 Agent 与可观测性

**G01｜5 月 29 日：官方内化作为 Harness 的实践检验**  
[L29640–29654：两三个月内是否被官方功能覆盖的个人判断](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29640)

- 这是强烈的个人评价标准，不是可证定律。正文只保留“模型与产品会吸收有效结构”的讨论方向。

**G02｜6 月 15 日：有用的机械结构应进入模型**  
[L42618–42642：Harness/Flow 吸收论；`/goal` 的 Progressive Planning 与 Reviewer Loop](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42618)

**G03｜7 月 9 日：第三方 Harness 与内置功能**  
[L51943–51975：产品内置清理、去重、自动模式；“第三方 Harness 被官方蒸馏”](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:51943)

**G04｜7 月 10 日：自动 Sub-agent 改变外部 Harness 的位置**  
[L52441–52521：10、70、101 个子 Agent 的个人报告；外部 OMH 转为实验的受控缰绳](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52441)

**G05｜7 月 10 日：模型内化 Review 与分解**  
[L53013–53050：自动规划、拆依赖、删除代码、对抗 Review；“模型把 Harness 都内化了”](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:53013)

**G06｜7 月 11 日：自动 DAG、成本与递归故障**  
[L53933–54007：Ultra 自审、自动 DAG、任务明确时可能过度自作主张](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:53933)  
[L54080–54115：子 Agent 无限递归打爆进程、并发实现问题](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:54080)

**G07｜7 月 14 日：Humanize 的哪些部分被“炼化”**  
[L55846–55935：Builder–Reviewer、Goal Tracker、短期记忆被认为已内化；Pop Quiz 留给人；直接许愿与讨论式编程](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:55846)

- “炼化”是参与者根据外部行为做的判断，不能写成模型训练过程的事实。

**G08｜7 月下旬：几百个子 Agent 的 UI 与生命周期**  
[L67657–67693：历史约 500 次、并发 32 的个人测试；桌面端加载、软硬上限与进程管理问题](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:67657)

**G09｜7 月下旬：派发能力超过基础设施承载**  
[L61570–61610：模型偏好启动子 Agent，但基建跟不上，个人报告消耗半个五小时窗口后白干](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:61570)

**G10｜记录末段：不可见后台任务读取浏览器上下文**  
[L68543–68550：Ambient Suggestions 临时任务、DOM 快照、未显示为普通 Session；审计报告未发现点击或编辑](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68543)

- 这是参与者对一次产品行为的排查报告，正文用它说明可观测性问题，不推断恶意行为。

### H. 裸 Agent、星舰与简化

**H01｜7 月下旬：模型越强，Harness 越轻**  
[L61740–61765：基模增强后 Less is more；共享记忆、自动记忆与过度结构的争论](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:61740)

**H02｜7 月 28 日：星舰、船坞与裸 Pi**  
[L64473–64568：动态 Steer、无限续跑、星舰/船坞梗；裸 Pi、极短 Prompt、角色选模型](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:64473)

**H03｜7 月 28 日：只留 Bash 与 Sub-agent**  
[L64856–64915：删除 Read/Edit/Write 后的个人体验；复杂 Bash；AI Native 系统难以止血](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:64856)

**H04｜7 月 6 日：Snapshot + Sandbox**  
[L51128–51183：tmux/SSH/容器/VNC 的类比；超长程探索回滚、动态 Fan-out、Runtime 与 Environment 分离](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:51128)

**H05｜记录后段：能力增强后仍不能外包 Thinking**  
[L65230–65320：高模型/低模型角色、Pi 极简、人的批判与规划、不要只 Approve](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:65230)

**H06｜记录后段：Agent 主动重写与删除代码**  
[L68637–68659：实现后继续阅读并提出更凝练解法](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68637)  
[L68773–68819：一夜删除一万余行、四个月前后能力对比、Build/Review/简化分工](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68773)

**H07｜记录末段：Simplify / Verify Hook**  
[L68910–68923：任务完成后调用 Simplify；反复 Simplify 与 Verify，收敛到最小完整实现](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68910)

**H08｜记录末段：标准化最好成为 Tool，而不是作文要求**  
[L68947–68975：Agent Fork/Hack 通用依赖；标准化降低工程成本；Tool/表格/填空式约束](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68947)

## 四、正文中应保持的事实边界

1. **不能把个人规模报告写成 Benchmark。** 22 个 Agent、4.7 万行、101 个 Agent、删除一万或十几万行都缺少统一任务、基线、质量指标和复现实验。

2. **不能把“禁止沟通”写成绝对规则。** 记录保留了跨代码库、Context Handoff、共享验证事实、Brainstorming 和探索任务的例外。

3. **不能把 h2/h3 写成成熟定型产品。** 记录中多次明确它们处于 POC、试验、接口存在但不稳定或路线变化阶段。

4. **不能把“模型炼化 Harness”写成内部训练事实。** 这是根据外显行为做出的社区解释。

5. **不能把 Memory 负收益写成普遍结论。** 这是 Coding 和特定项目中的多次个人经验；多人协作、知识型任务仍可能需要 Memory。

6. **不能把管理学角色与 PL/IR 写成互斥路线。** 记录后段的 Arch/PM/Audit 使用管理学命名，但职责、权限、输入输出仍是工程化定义的。

7. **不能替动态主义与组合主义判胜负。** 记录最后明确按任务分流，自动平衡机制仍未知。

8. **不能把产品行为写成当前产品文档。** 本文只是在还原聊天记录当时的观察；版本、额度、模型和 UI 都会变化。

## 五、出版前核对清单

- 回到原截图核对所有准备署名的原话。

- 对代码量、运行时间、Agent 数量等案例，询问发言者是否愿意公开，以及是否要补充项目背景、验证方式和失败条件。

- 确认是否保留具体模型与产品名；若小册子追求长期有效，可把部分名称改成“Builder 模型”“Reviewer 模型”“前沿模型”。

- 对 Humanize 的 h1/h2/h3 历史，邀请项目维护者做一次技术校对，尤其核对版本与时间顺序。

- 公开版删除本索引中的本地路径；如需引用，换成经过授权的截图编号或社区归档链接。

- 保留反对意见与未决问题，不把讨论整理成一套事后看起来从未摇摆过的路线。
