# Human Harness 与 Coach Mode

## 问题是怎样出现的

- 2026-05-09，群聊把 H2 的困难描述为两种极端：完全脱手后，人无法
  对代码负责；完全了解全部细节，人的心智负担又过高。随后提出的原始
  问题是“巨型 agentic 自动化系统如何保证人类设计者、使用者时刻知情”。
  [群聊原文 L18913](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18913)
- 2026-05-10，讨论继续收紧到“超过 15 个智能体构建出来的代码库，
  人怎样保持掌控”，并提出把人的有限带宽放在关键的
  Human-in-the-loop 检查点上。
  [群聊原文 L19098](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19098)
- 2026-06-18，另一轮长程任务讨论直接使用了 `cognition overload`。
  [群聊原文 L45831](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45831)

`Human Awareness Cognitive Load` 没有作为完整术语出现在原始群聊中。
正文将它作为回顾性标签使用时，应说明原文分别讨论了“保证人类知情”
和 `cognition overload`，不能倒写成当时已经确定的项目名。

## Human Harness 的原始设计

- 2026-05-12，社区把“抽样层级考试”选作 H2 的“人类被介入”机制，
  同时保留跳过选项。这里的思路是让 Flow 主动选择值得人理解的决策，
  控制检查频率，而不是把全部 Trace 再交给人通读。
  [群聊原文 L19874](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19874)
- 同日晚些时候，群里出现“agent harness 让 AI 更强大，human harness
  让人类更负责”的表述，并提出在 `gen-plan` 生成过程中设置检查，
  不等到完整 Plan 出来后再统一审阅。
  [群聊原文 L19933](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19933)
- 问题分成三类：让人复述自己的设计；让人检查 Agent 的设计是否符合
  本意；补足继续规划所需的背景知识。群里将其概括为
  “记忆—自检—教育”。
  [群聊原文 L19970](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19970)

## 从讨论到仓库实现

- 2026-05-13，群里使用了 `Plan-time Human Verification`、
  `Interactive Plan Comprehension Gate` 和“老师模式”等名字。
  [群聊原文 L20401](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20401)
- 同日创建的 [Humanize PR #159](https://github.com/PolyArch/humanize/pull/159)
  将它实现为 `gen-plan --coach`。PR 于 2026-06-13 合入 `dev`。
- 合入版本在 First-pass Analysis、Candidate Plan、每轮 Convergence 和
  Finalization 之间设置强制检查。回答偏差会分别进入设计意图漂移、
  AI 设计修正或背景知识缺口；最终 Plan 写入前还需整体接受。

Coach Mode 因而有两个时间点：5 月 13 日是概念和 PR 的出现，6 月
13 日是代码合入。正文不应把早期讨论写成当时已经发布的稳定功能。
