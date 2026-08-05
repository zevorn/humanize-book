# Humanize 3、Dynamic Workflows 与 KDA

## 三种“动态”需要分开

1. **静态 Flow**：人在运行前写好图、条件和检查，Agent 按已知结构执行。
2. **动态生成或选择 Flow**：Agent 根据任务生成编排脚本或选择模板；这次
   运行仍有一份具体的执行结构。
3. **运行中可修改 Flow**：Agent 或人依据中间结果提交 Graph Revision，
   后续节点使用新版本；这正是 H3 的核心实验。

Anthropic 于 2026-05-28 发布
[Claude Code Dynamic Workflows](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)，
首发版本是 [Claude Code v2.1.154](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21154)。
官方说明 Claude 会现场写 JavaScript 编排脚本，调度数十到数百个
Subagent，并在汇总前做独立验证。首发状态是 Research Preview；
公告后来更新为 GA。

6 月 2 日，Humanize 群把厂商方案理解为“动态生成、静态执行”，把 H3
定义为 Agent 可以修改正在运行的 Workflow。作者同时承认谁来改、何时
触发、怎样证明修改合理，都还没有答案；早期设计要求修改经人类批准，
也保留实验性的放开模式。
[群聊原文 L32248](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32248)
[群聊原文 L33113](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33113)

## 从热修改收紧到受控演化

H3 的实现边界在 6 月中旬很快发生了变化：

- [6 月 12 日的 Mutable Runtime](https://github.com/humanfia/oh-my-humanize/commit/eea3778e2e5ba7fa38f90eae6da4d9d9461a1474)
  集中实现 Lifecycle、Graph Patch、Checkpoint 与 Session Runtime。
- [6 月 13 日的安全校正](https://github.com/PolyArch/oh-my-humanize/commit/eb78a8eacc905434dd340f01a0f1ea8fa5d90276)
  开始拒绝向 Active Run 直接提交 Graph Patch，要求改走 Workflow Change
  Request。
- 6 月 14 日的工作流文档规定，生产 Attempt 绑定 Immutable Freeze。需要
  改 Flow 时，操作员先停止运行、保存 Checkpoint、批准变更、冻结新图，
  再从 Checkpoint 重启。

这段实现史说明，早期的 Live Mutation 很快收紧成了 **Controlled
Workflow Evolution**。Agent 仍可提出和参与修改，生产运行则保留授权、
不可变快照、审计与恢复边界。正文若只写“Agent 能修改正在运行的
Workflow”，会漏掉这次很关键的工程回摆。

## 九种 Flow 的上线与撤回

- [2026-06-14 的提交](https://github.com/PolyArch/oh-my-humanize/commit/aaf46428db15a2cfe2b18f9eae9a61827f47d1c1)
  将一批实践 Flow 升为 Built-in。
- 6 月 15 日的公开试用共有九种 Flow，包含 Humanize 1.0 RLCR 与 KDA。
- [2026-06-16 的提交](https://github.com/PolyArch/oh-my-humanize/commit/21e56a0892beeffdab258157860ec9d94f25e378)
  又把未充分验证的 Built-in 降级。6 月 18 日，作者在群里解释：发现
  一两个 Flow 有 Bug 后选择整体回滚，要求本地连续运行 80 小时后再升格；
  RLCR 与 KDA 当时仍被认为可用。
  [群聊原文 L45897](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45897)

“九种 Flow”因此只是一段短暂的公开试用状态，不能写成持续稳定的
正式内置列表。80 小时也是作者当时设定的工程门槛，不等同于成熟的
Agent Benchmark。

## KDA 的证据边界

- [Kernel Design Agents](https://github.com/mit-han-lab/kernel-design-agents)
  是面向 CUDA Kernel 研究、实现、验证与迭代的 Agent Workflow。公开
  原型使用 Humanize 生成 Plan 与运行 RLCR，并结合 KernelWiki、Nsight
  Compute 报告 Skill、正确性验证和性能证据。
- [MLSys 2026 FlashInfer Contest 复现仓库](https://github.com/mit-han-lab/mlsys2026-flashinfer-contest)
  记录了 Full-Agent Approach 三条赛道的成绩：MoE 第 1、DSA 第 2、
  GDN 第 3。该仓库把 Humanize 列为核心方法，并明确将最终 Kernel、
  验证环境和工作流材料分开。
- OMH 中的 `kda-humanize` 直接把 Humanize RLCR 表达成 Subflow，这使它
  成为“H1 专用 Flow 如何进入 H3 Flow Infra”的具体样例。

群聊常把 KDA 与 NVIDIA Track、NVIDIA 工程背景成员放在一起讨论；公开
仓库归属 MIT HAN Lab，竞赛名称是 MLSys 2026 Competition NVIDIA Track。
现有一手资料不足以把 KDA 写成 NVIDIA 官方产品或主要由 NVIDIA 内部
使用的系统。
