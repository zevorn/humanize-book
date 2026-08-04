# Claude Code Dynamic Workflows 一手资料卡

## 名称与时间

- 正式名称是 **Dynamic workflows**；Auto Work 与 Auto Code 均属误记。
- Anthropic 于 2026-05-28 发布[产品公告](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)，并随 [Claude Code v2.1.154](https://github.com/anthropics/claude-code/releases/tag/v2.1.154)正式引入。
- 同日发布的 [Claude Opus 4.8 公告](https://www.anthropic.com/news/claude-opus-4-8)将它标作 Research Preview。产品文章后来更新为 Generally Available，整理历史时要区分首发状态与当前状态。

## 官方机制

- Claude 会根据任务动态编写 JavaScript 编排脚本，将工作拆给数十到数百个并行 Subagents，并在汇总前安排独立验证。
- Workflow 的协调发生在主对话之外，运行进度可以保存，任务中断后可以恢复。
- Auto Mode 是官方建议搭配的权限模式；`ultracode` 是 `xhigh` Effort 加自动 Workflow Orchestration 的触发设置。两者都不是功能名称。

## 与 Humanize 的关系

Humanize 群在 5 月 29 日把 H2 概括为强契约静态 Workflow，把尚在设想中的 H3 概括为 Agent 可更新的动态 Workflow。[群聊原文 L28740](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:28740)

两条路线在时间上接近，技术关切也相似；目前没有证据证明 Anthropic 参考了 Humanize。正文宜写“同向出现”或“互相映照”，不写成直接影响关系。
