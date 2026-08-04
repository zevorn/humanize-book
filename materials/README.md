# Humanize Book 编辑材料

这里集中存放正文写作之前的时间序语料、历史证据和检索索引。根目录的 [README](../README.md) 是小册子正文入口。

## 时间序材料

- [Agent 发展史：时间序语料初筛](timeline/Agent发展史_时间序语料初筛.md)：按聊天记录日期排列的长篇原文底稿。

- [Agent 发展史：关键节点导览](timeline/Agent发展史_关键节点导览.md)：模型、产品与 Humanize 思路变化的中性导航。

## 研究证据

- [Agent 发展史：一手资料核查](research/Agent发展史_一手资料核查.md)：官方公告、GitHub、技术文档和 X/Twitter 证据。

- [第一章「Humanize 诞生」一手资料补充核查](research/第一章_Humanize诞生_一手资料补充.md)：GAAC → Humanize 起源、CCC、个人工程线、社区讨论及典型 Issue 的逐项证据与勘误。

- [第二章「Humanize 1 → H2」一手资料核查](research/第二章_Humanize2_一手资料核查.md)：PID 长尾、1.17 版本边界、Flow ISA / `hvm` 及后见性的 Flow IR 术语、Codex `/goal` 与 Claude Dynamic Workflows 的逐项证据。

## 参考资料快照

- [第二章参考资料卡](references/第二章/README.md)：Humanize 版本、`/goal`、Dynamic Workflows，以及 2026 年 4—5 月国内外模型与 Agent 工具变化的一手资料快照。

## 检索索引

- [群聊引用链接索引](indexes/Agent发展史_群聊引用链接索引.md)：初筛语料中保留的外部链接及邻近语境。

- [Agent 篇素材索引](indexes/Agent篇_素材索引.md)：早期主题整理使用的原文行号索引。

## 草稿与工具

- [Agent 篇主题总结初稿](../drafts/Agent篇_主题总结初稿.md)：第一轮压缩式文章草稿，作为历史草稿保留，不是当前主稿。

- [时间序语料生成脚本](../scripts/build_agent_timeline.py)

- [群聊链接索引生成脚本](../scripts/build_agent_link_index.py)

## 建议使用顺序

1. 从关键节点导览确定要研究的月份或阶段。

2. 回到时间序语料阅读当时的连续聊天和社区反应。

3. 用一手资料核查确认外部事件、仓库版本和发布日期；需要快速回看官方节点时，再打开参考资料快照。

4. 需要查某条引用时，再使用链接索引或素材索引返回原文件。
