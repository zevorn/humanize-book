# Pi、Oh My Pi 与 oh-my-humanize

## 名称勘误

- 正确项目名是 **Oh My Pi**，常缩写为 **OMP**；`OmniPi` 是误记。
- [Oh My Pi](https://github.com/can1357/oh-my-pi) 的官方 README 将其说明为
  Mario Zechner 的 [Pi](https://github.com/earendil-works/pi) 的 Fork。
- 群聊中的“龙虾”或“小龙虾”指 [OpenClaw](https://github.com/openclaw/openclaw)，
  不指 Humanize。6 月 10 日的对话也明确把 OpenClaw 与 Pi 联系在一起。
  [群聊原文 L38222](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:38222)

## H2 为什么转向 OMP

- 5 月 22 日，Oh My Pi 首次在群里被强烈推荐；同一段对话还回忆了
  用 Pi 修 OpenClaw 的经历。
  [群聊原文 L25004](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25004)
- 5 月 28 日，刘思皓提出 “I need to build h2 on omp”，随后解释 OMP
  已经提供了模型接入、Agent Loop、工具和终端交互所需的脚手架。
  [群聊原文 L27882](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27882)

这里存在一条容易混写的实现顺序：5 月 17 日公开的 H2 POC 使用
TypeScript、HTML Workflow Runtime 和 MCP Hub；它先于 OMP 路线。
后来的 `oh-my-humanize` 才在 OMP 上重新实现 H2/H3 的 Flow 能力。

## oh-my-humanize 的公开历史

- [PolyArch/oh-my-humanize](https://github.com/PolyArch/oh-my-humanize)
  创建于 2026-06-01 UTC，对应北京时间 6 月 2 日。最早的一组提交先
  加入 Workflow 定义、条件、调度和运行记录；[随后数小时的提交](https://github.com/PolyArch/oh-my-humanize/commit/fccda309629d02ee033f06819a2554d8b6a8ca22)
  已支持在运行时调度 Workflow Graph Revision。
- [6 月 12 日的 mutable runtime 提交](https://github.com/PolyArch/oh-my-humanize/commit/eea3778e2e5ba7fa38f90eae6da4d9d9461a1474)
  将 Agent-mutable Workflow 作为可运行能力集中落地。
- [6 月 13 日的安全校正](https://github.com/PolyArch/oh-my-humanize/commit/eb78a8eacc905434dd340f01a0f1ea8fa5d90276)
  随即拒绝向 Active Run 直接提交 Graph Patch。生产运行后来绑定
  Immutable Freeze；变更通过 Stop、Checkpoint、Approve、Freeze、
  Restart 生效。这使 Live Mutation 收紧成可审计的受控演化。
- 6 月 15 日，群里公开邀请成员试用，并把 OMH 描述为 OMP 的增量实现；
  H2 的 Flow Language 与 H3 的 Flow Infrastructure 都被放进 OMH。
  [群聊原文 L42888](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42888)
- 6 月 19 日 UTC（北京时间 6 月 20 日），项目从 Fork Network 迁移到
  [humanfia/oh-my-humanize](https://github.com/humanfia/oh-my-humanize)。原
  PolyArch 仓库保留迁移说明，不能把两个地址误写成两个独立实现。

今天的 OMP 与 OMH 已继续大幅演进。整理 6 月历史时应优先引用当时的
提交和群聊，不能用当前 README 中后来加入的功能倒推早期版本。
