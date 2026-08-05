# 模型“内化”与轻量 Harness

## “内化”是社区解释

2026-07-10，群友观察到 GPT-5.6 会自动规划、拆分依赖、派出
Subagent，并主动进行多轮 Adversarial Review，随后用“把 Harness 都
内化了”描述这种体验。
[群聊原文 L53013](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:53013)
[群聊原文 L53044](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:53044)

[GPT-5.6 官方公告](https://openai.com/index/gpt-5-6/)可以确认：

- `max` 给单个 Agent 更多时间推理、检查和修改；
- `ultra` 默认协调四个 Agent 并行工作；
- Responses API 的 Multi-agent Beta 可构建类似 `ultra` 的体验；
- Programmatic Tool Calling 允许模型写小程序协调工具与中间结果。

这些公开信息无法继续拆分权重、System Prompt、Runtime 和产品编排分别
贡献了多少。正文中的“内化”应解释为一组 Harness 能力进入了产品默认
路径，不能写成已经证明所有 Workflow 都训练进了模型权重。7 月 28 日，
群里也直接追问 `ultra` 到底来自权重还是隐藏 Harness，说明参与者当时
并没有一致答案。
[群聊原文 L64429](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:64429)

## 长程失败使 H1 再次出现

2026-07-24，一次 Sol 长程重构经历五次 Context Compaction，产生六千多
行改动，却重新采用了人类已经否决的设计。讨论随即转向 Monitor、RLCR
和 Humanize 1.0，并留下“说好的不需要 Harness 的时代呢”这句反问。
[群聊原文 L62193](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62193)
[群聊原文 L62245](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62245)

2026-07-26，另一位群友报告 Sol `ultra` 在多次压缩后丢失深层
Subagent 的生命周期，主 Agent 的职责也发生漂移。现阶段的处理方法是
按阶段停下，与人重新对齐；群里把它叫作 `human as memory`。
[群聊原文 L63768](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:63768)

这两段属于社区个案，不能推导出 GPT-5.6 的普遍故障率。它们可以支持
一个更窄的结论：模型具备自动编排能力以后，持久目标、独立验证、停止
条件和 Human Checkpoint 仍有真实用例。

## Bare Pi 也是 Harness 选择

2026-07-29，群友将 Kimi K3 的 Pi 环境缩减到 Bash 与一个 Subagent，
自报 Token 使用下降、效果反而更好，并总结为“高级食材不需要高级
烹饪”。这是单个项目的体验记录，无法作为普遍效率数据。
[群聊原文 L65151](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:65151)

[Pi Extensions 文档](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md)
显示，Pi 允许动态加入工具、命令、事件 Hook 与界面组件，也允许从
`--no-tools` 的空工具面开始。轻量 Harness 的含义因此很具体：让模型
保留更大的现场判断空间，只外置真正需要的权限、工具与验证器。

Claude Code 走的是另一种产品形态，但也能看到同一组边界：

- [Permissions](https://code.claude.com/docs/en/permissions)控制工具和
  敏感动作；
- [Hooks](https://code.claude.com/docs/en/hooks)把确定性检查放进生命周期；
- [Subagents](https://code.claude.com/docs/en/sub-agents)隔离 Context、角色
  与工具权限。

由此可见，Harness 的方法并不取决于框架大小。删除工具、缩短 Prompt、
保留独立 Review，和增加一套 Workflow Runtime 一样，都是对 Agent
信息流与动作边界的设计。
