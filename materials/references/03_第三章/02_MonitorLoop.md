# Monitor Loop：长程任务的外部监工

## 名称与时间边界

`Monitor Loop` 是群聊中出现过的原词，也是社区给这套长程任务监控
实践起的名字。当时没有厂商使用它作为正式产品名：

- 2026-06-06，群里第一次完整描述 Claude Code `/loop` 监控 Codex
  `/goal` 的做法。
  [群聊原文 L34718](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:34718)
- 2026-06-07，这套做法被称作 “Humanize 2.7”：第三方 Agent 监控整个
  Workflow，在大尺度偏离时生成 Steer Prompt。
  [群聊原文 L35444](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35444)
- 2026-06-08，作者称自己同时运行十个“监控 loop”，并为已经确认的
  原则加入少量 Auto-inject 白名单。
  [群聊原文 L36338](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36338)
- 2026-06-10，群聊直接使用 `Monitor Loop`，将 Human 放在有限的关键
  Check Point 上。
  [群聊原文 L37862](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:37862)
- 2026-06-17，[`monitor-codex-goal` Skill](https://github.com/SihaoLiu/skills/tree/ec9cd9e2733f28d93bbf66c37ef58722cf6390ce/monitor-codex-goal)
  公开，将这套实践写成可复用规则。
  [首次公开提交](https://github.com/SihaoLiu/skills/commit/ec9cd9e)
- 2026-06-18，社区又把 Monitor Loop 用到 Flow 测试中，让它观察测试
  Path 是否符合预期、执行有没有跑偏。
  [群聊原文 L45971](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45971)

## 当时的典型链路

1. Human 给 Codex `/goal` 一份 Plan 或 Goal，由它持续执行长程任务。
2. 独立 Claude Code Session 使用 `/loop 1h` 定时读取代码库与 Codex
   Transcript。Monitor 不参与目标仓库的实现。
3. Monitor 检查主线进展、低效深挖、死胡同、伪造数据、Stub 和项目
   Invariant。最初讨论主要关注“进度监工”，后来的 Skill 扩展了事实与
   完整性检查。
4. 发现问题后，Monitor 拟定 Steer Prompt，并通过 Remote Control 向
   手机发出通知。
5. 涉及新方向、策略、优先级或范围的 Prompt 由 Human 审批，再通过
   tmux 注入正在运行的 Codex TUI。已经明确的人类原则可进入受限的
   Auto-inject 白名单。

对应群聊：

- [`/loop`、Transcript 与 Remote 通知](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:34720)
- [Claude、Codex 与 Monitor 的角色分工](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:34984)
- [读取完整 Transcript、tmux 注入与人工审核](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35045)
- [从三个 `/goal` 到十个 Monitor Loop 的自报实践](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35444)
- [手机审批后再注入 Steer Prompt](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35813)

## 两个容易混淆的地方

第一，主路径中运行 `/goal` 的是 Worker，Monitor 使用 Claude Code
`/loop`。群里也有人用一个 Codex `/goal` 监控另一个 `/goal`，但当时
已经有人担心同模型会陷入相关错误。

第二，[`watch-codex-goal`](https://github.com/SihaoLiu/skills/blob/main/watch-codex-goal)
是 6 月 23 日后加入的机械 Watcher。它发现 TUI 被 Block 或长时间无变化
时发送 `/goal resume` 或 `continue`。它没有承担高层语义审计，不能与
`monitor-codex-goal` 混写。

## 后来的公开 Skill 固化了什么

[当前公开的 `monitor-codex-goal`](https://github.com/SihaoLiu/skills/tree/main/monitor-codex-goal)
将 Monitor 设为只读审计者：它从目标
Transcript 中重新提取人类约束，以独立 Subagent 检查进度、Git 变化和
Artifact 合理性。新的方向必须经人批准；只有重复既有原则或拦截严重
完整性问题时，才允许在通知链路有效的前提下自动注入。

Claude Code 的官方文档也能解释两个底层能力：[`/loop`](https://code.claude.com/docs/en/scheduled-tasks)
负责在当前 Session 中重复运行检查；[Remote Control](https://code.claude.com/docs/en/remote-control)
让本地 Session 可以从手机继续操作，并在需要决定时发送移动通知。

这套实践的价值在于调整 Human 的介入频率。日常巡检由 Monitor 完成，
Human 只在需要改变方向、处理未知问题或批准高风险反馈时回来。
