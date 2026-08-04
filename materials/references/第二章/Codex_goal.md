# Codex `/goal` 一手资料卡

## 首次公开版本

- OpenAI 于 2026-04-30 16:40 UTC 发布 [Codex CLI 0.128.0](https://github.com/openai/codex/releases/tag/rust-v0.128.0)，对应北京时间 5 月 1 日凌晨。
- Release Notes 将 `/goal` 列为新功能：持久化 Goal、App Server API、模型可调用工具、Runtime 自动续跑，以及创建、暂停、恢复和清除等 TUI 控制。
- 5 月 1 日，OpenAI 维护者在 [Issue #20591](https://github.com/openai/codex/issues/20591#issuecomment-4030419128) 中说明该功能仍处于开发和实验阶段；用户需要经 `/experimental` 开启。今天看到的稳定状态不能倒推为首发时已经成熟。

## 它具体做了什么

- [PR #18073](https://github.com/openai/codex/pull/18073) 为每个 Thread 增加可持久化的 Goal 状态，记录 Objective、Active/Paused/Complete 等状态，以及 Token 与运行时间。
- [PR #18076](https://github.com/openai/codex/pull/18076) 把自动续跑放进 Core Runtime：当前 Session 空闲、没有更高优先级的用户输入时，Runtime 可以继续推进 Goal；中断会暂停，恢复 Thread 时可重新激活。
- [PR #18077](https://github.com/openai/codex/pull/18077) 增加 `/goal <objective>`、`pause`、`unpause`、`clear` 与状态展示。

## 出版时的表述边界

`/goal` 首发时属于 **Codex 产品与 Runtime 内置的 Harness 能力**。它不是 GPT-5.5 基座权重中的一个可单独验证特征。正文可以写“Codex 把持续目标和自动续跑做进了自身”，避免直接写“模型已经把 Ralph Loop 训练进权重”。

Humanize 群的体验也有明显分歧：5 月 6 日，有成员认为它把 Build、Test、Review 融在同一推进过程中；5 月 26 日，另一轮讨论又把 Humanize 概括为“强 Review + Static Planning”，把 `/goal` 概括为“弱 Review + Dynamic Progressive Planning”。[群聊原文 L17817](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17817) [群聊原文 L26500](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:26500)
