# Humanize 1.17 与 H2 原型

## H1 收官版本的证据边界

- 2026-04-21，群聊中明确说“1.17.x 会是 Humanize 1.0 的最后一个版本”，并把 H2 的第一项目标描述为模型无关。[群聊原文 L12943](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12943)
- 2026-05-01，开发线上出现 [`f4e5721`](https://github.com/PolyArch/humanize/commit/f4e5721e344ef602a77cfb3511ec51b74e387120)，提交信息为 `chore(release): bump plugin version to 1.17.0`。
- 2026-04-30，[PR #51](https://github.com/PolyArch/humanize/pull/51)将 1.16 合入 `main`；公开主线的 README 与插件清单后来仍标为 `1.16.0`。GitHub 也没有对应的 `v1.17.0` tag 或 Release。因此，正文宜把 **1.17 写成 H1 的开发线收官标记**，并注明公开主线最后一个明确合并里程碑是 1.16。

## H2 的概念线

- 2026-04-22，群聊提出三层结构：`humz` 描述 Agentic Flow，`hcc` 把 Flow 编译成实际 Harness，`hvm` 执行编译结果与用户输入。[群聊原文 L13255](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13255)
- 2026-04-23，讨论把 Codebase、Context、Prompt、State 视作 Flow 中的类型，并给出 `Agent = Model × Tool × Action × Permission`。[群聊原文 L13960](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13960)
- 同一轮讨论强调，Workflow-as-PL 是一套思维模型，实际实现可以采用现成语言；重点在于抽出稳定的编排原语，并将 Flow 与具体 Agent 解耦。[群聊原文 L14263](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14263)
- 2026-04-30，H2 被概括为“AgentVM + flow 编程语言”，同时仍被作者称为失败概率很高、不适合生产的 MVP。[群聊原文 L16788](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16788)

## 可核验的 H2 代码原型

- 2026-05-17（北京时间），[`3fccb60`](https://github.com/PolyArch/humanize/commit/3fccb60c11332fb322a295db0583432416c7cf07) 将 H2 原型合入 `h2-dev`。
- 这次提交采用 TypeScript，实现 MCP server hub、HTML workflow runtime、Codex/Claude Agent backend、Dashboard、Workflow Coordinator、Storage、Recovery，并把 H1 的 RLCR、gen-idea、gen-plan、refine-plan 表达成 Flow cartridge；当时可用的 Agent backend 只有 Codex 与 Claude。
- 这条实现路线与 4 月讨论中的 Rust、MLIR 类比和小型 VM 设想有明显差异。正文应保留这种变化，把 H2 称作路线与 POC；公开仓库没有独立的 Humanize 2.0 tag 或 Release。
- 5 月 16—17 日的群聊也给出了同样的使用边界：H2 用于开发和测试 Flow，本阶段不面向普通项目的稳定生产使用。[群聊原文 L21886](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21886) [群聊原文 L22098](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22098)
