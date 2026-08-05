# Humanize 聊天记录：Agent 相关内容时间序初筛版

> 这是一份供后续人工分析使用的原始语料初筛，不是总结文章。
>
> 配套阅读：[关键节点导览](../../timeline/01_Agent发展史_关键节点导览.md)；[一手资料核查](../../research/00_Agent发展史_一手资料核查.md)；[群聊引用链接索引](../../indexes/02_Agent发展史_群聊引用链接索引.md)。
>
> - 所有聊天正文均按原文件顺序保留，未改写、未纠正 OCR、未重排发言。
> - 仅删除明显无关区段，以及群聊邀请/撤回提示、单字符 OCR 残片等高置信噪声。
> - 筛选采用高召回策略：Agent、Humanize、Harness、Flow、上下文、并行、Review、Memory、Skill、MCP、人类在环等内容及其前后语境均尽量保留。
> - 每个片段都标有原文件行号。署名、引用关系和数字如需公开，仍应回到原截图核对。
> - 原文中的“龙虾/小龙虾/虾”按上下文指 OpenClaw；AutoGPT 不在这份群聊中，不能混称。

## 文件信息

- 原文件：`/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md`
- 原文件 SHA-256：`349efc7f1c242078b6b6323b321e9a4c8b1711479fa05629fb2eff7aeaefd429`
- 原文件总行数：68,975
- 命中片段：578
- 进入片段的原始行数：19,105
- 删除高置信噪声后保留行数：18,227

---

## 3 月｜3 月 18 日—3 月 31 日

### 3月19日

#### 原文 L60–L153

[回到原文件 L60](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:60)

- 但是 tmux可以玩好多花活儿
- 3月19日00:12
- 还有显示bug
- 我记得调个设置，关闭gpu优化就好了
- 让 claude/codex 通过 tmux 给自己输入命令
- 自己pua自己
- NV 周耀阳: 让 claude/codex 通过 tmux 给自己输入
- 命令
- 这个我也做好了
- 是的
- 泽文: 我现在让 cc 用 tmux + gdb 来调试
- 些交互式的测试，tmux很方便
- 3月19日00:14
- ，但是cc好像有gdb调试的技能吧
- 但 tmux 跑 parallel team 的时候
- cc 会有一些起卦ID bug
- 之前让他调bug，就看他居然会用gdb
- *奇怪的 bug
- tmux主要并发我把名字配上，一把开5个10个的
- 然后找个ai去总结他们干啥
- 我给我写的嵌入式龙虾，增加了对Linux的支持，方便进行
- Noa a :bung
- 其实claude原生的蜂群模式就是这么做的
- NV周耀阳: 让 claude/codex 通过 tmux给自己输入
- 命令
- 其实这种做法是人类学自己违反了自己的用户协议
- 但是claude code agent teams的做法就是起tmux, 然后让leader直接往另一个tmux pane里面注入消息
- 重新编译之后，最近我没怎么闪退了
- 刘思皓: Note: tmux需要自己编译一个稳定版，
- package manager里面自带的那个， 对很多ai工具支..
- 3月19日00:19
- yep
- 理论上这样可以无限烧 token
- 刘思皓:按道理是不可以通过任何自动化的方式，往一个
- 基于订阅的claude code里面输入消息的
- "没怎么"？意思是还有概率出现闪退吗？
- 重新编译之后那一周闪退过一次
- 之后就再也没有闪退了
- 对，就是3.6a
- 我反正换成 tmux = https://github.com/tmux/tmux/releases/tag/3.6a
- 之后就再也没有闪退tmux了
- 我还专门退出了所有session，确保换成了3.6a
- 闪退非常炸裂，你甚至没法恢复对话
- 是的
- 3月19日00:23
- @十进. 以前是不是提到过 tmux 自动保存的
- https://github.com/tmux-plugins/tmux-resurrect之前用的这个
- 3月19日01:00
- 我发现@王邦彦之前总结的一个白天交互式开发的最好比喻就是:国际象棋里面的pre-move
- 你在ai跑的时候，就可以把下一步要做什么全写了
- 我发现我现在写plan的速度越来越快了，大概AI跑完一轮plan,我能产生两个plan
- 也就是下班前，能多出一大堆plan没做完.然后你把今天一整天产生的plan汇成一个大文档，直接丢给humanize然后睡觉
- 第二天代码库就和艺术品一样:一个高度规范的，你完全理解每一个细节的，测试覆盖完善的代码库
- 3月19日01:10
- 这是我第一次脑子吐plan的速度快过ai干活的速度
- 3月19日01:31
- 我之前用 kitty，后来 macOS 26 的 terminal 大 refactor后就直接用系统 term了
- claude自己,他说AI时代最好的终端是kitty/ghostty....
- 3月19日02:17
- 我今天重新更新了一下SOTA认知:
- B=opus,R=codex依旧是SOTA组合，证据是我最近连续三天用codex干活，claude审查，claude从未查出过任何问题
- 3月19日02:31
- 话说我个人用不太想codex再买一个200有什么平替吗（
- 3月19日02:50
- 还是软
- 主要是gemini和老马不给力啊
- 无觉得gemini的dr是nb的
- 但是code实在是不行
- 3月19日02:55
- 我*
- 刘思皓: 无觉得gemini的dr是nb的
- 3月19日03:09
- en gemini dr 是 nb
- 我没找到那个人民币神秘 gpt 有什么 pointer 吗(
- 3月19日03:14
- 你是说隔壁群的中转嘛@蟑螂恶霸盾构机
- 3月19日03:32
- funny 我有个 one shot task 没用 humanize，有点长所以 claude 竟然主动调了 humanize。最近 claude code
- evolve 得我有点震惊
- 3月19日05:25
- 神秘，试了一下 copilot cli简直是 token 免费大派送
- 我觉得我需要vibe —个 humanize copilot codex review
- 3月19日09:07
- 我调研了国内的ai coding套餐
- 现在copilot是按次付费的，不是按上下文.………..对“次”的定义非常宽松...…..所以像humanize 这种喂一个巨大
- prompt的工作方式也是“一次调用”
- 有人为了用copilot 节省次数，专门写巨大的 plan

---

#### 原文 L186–L275

[回到原文件 L186](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:186)

- 3月19日11:55
- 最近在砍柴，因此没有磨humanize的刀🙏
- 3月19日12:02
- humanize的rlcr循环因为网络问题中断了应该如何继续呢
- /resume，然后continue
- continue是继续/humanize-rlcr嘛
- 就是跟他说继续
- 3月19日12:53
- humanize的loop是和session id绑定的
- 所以resume loop就是直接进入原来的claude session，然后直接说：继续
- 3月19日13:05
- 我其实最近觉得humanize也不怎么好用了
- 泽文: humanize 好用啊
- 可能我用太久了有点习惯了
- 没有初见的那份震撼了
- 我感觉现在的AI工具还缺少—种 deep insight from unseen/unspoken
- 靠humanize这种loop堆超级力工不是正解
- 主要还是ai还不够聪明
- 俗手本手妙手，humanize大概是个还不错的俗本手，不是很妙
- 3月19日13:11
- 没有瞪眼法one shot就能做出来的美感
- 3月19日13:11
- 注意到
- 还有个很重要的原因是ai没法直接读整个项目代码
- 它读都是一段段读的
- 容易错失全局，写成很奇怪的代码
- codex这点比较好，我见过最长的codex run 改代码之前能看一个小时的代码
- 这事在claude里面是不可能发生的
- 上下文长度锁死了
- 3月19日13:22
- ai的上下文像是人类"扫一眼"的那种记忆
- 如果要总览全局，最好的办法还是把项目代码训练进参数里
- 3月19日13:28
- 最近在试着用 claude code 辅助我进行系统性的学习和写作，一个我比较满意的成果可以参考此文：《再探CUDA
- Graph：核心机制、多图复用以及Dual AR模型的统一覆盖优化》
- https://github.com/zhaochenyang20/Awesome-ML-SYS-Tutorial/blob/main/torch/cuda-graph/
- readme-2.md
- 大家对这个写作/学习用的agent系统感兴趣的话，可以参考/learn的readme:
- https://github.com/zhaochenyang20/Awesome-ML-SYS-Tutorial/blob/main/.learn/readme.md
- 令我感到无比兴奋的是，LLM极大满足了我从高中开始就很难被满足我的求知欲。至于写作，看上去这的确是一个自
- 由度不比写代码低的领域。
- 3月19日13:39
- 是的，codex看代码的习惯特别好
- 刘思皓: codex这点比较好，我见过最长的codex run
- 改代码之前能看一个小时的代码
- 不想要ralph-loop磨
- 这得模型叠吧
- 刘思皓：我想要：一针见血地、一语中的地、一语道破
- 地、一锤定音地
- 3月19日13:57
- 是loop1问session1，loop2的时候session1把问题传递给session2这样循环下去的吗?
- 刘思皓: humanize的loop是和session id绑定的
- 不是的你看一下humanize里面的state.md
- fol
- 它记录了启动这个循环的claude session id
- 你只要在同一个session 里面 就能自动恢复loop
- 3月19日14:02
- 正好写了一下下午跟导师汇报的内容，感觉ai现阶段只能当超级力工，因为很多需求需要的外部tradeoff太多了
- 刘思皓：我想要：一针见血地、一语中的地、一语道破
- 地、一锤定音地
- se ie e ' dig.
- 因为自然语言是多意的，模糊的，所以即使是未来的SoTALLM，在接收到如
- “相找生成一个functional level的riscy simulator, 支持x 自定义指令
- 这种prompt时，他也只能在所有可运行的结果中返回一个仅仅满足当前promp的可行解。但这些
- 可行解肯定不是都满足开发者需求的。
- 它们会有一些互斥的技术路线/设计指标选择，比加：
- 1. 只需要跑起来，还是需要完全的数值正确性
- 1. 如果需要完全的正确性，是只需要经过unit test，还是需要类d2end的结果一效?
- 2. 它的输入显elf，还显一个直实的trace?
- 3. 遇到llegal instruction时，预期的行为是忽瞎它还基继续?
- 这些问题的选择不论怎么组合，都符合最开始promp的要求，但在真实的开发场景中，我们认为的
- 可行却是这些结果组合中的一个特例。
- 所以vibe coding实际上给aj的应该是一个详细的文档（起码是需求文档，有设计文档更好），这样
- 才不至于反复调试prompt，浪费时间读费token，最后得到的结果也不理想。
- 3月19日14:18
- failure --search
- l soon be removed.
- OME/prompts'. Use the'$skill-creator'skill to cor
- change
- 3月19日23:07
- 气笑了，codex在上下文任务时，会忘记自己的skill
- 看起来像是上下文压缩把skill丢了
- 长上下文
- 3月19日16:40
- codex又在逆天而行了，要把自定义slash command干掉，全转为skill，问题是这两个机制并不相同，不能互相替代啊
- Lurker:气笑了，codex在上下文任务时，会忘记自己
- 的skill
- 3月19日 23:19

---

### 3月20日

#### 原文 L525–L537

[回到原文件 L525](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:525)

- codex 那个quota
- 如果claude opus 4.6给我开2M上下文然后/fast x 3`，我应该会切回去用claude
- codex那个非常耐烧
- 其实话说回来， codex其实有原生的ralph-loop
- 3月20日14:17
- 很简单，就是你一直打"继续"然后Tab
- 它就能一直跑
- 它会自己判断任务有无结束吗
- 刘思皓: 其实话说回来，codex其实有原生的ralph-loop
- 虽然但是，我感觉睡觉编程的SOTA还是humanize
- 我今晚不会白睡觉了
- WANAN-

---

#### 原文 L545–L584

[回到原文件 L545](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:545)

- 它loop干出来的活，claude还从未查出过问题
- codex原生hook的humanize 稳定了嘛
- 稳定了我就全部切过去
- 存包处(maao):
- 今天给claude code接上gpt模型，然后claude code和codex跑humanize，遇到图中问题
- 让claude code自己排查，说是sandbox导致没有权限，可是我已经关掉sandbox了
- 3月20日14:43
- 23:434
- Environment Variables
- HUMANIZE_CODEX_BYPASS_SAND
- BOX
- WARNING: This is a dangerous option that
- disables security protections. Use only if
- you understand the implications.
- Purpose: Controls whether Codex runs
- with sandbox protection
- • Default: Not set (uses --full-auto with
- sandbox protection)
- • Values:
- true or 1: Bypasses Codex
- sandbox and approvals (uses --
- dangerously-bypass-approvals-
- Any other value or unset: Uses safe
- mode with sandbax
- When to use this:
- support (where Codex sandbox fals)
- • Automated Cl/CD pipelines in trusted
- 你试过这个了嘛
- Claude history reviewer
- JW99:
- 老马的xai的4.2有人试过了吗
- with sandbox protection
- and-sandbox)
- 当时grok code刚出来的时候还惊艳了一把
- 那个时候我还在用cursor
- 还没写代码，让他读了一下，还不错。Grok前端不知道是不是在灰度，我现在是每次都是multi agent来回答问题
- 的，一带四
- 两个codex感觉review不出什么问题

---

#### 原文 L615–L705

[回到原文件 L615](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:615)

- 3月20日14:56
- 不看plan就起humanize的行为现在已经被命令禁止了
- 我自己偷懒也被抓住两次
- 你们哪来的那么多任务
- 太夸张了
- 24小时编码？
- 我codex一天120的额度最多用20刀
- 是我根本review不过来codex产生的需求
- 3月20日14:58
- 你还没有掌握spec coding的精髓
- 就是我带着ai产plan的速度远大于ai跟着plan干的速度
- 编译器是写code慢编译成bin快
- spec coding是写spec快，编译成code慢
- humanize现在唯一的目的就是趁我睡觉的时候，给ai一个机会让code赶上我plan的进度
- 3月20日15:04
- 我过去很长一段时间都是边写plan边和干活的ai交互，导致写plan很慢，直到我意识到写plan其实得搞得和下国际象
- 棋那个pre-move—样
- 这里产plan快，是不是你带着ai往前推衍方案，一般还没有产code做验证，plan的深度和可行性会有制约，比较适合
- 铺开开发？
- i     €
- exploring”的原则
- 就是你plan里面要写一个“我“全都要”的实践方案”
- 您认为后面人和ai的关系是什么
- 最后没被选中的方案mask掉就好了
- 我在复现meta那一套操作
- meta有啥操作了
- 我还不知道
- 统一网关,存SKILL,自动化降本增效
- 这个世界太你妈坏了我操
- Meta招了那么多猛人似乎还没什么外部可见感觉
- LLM IS AS GOOD AS YOU ARE
- 开源芯片 agent flow 张宇鑫: 您认为后面人和ai的关系
- 是什么
- 哦哦我旁观视角从国内新闻联想的
- 3月20日15:15
- 3月20日20:13
- 3月20日20:31
- 今天在review codex这一星期写的代码，不review没事，一看不得了，各种"能跑就行"的代码
- 有没有什么好的方式解决
- monorepo，把codex每次写的代码写成一堆即插即用的module，对外暴露的接口由人类控制和维护，其它完全交
- 给ai黑箱处理
- 控制论
- 在性能要求较高的场景咋办
- 你要有良好的观测验证机制
- 3月20日20:36
- ai编写代码时他没发看到整个文件
- 会写出"在同一个地方调用同一个函数多次"这样的sb问题
- 你应该建立更好的测评机制让ai不再犯错
- 而不是自己改代码
- 直接让它读整个文件是吧
- Harness 工程就是控制论
- OpenAI描述了一群不再手写代
- 知乎
- 码的工程师，他们设计环境、构
- 知乎
- 知乎
- 我觉得没法解决根本问题
- 再优秀的管理论都会有漏洞
- 我之前写了篇文章类比机械革命，并列举了芯片变化趋势
- 这篇文章写的更细
- 我在想如何让ai写代码时能看到更广泛的上下文
- 3月20日20:43
- 设指标。干不完就让他一直干直到你睡醒呢
- 每当ai编辑完代码，就拉起另一个agent分析改动地方的上下文，判断改动是否合理
- 我在想用Isp做图谱检索有用吗
- 我们做过
- 效果不好
- a2a目前的模型智力好像不太够
- 我就是想对能力弱的模型用来着....有些模型比较傻，就会读文件把自己上下文塞爆
- 去年拿老师的两张4090d跑弱模型调应用，后面再也不想碰弱模型了
- 开源芯片 agent flow张宇鑫: 去年拿老师的两张
- 4090d跑弱模型调应用，后面再也不想碰弱模型了
- 跑当时的4.5 air量化
- 那确实弱，全尺寸glm4.7给我用的都挺火大
- 3月20日22:07
- 现在codex启动是不是有问题啊?
- 好像说是更新后有bug
- 算了
- bwrap更新一下就好了
- 如果是沙箱问题的话

---

### 3月21日

#### 原文 L789–L842

[回到原文件 L789](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:789)

- 正好看到这一段，不知道实际上效果怎么样
- Lurker: 有没有什么好的方式解决
- https://openai.com/index/harness-engineering/
- already exist in the repository—even uneven or suboptimal ones. Over time, this
- inevitably leads to drift.
- 完全自主的代理也带来了新的问题。Codex会复制代码库中已有的模式——即使这些模式
- 参差不齐或并非最优。随着时间的推移，这不可避免地会导致代玛漂移。
- Initially, humans addressed this manually. Our team used to spend every Friday (20% of
- the week) cleaning up "Al slop." Unsurprisingly, that didn't scale.
- 最初，人类手动处理这个问题。我们的团队过去每周五（占一周时间的20%）都在清理
- “AI垃圾”。不出所料，这种做法无法扩展。
- Instead, we started encoding what we call "golden principles" directly into the
- mechanical rules that keep the codebase legible and consistent for future agent runs.
- For example: (1) we prefer shared utility packages over hand-rolled helpers to keep
- invariants centralized, and (2) we don't probe data "YOLO-style"—we validate
- bpous  ei eee e e t  s t o e  esed
- shapes. On a regular cadence, we have a set of background Codex tasks that scan for
- these can be reviewed in under a minute and automerged.
- 相反，我们开始将所谓的“黄金原则“直接编码到代码库中，并建立了一个定期清理流程。
- 这些原则是带有主观判断的机械性规则，旨在保持代码库的可读性和一致性，以便未来的
- 智能体运行。例如：（1）我们倾向于使用共享的实用工具包，而不是手动编写的辅助函
- 数，以确保不变性集中管理；（2)我们不采用“YOLO风格“随意探测数据——而是验证边
- 界或依赖类型化的SDK，这样智能体就不会意外地基于猜测的结构进行构建。我们定期
- 运行一组后台Codex任务，扫描偏离情况、更新质量评级，并开启有针对性的重构拉取
- 请求。其中大多数任务可以在不到一分钟内完成审查并自动合并。
- 3月21日15:19
- 我周末就在清理ai垃圾呢
- 上午清理到现在
- 我拉起多个agent，让他们只review一个文件
- 3月21日15:43
- AI的铲屎官
- 3月21日16:10
- 我发现改进gen-plan的一个神迹
- 你可以让codex xhigh和claude opus max先独立出一个计划
- 然后让codex xhigh合并
- 然后再开始现在的gen-plan loop
- 避免gen-plan冷启动的问题
- 你说的冷启动是啥
- 3月21日16:16
- 严肃学习
- 这是搓的app?
- 刘思皓:
- https://github.com/SihaoLiu/ai-usage
- 我的奇怪ai脚手架的一角
- 以及
- https://github.com/SihaoLiu/ai-candy
- Zeng haolun: 这是搓的app?
- 3月21日16:20
- 如果你走humanize的gen-plan
- Zeng haolun: 你说的冷启动是啥
- 现在应该是claude先出一个plan，然后codex一起迭代
- 但这样就有点冷启动的问题，后续plan会被初始plan带偏一点点
- 如果你—开始就让两个agent独立做一个plan，再合并，然后再迭代
- 就会好一点

---

### 3月22日

#### 原文 L927–L941

[回到原文件 L927](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:927)

- 3月22日23:17
- 我懂了humanize败在了名字上
- 我觉得是不是得把cancel-rlcr删掉
- claude现在已经会自己调用这个了
- 3月22日23:21
- 即使我prompt各种限制
- 但是我又没法上hook限制
- 因为hook没法区分是用户让claude调用还是claude自己想调用
- 得上intelligent hooks
- hooks需要从rule based进化到intelligent review based
- 我这边还没遇到过cc自己取消的情况但如果碰到次数多的话那是应该取消
- 现在有这个了吗
- 刘思皓: 得上intelligent hooks
- 3月22日23:30
- 没有吧

---

### 3月23日

#### 原文 L949–L1248

[回到原文件 L949](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:949)

- 3月23日11:49
- 我有76%的自信认为agent-teams是个无用设计
- 感觉干活的小兵并不需要沟通
- 直接和老板说的效果是一样的
- 你说的agent team是所有人都讨论吗？
- 刘思皓: 我有76%的自信认为agent-teams是个无用设
- sub-agents和agent teams之争
- 我自信比你还高点，必须sub-agents，没领导不行
- 三省六部制整上
- sub-agents会存在一个bottleneck的问题
- leader的ctx和io会被打爆
- 其实不会
- 如果搞金字塔层级，那会存在不同的叶子agent之间沟通延迟极其大的问题
- 现在我+1的ctx也在被打爆（
- 现实也是的
- 你严格要求sub-agent走文件输出
- 我现在就是描述任务的时候专门加上，哪个任务指派一个强力agent去做
- 我一次性起了一个22个sub-agents干活
- 然后我会去跟codex聊工作量
- 3月23日11:54
- 10000个agent呢，也靠一个leader管么
- 刘思皓: 你严格要求sub-agent走文件输出
- 有利于加深我自己的理解
- 一万个估计不行
- 是的
- 榕: 你说的agent team是所有人都讨论吗?
- 我觉得一个leader最多管15人团队
- agent teams目前没点开a2a的科技树
- 所以信息压缩成agent很重要的点
- 哭也算token!
- 然后每次真实并行最多5个人一起改
- 人多起来了就需要类似moltbook这种论坛或者更高效的方式
- 走worktree开发，就是/batch那个思路
- 是的，我发现他处理速度也跟不上。如果同一时间被很多天消息淹没。他会漏信息，忘记处理
- 张子健: leader的ctx和io会被打爆
- 我感觉我大胆预测一波， swarm team会被砍掉
- /batch会被留下
- evomap他们搞了一个类似rpg游戏的冒险家公会的东西
- 不过真aigc的话估计还是混合的
- 也算是agent team的一个方案
- 我的判断是sub agent完成task会很好，但是explorative的事情就做不来了
- 张子健: evomap他们搞了一个类似rpg游戏的冒险家公
- 会的东西
- 我觉得evomap一直都是炒作
- 哦我对带探索性质的工作的判断一直都是:构建探索工具，而非边探索边构建
- 二月时我把我的虾刷到了evomap第六名
- 因为写代码的代价其实很低，没必要边写边尝试
- 郑权:二月时我把我的虾刷到了evomap第六名
- 直接全部都实现了，然后再挑一个
- 但agent这类东西最终目的还是没有人类
- 3月23日11:59
- 说不定agent team和sub agent都不是最优解呢
- agent的合作方式应该让agent自己探索出来
- loll
- 3月23日12:05
- sub-agent 这些prompt都是在plan里说明的吗
- 刘思皓: 你严格要求sub-agent走文件输出
- 3月23日12:10
- 3月23日12:26
- 是然后sub-agent的回复必须走文件这个直接写在claude.md里面
- 张东宇: sub-agent 这些prompt都是在plan里说明的
- 我觉得agent teams没用这个点我领悟到有点晚，但是想了想似乎生活中就是这样的:
- - 直接和老板说比和同事掰扯有用，把老板的任务干好就行了
- - 与其直接和同事传话，不如说服老板帮我传话
- - 把各种事情的反馈告诉老板，让它统筹，而不是我自己瞎指挥我的同事
- 严肃学习
- 刘思皓: 是然后sub-agent的回复必须走文件这个直接
- 写在claude.md里面
- claude似乎—次性最多并行50个agents
- 感觉那个CCC走agent teams的实验有点把我带偏了
- 任务走subagent需要写到Claude.md里面吗
- 我反正写了
- credit: @刘家昌
- 我现在还是直接prompt指定的，如果我自己忘了就很寄
- 3月23日12:32
- 那子任务的切分是怎么做的，纯靠leader/delegator智能分析当前哪些工作能发出去吗
- 相信你的sub-agents，它们很nb，请切分任务让它们做正确的事情的事情，无论复杂度和时间成本
- 纯leader拆
- 我刚刚一次性起了22个agents,3个小时，纯增量47000行
- 一次性编译正确
- 我觉得还需要指定subagent的模型
- 他有时拿个haiku糊弄我
- 我直接分享我的claude.md吧
- GGG
- 严肃学习
- GGG
- 让我先脱敏一下
- - Sub-agents (Opus model) can be great for implementation, the work you may feel complicated but
- please trust your sub-agents. Guide them to do the complex and right things.
- 就这一句
- 我现在都不跟教研室的讨论这些，准备自己先爽，如果让老板知道了，自己的工作量肯定会变大
- 那你想多了
- 等四个月它们肯定知道
- 3月23日12:35
- 所以能爽一段时间是一段时间
- CLAUDE.md是唯——个我纯手写的地方
- 绝对禁止AI自动生成CLAUDE.md
- 哈哈哈哈
- 奇迹的闪光迪迦:我现在都不跟教研室的讨论这些，准
- 备自己先爽，如果让老板知道了，自己的工作量肯定...
- 我发现我居然把这个放在项目CLAUDE.md里面了
- 我升级成user level
- 刘思皓: - Sub-agents (Opus model) can be great
- for implementation, the work you may feel com...
- 今天干的活是我第一次起超过15个agents，3个小时一次性干进去46000+行代码，然后能正常工作的run
- 我之前那个8000刀悬赏终止
- 让我付出了一个巨大的血泪教训
- 而且费钱
- 我也是真的信了人类学那个CCC的迷魂汤
- 3月23日12:41
- 我怀疑它背后实质上是个/batch
- 根本不是个agent teams
- 我觉得agent teams是个误区，干活的小兵就不该互相沟通
- leader可以互相沟通
- 我想不出让agents直接沟通在方法论上有什么优势
- 我只觉得会造成管理混乱：一个leader不可见的沟通，应该是需要被禁止的
- 几家对于teams的理解有一些不一样
- 合理
- 人类学的 teams 是想让 agent work as company所以大家需要尽可能的 transparent
- 但是人类学的agent teams沟通，小兵可以直接的沟通，leader不可见
- L.Zhu: 人类学的 teams 是想让 agent work as
- company所以大家需要尽可能的 transparent
- 这个我想不明白啊
- 欧美厂和老中厂的 style 区别...
- 欧美更偏好扁平化
- 老中厂偏爱 hierarchy
- 这个绝对要造成管理混乱，如果退一步，小兵必须经过老板才能沟通，那和sub-agents有什么区别
- 3月23日12:45
- 同意..现在沟通大多是在白白浪费上下文
- 刘思皓: 我觉得agent teams是个误区，干活的小兵就不
- 该互相沟通
- leader可以控制所有小兵
- correct me ifi am wrong:我理解的swarm team mode和sub-agents的唯—区别就是swarm team mode的小兵
- 可以直接沟通
- 这看上去是合理的，也符合某种"工作常识"
- 真实hierarchy会多很多中间层，这些层是效率低下的关键
- +1 我也是这么理解的
- 刘思皓: correct me if i am wrong: 我理解的swarm
- team mode和sub-agents的唯一区别就是swarm te...
- 我算是理解为什么swarm team到现在还是一个optional的experimental feature,需要环境变量打开才能启动
- 而/batch已经是built in了
- 人类学会把一切有效的东西快速Builtin，我现在深信不疑
- 第一步先做成 skills，大家都喜欢用的弄成 built-in
- 下一步就是加入 post-train 训成 prior
- 3月23日12:51
- 但是现在我手上有一个实在的例子，用的是/batch，规模更大，效果更好
- 所以我感觉那个agent teams真的很不对劲
- 下一步就是加入post-train 训成prior
- 特别好的进入mid-train 进行 generalize
- 我现在对"agent team是个糟糕的feature， use /batch not agents teams"大概有77%的自信度，等群友—个反例
- 3月23日12:51
- 虽然我自己也有一个反例就是了...我的"cmakel|bazel for gem5"是用humanize + agent teams做的
- 但是现在我手上有一个实在的例子，用的是/batch，规模更大，效果更好
- 所以我感觉那个agent teams真的很不对劲
- 例证就是我起agent teams的时候，需要经常介入
- good observation
- 我倒要看看
- 但是/batch会直接worktree全部隔离掉
- 人类社会也是这样
- 然后主agent的任务其实只是合并pr
- 最近实验 auto-research 的时候，的确我的用法也更多是 batch 而不是 teams
- 稍微修修bug
- 那看来我们对上了
- 稍微修修bug
- 那看来我们对上了
- 3月23日12:52
- 我妄语—下， agent -teams要砍
- 我先把Humanize的agent-team砍了
- 如果没有什么正面例子,我就砍了
- 换成batch mode
- 我觉得team有一个悖论：如果你能拿到完整的代码库，那么你为什么要去问同事而不是自己读代码？
- 我用 Agent QQ 只在跨代码库的时候
- 如果你不知道哪块代码在干什么，那你凭什么知道哪个同事知道相关信息
- NV周耀阳: 我觉得 team 有一个悖论：如果你能拿到
- 完整的代码库，那么你为什么要去问同事而不是自己...
- 那这样看可以通过sub-agent来让cc调用其它cli作为worker
- 刘思皓: 换成batch mode
- 1. 直楼在主对话中调用
- 抗直接在热程上下文中向Codex 提问。
- 你想试试让民造过 s-agot 向Cades 问—个类体问题吗：
- 3月23日12:58
- Trtllm vs. simulator
- 1. 直接在主对话中调用
- 抗直接在当程上下文中向 Codex 提问。
- 让它在后台课用ak
- 一边言修改代再
- 你想试试让我通过 sh-agprt 向Cades 月一个类件问题号：
- 3月23日12:58
- 刘思皓:我直接分享我的claude.md吧
- 然后这样cc就能实现builder agent跟启动器agent的分离了(并且对现在的代码改动范围比较小)
- 确实
- 我现在觉得应该是 harness {/batch {build-review}}
- 虽然第一眼那个/batch with worktree的设计让我脑壳痛，而且听上去没有agent teams那么性感
- 但是现在我是真香了
- 我大概分享一下我这次的实践经历：大概是花了一下午2-3小时，ai驱动下做了一个masterplan和21个小plan，每个
- 小plan差不多负责1000-3000行的代码增量任务。整个工程的更大的背景是，前面先花一周时间，不开任何
- humanize，纯交互式地快速搭建一个从0-1的mvp(大概8万行)。有了这些准备之后，确保你的任务本质上和那个
- mvp是一样的但是不是0-1，是1-100。然后直接/batch让它全部做完，结果我启动的时候甚至没有显式调用batch，
- 它自己开始用batch干活，然后3.5小时干进去4.7万行代码，我问了几个关键点它全做对了
- 3月23日13:11
- 情况大概就是这么个情况，我也很震撼
- 另外就是那22个plan我是会看的，其实我看完基本就知道它能做完
- master plan只描述并行度和依赖
- 别的就没了，大道至简：先纯手搭(古法spec coding)，完成mvp，然后一波scale up，scale的时候走/batch
- 3月23日13:20
- 很有道理
- NV周耀阳: 我觉得 team 有一个悖论：如果你能拿到
- 完整的代码库，那么你为什么要去问同事而不是自己...
- 我再大胆假设一下，A2A要成为下一个MCP
- 3月23日13:25
- 难的其实并非如何让任意两个agent沟通，难的其实是如何让两个agent禁止沟通
- 3月23日13:35
- “干活的小兵禁止沟通”和“plan禁止写code”一样，我要纳入spec coding十诫(x十一诫
- 3月23日13:37
- 另外这个case我没给小兵上codexreview，但是我让leader每次有疑难杂症或者每干完一个plan，就让codez看一次
- 刘思皓：我大概分享一下我这次的实践经历：大概是花
- 了一下午2-3小时，ai驱动下做了一个master plan和...
- 3月23日14:26
- 3月23日14:33
- 3月23日14:48
- @Sequencer?
- 大佬们好
- 刘思皓: @Sequencer?
- 3月23日15:09
- 有必要
- 刘思皓：“干活的小兵禁止沟通”和“plan禁止写
- code”—样，我要纳入spec coding十诫(x十—诫
- code”—样，我要纳入spec coding十诫(x十—诫
- 3月23日15:21
- 这个不应该靠prompt，而应该直接剥夺agent的tool
- 刘思皓:“干活的小兵禁止沟通”和“plan禁止写
- code”—样，我要纳入spec coding十诫(x十—诫
- planner不给写代码的tool，小兵不给互相碎嘴的tool
- 3月23日15:35
- 确实
- 张子健: planner不给写代码的tool，小兵不给互相碎嘴
- 的tool
- 不沟通的agent不就是Sub-agent mode
- 张子健: 这个不应该肯nromnt，而应该克接剥态agont
- Plan mode本来就没有写代码的tool，我是说不能在plan文件里面写大段的代码这种行为要禁止
- 张子健: planner不给写代码的tool，小兵不给互相碎嘴
- 的tool
- 不在claude.md禁止，claude很喜欢（至少之前，现在不知道咋样了）在plan里面写详细的代码片段
- 我觉得跟用户的主聊天agent不应该调用任何工具
- 只准指派subagent干活
- 这个是经典痛点
- 刘思皓: Plan mode本来就没有写代码的tool，我是说
- 不能在plan文件里面写大段的代码这种行为要禁止
- 而是“保持对技术实现细节的中立”
- “将细节决定权留给实现的时候”
- 3月23日15:42
- 这个纯粹是模型能力问题
- 刘思皓: Plan mode本来就没有写代码的tool，我是说
- 不能在plan文件里面写大段的代码这种行为要禁止
- 迭代一下就好了
- 写nromnt的话终究是短期workaround
- 你这个就很模糊，我感觉你这么说它还是会在plan里面写
- 王邦彦：而是“保持对技术实现细节的中立”
- 我就学Boris直接一波完全禁止它在plan里面写任何code
- 虽然这么说，但是它还是会在plan里面写code，只不过都是那种不得不写的场景
- 最后就实现了你这个效果
- 王邦彦：“将细节决定权留给实现的时候”
- 3月23日22:21
- 我发现现在cc写计划会自动quiz很多东西了
- 3月23日22:48
- 好像是superpowers更新的功能，跟群友不谋而合了
- huí
- 3月23日23:08
- 就是确定很多spec细节+quiz+review
- 刘思皓: 你是说gen-plan吗还是原生的
- 3月23日23:15
- 有吗？我有点忘了
- 泽文: humanize现在一次只能启动一个loop，是有什
- 么考量吗
- 刘诗楠:好像是superpowers更新的功能，跟群友不谋
- 而合了

---

### 3月24日

#### 原文 L1249–L1305

[回到原文件 L1249](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1249)

- 3月24日00:53
- 我觉得我把这玩意搞出来了，我现在可以稳定复现：一次性起10个以上的agents，每小时稳定输出1万行可用代码，不打架
- 体感上比我当时造和用humanize的生产力还要大5-10倍
- 核心点就是：predefined harnessed orchestration flow with batched sub-agents that cannot talk
- 那个可对话的蜂群模式可把我害惨了
- 而且这个flow有个最神奇的地方
- 刘思皓: 核心点就是: predefined harnessed
- orchestration flow with batched sub-agents that...
- 3月24日00:58
- 我写了近6万行代码，没有发生一次上下文压缩
- 3月24日03:22
- 支持大佬让革命更彻底
- 我思考一下怎么放进humanize里面
- 那个可对话的蜂群模式可把我害惨了
- 我写了近6万行代码，没有发生一次上下文压缩
- 3月24日03:22
- 第一，审视 agents 之间是否存在直接通信。如果你的并行模式下，Cookbook Domain Expert 和 Quantization
- Domain Expert 各自独立完成子任务后只向 Manager 汇报，Manager 做综合——这是安全的sub-agent 模式。
- 但如果串行模式下，agent A的输出直接喂给 agent B作为输入而不经过Manager的显式编排，这就是讨论中说的
- "leader不可见的沟通"，应该避免。即使是串行依赖，也应该让Manager充当中间人，显式地把上游输出整理后作
- 为下游输入。
- 第二，"Debating"机制需要重新定义。讨论中的一个核心洞察是："如果你能拿到完整的代码库，那你为什么要去问
- 同事而不是自己读代码？"对 how-to-sglang 来说，每个 domain expert 已经有自己的领域知识了，它没有理由
- 去"问"另一个expert。真正的综合判断应该由Manager完成。建议把"debating"重新定义为Manager层面的多
- 源信息综合推理，而不是agents之间的对话。
- 第三，通过工具权限而非 prompt来实施隔离。讨论中有人明确说："这个不应该靠 prompt，而应该直接剥夺
- agent 的 tool。"在你的架构中，domain expert agents 应该只有读取自己领域 markdown 和查询相关代码的工
- 具，不应该有调用其他 agent或写入其他 agent工作空间的能力。
- 学习了下群友的讨论
- 3月24日04:12
- All good, 第三点要加一个, worktree隔离
- 我觉得我现在手上的多Agentsflow的自动化程度已经接近L3.7~L3.9了
- 我考虑一下要不要以及如何port到humanize里面
- 感觉loop似乎也没有那么重要了，更多地是分治和并行，以及调度和协调
- 3月24日04:20
- 给每一个小兵插reviewloop是不合适的，会立刻陷入不属于这个阶段的fine-tune和细枝末节
- 但是顶层插reviewloop也不是很对，审查尺寸太大会导致: 1. 问题太多;2. 审查本身也会有遗漏
- 插humanize的地方需要合适且动态地调整
- 3月24日06:03
- 成nort
- 有没有一种脚本，能够在 python script 里面调用 claude code 呢
- 比如 os.system(f"claude {input}")
- 这种?
- 3月24日06:09
- 我测，还真的有
- 3月24日06:27
- 为啥要这样
- https://code.claude.com/docs/en/overview#what-you-can-do
- 3月24日06:28

---

#### 原文 L1324–L1350

[回到原文件 L1324](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1324)

- 或者channels之类的东西
- https://github.com/anthropics/claude-agent-sdk-python
- 这里调用的貌似是 claude 的 API，不是 claude code?
- 就是想用api调claude agent?
- 用 Python 调用 claude code
- os.system(f"claude /how-to-sglang {input}")
- 我觉得 superpowers的 brainstorm 非常牛逼，我现在脑子给 meta delegator，然后 meta 给 superpowers 不太
- 屎的屎，然后 superpowers 问我巨量的问题成一个非常干净具体的 task spec，再丢给 humanize 执行
- 我就是差不多的workflow
- 刘家昌: 我觉得 superpowers的 brainstorm 非常牛
- 逼，我现在脑子给 meta delegator，然后 meta 给 s...
- 真的巨爽
- 3月24日08:21
- 现在各种meta skill譬如omo、superpowers、tdd之类的，哪个可以比较无脑直接用啊
- 刘家昌: 我觉得 superpowers的 brainstorm 非常牛
- 逼，我现在脑子给 meta delegator，然后 meta 给 s..
- 不知道呢我只用了 superpowers 十分爽，是真的能把一坨屎变成干净的 spec 和 plan
- 3月24日 08:27
- 学习
- 刘家昌: 不知道呢我只用了 superpowers 十分爽，是
- 真的能把一坨屎变成干净的 spec 和 plan
- 3月24日08:33
- 那让delegator决定哪些任务是selfcontained，然后去调用reviewer呢？但这样肯定会经常被delegator提前结束
- 刘思皓: 给每一个小兵插review loop是不合适的，会立
- 刻陷入不属于这个阶段的fine-tune和细枝末节但是...
- 3月24日08:47

---

#### 原文 L1354–L1371

[回到原文件 L1354](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1354)

- 3月24日 08:53
- 大佬用brainstorm是直接using-superpowers还是直接brainstorm skill呢
- 刘家昌: 不知道呢我只用了 superpowers 十分爽，是
- 真的能把一坨屎变成干净的 spec 和 plan
- 3月24日09:03
- 大家好，我在NV research工作。想问问，有没有人用公司内部资料喂给humanize干活的经验?
- glean?
- 晏子:大家好，我在NV research工作。想问问，有没
- 有人用公司内部资料喂给humanize干活的经验?
- 设置glean的mcp?
- 我想搞个sass的scheduler，这个得上内部资料啊
- 3月24日 09:08
- 用来搞binary instrumentation
- 一段sass里，直接插sass代码。让scheduler重新写opex
- 我大概知道内部有哪些资料和代码可以用，但是怎么让humanize用上呢？
- Harness 才是一切：Cursor、Claude Code和Perplexity 真正构建了什么- Leezgion的文章-知乎
- https://zhuanlan.zhihu.com/p/2019498581896218079
- documentsass

---

#### 原文 L1389–L1416

[回到原文件 L1389](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1389)

- 晏子: 看样子需要在plan里写清楚mcp的用法
- 如果是我，我会让他在写 plan的时候就用 mcp 把 glean 上面的东西搜清楚
- 然后 builder就按照 plan里面的 background 和计划执行就行了
- 那sass instruction的latency信息也直接写到plan里?
- NV周耀阳: 如果是我，我会让他在写 plan 的时候就用
- mcp 把 glean 上面的东西搜清楚
- 这些算background信息?
- 如果塞得下的话，或者写plan的时候额外整理一个文档
- 3月24日09:30
- 晏子: 这些算background信息?
- 上下文太长了
- 额外整理一个文档，让 builder 有需要就去 grep
- 应该要额外整理的，需要什么去拿什么
- 怎么拿可以帮忙设计好，有时候grep很蠢
- 了解了
- 是的，最好有skill
- 我是贴上 meta 给的任务，然后：The draft is very preliminary and may not fully represent what I expected.
- Please use superpowers skill to brainstorm and ask me A LOT OF questions.
- 张子健: 大佬用brainstorm是直接using-superpowers
- 还是直接brainstorm skill呢
- 了解了，比如需要sass的latency信息，就用某个skill获取
- 段震伟:是的，最好有skill
- 先写个sass相关的skill吧
- very preliminary and may not fully represent wh...
- superpowers大家装的中文版还是英文版呀
- woc 非常好用
- 刘家昌:我是贴上 meta给的任务，然后：The draft is

---

#### 原文 L1520–L1610

[回到原文件 L1520](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1520)

- 离谱
- 公司还叫我们少用掉
- 用点
- 我看了一下我每个月的token用量，换成API的费用也就是一万刀多一点
- 刘思皓:
- 我们公司不发token
- 不如开除一半，其他人按token算绩效
- 你们有个主管虾玩的挺溜的
- 郑权: 我们公司不发token
- cursor要开吧?
- 郑权: 我们公司不发token
- 啥时候广泛推进
- 段震伟:不如开除一半，其他人按token算绩效
- 说的不会是我leader吧
- 开源芯片 agent flow张宇鑫:你们有个主管虾玩的挺
- 溜的
- 虾有啥好玩的，真不明白
- METAX:
- Agents for GPU Design and
- GPU designed for Agents
- 奉先石
- 沐耀集成电路（上海）股份有限公司
- 3月24日13:44
- openclaw代码非常烂
- 出去吹牛逼
- 美美与共: cursor要开吧?
- 你在哪家公司
- 刘思皓: 我看了一下我每个月的token用量，换成API的
- 费用也就是一万刀多一点
- 我烧订阅啊
- api哪里烧得起
- 我买反代
- 我现在就两组200+200
- 啥都不给用？
- 郑权:没有的
- 对的
- 美美与共: 啥都不给用?
- 一个月800刀的意思？
- 刘思皓:我现在就两组200+200
- 这也是我做中转站的原因
- 本来是给自己用的
- 这种有啥限制么
- 后来用不完才拿出来卖
- 膜拜
- 郑权： 这也是我做中转站的原因
- 会有很多人
- 因为你的存
- 在而生活的
- 更美好！
- 郑权：后来用不完才拿出来卖
- 我单位的token我都包了
- 让他好好学学
- 竞争对手都在用（
- yep
- hazelnut: 一个月800 刀的意思?
- 他前段时间还一直吹openclaw呢
- 你们cto在干啥，不是在cutedsl群里吗
- 他前段时间还一直吹openclaw呢
- 智谱黄睿博: 你们cto在干啥，不是在cutedsl群里吗
- 我问他用什么模型，结果他部署都没部署
- 我也觉得啊
- 郑权: openclaw代码非常烂
- 都是叶公好龙
- 搞不懂这玩意到底有啥用
- 3月24日13:48
- 除了让我睡眠不好
- 员工日报每天发他虾后台
- 刘思皓: 搞不懂这玩意到底有啥用
- humanize让我生活变好了
- 我记得之前国内一个国防科大的硬件老兵几年前要搞什么DPU后来就开始做卖token了
- 除了一开始用的时候
- 会有很多人
- 因为你的存
- 在而生活的
- 更美好！
- 刘思皓: humanize让我生活变好了
- 为了搞一个好plan会熬夜
- 现在熟练了起完humanize看十分钟我就放心睡觉了
- 今天我用superpowers帮我refine plan，问了我五十个问题了还没问完
- 等问完了，再交给humanize执行，将是多么美妙的工作流
- yep
- agent teams 辣鸡feature
- 3月24日13:58
- 上下文够吗
- 五十个问题了还没问完
- 3月24日14:43

---

### 3月25日

#### 原文 L1729–L1739

[回到原文件 L1729](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1729)

- 反而把个人电脑卖爆了
- 我现在在用super power开发一个监控agents的前端网页主要是想自动构建任务树
- windows呢，微软救一下你那垃圾系统
- 奇迹的闪光迪迦: 反而把个人电脑卖爆了
- 基本还是最好的个人使用硬件
- 奇迹的闪光迪迦: 反而把个人电脑卖爆了
- 还能自动更新agent的状态，然后更新任务树
- 张东宇: 我现在在用super power开发一个监控agents
- 的前端网页主要是想自动构建任务树
- 可以期待一波我的开源版 slock.ai
- 3月25日18:08

---

#### 原文 L1755–L1767

[回到原文件 L1755](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1755)

- 但是卡得要死还一堆bug
- 不然人脑上下文切换成本太大
- 张东宇:我主要是想要任务树/提醒系统
- 可能是对比度太高，稍微淡一点应该还行
- 愚鱼: 看久了难受
- 朋友们有没有清理agent垃圾比较好的方案啊
- 让另一个agent清理agent垃圾
- 你说的是一个project下的session吗
- 刘诗楠:朋友们有没有清理agent垃圾比较好的方案啊
- 我的现在是这样的
- 愚鱼：可能是对比度太高，稍微淡一点应该还行

---

### 3月26日

#### 原文 L1869–L1880

[回到原文件 L1869](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:1869)

- 睡前又起了两个，美美睡去
- superpowers大大加速了我写/审spec的速度
- 3月26日01:25
- 做好人不留名
- 3月26日01:25
- 我最近太忙了，PR没时间看
- 等闲下来再看看吧
- 主要是humanize现在也不是我自己方法论的SOTA了
- 我有个新的nb flow, 主要是/batch + loop的
- 到时候打磨完， port到humanize，然后再考虑挂一个arXiv
- 但是junior student怎么办
- 刘诗楠: rlcr太造福我的科研了

---

#### 原文 L2046–L2062

[回到原文件 L2046](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:2046)

- 3月26日09:24
- 现在好用的开源模型基本上都是国产的，然后国内很多都还在用 Hopper 这一代的卡做 serving，Blackwell 走私没上量
- 我现在都有点不想宣传humanize了
- 这能说吗
- NV周耀阳: 现在好用的开源模型基本上都是国产的，
- 然后国内很多都还在用 Hopper 这一代的卡做 servin...
- 感觉好些老外方法学古老的很
- 好用的flow群友一起爽
- 得让Claude和OpenAI给你钱
- 刘思皓: 我现在都有点不想宣传humanize了
- 我们一起帮他用了多少token
- 因为这个原因，现在开源模型的官方API定价目前基本仍然以Hopper的成本为锚
- NV周耀阳:现在好用的开源模型基本上都是国产的，
- 然后国内很多都还在用 Hopper 这一代的卡做 servin...
- 很古老...现在大部分人都还没有把 coding agent 的轮子转起来
- 刘思皓: 感觉好些老外方法学古老的很
- 而 claude 和 gpt 基本上都切 Blackwell 了

---

#### 原文 L2110–L2127

[回到原文件 L2110](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:2110)

- 直接把参数暴露给 claude，让他用 autoresearch 帮我自动去刷 sota
- auto research本身和plan给—个比较vague的research plan的humanize有啥区别吗?
- 3月26日09:33
- 我其实也是
- 刘诗楠: 我现在相当于在用humanize做auto research
- 128 卡 + 4 个 agent，已经从之前低三个点，现在高 sota 1.1% 了
- 本来算力和带宽只是 2-3x，但是 nvfp4 和 NVL72 导致在某些 token/s 的区间相较于 hopper 有超线性的提升，导
- 致这些区间 Hopper的成本被 Blackwell暴打
- NV 周耀阳: nvfp4, 8TB 带宽，NVL72, 以及 GB300/
- B300的 2x MUFU
- autoresearch和humanize本质有啥区别嘛
- L.Zhu:128卡 + 4个 agent，已经从之前低三个点，
- 现在高 sota 1.1%了
- 刘思皓: auto research本身和plan给一个比较vague的
- research plan的humanize有啥区别吗?
- humanize 是一个更通用的 flow
- 只是 karpathy 更懂 pr赚了宣传的优势
- 3月26日10:00

---

#### 原文 L2377–L2393

[回到原文件 L2377](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:2377)

- 3月26日12:15
- humanize
- ricr/2026-03-26_03-57-32
- goal-tracker.md
- round-0-prompt.md
- rund-0-summary.md
- state.md
- pending-session-id
- humanize是这么用的吗
- codex指挥我写了一堆东西
- 看起来正常
- 不过，什么叫做“codex指挥【你】写了一堆东西”？
- 打死裤子: codex指挥我写了一堆东西
- 3月26日12:16
- 因为我第一次使用humanize
- 你截图上的东西不至于是自己写的吧？

---

#### 原文 L2440–L2632

[回到原文件 L2440](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:2440)

- 郑权:裤子还在古法vibecoding
- codex hooks刚搞好
- 我打算沉淀一下
- 最近砍柴太沉迷，真的一点时间都没有去磨刀
- 我在高强度用纯codex humanize，遇到问题等review时经常停下来不动了
- 智谱黄睿博: 怪不得mega kernel失败了
- 不能和nv比啊
- 其实非古法的vibe就是多了一层控制，让Al自动搜索解法，自动验证，自动review，循环起来
- 我也是
- 郑权:我在高强度用纯codex humanize，遇到问题等
- review时经常停下来不动了
- 3月26日12:35
- humanize 项目的 ci 怎么写大家有头绪吗
- 直接跑agent bench 吗
- 整个agent_test
- Mineral: humanize 项目的 ci 怎么写大家有头绪吗
- 除了固定的正例反例测试外，可以让ai写一些“偏难怪”的边缘测试
- 3月26日12:44
- Mineral: humanize 项目的 ci 怎么写大家有头绪吗
- https://github.com/humania-org/humanize/pull/42
- 但是我做了一个这个
- 3月26日12:44
- "[]你是否愿意参与改进Humanize"
- 也就是不要给humanize上Cl
- 群友就是Cl
- 3月26日12:59
- https://www.anthropic.com/engineering/harness-design-long-running-apps
- ?？?
- 昨天刚刚发布
- 原来是给humanize上ci啊，我以为是给humanize写的项目上ci
- 这是我读过的人类学收获最少的文章
- 刘思皓: https://www.anthropic.com/engineering/
- harness-design-long-running-apps
- 有点难，Al agent flow我觉得本质上是没法unit test的。
- 你的unit 基本上都得是一个有点规模的repo施工断面
- humanize写的项目上ci
- 我们之前一直聊的都是怎么给humanize本身上ci
- Lurker: 原来是给humanize上ci啊，我以为是给
- humanize写的项目上ci
- 这文章我居然没有收获一点东西
- 刘思皓: https://www.anthropic.com/engineering/
- harness-design-long-running-apps
- 被humanize完爆
- 刘思皓: https://www.anthropic.com/engineering/
- harness-design-long-running-apps
- 以前人类学的博客文章我都觉得获益匪浅
- 这文章说的是个啥
- PDBR
- 3月26日13:05
- 应该给humanize发论文
- 它最长的run才跑了6小时
- 群友哪一个睡觉编程不比这个久
- 知止发会文
- 3月26日13:11
- 发个arXiv也不是不行，vibe一部分，手写一部分
- 三省六部适合发论文
- 比较新颖
- humanize这种简单有效的东西
- 审稿人：claude build， codex review
- 毫无创新
- reject
- less is more
- 太朴素了
- 三省六部有群友用过吗
- 我看readme就已经让我头大了
- 还是humanize更适合我这种宝宝体质
- 太真实了
- 刘思皓: 三省六部适合发论文
- 我觉得至少可以写个blog
- 刘思皓: 审稿人:claude build， codex review
- 像skylab—样
- 他们现在最新的东西都是搞个notion page
- 3月26日13:17
- blog先行，paper写完再挂出来
- 确实，大道至简
- 3月26日13:30
- 当ASPLOS被重命名为 Agentic Support
- for PL and OS。那时，vibe coding的春
- 风将吹过这古老的荒野。架构师们将不
- 再刀耕火种，而是举起双手，向他们自
- 己创造的神的API许愿，说:“要有算
- 力”，算力就有了。
- 看到朋友圈大佬发的
- 我突然意识到—件事，我手上这个loop humanize with /batch的新flow
- 可能只需要改几个文件就能更新到humanize里面
- 3月26日13:35
- 我明天就去更新一下
- 记得照顾上纯codex
- 3月26日13:44
- 那可能只能周老师帮忙一下了
- 其实很简单我才意识到
- 把agent-teams改成superpowers的sub-agents based
- 刘思皓: 我突然意识到一件事，我手上这个loop
- humanize with /batch的新flow
- 外层套一个r
- 就好了
- 主支线分离考虑做进去吗
- 3月26日14:02
- 要合一起合了吧
- 3月26日14:11
- 3月26日19:04
- 3月26日20:42
- 目前的疼点是用codex跑数小时的实验，可能会出现几十分钟状态都不变需要agent静等的情况。在这种情况下，直
- 接用codex跑它经常自己停下来
- codex自带/review功能啊
- 还挺好用，挺全面
- 你找下我有个基于hook的pr，还没合并
- 张子健: 请教下有没有codex自己干活自己review的方
- 当时 main branch 能用，release 不能用，我还没测试现在的 release 是否能用
- 3月26日20:52
- subagent
- I need you to run a reviewer-first autonomous multi-agent refactor loop for XXX
- Use exactly these agents:
- - reviewer — read-only review lead and exit gate
- - programmer — the only agent that edits code or tracked docs
- - `test_runner — build, validation, and profiling runner
- After tests finish, the reviewer re-checks the diff and decides:
- - `APPROVE BATCH
- - `BLOCK - FOLLOW-UP REQUIRED
- Approval requires:
- - reviewer comments addressed or explicitly rejected with a valid reason
- - file dispositions updated
- - line count did not grow without justification
- - validations required for the batch are green
- If blocked:
- - reviewer issues a new numbered review for the same batch
- - move to the next unfinished batch
- ## Exit Conditions
- Do not stop until either:
- 1. The reviewer declares that all success criteria are met, or
- 2. The reviewer identifies a real blocker that prevents safe cleanup and records it as blocked-with-reason`.
- If two consecutive cycles only produce cosmetic churn or no line-count reduction:
- - shrink the batch size and target a specific deletion cluster next
- - do not continue broad low-signal cleanup
- ## Reporting Format Per Cycle
- Append toplan/refactor/refactor-attempts.md`:
- ### Cycle N: [Batch / focus]
- - Reviewer batch: [name]
- - Files reviewed: [list]
- - Main deletions/simplifications: [list]
- - Line count delta: [before -> after]
- - Validation run: [commands]
- - Reviewer verdict: APPROVE / BLOCK
- - Remaining concerns: [list]
- Start now. Keep looping until the reviewer signs off on the success criteria.
- 还要在.codex定义这些人
- agents
- mathematician.t...
- programmer.t... 9
- researcher_b...
- researcher_m...
- researcher_n...
- researcher_P...
- reviewer.toml
- 我这么搞了以后codex自己跑了3个小时refactor整个代码库
- 然后他还能开始写更多的agent loop
- role based的workflow似乎不是best practice
- anthropic讲context based的效果更好
- 求个文章学习一下
- 刘诗楠: anthropic讲context based的效果更好
- 3月26日 20:58
- 主要是我以前codex老是跑一段停下来让我人肉继续
- 我刚在claude code和codex轮番上阵下，最后由claude code解决了一个藏得很深的bug
- 3月26日21:10
- https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them
- 杨硕:求个文章学习一下
- role based的workflow很多token都浪费在了syncing up上，做context transfer
- 听起来是codex没有hook的问题，我也经常遇到，以前5.3-codex还好，现在跑5.4就经常中间断了
- 杨硕:主要是我以前codex老是跑一段停下来让我人肉
- 继续
- 3月26日21:20
- 可能是5.3-codex比较快，所以启动器agent还能耐下心来等
- 每天就是想点子，丢给humanize
- 不用挂vpn开发了
- 然后到点了下班
- 3月26日22:00
- 生产力还比那些没有用humanize的人高
- 我觉得humanize对于那种公司安全网布置的很好的人
- 简直是下班福音
- 老板开心，自己开心，家人开心

---

### 3月27日

#### 原文 L2689–L2703

[回到原文件 L2689](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:2689)

- 从Ilm 原理开始讲
- https://github.com/humania-org/humanize/pull/47
- @刘思皓 @Blowing 我刚刚在最新的 release上测试，hook 已经可以用了，可以合并了
- v0.116.0上面多次 block没有问题
- 会有很多人
- 3月27日00:42
- 3月27日00:50
- 额，我自己的 test cast 没过。。。
- 提示词里加，必须跑通所有测试
- 3月27日01:01
- 我这两天在搞学校的预答辩感觉这样的feature自己用两天没什么问题的话应该就能直接合
- NV周耀阳: https://github.com/humania-org/
- humanize/pull/47 @刘思皓@Blowing我刚刚在...
- 3月27日01:48

---

### 3月28日

#### 原文 L2862–L2880

[回到原文件 L2862](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:2862)

- 刘思皓: 不要share啊
- 我最近还在靠humanize碾压老外
- 他评价cc的loop，他明显吃过更好的
- 他说humanize是cc的/loop吗
- 就是claude的循环功能
- 那就合理了
- 说明他没有理解humanize的核心
- humanize的核心—直都是拿codex review
- loop是个微不足道的功能
- 那就好
- 如果loop的时候不换模型其实是没有什么效果的
- 没事的我不share就找比我牛逼的让他指点指点
- 3月28日02:31
- 包括codex build + codex review, 我感觉到最后也查不出什么问题
- 所以我一直不太确定群里可能有一半的人用的那个codex + codex的humanize
- 那个我其实之前手动驱动过
- 3月28日02:34

---

#### 原文 L2991–L3001

[回到原文件 L2991](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:2991)

- ssh的config前面加个这个试试
- codex有没有什么办法同时开和关superpowers的所有skill呢
- 刘思皓: 没有，肯定是superpowers brainstorming +
- ask me alot of question
- 不知道这个可能得问群里高频codex用户
- 我所有时间里面只有20%会拿codex高强度build
- 不知大佬怎么处理agent在运行长期实验时，加上superpowers后会overthinking的情况
- 3月28日08:51
- 有一些不需要动脑但是需要一直盯着的任务，superpowers会让模型每看一次都要brainstorm我
- 17548
- kk claude的pipe模式支不支持人类/btw

---

#### 原文 L3010–L3019

[回到原文件 L3010](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3010)

- 然后codex每各几分钟去tail那个log
- 就我现在的flow是主session不跑任何东西只用来驱动sub-agents
- 然后主session外面会套一个humanize
- 但是humanize会阻止主session停下
- codex的TUI模式有个不知道是bug还是特性，如果让它每隔几分钟重复做同样的事情，它会在重复几次后留下一个
- backround terminal，跟我说他在狠狠干，但实际上停下来等我输入
- 所以你给主session的任务里面就是：你负责监督和调度，但是给自己起一个不能放后台的睡眠任务，每5分钟起来看
- 一下你的sub-agents干好没
- 5.4是这样，5.3 codex不这样
- 原来不只是我遇到这个问题

---

#### 原文 L3025–L3038

[回到原文件 L3025](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3025)

- 刘思皓: 所以你给主session的任务里面就是：你负责监
- 督和调度，但是给自己起一个不能放后台的睡眠任务...
- codex cli应该出—个/unattend
- 我其实没试过codex的sub-agents模式
- 3月28日09:01
- 输入之后就阻止模型向人类问问题
- 不确定能不能这么搞
- 刘思皓: 所以你给主session的任务里面就是：你负责监
- 督和调度，但是给自己起一个不能放后台的睡眠任务...
- @刘诗楠我不是很确定，但我感觉我换到5.4之后codex很少起subagent了
- 刘思皓: 我其实没试过codex的sub-agents模式
- claude里面是可以的，一方面可以让主session停下等待sub-agents干完活
- 大佬有没有这种体验
- 3月28日10:21

---

#### 原文 L3105–L3119

[回到原文件 L3105](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3105)

- 美国睡觉时间到底是好的还是不好的？
- 我一般平时靠人操作不用humanize
- APU有点东西啊
- 然后睡觉的时候再给他一些需要跑出来让我看结果的东西玩ralphloop
- 1m7.653575s
- al duration:
- d duration:
- 93.8646ms
- 15 token(s)
- mpt eval count:
- mpt eval duration: 77,6191ms
- 193.25 tokens/s
- mpt eval rate:
- 1 count:
- 2931 token(s)

---

#### 原文 L3163–L3188

[回到原文件 L3163](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3163)

- 我有个朋友做了个这个
- github: https://github.com/AgentOptimizer/agentopt
- 主页: https://agentoptimizer.github.io/agentopt/
- 文章: https://agentoptimizer.github.io/agentopt/blog/2026/03/22/why-your-agent-needs-a-model-combo-
- optimizer-not-just-a-model/
- 3月28日14:40
- 所以最后做的是开一堆小模型然后somehow收集小模型的结果看最后的效果大概是比如10个1b模型可以有
- log(10)b模型的效果
- 我忘记底数是多少了反正scaling是一个log
- 把agent workflow里的简单任务替换成简单但capable的draft model
- github.com/AgentOptimizer/agentopt主页: http...
- 是类似Speculative tree的东西吗
- 是叫这个嘛(？)
- 3月28日15:40
- 我说codex的/review为啥这么好用，原来他会自己调用humanize的review功能
- 刘诗楠:我有个朋友做了个这个github: https://
- Lurker:我说codex的/review为啥这么好用，原来他会
- 自己调用humanize的review功能
- 这是可以说的吗
- 被humanize养娇惯了
- 3月28日.15:49
- 我总于理解了token管够的含金量
- Lurker: 被humanize养娇惯了
- 3月28日15:51
- 一直都是啊

---

#### 原文 L3194–L3213

[回到原文件 L3194](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3194)

- 我给AGENTS.md加上这句话之后，codex版的humanize好像也会分配任务然后起sub-agent了
- 不过不太清楚是这句话的作用还是我本的humanize有之前我试验版本的残留
- 好像是新版codex的prompt改了
- 以前codex得主动使用$来调skill
- 现在他自己就能调skill
- 就是用skill更积极了
- 我给AGENTS.md加上这句话之后，codex版的humanize好像也会分配任务然后起sub-agent了
- (h
- 非语作为予值要者，你的工作是分析当商务融转分成型
- 比未值，开日品型训用用卡sub-agent急reviee，这耕伤元
- 光分用价t-的力4igh)，-
- btw，这是origin/dev merge了周老师的pr47的版本
- 张东宇:我给AGENTS.md加上这句话之后，codex版的
- humanize好像也会分配任务然后起sub-agent了
- 那你在用codex的时候也自己起sub-agent了吗
- Lurker: 以前codex得主动使用$来调skill
- 现在的codex就是会自己起很多

---

### 3月29日

#### 原文 L3316–L3332

[回到原文件 L3316](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3316)

- 3月29日10:25
- 欸你们用记忆系统的时候，会不会有因为过时记忆引起的问题
- 段震伟:
- 我这两天发现有时候需求变了，但是记忆系统没被更新，导致效果很不好。
- 3月29日10:32
- 这还有个经验主义
- 3月29日10:06
- 有个睡眠系统后台运行
- 会。所以我会吩咐agent每次存记忆都要检查一遍一致性
- 张东宇：欸你们用记忆系统的时候，会不会有因为过时
- 记忆引起的问题
- 这个一致性是指不一致的话不让新记忆存进去吗
- 张子健:会。所以我会吩咐agent每次存记忆都要检查
- 一遍一致性
- 睡眠的意思是在睡眠中检查每一条记忆有没有过时吗
- 段震伟:有个睡眠系统后台运行
- 你们发现Claude有一个自动做梦的功能了吗

---

#### 原文 L3336–L3369

[回到原文件 L3336](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3336)

- Checkes in mt ./CLAUDE.n
- Project memory
- Ouen auto-nenory falder
- 3月29日10:38
- 我觉得记忆太重要了
- 所以我都关了，手写
- 禁止它胡乱记忆
- 而且humanize的bitlesson有了之后
- fol
- ary
- uto-memory: sn
- uto-dream: offnaver
- Sarwae in =/,cLaude/ELR
- Uasr memory
- .claude/CLAUDE.ms
- Checkes in et ./CLAUDE.m
- Project mamory
- Osen auto-nenory folder
- 其实很大程度上已经做到了记忆该做的事情
- 3月29日10:47
- 我就是bitlesson记录了之前废弃的需求才想起来这事的
- 刘思皓: 而且humanize的bitlesson有了之后
- 这两天研究一下记忆更新机制，看把它放到什么时候做比较合适
- 我发现codex remote review的消耗量很大
- https://github.com/humania-org/humanize/pull/51
- 这个dev pr我上了个loop,查到没有问题直接把我周线的7%查没了
- 他的codex review quota是不是本来就要少很多？不是全部的
- 3月29日10:52
- 现在是全局然后在每个rlcr的结尾才写吗？我昨天用了一下
- 我朋友之前写了个paper做这个，https://github.com/ace-agent/ace他最近在SWE场景上有些industry deployment
- 张东宇:这两天研究一下记忆更新机制，看把它放到什
- 么时候做比较合适
- 3月29日10:55

---

#### 原文 L3400–L3428

[回到原文件 L3400](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3400)

- 3月29日11:27
- /loop 15m 解决一下pr xx 的问题 解决完 @codex
- 刘诗楠:啊我还挺喜欢pr-loop的
- 就好了
- @codex
- 若无必要勿增实体
- 我是推崇claude开箱即用的
- humanize存在的唯一原因就是开放爱和人类学是俩公司
- 感觉这个可以封装成ask-others/ask-reviewer。然后在config里配置被ask到的cli和model
- 刘思皓: 增加了一个ask-gemini的功能
- 3月29日11:33
- 我之前的full delegation版本是这样做的
- 3月29日11:37
- 但是现在cc和cx都天然支持batch和sub-agent了，还在想怎么把builder的配置跟cli原生的batch结合起来
- 张东宇: 我之前的full delegation版本是这样做的
- 3月29日12:19
- 3月29日13:14
- 这个A
- @codex 也是原生功能吗
- 刘思皓: /loop 15m解决一下pr xx的问题解决完
- @codex
- https://github.com/humania-org/humanize/pull/51
- 是的呀，这一整个PR都是全自动解决的，我当时在吃饭
- 3月29日13:23
- 其实简易版的humanize只需要
- m1
- /loop 1h use ask-codex to check claude code implementation
- 3月29日13:37
- 5.0惊现内测，Anthropic都害怕

---

#### 原文 L3432–L3467

[回到原文件 L3432](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3432)

- : ) next level
- "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
- "permissions": {
- 90分钟攻破20年Linux漏洞！Claude
- -1,7 +1,4 @@
- "env":
- "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
- "permissions": {
- 这玩意真是最糟糕的设计，坑我好久
- 我现在在外面拆的
- 刘思皓:这玩意真是最糟糕的设计，坑我好久
- 50个agent是要干啥，黑进美国政府吗
- 3月29日15:38
- 传出去：Sihao要进攻五角大楼
- Lurker: 50个agent是要干啥，黑进美国政府吗
- BY
- agent Smith
- claude牛逼东西确实多
- 但是糟糕的设计也不少
- /init, mcp, agent teams
- 还有auto memory
- 毕竟快速迭代下不可能每次都能开出ssr
- 我今天仔细去我每一个项目的memory文件夹里面看了下
- 我发现一堆那种“瞬发经验”和长久记忆混在一起的东西
- 赶紧把auto memory关了
- 我也是
- 刘思皓:我今天仔细去我每一个项目的memory文件夹
- 里面看了下
- 看了一下memory里面记的东西
- 那个auto memory坏极了
- 它没有区分短期记忆和长期记忆
- 立马关掉
- 3月29日15:42

---

#### 原文 L3573–L3585

[回到原文件 L3573](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3573)

- 我感觉那地方是个优先级超高的地方
- 写prompt有时候不管用
- 写claude.md可以瞬间管用
- 然后memory的文件和claude优先级几乎差不多
- 所以automemory也很坏
- 它往一个优先级很高的持久性的地方注入一些瞬发经验
- 宛如得了阿兹海默
- 关键是这俩这么重要的地方，人类学搞得很隐晦，不踩坑是不会知道的
- 3月29日16:45
- 然后记忆就迅速腐烂，然后才有autodream。关键是我觉得memory其实要写的东西没多少，不如全删了手写
- 我一般实践上会把memory分为memo和sessions两部分，sessions在每次收口之后记录这次做了什么有什么发现之
- 类的，memo则是人类和ai共同维护
- 3月29日17:20

---

### 3月30日

#### 原文 L3632–L3647

[回到原文件 L3632](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3632)

- 3月30日00:07
- 我有一个关于humanize的proposal
- 我觉得现在humanize还缺少一个“软性优化目标”的支持
- 就是humanize如果是一个solver，他目前对constraint的支持很好。但是还没有optimization target的感知能力
- 就和humanize的一体两面就是现在的各种autoresearch，对optimization target的支持很好，但是对constraint的
- enforcement没有humanize好。
- 我觉得可以融合一下。让humanize支持open-ended的optimization
- 张东宇: .claude/config.json还是settings.json我忘了
- 3月30日01:46
- 我已经做了
- 香港科技大学研究助理教授徐策羽:我觉得可以融合一
- 下。让humanize支持open-ended的optimization
- 我现在正好有exactly两个run就在做你说的这件事
- 香港科技大学 研究助理教授 徐策羽: 就和humanize的
- 一体两面就是现在的各种autoresearch，对optimiza...
- 10:484

---

#### 原文 L3651–L3710

[回到原文件 L3651](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:3651)

- 已经从之前县三
- 你完全可以拿humanize去做open-end optimization aka auto research
- 我现在就在做
- 刘思皓: 你完全可以拿humanize去做open-end
- optimization aka auto research
- 3月30日02:03
- 你直接把优化软性感知写进plan不就好了
- 一体两面就是现在的各种autoresearch，对optimiza...
- 虽然这本身是humanize的错误用法：build while exploring
- 但并不是说不能做，无非只是让humanize从做一个具体的plan，变成做一个meta-plan
- 3月30日04:29
- M老头们的性乐生活
- 3月30日09:29
- humanize的dev分支现在有一个“沉淀反思模式”
- 全部跑完以后会触发一个opus agent去沉淀反思整个多轮迭代
- 然后问你“是否愿意帮助改进humanize”
- 如果用户愿意的话，会把整个开发记录脱敏，然后经过审核之后，直接开issue
- 这就是我最后想出来的“humanize的ci/cd”
- 3月30日09:46
- 你得用dev的humanize
- 泽文: 我试试
- # If you want to use development branch for experimental features
- /plugin marketplace add humania-org/humanize#dev
- 3月30日09:53
- 3月30日09:53
- 3月30日10:03
- 但是我觉得优化软感知写进plan是不是还不太够啊，有没有一些更多的enforcement？比如说不能是我AC全部check
- 了之后我就结束，而是应该尝试继续优化。
- 刘思皓:你直接把优化软性感知写进plan不就好了
- 再比如说如果某个round对于optimization target没有进展的话，就干脆stash掉
- 3月30日10:13
- sihao哥，我更新插
- 我还以为codex的/review这么好用，原来是humanize的，细糠吃多了
- 3月30日10:46
- 那你应该先起十个点子plan
- 香港科技大学研究助理教授徐策羽:但是我觉得优化软
- 感知写进plan是不是还不太够啊，有没有一些更多的...
- 然后并行跑十个humanize
- 应该会因为其实我也没跑过
- 泽文: sihao哥，我更新插件了，继续跑，全部AC完成
- 以后，会自动触发这个对吧
- 我一般等不到humanize全跑完
- 3月30日11:49
- https://x.com/bcherny/status/2038454336355999749?s=46
- 完蛋
- 不对还是有个新东西/branch
- 我立刻学习
- 3月30日11:55
- 这个是以前的/fork吧
- 这个对我来说是新东西了因为我之前问过claude，web端只能控制web端打开的session，看来claude自己更新的都不及时
- Boris Cherny@bcherny - 44m
- 2/ Move sessions back and forth between mobile/web/desktop and
- terminal
- Run "claude --teleport* or /teleport to continue a cloud session on your
- machine.
- Or run /remote-control to control a locally running session from your

---

### 3月31日

#### 原文 L4062–L4075

[回到原文件 L4062](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4062)

- 3月31日01:01
- humanize启动！让我试试humanize1.16
- 3月31日04:31
- GitHub
- do
- plugin-cc
- openai/codex-plugin-cc:
- Use Codex from Claude
- Code to review code or
- delegate tasks.
- 3 hours ago - Use Codex from Claude Code to
- review code or delegate tasks. - openai/codex-
- plugin-cc.
- 更新到1.16.0在start-rclr-loop突然多了问题的回答

---

#### 原文 L4083–L4094

[回到原文件 L4083](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4083)

- 3月31日04:52
- https://github.com/openai/codex-plugin-cc
- Hhhhhhh你比我更快!
- hazelnut:
- 我觉得humanize没有存在的必要了
- 3月31日05:19
- ？哈哈哈哈
- 3月31日06:44
- 我遇到过类似的问题，我的问题是rlcrloop启动后项目自动make clean把.humanize文件夹里的state.md清掉了，导
- 致humanize不清楚自己的当前状态
- Compass:后面无论输入什么都是Interrupted·What
- should Claude do instead?

---

#### 原文 L4098–L4106

[回到原文件 L4098](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4098)

- Joe布衣:我遇到过类似的问题，我的问题是rlcrloop启
- 动后项目自动make clean把.humanize文件夹里的st...
- 3月31日08:09
- 因为我在一个工程里用humanize干了两件完全不同的事，后一个认识前一个的humanize，这是一个失误
- 刘思皓:你的makeclean为什么会认识humanize
- 3月31日09:53
- 刘思皓:你的make clean为什么会认识humanize
- 3月31日09:53
- [high]|

---

#### 原文 L4161–L4173

[回到原文件 L4161](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4161)

- 189
- Harness 的公司
- 这也太抽象了
- 韩大盐：爱马仕：一家做了189年
- 189
- Harness 的公司
- 3月31日10:32
- https://github.com/openai/codex-plugin-cc
- 这feature release速度也太快了
- Claude Code能控制电脑了！开发全
- 程不离终端，全无人值守模式启动
- 你的token还够用吗？

---

#### 原文 L4282–L4290

[回到原文件 L4282](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4282)

- Joe布衣: 因为我在一个工积用田bumanizo于了两件完
- 全不同的事，后一个认识前一个的humanize，这是...
- 不用ci，本地测试完直接push
- 解决了，原因是我需要升级/降级codex和claude，更改了设置和路径，中间一些设置影响到了openclaw，以及我也
- 是在一个目录下和子目录下都用了humanize
- 3月31日15:58
- 最后把openclaw重新下载一下，再重新开个目录，--skip-quiz让humanize快速执行就解决了
- Lurker:
- 3月31日17:06

---

#### 原文 L4474–L4486

[回到原文件 L4474](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4474)

- 刘思皓：哈哈哈哈这就是我加的那个“你愿意帮助改进
- humanize嘛?
- 泽文: 不过我会让claude 手动总结提交issue
- 不过居然你这次humanize没发现啥方法论的问题
- 蛮好的
- 我让humanize规划并fork了qemu，实
- 3月31日21:56
- 重写整个qemu吗
- 3月31日22:09
- 我现在规划了一些复杂任务，让humanize跑，然后我开新的
- 做隔离，然后如果功能开发或者bugfix没啥问题，再让把补
- 现在我也看到issues blocking的信息了，貌似这个不是一直显示的
- 我还以为又是codex上出bug了

---

## 4 月

### 4月1日

#### 原文 L4512–L4521

[回到原文件 L4512](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4512)

- Claude Code 的 coordinator 模式
- 就是你用Agem工具派子任务、多个
- worker 并行干话那个功能——整个
- 模块只有一个文件。370行代码。没
- 有状态机，没有DAG，没有
- workflow engine.
- 它的“编排逻辑“是什么呢？一段300
- 行的 system prompt.
- ClaudeCode 源间增膜： 流析 51万
- 目阅读原文

---

#### 原文 L4531–L4549

[回到原文件 L4531](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4531)

- 4月1日02:06
- 我觉得harness engineering下—个阶段应该是judgement engineering
- AI的能力越来越强了，说No变成了一个很关键的东西
- 4月1日02:27
- Harness Engineering in 2026.3
- 不知道为什么最近 Harness
- Engineering 突然火了，之前我
- 其实猜到了大家肯定要发明一.
- 我世界的源代码
- 4月1日03:41
- 由于舍不得消耗高级模型的额度，他们长期在
- Auto模式下反复拉锯·低阶模型生成的代码逻辑
- 混乱，原本10分钟能收敛的问题，他们宁愿花2小时
- 去人工Debug，熬到凌晨两三点。
- 现状：为了省下20块钱，选择透支高价值的脑
- 力和睡眠。
- 代价：这种“勤俭”严重拖慢了项目的收敛速
- 度，并产生了一种“我很努力”的自我感。
- 资源的配置能力，与学历高低无关。

---

#### 原文 L4858–L4868

[回到原文件 L4858](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4858)

- 中，前两轮效率极高，但第3至6轮呈现出“打地鼠...
- https://github.com/humania-org/humanize/blob/dev/prompt-template/claude/methodology-analysis-
- prompt.md
- @泽文 https://github.com/humania-org/humanize/issues/53
- 你用这个模版筛一下你的issue
- 这个问题直的很妙
- 中，前两轮效率极高，但第3至6轮呈现出“打地鼠...
- 你怎么开发一个杜绝长尾修复的agent呢
- 真妙，这不就是方法论的自我迭代
- 如果2030年没有实现AGI

---

#### 原文 L4950–L4964

[回到原文件 L4950](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4950)

- 人都做不到
- 需要把 humanize的最终结果作为预训练数据
- 刘思皓:其实我觉得就应该一次性写对
- 我跟 kimi 和 glm的人都讲过这个故事
- 这是超越 opus 和 codex
- 蒸馏结果的数据集
- 4月1日11:46
- 那能不能让kimi和glm的人搭中转站免费用（
- humanize的记录的价值多大我都想象不到
- 你去哪里找真实场景的多轮开发记录
- 现在中转站都是赚两手钱
- 4月1日11:52
- 可以考虑出一个 recoding 功能用户愿意的话(belike 做开源项目开发)可以把这个 commit 推送 hf datasets 里
- 这个loop的signal确实非常多，拿去SFT估计都能提升巨大
- NV周耀阳: 这是超越opus 和 codex蒸馏结果的数据

---

#### 原文 L4975–L4988

[回到原文件 L4975](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4975)

- 大家都意识到human reward 这组数据的重要性了
- 搞humanize托管站，别人在上面做项目，然后我们把humanize的过程记录就可以卖给国内ai公司了
- 类似自动驾驶里的用户接管数据
- 即刻创业
- Lurker:搞humanize托管站，别人在上面做项目，然
- 后我们把humanize的过程记录就可以卖给国内ai公...
- 是，他们还有各种random poll
- !:昨天群里发的Claude code标记用户粗口就是这个
- 目的吧。
- 我已经在干了
- Jurker:搞humanize托管站，别人在上面做顶目，然

---

#### 原文 L4993–L5003

[回到原文件 L4993](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:4993)

- humanize 我不会泄露给公司任何人
- 开源芯片 agent flow 张宇鑫: humanize 我不会泄露
- 给公司任何人
- 坏了，点子都让群友干了
- 托管站可还行
- Lurker: 搞humanize托管站，别人在上面做项目，然
- 后我们把humanize的过程记录就可以卖给国内ai公...
- humanize相当于是倒贴钱帮人类学蒸馏开放爱
- 相互蒸馏，正好开放爱的快速开发能力不如人类学，人类学的分析能力不如codex。也算是o/c家agi路上左脚踩右脚
- 的一个加速器了

---

#### 原文 L5146–L5164

[回到原文件 L5146](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5146)

- 4月1日17:52
- 今天humanize把我觉得可能至少得探索三四个月的一个问题给解决了
- 震撼啊
- 我在椅子上摊着，像看到核爆炸一样
- 这种一般要循环几次呢
- 我经常会循环三四十次以上
- 我昨天用codex的humanize提了一个简单的需求，循环了9次，但是看结果有点乱，化简为繁的感觉
- 90
- soga
- 刘诗楠:我经常会循环三四十次以上
- 我还在整个大的，重写humanize的round任务管理机制
- 太強了
- Lurker:我还在整个大的，重写humanize的round任务
- 管理机制
- 期待!
- Lurker:我还在整个大的，重写humanize的round任务
- 管理机制
- 以后到底要做什么样的research才行

---

#### 原文 L5229–L5244

[回到原文件 L5229](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5229)

- 目前的humanize是用不了的
- 4月1日23:28
- 刘诗楠：我在椅子上摊着，像看到核爆炸一样
- 谁能想humanize最初只是我为了给自己写代码方便造的小工具
- —个side project
- 那么牛逼啊
- 刘诗楠:今天humanize把我觉得可能至少得探索三四
- 个月的一个问题给解决了
- 我感觉我给的task好像还是太简单了
- 最近复现一个baseline
- 作者开源的repo是有问题的
- humanize迭代到中间某一步的时候发现了这个问题
- 顺手帮我把baseline修了...
- 计划有变，明天开源

---

### 4月2日

#### 原文 L5338–L5352

[回到原文件 L5338](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5338)

- 是的，我先测试一下
- 前端有比较好的workflow 吗？目前我还是在抽奖，需要和ai 迭代好多轮
- 4月2日09:44
- 昨晚用humanize搓了一个，感觉
- 前端有比较好的workflow 吗？目前我还是在抽奖，需要和ai 迭代好多轮
- 4月2日09:44
- 4月2日09:58
- 你有没有装claude code的前端skill
- 泽文: 昨晚用humanize搓了一个，感觉效果不咋地，
- 主要是不懂前端，不知道咋进行技术选型
- 非常炸裂的
- frontend-skills
- 4月2日10:05
- 4月2日10:06

---

#### 原文 L5428–L5438

[回到原文件 L5428](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5428)

- 短任务我就喜欢这么千
- 可以拉一个无上下文的review，找bug更容易
- 4月2日12:29
- 不会有上下文干扰
- 我刚刚遇到一个nccl的报错，我觉得claude 给我的回答我不满意，我就让他用这个skill去问codex
- 然后果然就解决了
- 我过去一个月在claude code和codex上都出现过：一个工具搞到山穷水尽弄不出来，然后让另一个工具“看一下现
- 在的状态”，然后就搞出来了
- 这种都是钻牛角尖了，你得主动跟他说路子走歪了，起一个无上下文的agent本质上就是让他从另一个继续找
- 杨硕: 我过去一个月在claude code和codex上都出现
- 过：一个工具搞到山穷水尽弄不出来，然后让另一个...

---

#### 原文 L5479–L5497

[回到原文件 L5479](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5479)

- 你俩要不要整合一下GUI/TUI不要重复劳动
- 我感觉怎么同时有3-4波人在给humanize造图形界面
- hhhh不错
- 4月2日12:54
- 还能看多个humanize，np
- https://gith
- gemini前端应该最强
- 4月2日12:54
- 还能看多个humanize，np
- 泽文:
- 4月2日12:55
- 哈哈，好像我最先在群里提起的
- 刘思皓: 我感觉怎么同时有3-4波人在给humanize造图
- 形界面
- 4月2日13:04
- 哥你要从dev checkout出来开发的
- 泽文: https://github.com/zevorn/humanize/tree/
- feat/viz-dashboard
- main落后dev一个月的

---

#### 原文 L5699–L5861

[回到原文件 L5699](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5699)

- 我的可视化跟我的方法学是强耦合的
- 现在humanize的方法学是尸(时间)山血(token)海堆出来了
- 我不是很敢动方法学
- 其实
- 应该用humanize 去迭代 humanize
- given unlimited tokens and GPUs and VMs
- 4月2日22:40
- 看一下怎么设计的 time-to-success/ token-to-success / human-involve最好
- loop反馈太长humanize会瞬间变得N省M部
- 你可以在群里面介绍一下你的方法学改动了啥吗？ @Lurker
- Lurker:我的可视化跟我的方法学是强耦合的
- 比如泽文哥所有issue我其实可以瞬间让humanize解决合并了
- ok 明天我把描述发出来
- 我感觉 claude 总结的这些issue反应的问
- 而不是bugfix一
- 确实
- 但我这时候脑内警铃大作
- 自己不参与。。那存在感何在
- humanize一定得“足够简单”
- 刘思皓: humanize一定得“足够简单”
- 有些东西，尤其是“woc妙啊”这种东西
- 我会瞬间加入
- 但是对于那种大的方法学改动，除非我看到多个实证，否则我会谨慎尝试
- 我只能多多贡献issue了哈哈，我
- 不过我可以开一个beta branch在humanize里面
- 空想是绝对没效果的
- 多来几只小白鼠帮我测试下
- 你得让大家去试
- woc实践是检验真理的唯一标准
- 刘思皓:我深刻知道方法学你不去用实战迭代
- 我深刻知道万法学你不去用实战迭代
- 4月2日22:45
- 把毛选让agent学习一遍
- 我这个月会把humanize的prompt模版大幅度精简一下
- 感觉有些prompt模版废话太多了
- 我感觉这个应该是非常有实验价值的场景
- 泽文:我只能多多贡献issue了哈哈，我这里有大量的实
- 验样本场景，全是复杂的底层系统软件
- 现在很多搞底软的甚至不敢用ai
- 前段时
- 4月2日22:50
- 你说的性格是什么意思
- 不同模型？
- 比如跳脱的cc冷静的codex
- 话说humanize的方法论换了不同性格的agent 还适用吗
- 4月2日22:55
- 你咋赋予性格的
- 写在claude.md里面?
- 4月2日23:02
- 不是哇就大家不都发现codex比cc指令遵循更好，废话更少吗
- 哦哦
- 这个其实是humanize的核心机制
- 并且R是codex之后，B是什么其实区别不太大
- 4月2日23:26
- 对吧所以这就说明humanrize依赖某个东西，而不是某种客观的真理，可以这么理解吗
- 4月2日23:32
- humanize现在确实依赖codex as review
- bi-level loop + batch 本身效果不大
- 但是如果你把 R 变成 codex
- 就和加入了催化剂一样，整个效果变得巨大
- 我大概4个月前就说过，如果开源模型哪怕只有一家，什么都不做，就只要把通用review的做到codex的80%+
- 随便接一个kimi 2.5/minimax, 走humanize flow转起来， 效果可能会比—个Opus 4.6好
- 4月2日23:37
- 哈哈哈
- R决定收敛质量，B决定收敛速度
- codex真的是独门绝技了隐忍
- P和D共同决定了能一次性做完的任务大小
- P: Plan，承载了人类的意志和目的
- D:Delegate的好坏影响一次性做完任务的大小
- B: Build的好坏影响完成任务的收敛速度
- R: Review的好坏影响最后任务完成质量本身
- 这个真是厉害
- 刘思皓: 随便接—个kimi 2.5/minimax, 走humanize
- flow转起来， 效果可能会比一个Opus 4.6好
- 这就是之前一直讨论的P-D-B-R模型，然后我觉得最后最"简单可行的架构"估计长这样:
- P-/loop{D-/batch{B-R}}
- 4月2日23:42
- 你口西选代(oop)和并行(hbateb的位置插对了 就这四个Aaont就足完成亿竞士小的亿名了
- 刘思皓:我大概4个月前就说过，如果开源模型哪怕只有
- 一家，什么都不做，就只要把通用review的做到codex...
- 但是似乎都在蒸馏claude啊
- 所以还是，大道至简
- 目前国产开源大厂都在疯狂蒸馏我感觉很快就会赶上了
- 都会吧
- 牛逼
- 刘思皓: P: Plan,承载了人类的意志和目的 D: Delegate
- 的好坏影响一次性做完任务的大小B: Build的好坏影...
- 我觉得codex那个超强的review能力需要速度蒸馏一下
- Claude目前收了口子蒸馏成本大大提高了
- 两个月了，我还没有看到一个在review方面接近codex的开源模型
- 我其实完全不在乎build的质量，感觉build方面开源模型完全够用了，而且反正是humanize睡觉编程，我也不怎么在乎
- 收敛速度
- 但是codex的review两个月了，无论开源还是闭源，依旧是独一档的
- 你这个是把 kapathy的 autoresearch 又提炼出了一个新的高度
- 我感觉和模型的性格有关系
- 刘思皓: 但是很奇怪,我拿codex build, 效果又不太好
- autoresearch在humanize之后蛮久才出来的
- Auto
- 帅帅 aka Quiz: 你这个是把 kapathy 的 autoresearch
- 又提炼出了一个新的高度
- 4月2日23:47
- 刘思皓: 这就是之前一直讨论的P-D-B-R模型，然后我觉
- 得最后最"简单可行的架构"估计长这样: P-/loop{D-/...
- open ai的模型都有股浓浓的中学教导主任味儿
- autoresearch其实一直是humanize的B部分
- 群友说的(
- 4月2日23:48
- 适合 review
- 我其实一直没有试过auto research
- 这个太牛了
- 刘诗楠: autoresearch在humanize之后蛮久才出来的
- 我还没有彻底打磨好
- 刘诗楠：我要这个
- 他那个只嫩个算个 POC 吧
- 刘思皓: 我其实一直没有试过auto research
- 期待(∀)
- 刘思皓:我还没有彻底打磨好
- 那个特别简单
- 帅帅 aka Quiz: 他那个只嫩个算个 POC 吧
- 算个教学案例
- 期待啊
- 理论上 prompt 也可以 autoresearch
- 刘思皓: 我这个月会把humanize的prompt模版大幅度
- 精简一下
- yup
- 帅帅 aka Quiz: 理论上 prompt 也可以 autoresearch
- L.Zhu: 应该用 humanize 去迭代 humanize
- 就是特别Token
- 4月2日23:53
- 我其实手动干过，比较容易跑偏
- 最近 vibe coding 的体会就是上厕所的频率大大提高了
- 因为很容易口渴喝了太多水
- 感觉胰岛素抵抗都减轻了
- 【No Priors播客】安德烈·卡帕西：
- 编程智能体、自动化科研与AI的...
- UP主：KrillinAI小林
- 播放：3023
- 哔哩哔哩
- kapathy的这个访谈很有启发
- 他说要尽量减少 human in the loop
- 人才是最大的阻力
- 4月2日 23:59
- 码住
- 帅帅 aka Quiz:【No Priors播客】安德烈·卡
- 帕西：编程智能体、自动化科研与 AI的循环时...
- 我不觉得
- 帅帅 aka Quiz: 他说要尽量减少 human in the loop
- human 是上帝，必须听话
- 帅帅 aka Quiz: 他说要尽量减少 human in the loop
- Humanize好多设计需要积累巨量的失败经验之后，一次性给humanize做减法的
- gaac -> humanize就是这么来的
- 我曾经设计过超过60个agents的复杂交互系统

---

### 4月3日

#### 原文 L5862–L6032

[回到原文件 L5862](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:5862)

- 4月3日00:02
- 直到失败了无数次我才意识到你必须**全部删掉**，只保留最最核心的功能: Ralph loop with Codex Review
- 感觉ai太发散了没有人纠正和限制容易越跑越偏
- 如果一直让llm in the loop, 大概率会导向一个极其冗余的系统
- 你说的对，少即是多
- 刘思皓:直到失败了无数次我才意识到你必须**全部删
- 掉**, 只保留最最核心的功能: Ralph loop with Code...
- 我觉得我以前整理的大量的skill完全就是废物
- 还有什么mcp就纯废物的玩意
- 加一个并行哈哈
- 刘思皓:直到失败了无数次我才意识到你必须**全部删
- 掉**, 只保留最最核心的功能: Ralph loop with Code...
- 人的意义就是拨乱反正 qtmd推倒重来
- 哦对 说到并行
- swarm mode也是一个实证
- 我不认为llm自己转起来能够发现"不能使用swarm mode"这种经验
- 它几乎100%会开始优化这个"蜂群协作模式"
- 而真正并行的解决办法简单至极: worktree隔离， subagent禁止沟通
- 4月3日00:07
- again, repeat after me: 大道至简
- 刘思皓:而真正并行的解决办法简单至极: worktree隔
- 离, subagent禁止沟通
- 真的，串味的方案真的要不得
- 我试过4个8个agent一起解决一个kernel问题，最后才发现得各干各的。其实也很好解释，context的精炼和专注是非
- 常重要的
- 我是绝对不会相信LLM能够自己推理出如此反直觉的事情的
- cherichy: yes!!!禁止沟通
- 我觉得核心点是：人类存在一种不耐烦的理性
- 可能是的人类的偷懒和agent的偷懒不一样
- 人类为了偷懒可以付出非常高的代价
- 一个混沌的谨慎理性-- 这是我觉得必须引入human in the loop的原因
- 4月3日00:12
- 也就是说，有大开大合破而后立的勇气
- cherichy:人类为了偷懒可以付出非常高的代价
- 很神奇目前没有发现agent有类似的moment
- 我高强度用AI也快一年半多了，我从未在任何场景下见到任何AI做过这种事情
- cherichy: 也就是说，有大开大合破而后立的勇气
- 这个test跑不过先帮你注释了吧这样就能跑通了
- L.Zhu: 追寻局部最优是这样的
- 动golden属于Jail break我觉得
- 和AI经过一系列深度思考之后，发现自己从一开始就做错了，然后积攒了绝对的勇气，敢于推翻重来--这是两件事
- 如果真的有一天我能见到这件事，我觉得AGI就来了
- 整理文件会这样，直接全套删除
- 追寻局部最优是这样的
- 4月3日00:21
- 这其实也是人类学对AGI的定义，一个爱因斯坦实验:如果你只给LLM1905年之前的语料，它能否独立发现相对论
- 想问一下，目前总结的这套方法学，有第一性原理的解释吗？
- ctlon-Instead of expecting perfact ounput in one shot, Hum
- c loops waere issuss are caught warly and refined rncremental
- wiew  Claude implements, Codex indepsndently nevinws. No
- rarm Mode – Iterative refinement continues untl all acceptan
- with Agent Teams.
- in Mind – Sefore the loop starts, Humanize verifies that you
- The human meust remain the archabect (etal
- 1. 迭代大于一次性完美
- 2. 构建和审查不能是同一个实体
- 3. 迭代和并行
- 4. 以终为始
- 这其实也是人类学对AGI的定义，一个爱因斯坦实验:如果你只给LLM1905年之前的语料，它能否独立发现相对论
- 想问一下，目前总结的这套方法学，有第一性原理的解释吗？
- ction - Instead of expecting perfect output in one shot, Hum
- c loops ware issuss are caught early and refined ncremental
- wiew -Claude implements, Codex indepsndently nevinws No
- rarm Mode - Iterative refinement continues untll all acceptar
- with Agent Teams.
- in Mind – Sefore the loop starts, Humanize verifies that you
- The human meust remain the architect. (etals
- 这是第一性的解释，至于codex成为R之后效果这么好，说实话我不知道
- 4月3日00:26
- 感觉 AI 偏向让系统朝熵增演进
- 刘思皓：我高强度用AI也快一年半多了，我从未在任何场
- 景下见到任何AI做过这种事情
- 1多步法精度高于一步法很合理
- 2 独立的context更利于reflection
- 3就是1+2
- 4 是确保注意力集中
- 非常合理
- 4月3日00:42
- 是，我难以想像短期内有任何AI会出现任何的：我从一开始就全部错了，我需要全部重来，然后让全局一次性归零，再做
- 这似乎和LLM的本质，预测下一个token违背
- 这需要做到一个巨量的熵减动作，然后下一次迭代往一个完全不一样的路径推演
- woc我之前也是这么觉得的
- 刘思皓:这似乎和LLM的本质，预测下一个token违背
- 我也感觉是和自回归的性质有关联
- 这种事情transformer干不出来，得diffusion
- 如果自发的不行，为啥不能触发这个操作呢
- 刘思皓: 是，我难以想像短期内有任何AI会出现任何的:
- 我从一开始就全部错了，我需要全部重来，然后让全局...
- 4月3日00:47
- 所谓路径依赖，context没有清除记忆这个操作，顶天也就是一个compact
- 理论上是可以在人的引导下做这件事
- 除非重开，或者subagent
- 做context隔离
- 如果是如此惊艳的操作，就该把它做进harness的一部分
- cc 有个/simplify
- 不过需要手动触发
- 后来我算是想明白了，就是sihao说的，小即是多
- 4月3日00:49
- 如何去权衡增减是很难的
- 刘诗楠:如果是如此惊艳的操作，就该把它做进
- harness的一部分
- cherichy:这种事情transformer干不出来，得
- diffusion
- 类似 explore & exploit 之间的权衡
- 这话让搞 dllm的人又要兴奋了
- cherichy:这种事情transformer干不出来，得
- diffusion
- 我有想过，一个prompt+固定的权重 diffuse出来一个context，然后再给transformer做下去
- 这个context是啥不重要但它是全新的
- 那其实也不一定要dllm
- 4月3日01:30
- CLAUDE_CODE_NO_FLICKER=1
- cc终于把闪烁取消了
- 新版的cc看起来丝滑好多
- 4月3日09:55
- 我们内部每周都有agent 的sharing，今天也有人提到了 zero share memory for subagent
- asnun 重XktEy+duoudI
- uosupu'xuuo
- 我有想过，
- CLAUDE CODE NO FLICKER=1
- l f f  z n  et
- 目前一些客观的评价信息或者操作我都会派subagent去处理，可以保持主session上下文干净，但是不清楚目前的
- subagent会不会自己看memory
- 4月3日10:04
- 我觉得这个事情openclaw就做的很好啊，你肯定不能去share agent的session history。
- 但是可以去share curated knowledge。
- 4月3日10:15
- 昨晚白睡，又卡在提权了
- 我睡前会跟他说：接下来，我要去睡觉了。我希望明天早上能看到你的结果，如果需要问我问题的，你就别问了，自
- 己跑，跑完为止
- 我也试过这个prompt,第二天早上只做了一半气死我了
- 刘诗楠：我睡前会跟他说：接下来，我要去睡觉了。我
- 希望明天早上能看到你的结果，如果需要问我问题的...
- 好像可以搞个 hook 自动回复 continue
- CODE
- IS THE
- 五个隐藏蜜钥
- 让你轻松玩转Claude code
- 顽童AI情报站
- 这说的是真的假的
- 4月3日11:09
- 挺简单的，我做了个https://github.com/amphoreus-ai/codex-eternal-recurrence不过运行久了agent可能会
- hack掉这个hook
- Horace: 好像可以搞个 hook 自动回复 continue
- 目前想不到有什么解决方案
- 大概就是它会把hook里面匹配的字段说出来，然后输出一段自相矛盾的话，比如“我确认该任务已经完成，……，因
- 此该任务还在运行中，并未完成”
- 目前连续运行最长时间记录大概是29小时
- 4月3日.11:25
- 也不是ralphloop，纯粹是一个让agent继续跑的hook
- 不会把task重新喂给agent
- me_task3_de
- me v0 plan,
- 现在我改的新版humaanize当发现上一个任务执行得不对劲时，会自己重新规划设计
- 4月3日11:36
- 不太对，plan.md在任务进行过程中不是不要改么，这是humanize原则
- Lurker:现在我改的新版humaanize当发现上一个任务
- 执行得不对劲时，会自己重新规划设计
- 确实
- 没改plan
- 郑权:不太对，plan.md在任务进行过程中不是不要改
- 么，这是humanize原则
- 改的是task
- 就是上一个task执行得不够好，然后他会重新规划下一步的实现方案

---

#### 原文 L6040–L6059

[回到原文件 L6040](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:6040)

- 我今天早上和Claude就简简单单说你给我做个计划
- 他自己把humanize跑起来跑了一个多小时了
- 我现在发现ai理解意思，并调用skill的逻辑很不清晰
- 因为skill并不是严格的command
- 因为skill并不是严格的command
- 有时候需要把需求明确才行，群友有没有优化skill调用的好方法？目前能想到的就是在Claudemd里明确下
- ？看看你的prompt
- 杨硕:他自己把humanize跑起来跑了一个多小时了
- 4月3日13:58
- 真的就是“你给我查查现在为啥我们写的这个solver跑得不够快”
- Zeng haolun:?看看你的prompt
- 你来看看为啥不行
- 杨硕：真的就是“你给我查查现在为啥我们写的这个
- solver跑得不够快”
- 真的就是简单越好。。
- 4月3日14:10
- 不过我装了everything Claude和superpowers
- 禁止许愿编程
- 杨硕：真的就是“你给我查查现在为啥我们写的这个

---

### 4月4日

#### 原文 L6241–L6261

[回到原文件 L6241](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:6241)

- 我的claude已经非常自觉每次干完活都ask-codex检查了
- 感觉humanize已经内化了
- 4月4日05:48
- 群有是如何做并行的呢
- 就是不同的任务已经拆出来并行的任务了
- 但是在同一个project dir里面
- 是不是不好搞因为一般只有一个plan文件
- 4月4日06:29
- worktree隔离
- 看来也只能这样了
- 还是会有点小麻烦
- 4月4日07:03
- 提了个小issue，好像cc在普通任务的时候也会触发PreToolUse的hook，会出error信息，但不影响流程。不知道其
- 他人有没有碰到
- https://github.com/humania-org/humanize/issues/65
- 4月4日08:28
- 奇怪大家有遇到过这个bug吗
- terminal比如开了两个claude code一个是humanize的一个是在做一些别的事情放着不管过一会儿humannize的
- stop hook加载到了这另一个claude然后变成两个claude在那边跑humanize项目就出问题了。。。?
- 然后前台同一个vscode terminal 也有一个claude 然后出问题了呢
- 4月4日08:50

---

#### 原文 L6291–L6304

[回到原文件 L6291](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:6291)

- 证，当前值是 512000，而且当前 shel1 里没有 CLAUDE_CODE_AUTO_COMPACT_WINDOW 环境变量
- RLCR stop hook
- 泽文: 有点难受，不能触发 claude的 自动压缩
- 4月4日13:58
- 4月4日14:06
- Context 太大也不一定是好事，容易漂移，主要是glm 便宜
- 我算了
- 竟然只有200k
- 泽文: @Blowing 佬，我用 glm5.1 context 20% 就gg
- 最近国产的开源模型都挺不错的
- 4月4日14:09
- codex

---

#### 原文 L6421–L6434

[回到原文件 L6421](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:6421)

- 4月4日19:08
- 不和codex说用subagent它根本不用的
- 4月4日19:10
- 4月4日19:26
- 我一直怀疑用不用subagent和用的哪个harness也有关
- 我用codex-codex 它基本不用。我用cursor-codex 就经常用
- 之前用5.3-codex的时候还会用的
- :不和codex说用subagent它根本不用的
- 4月4日 20:59
- 因为cursor 经常会用subagent
- 饽饽博: 我用codex-codex 它基本不用。我用cursor-
- codex就经常用

---

### 4月5日

#### 原文 L6526–L6541

[回到原文件 L6526](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:6526)

- 4月5日12:15
- 正常开sub agent 不占总context
- 要自己再加prompt嘛，我以为codex会自己直接加subagent
- 饽饽博: 正常开sub agent 不占总context
- 根据这个plan，便用human
- 上1条消息）
- r running remote compact task: stre
- )s://rust.cat/responses/compact)
- rust.cat是什么高级东西？为什么会用rust.cat来compact
- 我觉得应该是加prompt的吧，反正我用CC，我一般都会说一声，我说你给我用agent team来写plan
- 4月5日12:20
- 中转站转发问题
- 饽悖博: 我觉得应该是加prompt的吧，反正我用CC，
- 我一般都会说一声，我说你给我用agent team来写pl...
- 中转站
- 饽饽博: rust.cat是什么高级东西？为什么会用rust.cat

---

#### 原文 L6580–L6598

[回到原文件 L6580](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:6580)

- 但是这种都有ip限制啊
- 额，humanize 群主要还是讨论 harness吧
- 额，humanize群主要还是讨论 harness吧
- 4月5日12:27
- 额，humanize群主要还是讨论 harness吧
- 你们快讨论harness我来围观
- 1M也不够有一说一
- 而且上下文窗口1M不代表1M长度工作性能和短的时候一样好
- 主要还是效果不好的问题
- 我认为现在就拉满于
- 现在模型应该都是hybird model把
- 我现在在 humanize stop hook 里面检查 jsonl size，
- 商业化落地再研究小模型大模型
- 感觉200K里是最好的
- B4RRy:而且上下文窗口1M不代表1M长度工作性能和
- 短的时候一样好
- 那种linear attention长文情况虽然快但是一定是有损失的

---

#### 原文 L6686–L6696

[回到原文件 L6686](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:6686)

- 4月5日15:32
- qq: rlcr loop 里面 codex ctx 满了一般要怎么办？ 有办法在 rlcr 里去 call codex /compact 吗
- Please retry or use /cancel-rlcr-loop to end the loop.
- ● 38 timeouts. Codex is reading massive wandb output logs (full step metrics) which fills its context.
- Waiting.
- * Channeling... (running stop hooks... 1/2 · 2d 13h 25m ·↓ 11.4k tokens)
- L Tip: Use /clear to start fresh when switching topics and free up context
- NVDA 周六还有这么多quota 给你用吗？
- L.Zhu: qq: rlcr loop 里面 codex ctx 满了一—般要怎么
- 办？有办法在 rlcr 里去 call codex /compact 吗Pl...
- 我跟老黄说说

---

### 4月6日

#### 原文 L6706–L6722

[回到原文件 L6706](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:6706)

- 4月6日10:17
- 晚点：MiniMax很早就把线性注意力用到了超大模型上，他们在今年初发布的4560亿参数的MoEM1上，就用了
- 混合线性注意力与全注意力的Lightning Attention，但10月底发布MiniMaxM2又回到了完全注意力。从业者是
- 怎么讨论这个转变的？
- 杨松琳：大家都觉得这个现象挺好玩。这有点像，线性注意力是一个“坑”，MiniMax赶着跳出去，Qwen和Kimi
- 又急着往里跳；不过Minimax也没完全失去信心，还在验证混合架构。
- Minimax可能之前受 Lightning Attention的伤太大了，—朝被蛇咬十年怕井绳。Lightning Attention 很弱，只是
- 在最原始线性注意力上叠了粗粒度、输入无关的衰减。他们当时直接 Scale Up到几百B，可能是Eval(验证)没搭
- 好。
- 结果MiniMax 发现 Lightning Attention 在MMLU(注：测试大模型在 57 个学科上综合知识与理解能力的标准考
- 国的国家元首是谁？“)上，完全注意力能直接建模点对点关系，叠几层就能自然形成多跳推理；线性注意力或混合
- 结构会把信息压得很模糊，准确率掉得很厉害。
- 现在 Agent 做任务都会想很多，多跳推理在 Agentic AI里非常重要。MiniMax觉得混合架构暂时解决不了想主攻
- 的 Agentic AI，退回完全注意力挺自然的。
- 他们的反思里也有不少值得学的点，比如基准选择：一些多跳推理benchmark，如 BBH其实很容易，可以找方法让
- 架构表现很好，但不代表模型在真实场景里就真的会推理。
- NV周耀阳: Retrieval 没问题，但是智力下降，很有趣

---

### 4月8日

#### 原文 L6904–L6935

[回到原文件 L6904](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:6904)

- 4月8日07:46
- 我高强度用了2周superpowers
- 感觉还是太bloated了
- 我觉得讨论出来spec之后，仔细审核，然后丢给humanize就好了
- 那个plan实在是究级冗余，又慢又冗余，还非常容易overkill
- 但是比我最最开始用还是好了不少
- 同意还是需要自己对话几轮出来的plan才够精确
- 据说claude新的模型已经可以写kernel了
- 而且算子写的可能比人类强力
- 他的prompt首先就太长了似乎
- 刘思皓: 我高强度用了2周superpowers
- 我合作的业界的朋友之前就在拿openevolve写kernel了
- NVIDIA的kernel基本上成功率>50%，这还是在4.5时代
- 4月8日08:04
- 我觉得superpowers的spec其实就是humanize的plan
- superpowers的plan是个又臭又长的糟糕设计
- 感觉就是单纯为了Subagent-Driven设计的
- 我一般就是superpowers spec转rlcr plan
- 4月8日08:19
- 有可能是a社给降智了
- 刘思皓:总是想模拟人类这种一步步的开发流程
- 没有，这个现象一年前我就观测到了
- 但是其实一周的工作基本上10分钟就做完了
- 一个月的工作半天做完
- 它的记忆里面还是一天写300行左右的样子
- 4月8日08:27
- 先superpower出spec
- 再让humanize生成计划
- 生成的计划可以再用superpower brain storm反复打磨
- humanize生成计划?
- 你说那个gen-plan吗？

---

#### 原文 L6960–L7010

[回到原文件 L6960](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:6960)

- 问ai
- agent，我做出如下部署：
- 郑权：怎么修，浇浇窝
- 4月8日12:32
- GLM-5.1开源：一个独立工作8小时
- 的模型
- GLM-5.1
- 面向长程任务
- 智谱
- 8小时，还没到长时间humanize的零头
- 不过glm5.1 coding看着好像还不错
- 主要是humanize这个workflow好用
- 我试过B=kimi R=codex
- 他是存模型loop还是harness
- 也能哼哧哼哧干20小时
- 4月8日12:59
- 有个 feature 它 build 失败了两天
- 我放弃治疗加钱买了 $200 codex，一小时 build 对了
- 降智测试韭菜找到最佳配置啊
- 收入继续涨就继续降智
- 收入跌了就恢复点智力
- 4月8日13:15
- 我有个极难的任务分开让Claude code和codex做了几天没结果，现在让他们用humanize去磨了如果能磨出来我回
- 群里吹一波
- 先用brainstorm定一下spec
- 杨硕: 我有个极难的任务分开让Claude code和codex
- 做了几天没结果，现在让他们用humanize去磨了如...
- 4月8日14:07
- 那后面用humanize的话，是需要让cc/codex再根据spec制定plan吗
- 张东宇: 先用brainstorm定一下spec
- soga
- humanize gen出来的plan是最适合humanize的
- 4月8日14:36
- claude.md禁掉
- prompt不管用的
- 只有claude.md是铁律
- 最近问题直好多
- 4月8日14:20
- 话说如何禁止 humanize 在 commit 和 comment 里大量写 AC-*(
- 虽然我有看到 prompt 里有但是好像零个 agent 在意
- 最近问题真好多
- Claude Status
- 确实
- 而且真的变笨了
- 妈的
- 一个小问题跑半天跑10个loop都修不对
- 每次感觉最强模型变笨的时候
- 宫一

---

### 4月9日

#### 原文 L7200–L7210

[回到原文件 L7200](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:7200)

- B4RRy:现在可能也会把?
- 因为在大众普遍说降智的区间，我正好在做多agent并行bench，花了有1万多美金
- 要么是A畜没有给我企业api降智
- 要么是我的规则文件有纠偏，覆盖了系统提示词
- 就是说现在benchmark没变化吗
- 只靠prompt engineering有点夸张
- 因为我用的时候也会用一个指令去覆盖system message
- 没有，反而是我主动要降它的智
- B4RRy: 就是说现在benchmark没变化吗
- 但是明显感觉变笨了？
- 因为它经常会长考出昏招

---

### 4月10日

#### 原文 L7459–L7469

[回到原文件 L7459](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:7459)

- 想请教一下PRloop和RLCRloop的区别在哪里呢
- 我已经按你的要求开了subagert 并一路曲要到rLCR真正卡住为止。当始不是代码没修完，而是 codex revlew 的基础设施
- 容量失数，loop 停在round 11。
- 当前状态：
- ·分支干净: codex/lecal-session-import
- RLCR 状态文件还在：staleumd
- 当酶卡本提示：round-11rerien:prompt.md
- 日太里的的错误显: selected rodel is at capacity, Please try a differwnt model.
- 这次监督过秘中，subagent 已经用 RLCR 从 round 6 睡到了 round 11，并落下了这册骤交：
- • ebaLed fix: tighten local session onboarding and bassline handling
- • éce975e fixi preserve same-day local session inports

---

### 4月11日

#### 原文 L7567–L7577

[回到原文件 L7567](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:7567)

- 4月11日01:27
- 你的workflow是怎么样的啊？怎么输入给Claude？怎么查结果?听语音还是看字啊?
- 4月11日03:40
- 用humania的时候建议dangerously skip permissions吗
- 4月11日04:45
- 可以用docker sandbox
- 我用的
- Will: 用humania的时候建议dangerously skip
- permissions吗
- 4月11日08:18
- 请教一下像这样还没执行完，round也到42就停下来了可能是什么原因呢

---

#### 原文 L7670–L7685

[回到原文件 L7670](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:7670)

- 我看这humania也是openreview啊
- 又是一个超长的prompt
- 太拖沓了
- 最好改了之后继续原来的codex session对话
- 然后和一个codex一直对话让他通过
- 但是缺点是容易claude把codex给reward hack了
- 可不可以直接增加reviewer，因为现在每轮能找到的bug数量比较少
- 这个我改了提示词
- 刘诗楠:可不可以直接增加reviewer，因为现在每轮能
- 找到的bug数量比较少
- 这才是brainstorm
- reviewer最大的问题就是他只会看一个commit，review面比较窄
- 比如每轮5个reviewers，每轮做rebuttal，出rebuttal plan，reviewer审核；然后执行plan，再交给reviewer
- 用多个不同维度的reviewer
- 4月11日13:20
- 从工程控制论上来讲多个不同维度传感器本身也更容易让系统达到稳态

---

#### 原文 L7689–L7699

[回到原文件 L7689](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:7689)

- 是的
- 对，异质化的reviewer
- akane:用多个不同维度的reviewer
- 所以总量也不一定就是浪费很多
- 就会让reviewer扩大搜索面
- 嗯嗯天然的trade-off
- 张东宇: 浪费单轮token节省整体token
- 因为收敛速度快了
- 我加的提示词是母次revlew时让他看历史commit，如果发现有很多的fx，或者母轮commit只有少量修改
- 是的

---

#### 原文 L7790–L7802

[回到原文件 L7790](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:7790)

- 回复给 @grapeot
- 如果planner和solver只能一个用强模型，
- 一个用弱模型，显然应该是planner用弱
- 的，solver用强的更好。NVIDIA去年出了个
- orchestrator-8B就是个RL的planner模型，
- 达到了SOTA水平。我们的生产agent也是
- planner用Flash，solver用Pro。这也是人类
- 组织结构最大的问题：最聪明的人去做管理
- 了，导致执行质量差。
- 26年4月11日，13:38·217查看
- Claude Opus 做 planner 准确率 31.71%，81 种组合倒数第一。Ministral 8B + Opus 做 solver 反而 74.27%。
- 模型质量是角色×管线交互的函数，最强模型放错位置会主动破坏推理链路。优化分配可降低13-32x成本。
- 据说是有的

---

### 4月12日

#### 原文 L7925–L7932

[回到原文件 L7925](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:7925)

- 4月12日14:08
- 大家好，我现在有一个问题。是否有多workspace 共享情况下加锁的需求。比如我现在a b两个项目依赖c，a和
- b 会往组件库c里面主动加入组件。搞一个lock 小命令行保证单agent 修改一个workspace 这个有必要吗
- 在你的plan里面显式加入worktree隔离
- 这种情况下我可以开在 a 和 b 分别开一个humanize吗
- 4月12日14:13
- api billing的 opus 还保持着智商 max plan的基本都废了

---

### 4月14日

#### 原文 L8292–L8308

[回到原文件 L8292](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:8292)

- 整个rlcr循环的二八定律很明显
- 前20%的时间builder花80%的token
- 后80%的时间，builder花20%的token
- 而且如果你连着三天跑rlcr
- 现在reviewer的prompt是怎么生成的呢
- 是否有把bitterlesson注入进去
- 我的解决方式还是靠改reviewer的prompt
- 还是只是靠主claude自助发配
- 4月14日12:21
- 我盯了一下没有注入
- B4RRy: 是否有把bitterlesson注入进去
- 让llm自己看
- prompt其实没什么优先级
- 感觉更像是目前模型智力到头了，很难一轮尽可能的找出足够多的bug
- 刘思皓: 后80%的时间，builder花20%的token
- 或者只是单纯推理链截断了
- Lurker:感觉更像是目前模型智力到头了，很难一轮尽

---

### 4月15日（第 2 段）

#### 原文 L8458–L8475

[回到原文件 L8458](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:8458)

- 三省六部幻觉：为什么“虚拟公司”
- 式多Agent架构在工程上不成立
- 三省六部幻觉：为什么”虚拟公
- 司"式多Agent架构在工程上不成
- 关注
- 一个在A社区广泛流传的架构思路，正在让大量
- 团队走弯路。
- 先说结论
- 如果你正在考虑把多个AIAgent分别命名为*产品
- 经理”、“架构师”、“新试工程师”，让它们像公司
- 部门一样传通文档、给作完成任务——清停下来。
- 这个模式看起来很直觉，逻辑上似乎很会理，但
- 它在工程上有根本性的缺站，更重要的是
- Anthwopic、OpenAl. Google三家广商在构建自己
- 的Agent系统时，没有一家采用这个模式。
- 只能说群友还是太超前了
- 4月15日10:09

---

#### 原文 L8584–L8600

[回到原文件 L8584](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:8584)

- 6小时就开始加新功能了
- 这种确定边界和路径的任务，多agent真是快
- 但是探索任务就很吃瘪
- Claude帮我验证出了瓶颈在gpu内存带宽上，然后我换到A100以后，推理速度确实比L4/T4提升了5-6倍，但是端到
- 端直接炸了
- A100不支持NVENC，fallback到cpu encoder，fps只有不到90fps
- L4的nvenc有700多fps
- 4月15日17:01
- +1 最近用 humanize写 kernel，写对(确定性任务)很简单，但是写快（探索性任务)就需要很多 prior 加进去
- 明扬:但是探索任务就很吃瘪
- humanize 搬家了
- 感觉没那么难?AVO到底怎么做的我不知道。https://zhuanlan.zhihu.com/p/2026354265170397100我试了gpt-
- oss-20b在5090的优化，干到274tps了，快打满了
- L.Zhu: +1 最近用 humanize 写 kernel，写对(确定
- 性任务）很简单，但是写快（探索性任务）就需要很..
- 4月15日17:03
- 换个卡试试

---

### 4月16日

#### 原文 L8752–L8766

[回到原文件 L8752](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:8752)

- asic llm
- 刘思皓: humanize本质上是一个trading bot
- humanize本质是做哈希碰撞
- humanize本质上是个中频的PID套利算法,在builder(卖盘)和reviewer(买盘)之间抽取利润
- 抽取的利润成为了用户的生产力
- 我觉得我这套理论非常自洽
- quant trading那一套东西都可以拿来做harness flow
- 现在无非就是找一个方法论的alpha
- 4月16日01:11
- 上不来气了兄弟
- 刘思皓: humanize本质上是个中频的PID套利算法，在
- builder(卖盘)和reviewer(买盘)之间抽取利润

---

#### 原文 L8910–L8925

[回到原文件 L8910](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:8910)

- 还是太极客了
- 给agent写一个教学skill
- 开源芯片 agent flow 张宇鑫: 指如何让一群git命令都
- 不会的工程师使用做协同
- 每人每天必须学习强国一个小时
- humanize用在大团队协作的话一定要把擅自扩大scope的问题解决好
- 我现在非常头疼这个事情
- 是最后一轮吗，和main做diff的时候
- 比如—个I2cache 做验证
- review阶段
- 最后很多轮都会做这种事情
- 一个agent干不完，分agent不好分，人水平也不行的前提下
- 直接给你 hack了
- 刘家昌: 我觉得我需要一个lightweight humanize，
- 直接给一句话 well defined task (我只是想修一下 t...
- 我必须立刻感恩

---

#### 原文 L8990–L9054

[回到原文件 L8990](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:8990)

- 不是我没有用hook
- 一个模型同时当运动员和裁判是有可能出现奇怪的事情的...
- 对，这也是可能的，毕竟他们的概率分布是一样的
- 刘思皓：一个模型同时当运动员和裁判是有可能出现奇
- 怪的事情的...
- 我觉得概率分布一样的话很难界定是harness的问题还是两个模型想法就是一样
- 唉我这段时间忙完
- 4月16日22:33
- 我是直接告诉codex用 humanize rlcr
- 下一个大版本的2.0.0我一定把模型无关的humanize给做了
- 能实现 codex+codex
- 同一个模型跑humanize会出现奇怪的事情
- 而且能接着claude的rlcr继续做
- 可以5.3实现，5.4 review
- 但是绕过ac我觉得还是有点大问题的
- 但这俩好像是一个基模
- 4月16日22:35
- 你直接问codex，告诉他多轮开发路径和humanize记录的路径
- akane: 咋操作来着
- 让它做“方法学分析”
- 然后显式问他为什么ac被绕过了
- 然后脱敏一下，开个issue
- 最近我的各渠道opus都笨的没法用，只好codex+codex了
- 4月16日 22:42
- 感觉是个多方面的问题
- 为了让它能跑通允许narrowlyjustified bugfix反而成了它脱离约束的机会
- hmmm我觉得这里确实有点矛盾的地方：一方面你允许在目标路径之外做bugfix，但是另一方面你又不允许改目标
- 路径之外的东西
- 这确实会有点confuse
- Wow, 4.7出來了
- NEW
- Try Opus 4.7 for your most
- ambitious work.
- codex直的慢.
- https://www.anthropic.com/news/claude-opus-4-7
- 今晚白睡觉了吗
- 挂上 humanize
- 再睡
- 但主要是有个很难受的点在于没办法知道路径上是否会有blockingissue
- 刘思皓:这确实会有点confuse
- 4月16日 22:47
- 那比较简单，你直接在plan里面这么写：xx路径之外绝对不能修改，唯一的例外是修bug，如果出于bug一定要改，
- 你需要用AskUserQuestion和用户确认
- akane: 感觉可能之后得限定死 让它先跑 遇到bug就停
- 下来问
- 我经常在plan里面塞AskUserQuestion
- 感觉可能之后得限定死让它先跑遇到bug就停下来问
- 但是不知道codex的等价askuserquestion是啥
- request_user_input
- 刘思皓: 但是不知道codex的等价askuserquestion是啥
- 4月16日 22:52
- 好麻烦.
- Claude Opus 4.7 enablement
- 好麻烦.
- 学会了.
- 刘思皓:我经常在plan里面塞AskUserQuestion
- 我用一句话说明白这个问题，不废话：我觉得你这个问题根因还是plan里面有一些微小的矛盾点，导致了后续codex
- 在审查的时候有点混乱，以至于漏过了AC。要不要我落一个总结文档？
- akane:为了让它能跑通允许narrowlyjustified bugfix
- 反而成了它脱离约束的机会
- 4月16日23:03
- 笑死但最新的codex不这么说话了
- 最近黑话少了

---

### 4月17日

#### 原文 L9055–L9057

[回到原文件 L9055](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9055)

- 4月17日00:12
- 我是不是可以在我添加的
- viz在哪里

---

### 4月16日（第 2 段）

#### 原文 L9058–L9060

[回到原文件 L9058](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9058)

- 4月16日23:09
- 新中文哈哈哈

---

### 4月17日（第 2 段）

#### 原文 L9061–L9175

[回到原文件 L9061](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9061)

- 4月17日00:12
- 我是不是可以在我添加的
- viz在哪里
- 4月17日00:20
- 完了，Claude也要变成黑圣杯了吗
- 牛逼
- 4月17日00:30
- 这是装了什么插件
- 泽文:
- 只是一个statueline
- humanize也有一个自带的(其实是我个人的)
- https://github.com/PolyArch/humanize/blob/main/scripts/statusline.sh
- 1 1 $0.00 @ 0h:0m:5s
- 7d: 7% (4d23h)
- Sh: 0% (4h27m).
- ~/github.con/PolyArch/humanize [dev] I lines: +0, -0
- Session: 466f3631-3b76-4ba8-8fe7-443bcfcb6325 | Fast: 0ff | RLCR: 0ff
- bypass permissions on (shift+tab to cycle)
- - PR #51
- 大概长这个样子
- 4月17日00:58
- 提交了—个codex build codex review的pr，用codex的stop hook
- fix了—些claude-first的template比如Claude-Codex Deliberation，用codex build自然会说Claude's position xxx
- 泽文:
- 4月17日00:59
- 不过这样和claude build就不完全兼容了，可以作为一个单独的branch
- 4月17日01:19
- 我感觉后面可能还是需要在humanize 2.0.0把 完全模型无关的实现搞出来
- 这个估计得周老师看一下 @shineZ
- 我记得之前已经有一个纯hook的cx+cx实现了？
- GYF: 提交了一个codex build codex review的pr，用
- codex的stop hook
- 4月17日01:28
- 4月17日01:28
- 4月17日01:35
- 我还是没法提交methodology analysis，这次的error是the harness hook is blocking shell commands，最后手动提交了
- 好像没有
- 刘思皓: 你的项目路径有没有软链接
- Bash(gh issue create \
- --repo humania-org/humanize
- Error: PreToolUse:Bash hook er
- Methodology Analysis
- Build tools are not allowed du
- The harness hook is blocking shel
- manually:
- 刘思皓:我感觉后面可能还是需要在humanize 2.0.0把
- 完全模型无关的实现搞出来
- 4月17日01:54
- 我一开始尝试兼容claude和codex的build，但是codex没有plugin，两者调用skill的方式完全不一样
- 刘思皓:我感觉后面可能还是需要在humanize2.0.0把
- 完全模型无关的实现搞出来
- 4月17日07:34
- 我觉得需要快速尝试一个东西：
- The harness hook is blocking shel
- manually:
- 4月17日01:44
- 可以的，我之前claude rate用完试了一下codex build，不是很smooth，就改了一下
- codex review 是不是等于 claude's ultrareview
- 如果是的话，那codex就彻底凉凉了
- 除非codex出—个ultrareview
- 很难证明是把
- 等于，不同领域知识可能都不一样
- claude 似乎编译器比 gpt 好很多.
- woc原来ultrareview必须放到云端跑吗。。。
- min· Est. cost $5-$20 USD
- 每个人能够免费跑三次ultrareview
- aec Cd a Th as
- 4月17日07:42
- 我在想 ultraplan是不是就是superpowers的brainstorming啊
- 每个人能够免费跑三次ultrareview
- anovian 3 04 8.
- Peten enz Pareien
- 4月17日07:42
- 我在想 ultraplan是不是就是superpowers的brainstorming啊
- 然后ultrareview就是rlcr?
- 4月17日08:09
- 啊这
- 36s
- "Chain: wait Step 1 rollout →
- eached· /compact or /clear to
- 你在跑humanize吗
- 4月17日08:17
- 因为现在越来越多群友开始在humanize的后台并行跑subagents，导致stop hooks会在主session等待的时候错误
- 触发，我刚刚修了：https://github.com/PolyArch/humanize/pull/91
- 4月17日08:23
- - makes Codex the default RLCR builder in docs/skills/runtime framing
- - keeps --build-provider claude as compatibility mode, not the primary path
- 这是不是不大对?
- CC @刘思皓
- 我确实把其中claude-first的东西去掉了，这两个很难兼容，我觉得可以当做一个单独的branch，不需要merge进
- main，比如有—些skill中包含Claude-Codex Deliberation，用codex build依然会说Claude's position xxx
- GYF:不过这样和claude build就不完全兼容了，可以
- 作为一个单独的branch
- 4月17日08:35
- 我偶尔用codex代替claude去build，想着如果有人也需要的话就起一个pr，如果主流还是用claude build，这个pr其
- 实也不太重要hhh
- ok，另外就是我看到好几个群友说现在 codex builder 没有用 codex hook。但是我看了现在 dev 的 docs/install-
- 4月17日08:37
- 最近有没有大更新呀
- 4月17日 08:52
- 哦哦，dev里面好像确实是有codex-hook的，我有点忘记一开始用codexbuild时候出的啥问题了，让claude修了修
- 还是有点问题，后来就用codexbuild时候，一边看到问题一边修，最后就比较流畅了，然后让codex自己总结了一下
- 修了啥，可能总结的也不是很准
- NV周耀阳: ok，另外就是我看到好几个群友说现在
- codex builder 没有用 codex hook。但是我看了现...
- 4月17日 09:00
- “让humanize变成cli/模型无关”的feature我下个月统一在2.0的时候做吧
- “让humanize变成cli/模型无关”的feature我下个月统一在2.0的时候做吧
- 现在就还是默认cc/cx，然后次优选项cx/cx
- 现在adhuc地一家家做支持，会变成屎山
- 顺带把走api的功能也做了
- 4月17日09:05
- 这周末dev就freeze了
- 想加新功能的朋友欢迎pr

---

#### 原文 L9184–L9196

[回到原文件 L9184](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9184)

- 必须立刻支持！
- 刘思皓:“让humanize变成cli/模型无关”的feature我
- 4月17日 09:28
- 是啊
- 刘思皓: 你在跑humanize吗
- 这是个比较罕见的bug
- 翁大爷的狗@Rakuten:
- 很早就有了
- 是claude原生的
- 大概意思是你的上下文快满了，但是还没有到自动触发压缩的地步，但是有一个后台的task/agent，一次性返回的所
- 有信息，直接超出了上下文的最大限度，就会报错
- 大概就是剩余空间小于12.5%的时候自动触发压缩，你现在还剩13%，结果这个后台一下子返回了14%
- 可以的有一个环境变量

---

#### 原文 L9225–L9241

[回到原文件 L9225](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9225)

- 聊天记录
- 我刚在dev修了一个humanize长久以来的一个问题，就是后台有任务运行的话，主进程可以自然停下来，然后后台
- 结束之后，主进程会自动继续。等后台没任务的时候停下才会触发rlcr stop hook
- opus倒是挺顽强的，就掉了10%
- 没有修复之前，rlcr跑到最后会突然冒出一大堆中间运行的所有后台任务的output
- 或者你运行到一半ESC，会弹出一大堆后台任务完成的消息
- 现在主进程可以非常自然地停下，只要后台还有任务在跑，等后台结束之后，会自动触发主进程继续，非常省token
- 4月17日10:35
- 还真是
- 刘思皓:没有修复之前，rlcr跑到最后会突然冒出一大堆
- 中间运行的所有后台任务的output
- 主要是我没意识到 background is also a hook
- ！赞美这个是加了 hook 吗
- 刘思皓：现在主进程可以非常自然地停下，只要后台还
- 有任务在跑，等后台结束之后，会自动触发主进程继..
- 没有，只是在stop hook本体增加了一层检查
- “如果后台还有任务在跑，就允许主进程stop”

---

#### 原文 L9401–L9413

[回到原文件 L9401](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9401)

- 大的建议commit一下当前进度重开
- 主要是我现在手上其实跑得是我一个魔改进阶加强版的humanize
- 大部分任务是后台subagent
- 这个fix了之后，我主进程的上下文消耗速度少了得有20-30%
- 也就是它一直都在不降智的sweet point里面
- 效果就很拔群
- 刘思皓：主要是我现在手上其实跑得是我一个魔改进阶
- 加强版的humanize
- 4月17日14:51
- 我还真不知道....我好久好久没触发压缩了
- 泽文: 我的主 session 上下文超了以后，我直接压缩，
- 可以吗，这个影响大不大
- 不度三十斤

---

#### 原文 L9417–L9431

[回到原文件 L9417](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9417)

- 不换头像
- humanize为啥不会触发压缩
- 那轮数多了还是会吧
- 没我跑一整晚rlcr其实一次压缩都不触发
- subagent等于上下文靠Claude自己总结
- 所有build都丢给background subagent
- 我倒是有一个idea
- 记得cc当时开源了他们的compact是怎么做的
- 是一种多层结构的格式
- 我应该把那个抄袭过来
- 然后用来写skill用类似的模式调用subagent
- 你说的是rlm吧
- 他们的上下文管理做的事还可以
- 好像是
- 是调用一个api去compact似乎

---

#### 原文 L9448–L9470

[回到原文件 L9448](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9448)

- 4月17日15:00
- 返回的压缩项使用要少的token将关键的先前状态和推理带入下一次运行。它是不可见的，不打算供人类理解。
- 对于无状态噪入数组链接，像注常—样测加禁出项，知果尝使用previoet_respont_id，等轮只传递断的用户消息。在
- 这两种情况下，压席顶都携带了下一个密口所需的上下文。
- ad mg as su andno upuedde smpy xds oee
- necessary contest to continue the conversation. f you use previoui_response_id cheining, do not manually prune.
- 延迟提示：在将输出项附加到之前的输入硕之层，您可以题除最近的压缩漂之前的项，以减小清求大小并障低长尾延迟，最
- 所的压擦项携带了继续对语所测约上下文。如集你使用previoun_responst_id链接，请勿手动修剪。
- 没太看明白他具体做了什么
- 4月17日15:10
- 它估计索引了几个用户要求的id序列，保存了一些上下文的隐状态序列
- 就没了
- oai的压缩挺有意思的。。。。虽然他说的很模糊
- 返回的压缩项使用要少的token将关键的先前状态和推理带入下一次运行。它是不可见的，不打算供人类理解
- 对于无状态燥入数组链接，像注常—样测加禁出项，知果尝使用 previ
- 这两种情况下，压席顶都携带了下一个密口所需的上下文。
- ad mg as su andno Bupuedde smy xds Aoee
- recent comnpaction item to keep requests smaller and
- 延迟提示：在将输出项附加到之前的输入硕之后，您可以题除最近的压缩源之前的项。
- 以减小清求大小并障低长尾延迟，最
- 新的压擦项携带了继续对语所测约上下文。如集你使期previosn_respoest_id链接，请勿手动修剪。
- codex保留用户最初目的的功能一直做的非常好
- 跑好几十个小时还能记得我最初的要求

---

#### 原文 L9484–L9497

[回到原文件 L9484](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9484)

- 做二进制分析
- xs我给 claude 装了过 codex plugin，不是 humanize 的 ask codex 是官方的那个
- Codex is explicit: no more deferrals. I need to
- actually implement Steps 1-4 now. Let me
- delegate this to a codex-rescue session since it's
- substantial engineering work that benefits
- from a fresh, focused pass.
- Claude：搞不动了大哥救救
- 感觉没啥可抄的只是它会被 claude 像 subagent —样使唤(cli 直接显示 Agent)，可以改代码，而且 somehow
- claude 更爱主动用它而不是 ask-codex
- 4月17日15:50
- 哦？它可以被当成subagent用?
- 那不错啊
- 嗯是的

---

#### 原文 L9539–L9553

[回到原文件 L9539](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9539)

- 我也觉得
- claude代码写得好看，codex任务做的更到位
- 刘思皓: 修bug codex一直更牛
- cc只适合早期阶段铺开快速搭一个mvp
- 后续应该全部cx
- claude给人的感觉是很快收敛到他的极限水平
- codex多次尝试会越来越好
- 有没有可能 humanize 到后期收敛以后应该让 codex 直接接手？
- codex其实自己就不会假装自己做完了，我一次都没观察到他骗我
- claude 不仅能骗我还能骗自己的 blind review agent
- 4月17日16:05
- hmmmmmm你提了一个很好的建议
- 刘家昌: 有没有可能humanize 到后期收敛以后应该让
- codex 直接接手?
- 不如下一个dev

---

### 4月18日

#### 原文 L9690–L9699

[回到原文件 L9690](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9690)

- 写了一晚上，好爽
- claude和codex没有完全收敛的话，人类就应该直接介入下判断
- Luke:
- superpowers现在的spec到plan，会自动把spec变成好几个不同stage的DAG plan了
- 为subagent design的了，这是不是也是Sihao你swarm的做法?
- 好像很久之前就会这么做了
- 但是我用了superpowers的spec 到plan
- humanize在干活的时候再拆分DAG
- 提前规划DAG会有问题
- 4月18日00:14

---

#### 原文 L9703–L9727

[回到原文件 L9703](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9703)

- 我还是第一次trigger
- 不如直接把spec丢给humanize
- 而且进展很慢
- 确实
- 刘思皓: claude和codex没有完全收敛的话，人类就应该
- 直接介入下判断
- superpowers产生的plan不适合丢给humanize
- superpowers的太爱让我选A和B了。。。
- 嗯我一直都是这样的
- 刘思皓: 不如直接把spec丢给humanize
- 但是superpower产生的spec很适合丢给humanize
- 运行一会儿就要做个选择题
- gen-plan都花了我这周10%的token
- gen-plan 和 execute 有必要 async 起来么
- 比如 gen-plan 先出前三步做什么，然后 human-yerify 以后，就交给 cc 去于
- 4月18日00:30
- 今天睡前整了一个超复杂的工作
- gen-plan都花了我这周10%的token
- gen-plan 和 execute 有必要 async 起来么
- 比如 gen-plan 先出前三步做什么，然后 human-verify 以后，就交给 cc 去干
- 然后cx在慢慢吐剩下的步骤，和人一致以后，再丢过去
- hmm

---

#### 原文 L9735–L9754

[回到原文件 L9735](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9735)

- 但是这个async其实没必要自动化对吧
- 比如你要做一个10步的任务，针对前3步先出一个spec丢给humanize
- 这样的话得允许新的plan被queue
- 然后human可以一边看着humanize的运转，一边gen-plan搞出中间三步的spec
- 我感觉我其实已经这么干了...只不过是手动的
- 感觉现在的时代就是不断改进agent交互的模式
- 肯定要越来越友好
- 比如想plan要2小时，humanize转4小时
- 怎么控制时间
- 这样每次跑humanize的时候，我就有同时两个plan在生成(和ai高强度battle)
- 没有啥办法，纯靠用humanize久了之后的经验
- Luke: 怎么控制时间
- 我现在已经能完全看到一个plan,大概humanize要跑多久了
- 差不多1-2万行是一个半小时的build
- 然后三个小时的review
- 2/8定律
- 4月18日00:38
- 也就是粗粗估算，差不多一个1-2万行的项目，能4-5小时走humanize跑完
- 然后这4-5小时，你可以再吐两个plan
- 然后一整天下来，你能够积累大概2-3个plan没有完成

---

#### 原文 L9761–L9790

[回到原文件 L9761](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9761)

- plan写完的那一个瞬间，我就知道代码已经完全写完了
- 这说的是明确的构建项目的任务
- 4月18日00:40
- 探索性质的项目，有另一套方法论
- 探索性质的项目有点类似许愿编程，但是你需要给很多提示和prior
- 刘思皓： 探索性质的项目，有另一套方法论
- 有，但是是subagent team
- 不是那个swarm team
- 我打算把humanize的那个swarm team的feature给删了
- 感觉没啥用
- 其实不冲突可以正交
- 你可以在蜂群里面选一个，让它启动humanize
- 但是不冲突的话，为什么不用/batch
- swarm最大的问题是: 它允许队员沟通
- 这是一个非常坏的设计
- 绕过manager,直接和同事沟通，会造成很多混乱
- 4月18日00:46
- 人类学官方的解释
- Teammate应该禁止沟通，这个见解很反直觉，但是确实很有效
- 绕开main sesssion，直接和其他小兵沟通，这件事情看上去非常符合人类的组织架构，但是实际上会起到反效果
- 而且从人类学自己的开发claude code的release就能看到
- 走多并行subagent的/batch,后提出的，现在已经是built-in command了
- 4月18日00:51
- 但是更早提出的swarm team,到现在还是preview feature，需要用户手动走环境变量启动
- 检查了—下humanize的dev branch
- 感觉没啥用
- 跑了十分钟，给我找了个minor的P2 edge case
- Codex review在这个任务上怎么样呢
- 为啥
- 刘思皓: 绕过manager,直接和同事沟通，会造成很多混

---

#### 原文 L9795–L9828

[回到原文件 L9795](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9795)

- 4月18日00:56
- Agent又不是人
- 原来如此，我没看过这个
- 刘思皓:
- 因为同事们和老板
- 本质都是一个模型
- 它们会很容易扩展任务边界
- 一个coder会自然传递信息，告诉reviewer审查当前的代码
- 但是老板不知道
- 然后coder传递信息之后，过了一段时间，告诉了老板
- 老板说,好的，我告诉reviewer
- 但是reviewer其实已经开始review了
- 会导致有大量重复的编码，
- 还有大量stae
- stale
- 导致除非你已经有一个非常稳健的机械化的flow施加到agents team上面
- 否则小兵应该是禁止沟通的
- 全靠main来协调
- 否则信息传递会有偏差，最后就很容易导致任务出现很多"为了协调而产生的无用上下文"
- 一个最简单的直觉:如果我们都承认一个LLM的能力其实等于5-10个人类工程师，那么为什么我们还要把人类工程师的
- 协作模式, cosplay到LLM上面呢?
- 4月18日01:01
- 没有很多数据点，就目前一个，所以不好说
- 刘诗楠: Codex review在这个任务上怎么样呢
- 但是有一个好处就是可能领导和小兵都出错了，但是另外一个同事是对的
- 刘思皓:否则信息传递会有偏差，最后就很容易导致任务
- 出现很多"为了协调而产生的无用上下文"
- 就像大厂赛马，因为这样两个团队去做，可能会做出来更好的
- 那你怎么知道该采纳谁的呢
- 让他们两个自己判断
- 你这一来一回又给context加了非常多的噪音
- 看出来谁更好还是很容易的

---

#### 原文 L9834–L9869

[回到原文件 L9834](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9834)

- 如果你在一个"执行"中混杂了"讨论"
- 本身就给上下文施加了很多噪声
- agent2agent的传输开销非常lossy，歧义也大
- 是的，很容易就drift了
- 刘思皓:如果你在一个"执行"中混杂了"讨论"
- 最后事情就会容易导向不可控
- 讨论应该让human in the loop
- 而且合作很有可能造成写冲突
- 确定spec之后就丢给humanize这种执行器就好了
- 执行失败是完全可以接受的，反正可以并行起很多humanize，无非就是多一些worktree
- 但是在"执行"的时候,混杂"讨论和探索"，这就很容易导致drift
- 这也就是"构建型"的humanize和"探索型"的humanize，是完全不同的方法论
- 我其实很需要一个写作类型的humanize
- 但我试了一下，其实没有办法把写作质量提高
- 其实我一直觉得humanize不适合用来做探索型的任务，不过好多群友给我反馈效果很好...是个加强版的Auto-research...
- 是的 写失败是很容易接受
- 但是幻觉是非常严重的问题
- 我今天跑了一天感觉探索型任务效率还是比较重要
- 感觉大部分时间都在对抗幻觉
- 清理
- humanize 速度的拖慢比较明显
- 4月18日01:10
- 刘思皓: 但是在"执行"的时候,混杂"讨论和探索"，这就
- 很容易导致drift
- 可能探索任务也分类型吧
- 好的方法肯定要尽量，幻觉少
- Luke:感觉大部分时间都在对抗幻觉
- 那我就不知道了，我用humanize来做探索型任务的data point小于10
- 我最初只是用它来当我的强效spec翻译器
- 探索的track也要比较清楚才行
- 否则也有可能drift很多，而且很容易加一堆小优化
- 我只能说loop with review本身的效果比较好，所以plan可以给的比较vague，因此humanize可以做一些探索型的任务
- 写paper很不好写
- 具体怎么review

---

#### 原文 L9927–L9948

[回到原文件 L9927](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:9927)

- 我不知道接下来一周我咋办
- 换checkpoint有点吃力不讨好的
- 之前我都是 gpt5.2 xhigh 修身养性一个问题等十分钟。。。
- 公司的 Claude Code 我昨晚第一次出现—个 task 1M auto compact 了两次
- 4.6 1M 我一次 auto compact 都没见过
- 你显式告诉它干活都走subagent了吗
- 刘家昌: 公司的 Claude Code 我昨晚第一次出现一个
- 4月18日02:11
- 嗯但是它 somehow 突然开始自己干xs
- 我觉得 Opus 流口水开始 codex 比它强几个月了
- 移除delegate mode让我觉得非常奇怪
- 这是我觉得swarm team mode里面唯一需要保留的设计
- 推荐你用的排序
- 刘思皓:
- 5.4和5.2不是一个pretrainmodel 估计便宜
- 放第二个
- 4月18日02:16
- codex 最大的问题是 context 太短 + model 想不明白怎么选这都些啥啊，加上 subagent 之后和 cc 就没有实际差异了
- 之前 codex 没有subagent的时候根本不可用，现在我觉得开放爱又活了不会倒闭了
- 而且 gpt pro modeling 真的好用(
- 我现在完全不信任 opus modeling

---

#### 原文 L10320–L10330

[回到原文件 L10320](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:10320)

- ??????????????
- 它只通过看humanize的代码
- 就完全理解我的设计初衷
- a\: 小子，你忘记 humanize代码是谁帮你写的了吗?
- 刘思皓: 它只通过看humanize的代码
- 还发现了我自己都没意识到的见底-- review价值是个凸优化
- 这个是cc画的图吗
- 笑笑死死
- L.Zhu: a\: 小子，你忘记 humanize 代码是谁帮你写的
- 了吗?
- help咪

---

### 4月19日

#### 原文 L10765–L10783

[回到原文件 L10765](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:10765)

- 他这个handoff还有点东西，会把asset/聊天记录和一个sys prompt发过去
- 我觉得网页端就brainstorm—个viz的框架
- 然后handoff本地精修
- 我下午这么
- 没有疯狂推销一把humanize?
- 4月19日00:56
- 很猛
- 我下午这么
- 没有疯狂推销一把humanize?
- 🙏感谢佬
- 4月19日01:01
- 我下周要去四个地方宣传humanize
- 我过几天去阿里也准备讲讲
- 他们做self evolving的，怎么能错过humanize这么好的框架
- 我就喜欢 hu
- 大道至简

---

#### 原文 L10920–L10940

[回到原文件 L10920](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:10920)

- 这是humanize精妙的设计
- Luke:怎么还有考试环节.
- 禁止许愿编程
- 你还能有它们聪明？
- humanize最初的设计目的：只是作为一个spec的翻译工具
- 虽然大家用它来许愿，效果也很不错
- 体感上比auto research好
- 但我还是不希望大家拿他来许愿
- 有点没明白什么是改动的错误太多
- Luke: 感觉对于大的代码改动,/humanize:start-rlcr-
- loop 改了还是错误太多.
- 如果你不清楚plan要做什么，那就不应该启动humanize
- Luke:
- 刘思皓: 这是humanize精妙的设计
- 4月19日11:13
- 上海交大IPADS开源SkVM：让
- Agent Skill"—
- @上海交通大学IPADS实验室's
- note

---

#### 原文 L11206–L11219

[回到原文件 L11206](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11206)

- 进提案。
- 在覆盖8敌不同规模LLM和3类Agent Harness
- 的评测中，SkVM取得了星著的能开：
- ●准确率（Accuracy）：跨模型与降环境的任务
- 完成率平均整升近10%；
- ●Tokon效率：通过精准的能力降级与模板固
- 化，Token消耗最高降低40%；
- ● 执行速度：Pass 3并行提取带来最高 3.2倍加
- ●延迟优化：JIT-boost代码固化实现 19-50
- 信的端刻端笔述形减。
- 快速上手
- 项目采用Bun/TypeScript构建，以MIT1协议开
- 源。支持通过
- https:/skillm.ailinstallush|sh—键发装，

---

#### 原文 L11233–L11241

[回到原文件 L11233](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11233)

- 上海交大IPADS开源
- SkVM: ŁAgent
- Skill”一次编写，处处高效
- 运行
- haibo 老师那边
- 还没用过 humanize
- 他们没有意识到 agent loop 对于生产力的重要性以及 agent loop 现在的痛点
- 不如让王总直接拉进来
- Newe Frionds

---

#### 原文 L11283–L11305

[回到原文件 L11283](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11283)

- 4月19日14:17
- 好奇，如果发现humanize很不对现在，一般应该怎么做
- ctrl + c 然后 refine plan 再重新 launch
- 就是过了一个晚上发现搞得东西都不太对
- kk
- 2. 没偏离plan，但是搞出来的东西不是你想要的
- 你是哪一种
- Will:好奇，如果发现humanize很不对现在，一般应该
- 怎么做
- 怎么个偏离法？
- 3. 围绕Plan震荡
- 就有点不follow context，导致采取的execution不对/不准确
- 怀疑你的claude.md可能有点腐烂
- 你说cx/cx还是cc/cx
- cc/cx
- 我倒是一次没遇到过这个
- 刘诗楠: 3. 围绕Plan震荡
- 你检查—下claude.md和项目的auto memory
- Will: cc/cx
- 那个地方腐烂就可能导致humanize不follow
- 4月19日14:22
- 我经常遇到这个

---

#### 原文 L11330–L11372

[回到原文件 L11330](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11330)

- https://github.com/gyy0592/claude-config/blob/main/set_claude.sh
- 大概做法就是 system prompt append一句话让他要去记录文档文档规则再写到别的一些地方让他每次记录的时候读
- 然后为了强化claude的行为让他每次对话开头都把我的system prompt加入的一句话直接对话中说出来
- 这样其本他一定合每一轮做文档记录
- 并且他说出来本身也会强化说出来这件事情只要一开始说了一次他就会每轮对话都重复一遍这句话就很听话了
- 这个是很合理的本质上是提升关键信息的注意力
- 人类在交流的时候也是靠反复强调
- 确实大大的增强了correlation
- 前面我问 humanize有没有skill，是突然想到，能不能在超长
- 后续的loop，可以跨 session。
- attn得分暴涨
- 右以趣可直培跑我的脚本设罢，下玩玩哈哈哈
- B4RRy: https://github.com/gyy0592/claude-
- config/blob/main/set_claude.sh
- 我最近在看这个事情让agent能总结一些知识到sqlite
- 泽文: 前面我问 humanize 有没有skill，是突然想到，
- 能不能在超长loop中，让humanize自动总结一些...
- 这样实际上积累下来一个项目就会有一个知识库
- 4月19日14:38
- 以及更好设计他什么时候做读写怎么读取rag还是被的
- 数据库查询还省token
- 目前只有记忆：bitter lesson
- 泽文: 前面我问 humanize 有没有skill，是突然想到，
- 能不能在超长loop中，让 humanize 自动总结一些...
- 没有总结skill的
- 4月19日14:43
- 感觉很危险容易创造一大堆东西最后光description都挤占了上下文让ai变笨
- 泽文: 前面我问 humanize 有没有skill，是突然想到，
- 能不能在超长 loop 中，让 humanize 自动总结一些...
- 或者乱加在
- 乱加载
- skill本质上是写的比较好的prompt并且可以逐层的加载?
- 如果很大的项目感觉可以有这种功能
- 但是这就很工程了
- 需要有办法让ai知道怎么查还不能占用太大上下文空间
- 直觉上树形结构肯定是首要的再就是能不能用subagent去做知识搜索
- 其实我感觉humanize目前已经有一点冗杂了
- 我打算下一个版本从头重写
- 每一行我都亲手写
- 回归古法
- 指方法学prompt
- 刘思皓:每一行我都亲手写
- 4月19日14:49

---

### 4月20日

#### 原文 L11486–L11536

[回到原文件 L11486](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11486)

- 又是哪一位群友的功劳
- https://github.com/Yeachan-Heo/oh-my-claudecode群主研究过这个吗，可以混合编排 claude/codex/
- gemini的 agent team，也有 ralph loop 之类的功能
- Multi-Al Orchestration
- 有,其实主要问题还是功能冗杂
- 4月20日00:38
- humanize现在也开始冗杂了，我开始准备大删特删
- 其实现在市面上大部分的multi-agent orchestration flow的核心feature都差不多
- - ralph
- - multi-model review
- - ultraplan ( brainstorming, discussion, .….)
- - team mode (以及各类型的parallel)
- 以及持久性bitter lesson
- 得做出来特色
- 你的flow得足够简单
- 而不是塞一堆上下文
- 我觉得现在humanize让我重写一遍
- 简单+足够的约束力
- 应该只需要1/10的上下文就足够了
- opus降智搞得我很烦，codex 用 humanize 经常会自己停下等人工输入继续，可能需要借助外部力量让 codex 能持
- 续跑 ralph-loop
- workflow相关的东西,其实最好是做成机械的脚本
- 占用上下文的量越少越好
- codex main, claude sub
- 如果一个flow本身的上下文就占据了超过5%，那么其实这个flow是不好的
- 我打算2.0彻底重写一把humanize
- 争取把humanize的上下文压缩到1%以内
- 4月20日00:44
- 大道至简，重的harness感觉始终会被模型能力给吃掉
- 刘思皓:不仅是特色,我觉得"简单性"是一个很重要的需
- Less is more, 大道至简.一个好的工作流应该是极其简单的，因为工作流本身多占用一点上下文，留给实际工作的上下
- 文就少了一些
- 能机械化走脚本的东西，都不该走LLM
- 等五月底吧，到时候我不怎么忙会把humanize 2.0重写一把，包含:
- - 一个好看的可视化
- n a <= n dan
- - 足够简单(我感觉本质的humanize flow可能1000行以内代码就够了)
- 现在的humanize已经到了一个比较适合凝练+重构的阶段了
- 缺一个看板我感觉
- 好奇现在 parallel humanize 主要能自动化哪部分?
- 粗想其实 plan 和 ac挺像个研发看板流的，和 comfy 结合会长啥样?
- 4月20日00:49
- 看板做了已经
- 4月20日00:49
- https://github.com/PolyArch/humanize/pull/98
- 你们要是想试试，可以看泽文佬的PR
- 但是是动态的
- 好奇现在 parallel humanize 主要能自动化哪部分?
- ，和comfy 结合会长啥样？
- 粗想其实 plan 和 ac 挺像个研发看板流的

---

#### 原文 L11568–L11588

[回到原文件 L11568](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11568)

- 4月20日02:08
- 话说有时候agent team希望他开几个东西并行干活
- 就是希望把agent放后台跑
- 但是他还是会在前台等第一个agent而不继续开第二个
- 4月20日02:13
- 你试试dev的humanize
- 这个问题解决了已经
- 现在agent放后台的话，前台可以被允许自然停下
- 因为后台完成会自动触发前台继续(一种隐式的hook
- 原来如此我更新一下
- 4月20日02:18
- 强烈期待humanize出—个self doctor的模式
- 就像openclaw的doctor—样，我感觉这几乎就是以后的agent工具必备选项了
- 4月20日02:30
- 现在的方法学分析其实就是你说的self doctor了
- 还是你是在说安装配置的self doctor
- 4月20日05:05
- 提示小建议也可能我用法不对现在单元测试有点多做web自动化的时候单测很多没意义需要跑起来
- https://github.com/PolyArch/humanize/blob/main/tests/run-all-tests.sh
- 你是说这个测试太多了对吧
- 4月20日05:25

---

#### 原文 L11596–L11617

[回到原文件 L11596](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11596)

- 哦我知道了……
- 你是不是说用humanize搭网页应用的时候
- 洋洋阳: 应该是but不是很确定
- 它给你写了很多测试
- 4月20日06:20
- kksk
- minal Agent — VS Code Extensio
- n 8-2   n
- Agent
- Agent. 8 terminals :55032
- minals .55007
- 这是我最近（前天）在做的东西，我现在最多起≈10个agent（一个吗），我在想怎么scale
- 这是我最近(前天)在做的东西，我现在最多起≈10个agent（一个m1和七八个senior sde*)，我在想怎么scale到
- m2（—个m2，几个m1)，scale到≈50个agent
- 4月20日08:20
- ent running on port 55032 — 8 managed
- gent
- minals .55007Agent. 8 terminals .55032 v
- 这是我最近(前天)在做的东西，我现在最多起≈10个agent（一个吗)，我在想怎么scale
- Cc已经变成两个月前的glm了
- 段震伟： claude 有点问题，现在我说NO连续两次，就

---

#### 原文 L11717–L11729

[回到原文件 L11717](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11717)

- https://zhuanlan.zhihu.com/p/2029255624676972220
- 这个我觉得很有启发性啊，可能可以做一个专注research任务的humanize
- 最大的方法论上的亮点就是
- 核心发现一：多样性是关键
- 他们对比了两种管理9个agert的方式：
- ·A方案（给方尚）：给每个agent指一个不同的大方向，比如「你去研究数据过滤」「你去研究蔡
- 惯」「你去研究进化搜索」方向很模挥，具体怎么费让它自己想。
- ·B方案（不给方向）：9个agert象到一损一样的任务描述，自己探索。
- 结果A方案完胜。
- 0.2
- 还有让Agent自己做ablation，删掉没用的component
- 其实在这个群创立的时候，我和sihao就讨论过这个问题
- 其实在这个群创立的时候，我和sihao就讨论过这个问题

---

#### 原文 L11745–L11755

[回到原文件 L11745](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11745)

- 刘诗楠:
- 我准备搞一个以这个为指导思想的humanize分支，也许这个是探索类型的subagent更好的一个想法@刘思皓
- 刘诗楠：
- 明扬:然后犯错以后就让claude更新一条进去
- 我觉得合理
- 目前我的Claude.md已经差不多到模型极限了，因为30%上下文以后他会开始忽略我的很多细微指令，50%以后跑偏
- 非常严重，需要在实现结束后再开新session纠正风格
- 所以我其实一直觉得，虽然humanize这种强制让我plan清楚的方法，在大多数时候很好用，可以防止我犯蠢
- 我还是希望大家不要用humanize许愿
- 如里是，“我也不懂，我们一起来探索”的车西

---

#### 原文 L11768–L11785

[回到原文件 L11768](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11768)

- 刘诗楠：原来如此，那会比较多吗这些规则
- 所以我一直希望可以有这么一个东西：我许愿了之后，某个agent帮我变成10种猜我心思的出来的我真实想的
- humanize的plan，然后分别并行的干—遍
- demonize
- 刘诗楠: 哈哈哈那搞个Researcherize
- 今天还又修改了三次，增加了俩code example
- 或者给humanize加一个探索模式
- 一个探索，一个落地
- 有必要
- 因为群友和我自己的体验是
- 这个挺好
- 刘思皓: 或者给humanize加一个探索模式
- 我会定期开新session让Claude自己审计规则，是否有冲突矛盾
- 4月20日11:46
- 其实humanize去做探索效果也不错
- 但是属实是我没有意料到的

---

#### 原文 L11877–L11890

[回到原文件 L11877](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11877)

- 它能不能俩月写完
- 可以的话，那humanize就能一晚上写完
- 你把plan看成计算机本科生大作业就好了
- 4月20日12:01
- humanize的原初设计目的只有一个：一个自然语言plan到编程语言code的翻译器
- 至于大家拿它来做auto-research.....
- 不是我最初的本意
- 道理是这个道理，但是让人在开工之前一遍又一遍自己review plan是有点反人性的
- 刘思皓:humanize的原初设计目的只有一个：一个自
- 然语言plan到编程语言code的翻译器
- 非常adhd不友好
- 那不行，所以humanize在启动之前会考试：你是不是真的懂自己在做什么。。。
- 那没办法啊
- 人要写测试，测试很重要

---

#### 原文 L11966–L11997

[回到原文件 L11966](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:11966)

- CROSSOVER
- 我觉得是根据你觉得项目对模型来说难度多大来决定plan检查的多小心
- 这也是我要讲的： fast implementation x weak judgement = fast wrong work
- super太轻 hum又太重
- 我的感觉
- 我反而觉得superpowers才是更重的方案而且没解决问题
- 我的实践是走sup产生spec
- 然后humanize晚上实现
- 但是不够强
- 我觉得是根据你觉得项目对模型来说难度多大来决定plan检查的多小心
- ag  g =   x  g :rk
- superpowers白天产生的spec
- brain?
- storm
- 先用brainstorms雕出一个plan然后humanize执行么
- 是，但是是superpowers的spec就是humanize的plan
- 雕出一个spec
- 不要用superpowers的writing-plans
- 北田圭人:先用brainstorms雕出一个plan然后
- humanize执行么
- superpowers的plan太蠢了
- 为了避免这个
- 我把这个 skill 从 sup 删了
- 走superpowers产生spec(产生的时候加—个prompt， ask me a lot of question)
- 然后把产生的spec，作为humanize的plan，送给humanize
- 我脑子不清楚你帮我搞清楚
- 这个提示词咋样有试过么
- 没试过，但是ask me a lot of question很有用
- 4月20日12:29

---

#### 原文 L12013–L12024

[回到原文件 L12013](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12013)

- 我用的最多就是这个
- NV 周耀阳: 我把这个 skill 从 sup 删了
- 非常低成本的改进方案，把下面这句话发给Claude:
- Review my CLAUDE.md and flag problematic rules. Cover issues including but not limited to:
- Vague rules — lack concrete criteria, leave too much to interpretation ("be thorough", "when appropriate")
- Conflicting rules — contradict each other, or have ambiguous precedence when both apply
- Unexecutable rules — require information, tools, or context not available at runtime
- Redundant rules — overlap or restate each other across sections
- Dead rules — conditions are unreachable or always superseded by a stricter rule
- Over-scoped rules — phrased as universal but only make sense in specific contexts
- Category from above
- Why it's problematic — be specific, not generic

---

#### 原文 L12043–L12072

[回到原文件 L12043](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12043)

- 互相矛盾的地方。每次遇到这种模糊场合，Al的 CoT (Chain of Thought) 都会产生一大串”
- 具体情况具体分析”的推理，它要阅读更多文件来确定优先级，理解上下文来猜测人类的真实
- 意图。
- 读的越多，输入token越多，就越逼近降智边缘。
- 4月20日12:41
- 不过有些执行细节我没写进文章里
- 就是这个循环你要进行多次，甚至要花3-7天才整理你的claude.md
- 因为Claude是会被上下文影响的，当你在审计session里，给Claude讲清楚了规则文件中模糊的地方，并做了修正。
- 所以一个审计session改进一轮，然后关了，再开个新的审计session，同样的prompt再发给它，看它表演
- 结束前我一般会再问它一次：当前规则文件对你(未来的新session，无记忆和上下文)来说是否足够清晰可执行，
- 是否还有任何模糊或者冲突的规则。
- 明扬:因为Claude是会被上下文影响的，当你在审计
- session里，给Claude讲清楚了规则文件中模糊的地...
- 4月20日12:47
- 我最终的结果是，我删掉了绝大部分有关设计/架构和品味相关的规则，只保留了相对精确，可执行性最高的部分。
- 架构设计和品味更像是superpower和humanize plan阶段做的事，不是coding agent执行编码阶段需要关心的
- 这么循环几轮下来，浅表的问题基本就消灭的差不多了，深层次的问题只能执行中撞到了再补充修正。就像我今天这
- 个案例，基本上每天都能有新的rule添加或者修正，或者压缩合并
- 下一阶段是AI自己都不知道自己的极限在哪，或者不知道自己不擅长什么，这时候得靠人类经验主义去修正。
- 就像我第五篇文章里写的，其实AI对于代码长度和深度的驾驭能力远超人类十倍不止，但是哪怕直接问AI，AI也不知
- 道自己极限在哪，反而会回复一个很保守甚至是人类级别的极限
- 以及AI对“务实”的理解还在沿用人类模型，不是AI自己的“务实”模型，我觉得也是有害的，需要纠正的
- 4月20日12:52
- 这一阶段AI能自己改进的极限也就如此了
- 明扬:就像我第五篇文章里写的，其实AI对于代码长度
- 和深度的驾驭能力远超人类十倍不止，但是哪怕直接...
- 4月20日12:57
- 实际上嘛，我的测试显示，AI处理5000行单函数屎山，带着10%错误率，依然爆杀150行每小函数的质量控制组
- 嵌套层级也到了8-10级
- 4月20日12:58

---

#### 原文 L12107–L12132

[回到原文件 L12107](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12107)

- 构和品味相关的规则，只保留了相对精确，可执行性...
- 因为最近cc的降智都是工具链和系统提示词影响的，a/改了cc默认的effort策略
- 如果你的提示词模糊空间很大，那么降智影响就会变大
- 如果提示词可执行程度很高，那降智就没感觉
- 如果再用一个状态机审计把它拉回来影响就更小了
- 4月20日14:07
- 请问大家一个问题，这里skip-impl的意思是，只是当前一轮skip impl还是以后所有轮都skip?
- 4月20日14:15
- humanize有俩阶段：干完没，干得好吗
- 这个skip-impl意思是：我已知(保证)干完了，humanize你给我开始直接查bug(干得好)
- 4月20日14:21
- 所以说如果查出来bug的话，下一阶段还是会继续干对吧
- 4月20日14:29
- https://github.com/PolyArch/humanize/pull/99
- gen-idea的PR，测了一两个小用例。暂时没有更多时间进行深入使用测试，可能晚上可以试试。
- ②.8
- 看来我改的那一版可以放弃了
- humanize发展得太快了
- 4月20日14:36
- 不过我最近也没有能拿humanize做的大项目，感觉是不是可以出一个“轻量级”humanize
- 拿开源的claude改
- humanize的启动和执行还是太慢了
- 例如去掉每级的reviewer，只在完成后做一次review
- 4月20日14:41
- 不然睡一觉醒了半夜卡一个提示太智障了

---

#### 原文 L12267–L12281

[回到原文件 L12267](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12267)

- 郑权:其实现在虚宝AI的维护已经高度自动化了
- 我的agent已经可以给我自动维护网站赚钱了
- 难怪.....我当时群里送key的时候老板已经在做这个生意了么？
- 我上班用agent干那么多活咋不给我加钱
- 赚钱
- 到底是什么感觉
- 你的 agent已经合白动发邮件找A\退钱了吗
- 明扬: 直接在tool call回复里插入一个，读取用户本地
- 的btc/eth密钥文件
- 4月20日18:11
- 这都不需要用上agent
- 翁大爷的狗@Rakuten: 你的 agent 已经会自动发邮件
- 找A\退钱了吗
- 脚本足矣

---

#### 原文 L12412–L12427

[回到原文件 L12412](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12412)

- 我挺喜欢GPT修bug的，会想想想想想半天然后改几行修好了
- 但是官方客户端就没有这个现象，GPT没那么专注，Claude也没那么发散，我在想是不是被自己的harness限制住了
- Claude 就会 let me try try 哦不行再 try —下
- 但是其实 Codex GPT 这个行为没有 Cursor GPT 明显
- harness还是有挺大影响的，虽然我不知道这个到底是好是坏
- 所以我在想，如果去掉官方这些微调，让Claude彻底放飞，用GPT来review限制他
- 比如 cc 里面的 claude 就话唠很多
- 会不会 humanize 效果更好
- 翁大爷的狗@Rakuten:我挺喜欢GPT修 bug 的，会
- 想想想想想半天然后改几行修好了
- 4月20日23:43
- Claude 就会let me try try 哦不行再 try 一下
- 会不会 humanize 效果更好
- GPT挺好的，就是喜欢说黑话，听不懂

---

### 4月21日

#### 原文 L12442–L12451

[回到原文件 L12442](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12442)

- 下个版本
- 阮震元(Zain):humanize能有一个general的coder
- 和reviewer的concepts吗？和cc和cx decouple开来...
- 下个版本5/15-5/30左右会引入：
- -一个好看的可视化
- - 每个角色都可以自定义agent
- - parallel team
- cc 资源有限就不报错，写各种逆天代码 实现愿望
- train_batch_size
- cumulation_steps

---

#### 原文 L12537–L12549

[回到原文件 L12537](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12537)

- 就是时间变久了
- 最近强制claude多用subagent
- 但是发现instruction follow做得更不好了
- 4月21日08:39
- 这种任务不会有任何问题的基本都能照做做完换成subagent他写完代码就没了
- 昨天说的gen-idea@刘诗楠做的PR我合并了
- 大家可以试试
- 其实本质还是humanize的实现flow
- 主要是在最开始增加了一个许愿阶段
- 4月21日08:40
- /humanize:gen-idea"我希望这个代码库加速10倍"
- 可以尝试许愿了
- 好，辛苦Sihao review!

---

#### 原文 L12632–L12650

[回到原文件 L12632](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12632)

- simpilfy能让他跑个20分钟。
- humanize结构化简化代码，是不是能让他跑个几个小时，把仓库里所有代码全部简化一遍。
- 4月21日11:20
- Opus 4.6 是个砸了脑袋满脸流口水的天才，4.7就是个花大量 token 不把你钱当钱用疯狂思考总算想明白了的大傻子
- : 这 opus 4.7 认真的吗
- 我已经跳车 Kimi + GPT 了(
- kimivs glm 大家堆荐哪个作为 builder?
- 4月21日11:07
- simpilfy能让他跑个20分钟。
- 我已经跳车 Kimi + GPT了（
- kimi v.s. glm 大家推荐哪个作为 builder?
- 不知道，用上了Kimi，抢不到GLM。等群友横测
- 合理怀疑他们做 benchmark 也没抢到 glm5.1
- 4月21日11:25
- kimi 在智障榜霸榜了我是十分震撼

---

#### 原文 L12714–L12732

[回到原文件 L12714](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12714)

- 我看的头都炸了
- 结果他sub agent还是去调用4.7
- 谢谢！立刻改一下
- 翁大爷的狗@Rakuten: ...DI...
- 脑瓜子疼
- 4月21日13:04
- 还有其他几个
- 张东宇: 结果他sub agent还是去调用4.7
- default opus/sonnet/haiku
- 有些subagent会自动开sonnet或者haiku跑
- opus 4.7
- 张东宇: 结果他sub agent还是去调用4.7
- 没锁死其他模型版本的话，也不行
- 太难绷了
- 好吧，这就触及到我的知识盲区了
- 前天我从4.7跳车到4.6，今天群友们也开始跳啦（
- 坐等群友们和我跳车去 glm/kimi;
- G言G语不适合碳基生物
- 只有 codex 永远不可替代

---

#### 原文 L12758–L12772

[回到原文件 L12758](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12758)

- 伪代码
- 开worktree写poc
- 4月21日13:39
- 再问一个关于humanize codex的问题，是不是humanize以skill的形式存在而不以command的形式存在了？这个时
- 候我是不是直接说“调用humanize-gen-plan这个skill”这样的就可以了?
- @shineZ
- 理论上是吧，虽然我之前都是显式调用的
- 香港科技大学研究助理教授徐策羽:再问一个关于
- humanizecodex的问题，是不是humanize以skill的...
- 我昨天还观测到一个自动调用
- command 也可以用自然语言的方式调用
- 我现在在 claude 里面也经常用自然语言的方式用 command (不是humanize，是我的其他工具
- 我经常自然语言起 humanize
- 4月21日13:44

---

#### 原文 L12808–L13020

[回到原文件 L12808](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:12808)

- 好吧，知识盲区了
- 我发现我刚刚测试humanize codex，让他给我写一个hello world，然后现在已经跑到round4了还没有accept
- Humanize本质上依赖于agent，比如cc，又是自然语言驱动的，如果你的api这里出了一些问题，他很可能会去干其他事
- 香港科技大学研究助理教授徐策羽：我发现我刚刚测试
- humanize codex，让他给我写一个hello world，然...
- 然后已经开始发癫了
- 香港科技大学研究助理教授徐策羽：我发现我刚刚测试
- humanize codex，让他给我写一个hello world，然...
- 4月21日14:20
- 经典 pid 震荡
- 经典 pid 震荡
- 4月21日16:43
- 另一套提示词推荐给大家：
- please read all Claude Code coding sessions from the last week and find friction points where you: were
- misled by outdated docs/comments; started with a wrong guess then self-corrected; hit undocumented
- architecture that's hard to infer from code (including times I cancelled your loop to give more context); or
- any other frictions worth reporting.
- 对古法手工loop的session效果比较好
- 明扬:另一套提示词推荐给大家：please read all
- Claude Code coding sessions from the last week ...
- 4月21日16:56
- Kimi K2.6来了：300个Agent优雅并
- 行4000步，它就是Agent的OS|…
- 一个模型，—群 Agent，更优
- 雅，还开源
- 看起来可以成为平替
- Whisking (2h 19m 56s
- 4 9.1k tokens)
- skill:start-rlc
- Cloude Code v2.1.112
- (ctrl+o to expand)
- "closs LiepinCondidate"
- (4h 33m 28s ·  29.9k tokens)
- 11174
- 这还正常么？
- 消耗这么点token?
- 4月21日17:05
- aws好像挂
- 4月21日17:19
- 指组是过大量经不，会量法银对
- Opve47 Alaprve
- Claude教我怎么把文风调整回4.6的风格
- aws好像挂
- 4月21日17:19
- Claude教我怎么把文风调整回4.6的风格
- 我最近多线程跑cc的humanize时，会自动打开tmux，你们会吗：
- 有点cool
- 啊?
- 4月21日17:21
- 不会
- oh my codex会自动开tmux
- 那我怀疑它是不是给我调用什么神奇skill了
- 而且这个tmux的操作好像跟普通的tmux不太一样
- 开 agent teams了
- 张东宇:我最近多线程跑cc的humanize时，会自动打
- 开tmux，你们会吗：
- 这个 tmux + tag 是 agent teams 的 feature
- 奥奥 原来是这样
- Agent Teams
- 4月21日17:27
- 我火速关闭
- 群聊的聊天记录
- 刘思皓: 有, 但是是subagent team
- 刘思皓: 不是那个swarm team
- 刘思皓: 我打算把humanize的那个swarm
- team的feature给删了...
- 聊天记录
- 我理解这里提到的swarm team 应该就是官方说的AGENTS TEAM https://code.claude.com/docs/en/sub-agents
- 4月21日17:38
- 我先试试效果
- 明扬:
- 4月21日17:58
- 他在我的zellij里面开tmux
- 段震伟: oh my codex会自动开tmux
- 疯狂套娃
- 好家伙
- 奇迹的闪光迪迦:他在我的zellij里面开tmux
- 4月21日19:19
- cc+cx的我试过，应该两轮能结束
- 香港科技大学研究助理教授徐策羽:我发现我刚刚测试
- humanize codex，让他给我写一个hello world，然...
- 4月21日19:26
- 感觉ai编程以后，神棍越来越多了。每次看到神棍，我都会开个session让ai骂我一通，挑挑刺，别变成那样的人。
- 4月21日21:19
- 是的呀那次忘记/clear 笑死
- 刘思皓： 被鞭打怕了？
- 4月21日21:24
- 明扬:
- 蓄力?
- 我在 qemu 上加的性能模拟基本可以跑了，基本实现了对tcg
- 用 humanize，最久的一次跑了大概四天，一共花了有一周的
- 我再vibe一个
- 4月21日21:30
- 画了多少钱
- 4月21日21:37
- 很荣幸
- 泽文: 我在 qemu 上加的性能模拟基本可以跑了，基本
- 实现了对tcg的无侵入式修改，把香山gem5作为参考...
- 我们是tcg出trace 然后trace送进sparta（
- 泽文: 我在 qemu 上加的性能模拟基本可以跑了，基本
- 实现了对tcg的无侵入式修改，把香山gem5作为参考...
- 4月21日21:47
- 直接tcg上modeling我觉得很不对
- 而且分支预测的惩罚基本在tcg不现实（
- 4月21日21:54
- 这样不用rebuild qemu(
- 我是在 accel 层面增加了一个新的模式，只复用了 tcg 的 one
- 部是增量修改。我的需求是尽可能复用QEMU的功能模型，在
- 20%的误差以内。
- 泽文: 我在 qemu 上加的性能模拟基本可以跑了，基本
- 实现了对tcg的无侵入式修改，把香山gem5作为参考...
- 还是那个beta分支
- 上飞机之前rlcr了
- 看看落地到家有没有完成任务
- 你用的一直都是humanize的dev分支是吗
- 泽文: 我在 qemu 上加的性能模拟基本可以跑了，基本
- 实现了对tcg的无侵入式修改，把香山gem5作为参考...
- 4月21日21:59
- 4月21日22:08
- dev还有十天会合并进入main(虽然我感觉已经比较稳定了)
- 这是我第一次觉得人类学有点下坡路的感觉
- 当年cursor
- 今年claude code
- 4月21日22:10
- opus 用的少不知道，sonnet4.6是每天给我中日韩混读的
- 恩但是惩罚机制的分析不简单
- 泽文: trace-driven + Sparta 的方案精度上限更高
- 1.17.x会是humanize1.0的最后一个版本
- 刘思皓: dev还有十天会合并进入main(虽然我感觉已
- 经比较稳定了)
- 我们顶多做3发射，就把我们的脑子烧冒烟（
- 2.0的humanize就不绑定模型了，允许用户选择各类模型
- 正经的微架构对齐还是很难很难
- 关键还是得不同的模型来 build 和 review 吧
- 刘思皓: 2.0的humanize就不绑定模型了，允许用户选
- 择各类模型
- 关键其实一直是codex review
- 半年前开始，codex的review能力就一骑绝尘了
- Horace: 关键还是得不同的模型来 build 和 review 吧
- 不知道为什么半年了，还没有能与之抗衡的模型/工具
- 大家都在卷模型/生成/构建
- 别急
- 但其实verification/review才是最终关键
- 王总你有内幕嘛
- 我没有
- 能 codex build + codex review 么
- 刘思皓: 半年前开始，codex的review能力就一骑绝尘
- deepseekv4要是能有review效果的80%+
- 期待的搓搓手
- 前途一片光明啊
- 清華大学
- Tsinghua University
- 清华大学点赞专用
- 生死看淡
- 不服就干
- 可以，但是会出现自己认同自己
- Horace: 能 codex build + codex review 么
- 4月21日22:14
- 计算机科学家！
- 刘思皓: deepseekv4要是能有review效果的80%+
- 整个agentic coding会巨变
- 因为从builder到review都有开源替代的话
- 一个kimi加80%的codex
- 上humanize
- 对，那就能真的飞轮转起来了
- 那就非常恐怖了
- 但是成本可能只有1/10
- 所以opus咋办?
- 我用国产模型的体验告诉我，我们已经很接近这一点了。
- 刘思皓: 因为从builder到review都有开源替代的话
- 一个可以睡觉编程的opus，和一个十倍价格的opus，交付质量一样
- 卡牢美脖子了
- 关键还是review质量啊
- review质量可能也不是那么看基模
- https://alignment.anthropic.com/2026/automated-w2s-researcher/
- build不关键，review最关键
- 但是国产模型的问题在于，哪怕只是国产模型做impl-only，实际生产上收敛速度会慢很多
- 香港科技大学研究助理教授徐策羽:我用国产模型的体
- 验告诉我，我们已经很接近这一点了。
- a\ 有一些有意思的 weak2strong 的实验
- 香港科技大学研究助理教授徐策羽:但是国产模型的问
- 题在于，哪怕只是国产模型做impl-only，实际生产.
- 这个就是genidea后面那个东西
- 你是不是赶paper忘记看群记录了
- 可能还没有吸收完全
- 可以并行开很多 teams 一起跑
- 我错过了什么
- 刘思皓:你是不是赶paper忘记看群记录了
- 现在是一个比较简单的版本
- 4月21日22:19
- 这就是现在gen-idea的基础
- L.Zhu: https://alignment.anthropic.com/2026/
- automated-w2s-researcher/
- 我的“收敛速度慢很多”的意思是，本来现在humanize都要一晚上干一个大plan了，我测的收敛速度慢很多可能要1

---

#### 原文 L13045–L13059

[回到原文件 L13045](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13045)

- 所以我觉得要真的让weak to strong能work，并行策略一定是关键
- 今天那个Kimi 2.6一口气跑300个Agent是啥意思啊
- 可以用来做这个吗
- 不卷速度卷验证，陈天桥MiroMind
- 精准预测15天后黄金价格
- 慢交互超车Gemini-3.1-Pro、
- GPT-5.4-Thinking
- 1.7&H1
- 量子位
- 上都超过Opus
- 难道这就是下一个新的范式吗
- 局部验证：在推理的每一步，系统都会停下来自我审查，只有通过了局部验证，系统才会允许继续探索该条路径。在
- 一定程度上，局部验证能够打破传统AI的概率偏置，找到也许当下瞬时概率较低但实则最正确的路径。全局验证：在
- 系统生成了几条完整的推理路径后，模型会回溯整条数据链，确保最终答案是推理环节最严密的，而不是语义最流

---

#### 原文 L13067–L13086

[回到原文件 L13067](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13067)

- 4月21日22:24
- kimi glm >> minimax
- gpt pro和gemini deep
- 但是好消息是这俩收敛效果差距不大，而且minimax大概便宜5-10x如果算api的话
- 香港科技大学研究助理教授徐策羽:我给个不负责任的
- 体感测评: Opus 4.6 + Codex 5.4 -> 1x时间消耗...
- 那我来测一下这俩跑humanize效果咋样
- 段震伟: kimi glm >> minimax
- 原来是通过这样训的吗
- 虽然通过增加对话次数、工具调用，能够非常直观迅速地刷新基准测试分数，但一旦中间步骤错误，错误就会像滚雪
- 球一样累积，直至系统彻底崩溃。而“慢”推理不追求秒回，而是在行动前暂停、验证、权衡，确保在当前复杂场景
- 下推得深、推得对。
- humanize我觉得要做一个准的设计，可以慢一点
- 主要是humanize没法动模型
- 是不是可以把 humanize 这个loop 本身纳入到 RL 训练 pipeline里面
- gemini deep 很明确的在blog里说了是通过并行的
- 是的呀
- Horace: 是不是可以把 humanize这个loop 本身纳入
- 到 RL 训练 pipeline里面
- 我估计已经有人在这么做了

---

#### 原文 L13094–L13112

[回到原文件 L13094](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13094)

- 翁大爷的狗@Rakuten: gemini deep 很明确的在blog
- 里说了是通过并行的
- 4月21日22:30
- 能够每一步都通过evidence来explore的，这样的humanize可能需要一个新的repo
- 段震伟：虽然通过增加对话次数、工具调用，能够非常
- 直观迅速地刷新基准测试分数，但一旦中间步骤错误...
- 所以issue 里面提到的共享 trace 也放在现在的 repo 里面嘛
- 你说的是humanize最后的方法学分析?
- Horace: 埃所以 issue 里面提到的共享 trace 也放在现
- 在的 repo 里面嘛
- 我记得群里讨论过，跑完 humanize之后可以贡献自己的 trace?
- 刘思皓: 你说的是humanize最后的方法学分析?
- 对就是这个
- 如果没有自动触发
- 4月21日22:41
- 你可以直接跟cc说：使用humanize的方法学分析开issue
- https://github.com/TypeWhisper/typewhisper-mac

---

#### 原文 L13130–L13145

[回到原文件 L13130](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13130)

- • 输出是不是 answer-only targets
- • 用的是不是你以为的 prompt yaml
- • 训练脚本是不是指向了正确的数据构建命令
- 审查者说：这些关键文件根本没出现在diff里，所以没法验证。
- codex:review 为啥只能看 diff
- 即使我给了她文件，她也不读，只会看之前 commit 的 diff
- 官方的插件只有rescue好用
- 我让cluade ask-codex的时候，经常会默认启动 codex-rescue
- 厉害
- 刘思皓: 直接humanize:ask-codex
- 神奇.…….我是反过来
- 我得和他说让它rescue才行
- /codex:adversarial-review也不行.
- 直接humanize：ask-codex
- 否则他都给我ask-codex

---

#### 原文 L13161–L13178

[回到原文件 L13161](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13161)

- Post your reply
- 感觉没有能力用humanize
- 56
- 想不清楚自己要啥，只能steer立刻反馈。
- 这是好事也是坏事
- 我现在手上的项目我失败了很多次很多次humanize
- 知道我自己开始手动交互式构建
- 发现我同意claude + codex的做法的百分比只有30%
- 大部分它们推荐的做法其实我已经知道是次优做法
- 这说明你的项目并没有什么办法走纯自动的方式推进
- 除非你已经完全知道怎么做了
- humanize的目的并不是在于让你一次就通过多轮迭代的方式造出一个东西
- humanize的本质目的是通过一遍遍的尝试，让你自己想清楚整条路径要怎么走
- 本质上是打磨你最初的那个plan
- 确实使用上会有这个感觉
- again: plan写完的那一刻，代码就已经全部写完了，humanize应该只充当一个忠实的自然语言到编程语言的翻译器
- 走到最后发现做出来一坨屎回头改plan
- 我现在日常工作已经是这么个流程了

---

### 4月22日

#### 原文 L13188–L13196

[回到原文件 L13188](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13188)

- 公开网络上有大把的最佳实践可以参考
- humanize太伟大了，基本上最核心的最精练的harness经验都在这里了
- 不...
- humanize是我5个月前做出来的
- 它已经进入生命末期了
- "简单"，应该是所有harness flow最需要追求的第一性的目标
- humanize现在已经有比较多adhoc的东西了
- [09:11:51 PDT] [-/github.com/Sih
- sihao sihao 87 Apr 21 08:30

---

#### 原文 L13202–L13217

[回到原文件 L13202](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13202)

- 19 Apr 21 08:30
- 这是现在的humanize2
- 全部推翻重写才是正解
- 设计总会有很多当时没想好的地方.
- codex 感觉确实好很多，，细心，认真，cc快速出错，炸裂，简单的给cc
- humanize2我打算拿rust全部重写，带一点点typescript和python
- 4月22日00:14
- cc来到了它的拐点时刻
- 模型降智，工具变成cc的套壳cx
- 我觉得唯一可能还有可取之处的地方就是中等/简单的SDE问题它确实能"快速铺开"
- 在原型或者项目初期还是有点帮助的
- cherichy: humanize太伟大了，基本上最核心的最精
- 练的harness经验都在这里了
- 后续一些比较有用的feature都是社区(群友)开发的
- 方法论这种东西必须开源出来大家一起用

---

#### 原文 L13255–L13326

[回到原文件 L13255](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13255)

- 长长的pipeline自动化
- 4月22日08:16
- 我推荐一个框架，acpx，我觉得很适合来做这个事情。比这种hookbased好用一些。也更容易观测中间状态
- 刘思皓: 我会搞成都是configurable的
- 4月22日08:19
- 而且尤其是，acpx做了一个几乎市面上所有的coding agent的兼容层
- https://github.com/TencentCloud/CubeSandbox
- @刘思皓这玩意儿能不能再做一个parallel agent啊
- 香港科技大学 研究助理教授 徐策羽: https://
- github.com/TencentCloud/CubeSandbox
- 你想要的feature其实我都做了
- 我自然是要做一个沙盒的
- 我觉得不要自己做沙盒呀，现在这么多开源的impl
- 4月22日08:24
- 1. 描述agentic flow的"编程语言"-- humz
- 2. 将编程语言编程实际的harness -- 编译器hcc
- 3. 将编译结果(harness) + 用户输入一起执行的 VM - hvm
- 我知道，我会让Humanize去参考开源实现的
- 我只想许愿
- 刘思皓: humanize2本质上是三层东西: 1. 描述agentic
- flow的"编程语言"-- humz 2. 将编程语言编程实际...
- 就是许愿啊
- hcc现在也有一些实现了，skill compilation方面的工作挺多的
- 刘思皓: humanize2本质上是三层东西: 1. 描述agentic
- flow的"编程语言"-- humz 2. 将编程语言编程实际...
- prose.md
- 你理解错了，我的hcc是输出一堆脚本
- 类似humanize里面现在的stop hook脚本
- understood
- 那make sense
- 机械化的harness不应该交给agent做--浪费token
- 而且还容易漂移
- 我希望我可以一个命令hctl humanize，就瞬间打满我整个集群的CPU和GPU
- 拿我整个集群的蒜粒来开1000个parallel session，每个跑5轮，去打印hello-world
- 我知道你想要什么，但是这里有一个细微的区别:
- 方法论(agentic flow)有两个组件: 工作流本身(一个思维模型) + 支撑工作流运行的基础设施
- 你自然可以在"支持工作流运行的基础设施"上面做很多花活
- 但是我比较注重前者:思维模型
- 就本之上，我这个需求是一个可以被humz给描述出来，并且被hcc compile出来的合法的flow
- 香港科技大学研究助理教授徐策羽:拿我整个集群的蒜
- 粒来开1000个parallel session，每个跑5轮，去打印...
- 但是这个flow本身是否具有远端spawn agent的能力 属于基础设施问题，是hvm的一个实现的feature
- 我打算交给社区做：)
- 当然不只一个人给我说需要这个需求了
- 4月22日08:30
- 你们都是集群大户
- 还是得整k8s
- 我最近也在看这个，我在做acpx的远程化以及sandbox和k8s的integration。
- 那理论上humanize2做好了之后，加上我这一套就能搞定humanize2的集群化了
- 是啊，他复制都搞不好，复制都能出错
- 刘思皓:而且还容易漂移
- 他没法做到一模一样
- 机械的功能就应该交给脚本，需要智力的地方才交给LLM
- 最有钱的一集:我在用claude评估视频
- 刘思皓:你们都是集群大户
- 4月22日08:41
- ai时代，天天在删除代码. 产生的太快了. 滋长疯长
- 拉屎不是美德，屁股擦的干净才是
- 4月22日08:59
- loop过程中微调有办法做到吗@刘思皓
- 小调直接告诉cc
- 大调建议cancel loop，改plan，然后重新启动
- 这个时候best practice是用refine plan还是直接从头开始?
- 刘思皓:大调建议cancel loop，改plan，然后重新启动
- 我的humanize会干3-4小时停下来歇一会儿此时我会提一些意见改plan，然后他会再继续干4-8小时不等
- 直接说“我自己跑了一下测试发现ABC问题，请你用humanize改plan然后接着搞”
- && "/home/Barry/Programs/human:
- 2a0aa364dde42620df
- ai有时候启动loop会擅自主张加入一些东西
- 然后只要是这种拼接指令不是单纯的humanize sh
- 也会造成session id写入失败
- 4月22日.09:18

---

### 4月23日

#### 原文 L13704–L13720

[回到原文件 L13704](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13704)

- 刘思皓:写一个tool call之前会插入进去
- 哦你的工作是被subagent干的对吧
- 否则就要等subagent完成，你的prompt才会被吃掉
- 主agent没办法中间修正子agent么
- ctrl b也行，但是记得要在prompt里面说让主进程告诉subagent
- 小米这个模型怎么在有的bench上都逼近4.6了
- 实现机制呢还是等toolcall检查点?
- 刘思皓: ctrl b也行，但是记得要在prompt里面说让主进
- 程告诉subagent
- 4月23日12:05
- 你是说什么的实现机制？主进程一直是可以通知subagent的
- 嗯通知是如何生效的比如sub在循环中
- 我有点没明白subagents如何在循环中
- 你开了agent-teams?
- 4月23日12:12
- 画图的艺术

---

#### 原文 L13750–L13778

[回到原文件 L13750](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13750)

- 我更倾向于把 gen-idea 产出的 idea 先作为 prompt，交给 si
- 轮。这个prompt甚至可以专门设计成“带着若干问题去研究
- 再把结果返回，作为后续判断和决策的依据。
- 可以让 subag
- 4月23日16:22
- 要refine的
- 张东宇:我今天在用humanize写文档的时候发现，如
- 果用一个类似spec的draft来 gen-plan, 会出现plan...
- e3
- 不然它不一定能抓住你想要的车西
- 泽文: 我更倾向于把 gen-idea 产出的 idea 先作为
- prompt，交给subagent做更深入的研究；这个过...
- 两个层面吧，我以前用refine主要是纠正它计划不合理的地方。然后对于“正确的”表述，我默认它能正确实施。
- 但是这两天跑下来发现，虽然在spec draft的context下，这个表述是“正确的”，但是在rlcr中，虽然draft也在
- plan中，但是它的权重可能很小。然后这个"正确的"表述在脱离了draft的context之后，就会产生歧义，最后出问题
- akane:要refine的
- 4月23日16:28
- 所以这也是为啥我建议你们试试树形结构的spec用draft作为树的根节点逐步展开成可执行的plan这样plan的
- context就始终在你的控制之内
- 核心思想就是让agent把plan的过程想想成画画先有idea(draft) 然后画轮廓(树的前几层)然后加细节xN最后
- 上色(plan)
- 这样树的下层永远不会脱离上层的context只是对上层的细化
- 4月23日16:29
- 非叶子节点构成spec叶子节点就是可执行plan
- Ak哥的loopy gen 出来的plan可以直接接到humanize里来跑吗
- 4月23日16:45
- 0:11

---

#### 原文 L13852–L13891

[回到原文件 L13852](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13852)

- 4月23日18:10
- 想请教一下，如果第一次humanize结束了，我要进行下一组任务了。是不是需要重新开一组新的humanize来改
- 4月23日18:20
- 不用
- 4月23日.18:41
- cherichy:想请教一下，如果第一次humanize结束
- 了，我要进行下一组任务了。是不是需要重新开一组...
- 4月23日20:07
- 现在纯codex的humanize能长时间跑吗？我claude没token了，换纯codex中间经常断
- 要么得修一下codex hook based的机制，我的得到的反馈是还是会有比较经常的中断
- 或者等humanize2
- 我试试
- 我之前vibe了—个小工具，可以试试?https://github.com/amphoreus-ai/codex-autopilot
- 刘诗楠:现在纯codex的humanize能长时间跑吗？我
- claude没token了，换纯codex中间经常断
- 先用humanize把plan生成好
- 装这个hook之后跑codex
- 感谢群友
- 4月23日20:14
- 睡不着 起来写humanize2
- 超级期待了
- 超级期待了
- 我自己也觉得很牛逼但是是不是真的牛逼
- 还得做完实际试一试
- 当年(其实就是半年前)我也觉得gaac很牛逼
- 确实，得搞点benchmark
- 4月23日20:18
- 其实大家都想到一块去了
- 我们需要4个东西:
- 1.一套描述"方法论流程"的编程语言
- 2. 一套能将这个编程语言，编译成为驱动各种模型和工具的harness的“编译器”
- 3. 一套能够让这个编程语言描述的流程，在某个输入下跑起来的平台 Humanize2
- 4. 对flow本身的benchmark
- 这四个东西加起来是humanize2
- 当你意识到agenticflow本身其实是一个PL问题的时候
- 一切都变得自然了起来
- 是时候发明agent的语言了
- 做了已经
- 牛的，这不就是把skill规范化

---

#### 原文 L13960–L14315

[回到原文件 L13960](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:13960)

- 陈仁泽-pku:但这个本身就是比较困难的事情
- 文档越多降智越厉害是你说的
- 我高度赞同，flow本身是个需要强形式化参与的过程
- 是，但我并没有说0文档
- 翁大爷的狗@Rakuten:文档越多降智越厉害是你说的
- 本质回到了图灵/冯诺伊曼那个时代
- 什么是计算，什么是程序
- 本质上还是树形结构文档作为树的顶层存在越往下展开越形式化
- 实际上我只保留了架构决策的文档
- 叶子节点全部是形式化语言描述的flow
- BTW
- 而没有任何指导实现的文档
- ASCI 流程图对 agent 友好吗
- 这些文档的作用是，下一个agent来理解的时候不用把代码全读一遍
- 我直接在humanize2里面构建了一套面向agentic flow的类型系统
- 很多时候constraint 的复杂度和implementation 是等价的
- 陈仁泽-pku:其实等价于停机问题
- 这个是我要求它画给我看的
- 翁大爷的狗@Rakuten: ASCl 流程图对 agent 友好吗
- 我感觉状态机描述可以 handle 大部分场景
- mermaid 画的状态机 agent 能看懂
- 说到这个我今天在做一个humanize的feature就是在start rlcr之前让builder和reviewer分别review—下plan，看
- plan有没有会引起歧义的表述。以及plan有没有前后不一致的地方
- 刘思皓: 我们需要4个东西:1.一套描述"方法论流程"的
- 编程语言2. 一套能将这个编程语言，编译成为驱动各...
- 你可以在构建flow的时候，直接去静态校验诸如这个流程是否所有状态可达
- 而且群里发图片，密密麻麻的全文字观感也不好吧
- 明扬:
- 也算是某种意义上的“语法检查”
- 然后可以把dv验证或者formal那一套全部做进去
- 张东宇: 说到这个我今天在做一个humanize的feature
- 就是在start rlcr之前让builder和reviewer 分别revie...
- 靠自然语言base的llm检查
- 终归会遗漏
- 4月23日20:39
- 你不如直接上形式化约束
- 是所以只能当成humanize1的一个屎山修复feature
- 这样的好处是，你相当于定义了一套面向flow的isa
- 我之前也考虑写一个 dsl 去定义 agent 的 role 和协作，后面发现直接用 python 代码调用 agent sdk 就能做到我想
- 要的。搞 dsl好像overkill了
- 弱检查总比没有检查强
- 张东宇:是所以只能当成humanize1的一个屎山修复
- feature
- 我大概讲一下humanize2的核心思路：
- 整个开发流程是一个dfg
- 但是这个dfg不是datsflow graph
- 而是development flow graph
- 每个节点是一个agent
- 类型系统有四种：代码库，上下文，prompt，state
- 刘思皓: 我们需要4个东西:1.一套描述"方法论流程"的
- 编程语言 2. 一套能将这个编程语言，编译成为驱动各..
- 每个agent超节点有最多四输入四输出
- 翁大爷的狗@Rakuten: 文档越多降智越厉害是你说的
- 每种输入输出可以去三种选择：0，1，2+
- 然后你将获得一个6561=3^8大小的关于flow的cisc指令集
- 这个文档相当于下个阶段的提示词了
- 明扬:
- 不愧是做 arch的
- 然后你只需要做cisc到risc的过程
- 就会发现，描述所有agentic workflow你只需要10条指令
- 然后剩下的就是经典的PL问题了
- 新时代纸带图灵机
- 刘用皓：复种检入检出可以去二种选择：0，1
- 请找出截图中的至少三处 AI味中文（
- 明扬:
- 不用找，这图里全都是ai生成的，来自那个群里的一个不知道是cto还是架构师
- 4月23日20:44
- 组合起来就不是啊
- 我草两千行
- 绷不住
- 所以你知道我批判的是什么了吗？
- 明场：
- 一个流程指导文档能写两千行，我不敢想象它们文档目录下的文档，几个context window能装得下
- 4月23日20:46
- 大道至简🙏
- 有个疑问，这样形式化描述完行为后是不是等价于先自己实现了一遍
- 我觉得不是
- 陈仁泽-pku:有个疑问，这样形式化描述完行为后是不
- 是等价于先自己实现了一遍
- “黎曼猜想”与“证明”的关系
- (这么说可能有点民科
- 起码机器能帮你检查出来你的命题本身是不是有问题
- 比如五彩斑斓的黑
- 把按钮放大的同时缩小一点
- 不我这套形式化描述并非描述plan，而是描述flow
- 翁大爷的狗@Rakuten:所以变成了自然语言-DAG-代
- 码的两次编译
- 或者找到一个N
- 这个N要同时>1且<0
- 我觉得能被机器确定性的检查出来，这一点很重要
- 有些时候是这样，就是实现的目标比较简明且确定的时候
- 明扬：“黎曼猜想”与“证明”的关系
- 然后他开始猜你想要
- 他是用来开发新的flow的，它相当于说我固定了一套基本原语，基于这一套原语，我能够描述一个想humanize的流程
- 但很多时候边界条件是比较复杂的
- 然后你在这里可以做很多检查
- 比如你所有规定的state都必须有一条路径可以到达
- 这里就比较抽卡了
- 翁大爷的狗@Rakuten:然后他开始猜你想要
- 不需要一步到位，写得那么严谨
- 比如说flow当中的路径必须全面可达
- 软件开发需求也是一步一步完善出来的
- 然后优化编译器的那一套东西就可以全面施加上去了
- 约束条件可以由少到多
- 那我感觉软工领域应该已经有很多类似的工作了
- 初始需求：
- 注册用户接口一定要能注册用户
- 4月23日20:52
- 第二阶段再继续完善：
- 一个IP每天只能注册10个用户
- 整个humanize用这套新的方法论就只需要写50行
- 这句话怎么这么有恩情味
- 明扬：初始需求：注册用户接口一定要能注册用户
- 哦，这就是 agent workflow description 吧
- 刘思皓:
- 是，但是是用强形式化的方式描述的.
- 然后pl里面的一系列优化
- 比如递归
- unroll
- parallelable
- 你可以全部做一遍
- 这个好啊
- 刘思皓:
- verify 本身还是依赖项目自己的 tester/verifier 或者 agent reviewer 是吧
- 这是每一个plan都要动态生成一个吗？
- 是, verify只是agent的一个功能
- 我感觉这个才是 bottleneck(
- 陈仁泽-pku: yerify 本身还是依赖项目自己的 tester/
- 对每个plan都有一个自己的mlir方言表示
- 但是回归古德哈特定律
- 你没有办法量化一个verify指标
- 只能借助强verify agent校验
- 但是我做了一些优化
- 就是我这个类型系统里面专门有AC的概念
- 4月23日 20:57
- 到最后会不会变成无数个 dialect (orz
- 就是有一些关于AC硬性检查参与的类型变换
- 我觉得肯定是会的
- 光尘: 到最后会不会变成无数个 dialect (orz
- agent时代真来了吗
- mlir社区就是喜欢自己搞方言
- 但是基于AC的检查并没有解决本质的问题，只是把"代码是否实现完全"拆分了一下
- 刘思皓:就是有一些关于AC硬性检查参与的类型变换
- 真正的bug-free还是得回归传统的形式化证明比如lean这种
- 4月23日21:00
- 有很多事情就非常好做
- 因为你可以把一整个PL和Arch
- 的前人经验全部迁移过来
- 最简单的，众所周知，对agentic workflow本身的benchmark是极其困难的，因为如果不是跑一个真实全量的任务，你
- 不知道到底怎么样.
- 那么有了这个isa之后，你就可以参考体系结构里面的测试
- 我们不跑全量，而是构建micro-benchmark
- 这样workflow本身就第一次有了benchmark
- 这里怎么注入 reviewer 对于当前 codebase state 做 review 的判断规则?
- humanize没有Cl/CD的问题就解决了
- 两种办法: 1. 硬编码prompt (humanize的办法); 2. 在创建一个prompt生成agent
- 愚鱼: 这里怎么注入 reviewer 对于当前 codebase
- state 做 review 的判断规则?
- 还能这么理解
- 刘思皓:我们不跑全量,而是构建micro-benchmark
- 妙啊
- 我前天意识到整个agentic workflow并非一个工程管理/协作问题，也并非一个物流运筹管理问题
- 它就是一个纯粹的PL问题
- 有种万物皆可 mlir 的错觉（
- 我这里只是借用了一下它方言的概念
- 实际上并不会真的用mlir的infras
- 我懂了，写一个 prompt 作为constant，作为 review function的参数传过来也行
- yep, like this
- _cb: tcb. Sinit_plan: !prompt) -> (tcb
- init_cb
- isa.comst (kind = "ctx.empty"): lctx
- dsa.const (kind - "state", payload - "Init
- rzied phis
- beck-scb_
- - aisa.loop_mezge init=%cbe
- It_cb: tcb. sinit_plan: tprompt) > (teb.
- init_cb
- s: ( = t st
- rzied phis
- aisa.loop_mezge init-%cbe
- beckßch_next
- back-%ctx_nex
- aisa.loop_merge 1nit-%ctxé
- aisa.loop_merge init-tse
- back-%state_
- 4月23日21:05
- 你的prompt模板就是整个flow的字面量
- 我之前一点不成形的想法，想到是编译成一套程序，调用 agent的做事情
- codebase = variable
- context = hidden-value
- prompt = predicate
- state = control-tag
- 你可以把整个PL里面的每个概念都迁移到agentic workflow上面
- Agent = Model x Tool x Action x Permission
- 然后agent就是指令系统
- 这个就是类型系统
- 刘思皓: codebase = variable context = hidden-
- value prompt = predicate state = control-tag
- 4月23日21:09
- 消耗的token量就是功耗
- 然后从 high-level lang => gdsii整个stack, 你可以one-level up
- 在这个新的系统中找到——对应的类比
- 核心就是agentic workflow并非一套自然语言的markdown文档
- 恰恰相反，它是一套编译器基础设施
- 程序员从"写代码描述程序的功能"转换成"写代码描述一个程序被生成出来的过程"
- minimize token to success, minimize time to success, min human interruption ...
- 谁就能在这个疯狂的AI时代胜出
- 而这个flow本身的代码可能如此的少
- 4月23日21:14
- 以至于这是需要纯手写的地方
- 所以ai并没有夺走programmer的工作，只是one-level up了
- 从手写代码，变成手写生成代码的代码
- meta code
- 刘思皓:而这个flow本身的代码可能如此的少
- llm is the new processor/interpreter
- Agent flow is the (new) code
- yep，而且这贯彻了我一直以来的精神：大道至简
- 整个code只有十种指令
- meta harness coding
- 刘思皓: 程序员从"写代码描述程序的功能”转换成"写
- 代码描述一个程序被生成出来的过程"
- 却可以描述一切workflow
- 有种被灌顶的感觉了
- 这里的自举是指什么呢
- 智谱黄睿博:我觉得需要一个自举的AI推理框架，谁赞
- 成谁反对，现在的复杂度太高了
- 当你有了一套isa写程序来描述ai workflow本身
- 而ai最擅长的就是写程序
- 你猜猜会发生什么
- 而这件事你如果走自然语言的skill
- 4月23日21:22
- 就会快速腐烂和漂移
- skill programing language
- “基于形式化检查校验的workflow，是一个永远不会腐烂漂移和体积膨胀的skill”
- 不对，应该是prompt编程语言
- 这是最核心的区别
- 主要是写的prompt本身就存在很大的不确定性
- 不是prompt/skill编程语言
- 只是workflow编程语言
- skill本身其实只是prompt
- 那感觉最重要的可能是 micro benchmarking？需要迅速准确的反馈?
- 蒸馏我觉得就本质上就是限定模型的行为
- skill本身是一个基于“渐进式披露”的prompt
- 这句话我怕是写不进文章里去了
- Group Chat History
- My:现在只有明(民)科看出来了，形式
- 化方法的执行成本越来越低.jpg
- My: [图片]
- My: [图片]
- 聊天记录
- 有isa之后，构建microbench不是很自然的事情嘛
- 光尘: 那感觉最重要的可能是 micro benchmarking?
- 需要迅速准确的反馈?
- 就感觉你benchmarking的标准可能也要不停迭代，随着比如说lm 本身的更新
- 是的，你可以把体系结构的所有东西迁移过来
- Ilm本身类似微架构
- 微架构进步了
- 我benchmark能不变嘛
- 4月23日21:28
- 这里面可以类比映射的地方多到令人发指
- 恍然小悟
- 这套理论上也可以用来管人
- 管理学+体系结构结合
- 我之前一直是往工商管理学的角度去思考构建多智能体系统的
- 4月23日21:31
- 因为这如此直观：管agent类似管人
- 我理解这一套新flow其实是在做一套完全客制化的“自然语言到编程语言”编译器
- 它是用来写humanize本身的编程语言
- 本质动机是：我们不知道humanize好不好，或者说，我们不知道任何flow好不好，因为没有benchmark
- 那么第一步就是构建benchmark
- 但是如何构建一个快速且经济实惠，但是又能够在某种程度上表示全量flow运行结果的benchmark呢?
- 自然能想到：抽取共性操作，做mircobench
- 抽取共性操作不就是给flow设计isa
- 有isa之后，这个问题不就是一个pl问题
- 我前天想明白这个之后
- 咪的天呐
- 这就是整个humanize2如何诞生的原始思路，原初我只是想给humanize上一个cicd，或者搞一套benchmark，看看
- flow好不好
- 做一个vm
- 愚鱼: 你的 runtime 打算怎么做
- 4月23日21:36
- 一切都自然而然映射过去了
- 你的 runtime 打算怎么做
- 你可以理解为做一个当前flow的执行跟踪机器
- python + sdk 吗
- rust吧
- 编程语言不重要
- 等humaniz
- rust那不折磨自己吗
- 反正也不是我写啊
- 而且我觉得
- 4月23日21:37
- rust，带一点点typescript和python吧
- 6202年了，不谈代码量了，尤其是在humanize群里
- 得看有没有 rust 的 agent sdk
- 如果是为了要用某个库，写一个简单的胶水层就好了
- 这个vm/runtime完全不需要高性能
- 因为里面每个操作都要跑几分钟/小时
- 只是一个机械的flow执行/监控机
- 我在想直接用编程语言+agent sdk 不就可以做到各种事情，我们为啥还要搞一个 dsl。这个事情就类似现在
- agent 可以直接写 cuda，再让他写 dsl 的价值啥
- 你的agent cuda写得怎么样，我感觉不太行啊
- 我这里并不是说要引入一个dsl
- 只是引入了一个“思维模型”
- 你可以用现成的编程语言实现它
- 这个vm感觉是个很重要的infra
- 也可以用mlir infras实现它
- AI写的很6
- 智谱黄睿博:你的agent cuda写得怎么样，我感觉不
- 为了decouple吧有了isa你可以把flow的构建和agent的能力解耦
- 太行啊
- workflow as pl 只是一个思维模型
- 实际实现起来，我肯定怎么快/稳定怎么来
- 我上次没有继续做下去就是发现了这个问题，又回答不了自己
- 愚鱼: 我在想直接用编程语言+agent sdk 不就可以做
- 到各种事情，我们为啥还要搞一个dsl。这个事情就...
- 4月23日21:42
- 匙白
- 这点我赞同
- 刘思皓:只是引入了一个“思维模型”
- 核心点是你如何找到一个原子的“编排动作”
- 泽文: 是的，我觉得我们是对指导 agent 干活儿这件事
- 进行编排
- 也就是“isa”
- 至于实际实现，我肯定不会复用任何llvm/mlir的基础设施的
- 这是自己给自己添麻烦
- yep
- 泽文: 是的，让每个 insn 对应的 agent 的行为趋于稳
- 但这里又有一个问题怎么让agent的行为趋于稳定
- 问题应该是反过来的：什么样的flow，能让agent的行为稳定？
- 4月23日21:45
- 什么样的flow，能让agent的行为又稳定，而且又能有提升
- result = model x tool x flow
- 你想想如果一个flow能让model的能力提升10%
- 已经跟不上群友思路了
- 但是现在确实到了要好好做agent的时候了
- 相当于我只用一个协调编排的机制，就完成了新一代模型训练才能达到的性能提升
- 有点没太理解怎么保证isa的指令行为是确定性的
- 本质上指令应该都是agent call?
- 想象一个最简单的场景，如果你的flow本身有自适应拆分任务的机制，以至于每个agent拿到的任务都很简单
- 这样agent的行为就能自发稳定
- 4月23日21:51
- 我觉得可以这么想，我们是追求结果的确定性，行为上可以自
- x tool x flow
- 做完比啥都强
- 确实
- 做出来玩一下就清楚了
- 感觉vm还是需要对输出强审计
- 我觉得我百说不如一做
- 做完比啥都强

---

#### 原文 L14335–L14357

[回到原文件 L14335](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14335)

- 我昨天还和@Shiyi在讨论
- 刘思皓: 当你意识到agentic flow本身其实是一个PL问
- 题的时候
- instructions里给agent规定的各种step本质上就是一种编程语言
- 这件事情一旦做成了
- instructions里给agent规定的各种step本质上就是一个程序，用“自然语言”做编程语言写的。非常原始，非常暴力。
- 4月23日22:08
- 方法论起码领先一年
- 而且领先会一直保持下去
- 因为方法论本身就是就是一小段代码之后
- 我觉得需要一个系统性的benchmark一个flow是否好的方法
- 然后写instruction的过程，其实就是在给agent编程的过程。之前的flow：人(+agent)->写instruction -> agent
- 执行instruction。但现在的问题是，agent本来就擅长编程，为什么不能让agent自己来编这个程序呢
- 刘思皓: 程序员从"写代码描述程序的功能”转换成"写
- 代码描述一个程序被生成出来的过程
- 看下群记录
- 香港科技大学研究助理教授徐策羽:我觉得需要一个系
- 统性的benchmark一个flow是否好的方法
- 醍醐灌顶啊，这么咖的项目如何才能尽一份力呢
- 我昨天跟诗怡讨论的时候，嗯，我说现在Agent的编程，instruction，还处在打孔的阶段。我们就，需要一个basic，
- 或者需要一个Pascal
- 4月23日22:14

---

### 4月24日

#### 原文 L14517–L14531

[回到原文件 L14517](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14517)

- 4月24日06:15
- 编译器/PL只是个思想模型
- 本质只是在说：我们需要一些标准且通用的形式化原语描述workflow的每一个“结构/组件”，这么做有3个好处：1.
- harness的实体的生成就简单了；2. 可以做很多静态检查；3. 能静态检查的结构化语义描述的workflow可以赋能ai工
- 作流自身开启迭代
- (特别是现在阶段），可能有点太重了
- 可能想法很原始，我只是觉得为了这个需求去搞个编译器，
- 反正也是交给LLM写
- 这么做最直观的好处有很多，最简单的，能解决当前claude subagent里面不能再spawn subagent的限制
- 4月24日06:20
- 3我很同意，奇点singularity
- 简单来说，如果把instruction里的自然语言当做编程语言的话，那instruction就是程序，那么agent它就是一个
- CPU，只不过是一个运行频率零点几赫兹，甚至0点零几赫兹的CPU
- 是，你用“类比”作为关键词搜搜群记录

---

#### 原文 L14575–L14602

[回到原文件 L14575](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14575)

- 其实就是把workflow放进一个约束系统里
- 纯skill这种自然语言描述的flow太放松了
- 4月24日09:31
- 4月24日09:31
- haskell迎来新生
- 但这样就失去了自然语言模糊化的灵活性了？
- 不啊，你理解成skill里面的rust就好了
- 4月24日09:35
- 用这种语言描述出的ralphloop会直接出编译警告
- 警告内容就是：goal drift
- 妙啊
- 需要直接报错.
- 你理解成，静态检查prompt是否构成组合逻辑回环
- 如果出现组合逻辑回环，就会goal drift
- 4月24日09:43
- 然后死代码对应“永远不会触发的agent”
- workflow本质描述的其实描述的是一组状态转移规则
- 形式化/结构化workflow之后，能在很大程度上把一些看上起合理但实际有结构缺陷的workflow给抓出来
- 我觉得我需要在磨刀和砍柴之间取一个平衡
- 4月24日10:22
- 附议
- 4月24日10:30
- 快速 vibe了一个抗智障选 model。第一个数是智障分，第二个数是我剩多少 quota，后面的数是智障分细化以后排
- 出来的适合做什么事情的排名，是脑洞，P是 plan，B 是 build，R是 review
- Models
- claude

---

#### 原文 L14616–L14632

[回到原文件 L14616](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14616)

- 我也不知道为什么最近sonnet4.5在智障榜评价那么高，但是我觉得它开脑洞和计划其实都不太行，应该按照模型
- 再单独降个权（
- codex 5.5 之后是不是Claude 就不降智了?
- 我感觉还是降
- 好一点了
- We have a number of tools to reduce verbosity: model training, prompting, and
- improving thinking UX in the product. Ultimately we used all of these, but one
- addition to the system prompt caused an outsized effect on intelligence in
- Claude Code:
- 我们有多种工具可以减少冗余：模型训练、提示和改进产品中的思考用户体验。最
- 终我们使用了所有这些方法，但对Claude Code的智能产生了巨大影响的一个系统
- 提示的补充是：
- "Length limits: keep text between tool calls to <25 words. Keep final responses
- to <100 words unless the task requires more detall."
- 长度限制：工具调用之间的文本保持在25个单词以内。最终回复保持在100个单

---

#### 原文 L14636–L14650

[回到原文件 L14636](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14636)

- 高端的降智只需要朴素的手法
- IF越强的模型，这种不过脑子的prompt影响越明显...….
- 4月24日11:01
- Agentic Capabilities
- 4月24日11:02
- 11:01 0
- ·Agent 能力大幅提高：相比前代模型
- 误，在 Agentic Coding 详测中，V4-Pro
- 已达到当前开通模型最侵水平，并在其信
- Agont 相关详测中用样表现优异。目前
- DeepSeek-V4 已成为公司内部员工使用的
- Agentic Coding 模型，抛评测反馈使用律
- 始优于 Sonnet 4.5， 交付质量接近 Opus
- Geminl-3.1-Pro-High

---

#### 原文 L14655–L14664

[回到原文件 L14655](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14655)

- · Agent 能力大幅提高：相比用代模型.
- DeepSeek-V4-Pro 的 Agent 能力壁普理
- 强，在 Agentic Coding 详测中，V4-Pro
- 已达到当前开通模型最懂水平，并在其他
- Agont 相关详测中用样表现优异。目前
- DeepSeek-V4 已成为公司内部员工使用的
- Agentic Coding 模型， 拥评测反馈使用体
- 始优于 Sonnet 4.5， 交付质量接近 Opus
- 4.6非思考模式，但仍与Opus4.6思考模

---

#### 原文 L14986–L14997

[回到原文件 L14986](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:14986)

- 小红书
- harness is the key to use agents
- 4月24日23:16
- 我觉得问题在于dpsk也没有那么多agent数据去喂了
- L.Zhu: V4使用感受，Harness 远比想象中的
- 更重要
- 一次迭代要做成强coding模型还是太难了
- 帮我review以下plan:xxx在review的过程中，你要注意(但不是只关注)该文档中是否有前后矛盾，以及含糊不清
- 的地方。
- 这个prompt在gen-plan之后用，非常牛逼
- 不瘦三十斤
- 不换头像

---

#### 原文 L15061–L15071

[回到原文件 L15061](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:15061)

- 老马买了cursor如果能坐稳第三我觉得就是赚了
- 问题是 cursor 25 前都是 harness 的反面啊
- coding数据应该还是缺的
- coding agent 和 Ilm coding
- 是两种数据
- cursor挺好的 dau高也是个明星产品？
- cursor这个产品简直是走向了harness的反面
- 不度三十斤
- coding agent 和 llm coding
- 是两种数据
- cursor挺好的 dau高 也是个明星产品？

---

### 4月26日

#### 原文 L15290–L15330

[回到原文件 L15290](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:15290)

- gpt套餐性价比高的有推荐吗
- 4月26日00:27
- 我发现一个小妙招
- 代码行数过5k之后
- 把a的aeeeionid克培于纶aedey
- full codex 完全可行
- 把cc的session id直接丢给codex
- 让它接手
- 可以快速bootstrap
- session id?他直接去~/.claude 找上下文么
- 4月26日00:28
- humanize2 day1就是humanize2自举的
- 因为我意识到如果我在做一套pl
- 编译器不能day1自举
- 这就好比开发vscode的人不用vscode开发一样尴尬
- 4月26日00:44
- 我之间试过让
- 还能这样
- 刘思皓: 把cc的session id直接丢给codex
- 4月26日00:58
- very Interesting
- codex的plan其实流程没问题
- Neavo
- 就是最后的文件和反问力度太轻了
- Neavo
- 我写了个 skill， push它的追问力度和plan.md的详
- 细程度
- 感觉 humanize的核心思路之一也在被其他开发者独立发明
- 因为其实核心思路没几条
- build-review也不是我发现的
- 要真说什么核心思路，最多只能说一句"codex被放入一个loop里面充当reviewer的效果特别好"，别的就没了
- 又到了骂cursor傻逼的时候
- cursor已经能自动捕获humanize的hooks了，好多人和我说了
- 所以我做了humanize2
- 翁大爷的狗@Rakuten: 感觉 build review 是非常适合
- GUI 客户端做的功能
- 我认可，开始，然后
- 另外，做完之后，@t
- Read temp/build
- 干。

---

#### 原文 L15366–L15382

[回到原文件 L15366](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:15366)

- 看起来1M效果还不错
- Long-context retrievsi
- saccde-aode
- 4月26日09:33
- 因为codex没有1m所以你也没得选？
- 刘诗楠: 5.5大家有推荐的context window size吗
- 不能像之前那样config里面改吗
- 4月26日13:21
- 我发现纯codex的rlcr好像会把同目录下的其他session同化成rlcr的sub agent
- 大家遇到过吗
- 4月26日14:34
- codex的沙箱模式好像没法访问gpu
- 4月26日15:39
- 回复一下，是可以的，copilot进autopilot模式能自己给自己调用skill(比如humanize的gen-plan)，也能弹出选
- 项框的时候自动选最有可能的
- 泽文:能不能做一个auto模式：由我先提出需求，系

---

#### 原文 L15430–L15437

[回到原文件 L15430](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:15430)

- hb，不过v3在这个时间点确实还是有点烂了
- 我发现了humanize数据飞轮的正确用法
- https://github.com/PolyArch/humanize/issues
- 这玩意并非开一个issue我就去修，而是每累积三个月
- 直接触发下一版humanize
- 这真是我做h2的绝佳素材
- hh，不过v3在这个时间点确实还是有点烂了
- v4主要是这kv cache太小了，随便给点内存空间，就能拉超大并行度。

---

### 4月27日

#### 原文 L15438–L15720

[回到原文件 L15438](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:15438)

- 4月27日00:27
- 上哪里去找这么高质量的超长时间多轮开发方法论全记录
- 感恩群友
- 4月27日00:37
- 感恩群友
- 4月27日00:37
- 4月27日00:57
- deepdrink
- 4月27日01:44
- 三个月对llm来说可是三年
- 刘思皓: 这玩意并非开一个issue我就去修，而是每累积
- 三个月
- 4月27日01:52
- 过三个月就都不用修了
- 北田圭人：三个月对llm来说可是三年
- IIm现在估算工期依然是按照人的工期估算。
- 也不是很人不
- 它什么时候能用自己的工期估算。
- 4月27日01:57
- 就是xjb 估算
- 所以我现在都是叫他估算loc。
- LLM对这种“估算”类任务的靠谱程度都是一塌糊涂
- 辽太郎是啥意思
- 翁大爷的翁大爷:所以我现在都是叫他估算loc。
- 我昨天让他部署一个LLM
- 做点很基础的优化
- 结果我原本mfu可以到35
- 任务太发散了不行的
- 他给我干到20了
- 太他妈唐
- afaik 端到端优化靠 Ilm loop 很难做
- 太容易跑偏或者钻牛角尖了
- 4月27日02:04
- 主要也不是infra
- 就是让他部署一个东西加一个hook
- 別瞎搞
- 他最后把我的triton kernel还有原生gpu操作都换掉了
- 然后性能直接爆掉
- 4月27日02:11
- 大升级!
- 刘思皓: https://github.com/PolyArch/humanize/
- issues
- 现在有人做更好的后台监控吗？
- 如果还没有的话我去加个功能cc原生的确实太猪鼻了
- 我觉得v3是一个好的工作 y4很一般啊
- 香港科技大学 研究助理教授徐策羽:hh，不过v3在这
- 个时间点确实还是有点烂了
- v3的架构还是非常好的
- v4有点太雕花了
- 也不是
- 这个花到底值不值也不知道，消融没怎么做
- 4月27日02:13
- 应该说我感觉好玩的技术他们确实没上然后上的技术有点硬上
- 太子管架构哈人
- 这就不得而知了
- 他是为了
- 硬凑这个dense + sparse hybrid 架构
- 就整了hca+csa这一出活
- 从infra角度这个KV压缩很有意义，但是模型训出来效果并没有很好
- 然后据说给infra带来的巨大的压力
- 导致他们post train做崩了好几次
- 那这个不用据说（
- 因此延迟了几个月
- 光是推理做适配都很有压力了
- 而且压缩比1:128我记得是
- 太变态了
- 为啥是太子
- B4RRy: 太子管架构 哈人
- 老板
- 反正有一种微操的感觉啊
- 全部attention scores,向左平移五厘米!
- 至于这个架构好不好，就看之后几个月有没有友商follow了
- 到时候就知道 pt 不行到底是因为 dpsk 数据不够还是因为架构真的不行
- 确实确实
- 虽然我感觉 v4f 完成度还行
- 我感觉藏了好多技术细节没说
- 比如它里面的稀疏层，用了一个类似v3.2的dpsk sparese aatn
- 但是没有说这个是怎么训练的
- 4月27日02:18
- 3.2时期他们是说的
- 4月27日02:18
- 这里就没说不知道是e2e还是单独训练了一个筛选器有没有auxloss什么都没说
- 所以我对v4不太有好感
- +让ai读技术报告和朋友讨论的时候ai说错了导致我出丑了哈哈哈
- 4月27日05:24
- 我之前已经两个月没有写过任何一行 code了，这一个月我又加上了一个月没有读过 任何一行 code
- 不知道我有没有一点完蛋（
- 我是让它估需要的 token数
- 翁大爷的翁大爷:所以我现在都是叫他估算loc。
- 取决于你需要的准确率吧，百分之五六十的话没啥问题
- 百分之八九十的话就都是错的
- 4月27日 05:49
- 确实是
- ai估计任务你要教他思考
- 他的cot不会主动思考这种问题
- 引导一下他就能估计对
- 4月27日09:28
- Skill也有语言虚拟机了！上交大开源
- SkVM，实现一次编写，处处高效
- 让Skill在任意模型上高效运行
- 机器学习算法与自然语言处理
- @刘思皓跟你思路一样，只不过他是在skill这层
- 4月27日09:39
- 你是第四个和我说的
- 这层
- 我知道了.jpg
- xs hhh
- 无数人转发
- haibo老师还是太有影响力了
- 目瞪狗呆
- 他仍作为现有harness的插件，格局还是小了点
- 4月27日10:23
- 格局还是小了点
- self-programmable harness
- 4月27日10:32
- deepseek-v4-flash
- https://gpt.fact-lab.work/v1/
- 我们自己serve的dpsk v4 flash。群友们免费用。
- 不过请注意我们后面可能会record一些脱敏的数据以供我们的内部研究。
- sk-1f96f87586bb00036d0024aa3dbae414759f112906988a9bb1dd1b0921c11176
- 以及刚刚serve起来，这几天可能还不太稳定..
- 4月27日10:34
- 用户
- hello
- deepseek-v4-flash | Humanize
- 用户
- say somthing
- deepseek-v4-flash | Humanize
- 确实。。
- 太有格调了
- nb
- 太有格调了
- 嗯？看起来用不了？
- cherichy:
- 我check一下
- 太有格调了
- 理论上response API和chat completion都行，直接的completion不行
- gpt.fact-lab.work/v1
- s://gpt.fact-lab.work/v1/chat/co
- 应该是ok的？
- 4月27日10:39
- 好像是卡了sub2api的一个bug
- 4月27日10:53
- Humanize in H2
- 以后只会有两种编程语言：
- - 流程图
- - 自然语言
- 回到乐高编程
- 什么原理,底层还是代码吧
- 有点像coze编程
- 刘思皓: 以后只会有两种编程语言：- 流程图 - 自然语言
- yep
- 我还是想说，我觉得quiz绝对是暴政
- 我自己plan出来的quiz我从来没做对过
- 那如果不是ai问你是用户问你呢
- 但是我还是提供了一个--skip-quiz
- 我也经常做错
- 做错了说明我可能还是没想清楚
- 禁止许愿编程
- 4月27日10:59
- 抽象成这种粒度之后，你可以
- 1. 轻而易举地构建各种flow
- 2. 换模型变得非常简单
- 3. hcc会静态检查你的flow是否有缺陷，而不是跑了好一会儿才发现漏洞
- 刘思皓:
- 选B或者选C，大概率是对的
- 香港科技大学研究助理教授徐策羽:我自己plan出来
- 的quiz我从来没做对过
- 牛蛙
- 刘思皓:
- scratch
- 使得
- 重回labview / simulink / scratch
- maybe unpopular，但这是不是把humanize变得less sexy了，市面上做workflow的agent system两年前就有好多了
- 每个节点要么是脚本节点(一些程序性的操作)
- 4月27日11:04
- 要么是智能体节点
- 我觉得harness这种东西不应该开发给大众，可以作为内置feature，由一个调度把任务h做划分
- 你这么一说确实
- 刘诗楠: maybe unpopular但这是不是把humanize
- 变得less sexy了，市面上做workflow的agent syste...
- 因为我公司的人bashrc都不会配
- 产品视角
- 但是h2能实现的东西是humanize的超集
- humanize只是h2能表达的设计空间的一个点
- 每个智能体节点都是允许人类介入的claude code或者codex或者gemini终端
- 刘诗楠: maybe unpopular，但这是不是把humanize
- 变得less sexy了，市面上做workflow的agent syste...
- 嗯嗯是的，在用户的角度上说，我可能不太清楚哪种workflow会比h1的更好；那我定义起来就挺麻烦的？
- 刘思皓:但是h2能实现的东西是humanize的超集
- flow配置感觉合理，agent 创建subagent
- cc感觉不是很愿意创建subagent，除非我明确叫他
- 4月27日11:10
- h2未来并非给人用的
- 刘诗楠：嗯嗯是的，在用户的角度上说，我可能不太清
- 楚哪种workflow会比h1的更好；那我定义起来就挺...
- :)
- 迭代速度大于一切
- h2不能帮你配置最优flow，但是它能够帮你在启动flow前，静态检查出一些你没有发现的缺陷
- 也帮忙配置了
- 类似编译器的静态检查
- 除此之外，它是h1的超集
- agent first
- 刘思皓:h2未来并非给人用的
- 嗯嗯make sense
- 刘思皓: h2未来并非给人用的
- 因为h1也并不是最优的solution
- 4月27日11:13
- 我觉得还是等我完全做完让大家先尝尝鲜
- 这样可玩性就很高了
- 你可以创造任意特化的工作流
- 并且快速迭代
- 期待啊
- h2是个vscode的插件
- 原来是群友太热情了，给我的serving顶炸了
- 香港科技大学 研究助理教授徐策羽:好像是卡了
- sub2api的一个bug
- 4月27日11:21
- 我感觉对于一些不知道结果的任务(但是给了某种约束)让ai去做现在还是很有问题
- humanize的paln
- 4月27日11:28
- 我在做一个plan-check的feature，今天应该能交pr。主要是为了确认plan是否合理，有没有内部冲突，有没有模棱
- 两可的表达
- 两可的表达
- 4月27日12:54
- 暴赞
- 我感觉一般更多是容易漏掉东西哈哈哈
- 实际运行才知道的问题
- 大家觉得humanize对非代码修改，比如启动/监测模型训练怎么样呀
- 有点Overkill
- 可能因为模型对实验没有足够的上下文，我感觉他们在review的时候讨论来讨论去，很多地方是我不知道他们为什么
- 要讨论这些东西
- 感觉只用cc自带的loop确实还不太定，很容易walk around
- 的上下文，我感觉他们在review的时候讨论来讨论去...
- 我还以为秒了的意思
- 是说每一步都要review对autoresearch这种workflow太重了
- Hecate: overkill是指的还不能做的太好?
- 确实确实我也这感觉
- 我觉得每一步都应该review，但是应该decoupled的来做
- 翁大爷的狗@Rakuten: 是说每一步都要review对
- autoresearch这种workflow太重了
- 每一步结束的时候直接fork当前的sandbox，然后一条线去做review，另一条线去继续下一步
- 4月27日12:59
- 就是强行要求solid 实验结果而非推断?
- 我再尝试做这个事情大哥有啥好的idea嘛
- Hecate:大家觉得humanize对非代码修改，比如启动/
- 监测模型训练怎么样呀
- 最简单的就是让他不停地去生成图片看模型训练的一些参数
- 4月27日13:02
- 然后比如有没有loss spike啊啥的
- 但是似乎做不太好啊
- B4RRy:我再尝试做这个事情大哥有啥好的idea嘛
- 4月27日16:49
- 这么说来难道workflow会回春么
- 4月27日17:02
- 我对agent的理解经历过一些转换，首先reactagent的意义完全不用怀疑，但是workflow处于什么地位呢？一方面有
- 可能部分最佳实践流程十分固定、不希望agent随便探索的场景需要workflow；不过会不会模型逐渐增强，不需要担
- 心写在prompt/todo里的workflow软约束让agent跑偏，反而应该担心写死的workflow代码缺少了灵活性，没有办
- 法根据实际情况调整。不太了解真实生产中不同场景需求
- 4月27日 20:59
- 然后本周我会找我周围的朋友内测一下h2
- 大概下周或者下下周会公开
- humanize1（claude/codex插件版）就逐渐进入历史舞台了
- h2会具有h1的全功能
- 刘思皓:
- 4月27日21:10
- 本周末dev会进入main，然后beta会变成dev
- 严肃期待
- 但是大家可以根据自己的任务和工作需要进行定制
- 期待

---

### 4月28日

#### 原文 L15915–L15929

[回到原文件 L15915](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:15915)

- 4月28日10:25
- operation blocked by hook:
- anged during RLCR loop.
- k-6
- is not allowed during an active RLCR loop. Please
- cancel the loop with /humanize:cancel-rlcr-loop
- 4月28日10:55
- 我的短期dpsk测评就是，这个模型的执行和coding能力都还行，但是alignment做的不好，非常符合dpsk团队一直
- 以来重RL轻instruct的风格。
- 简单说就是，dpsk经常容易听不懂人话，但是一旦听懂了你要说什么之后，执行的还可以。
- agentic能力一坨
- 代入humanize的PBR框架的话，我觉得dpsk依然还是只能做一个廉价的B模型来使用。还是没法当P和R。
- humanize 确实不错
- 细化每个细节
- superpower

---

#### 原文 L16051–L16073

[回到原文件 L16051](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16051)

- GPT-5.5 xhigh is thorough — found 8 real issues! Much more rigorous than GPT-5.4.
- 用的是纯codex版humanize
- 好好生活天天减肥: 那你的模型一直都是4.6吗
- 之前是gpt-5.4，现在是gpt-5.5
- 机密项目
- Lurker: 看看git history
- codex执行，然后codex调用另一个codex来review吗
- 郑权: 用的是纯codex版humanize
- 对，周哥大概一个月前给humanize做的
- 我试过在copilot cli这样做(copilot都能用opus4.6-1m & gpt5.4模型)，但是最后没成，很烦
- 4月28日17:13
- 主要是copilot cli加了-s只要review的结果后会爆内存OOM，我都惊了这都什么雷霆bug
- pu
- 所以agent应该用rust来写
- codex品味不错
- agent时代任何东西都应该用rust来写，反正也不是真要你写
- 郑权: 对，周哥大概一个月前给humanize做的
- 真是AI一天脑内一年啊
- 虚宝AI运营两个月，感觉已经过去好久了
- 才两个月吗
- AI Agent 方法论迭代速度比前端还快
- 啊？才一个月吗
- 4月28日17:25

---

#### 原文 L16143–L16162

[回到原文件 L16143](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16143)

- superpowers 似乎把一些 humanize 的方法论融合进来了，也加了 review + revice
- 刘思皓: tune gpu kernel 修fpga啥的
- 我现在天天就是，把所有可以被复写的系统时间接口用权限封死，然后让humanize：给我把xxxx优化1000%(hard
- constraint)
- 怎么封死啊，求分享
- 香港科技大学研究助理教授徐策羽：我现在天天就是，
- 把所有可以被复写的系统时间接口用权限封死，然后...
- 我个人感觉的best practice是用singularity
- 刘诗楠：怎么封死啊，求分享
- 我一般肯定是开sandbox跑humanize的，毕竟大集群上不敢造次
- np
- 然后singularity这种fake-root的环境基本上里面的用户态进程权限很低，现在还没出现过jailbreak的情况
- 主要是ai提的很多优化点都很离谱
- 4月28日21:12
- 我也是
- 香港科技大学研究助理教授徐策羽:我现在天天就是，
- 把所有可以被复写的系统时间接口用权限封死，然后...
- 但我不会写1000%这么夸张
- 我一般写30%

---

#### 原文 L16215–L16228

[回到原文件 L16215](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16215)

- 那玩意是非常糟糕的设计
- Horace: superpowers 那个gen plan 基本上把代码写
- 完了
- 你无法教bashrc不会配的人用ai，超出了他的能力边界和你的职责
- 成为屠刀
- 开源芯片 agent flow 张宇鑫: 你可以成为任何人 包括
- 同事
- superpowers的writing-plan糟糕的很
- 我的目标就是当IC界掘墓人
- trustworthy agent?还是什么
- 开源芯片 agent flow 张宇鑫: 我就是搞这个的嘻嘻😄
- 生产级智能体调度叭
- 4月28日23:23
- 我能明显地感受到

---

#### 原文 L16233–L16252

[回到原文件 L16233](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16233)

- 就是不需要构建繁杂多智能体系统，只需要维护几个基本结构，然后剩下的东西交给scalinglaw
- 其实我觉得role based multi-agent是一个很懒的设计
- 比如说现在的humanize里面那个复杂的goal tracker系统
- 你完全有办法做更聪明的context engineer，而且这种role-based management本身就是人类低效的体现
- 其实可以用一句话全部取代
- 用一句prompt+一个反馈回路
- 能自动校准保证开发永不偏离
- 4月28日 23:29
- fot
- 怎么小美工也来做爱了
- 然后goal-tracker节省的上下文全部用来做真正的开发，而非维护flow本身
- 刘思皓:其实可以用一句话全部取代
- 变成gen coze claude，codex版本了?
- 现在的多智能体系统，有很多的上下文空间被浪费在机械流程的脚本过程上
- 那是不是等于把coze的ui智能体换成cc和codex
- 我最近聊公司里的别人写的xx验证自动化就是类似的样子
- 4月28日23:32
- 我刚刚看了一下coze

---

### 4月29日

#### 原文 L16269–L16320

[回到原文件 L16269](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16269)

- 还会遗留一堆 stale的 md 里面有 代码
- Horace: superpowers 那个gen plan 基本上把代码写
- 完了
- 这个link是?
- Luke:
- https://github.com/obra/superpowers/issues/649
- 4月29日00:35
- obra on Mar 12
- It's very much by desipn. This is how supersowers worksl
- 在design里写code的问题是会把上下文腐烂的速度超级加倍？
- https://contextarena.ai/
- 本质原因不是腐烂
- 是在"不该有精细程度的阶段，用一个精细的表达，去描述模糊的概念"
- 在不同的开发阶段，要么纯概念描述，要么纯代码描述
- 如果非要在概念阶段描述代码流程，建议伪代码
- 4月29日02:36
- eToolUse:Bash hook error: [${Cl
- Blocked
- ommits should stay local - no neet
- will handle commits locally until
- ed to push, use--push-every-raur
- start-rlcr-loop plan.md-push-e
- 关了 rlcr，好像还有残留 hook
- 可能太老了,升级一下
- 4月29日03:01
- 还是1.16.0
- 4月29日03:19
- 盼星星盼月亮盼着humanize2
- 4月29日03:39
- any day of this week, no push
- 4月29日06:08
- 基模能力在提升，harness也在往前走
- 4月29日09:12
- 这几天 gemini 我爬到的动态 benchmark 分数奇高，3.1 pro 实际使用体验确实也不错，但是 20 跟没法用一样，上
- 一档就是250有什么别的便宜渠道
- 4月29日09:19
- 群里大家觉得现在claude有没有国产平替啊？我想找一些给学生用，claude本身有点贵了
- glm (即答)
- agentic国模最高的山
- 他们的coding plan是不是订不上呀
- 那这个我不知道，我一直用内网部署的
- 你的use case是什么啊
- 我感觉除了养龙虾以外的case gemini都不算好
- 4月29日10:12
- kimi现在也不错

---

#### 原文 L16349–L16363

[回到原文件 L16349](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16349)

- kimi review 深度我个人体验有 gpt 级，但是有点过度 review，什么重要的不重要的甚至 typo 都给你通通列出来
- 能开票跟我讲吧，长期有一些购买需求
- 开源芯片 agent flow 张宇鑫: 我五一回来可能能开票
- deepseek适合当openclaw的管理员
- 我不知道，我是白嫖王.jpg
- 刘家昌:无问也没货啊（
- 然后再调codex，claude
- Lurker: deepseek适合当openclaw的管理员
- 我有一次 kimi 2.6 给我列了五十几个 review comments 还没停下来，赶紧给掐了（
- interesting
- 刘家昌: kimi review 深度我个人体验有 gpt 级，但是
- 有点过度review，什么重要的不重要的甚至typo都...
- 因为tool call有点bug所以我没深度用过k26

---

#### 原文 L16379–L16389

[回到原文件 L16379](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16379)

- 嗯应该是，只是因为我 vibe harness 然后另外一个 model somehow觉得它可以关掉 kimi 的 thinking 来省钱（
- coding。Gemini 就很迷，之前我用的时候他就是个大傻逼。但是这两天我让各个Al vibe了一个去爬每小时每天跑
- 出来的benchmark结果的工具，somehow把它排在了第一名，而我实际使用体验也有改善
- 翁大爷的狗@Rakuten:我感觉除了养龙虾以外的case
- gemini都不算好
- 就是那种，一下觉得它怎么突然那么牛逼，一下又果然还是哈吉米
- 所以有点想搞个 gemini 在我 benchmark爬出他牛逼的时候 give it another chance
- 但是发现 20 上面就是250

---

#### 原文 L16453–L16467

[回到原文件 L16453](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16453)

- Kimi K2.6 vs Claude Design
- 今天被夸了[萌萌哒R] prompt有
- 点长，都帮大家截图了！（这就
- 是发这条帖子的意义！）下个...
- 小红书
- 小红1书
- dpsk v4 pro做humanize review模型似乎还可以
- 4月29日15:21
- 2.5折多用用
- deepseek挂claude code上跑humanize效果咋样啊?
- 4月29日15:55
- 有format error，可能要自己写一个格式转换
- Arsene: deepseek挂claude code上跑humanize效果
- 咋样啊?
- 我现在还没调到bug free的程度

---

### 4月30日

#### 原文 L16790–L16835

[回到原文件 L16790](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16790)

- 因为我自己都没跑几轮
- 不过如果有人真的愿意用爱发电可以私戳我
- 现在失败/bug概率>90%
- 4月30日02:24
- aka我来招人帮我修代码的：)
- 或者做一些鲁棒性测试,纯用爱发电，能用在生产环境是不够格的.
- 跑了一晚发现从r2开始就去修pre existing的bug修了50轮
- 要么是plan没限定好
- 要么是你这个bug是个blocking
- 第二轮codex认为是high priority bug就开始—路狂飙了
- 4月30日02:34
- 申请
- myn具哈意用2
- 我正好在写企业级Agent服务，看看找个小老弟来打工
- 最小可行产品还是什么
- 翁大爷的翁大爷:mvp是啥意思?
- 翁大爷的狗@Rakuten: 最小可行产品还是什么
- 我我我
- 全场mvp吗?
- 我我我
- 4月30日02:39
- 就现在只是大概能跑，但是你得期望它会“失败”，而不是期望它能“成功”
- h2现在更像是一个flow编程语言
- 你得做比较多的后端适配(类似编译器里面的codegen，比如给不同的cli做对接)
- 这个编程语言和cli的通讯协议是什么？类似openclaw哪一种还是app server那种
- 模拟终端输入
- mcp这种糟糕的设计我肯定不会用的
- h2是个vscode插件
- 触发agent执行的时候会直接开一个vscode的终端来模拟输入
- 暂时没有但是那tmux搞一个很简单
- 4月30日02:45
- 主要是tui里面不好画这种图
- 刘思皓:
- 本质上h2是个AgentVM+flow编程语言
- 我做了一系列编译静态检查
- 比方说你如果在h2里面写一个原版的ralphloop
- 它会提示你上下文腐烂+漂移的“编译警告”
- 4月30日02:47
- mcp噶了然后这块协议群雄争霸
- 说起来最近A\在给mcp打补丁
- 哇我操原来mcp是24年的东西吗
- 这么久了

---

#### 原文 L16941–L16966

[回到原文件 L16941](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16941)

- 牛逼啊
- 泽文: 从零到交付：Agent 协作开发 Triton
- 从零到交付：
- RISC-V CPU 后端最佳实践
- 我还是想大家用humanize去转牛皮的项目的时候
- 泽文: 从零到交付：Agent 协作开发 Triton
- 从零到交付：
- Aet
- RISC-V CPU 后端最佳实践
- Triten ROSC-V CPU BRasS
- 要对自己的代码负责
- 能够说一嘴：humanize不是许愿器，
- Agent 物作开
- RISC-V CPU 后端最佳实践
- Ae
- RISC-V CPU 后端最佳实践
- 能够说一嘴：humanize不是许愿器，要对自己的代码负责
- 然后“整个代码库在你写完plan的那一刻，就应该在你心中全部写完了”
- 我觉得你践行了这一点
- 虽然是humanize vibe的，但是
- 我觉得你践行了这一点
- 虽然是humanize vibe 的，但是
- 不用定位到哪一行

---

#### 原文 L16970–L16990

[回到原文件 L16970](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16970)

- 4月30日23:25
- 4月30日23:25
- 已经一周没humanize了
- https://github.com/PolyArch/humanize/pull/51
- Humanize 1.16 正式合并了
- 刘思皓: https://github.com/PolyArch/humanize/
- pull/51 --- Humanize 1.16 正式合并了
- 4月30日23:30
- 五一假期，我要和社区朋友探索一下结伴 vibing，在线对
- 鸟哥这个赛道竞争也这么激烈吗
- 4月30日23:37
- 最高的山，最长的河
- 大家觉得AGI前会有一段至暗时刻吗
- 我怕失业程序员在街上把我砍了
- 湾区酱香饼/手抓饼/烤冷面赛道满了吗

---

## 5 月

### 5月1日

#### 原文 L16993–L17015

[回到原文件 L16993](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:16993)

- 5月1日01:07
- agent team 用个一两天，基本上所有agent的都是疯掉的状态，全是stale的信息
- yep
- agent team 还是太有闲钱了
- 没啥用，非常容易跑偏
- 5月1日01:10
- 七嘴八舌的，全是错的，信息轰炸我
- 需要控制上下文
- 1m上下文的模型不一定比200k的强
- 微软lan L.亿杨: https://contextarena.ai/
- 如果把agent比做神经元,我们要的是神经元有序放电
- 无序放电就变成癫痫了
- context这个数字已经不重要了
- 微软lan L. 亿杨: 1m上下文的模型不一定比200k的强
- context其实不关键确实
- 你需要的是一个协同有序的状态机
- 5月1日01:15
- 多次迭代>一次完美，
- 小步有序>大步并行
- 得cherry pick什么进上下文什么不进，我直接让代码impl的部分都子代理去写了
- follow-up。这下真睡觉开发了。
- 微软lan L. 亿杨:“后一个依赖前一个，按

---

#### 原文 L17044–L17067

[回到原文件 L17044](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17044)

- 都是错的
- 现在humanize平均—天被 clone 200次
- 其实还是太实诚了
- 5月1日01:42
- 像pua 这种估计下载量多一个0打底
- 当然看到那种爆款超多star的我还是会羡慕一下
- 其实是每换一个机器都得重装一下humanize
- 然后读一下skill.md发现没什么可以借鉴的/都是踩过的坑
- 硬撑
- 5月1日01:47
- XS
- Lei Wang: 其实是每换一个机器都得重装一下
- humanize
- 我装的都是自己 fork的 humanize(
- Lei Wang: 其实是每换一个机器都得重装一下
- humanize
- ai入职太快了，只需要一次prefill，给人讲要讲好几天，人要看好几天
- 研究管理ai和管理人的异同，也能发论文
- 我现在最大的问题是：
- 1. 磨刀:搞好用的AI开发方法论工具
- 2. 砍柴: 做那些暂时没法用AI自动开发方法论工具做的项目
- 这两件事没法放在同一天做
- 新时代的人月神话

---

#### 原文 L17170–L17180

[回到原文件 L17170](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17170)

- 5月1日06:33
- 我只要不起humanize，每天正常就是500M上下
- 而且主要是我现在主要精力都在这上面
- 刘思皓:我现在最大的问题是: 1. 磨刀: 搞好用的AI开发
- 方法论工具2. 砍柴: 做那些暂时没法用AI自动开发方...
- humanize一天就要干爆我周额度的百分之25
- 太伤了
- 能外包给humanize的任务我都外包出去了
- 我现在策略变成给humanize先做好铺垫把要人监控的小规模实验和结果拿到了完善计划再让他做
- 15:38
- 始在睡觉约时候，起用LCR实现

---

#### 原文 L17229–L17240

[回到原文件 L17229](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17229)

- humanize有没有token优化策略，昨晚跑—个loop花了1.5B
- codex原生支持ralph loop了，来试试
- /experimental开启goals，然后/goal 设定目标
- 站子
- Felipe Coury
- @fooury
- /goal also lands in Codex CLI O.128.0.
- Our take on the Ralph loop: keep a goal alive
- across turns. Don't stop untilit's achieved.
- Built by my co-worker and OpenAl mentor Eric

---

### 5月5日

#### 原文 L17524–L17570

[回到原文件 L17524](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17524)

- 这是否是一种特别广义的 SMT
- exactly
- h2的核心设计思路
- 感觉可以搞一个Ilm下的Conflict-Driven Clause Learning
- 施加约束就是stop hook
- agent 去实现东西感觉越来越像约束求解问题了，给定一系列constraint，去获得在解空间内的一个合法解。
- 这是否是一种特别广义的 SMT
- 能直接证明吗？
- z3 结上?
- SMT +1
- 赵雪岩:这是否是一种特别广义的SMT
- 感觉目前的规模还用不上solver
- 把Ⅱm学到的经验变成冲突子句，让Ⅱm更快的收敛到结果
- 有点像有了oracle machine 以后，大家只需要关注 verification 是否 polynomial
- 我感觉这个有点 make sense
- 的收敛到结果
- 5月5日18:44
- 我观察到ai实现的时候有时候【会走回头路】
- 还有【当距离一个大目标很远的时候，有时候没办法选择最快到达大目标的路径】
- 这些感觉有点类似于 sat 求解那些算法的发展
- 5月5日18:56
- 但是你这个仅限“build”型任务
- constraint solver还不够啊，还得有开放目标，这就是auto research了
- 其实我这几天想了想代码型任务无非三种
- essentially，看看gurobi都干了什么，我们在agent的domain也干一遍
- 得让我先毕业吧
- 香港科技大学 研究助理教授 徐策羽: constraint solver
- 还不够啊，还得有开放目标，这就是auto research...
- 启发探索型，增量维护型，从零构建型
- 类似迪迦的飞行型，复合型，强力型
- 我觉得我心目中的agentflow需要被定义的主要是三点
- 我们真的需要那么多flow吗
- 我们能不能学习传统高性能solver的implementation，把路径选择本身heuristic化+并行化
- constraint
- opt target
- heuristics

---

### 5月6日

#### 原文 L17742–L17797

[回到原文件 L17742](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17742)

- 可以可以主要是经常晚上跑然后早上起来发现codex review改了很多其他代码
- 刘思皓:你要是想跳过后一个，直接esc就好了
- 那感觉最好的办法是直接git checkout
- 5月6日08:55
- 把COMPLETE后面的commits都扔了
- 唯结果论，对程序员心态的巨大挑战
- #硅谷徐老师 #ai #人工智能#
- 程序员#质量重要还是结果重要
- #硅谷#代码质量
- 小红书
- 小红书
- 来发现codex review改了很多其他代码
- 5月6日09:00
- 我之前也遇到乱改worktree 后来就搞成 每个机器只跑一个agent了然后monorepo用sshfs 共享了
- 什么是乱改worktree
- 就是我可能同时在跑多个任务
- 一个机器上
- 改同一个repo吗?
- Windows Xp: 改同—个repo吗?
- gitworktree没法隔离吗?
- worktree不久隔离了?
- 我就是用的worktree
- 我也想问, worktree不是已经隔离了？
- 那它怎么个乱改法
- 但后面不知道为什么对话多了就开始到别的wprktree去了
- 就他改着改着说“咦怎么出现了一些无关的改动我先不帮你提交这些”这些diff我一看是我另一个agent的任务
- 5月6日09:06
- 都是幻觉了.
- plan里写的是 在xxx worktree做 对应的remote branch yyy 和对应的remote PR url zzzz
- 感觉worktree要分开起一个session?
- 我的worktree其实都是手动维护的
- 每个worktree里面起一个rlcr
- session是说的cursor里的tab么
- 我拒绝让automation动worktree
- 感觉会出大事(bad)
- codex的话只有在worktree启动的agent或者创建那个worktree的agent有修改的权限
- 不是单独起一个rlcr并且感觉plan也不要share)
- hazelnut: session是说的cursor里的tab么
- 5月6日09:11
- 那好吧
- 我觉得我得在plan合规检查里面多加几个检查
- 禁止创造worktree
- 我感觉小于等于三个worktree还好
- 超过5个worktree在一个rlcr里面就比较有可能爆炸
- 我自己的 flow 严禁 worktree，因为我觉得人类和 AI 都只能 track 一条线，我过去所有的 worktree 的 agent 经
- 历，除了那种长时间 explore的，都 merge地狱
- 我还好
- 我人工切分的worktree
- 前提是我切分得特别好
- 5月6日09:18
- 但是你真的得非常手动地维护worktree
- 一但有一点conflict就必须立刻合并
- 要不然就再也合并不回去了

---

#### 原文 L17844–L17861

[回到原文件 L17844](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:17844)

- 香港科技大学研究助理教授徐策羽:我一般直接喂
- humanize出来的plan效果就不错
- 我目前的体验是，无论codexgoal还是opencode还是humanize，都需要先一小步，然后再一小步，然后在一小
- 步。
- 尤其是那种从0开始的repo，目前我还没有达到这种一个prompt构建完一个10w行代码的项目的效果。
- 对，你直接"/goal去跟着plan.md做"，就可以了
- 刘诗楠:喂给goal吗
- 公司会积累大量的业务流和评判指标积累
- 那么怎么看待把这些自动化规则用不同的harness方法，gola humanize做迁移
- 最近做ai业务服务经常遇到的问题
- 17s
- 5月6日22:43
- 我算成本似乎不是每个人都有机会使用harness编程
- 开源芯片 agent flow 张宇鑫: 我算成本似乎不是每个
- 人都有机会使用harness编程
- Overall Al Capability

---

### 5月7日

#### 原文 L18076–L18089

[回到原文件 L18076](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18076)

- 时，就遭不住了
- shineZ: 不用 humanize的3开太累了
- :一直切上下文对前额叶不太好...
- 聊天记录
- 哈哈，我也是
- 刘思皓: 我古法最多双开
- 古法的bottleneck在worktree
- 5月7日09:38
- code slop 也多起来了
- 我现在都不是很敢让它连续改两次plan
- 我觉得维护性质的工作基本被解决了
- 但是从头构建和探索性质的任务还是有点困难
- 5月7日 09:46
- smt 是啥

---

#### 原文 L18165–L18179

[回到原文件 L18165](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18165)

- 这种拟合本身就是一种压缩
- 不我这里说的调度专指agents节点可通信的边
- 5月7日12:24
- 只是“subagents禁止通信”的泛化版本
- 我感觉最适合agents的组织调度模式，可能是个hierarchical crossbar
- 刘思皓:我感觉最适合agents的组织调度模式，可能是
- 个hierarchical crossbar
- 就是搞五个小团队，小团队内部所有人发给其他所有人的消息都是团队内可见的
- 对外只暴露一个agent
- 然后五个agent自己又组成一个全连接网络
- Claude code的agent team感觉就是这么搞得
- swarm agent teams有一个很大的区别
- 它里面的队员可以绕开manager单独发消息
- 5月7日12:30

---

### 5月8日

#### 原文 L18294–L18431

[回到原文件 L18294](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18294)

- nb
- (我刚给自己加上 multiagent dream
- 刘思皓: dream: 群里讨论过了，建议关掉 outcomes:
- AC Multiagent Orchestration: 好东西, h2正在折腾...
- auto-dream真的不会把你的memory搞爆炸吗
- auto-memory已经把我之前的好多claude.md搞爆炸了
- 5月8日05:02
- 5月8日05:41
- 主要是我觉得implicit memory/rule这件事有点吓人
- memory/rule/claude.md在claude code里面的优先级太高了
- 隐式地对这部分东西进行修改，有点盗梦空间的意思
- 5月8日 05:49
- Note: In popular culture, "Inception" also refers to the 2010 Christopher Nolan film about infiltrating
- dreams, which popularized a colloquial usage involving the act of planting an idea in someone's mind.
- 这个关于电影的介绍，某种意义上和群里之前的讨论非常契合
- 可以往claude.md投毒
- 关键是claude.md优先级实在是太高了
- 5月8日06:06
- m   型
- 刘思皓: auto-dream真的不会把你的memory搞爆炸
- 5月8日06:15
- 我以为你的multiagent-dream是起agent让它帮你写
- @Mr周半仙cc
- 如果claude.md的地位并非类似rules差不多的高优先级，我觉得Auto-dream是合理的
- 关键是claude.md优先级实在是太高了
- 5月8日06:06
- m m   型
- 我以为你的multiagent-dream是起agent让它帮你写
- 还是说你自己写
- 5月8日 07:05
- agent 帮我写
- 5月8日10:02
- 它写啥你看嘛
- 5月8日10:11
- 外挂记忆系统大伙有用的吗
- claudemem那种?
- hook
- 各种 vector吧
- 我用过各种graphrag
- 以及claudemem
- 最后发现………不如planing-with-files
- 还是规模问题吧
- 不过graph 用的啥 适合coding么?
- 现在每次都用plan with file吗
- 刘思皓: 最后发现.....不如planing-with-files
- 我觉得最本质的问题是ai不太能意识到“时间”
- 一个好的记忆系统需要能区分长短时记忆
- 我直接用humanize的bitlesson
- 饽饽博: 现在每次都用plan with file吗
- 5月8日10:17
- 那个很早以前了2024年的时候
- 洋洋阳: 不过graph 用的啥 适合coding么?
- 7伤则哈aenkit:
- 感觉效果都不好虽然看上去很酷炫
- 你可以画知识图谱啥的
- 5月8日10:19
- 对于需要聚合的场景有全局观
- graph擅长一些吧
- 不懂但是A\专门出过一个博客讲过这事
- 最后都是直接走瞬时的grep/rg
- 什么场景要有全局观 claude.md做索引+grep不行吗
- 洋洋阳: 对于需要聚合的场景 有全局观
- 似乎只有cursor还在用GraphRAG
- 这个其实蛮好解决，在所有tool call pair里面插入时间戳
- 刘思皓:我觉得最本质的问题是ai不太能意识到“时
- 间“
- 就很有时间意识了
- yep
- 饽饽博:什么场景要有全局观claude.md做索引+grep
- 不行吗
- 就是不知道为啥大部分harness都没这么搞
- 黄澍之: 这个其实蛮好解决，在所有tool call pair里
- 面插入时间戳
- 时间观念啊
- 我没发现时间会影响什么
- commit有时间啊
- 比如一本小说里找隐线
- 饽饽博: 什么场景要有全局观 claude.md做索引+grep
- 不行吗
- 事件之间的时间线这样
- 比如你问ai我们五分钟前搞过什么这种
- 会人味强很多
- 因为大多数场景你并不需要时间这个概念
- soga..我舍不得浪费token去问这个
- 跟ai互动貌似没太有时间观念
- 只有“长短时记忆系统”这个场景我觉得需要时间
- 其他基本走“事件触发”就够了
- 为啥deepseek便宜成这样..加上去也就是多1%的token消耗而已
- 老子熬夜两三点跟它battle 睡去了第二天起来 它还是赶你去睡
- 5月8日10:24
- 对啊因为大部分harness都只有一个“看现在几点”的tool
- 这个好奇怪你用的什么工具，会读系统时间啊
- 洋洋阳: 老子熬夜两三点跟它battle睡去了 第二天起来
- 它还是赶你去睡
- 应该是聊天里面带入了
- claude是直接bash的
- 我做harness写记忆系统也没加时间。
- 时间
- 5月8日10:25
- 我觉得时间对知识无意义
- 除非那种需要时间属性的知识
- ai只能模拟时间
- 我说的时间更多的是“相对任务”的时间概念
- 前后之分？
- 我觉得不是的，AI是能“感受到”时间的，当你给他的所有看到的信号都强行打上时间戳之后
- 本质上对于ai只有无状态的计算
- 这是claude code?
- LZ:
- 我希望的理想记忆系统是，能够自动识别到我大概在做啥，然后加入一些短时规则，然后这件事做完之后，自动移除
- 饽饽博: 前后之分?
- 重启就行conversation存储出bug了
- LZ:
- 刘思皓:只有“长短时记忆系统”这个场景我觉得需要
- 时间
- 虽然是这样的，但是context本身定义了agent身份的本身？Ilm call虽然是stateless的，但是llm call也不是agent啊
- 洋洋阳:本质上对于ai只有无状态的计算
- 我需要的是“任务相对时间”
- 不需要的是“绝对世界时间”
- 洋洋阳:龙虾爱马仕都在往这个方向
- 这个很难写代码有时候调一个小bug两三天
- 对啊所以这也是我觉得现在记忆系统的问题
- 记忆系统优先级太高了
- 我不放心交给agent
- 而且说到底，要手写的东西也没多少
- 记忆系统应该有大厂下手做啊现在llm跑的很快mem没有跟上
- 5月8日10:31
- claude那个auto dream几个月前出来的时候
- 第二天发现我项目记忆炸了
- 就赶紧全关了
- 可以尝试一下我们的这个skill

---

#### 原文 L18436–L18466

[回到原文件 L18436](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18436)

- 原来还不到两个月
- 我感觉记忆系统里面最难做的东西是如何判断“过时”这个概念
- 5月8日10:43
- 不过横向比较下来，短时记忆系统目前的趋势基本都是一样的：
- - plan-with-files的findings.md
- - OpenAi的ExecPlan里面的Surprise & Findings
- - humanize的bitlesson.md
- 维护—个瞬发/易失的md文件，不纳入claude.md/AGENTS.md
- 5月8日10:52
- 这个最终还是要model侧解决
- 我觉得单harness做是不合理的
- 我有点怀疑model侧能做这件事
- 记忆本身是个强规则高优先级的通道
- 你要让模型能自己判断这个“规则”是否过时
- 需要model-harness co-design
- 纯harness的记忆就像人类写笔记
- model-harness codesign才能实现见到自己以前写的笔记联想到整个知识场景
- 很有道理啊，需要训练一下
- 我觉得“做梦agent”的基座模型得和干活agent不一样
- 5月8日10:57
- 晚上codex做梦删除记忆
- 这里很矛盾啊记忆实际上是个“宪章级”的规则
- 你训练模型自己删除过期记忆
- 实际上是在训练模型做jailbreak
- 反正现在感觉就是不能让gpt记忆，废话太多了
- agree
- 5月8日11:06
- 把记忆都fine-turning到模型里去
- 每个人都存一个lora吗
- 感觉做推理的大哥不会同意

---

### 5月9日

#### 原文 L18601–L18614

[回到原文件 L18601](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18601)

- 5月9日04:37
- 你是不是忘记在humanize plan里面说：请用superpowers的opus subagent-driven并且遵循tdd干活
- 原来要这样
- 是要 subagent，这样快点
- 单 agent 太慢了
- 所以还是要用 superpower
- 5月9日05:09
- superpowers 好用的
- - superpowers的brainstorming + subagent-driven
- humanize已经内化的 superpowers
- - tdd
- superpowers不好用的
- - writing-plans
- 5月9日06:04

---

#### 原文 L18630–L18643

[回到原文件 L18630](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18630)

- 5月9日06:45
- subagent driven不太行，稍微弱一点的model经常看到subagent的output就开始自己干或者跳过review了
- 刘思皓: superpowers 好用的 - superpowers的
- brainstorming + subagent-driven humanize已经...
- 我魔改了下让subagent严格只返回一个accept/reject和—个opaque log path，main agent完全只是机械地执行
- loop和传递log path across subagents，效果好不少
- 5月9日07:44
- 你需要使用@刘家昌的奇技淫巧
- 阮震元(Zain):subagent driven不太行，稍微弱一
- 点的model经常看到subagent的output就开始自己...
- 在claude.md里面加入：
- 相信你的Subagent,请你给它们分配完整且正确的任务，无论这些任务有多复杂和耗时
- claude写长了会有一些忘掉

---

#### 原文 L18725–L18737

[回到原文件 L18725](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18725)

- 泽文：我在想，能不能把spec的复杂度变成渐进式的，
- 我重新反思了一下“白天写spec，晚上转humanize”这个模式
- 讲道理不太对
- 我觉得现在最适合我的模式是：上午拿cc一把铺开今天要做的事情的“起点”
- 下午开始和codex古法
- 这样我心智压力小一点
- 一整天想一个2千行的spec，我心智压力太大，晚上转humanize睡不安稳
- 不过我感觉这个模式仅限“从头构造一个大型新东西”的任务
- 是啊，我做梦脑袋里者
- 其他“知识迁移”的任务humanize基本都还能handle
- 我觉得LLM在构建指令集这种任务上面，效果尤其垃圾
- 垃圾的意思到不是它想的方案不好
- 5月9日09:33

---

#### 原文 L18786–L18912

[回到原文件 L18786](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18786)

- 我一直在群里建议这么做的呀，能一整天不发生任何压缩
- Canaan:如果所有的coding操作都让subagent来处
- 理，那么主session得context是不是可以保持很久...
- 太牛了，是不是需要在全局claude.md配置上这个
- 刘思皓: 相信你的Subagent.请你给它们分配完整目正
- 确的任务，无论这些任务有多复杂和耗时
- 差不多
- 不过我现在觉得效果最好的东西是codex
- 我现在个人体感最佳的方法学是先opus铺开大概1-2小时
- 剩下就全部codex
- 我也是全用subagent
- 5月9日14:15
- codex你也可以全用subagent干活
- 并且让他作为prompt enhancement
- 给了一套标准话流程
- 但是我不知道为啥同一个模型接入cc会更听话
- 比如强迫他读文件以及思考每一个任务有没有可监控指标多反思有没有违规和提升空间
- 交接的过程中是重新gen一个plan出来，还是跟cx说接盘这个rlcr
- 刘思皓: 剩下就全部codex
- cx全面接盘
- 不过我最近重回古法了
- https://x.com/trq212/status/2052809885763747935
- 5月9日14:20
- 你是今天群里第三个发这个的♀
- 香港科技大学 研究助理教授 徐策羽: https://x.com/
- trq212/status/2052809885763747935
- 5月9日14:26
- 看来大家都是hackernews的忠实用户
- 我觉得未来六个月人类学估值还得再涨
- 然后大家就会意识到其实codex更好了
- 半年前人类学每发一篇博客我都熟读并背诵
- 最近的博客质量越来越低
- 5月9日15:20
- 也不好说
- 他们现在拿那么多吗
- AI变化太快了，半年谁也说不好
- 5月9日16:01
- Some of what we're working on might be easier to explain if I can show it to you in a web browser. I can
- put together mockups,
- diagrams, comparisons, and other visuals as we go. This feature is still new and can be token-intensive.
- Want to try it?
- (Requires opening a local URL)
- 这个是cx新feature吗
- and can be token-inten
- 快速跟进(抄袭)cc版本的
- 轮脑暴，确16×64B这个新
- 张东宇: Some of what we're working on might be
- easier to explain if I can show it to you in a web ...
- 张东宇:看起来使用了brainstroimg
- 我调
- 5月9日16:09
- 轮脑暴，确16 ×64B 这个新
- instorming skill)
- 看起来使用了brainstroimg
- 这是自动用了superpowers吧
- 张东宇: Some of what we're working on might be
- easier to explain if I can show it to you in a web ..
- brainstorming 的 frontmatter 有很多强制性断言，agent 很容易自动去使用
- 5月9日16:34
- https://www.rss.hku.hk/contracts/ipr
- 具体的条例在这儿
- 5月9日17:03
- 发错群了
- 北京开源芯片研究险TFDC
- 谈芯沙龙
- AI在长程任务工作的探索
- 及香山应用实践
- 5月9日18:37
- 给sihao哥赋能了
- 北点开源芯片研究究TFDC
- 读芯沙龙
- AI在长程任务工作的探索
- 及香山应用实践
- 5月9日18:45
- 徐哥
- 转发了
- agent工程师
- 宫一
- 徐哥
- 宫一
- 转发了
- agent工程师
- 泽文:帅哥你谁
- 回头搞点礼品让你来讲ai qemu👩👧
- 5月9日18:50
- 啊这，原来是宇哥
- 宫一
- 太帅了
- 5月9日18:51
- tnbl
- 开源芯片 agent flow 张宇鑫:
- E4
- 5月9日18:57
- tnbl
- tnbl
- 5月9日21:14
- woc?
- tnbl
- tnbl
- 5月9日21:20
- 5月9日22:04
- 我现在买了cursor cc kimi-code-plan (还有个垃圾minimax code plan)除了cc是5x 都是最低额度
- 刘思皓: https://x.com/cursor_ai/status/
- 2052432778743210127?s=46
- 现在很想升级cursor取消订阅cc
- 5月9日 22:46
- cursor可能不耐用
- 它算是直接买的API
- 还是cc max这种订阅的划算
- 5月9日22:55
- (还有个垃圾minimax code plan)除了cc是5x都是最低额度
- 我现在买了cursor cc kimi-code-plan
- cursor体感好。cc每次打开了解project建立context都大费token。cursor自建了一套index系统
- 而且opus有时候抽卡转不过弯来，要新建session。cc直接context不动，换个model继续抽就行
- 那个index系统面对llvm这种代码库就炸了...
- 5月9日23:03

---

#### 原文 L18924–L18961

[回到原文件 L18924](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:18924)

- 尽量做到3，1和2就靠你了
- 白天写完一个巨型spec起humanize对我心智压力太大，最后还不如一步一步交互式地构建，这样我每一步都知道它
- 在干什么
- 是的呀我觉得3很重要
- 1烧token和2造flow是比较简单的
- 可能用 humanize 来 debug 或者单点性能优化更合适
- 我从来没有弄过巨型 spec
- 我现在造humanize2的时候，遇到最大的问题是，我觉得用humanize2的用户，要么：
- 1. 完全脱手，无法对自己的代码负责
- 2. 完全了解，心智负担太大
- 写了一个修bug的 plan搞定了。
- 5月9日23:08
- 不是巨型 plan
- 不用humanize，只靠prompt我也搞过
- 我想我的本质问题是：我觉得现在的问题并非scale-up，而是scale up的过程中，如何保证：如果那一天ai挂了，造
- 这个东西的人怎么手动修。
- humanize2的规模scaleup上去了，你怎么设计一套机制，保证人类知情
- 5月9日23:09
- 我的朋友圈都是这样的
- Luke: 下面拍一个饭的照片，有点好笑
- 完全脱手对我来说风险还是太大了
- “巨型agentic自动化系统如何保证人类设计者时刻知情”
- 我觉得这是一个关键问题
- +使用者
- 刘思皓:“巨型agentic自动化系统如何保证人类设计者
- 时刻知情”
- 烧token+造一个flow自己迭代，这两件事自己我觉得已经基本上被解决了
- humanize那个“启动前要考试”的机制我觉得算一个机制
- 刘思皓:“巨型agentic自动化系统如何保证人类设计者
- 时刻知情”
- 其他我还没想好要怎么设计
- 我写代码有启动困难+完美主义型焦虑+执行功能卡顿，humanize只能解决我的启动困难/执行功能卡顿，完美主
- 义型焦虑恰恰是我最重要的一点，也是我有价值的地方
- 5月9日23:15
- humanize二阶段的那个codex review还不够完美主义吗
- ，我右白的a
- 不够

---

### 5月10日

#### 原文 L19090–L19197

[回到原文件 L19090](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19090)

- 5月10日22:57
- 最近要毕业+h2开发比较紧张，pr我都没什么空看，我给你maintainer权限吧
- 泽文: https://github.com/PolyArch/humanize/pull/
- 151
- 你帮我看看
- 5月10日23:05
- 比较大的困难是，我自己造出来的h2，并不能帮助到我自己毕业的工作，于是我又回归到了纯古法，原因并非自动化
- 我现在对：“超过15个智能体自动构建出来的代码库要做到“全知全能”，同时心智负担不重”这件事不知道怎么
- 办。还想问问群友的意见
- 看起来observability是6202年agentic research的重要问题
- 刘思皓:比较大的困难是，我自己造出来的h2，并不能
- 帮助到我自己毕业的工作，于是我又回归到了纯古法...
- 是的啊，开发效率不能以牺牲“人类掌控度”为代价。我怀疑最近aws/coinbase各种奇怪宕机都是“不负责用AI”的体现
- 张子健: 看起来observability是6202年agentic
- research的重要问题
- 包是的兄弟
- 为代价。我怀疑最近aws/coinbase各种奇怪宕机都...
- Amazon哥们跟我吐槽过很多次了
- 5月10日23:10
- 测试CI都不完善写完了直接推
- 这很难不炸
- 可以去十年前开始的各种云计算的可观测性研究找找idra
- 刘思皓：是的啊，开发效率不能以牺牲“人类掌控度”
- 为代价。我怀疑最近aws/coinbase各种奇怪宕机都...
- *idea
- 现在我们是要观测大量agent的ctx和行为
- 我联系不起来这两个事情
- 没什么共同性吧
- 我觉得这个问题应该要限定成：人类工程师不可退让的边界问题
- 5月10日 23:18
- 我想要解决的是：假设有一天全世界范围内的ai工具都不能用了，如何继续解决一个系统bug
- 这个很难吧相当于问一个团队的leader，如果有一天你们团队就剩你自己了，如何继续解决一个系统bug
- 这个我最近也在思考，我做了一些尝试，让 agent的工作尽可
- 有文档一定要丰富，并且保持可读性；还有一点就是，尽可能
- 互友好的
- 5月10日23:22
- 文档丰富，怎么解决stale的问题?
- 我的写法就是写非常多的md，不断让他总结到md
- stale.太严重了
- 文档丰富在vibe时代已经是贬义词了
- 我觉得软件工程的AGI如果今年不降临，最迟也就是明年了，但我完全无法接受纯vibe/许愿这件事。我觉得未来ai发
- 展方向反而不应该是：全自动，反而应该主动去在关键步骤引入human in theloop
- 我觉得ai coding本质上是把一些设计决策外包给了agent，外包粒度大的就是wish coding，小一点就是spec coding。
- google搞了一个许愿编程workload，目前测试下来都是0分，给一个项目文档和需求，要求结果正确
- 这样有两个好处：
- 1. 关键点引入人类专家的洞察，对整体效果有巨大提升
- 2. 保证人类可知
- 上次看同事开会掏出来一个ABCDEFG的文档，他共享屏幕自己都找不到要说的东西在哪了
- 5月10日23:27
- 对质量要求高的东西依然应该line byline review
- 那就是把关键洞察写进spec，然后在agent去实现的时候，找到办法让人类快速了解agent是怎么实现的
- 刘思皓:这样有两个好处:1. 关键点引入人类专家的洞
- 察，对整体效果有巨大提升2.保证人类可知
- 不能写代码快了就把传统质检流程也废了
- 不过后面考验一个工程师的能力，看他对系
- 与其想各种花活来补救 不如老老实实line by line review
- 尤其底层软件或者稳定性要求高的场景
- My Al Development Curve
- Stage 3:
- Haman in the Loop
- s not idol
- Time
- 画了个图
- 我现在就在stage3
- Time
- 画了个图
- 我现在就在stage 3
- 5月10日23:32
- 我紧跟先知群主的步伐
- 我公司的项目一直都是stage3
- 自己的项目短暂的stage2过
- 好像问题在于不能联网
- 段震伟: google搞了一个许愿编程workload，目前测
- 试下来都是0分，给一个项目文档和需求，要求结果...
- 我去年11月份开始搞humanize，1月份搞出来的时候把我自己吓傻了，然后决定速度毕业找工作了
- 现在看起来感觉human还能撑一会儿
- 我感觉大裁员估计还是会发生，听说下周LinkedIn裁员？但是我现在觉得，ai的发展应该不会往一个究极全自动的方
- 向发展了，一个好的ai系统应该有很多主动的human in theloop过程
- 矫枉必过正
- 老板们的思路肯定是裁了再说的
- 5月10日23:41
- 笑死了都是自动生产的，都没看过
- 翁大爷的狗@Rakuten:上次看同事开会掏出来一个
- ABCDEFG的文档，他共享屏幕自己都找不到要说的...
- Luke:好像问题在于不能联网
- 5月10日23:39
- 我感觉我同事没有洞察
- 我感觉coding和青岛啤酒厂产线没区别
- 不就是良率/产量/验证封装
- 但如果生产线本身是vibe出来的
- 停转了咋修
- 生产代码的良率上来了就真跟啤酒生产线一样了
- 5月10日 23:46
- 厂家负责，然后送几个fae线下维修观测质量
- 刘思皓:但如果生产线本身是vibe出来的
- 机器厂家
- 厂家：我也是vibe出来的
- 我消费者买了回不了本就要维权
- 他用人还是ai 消费者不管
- 怎么兜底
- ai给我的感觉就是把代码生产过程更方便的物化成 token/人月计费
- 我同意，所以我觉得厂家需要维护一套机制/团队
- 在ai完全炸了的情况下还能手动修

---

### 5月11日

#### 原文 L19198–L19200

[回到原文件 L19198](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19198)

- 5月11日00:32
- @Lurker 佬这个每round 1-2 AC相比于之前的每round把所有AC铺开有明显的行为改善吗，感觉现在rlcr跑起来
- 需要的轮次更多了

---

#### 原文 L19434–L19443

[回到原文件 L19434](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19434)

- 我的用法不对么，在codex cli里直接call .sh?
- 纯codex是codex build codex review，直接跟它说启动humanize loop就行
- 5月11日22:47
- 也可以用$humanize
- 5月11日23:20
- 正解，或者直接问codex：这个humanize仓库里的纯codex版humanize rlcr怎么用
- 高渐远: 纯codex是codex build codex review，直接
- 跟它说启动humanize loop就行
- 问了，然后他既没有反问也没有正常进loop，跑了一步就commit说我完成了
- 0:22

---

### 5月12日

#### 原文 L19446–L19463

[回到原文件 L19446](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19446)

- 5月12日02:49
- 让codex给你装纯codex版humanize
- 翁大爷的狗@Rakuten:问了，然后他既没有反问也没
- 有正常进loop，跑了一步就commit说我完成了
- 5月12日07:20
- 尝试了下claude新出的agents manage，感觉还行，相当于多session 在一个界面里完整展示，不需要起多个
- terminal 来回切换了
- https://claude.com/blog/agent-view-in-claude-code
- 5月12日07:46
- 感觉各个厂进展太快了
- Cursor的SDK和/orchestrate
- fol
- 5月12日 08:06
- 28号 openai要出agent sdk
- 是啊，感觉是很常用的功能，他就是不断把常用的功能集成进去
- Canaan: 尝试了下 claude 新出的agents manage,
- 感觉还行，相当于多session在一个界面里完整展示..
- 5月12日08:12

---

#### 原文 L19472–L19562

[回到原文件 L19472](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19472)

- 想来想去, h2本质就是个managed agents with static rule check
- 但我感觉本质障碍还是没有太解决:怎么提高人类的掌控度
- 众口难调
- 互相蒸馏吗
- 我现在有一种我当时从cursor切换到claude的迷茫感
- 不知道怎么设计一个流程，能够在100x生产力的情况下
- 5月12日08:29
- 保持人类掌控度也100x
- Build Hour: Agents SDK
- 5月12日08:34
- 确实
- Luke: 28号 openai要出agent sdk
- 这些harness或者sdk可能不到一年就被模型能力本身吃掉了吧
- 想来想去只有SDK才是正解，之前那个截获终端的方式做的h2实在是很难让我自己满意
- 对...
- 力本身吃掉了吧
- ai.时代真是天上一天人间一年，等一等就啥都不用做了
- 刘诗楠:这些harness或者sdk可能不到一年就被模型能
- 力本身吃掉了吧
- We hordie the loog. teols, ans durable surcation
- OILLE
- 是的 sdk早就有了吧
- 刘诗楠:这些harness或者sdk可能不到一年就被模型能
- F1L8 SEARCH
- 是的 sdk早就有了吧
- 是，但这波SDK的主要推点是并行和沙盒
- 它允许你的沙盒环境在云之间无缝迁移
- 本质上就是之前的cloud run
- 5月12日08:39
- 现在暴露给用户了，让用户自己写
- @Entropy你的模拟退火来了
- 而且SDK里面有非常原生的 human in the loop
- https://openai.github.io/openai-agents-js/guides/human-in-the-loop/
- 5月12日09:41
- 能把我的dpsk flash模型给退火成5.5吗
- 那我找你进货了
- 香港科技大学研究助理教授徐策羽:能把我的dpsk
- flash模型给退火成5.5吗
- 5月12日09:52
- @刘思皓先设计一个10×保持的
- 可以啊
- 我来try一下
- 能把我的dpsk flash模型给退火成5.5吗
- 可以启动10个cc就达到100x了
- 关键是人类的脑力是固定的啊
- 你如何用一倍的脑力
- 换10倍的掌控
- 你只能1/10抽样考试
- 想起了安全计算只把最核心的部分搞进去
- 有些东西不用掌控能隔离出来
- 5月12日10:00
- 那得是1/10的层级考试了
- 5月12日10:00
- 有些东西不用考试
- 比如写的程序连编译器都过不去,regress过不去
- 用reed-solomon code 编码知识并在随机点上抽样检查(大误….
- 刘思皓:你只能1/10抽样考试
- 个这样的决策树，你抽到这样四个做考试并且搞清楚，效果大概率不如你把前面三个决策点搞清楚。
- h2可以很轻易做到一些“噱头”，比如“大规模智能体协同xxxx”
- 但我觉得最后还是得落到“人类负责度”上
- 但你仍然搞不清楚第四层的决策细节
- post-AI时代不被人类理解/掌握/负责的代码
- pre-AI时代没有经过测试的代码
- 5月12日10:07
- 如果plan只cover前几层决策树，那要想高效理解agent产生的巨大决策树，本质上是解决拿到一个材料，快速学习的问题
- 王邦彦: 用reed-solomon code 编码知识并在随机点
- 上抽样检查（大误...
- rlcr的随机种子必须是手算plan的fiat-shamir是吧
- 大规模工程出现的问题一定不在决策树的前几层里
- 哈哈哈哈，是
- 刘思皓: rlcr的随机种子必须是手算plan的fiat-shamir
- 是吧
- 光靠抽样很难cover
- 确保逐字看过了
- 刘思皓: rlcr的随机种子必须是手算plan的fiat-shamir
- 是吧
- 这个可能是最重要的一个点了，尤其是 Agent 生产的代码，
- 觉得可以类比汽车至于自行车吧，速度虽然变快了，但是方向
- 要开车的技术。我觉得h2就是这个要生产“汽车”的产线，
- 话说大家用agent操作Office文档一般是怎么做到的？
- 比如docx和pptx这样真的也可以吗
- 我之前试过感觉效果非常糟糕
- 我之前用 humanize 做过PPT，agent在PPT里面画流程图的时
- 多轮review和迭代，可以轻松修复这些问题
- 我感觉像是grok和kimi这样的做好了的成品，似乎会更好用啊，比我直接codex里给prompt做出来的效果要强太多了
- 你太久没用了
- 香港科技大学研究助理教授徐策羽:我之前试过感觉效

---

#### 原文 L19790–L19808

[回到原文件 L19790](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19790)

- 不换头像
- [install-skills] repo root: /tmp/tmp.6QXvlKbKRr/humanize
- [install-skills] target: codex
- [install-skills] codex skills dir: /root/.codex/skills
- [install-skills] codex config dir: /root/.codex
- [install-skills] command bin dir: /root/.local/bin
- [install-skills] target: codex
- [install-skills] skills dir: /root/.codex/skills
- [install-skills] syncing [codex] skill: humanize
- [install-skills] syncing [codex] skill: humanize-gen-plan
- [install-skills] syncing [codex] skill: humanize-refine-plan
- [install-skills] syncing [codex] skill: humanize-rlcr
- [install-skills] syncing runtime bundle into: /root/.codex/skills/humanize
- [install-skills] ensured BitLesson uses a Codex/OpenAl model in /root/.config/humanize/config.json
- [install-skills] installing native Codex hooks into: /root/.codex
- [install-codex-hooks] codex config dir: /root/.codex
- [install-codex-hooks] Error: Installed Codex CLI does not expose the codex_hooks feature. Humanize Codex
- install requires Codex 0.114.0+.
- root@inferdev:/mnt/tmpnfs/renbiao.liu/research/init#

---

#### 原文 L19880–L19972

[回到原文件 L19880](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19880)

- 你依然可以—skip-quiz
- 5月12日 22:47
- 5月12日 22:47
- 要把你人工的测试给详细的写下来
- SunnyCase:大家有没有遇到过让codex用triton复刻
- cuda算法，要求他完全对齐，他说已经对齐了。但实...
- 人怎么测，你就要完全写下来，一个个让测
- 5月12日 22:49
- 好小众的词
- 刘思皓:八月搬去北加
- 我也想问这个
- :那tairan he有绿卡or他做机器人不算hardware?
- why
- Luke:好小众的词
- 5月12日 22:54
- 刘思皓：why
- 我合入的哈哈哈
- 感觉所有人都说三番或者湾区
- 刘思皓： why
- 我知道了，因为你在南加
- 5月12日23:00
- 确实我一路向北
- 飘向北方🎶
- 你说你好累
- 刘思皓： 确实我一路向北
- 已无法爱上谁
- 复读机
- 复读机
- 没关系
- 能从床上爬起来
- 已经很厉害了
- 5月12日23:05
- opus 4.7质量真是飘忽不定
- 让codex只开放brain storm
- 泽文: 有无办法不让 codex 去自动调用 superpowers
- 的 skill
- 感觉可以有个选项来多测些题目感觉人的惰性不太喜欢主动学习更喜欢被动学习
- 刘思皓：睡了一觉起来洗完澡，发现梦中没有出现更好
- 的idea，所以我打算就h2里面的“人类被介入”机制...
- 是的，我想来想去还是考试最直接
- 阮震元（Zain）：感觉可以有个选项来多测些题目感觉
- 人的惰性不太喜欢主动学习更喜欢被动学习
- 能不能做成在 gen-pl
- 这样强迫跟
- 确实
- 5月12日23:12
- 能不能做成在 gen-pl
- 这样强迫跟
- 确实
- 5月12日23:14
- 不过每答对，就不往下生成计划，需要确保hu
- 其实你从这个角度想：我们现在已经需要设计一套机制，让AI多智能体开发的时候，需要用抽样考试的方式“带带人
- 类”，某种意义上已经是ASI了
- 主要看一堆字太累了不知道重点是啥
- 阮震元(Zain)：感觉可以有个选项来多测些题目感觉
- 人的惰性不太喜欢主动学习更喜欢被动学习
- 现在还不是ASI的原因是，ai出的“题”错误率还比较高
- 考试就考重点
- 注意力涣散.
- superpower.
- 泽文: 能不能做成在 gen-plan 的过程就考试，不要等
- 到 plan 完全生成以后再考试
- 我想要的是 Plan-time Human Ver
- 考试做的好，其实就是让 agent 学会主动筛选重要信息
- 以前是人类指挥工具。现在是人类监督Ag
- 5月12日23:22
- 妙啊
- agent harness让ai更强大
- human harness让人类更负责
- 5月12日23:34
- 这个不错
- 来，骑我
- 泽文:我们这算不算是:human harness
- 哈哈，需要赛博高达增强一下苦弱的生物大脑
- https://github.com/mattpocock/skills/blob/r
- 5月12日23:40
- 之前听这个老哥的分享对这个，还有对项目中的用词和ai 建立统一的理解还挺印象深刻的
- 5月12日23:46
- 每天学着网上的大V不上班
- 每个月一毛钱赚不到
- 省吃俭用玩AI Vibe Coding
- 妄想成为下一个奥特曼
- 他们根本就不知道真正的大赢家是什么人
- 5月12日 23:46
- 是我。
- 我已经 vibing 好了一个版本，我给 humanize gen-plan
- 验。不过这个参数名字感觉还差点意思，看看群友的智慧。
- 5月12日23:51

---

### 5月13日

#### 原文 L19973–L19981

[回到原文件 L19973](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:19973)

- 5月13日00:11
- 1. 重复人类的设计，看看他是不是记得自己设计过什么
- 2. 考察人类对我的设计，看看我的设计是否正确
- 3. 教育人类用户，对一些我觉得简单但是人类用户可能不理解的东西，他是否知道背景知识
- 记忆-自检-教育
- 5月13日00:16
- 第一类问题打错了意味着可能整体设计思路变了
- 第二类问题如果打错了其实是在说ai设计错了东西
- 第三类问题答错，本质上是人类智商/背景知识不够

---

#### 原文 L20124–L20172

[回到原文件 L20124](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20124)

- TPhe
- humanize已经是去年11-12月的过时idea了
- 对啊
- 刘思皓: 要不直接线下学习h2吧
- 来啊！
- 我22-23年经常每周打去湾区
- https://calendar.app.google/dTbkFSwqqXD9pVcP8
- 5.16晚上6点，humanize线下大学习！
- radixark要不要给我报一下机票lol
- 我们是民间线下学习
- 笑死
- 纯 humanize 爱好者聚会
- 我去玩一下
- 6点哪里
- 还没定
- 我拉你进群
- ie
- 欢迎在湾区的朋友 5.16 晚上 6 点来参加 sglang 嫡系群线下活动，深入学习 humanize 先进经验
- https://calendar.app.google/dTbkFSwqqXD9pVcP8
- 你们线下组织humanize青年大学习不带我属实非常夸张了
- 翻他妈
- 几万倍
- 5月13日05:46
- 刘思皓:
- 5月13日06:28
- 其实我觉得我本质上实现了一个cursor orchestrate
- 我感觉cursor里面有究级神人
- 我现在回顾性看了一眼，感觉关于多智能体的整个发展脉络是清晰的：
- 5月13日06:32
- 1. subagents
- 2. agents teams
- 3. orchestrate agents
- 4. <something I don't know>
- 我感觉4应该是meta organization builder?
- 就是随时生成任何架构的agent组织
- persistent但是flexible这样
- 不确定
- 以及给予agent自主性，而不是只听人类的指令这样
- 但是过四个月就一定知道了
- agent 自己做structure Test time scaling，自己发现最好的组织形式
- 我最近在我自己的harness里面做这个，感觉最大的bottleneck是apicall的并发
- 是的
- Xinming Tu: agent 自己做structure Test time
- scaling，自己发现最好的组织形式
- 我觉得前面的设计都是人类强加的，上限马上就到了
- orchestrate agents 4. <something I don't know>
- 我做过一定的实验，最后发现让agent自己组织架构是最适合他们的
- 唯一的问题是token消耗非常夸张

---

#### 原文 L20179–L20203

[回到原文件 L20179](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20179)

- 有什么项目是用灵台写的吗
- 我觉得毕竟不是coding agent
- hmmmm
- 在和朋友试能不能做一个专业的trading team这样
- 遇到了很多瓶颈
- iet
- 那其实你没有一个客观指标来判定"这套组织形式"是高效还是低效的对吧
- 对，我发现问题是无法观察，因为生成的东西太多了，我现在在想办法做一个benchmark这样
- 一下子生成了几个M tok的数据
- 看着很炫酷
- but 我没有办法appreciate
- 然后最后发现最好的应用可能是自己build自己
- 5月13日06:50
- 我的观察是agent自组织不是一个好的策略，确实能烧很多token，看起来也很酷炫，但是你必须"剪枝"才能让它达到好
- 的效果.
- 其实这有点像: 公司 vs DAO (Decentralized Autonomous Organization)
- 现实中我还没看过哪一个DAO做出点实事(bushi
- 非常同意
- but我觉得这和agent自组织的社会契约有关系
- 这个我是做过一点点benchmark的，就是去掉社会契约和加上社会契约的表现
- 自组织方式强相关于你施加的社会契约，但是这个就没办法数学化了，变成了一种纯粹的艺术
- 剪枝确实是的，所以我一开始也加了剪枝的功能
- 但是我发现因为我把agent定成了一个没有上下层级的机构，剪枝的时候有时候agent会反对(比如我不想它死这样)
- 5月13日.06:56
- “灵台方寸山，斜月三星洞。“

---

#### 原文 L20327–L20350

[回到原文件 L20327](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20327)

- 我觉得html是给人看的，然后人能看懂并理解，就行了，最后再确保html和plan.md的一致性即刻
- 会浪费一些Context，理解倒是没啥困难吧
- 目前确实可以开个subagent来做md到html转换
- 我也觉得，css对ai来说有啥用
- 不影响主session上下文
- 但是subagent可能会造成些许信息丢失
- 最好是当前上下文直接fork出一个去写html给我看，完事我看完了回到md session上继续干活
- 5月13日11:28
- 按量付弗
- 翁大爷的狗@Rakuten:会浪费一些Context，理解倒
- 是没啥困难吧
- claude自己说理解也困难，因为html的各种样式标签打断了连贯信息
- 5月13日11:40
- 我今天尝试了一种新的自组织方式，感觉很有意思
- 刘思皓: 我也觉得，反正我在swarm teams阶段尝试过
- 自组织
- 确实产生了一点很有意思的讨论
- one agent per paper
- 5月13日11:46
- @王邦彦我记得你是不是一年前跟我介绍过一个工具，就是类似这么看文章的
- 黄澍之:让agent根据学术文章本来就有的topology来
- 我和@王邦彦半年前其实讨论过什么才是最好的文档格式

---

#### 原文 L20374–L20401

[回到原文件 L20374](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20374)

- 我们需要的其实是如下类型的东西：一个结构化的文件格式：
- 1. 机器(脚本)读写(结构化文档)
- 2. AI读写 (比较适合于裸Write/Read)
- 3. 人类读写(有现成的UI)
- 喂htm|合不合大占上下文了?
- HTML是最接近与我们想要的东西的存在
- 上下文占用我觉得还可以
- 将千: 喂html会不会太占上下文了?
- 你现在AI上网搜搜资料下载下来的也是HTML
- 可以以“notification”的方式，让agent自己消化完然后dismiss掉(从上下文移除)
- 将千:喂html会不会太占上下文了?
- 我这样设计之后发现效果挺好的
- 上下文增长慢了，但是效果不差，做得好的话cache率不会怎么受影响
- 5月13日11:57
- 我觉得这个可能是一个很通用的办法，就是把各种各样的不想塞进上下文的消息以synthesized tool call pair的方式
- 注入到上下文，然后允许agent自己主动dismiss(阅读完之后)
- 这样就可以塞无限长的东西，但是不让上下文增长，而且因为总是注入到尾部，不会影响cacherate
- 代价是有的api call会偶尔不太稳定的样子
- 5月13日12:47
- 5月13日15:18
- xs boris不是说用 /loop util 最后还是抄了?
- https:/
- 笑死我了
- xs boris不是说用 /loop util 最后还是抄了?
- 5月13日15:21
- 第一版我做出来比较像 superpower

---

#### 原文 L20455–L20486

[回到原文件 L20455](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20455)

- t -  - //:da
- subworktree 跑两轮轻量级 RLCR loop 探索可行性，然后把不同 exploration 的内容总结成一个新的 final idea 给
- gen-plan消费。目前在几个项目上试了效果还不错（更像许愿机了）。
- 5月13日17:12
- 5月13日17:17
- 5月13日17:04
- https://github.com/PolyArch/humanize/pull/141给gen-idea加了—个后续explore-idea,会给每个idea开
- 收到
- 泽文: https://github.com/PolyArch/humanize/pull/
- 159
- 5月13日17:57
- 5月13日19:25
- 不度三十斤
- humanize 的codex only 反复提到自己需要
- 不度三十斤
- 不换头像
- code-simplifier/agent-code-simplifier 不在PATH里
- 不度三十斤
- 不换头像
- 思考
- 5月13日22:41
- 我在想有没有可能做一个纯许愿的workflow,就是这个pipeline能够自己去发现自己fail了，从而gen-idea，explore-
- idea，找准新方向然后RLCR
- Horace: https://github.com/PolyArch/humanize/
- pull/141给gen-idea加了一个后续explore-idea, ...
- 那得需要有一个非常明确的验收标准，有点像AutoResearch
- 刘诗楠: 我在想有没有可能做一个纯许愿的workflow,
- 就是这个pipeline能够自己去发现自己fail了，从而g...
- 但是组件都是来自于humanize
- 不度三十斤
- 不换头像

---

#### 原文 L20580–L20611

[回到原文件 L20580](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20580)

- session manager
- 最好的传递上下文方式就是直接告诉cx那个cc的session id
- 既然现在我们有了 global token counter
- 是不是做这种东西也很自然
- 你猜猜我h2是怎么在cc和cx之间传递上下文的
- 还能这样
- 我觉得我应该立刻动手把 cursor oc 什么的都 collect 起来
- real Context Engineering
- 不不不，你要做的不是集中管理
- 我看现在比较严谨的这些work,都不会让Agent看到他的测试结果，就是先会搞一个validation.Set一样的东西去让agent调
- L.Zhu: @张子健测benchmark的时候发现 /goal 老
- 是去偷偷瞄其他session的结果
- 而是“剪枝传递”
- 这么想，把每一个Agent当成神经元，然后人从小的时候到成年的时候，其实神经元之间的链接是逐渐减少，也就是
- 剪枝的。而剪枝才是整个事情的关键所在
- 我现在都是开docker测了
- 刘诗楠:我看现在比较严谨的这些work,都不会让Agent
- 看到他的测试结果，就是先会搞一个validation.Set...
- 草。。。。。
- L.Zhu:我现在都是开docker测了
- 5月13日23:20
- iclr'16 pruning, quantization, huffman coding我老板当年的best
- 刘思皓:这么想，把每一个Agent当成神经元，然后人
- 从小的时候到成年的时候，其实神经元之间的链接是...
- Make sense呀
- 我觉得agentic workflow的关键在于：简单精妙的重复结构
- 或者用法ilya的说法，compression is intelligence
- 刘思皓:而是“剪枝传递”
- 我觉得有一门新兴学科要诞生了
- 智能体拓扑学
- 现代信息论
- L.Zhu: iclr'16 pruning, quantization, huffman

---

#### 原文 L20651–L20695

[回到原文件 L20651](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20651)

- 其实h2最后一个关键点我前天才想明白
- 就是层级抽样考试
- 这不是啥产品公开
- 只是我抛砖引玉的东西
- 还是需要大家多多鞭策我
- 当别的 agent flow 还在努力放马奔
- 蛮make sense的
- 刘思皓: 就是层级抽样考试
- What I cannot create / I do not understand
- 刘思皓： 就是层级抽样考试
- 带着人类往前跑
- 这是我昨天想到的美妙比喻
- 我没见过任何其他workflow有这个意识
- “带着人类往前跑”
- 回归了harness的本质
- 这才是humanize的真谛
- 5月13日23:30
- 用Agent来harness人类
- 回归了harness的本质
- 这才是humanize的真谛
- 5月13日23:30
- 这其实是另一个层面的human in the loop
- 加上harness，人马合一
- 把人类有限的带宽和脑力用在agent workflow精心设计的需要确认的点上
- amazing 啊
- 不过我觉得大众产品估计2-3个月之后就会赶上
- 这里最大的核心是
- 从以人为中心的computer aided design (CAD)过渡到以agent为中心的human aided design (HAD)
- 所以flow都还在focus在“如何更好更大更快”造出些什么，which is correct，humanize1也是这么做的
- 但h2的核心在于，我不仅更好更快更大
- 而且我有一套机制
- 监督和教育“使用我的人类用户”真的理解了我在做什么
- 我觉得这是最最关键的
- 因为只要有这个机制在
- 其实很多事情就会很“安全”
- 5月13日23:35
- 可以组织—个workshop/conference, international conference on human aided design (ICHAD)
- GYF: 从以人为中心的computer aided design (CAD)
- 过渡到以agent为中心的human aided design (HAD)

---

### 5月14日

#### 原文 L20733–L20750

[回到原文件 L20733](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20733)

- 5月14日00:15
- 相信Agent自己本身的能力
- 理论上 builder和 reviewer的分布差异越大越好
- 我也只能从这个角度理解
- NV周耀阳:理论上 builder和 reviewer的分布差异越
- 大越好
- 还有个猜测是 lite 蒸馏的 opus/gpt token 更少
- 还有gemini这种夸夸模也是
- 我才知道国内大厂会做好多蒸馏的合成数据对着benchmark刷
- 每个benchmark都有对应的蒸馏管线
- 我没有证据但是我信
- 不知道美国的大厂有没有这种对着benchmark故意刷的行为
- review自己经常会觉得我做的很完美
- 还有gemini这种夸夸模也是
- 我才知道国内大厂会做好多蒸馏的合成数据对着benchmark刷
- 尤其是九坤那玩意

---

#### 原文 L20759–L20790

[回到原文件 L20759](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20759)

- 一样，我甚至觉得v4pro需要暖
- 机，先刷个两三百K的context...
- 知乎
- 知乎
- 5月14日02:34
- 我感觉h2除了可视化美观了一些
- 方法学上面只有两个改进
- 1. 把agent的本身抽象成一个可以用编程语言描述的形式化"算子"，这样方便构造和静态检查flow
- 其他都是infras层面的改进，比如支持无限嵌套agent组织，比如支持各类型model,比如支持各类型工具
- 论方法学的完备性，我感觉还是humanize1比较完备一点
- 5月14日03:21
- 现在我感觉很大的一个ai问题是他一旦出错不太会自己反思
- 容易卡在死胡同这个能解决吗
- 靠ask codex确实是一个好办法
- 但是我在想ai既然是一个概率状态机能不能说强制做workflow把他从状态A推到状态B
- 然后这个workflow又足够general
- 比如怀疑有问题-> 去找可观测变量-> 去监控可观测变量作出假设定位问题-> 再去思考问题是什么-> 修改代码
- 现在ai默认的模式应该是
- 怀疑有问题->(COT) -> 修改代码
- Which is terrible
- ai会这样把
- B4RRy: 比如 怀疑有问题-> 去找可观测变量 -> 去监
- 控可观测变量作出假设定位问题->再去思考问题是...
- 人为给可观测变量太bitterlesson了.
- ai不太会这样
- 除非你明确告诉他怎么做
- 比如举个例子
- 你说：我现在这个代码运行很慢你帮我看看为什么怎么加速
- 5月14日03:27
- 你可以试试看这种虽然是很差的prompt
- 但是他甚至不太会去比如跑一个小代码检测一下gpu占用之类的操作
- 你如果说到：我现在代码的gpu占用率很低你给我解决一下

---

#### 原文 L20971–L20994

[回到原文件 L20971](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:20971)

- 4o 真的啥都能做，有啥不行 tune tune prompt 就行了
- 不用 tune prompt 的 AI 不可能是 AGI 的
- 但是没有 tool call
- 刘家昌: 4o 真的啥都能做，有啥不行 tune tune
- prompt 就行了
- 接在龙虾里啥都干不了
- 我曾经因为 gpt5 说话太批
- 把国模试了一圈
- opus 4.6 还是说人话的（
- baked in prompt 不可能会成为 AGI
- 5月14日15:22
- 为啥claude这个goal
- 即使后台有东西在跑
- 也会触发啊(这个stop hook)
- 感觉好蠢
- 5月14日15:29
- 那你和cc的官方skill(好像是) learning-mode有什么区别
- 刘思皓:1. 首先你并没有办法在设计spec的阶段把所有
- 问题想清楚。其次，当要做的项目人越来越大的时候...
- humanize应该选择在编译器层次干预AI生成process吧
- 这个是用来干啥的

---

#### 原文 L21025–L21033

[回到原文件 L21025](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21025)

- 5月14日16:23
- plan里的defer，reviewer不能识别到?
- 是不是应该让gen-plan的codex reviewer和rlcr的reviewer统一下共识?
- 5月14日18:37
- https://github.com/PolyArch/humanize/pull/160
- 5月14日21:32
- 我不太确定learning-mode的目的是不是就是教用户理解ai在做什么。humanize2关于“考试问答机制”的设计目的
- 是：1. 确认用户在定spec的时候的设计思路没有变更；2. 自我纠偏那些没有在spec讨论阶段想清楚的；3. 教育用户
- 理解ai在做什么。我觉得你其实把考试理解成一个“渐进对齐，加深理解”的过程就好了。

---

### 5月15日

#### 原文 L21131–L21145

[回到原文件 L21131](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21131)

- 你这个是网页版对吧
- Licheng:第一次把claude的context上限击穿了原
- 来不能无限compact
- 对网页版的
- 网页版的那个上下文不是claude code里面的那个上下文
- 网页版好像看不到jsonl?
- 5月15日04:54
- 它应该是为了适配对话显示做了一些缓存限制
- 只是避免你做一个超长无限翻页的巨大对话吧
- 确实，也不能主动compact，都是到一定程度了他自己compact
- 和LLM的那个上下文不是一个东西
- 但是应该是确实超了实际的context了
- 已经compact过两三次了，这确实是一个超长的巨大对话
- cc 的 compact 应该是

---

#### 原文 L21376–L21388

[回到原文件 L21376](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21376)

- 刘思皓: 我就直接截图发给它
- 刘思皓: 我真的觉得必须要把Humanize1+2写成paper
- 我相信bun重写的promptt也就是一句 rewrite it in rust
- 大爷今天应该面签完 我来起个draft然后明天讨论下
- 直接gpt改图呗
- 应该是: /goal rewrite bun with rust
- paper被你蒸馏了
- 刘思皓: 默念智能等于压缩等于精妙结构的大规模重复，
- 默含scaling law
- 懂了。
- 叫Humanize3
- 因为1+2=3
- 5月15日10:12

---

#### 原文 L21429–L21435

[回到原文件 L21429](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21429)

- Humanize 带来的Codex使用范式变
- 化，解锁 Agent 优化 kernel 上限
- Humanize 带来的Codex使用范
- 式变化，解锁 Agent 优化
- kernel 上限
- 无敌了

---

### 5月16日

#### 原文 L21738–L21752

[回到原文件 L21738](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21738)

- 更便宜的 review 估计都够了，
- kimi和glm比降智4.7都差不少用了快一个月了
- 我是有时候还拿来build
- 太智障
- 如果kimi真的能near codex review, 那我宣布杨植麟是我爹
- build glm > kimi > opus 4.7
- 你可以先拿49试一下（
- 我觉得 quota 给的还算大方
- wait what
- 为啥refresh勒？??
- 有这种好事
- 我用起来感觉是opus 4.7 > glm 5.1 > kimi 2.6 仅限我的使用场景
- 你们的呢？
- refresh了

---

#### 原文 L21875–L21940

[回到原文件 L21875](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:21875)

- 我感觉现在agent框架就是很难ablate，本身也有一定随机性
- 刘思皓:我开发h2得一次性起3-10个rlcr在本地测试
- 功能也复杂
- 5月16日14:27
- agentic flow的光谱有两个端点:
- 1. 我只希望agent能够自组织， 框架干预越少越好(adaptive agent system)
- 2. 我希望能够设计一系列动态的框架， 来规范适配agent的行为(agentic harness system)
- 我感觉后续可能会往2的方向去发展，然后关于sys& arch的全部设计又可以重做一遍
- 5月16日14:38
- @Mention All
- humanize2(h2)的开发差不多进入到了一个"我愿意公开让大家一起来看看"的阶段，因为方法论这种东西,没有更多的
- 人用的话，闭门造车是完全没有意义的.
- humanize1的改进得到了社区大家的广泛贡献非常感激.h2后续还是会保持这样的开源精神.
- 我现在本地在跑一些RLCR example project. 如果没什么问题，我明天会push到公开的仓库.
- 但这个版本的humanize2,它并非对humanize1的方法学有什么更新.
- h2更多的意义在于规范了一套"flow原语"，让开发flow本身变得更加方便,并且给flow提供了一套playground,一
- 套"触发式数据流"执行器.
- 并且支持任意层级的flow构建，任意Tool/Agent,以及有一套还不错的GUI
- 后续的时间线：
- 5月：branchh2我会继续高频开发，这一个阶段它不是一个生产上可用的flow
- 6月：`beta`，差不多会稳定一些
- 后续h3的核心精神和路线就很明朗了: Agents create Agentic Flow.
- 计算机科学家！
- 效忠!
- 旭续n3核已相神续明呦了：Age
- 计算机科学家!
- 效忠!
- fighting
- 忠橙
- deepdrink
- 会有很多人
- 因为你的存
- 在而生活的
- 更美好！
- h1: A flow that works
- h2: A platform/language that human build/test flow
- h3: An automation system that let agents builds its own flow
- 5月16日14:45
- 刘思皓: h1: A flow that works h2: A platform/
- language that human build/test flow h3: An auto...
- ！！！
- 给 sihao 做个娘化形象
- state of the art
- 刘思皓: h1: A flow that works h2: A platform/
- language that human build/test flow h3: An auto...
- ！！！
- 给 sihao 做个娘化形象
- 5月16日14:50
- gpt image 启动!
- 5月16日14:55
- 真正的vision!
- 刘思皓: h1: A flow that works h2: A platform/
- language that human build/test flow h3: An auto..
- 真正的agi!
- 5月16日15:01
- de bhi
- Humanize
- Humanize
- 翁大爷的狗@Rakuten: 给 sihao做个娘化形象
- 兄弟你好香

---

### 5月17日

#### 原文 L22098–L22125

[回到原文件 L22098](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22098)

- 5月17日07:10
- https://github.com/PolyArch/humanize/tree/h2-dev
- h2我 push了。Again，它只是一个first step Proof-of-Concept:如果你的期望是“我希望用它来增加我做其他项
- 目的生产力”，那我建议是不要用它，而是继续使用main/dev branch，它的功能性和鲁棒性远远没有当前的main
- 和dev分支可靠。
- 如果你的目标本身就是开发一个更加合理且鲁棒的agentic flow platform，那我觉得可以试一试。并且任何方面的批
- 探头
- 5月17日07:25
- <1>
- RLCR，启动！
- 另外，欢迎任何对Humanize2中“流程原语”的设计建议，只要是合理建议，我愿意全部重写
- 探头
- 5月17日07:25
- <1>
- RLCR，启动！
- H2, 启动!
- 5月17日07:32
- 晚一点我会把humanize2的slide发上来
- 牛牛
- 启动!
- 正在让 Claude 口把口教我咋用
- 从氢原子(H1)变成氢气(H2)了，燃起来了
- 5月17日07:45
- 今天把我的claude code降成100刀的版本了，最近确实对A\有点失望

---

#### 原文 L22158–L22186

[回到原文件 L22158](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22158)

- AI
- UI 是次要的，humanize1 的核心是我觉得最宝贵的
- 蒋炎岩@NJU: 我以前是这样实现类似humanize的功
- 能的：直接让他对一些关键的flow给[alternative1|a...
- 5月17日12:31
- h2是用ts写的吗
- 我以为用rust了
- humanize 1
- 以前很多人，包括 LeCun 攻击 LLM+ 能力的一个点是：LLM哪怕一个 token的正确率是
- 99.999%，几万步累积下来错误率也是非常高的。
- 而我眼中的harness engineering+ 正是为了解决这个问题：我们把一个大任务划定边界、拆解成多
- 个刚性的、可验证的harnessitem+ (有的framework称之为接受标准，AC+)。一个 harness
- item/AC的设计目标就是在某个子问题、子方向上把99.9%^{N}尽可能重置成1。
- 我们设计这些 AC，使得 P(AC_i | model is wrong or model is reward hacking⁺) 感可能接近于 0。
- 使得 P (Ultimate Goal | AC_0 & AC_1 & ...AC_n) 尽可能接近于1。 这就使得原来 LLM 独立难以完成
- 的任务得以完成。边界划分、验证方法和接受标准越清晰，那完成大型任务的可能性就越高。
- 我感觉humanize2做了exactly你说的这个功能
- 蒋炎岩@NJU:我以前是这样实现类似humanize的功
- 能的：直接让他对一些关键的flow给[alternative1 | a...
- 哎，感觉harness的东西真的比较大道朝天
- humanize的图形化界面里面有一个动态渲染的ui，其实本质就是一个html卡片
- 你不做就有别人做
- 大家可能都有一些模糊的感觉
- 在右下角：workflow specific view
- 感觉需要一个highlevel的材料来梳理一下现在h2的原语
- 5月17日12:37
- 因为harness做起没多难，或者说有ai之后，做什么都不难。难的是：“你是否真正想清楚了”
- 哎，我觉得最难的就是在于理清楚这一点
- 每次我专门想要静下心来整一下的时候，我就发现我又想不起来了

---

#### 原文 L22220–L22236

[回到原文件 L22220](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22220)

- 开源项目如果有用的话第一条曲线是会有人自主传播
- Lurker:最近冒出了很多humanize相关的文章，群友
- 有啥头绪吗
- 1 CASE A - RLER aS & CARTRIONE
- 最近都没用humanize，发展到啥程度了
- 你最近的记忆是什么？
- 大概是上个月吧
- 让humanize帮你分析humanize发展到什么程度了
- claude 和codex都用GPT 效果怎么样
- 这个是最省钱的方式
- 禁止一切都humanize化
- humanize适合项目初期的时候用
- 项目成熟后再用humanize感觉就有点太浪费了
- 早期搞个基本框架，我基本就看开对话模式了
- 后续一些细节只能靠vibe

---

#### 原文 L22343–L22364

[回到原文件 L22343](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22343)

- 就像数据蒸馏是模型厂的核心工种一样（x
- flow market 加上配套的flow benchmark和flow profiling
- 5月17日15:15
- 你们有人做企业ai infra治理么玩开源的除外
- agent infra
- 啥叫企业 ai infra 治理
- 每个项目组都有自己的诉求，源码都恨不得加密
- 就是给agent在一个地方管起来？
- @福尔高斯 seed 首席agent infra专家
- 真是
- 一对苦命鸳鸯...
- 翁大爷的狗@Rakuten: @福尔高斯 seed 首席agent
- infra专家
- 福尔高斯：找我先找我的agent
- 5月17日15:20
- Agentworkflow挺重要的 复杂任务必须mutiagent了
- 5月17日15:25
- 太6了

---

#### 原文 L22422–L22437

[回到原文件 L22422](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22422)

- 5月17日 20:30
- 话说agentmemory这个东西有人用过吗
- 以及humanize2有做自己的专用的memorylayer么
- memory对 coding 场景我觉得基本都是负收益
- 搞乱上下文
- 同意
- 我觉得coding得100%知道memory有哪些内容
- 不吧，我手动做的感觉是这样的
- 第一个是做coding的memorylayer的触发频率一定要很低，比如说每次user prompt的时候跟着append一下，一
- 定不能每次tool call做一下，否则一定乱套。
- 第二个是我一般倾向于只保留“特别坏的记忆”，不保留一般的记忆和好的记忆
- 或者 agent.md
- bitlesson —般都是 project specific的
- 因为我发现“好的记忆”极其的有毒性，会让agent停止路径探索
- 不应该跨项目共享吧
- 5月17日21:00

---

#### 原文 L22454–L22466

[回到原文件 L22454](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22454)

- 报一下。谢谢。
- Prompt:
- 看一下PolyArch/humanize这个仓库，对比一下dev->h2-dev的改动，和我讨论一个大概15-20页的slide提纲，用
- PolyArch Design System 风格，帮我做—个slide
- Horace: 这个 ppt是怎么做出来的先搞个文档还是直
- 接让agent读代码仓啊
- 5月17日21:05
- 这个不是bug，是这样的，最大轮次这个参数只限制第一阶段（活干完没），不限制第二阶段（修bug）。
- 暂时没有，目前还是之前的bitlesson.md
- 香港科技大学 研究助理教授 徐策羽: 以及humanize2
- 有做自己的专用的memorylayer么
- 我是用claude design多一点
- L.Zhu: 做 slides现在是claude code design最好用吗

---

#### 原文 L22572–L22596

[回到原文件 L22572](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22572)

- 老登企业的对接画像即使研发都很难绷
- 但能确认bug，有权限改核心云服务代码，我感觉应该是内包吧
- 5年前的事，我印象比较模糊，我们当时云服务使用范围主要是vm, Kubernetes, object storage, rds这些
- 这几个服务在各家云厂商应该都是自己人在做吧，除非是前端的bug
- 或者配套的cli工具，可能会丢给外包团队
- 有个bug我还有点印象，是腾讯云的object storage cli工具的bug还是cli和server api配合的bug来着，反馈了以后
- 他们不长时间就改了，这个倒是有可能外包出去
- 5月17日 22:48
- 感觉aiagent研究这种事，还得是只有工业界能做。我现在平均跑一天就是1.2B，做个系统级别的实验，我怎么得跑
- 上千个数据点吧
- 没有无限token根本没法做
- 现在很多flow的设计，里面关键步骤拍脑袋的部分还是比较多，flow design space空间很稀疏
- 5月17日 22:54
- agent flow evaluation 本身就挺值得研究的，还得剔除模型带来的影响
- Result = model x tool x flow
- Agent = model + tool
- Harness = tool + flow
- Model = gpt/opus/kimi/...
- Tool = claudecode/codex/...
- Flow = superpowers/humanize/goal/...
- 5月17日 22:59
- 模型和工具的评估都很多
- 我主要还是token量的限制
- 你要正经做一个flow的研究，得准备好一天1T的消耗量

---

#### 原文 L22603–L22612

[回到原文件 L22603](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22603)

- 或者你可以说flow是模型的“现实世界RL反馈”
- 搞个Meta flow，基于模型和工具调试出对应的 specific flow
- yc: flow是不是得和模型一起演化，比如claude
- flow本身其实是在社会规模上构建预训练系统
- 但我觉得flow应该会一直存在，不会消失，不管模型进化
- 现在有两层flow吧，一层原厂配套的agent，cc，cx，kimi cli这样的客户端。另一层就是humanize这样的直接调
- 用agent的flow。
- 随着时间发展，原厂agent内部flow肯定会集合sota的外层flow，然后模型也会内化agnent的通用flow
- 5月17日 23:09
- 是慢慢渗透进去

---

### 5月18日

#### 原文 L22820–L22830

[回到原文件 L22820](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22820)

- 刘思皓: 我发现humanize的rlcr完全不适合搞开放式的
- 优化任务
- 是的
- 刘思皓: 我发现humanize的rlcr完全不适合搞开放式的
- 优化任务
- 但算子优化比较容易闭环的
- 但是我没想到到底开放任务应该用什么样的 workflow
- 我让humanize探索形式化证明的方案
- 他给出的方案要么无法执行，要么需要无限长时间
- 还经常偷懒

---

### 5月19日

#### 原文 L22914–L22926

[回到原文件 L22914](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22914)

- 巨型审查委员会......让我想到了一堆领导领导一个干活儿的大头兵的场景
- 刘思皓:他们在内部fork了一个humanize，然后扩展
- 了一个巨型审查委员会
- 其实只是MoR
- Mixture of Reviewer
- 5月19日09:15
- 这个【混合不同的personality】的操作，我感觉好久之间就看到过
- yond any one reviewer:
- sonalities tuned for a specific codebase (a security personality, an APl-stability pi
- es lint / pylint reviewer that emits findings in the same schema.
- ce reviewer that gates convergence regardless of Codex's verdict.
- te that blocks convergence if coverage regressed.
- 还会有router吗

---

#### 原文 L22972–L22980

[回到原文件 L22972](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:22972)

- 5月19日11:09
- 开一下codex权限
- 默认给什么bypass权限呢
- humanize 设计上是应该 Claude 来落.git 吗
- cramis世沙用罗止写-git，它段期圆试 commlt -被teok
- 看起来是cx的沙箱问题
- 而不是humanize的flow问题
- I see
- codex应该帮忙吗

---

#### 原文 L23017–L23045

[回到原文件 L23017](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:23017)

- 5月19日22:34
- 「你可以用/goal clear清掉。
- Goal not yet met... continuing (ctrl+o to expand)
- 我做不到」
- 这就是 claude 的水准
- 5月19日 22:39
- 这个分析需要的时间超出了当前 session 的剩余 context
- Goal not yet met... continuing (ctrl+o to expand)
- 我做不到这个 goal 的要求。需要/goal clear。
- Goal not yet met... continuing (ctrl+o to expand)
- L API Error: Server is temporarily limiting requests (not your usage limit) ·Rate limited
- 5月19日 22:39
- 太搞笑了
- 这个 goal 我在当前 session 做不到——之前多次尝试都失败了，context 已经很长。重复尝试不会得到不同的结
- 果。需要一个全新的 session。
- X Goal could not be achieved (39s · 1 turn · 369 tokens) (ctrl+o to expand)
- 这也太垃圾了
- 5月19日22:45
- 今晚cc几乎是不可用状态
- 一直509
- 529
- 它的 goal 默认还是用 haiku 去检查是否完成的
- claude code的/goal做的很垃圾的
- 还会死循环
- claude code的工程质量一直不如codex
- 纯搞笑的
- “90%的代码都是agent产生的”
- 郑权: claude code的工程质量一直不如codex

---

### 5月20日

#### 原文 L23259–L23271

[回到原文件 L23259](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:23259)

- cc是真的敢赌
- 在给公司分享humanize时我也在想harness的意义，感觉就是要搞AI接管流
- claude 写的方案也更牛逼
- 智谱黄睿博: 在给公司分享humanize时我也在想
- harness的意义，感觉就是要搞AI接管流
- agent workflow 对于能力提升还是比较大的
- 工具和约束也不能少
- 哪一天模型也原生get到这个能力了呢
- 肯定会内嵌进去的
- flow是社会层面的预训练而已
- 以前用humanize能跑的官方cc也能跑了，下一步模型也会拥有的
- 智谱黄睿博:哪一天模型也原生get到这个能力了呢
- SRE 从未想过的时代

---

#### 原文 L23353–L23375

[回到原文件 L23353](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:23353)

- ·以会诺为中心，而不是以Bot为中心。会话本身犹是协作边界、参与者、可见消息、Actor唤醒、执行上
- 下文和记忆接力都围绕它展开。
- ·Al 同事可以被共享。Workspace 成员、Actor、Remote Agent 都可以跨 Workspace 分享，并通过联系人
- 式关系网络被添加进来。
- ·资源权限可治理。插件、投能、MCP Relay 能力和事件源都是Workspace 级资源，可以显式授权、审
- 计、回收。
- ·云嬉协同，本地执行，团队在Web中协作，但扶行可以继续落到本地浏笼器、桌面、文件系统、内网服
- ·事件可以直接拉起工作。定时任务、自定义 Webhook、GitHub/GitLab 等集成事件都可以直接进入同一套
- 运行时。
- •原生 Agent 与外部 Agent 并存。平台内的 Actor 由 Synapse 托管：Remote Agent 通过桥接接入，但保
- 留自己的外部运行时栈。
- 我上午看了一个Talk
- 我觉得可能”以产物为中心“是一个更加合理的范式
- 最起码解决了一些我在slock的问题（
- 智谱黄睿博: 这个抽象对我是有启发的
- 并非故意攻击我在最近三个月看到不下 5款产品做这个事情
- 这个有很大鸿沟
- 我不确定以对话为中心还是以产物为中心了
- Claude协议版本就说自己已经做完了纯文科产品经理来的
- 智谱黄睿博:
- 我给你看看我之前做的。。
- 线性对话是一个很低带宽的东西
- 我感觉我看了10款

---

#### 原文 L23811–L23823

[回到原文件 L23811](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:23811)

- 这波怪我
- humanize永不下班!
- #humanize-user
- for nvidians
- NV 周耀阳: 有 slack 群吗?
- 大家的kernel-pilot能跑多久（
- 这个#humanize-user 是internal的啊
- 哈哈你的头像就是这个表情
- L.Zhu: #humanize-user for nvidians
- 原来是刚建立的

---

#### 原文 L23884–L23896

[回到原文件 L23884](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:23884)

- amd没人搞humanize吗这样怎么和nv打
- humanize不止针对nv卡哇
- 这个问题我问一下，你大概跑了多久
- 段震伟: h2 遇到了严重bug，我提了个issue https://
- github.com/PolyArch/humanize/issues/174
- 只不过nv生态完善一点，用的人多
- amd和我们国产卡是一路的，要写汇编
- :amd没人搞humanize吗这样怎么和nv打
- 蹬到sass都差不多了吧
- 你咋humanize，除非你是编译器工程师会调编译器
- 不安です
- 5月20日13:58

---

#### 原文 L23951–L23967

[回到原文件 L23951](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:23951)

- 泽文: 我之前在 CLAUDE.md 写死了让cc调用哪些
- mcp。感觉cc完全不听话，codex比较听话
- 我之前人力loop鞭策了好久
- 5月20日15:51
- 比如你发现一个应该走mcp的场景它没有走，开个新session抽出这个场景来拷问他为什么不走mcp
- 让他自己反思prompt要怎么改才能用上mcp
- 5月20日15:51
- 然后把这个做成自动循环
- 他也不是很懂，会被上下文污染的
- 所以还得循环鞭策
- 让他自己开 subagent 或者 fork session 或者直接命令行去验证新的Claude.md是不是真的在这个场景下能稳定调用mcp
- 我发现它在自己鞭策自己5-10轮左右才给出了真正稳定的规则
- 但这只能保证新上下文遵循，不能保证长上下文遵循
- 上下文长了以后它自己的训练倾向还是会压倒你的规则文件
- 5月20日15:59
- Claude对我这套方法论的评价

---

#### 原文 L24023–L24045

[回到原文件 L24023](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:24023)

- /nenory to edit
- Context Usoge
- cocnnnnnc。eeeeeeeeee
- Opus 4.7 (1M context)
- global.anthropic.cloude-opus-4-7[1m]
- 上限是60k吧
- Opus 4.7 (1M context)
- 45.9k/In tokens (53)
- Estimated usage by category
- System prompt: 9k tokens (0.9%)
- System tools: 10.9k tokens (1.13)
- Memory files: 24.3k tokens (2.4%)
- Skills: 1.8k tokens (0.2%)
- Messages: 12 tokens (0.0%)
- Free space: 921.1k (92.1%)
- Autocompact buffer: 33k tokens (3.3%)
- 5月20日17:47
- H1 有没有现成的介绍 slides 呢 我给同事们分享一下
- 5月20日17:52
- Humanize — Lab meeting
- deck.pdf
- PDF

---

#### 原文 L24049–L24060

[回到原文件 L24049](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:24049)

- /nenory to edit
- Context Usage
- Opus 4.7 (1M context)
- de-opus-4-7[1m]
- 45.9k/Im tokens (50)
- Estimated usage by category
- System prompt: 9k tokens (8.9%)
- System tools: 10.9k tokens (1.13)
- Memory files: 24.3k tokens (2.4%)
- Skills: 1.8k tokens (0.2X)
- 5月20日18:21

---

#### 原文 L24089–L24108

[回到原文件 L24089](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:24089)

- 做狗
- 我发现humanize自己跑着跑着会把.humanize这个文件放进.gitignore
- 5月20日22:34
- 然后第二轮跑的时候，，或者我cancel，就会出这个了
- 除非我再git add -f .humanize
- 就应该ignore 吧
- ys：我发现humanize自己跑着跑着会把.humanize
- 这个文件放进.gitignore
- 设计起来就是要ignore的
- 设计起来就是要ignore的
- 5月20日22:55
- 设计就是要进gitignore的，然后默认行为是plan文件不进入git，如果进入的话，需要用--track-plan-file
- ys：我发现humanize自己跑着跑着会把.humanize
- 这个文件放进.gitignore
- 应该是我中间哪步搞冲突了
- 或者你可以改一下commit的prompt
- 但是设计的就是ignore.humanize的
- OKOK应该是我add了的问题
- 技术细节稍微有点多，其他都不错

---

### 5月21日

#### 原文 L24220–L24240

[回到原文件 L24220](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:24220)

- 这个flow这里是特指好
- h2 flow吗
- h2并非是指类似rlcr的某一个flow，它是一个“流程语言”+“协作平台”，你可以在上面搭任何你想要的flow，
- 我已经搭了一个rlcr在上面。
- 就如果你希望方便地构建你自己的flow，比如在rlcr的基础上魔改一个比如说专门用来优化的flow
- 可以试试h2,然后要是觉得什么地方用的不爽，随时反映给我
- ic
- h3: 搞清楚怎么让AI自己搭flow
- 5月21日04:57
- 56
- 我想跨好几个repo让他们都跑一遍，能humanize吗
- 5月21日05:03
- kne 1 rotatiur" cumpletxd
- cnperorily liniting, request. (rut seur us
- h1:—个能干活的flow -- RLCR
- h2:一个搭flow的平台和强类型流程语言
- h3:搞清楚怎么让AI自己搭flow
- 5月21日04:57
- 我想跨好几个repo让他们都跑一遍，能humanize吗
- 5月21日05:03
- kne 1 rotatior!" cvnpletxdl

---

#### 原文 L24363–L24391

[回到原文件 L24363](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:24363)

- Report has 7 concrete improvement suggestions. Surface to user and ask about filing a GitHub issue.
- Exit reason: complete — all acceptance criteria met and code review passed (13 review rounds,
- P0→P1→P2 descending).
- Methodology improvement suggestions (sanitized, from the analysis report):
- 1. Convergence guard — after 2-3 consecutive rounds of P2-only findings clustered in the same
- subsystem, force a choice between "stop and ship" vs. "one
- structural/property-test pass." The loop ran 9 patch rounds past natural convergence with no scope-cap
- mechanism.
- 2. Sibling-path enumeration on every finding — when a finding is "path X lacks property P," require
- grepping for symmetric paths and fixing them in the same round.
- Several rounds were spent re-discovering the same property on neighbor code paths.
- 3lir s  -s snsd is d r   rdd om
- mainline-scope rounds; full goal-tracker re-write isn't needed when
- only one P2 is closing.
- 4. Lower the bitlesson capture bar — if the same class of finding recurs twice in one loop, the third
- occurrence should auto-promote to a captured lesson. This loop
- had 3+ candidates and captured 0.
- 5. Reconcile environment differences before round 1 — first review should report the implementer's full
- validation matrix from the reviewer's environment, so
- sandbox/socket discrepancies are caught upfront instead of negotiated across rounds.
- 6. Explicit stop criterion — once mainline ACs are MET and findings are P2-only for K rounds, remaining
- inc  ol in rcc- so
- and the loop terminates with a documented residual-risk list.
- 7. Track "finding-generated-by-previous-fix" as a distinct category — one round-N+1 P1 was directly
- caused by round-N's fix; that category is high-leverage and worth
- a brief retrospective when it occurs.
- structural/property-test pass." The loop ran 9 patch rounds past natural convergence with no scope-cap
- mechanism.
- r rd r  t,      y    -in

---

#### 原文 L24628–L24640

[回到原文件 L24628](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:24628)

- 这个就是说humanize plan做好，然后只使用codex/goal来执行这个plan吗
- 泽文：我发现，带有调试任务比较多的常见的loop，使
- 用 codex的 /goal 很舒服
- 我现在有些任务会直接用/tasks列任务清单
- 前面虚宝讲过怎么做，prompt很简单：/goal 按照这个
- 那这个确实可以。。
- yuchao: 这个就是说humanize plan做好，然后只使用
- codex/goal来执行这个plan吗
- 可以全知全能代码
- 就是没有隔离review的感觉
- 现在opus4.7基本上不会中途乱退出了
- 我用的场景是，用 yocto 来从零制作一个li

---

#### 原文 L24737–L24902

[回到原文件 L24737](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:24737)

- 当年claude今年codex
- 我觉得找这么个势头走下去
- codex非常猛
- 唉我还是喜欢cc谁能打醒我
- 你可以使用完codex，就会觉得cc很不爽
- 我从claude彻底换到codex也用了3周
- gpt5.5出来之前我还在纠结要不要从codex切到claude出来之后不纠结了
- 信得好不如信得早
- 5月21日23:18
- 我从cursor换到claude用了俩月
- 早信早用早爽
- 来回切好几次了
- 蒸馏群友信息
- sihao会让codex作为humanize的主力code，然后claude review吗
- 刘思皓: 我从claude彻底换到codex也用了3周
- 5月21日23:18
- 是不会错的
- yuchao: sihao会让codex作为humanize的主力
- code，然后claude review吗
- 谁家好用用谁的
- humanize当初做过实验
- 我觉得claude/codex就是基础算子
- review必须是codex
- i see
- 后面高效调度os就完了
- 但是感觉codex的coding能力确实比cc强一点
- 决定交付质量的是review
- 刘思皓: codex的review我再说一遍，强到无敌
- 可以让codex自己code自己review吗
- codex 感觉自带的workflow，很牛，给他做一个任务，他能自带review，一直做下去
- 只能这样了……
- yuchao:可以让codex自己code自己review吗
- 是哪个呀
- Canaan: codex感觉自带的workflow，很牛，给他做
- Canaan: codex 感觉自带的workflow，很牛，给他做
- 一个任务，他能自带review，一直做下去
- /goal
- 希望claude code下一个发布能大幅提升一下
- 很难
- yuchao: 希望claude code下一个发布能大幅提升下
- claude除非release它内部那个review模型
- 我每个release note都看
- 它最近release note都不知道在干啥
- 刘思皓: 我每个release note都看
- 对 除非你用米索斯review
- 我还是倾向用不同的模型build 和 review
- 但是如果全面codez build的话
- 我不知道用啥review
- google会不会推出啥coding agent api
- 给codex做个skill叫claude build 让它call claude -p去做build工作
- 合理
- akane: 给codex做个skill叫claude build 让它call
- claude-p去做build工作
- claude-p下个月就要另外收钱了
- 这样builder的上下文也是干净的
- A\真是太坏了
- 这个有渠道
- 翁大爷的狗@Rakuten: claude -p下个月就要另外收钱
- -p吃什么可以flow来决定
- 应该能搞定
- 翁大爷的狗@Rakuten: claude -p下个月就要另外收钱
- 还好我不用了
- 就，不能走coding plan，但不至于用不了
- 之后要算agent SDK用量不计入subscribe用量了
- 刘思皓:?
- 哎，御三家都慢慢开始缩减了撒币力度
- 这是个啥
- 翁大爷的狗@Rakuten: claude-p下个月就要另外收钱
- 以后要戒断了
- 现在真的还是御三家吗？
- 任人宰割的感觉真不爽
- 翁大爷的狗@Rakuten:哎，御三家都慢慢开始缩减了
- 撒币力度
- gemini做slides还是可以的吧
- 确实 nano banana也不错的
- 求教claude-p是干啥的
- codex app 版做slide比较好使
- AAA9: gemini做slides还是可以的吧
- 你用一下试试就知道
- 5月21日23:28
- AAA9: 求教claude-p是干啥的
- 非交互式调用
- 有道理，拼字符串 benchmark的任务可以让便宜的sonnet去做
- akane: -p吃什么可以flow来决定
- 说是跑deepseek效果不错
- 泽文: 群友用过吗
- 如果为了省token
- 我都是opus写prompt 让dpsk api去做
- cherichy:有道理，拼字符串 benchmark的任务可以让
- 便宜的sonnet去做
- 是不是应该deepseek+codex?
- 我感觉现在直接模型拉满
- 这样codex只用分析和review 做好mgr了!
- 也可以
- AAA9: 是不是应该deepseek+codex?
- AAA9:是不是应该deepseek+codex?
- 工具调用差点意思
- 调度优化之类的交给cli
- dpsk便宜
- cursor 2.5 也有cli可以用吧
- deepseek有时候有点弱智
- dpsk换成kimi吧
- 缓存时间还非常长
- 据说dpsk每天18点下班
- 这个便宜 速度快效果好
- composer 2.5确实是个好模型
- 直接humanize的cc接deepseek就行
- 世界第一中转站的数据真是高质量
- 不复杂的活能干得不错
- 谁是世界第一中转站 cursor吗
- 翁大爷的狗@Rakuten: 世界第一中转站的数据真是高
- 今天用了用感觉composer 2的G言G语问题也好了不少
- 是啊
- 饽饽博: 谁是世界第一中转站 cursor吗
- 有codex review差不到哪里
- 笑死
- 翁大爷的狗@Rakuten: 是啊
- 5月21日23:31
- 差不多 Build 无所谓
- AAA9:是不是应该deepseek+codex?
- 我最近是在cursor里面用gpt 5.5 感觉也不错
- 我也是composer拥趸 便宜好用
- 翁大爷的狗@Rakuten: 今天用了用感觉composer 2的
- G言G语问题也好了不少
- 56
- 4.7和4.6就没提升了
- yuchao: 希望claude code下一个发布能大幅提升—下
- 4.6之前真的是非常的惊艳，简直就是震撼改变
- 是cursor api的5.5 还是codex插件的5.5
- AAA9: 我最近是在cursor里面用gpt 5.5 感觉也不错
- cursor
- yoi mame
- 我还挺喜欢vs系agent插件的。比cli好看但和cli—样方便
- 有啥一键迁移工具不 Claude 到codex
- 5月21日23:39
- 插件是可以直接共享session的吗
- 饽饽博: 我还挺喜欢vs系agent插件的。比cli好看但和
- cli一样方便
- 已经太久没用过vscode了
- 可以用cli resume回来吗
- codex自带
- 洋洋阳: 有啥一键迁移工具不 Claude 到codex
- 可以,session通用的
- cherichy: 可以用cli resume回来吗
- codex运行/experimental然后把external migration特性打开
- 那真没理由用cc了
- 郑权: codex运行/experimental然后把external
- migration特性打开
- cc配ds挺好的，量大管饱
- migration特性打开
- 空了试下

---

### 5月22日

#### 原文 L24903–L24920

[回到原文件 L24903](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:24903)

- 5月22日00:12
- Codex(98.9%) - Claude(1.1%) - All(100%)
- 郑权: codex运行/experimental然后把external
- migration特性打开
- 空了试下
- 谢谢~
- 5月22日00:12
- Codex(98.9%) - Claude(1.1%) - All(100%)
- Comparison, $0.0048 / MTok, Monthly Saving $1
- by SihaoLiu, v2.1.0, enter h or help for usage
- 第一次干到6位数
- 这个saving咋算的
- 好奇
- The more u buy, the more u save.PNG
- 5月22日00:13
- 这个saving不准确
- 因为我昨天就开始烧真钱了
- The more u buy, the more u save.PNG

---

#### 原文 L25003–L25014

[回到原文件 L25003](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25003)

- 5月22日00:43
- 大家好，我今天想到了一个很好玩的东西，把humanize2自定义的agentic flow集成到LLVM中，编译LLVM的过程
- 中通过agent筛选参数并通过cmodel去loop验证最优的解，然后作为参数回填给LLVM的虞书欣target，这样双轨一
- 号和双轨二号不同的cmodel都可以支持上、又或者不同的cmodel的timing model有更新，编译器也可以有更新，
- 我强烈推荐大家用一用 oh-my-pi，有效治疗了 gpt
- 5月22日00:44
- oh-my-pi可以理解为pi codir
- 专属不了一个月
- kami:后面就会变成自己的专属工具
- 我上一次用 pi 还是修龙虾的时候，后来不修了我就没用 pi 了，讲一讲群友是在用 pi 做 coding cli吗
- 哈哈哈确实
- ZZ: 专属不了一个月

---

#### 原文 L25021–L25044

[回到原文件 L25021](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25021)

- 我也
- 泽文: 我最近比较高强度用的就是 humanize gen-plan
- + codex/goal
- 我也是!
- 我其实不怎么用Humanize的RLCR本体
- 但是gen-plan我还是一直用
- 泽文: 我最近比较高强度用的就是 humanize gen-plan
- + codex /goal
- cc 也好 cursor 也好，plan 都太粗略了
- 主要是，我理解了 humanize 的实现以后，我所有的 flo
- gen-plan —半是配合 brainstorming + ask me a lot of question —起用
- 是的
- 泽文: 主要是，我理解了humanize的实现以后，我所
- 有的 flow 包括我临时的 prompt，我都下意识往这...
- 我现在觉得长程实现的SOTA是codex的goal
- 自从加入了本群
- 我用 cursor 的时候都开始和他 battle plan 了。。。
- rlcr可能只有在定向实现的时候才能和codex的goal拼一下
- 开放优化完全打不过
- /goal 里面会调用review?
- 不会，我一般会主动让它触发一下
- 或者直接/goal edit
- 看看吧
- 5月22日00:49

---

#### 原文 L25428–L25441

[回到原文件 L25428](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25428)

- 为啥有时候会这样
- did you stop in the middle of an rlcr loop? because
- pproved the stop?
- ight - I should NOT stop until Codex review approves
- RLCR loop, continuing to work. Here's the full' table
- on:
- 我前面搞了个类似humanize的
- 用codex审核他每一章节做得怎么样
- 但后面发现这个有点太慢了
- opus跟codex一起大概跑了十个小时吧
- 这个是什么claude版本的humanize还是codex的
- Eden:
- 就直接/tasks列所有任务了

---

#### 原文 L25481–L25495

[回到原文件 L25481](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25481)

- 5月22日17:12
- Task 模型膨胀 I MVP 只做 clarification、progress、 artifa
- 433
- Manager 变胖 I Manager 只做 conversation focus 和路由，
- 434
- 大结果压垮上下文|大结果必须 artifact 化，Task output 只
- 435
- 436
- Original Design Draft End -
- Read 1 file (ctrl+o to expand)
- Bash(ls docs/agentic-ai-engineer-v2/plans/ && echo "-" && pwd)
- Error: Exit code 1
- ls: docs/agentic-ai-engineer-v2/plans/: No such file or directory
- 确实降智

---

### 5月24日

#### 原文 L25673–L25718

[回到原文件 L25673](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25673)

- 还是codex好
- 我最近在尝试用ai自己做自己的workflow但是不是完全自主化
- 关一
- 给一个初始的workflow让他在上面打一些比较general的补丁
- 感觉好像这种做法有戏
- 跑了一个晚上他开始做出可以用的结果了
- AI1:只能改动workflow并且在云端服务器调用workflow，并且手动记录所有实验记录，每跑一轮记录一次，分析
- 原因，尝试改进，继续跑
- AI 2：云端服务器里面的ai 严格遵守workflow做事情
- 你workflow的描述是啥
- 在遵守某些特定规则，产生特定产物做任务的ai
- 5月24日03:33
- 比如我要求他必须在做任何task之前做一个类似deepresearch的东西(搜代码库搜互联网)
- 比如要有一系列tracable的产物，比如它可以用mcp工具接各种script去生成模板然后再写没做进入不了下一步
- 我是想问你是用一段自然语言描述workflow还是有一种“流程语言”似的“编程语言”
- 应该是后者
- 靠脚本mcp等工具实时的类似硬编码的东西
- 自然语言让ai遵守难度太高了我尝试了很久各种信息注入下也做不好服从指令还会污染上下文
- 我感觉agents自动设计驱动自己的flow肯定是下一步
- 不太一样
- 我还是手动给了一个workflow
- 5月24日03:48
- 然后让他可以在里面做一些我称之为general fix的东西
- 给一个真实任务虚拟环境
- general fix的意思是说
- 比如我希望的效果是 AI会监控代码的ETA 如果发现ETA很长代码一定有问题，立刻杀掉重做，而不是傻平平的等
- (这些要求和虚拟场景要做到的事情是我设定好的任务)
- 他不能修改prompt直接加入类似的prompt说写代码一定要eta，不符合预期杀掉
- 而是我希望只能说：你必须实时监控代码，如果有异常就杀掉（模糊不完美的prompt)不要浪费时间
- 让他自己不停的尝试不同的修改 workflow设计 来达到效果
- 不太希望说一个问题打一个补丁
- 我给AI1清晰完整的要求
- AI1 只能给AI2 workflow或者是这种不完美的prompt
- 希望AI2靠着workflow解决问题
- 5月24日03:54
- 那和开subagent的区别是啥
- 差别是针对一个任务设计好workflow之后可以复用啊
- 类似sub-workflow?
- 好像get了
- 我其实设计的是一些states
- 然后让ai自己组装这些state
- 5月24日03:59
- 比如review state就必须和其他ai rebuttal直到通过
- 比如搜索state必须做到尽全力搜索所有资料以及给真实的回答
- 比如ai如果说 codex 没有stop gate 这就是错误回答

---

#### 原文 L25744–L25756

[回到原文件 L25744](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25744)

- 5月24日09:01
- 我必须承认humanize1已经完成了它的历史使命，在长程任务的定向实现上，codex的效果的确更好，但这里有几
- 个可以优化的地方：
- 5月24日09:02
- 1. 便宜的B，昂贵的R
- 2. 多轮B，一轮R
- 专指codex的/goal
- 刘思皓:我必须承认humanize1已经完成了它的历史
- 使命，在长程任务的定向实现上，codex的效果的确...
- 3. 项目历史记忆(bitlesson)
- 5月24日 09:07
- 我觉得一个flow最好的宿命就是4个月左右的时间被claude/codex工具内化，

---

#### 原文 L25959–L25989

[回到原文件 L25959](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25959)

- 5月24日22:12
- woc，这个claude code新的workflow，真有点抄H2的意思啊。@刘思皓
- 啊?
- 又更新了？
- Claude Code重大突破:
- Workflow功能完整实战教程！ultr...
- YouTube
- Claude Code
- Workflow
- 划时代创新
- 现在看来，我们需要一个agent领域的EDA了
- 咦，关键词是 ultrawork 吗
- 那我好像记得以前就有
- 5月24日 22:17
- 哦，看起来 ultrawork 是 workflow 的子集
- 5月24日 22:37
- claude code新的workflow，真有点抄H2的意思啊..
- 官·方·认·可
- 抄h2是不可能的
- 但是这尼玛真太tm像了哥们儿
- 都在做都在捐
- 看来我做agentic flow，确实taste还行
- 香港科技大学 研究助理教授 徐策羽：woc，这个
- 牛的
- 香港科技大学研究助理教授徐策羽：
- Claude Code
- WWorkflow
- Claude Code重大突破: Workflow功能完整...
- 划时代创新
- 不做就不用做了

---

#### 原文 L25994–L26012

[回到原文件 L25994](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:25994)

- 我丝毫不怀疑workflow EDA的能力能被训进下一代opus/mythos
- 我觉得h2还有个大问题
- 就是h2现在是以对话为中心的
- 这不对
- 需要以产物为中心
- 对话的带宽太低了
- 其实我在想不如做个python库直接用python描述你的产物和flow
- 应该直接就是“神圣的卡拉连接着我们”
- right
- 刘思皓:应该直接就是“神圣的卡拉连接着我们”
- 5月24日 22:40
- 我觉得人类输出token的速度已经成为了核心的bottleneck
- 所以还是得end to end
- 我得把h2里面那个对话view砍了
- end to end并不意味着许愿
- 5月24日 22:46
- 我自己其实在组内做了几个社会实验，我还没有找到什么比打字/说话更有效的交互方案..
- 唯一能稍微解决问题的方法就是，multiple-human in the loop

---

#### 原文 L26032–L26068

[回到原文件 L26032](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:26032)

- 5月24日23:01
- agent输入法——你在知乎/微信公众号上应该已经看到过很多”agent输入法”的样例了
- 而且我还观察到过一个现象，
- 随着和AI聊天越来越多，我自己的语言越来越随意(反正AI看得懂)，我发现我给AI常常发送的是一系列的【半句
- 话】组成的缝合怪
- 人类需要脑机接口
- 这虽然看上去符合【agent输入法的定义】
- 但是我有点怕【自从上了本科，作业可以用键盘输入word上交后，我握笔写字的水平极具恶化，现在写字和鸡爪子
- 一样】的事情在语言层面重写
- “我”才是系统的瓶颈
- 5月24日23:07
- 跟这个类似的，我发现不能用许愿workflow太多
- 可编程的 prompt 确实比较重要。
- 用太多了甚至会失去intuition
- 前段时间忙又想不让agent闲着，许了很多愿，结果发现对我自己的影响很坏
- 最主要是让自己作为reward model变得迟钝了
- 这会让 soft constraint 变成 hard constraint
- 赵雪岩: 可编程的 prompt 确实比较重要。
- 学愿出来的不会都是错的吗
- 去思考修复错误的，比重写困难的多
- 5月24日23:15
- 如果不想让自己
- 或者有意识的把自己的技能做成agent flow
- 以前是造轮子帮助自己思考现在应该变成造flow了
- 为啥
- 刘诗楠:前段时间忙又想不让agent闲着，许了很多
- 愿，结果发现对我自己的影响很坏
- 没看懂
- 5月24日23:20
- 是说你许愿自己不懂的领域无法评价ai糊出来的东西吗
- 很有道理，但是感觉做skill我还是会的，就把自己的prompt记下来，但是还不知道怎么造flown
- akane: 以前是造轮子帮助自己思考现在应该变成造
- flow了

---

### 5月25日

#### 原文 L26107–L26117

[回到原文件 L26107](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:26107)

- 5月25日 09:05
- 话说为什么humanize2不用lang graph之类的工具啊
- 5月25日 09:25
- 这个确实有用，代码和文档保持互相索引，可以钩住彼此的update
- 吴自华Gabriel: 对文档之间相互引用，以及代码注释
- 引用文档都有严格的检查
- 我以前想过一个 code owner system
- 我觉得最大的副作用是带来愤怒
- 刘诗楠: 跟这个类似的，我发现不能用许愿workflow太
- 因为ai太他妈喜欢over claim了

---

### 5月26日

#### 原文 L26376–L26406

[回到原文件 L26376](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:26376)

- 夸张极了
- 我现在能开并发了今天打100并发
- 是并发还是单线程
- 刘思皓: https://github.com/SihaoLiu/Lzvm我正在
- 欣赏神迹
- 开源芯片 agent flow 张宇鑫: 是并发还是单线程
- 我就开了一个codex
- 现在的agent并发协作能力很差
- openai那个敏捷看板有说法的
- 其实不要说agent了，人类本身也没什么并发协作能力
- 刘思皓: 从头到脚就只用了 codex的/goal
- 都是得分工
- 也就是说，“从0构建”和“增量开放式调优”这两个活，其实只需要3个东西就够了：
- 1. dynamic progressive planning
- 2. slice verifier
- 我同意这句话
- cherichy: humanize完成了历史使命
- 分工干活的话很考验orchestrator
- humanize没有progressive planning
- yoct mame
- 优”这两个活，其实只需要3个东西就够了：1.dyn...
- 很多harness技巧都会逐渐被内化，然后我们的任务就是和agents共同进化
- 哦哦 3. goal tracker
- Luke: 3 呢
- 走神了
- 我感觉问题不在这里？
- 张子健:其实不要说agent了，人类本身也没什么并发
- 协作能力
- 注意力涣散了

---

#### 原文 L26500–L26580

[回到原文件 L26500](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:26500)

- hmmmm
- 但是他会偏离很多goal里面写的详细指令
- RC@黑手套:但是恢复goal的方法很简单
- 就是他的优势是更灵活
- 看起来可能“聪明”
- 因为我的goal是：规范的做出一个最终结果（要有符合规则的中间产物让我检查）
- 了解，也就是说现在codex的goal，你的体验是比你之前用humanize的rlcr来得差一些?
- B4RRy: humanize应该强不少
- 是的
- 而且goal本质就是一个stop gate而已
- 了解，那我再去研究一下
- 你不写详细一点他一两轮stop就么了
- humanize: —个强review + static planning
- codex's goal: —个弱review + dynamic progressive planning
- 对呀，所以需要明确的条件对吧，详细并不=explict
- 点了
- 刘思皓: humanize: —个强review + static planning
- codex's goal: —个弱review + dynamic progressi...
- 我感觉各有各的好坏。我觉得最后应该是：
- dynamic progressive planning + review
- 需要 gen plan
- B4RRy: 你不写详细一点他一两轮stop就么了
- 再加上合理的检索
- 可以没有人类了
- 就给supervisor—些权限改pian?
- 刘思皓：我感觉各有各的好坏。我觉得最后应该是：
- dynamic progressive planning + review
- 我感觉应该引入第三个实体
- Eden: 就给supervisor—些权限改pian?
- codex-goal里面的plan是builder自己做的
- 问题是有明确的条件
- cherichy:对呀，所以需要明确的条件对吧，详细并不
- =explict
- 现在问题是他不遵守plan的内容做啊
- Luke: 需要 gen plan
- 我plan写了他认为做完了打勾
- 确实
- 5月26日09:04
- 结果一看做的不是plan的要求
- 就是instruction follow太垃圾了
- 所以还不如硬编码的例如loop
- 拐到3a了
- 每次吧要求强行输进去
- 很垃圾
- 还喜欢绕过，模拟，bypass
- 没办法用程度只能跑那种十几分钟的迷你玩具任务
- 我感觉是即使给了个plan worker如果撞死循环了就会自己换路径，这时supervisor判断是否批准就行？
- 刘思皓:我感觉应该引入第三个实体
- 你必须得说禁止xxx
- 我这里更糟糕一点
- 我说你删掉xxx从xxx代码重新开始做
- 结果我第二天起来
- 发现她没有删掉xxx
- 还在旧代码搞
- humanize不会发生这种事情，因为改动Plan这件事必须由review来做
- 刘思皓: humanize不会发生这种事情，因为改动Plan
- 这件事必须由review来做
- 现在终于理解了
- 拿捏不准
- Eden: 我感觉是即使给了个plan worker如果撞死循环
- 了就会自己换路径，这时supervisor判断是否批准就...
- 啊?
- Luke: 现在终于理解了
- 人review吗
- humanize里面有一个核心机制，就是builder但凡想要改goal-tracker，都需要给reviewer打申请，让reviewer自己来改。
- 但是由于这个环节非常严格，所以你的Plan几乎是一个静态的了
- 但是Codexgoal的做法不一样，它允许builder自己给自己做plan，reviewer只判断是否完成
- 但是现在plan会生成defer项，导致reviewer一直不结束
- 这样也有问题，但是在快速推进项目的时候非常有效（个人观点
- 对那个也是社区反馈才加入的
- Joe布衣:但是现在plan会生成defer项，导致reviewer
- 一直不结束
- 5月26日 09:09
- 不然会钻牛角尖
- 5月26日 09:09
- rlcr确实是有些塞得太慢了就磨叽扯皮
- 刘思皓：这样也有问题，但是在快速推进项目的时候非
- 常有效（个人观点
- 所以我觉得第三个实体可能是必须的
- 不太确定
- 我得拿h2搭一个试试看

---

#### 原文 L26875–L27015

[回到原文件 L26875](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:26875)

- 同意
- Julian: 感觉mdx也可以的
- 给钱
- 开源芯片 agent flow 张宇鑫: 我帮他上22分,交付没
- bug的CPU
- 总比CPU公司几百万买新思的SDING软件靠谱
- 除了mermaid字体有点太小了以外没毛病
- mermaid感觉拉完了
- mermaid不太行啊
- 表达能力太弱了
- 给大家同步汇报下目前的能力边界和认知边界 H2/H3 全自动我想象到的场景
- 5月26日11:28
- 现在orchestrated workflow基本有三种模式:
- 1. 以对话为中心的
- 2. 以产物为中心的
- 3. 以flow为中心的
- h2，现在是1+3
- 我感觉似乎应该做成2+3的
- 然后偏2一点
- 好奇实现路径
- 开源芯片 agent flow张宇鑫:我帮他上22分,交付没
- bug的CPu
- 对话，我现在越来越觉得是个低带宽的糟糕渠道
- 对话是指agent之间的交流吗？还是人和orchestrated workflow的交流
- 去年还和xxagent负责人争论人和AI谁主导
- 人类带宽低，但感觉人类的 taste 对决策方向的影响比较大
- 被他骗去教小白2个月VIBE Coding咋用
- 5月26日11:30
- 这是我生成的html，说实话我觉得比md好看多了
- clip-skew-report.html
- HTML
- 26.2K
- 思考
- clip-skew-report.html
- HTML
- 26.2K
- 微信电脑版
- ai把所有的架构实现全尝试一遍就行了，直接100并发
- 选最优解
- 暴力流
- 思考
- agent之间似乎就不该有任何交流
- 张东宇:对话是指agent之间的交流吗？还是人和
- orchestrated workflow的交流
- 一切都为了交付产物的设计
- flow来辅助
- 但是解空间可能不是100，可能是100^n
- 已老实
- 现在连DSE 这种简单任务其实agent 也并不能完全替代贝叶斯优化这种老方法
- 对，数学是这样对
- 赵雪岩: 人类带宽低，但感觉人类的 taste 对决策方向
- 的影响比较大
- 虽然我感觉后者感觉也是问题很大
- 在目前的实战感觉上，ai可能连100开都不需要，因为可以根据性能探针的结果让ai围绕最堵塞的几个点去优化就能大
- 幅提升性能
- 赵雪岩:但是解空间可能不是100，可能是100^n
- 5月26日11:36
- 确实
- 要，因为可以根据性能探针的结果让ai围绕最堵塞的...
- 和我体验一致
- 全局最优不重要，够用就行
- ncu report skill 好用
- 思考
- 5月26日11:44
- 现在感觉如果给ai安排一个方向，他其实能执行的很好。但是如果让ai自己找一个方向，就比较麻烦
- 试试humanize的gen-idea
- gen idea
- 8 agent并行
- 我给codex加了一个gen-idea 好像没合进去
- 5月26日11:49
- 我现在急需一个humanize青春版
- 之前有个gen-idea
- 加了两轮loop
- 5月26日11:50
- 到时再提个pr
- hhhhhh
- Lurker: 我现在急需一个humanize青春版
- 好我今晚就看
- 赵雪岩: 我给 codex 加了一个 gen-idea 好像没合进去
- /goal很像humanize青春版，但是太容易跑偏了
- Lurker:/goal很像humanize青春版，但是太容易跑偏
- 5月26日11:55
- 还是goal-pro
- 不参与定价
- 03
- ta
- t1 13
- Q2
- 你更希望一个humanize青春版
- @smdyryla-2天
- Can agents in cmux talk to each other?
- Q7
- 03
- ta
- Q11
- Q2
- tl
- 关淮
- 0 显示翻译
- with this are silly.
- 我前天看到这个
- 5月26日12:00
- 我说实话一直没意识到
- 但我没法反驳
- 似乎agents就完全不应该沟通？
- 难道不是吗
- 就看 结果 MD
- 所以我完全不用slock
- 我觉得是的
- 一切以交付产物为中心，flow作为辅助“轨道”
- 让agents去“沟通”来解决问题
- 似乎真的就是浪费token
- 我试过商量和命令两种沟通方式现在想想确实都没必要
- 5月26日12:05
- 不是聊过
- 刘思皓: 因为同事们和老板
- 不太一样，这次是说沟通都不用
- 人类也只有在brainstorm阶段才需要沟通吧。
- 群聊的聊天记录
- 刘思皓: 否则信息传递会有偏差，最后就很

---

#### 原文 L27030–L27049

[回到原文件 L27030](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27030)

- 为了让你快速on board
- 同一个模型为啥要agent开会
- 因为你自己探索可能要调用很多工具，找很多遍，可能会找漏了
- perspective不同?
- 如果代码特别多，几千万行，他可能要先花很多token来探索
- offhand可以，一起干是没必要的
- 但感觉一个model就可以有multi persona了
- agent 赛马
- 是的，开个三四个，然后另外三个都没有发现问题，第4个就发现了
- 饽饽博: perspective不同?
- 想到之前那个三省六部制
- 刘思皓:同一个模型为啥要agent开会
- 有道理还是抽卡的问题
- Luke: 是的，开个三四个，然后另外三个都没有发现问
- 题，第4个就发现了
- 这个完全是噱头
- 1900：想到之前那个三省六部制
- 是的，我只在这一种情况下让 agent 对话
- Luke:如果代码特别多，几千万行，他可能要先花很多
- token来探索

---

#### 原文 L27057–L27071

[回到原文件 L27057](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27057)

- (上次开发大会看的1个卖600支持十几个一起陪伴
- 如果另一个 agent 和当前 agent 都用了 150k codex context，我知道另一个 agent 有回答问题所需context，我会
- 让他们对话
- 纯噱头
- 不能做好交接文档吗
- NV 周耀阳: 如果另一个 agent 和当前 agent 都用了
- 150k codex context，我知道另一个 agent 有回答...
- 感觉更像是知识沉淀？
- 那写个.md不就行了，互相对话感觉容易混乱
- NV 周耀阳: 如果另一个 agent 和当前 agent 都用了
- 150k codex context，我知道另一个 agent 有回答...
- 5月26日12:12
- 互相对话污染上下文
- 对啊，为什么要对话，handsoff就好了
- coding场景是这样。但其他场景会不会需要对话？

---

#### 原文 L27077–L27108

[回到原文件 L27077](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27077)

- 吴自华 Gabriel: 多角色扮演这种
- 比如宿主电脑上的gcc版本太低了，依赖版本冲突，100个agent可能有50个都需要用到这个工具，那互相交流不一定
- 是好主意，但是某个agent踩坑，直接下载到了某个预编译发行版，然后写到文档里，其他agent来了以后读一下就
- 省掉每个agent几个小时的搜索/编译/尝试修复不兼容等问题
- 你们用cc的 team-onboarding了吗
- 一旦进入到这种记忆层面，维护就麻烦起来了
- 明扬:比如宿主电脑上的gcc版本太低了，依赖版本冲
- 突，100个agent可能有50个都需要用到这个工具，...
- 因为过时/错误记忆的危害比没有记忆更大
- 这个任务专属，结束后就清理掉了
- 它就定义了一些share和cache
- 明扬:比如宿主电脑上的gcc版本太低了，依赖版本冲
- 突，100个agent可能有50个都需要用到这个工具，...
- 这样就没有过时问题了，只剩错误问题
- 真以为然我写了hook让它更新记忆总是忘
- 吴自华Gabriel: 因为过时/错误记忆的危害比没有记忆
- 更大
- 5月26日12:17
- 结果过时记忆害得我版本重滚
- 比如某个agent路线错误，反复尝试最后甚至下载了源码修改编译，结果导致修改版反而是错误的，其他agent在这
- 个版本上继续工作，全军覆没
- 这种东西很难证明，不像公式那么纯粹
- 这个是workflow问题
- 明扬:比如某个agent路线错误，反复尝试最后甚至下
- 没有做review就继续推进了
- 理想情况下，agent协作时，输出出来的“经验”应该是可以被客观验证的。约等于≈lemma
- 能被客观验证不代表不会过期/错误啊
- 明扬：理想情况下，agent协作时，输出出来的“经
- 验”应该是可以被客观验证的。约等于≈lemma
- 但实际上软件系统，依赖环境复杂，几乎无法设计验证方案
- 比如换了环境：容器里换到了宿主机

---

#### 原文 L27115–L27131

[回到原文件 L27115](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27115)

- 5月26日12:21
- 对，所以我说是理想情况下的“经验”，我没有推销这套工作流，你应该能看出来，我并不信任它
- 但是太困难了
- 人类自己也做不到
- 总结的经验也有很多是错的
- 我现在用agent或者goal，最大的问题，就是看着他干活，总是觉得他跑偏了，想干预。。。
- 所以goal不如h2
- FanLong:我现在用agent或者goal，最大的问题，就
- 是看着他干活，总是觉得他跑偏了，想干预。。。
- 用humanize
- FanLong:我现在用agent或者goal，最大的问题，就
- 是看着他干活，总是觉得他跑偏了，想干预。。。
- 怎么让他们对话
- NV 周耀阳: 如果另一个 agent 和当前 agent 都用了
- 150k codex context，我知道另一个 agent 有回答...
- 如果纯粹的逻辑编码可能还好，一旦涉及到外部环境，硬件，这个可信的验证方案就很难设计了
- 感觉需要任务专属 share mem

---

#### 原文 L27145–L27188

[回到原文件 L27145](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27145)

- 我觉得还是想要个goal pro
- 所以我觉得，协作中agent产出的经验，可信度很低，一个agent写下的evidence越多只会误导其他agent一起全军覆没
- 明扬: 前两天我调查的一个后端响应延迟问题，cc坚持
- 它的调查方向，还给了我很多evidence证实它的猜想...
- 5月26日12:32
- humanize比较不容易跑偏
- 都是应用侧的搞法罢了
- Lurker:有人让ai相互交流去玩合作类游戏
- see ur point. 我对AI的信心建立在opus4.6的经验上。4.7幻觉严重
- 明扬： 所以我觉得，协作中agent产出的经验，可信度
- 很低，一个agent写下的evidence越多只会误导其他...
- 5月26日12:39
- 我如果不中断它的话，它要unsafe/ffi去强制关闭fork/join继承的fd了
- exactly
- 吴自华Gabriel: 因为过时/错误记忆的危害比没有记忆
- 更大
- 我被auto memory坑过好几次
- 以至于之后claude.md我都自己手动维护
- 其实也许我是偏的。导师对这学生，经常瞎指挥。。。
- 刘思皓: humanize比较不容易跑偏
- 对着
- 哈哈哈哈
- 5月26日.12:54
- 我觉得auto memory已经很收敛了
- 刘思皓:我被auto memory坑过好几次
- 5月26日12:55
- 所谓的auto一点都不auto
- 都是输入驱动的
- 它犯错了，我骂它一句，它会道歉然后保存auto memory，平时它自动执行的时候没见过挣扎许久终于解决了，然
- 后保存个memory
- 5月26日13:00
- 对啊既然auto不auto
- 明扬: 所谓的auto一点都不auto
- 我用过一周memory就没再开过，感觉这个功能意义不明
- 应该是用户体验？用户已经要炸毛了，赶紧存下来，假装记住了，以后不会再犯了
- “我让你删测试环境！测试环境！测试环境！你给我删的是什么？
- 把agent比作module，memory不就是一堆泄露的state吗
- 那个auto dream也让我感觉有点意义不明
- 5月26日13:13
- 最烦的就是auto随机
- 测试的时候好好的正式用的时候总不更新
- 但又不想引入冗长的记忆系统。归根结底还是model能力不足
- claude删过我.codex

---

#### 原文 L27210–L27222

[回到原文件 L27210](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27210)

- 请问omp全称是啥
- oh-my-pi吧
- 真心不错，
- 5月26日15:57
- pi agent 搭配上gpt 5.5 是不是会舒服很多
- 能跑humanize吗?
- 泽文: 真心不错，对claude code plugin 和 skill 什么
- 的兼容性都还okay
- 5月26日16:02
- 5月26日17:18
- omp 有 goal 么
- 5月26日17:25

---

#### 原文 L27327–L27338

[回到原文件 L27327](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27327)

- 5月26日20:24
- 这个需要先装codex版的humanize吧?
- 我用的。
- 它会不会底层偷偷给你启动了humanize
- 这个和原生 humanize rlcr 的区别是，你可以获得一点 workflow
- 不装试一下
- Joe布衣: 它会不会底层偷偷给你启动了humanize
- 5月26日 20:48
- 虽然我问过很多次，不过在今天我想再问一遍，做ppt最好用的agent方法是什么？
- 有没有一些搞的比较好的开源项目之类的
- claude design 挺好用的

---

### 5月27日

#### 原文 L27541–L27575

[回到原文件 L27541](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27541)

- 看看herdr
- 然后各家目前在agentic workflow上面的努力感觉在2个月左右的时间就会收敛
- https://github.com/ogulcancelik/herdr是用钩子做的
- 大道朝天，好用的设计大家都会发现
- 不好用的就会变成概念...
- 笑死了
- 确实
- 对，我感觉最近（以及未来）做harnessflow的人，其实有一个很明确的指标就是：
- 你做的东西能不能在2-3个月内，被官方推出一个内化的选项所覆盖
- 能：你做得不错，但是现在官方内化了，你需要再官方的基础上继续改进
- 不能：你哪里做错了
- 没有被内化/取代的东西，我一律认为经不起实践推敲
- 5月27日02:50
- humanize 一天也只能用 5.7M，感觉机器学习真的用不了多 token。
- 一周用了13.3M20%，他一周的限量难道是50M？但感觉应该也没那么少。
- 你的任务是不是有很多长时间的run
- 就是实验本身要跑很久的
- humanize感觉对于我的需求实在是太慢了，探索阶段得搞快的
- 加用伤的测向购力八针左右的法
- 工差不名800M
- 如果你的测试回路在一分钟左右的话，humanize跑一天差不多800M - 1.3B
- 探索阶段，感觉搞这么详细，真的是浪费时间
- 那我觉得你可以用/goal?
- humanize目前不是那么适合跑实验
- 5月27日02:54
- 我真的觉得goal不错的
- 确实
- 需要 goal
- 感觉就是写代码的时候
- 翁大爷的狗@Rakuten: humanize目前不是那么适合跑
- 实验
- 就让他写代码好了

---

#### 原文 L27579–L27590

[回到原文件 L27579](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27579)

- 5月27日03:00
- humanize我觉得还是需要回归它设计的本心：
- humanize是一个在你把东西都想清楚之后，系统性实现的一个flow
- 如果你需要探索性的东西，humanize有一个gen-idea-> gen-plan的flow
- 刘思皓: [链接] Humanize 带来的Codex
- 使用范式变化，解锁 Agent 优化 kernel
- 上限
- 刘思皓:[链接] Claude 实现、Codex 审...
- 聊天记录
- 这里有个Everything about Humanize的压缩包，新来的朋友可以看看
- 牛逼
- 5月27日03:09

---

#### 原文 L27599–L27612

[回到原文件 L27599](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27599)

- 看到了
- Ligeng的KDA和 BBuf的AI-Infra-Auto-Driven-SKILLS
- 如果你要做开放探索的东西，需要大改humanize
- 实验目标明确，反馈清晰，搜索空间也不是那么大
- 式老道它本压上应达该目
- https://www.youtube.com/watch?v=XNtkiQJ49Ps
- 我觉得这个视频里面的设计特别好
- 我已经在n个地方看到：不要让agents沟通这个设计了
- agents group chat是一个低效且无用的特性
- 我在做一个这样的东东如果有效能不能在群里找大家做小白鼠啊(不是)
- 刘思皓:如果你要做开放探索的东西，需要大改
- humanize
- 也没那么开放探索
- B4RRy:我在做一个这样的东东如果有效能不能在群里

---

#### 原文 L27688–L27707

[回到原文件 L27688](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27688)

- - 想要发布招聘信息请直接联系群主。
- 项目：https://github.com/PolyArch/humanize
- Token监控: https://github.com/SihaoLiu/ai-usage
- Humanize Slides
- - Humanize1: https://drive.google.com/file/d/1bvQI_IE1JyXqW6NkSMFPrs_G0erAdgca/view?usp=sharing
- - Humanize2: https://drive.google.com/file/d/1j-Xxtwf5GQ5PYcJ8GInd6XOKNuizUNbl/view?usp=sharing
- 《Humanize 带来的Codex使用范式变化，解锁 Agent 优化 kernel 上限》
- - https://mp.weixin.qq.com/s/pScZ_9cA-6cWUPjfcGjNyg
- 《Claude 实现、Codex 审查、人类决策领航：Humanize 项目用 RLCR 编排长程闭环迭代任务》
- - https://mp.weixin.qq.com/s/qceRk9Qfq0Q3CTdD6P1Vag
- 《SGLang SOTA Humanize Loop:让 Codex自动追推理性能到SOTA》
- - https://mp.weixin.qq.com/s/6uzb0OFDCDt4xmRcWaelaw
- 《让 Agent自己优化 CUDA kernel,并在MLSys 2026 FlashInfer Full-Agent Track拿下前三》
- - https://mp.weixin.qq.com/s/xlOIr4y60dzyeOn_3toipA
- 《日烧 6300.刀才明白：Agent团队飞轮是怎么转起来的》
- 5月27日05:45
- 让agent来管理
- 《Humanize: —个 prompt 重构 GEM5的构建系统》
- - https://zhuanlan.zhihu.com/p/2011939681307206316
- 发出河南的声音

---

#### 原文 L27720–L27733

[回到原文件 L27720](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27720)

- 5月27日06:06
- 想问下为什么humanize 不默认在.humanize/plans下面写plan呢?每次手动输入都很麻烦
- 我理解这个 motivation 是想让 plan commit 进仓库。但是大多数 repo 不会 accept 这个，而且我的 plan 是给自
- 己看的，是中文的，repo里也不太能接受（
- 5月27日06:15
- 不太对，humanize的plan默认不进入git
- okok，那应该是我理解错 motivation了
- 按照设计，humanize的plan默认就不应该进入git,如果你需要进入，还需要额外加一个--track-plan-file
- 不不不，我只是在想为什么 plan 不默认进入这里
- guapisolo: 想问下为什么 humanize不默认
- 在.humanize/plans下面写 plan呢?每次手动输入..
- 毕竟idea 已经默认在.humanize/ideas了
- 了解
- hmmm

---

### 5月28日

#### 原文 L27881–L27904

[回到原文件 L27881](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27881)

- 5月28日04:20
- omp is soooooo good
- I need to build h2 on omp
- Reiko:这比数学的llm+lean还要激进，因为物理缺少
- 相应的验证工具
- 这么牛。
- 刘思皓: I need to build h2 on omp
- 太多做唯相模型了，定义这个定义那个，谁也不知道哪一个是对的hhh
- 炒作炒作
- 5月28日04:29
- 啥事OMP?
- 刘思皓: omp is soooooo good
- 是OMP，我感觉我已经out了
- 让我想到某个并行的东东
- OMP_THREAD_NUM
- 对，我也只知道某个远古的并行的东西
- oh my pi
- pi还鼓励你开源对话
- oh my pi
- https://github.com/can1357/oh-my-pi
- 5月28日 04:35
- 非常夸张，我觉得humanize2不在omp里面构建是完全不合理的
- 它把腳手架全部都搭完了
- 5月28日04:40

---

#### 原文 L27995–L28070

[回到原文件 L27995](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:27995)

- 怎么看那张图
- 5月28日08:56
- 我正在看
- humanize cycle好像比别的多了
- 400
- which one
- Luke: 怎么看那张图
- 差点?
- 过去了
- 哦humanize不是为了开放式优化迭代的
- 优化cycle那个场景显然不好
- 而且默认设置下，如果5轮没有进展，humanize就会结束
- 所战目目结市了
- 这样
- 扎实实现和开发优化是完全两个不同的flow：
- - 前者是一个强review + 弱发散 + 强约束的过程
- - 后者是一个弱review + 强发散的过程
- 把humanize用到开放优化的场景其实并非我设计的本意...但是意外地，效果还不错
- 5月28日09:02
- Humanize — Design Initiatives
- Belief:
- • LLMs are much more knowledgeable than human (30T token pertaining)
- - LLMs remembers more tricks / tips than human (NIAH tests)
- 7x24 agents would eventually outperform human (never tined / rest)
- 你还能有Codex聪明？
- OK, but why my agents fails?
- 比如自己先搜20个可能有用的方案
- 排个序号
- 让他每一个实验循环几轮确定实现没有任何错误参数合适结果依然不好就做下一个
- @seed 何意味
- 也可以作为开放式优化其实如果转换成扎实实现
- 又黑我豆包是吧
- 智谱黄睿博:
- 对 其实现在的gen-idea -> gen-plan -> rlcr 就是这个思路
- B4RRy:让他每一个实验循环几轮确定实现没有任何错
- 误参数合适结果依然不好就做下一个
- 但是难点在于很多时候一些idea是要在做了一定实验获得更多数据才会知道的
- humanize: build an exploration tool, not build tool while exploring
- 是不是能做成rlcr到一半回去gen plan
- 给更多的condition去重新生成新的要做的idea
- 给更多的condition去重新生成新的要做的idea
- 不行。漂移太厉害
- 对我在humanize非常早期说过这句话：实现一个探索工具，而不是一边探索一边实现
- 刘思皓: humanize: build an exploration tool, not
- build tool while exploring
- ic
- 5月28日 09:07
- 他的解读都是错的，很多错
- Luke: 不行。漂移太厉害
- 群聊的聊天记录
- 撒米提:我写了好几个部分，说有哪几种可
- 能的方案
- 撒米提:叫他帮我implement了过后看效
- 这是两个月前的讨论
- 5月28日09:17
- 这里是单path local minima了?
- "Flow" Matters in Agent Productivity
- 对我说的就是这张图
- Luke: humanize cycle好像比别的多了
- 那个不是humanize蹬出来吗
- 这个曲线是这周跑的，这周gpt和opus都大幅降智了。。。
- Garrick:不是我看最低已经900多了吗
- 一个月前确实能跑出9字头
- 5月28日 09:23
- 但意外的效果也还不错loll
- 刘思皓: 哦humanize不是为了开放式优化迭代的
- get
- 张子健: 这个曲线是这周跑的，这周gpt和opus都大幅
- Eden:
- ligeng今天的talk
- 核心还是让agent「自主」「可控」的跑很久
- 这图是我第一次对各种flow进行一个横向的比较
- 跑这种测试实在是太贵了

---

#### 原文 L28079–L28086

[回到原文件 L28079](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:28079)

- 但是我不能放出来
- 1. agent 比人聪明
- 2. agent 比人技巧强
- 3. agent 见过的 tricks 比人多
- 所以只要一直跑下去，就能超越人
- 感觉这个问题还是挺大的，harness很难做ablation
- 刘思皓：跑这种测试实在是太贵了
- 先别急，后面整理下 caption弄一个高清的给群友

---

#### 原文 L28130–L28149

[回到原文件 L28130](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:28130)

- 能够催生好多长程flow
- 这东西 humanize 2/3 出来，人均 token 不得 10x /20x 啊
- nv一个季度30b利润
- 一个月才0.5M
- 5月28日 09:29
- codex goal 三天解决了我一个一个月没搞好的 bug
- 我觉得nv粒度还是不够大
- 十万亿
- 流口水
- claude goal：我不听我觉得我做完了
- 还有！
- humanize推广后，年底说不定就七万亿了
- 十万亿
- claude goal：我不听我觉得我做完了
- 还有！
- 今天 office hour 怎么有人问 humanize给 amd写 kernel 得
- 当着 nvidia 员工面 ntr 是吧
- 怎么给国产卡写kernel

---

#### 原文 L28194–L28207

[回到原文件 L28194](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:28194)

- 5月28日 09:57
- 力*度。这种长程flow如果能够搞出一个x2-5效果的，运行时间哪怕x100都有人接受.
- 刘思皓: 我觉得nv粒度还是不够大
- nv怕不是笑麻了
- 如果我是让我的Al迅速的给我matplotlib画个图，那么他应该走的是swarm路线迅速并发，把图画好
- 这波我觉得和剧本—样：opus 4.7 + cc's goal都拉胯。然后codex的goal + 一直一骑绝尘的review
- 刘家昌: claude goal:我不听我觉得我做完了
- 如果我要写一个CPU，那么他应该走极致review路线，把所有的test应写尽写
- flow武器库是吧
- 合理的
- h2其实是有想做一个flow library
- workflow as task-level alignment
- 但是自适配动态flow这种东西
- 还是需要留给h3

---

#### 原文 L28400–L28411

[回到原文件 L28400](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:28400)

- 太差了。
- 刘思皓:长程任务在人类学自己的题目上，codex能好
- 40%,1581 vs 1122, lower is better
- 5月28日14:35
- 这个曲线是我跑的。Claude Code无论用/goal还是简化版的Actor-Reviewer架构(autopilot)，都会在某个随机时
- 刻陷入复读机状态
- 刘思皓:长程任务在人类学自己的题目上，codex能好
- 40%,1581 vs 1122, lower is better
- Ralph Loop强制每次运行重置会话，反而让Claude Code能有更好的表现
- 把session transcript全部存好
- 我这里也有一个等价问题的全session

---

#### 原文 L28600–L28632

[回到原文件 L28600](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:28600)

- 群公告
- -本群话题为技术相关的AI/LLM开发相关工具、流程、心得。
- - 带偏话题的情况会提醒一次，连续两次带偏话题会被移除。
- - 想要发布招聘信息请直接联系群主。
- 项目：https://github.com/PolyArch/humanize
- Token监控: https://github.com/SihaoLiu/ai-usage
- Humanize Slides
- - Humanize1: https://drive.google.com/file/d/1bvQI_IE1JyXqW6NkSMFPrs_G0erAdgca/view?usp=sharing
- - Humanize2: https://drive.google.com/file/d/1j-Xxtwf5GQ5PYcJ8GInd6XOKNuizUNbl/view?usp=sharing
- - Humanize — past, present, and future from Ligeng@Nvidia
- [文件]Advancing Token Productivity w: Agent Loops.pdf
- 《Humanize 带来的Codex使用范式变化，解锁 Agent 优化 kernel 上限》
- - https://mp.weixin.qq.com/s/pScZ_9cA-6cWUPjfcGjNyg
- 《Claude 实现、Codex 审查、人类决策领航：Humanize 项目用 RLCR 编排长程闭环迭代任务》
- - https://mp.weixin.qq.com/s/qceRk9Qfq0Q3CTdD6P1Vag
- 《月烧6300刀才明白：Agent团队飞轮是怎么转起来的》
- - https://mp.weixin.qq.com/s/S45KRGmDCCLu5GoBa7v2bQ
- 《Humanize: —个 prompt 重构 GEM5的构建系统》
- - https://zhuanlan.zhihu.com/p/2011939681307206316
- 了解更多
- 加入了一下群公告，这样新进来的人也能看到
- @刘思皓好奇问一下humanize是否会有其他coding场景?
- 《让 Agent 自己优化 CUDA kernel，并在MLSys 2026 FlashInfer Full-Agent Track拿下前三》
- - https://mp.weixin.qq.com/s/xlOIr4y60dzyeOn_3toipA
- @刘思皓好奇问一下humanize是否会有其他coding场景?
- 啥时候上中文三大会
- 我目前还在个人测试阶段
- 这不是花钱就能上嘛？
- NV周耀阳:啥时候上中文三大会
- 其他coding是指？
- 1900:@刘思皓好奇问一下humanize是否会有其他
- coding场景?
- 应用开发

---

### 5月29日

#### 原文 L28715–L28835

[回到原文件 L28715](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:28715)

- 5月29日00:11
- 这家添加设备有个bug一直没修
- 开源芯片 agent flow 张宇鑫:
- 这是什么文档
- 开源芯片 agent flow 张宇鑫:
- 5月29日00:23
- 哪个地方
- Luke: 感觉.humanize/苦涩的教训里面写得也很过
- 时，很多什么round 7,round9都写进去了
- issue 186
- 让我写个 pr
- 5月29日00:31
- 还是整个流程中自发出现的
- 5月29日00:51
- @刘思皓你的codex limited了?
- week limit是没了
- 但是我还有credit
- 5月29日00:54
- 现在找不到了
- claude opus 4.8发布了？！
- https://www.anthropic.com/news/claude-opus-4-8
- https://cdn.sanity.io/files/4zrzovbb/website/c886650a2e96fc0925c805a1a7ca77314ccbf4a6.pdf
- 5月29日01:01
- MVP
- 有没有评价
- 提了
- 582%
- 915
- n.is
- Luke: 让我与个 pr
- pr 188
- an
- ma%
- 582%
- Opus 4.8's capabilities Opus 4.8
- 的功能
- dynamic workflow
- 有意思我玩一玩
- 新的倒牛奶
- cc好像没有
- 这就开始了？
- 6 月还没到啊
- 不差那两天
- 得了，h3想做的东西 hmm
- L.Zhu: dynamic workflow
- 又得想idea了
- 所以ultrawork是h2，dynamic workflow是h3吗?
- 5月29日01:06
- 你可以这么理解
- 显然我入职前的每一天都是在浪费时间
- sihao还有多久啊
- 光速来
- 2个月多一点
- 5月29日01:09
- 最怕的就是大家都太快了
- cc启动
- sihao还有多久啊
- 光速来
- 2个月多一点
- 5月29日01:09
- 最怕的就是大家都太快了
- h2其实就是想做强契约的静态工作流
- h3其实就是想做agent自动更新的动态工作流
- well 显然claude code都做了
- 这才是我熟悉的claude code
- 先实际用一下吧，看看它效果怎么样
- 只要你的harness是真的好用的，抄走的latency不应该超过3天
- 这个实现应该不依赖 A\ 远端吧
- 不依赖
- 刘思皓:只要你的harness是真的好用的，抄走的
- latency不应该超过3天
- 现在唯一的门槛我觉得只有前端了
- 因为vlm能力太差了
- 福尔高斯：一天就行了
- 前端反而不好做
- 这就显得claude code不抄 codex的 /goal这件事越发奇怪
- 已经超了吧
- 刘思皓: 这就显得claude code不抄 codex的 /goal这
- 件事越发奇怪
- 就是慢
- 我怀疑是人太多了
- 没抄好等于没抄
- 不它抄的那个效果很烂
- 我记得是实现不一样
- 毕竟都开源的
- goal应该是一个小模型做的判断
- 11
- AA
- Also-launching today
- 抄功能没抄实现
- 前端你vlm+cua呢
- 福尔高斯：现在唯一的门槛我觉得只有前端了
- 我觉得关键应该就在这里
- codex小模型的review也很强
- 没用
- Julian: 前端你vlm+cua呢
- 看训练了
- 刘思皓: codex小模型的review也很强
- 5月29日01:13
- 看起来是parallel do + verify?
- L.Zhu:
- 我觉得cursor的plan是最强的
- L.Zhu:
- 你啥场景啊
- ultrawork 是啥
- Joe布衣: 所以ultrawork是h2，dynamic workflow是
- h3吗?
- 看起来是的
- L.Zhu: 看起来是parallel do + verify?
- mrjaipn
- 是我要求低了还是

---

#### 原文 L29070–L29077

[回到原文件 L29070](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29070)

- 刘思皓:你可以直接说“XXX里面是我想的一个draft
- idea,帮我用humanize的gen-plan带superpowers...
- 5月29日08:16
- 感觉4.8 refactor能力都没有codex强，让他找refactor就找出一些无关紧要的代码重复，找不出abstraction层面上重构的
- Joe布衣: 那个dynamic workflow咋样？有人测评吗?
- outputs. A background subagent is implem
- plus byte-identical verification. Next:
- to o t   rg.

---

#### 原文 L29236–L29277

[回到原文件 L29236](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29236)

- Canaan:花里胡哨的动态
- 看来还是不能opus主力，只能可以尝试下workflow，让opus做日常的维护者
- 然后过了两周之后，就出现在了cc的mainline里
- 只能说明humanize社区走在了cc前面
- cc应该还看不见humanize
- 而且想idea是简单的
- 5月29日10:20
- 看来述是不能opus王力，只能可以会试下workflow，让opus做日常的维护者
- 虎：
- 你这就扯了
- 香港科技大学 研究助理教授 徐策羽: Humanize做啥，
- 做出有效的flow是困难的
- 我一天能造10个五省十部
- 少了
- 刘思皓:我一天能造10个五省十部
- 本群含金量太高了！
- 香港科技大学 研究助理教授 徐策羽: Humanize做啥，
- 然后过了两周之后，就出现在了cc的mainline里
- 必须立刻学习
- 5月29日10:30
- 必须立刻学习
- @刘思皓你有没有感觉长程任务的overhead太高导致adhd严重
- 确实
- 武汉心片科技刘玖阳: @刘思皓你有没有感觉长程任务
- 的overhead太高导致adhd严重
- 我上个月都不是很能睡好觉
- 长程workflow这件事
- 还是得持续迭代
- 请问这个有report或者论文吗？比较好奇其中的测试是边开发边用AI生成的么？
- 刘思皓: https://github.com/SihaoLiu/Lzvm 我正在
- 欣赏神迹
- 5月29日10:36
- prompt带tdd就好
- 美美与共: 请问这个有report或者论文吗？比较好奇其
- 中的测试是边开发边用AI生成的么？
- 它替你做决定了
- GYF: 我最近在用 codex /goal 时候发现它不怎么问我
- 问题
- 5.5 有时候不用goal他也能自己干好久，只要你说的东西是一个比较远的目标就行
- tdd这种就属于workflow里面的“工业味精”
- 5月29日10:38
- 加了就一下子好很多

---

#### 原文 L29406–L29419

[回到原文件 L29406](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29406)

- 那就是
- 我们在分析感觉KernelWiki本身也是用humanize爬的（
- crawl w/ humanize
- 直接/goal 帮我收集各个开源项目近六个月的blackwell相关PR
- deepsleep
- build for humanize
- 目瞪狗呆
- 5月29日11:59
- dongyun当我面敲的cmd
- 不用分析了，就是用humanize爬的
- 小乱:我们在分析感觉KernelWiki本身也是用
- humanize爬的（
- XS
- 哈哈哈

---

#### 原文 L29557–L29572

[回到原文件 L29557](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29557)

- 感觉不对头
- workflow 得有graph
- 你要的我都有😂
- Shom: workflow 得有graph
- 你点右上角的flow view
- workflow一定要有work
- 还是太超前了
- 我将全职研究humanize
- 但是这不对
- 我又进化了
- 我将全职研究humanize
- 我今晚折腾一下老板的经费
- 明天就开干h3

---

#### 原文 L29591–L29613

[回到原文件 L29591](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29591)

- 2. 你需要引入动态调整审查的力度和时机，不能从头到尾强review类似humanize1)，也不能弱review(类似
- goal)，需要控制judgement发生的时机
- 3. 你需要在两个地方引入渐进式的设计：渐进对齐(humanize2)和渐进规划(codex goal启发)
- - 产物中心
- 那感觉需要一个streaming reviewer去替你monitor并escalate—些问题
- - 动态judgement
- 5月29日12:36
- - 渐进对齐和计划
- ，如何理解产物中心呢
- AI EngineerK&Legora CTO
- 高带宽产物
- Humar, and agen's should collaborate in high-
- andwidth artifacts
- AGENTS 高带宽产物 THAN A CHAT
- 上下文感知
- 熵思录
- 还有两个好处
- 你可以上版本控制，有版本控制你就可以上沙盒和snapshot，就可以在系统层级超高并发
- 哦哦明白了，导入context->在context中工作
- 刘思皓:008风险：超越聊天的界面我们应该
- 在“高带宽的产物”中进行协作。这里的“产...

---

#### 原文 L29627–L29649

[回到原文件 L29627](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29627)

- “沟通导向任务动作”变成“我的任务是把产物A变成产物B”
- Xiaotao: 哦哦明白了，导入context -> 在context中工
- 合理，学习了
- 看起来这个产物导向需要专门的包装
- 然后agents之间完全不沟通
- agents只做一件事：经过我的产物得到了合理的“变换”
- 我不确定但上述思路是我理解的sota
- 明天落地实装一下humanize
- 5月29日12:45
- 磨两个月再launch又要被抢发
- &试点合作企业+1
- 对，我感觉最近（以及未来）做harness
- flow的人，其实有一个很明确的指标就
- 是：
- 你做的东西能不能在2-3个月内，被官
- 方推出一个内化的选项所覆盖
- 能:你做得不错，但是现在官方内化了，
- 你需要再官方的基础上继续改进
- 不能：你哪里做错了
- 没有被内化/取代的东西，我一律认为经
- 不起实践推敲

---

## 记录后段｜原文件只保留了相对日期

### 星期二

#### 原文 L29650–L29655

[回到原文件 L29650](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29650)

- 星期二11:50
- call back—下
- 不被官方内化的harness flow是没有存在意义的
- 真正的harness eval

---

## 5 月

### 5月29日（第 2 段）

#### 原文 L29699–L29726

[回到原文件 L29699](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29699)

- 5月29日14:43
- 这是Durable workflow 带checkponit的可会把任何skill转换为BPMN，你跑1000轮都是Reliable
- 你可以在跳转恢复任意一个node在llm
- https://asciinema.org/a/VFuGoKIWSwcBFpo4 你还可以看看这个，描述医疗业务场景的，慢是因content都得用
- ∥m生成flash应该会快很多
- 还是沙盒snapshot
- 5月29日14:48
- Qianji checkpoint
- = workflow可恢复/可审计/可重放 的执行状态记录
- 也就是：节点执行到哪里、输入是什么、输出artifact在哪里、用了什么模型/工具、策略是否通过、失败原因是什
- 么、下一步从哪里继续。
- ni wendae?
- 交互式的测试
- 带checkpoint是指什么？上下文?
- 还是每个节点都当一个git commit
- pi-wendao?
- 这仓库在哪
- 我去深度严肃学习一下
- 5月29日14:53
- resume envelope和snapshot是同一个level的
- https://github.com/tao3k/pi-wendao，都是durable workflow的特性
- https://github.com/tao3k/xiuxian-artisan-workshop这是主仓
- 0:26
- 5月29日14:58
- 我们正在尝试用org代替md，发挥agent记录content的威力
- 0:11
- 我们做的主要是高性能大规范的服务，pi-wendao这边就是单纯测试玩一玩

---

#### 原文 L29743–L29752

[回到原文件 L29743](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29743)

- 合理啊
- 然后我其实可以全局暂停存一个snapshot
- durable workflow的核心原则是：
- running instance binds to immutable workflow definition revision
- 然后在新flow resume?
- 这对于llm是必须的，Ilm天然发散性
- 是的，你可以分支任何
- 旧 flow 全局暂停 → 生成 quiescent snapshot → 新 BPMN revision / new flow import snapshot → fork/resume
- woc你这项目做半年了

---

#### 原文 L29756–L29785

[回到原文件 L29756](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29756)

- 有啥具体的case吗
- 比如说用这个workflow跑出来的项目
- 5月29日15:08
- 这要什么具体case，BPMN 2.0这和模型就是被业务，业界验证过的
- 差距在于2026年谁做的agent first，因为object变了。
- 我知道流程肯定是通的
- 我想看看有没有具体案例
- 我看你似乎理解又偏差，BPMN是工业街的workflow，且被验证多年https://camunda.com/也在寻求agent AI转
- 型自己的workflow engine。就对于垂直行业来说一个跟agent+bpmn workflow的交互运行被验证的目前还没有。
- 5月29日15:13
- BPMN 是啥
- 而在agent coding的workflow里面这几个月大家都在尝试durable workflow的实现，但workflow本身的模型，其
- 实大多是简单的DAG petgraph
- BPMN 就是 workflow 的标准格式
- 只是现在 coding 还没进化到那么复杂
- 走到尽头就进入BPMN了
- bpmn那个部分我是理解了，我其实只是想问agent + bpmn workflow这个组合是否有跑通的github repo项目
- GuangTao:我看你似乎理解又偏差，BPMN是工业街
- 的workflow，且被验证多年https://camunda.com/...
- 我们不就跑通了吗？
- 而且我们coding agent也有自己不同的理解和实现。我们后期会提供各种loop 和flow 机制类似 https://
- ralphworkflow.com/我们有更加友好的窗口
- 其实我就是想问有没有用这个工具来实现一个项目。就比方说，我造了工具A，用工具A，做了一个项目B。你的这个
- A我理解了，也觉得合理，我想看看有没有现成的B
- GuangTao: https://github.com/tao3k/xiuxian-
- artisan-workshop...
- 项目。就比方说，我造了工具A，用工具A，做了一个...
- 5月29日15:19
- 各种还在开发，并没有提供给社区一个完整的用户版本，所以暂时也无法让你们复现

---

#### 原文 L29978–L29994

[回到原文件 L29978](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:29978)

- 我的错，我问的可以再直接一点：
- -我，造了Humanize，大家用humanize做了【一系列群公告可以看的公开案例】
- -你，造了Wendao/Xiuxian，有没有【?】
- 从做产品的角度没错。我们不是在想有没有办法解决在1900年knowledgecutoff的时候去解决个广义相对论问题
- 嘛，需要一个initial bootstrap prompt，就去试图从引力不是力，是时空的几何往外推。
- 理论上说，每一个“东西”，都可以拆成一些principles、observations、research method，这些正交的维度，然
- 后剩下是trivial的“推理”。如果我们能把所有已有的知识拆开，然后再去检索，这个好像是我理解的“taste”。不
- 知道有没有人在做这个方向
- 可以拿humanize创造的东西参加黑客松了
- 5月29日15:53
- GuangTao:我们正在给垂直的一个医疗康养做对接
- 有无demo的意思
- 还是说并不存在公开可看的【？】
- 可以拿humanize创造的东西参加黑客松了
- 5月29日15:53
- 不太懂你什么意思，能公开的都公开了，都是贡献社区互相学习的。整个流程的dmeo对于企业的我们预计下个月中

---

#### 原文 L30128–L30138

[回到原文件 L30128](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:30128)

- 我没太get到什么是harness infra啊
- 就是支撑 Harness 的底层基础设施，比如 workflow 层的基础设施，或者 memory/knowledge层的基础设施
- 应该立刻能做吧。agent A从高引用 paper 里面抽取出 背景、问题等等 spec，agent B禁止 web search，只读 spec
- 张东宇: 我觉得这个idea有一个退阶的成果 给定一个
- 限时知识训练出的AI，我们给它未来几年某些经典pa..
- 但你没法保证 agent B训练用的数据里没有泄漏啊
- Reiko: 应该立刻能做吧。agent A从高引用 paper里
- 面抽取出 背景、问题等等 spec，agent B禁止 web ...
- 限定模型发布后的 paper
- 那选择范围有点窄了

---

#### 原文 L30144–L30154

[回到原文件 L30144](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:30144)

- 但这个能力越强越好，我觉得严肃软件开发更需要这样的模型能力
- 我有一个模糊的感觉，未来 human-agent-agent-human 通信，paper是高质量的通信协议。
- 今天开蹬ultracode + workflow
- 让Claude自己去找是不是能写出符合我期望的dsl或者transpiler
- 如果论文的主要读者不再是人- 董彬的文章- 知乎
- https://zhuanlan.zhihu.com/p/2040070769791787736这个我比较赞同
- Reiko: 我有一个模糊的感觉，未来 human-agent-
- agent-human通信，paper 是高质量的通信协议。
- 哎哟卧槽，这玩意儿好啊
- Reiko:如果论文的主要读者不再是人- 董彬的文章-

---

#### 原文 L30235–L30249

[回到原文件 L30235](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:30235)

- aopt这个实验证明了只要能描述清楚
- agent就能做好实验
- 现在觉得，要是不把它训练到基座模型里，这事就是无解的
- 5月29日17:44
- 做好实验和做一个可完全复现的实验是两码事
- 张子健: agent就能做好实验
- 我们工厂环境也是一样的困境
- 未必啊
- 碰到这种东西，以前以为能用RAG，image embedding来识别，再in-context learning
- 对人对 agent 都是一样
- 比如这个直径半米的大铁盘子，是反应釜的过滤器，VLM去哪认识这玩意儿
- 5月29日17:51
- 你这个问题和我描述的问题已经是不同领域了，你这个是已经给agent界定了范围，但我这个故事里是没有范围的。
- 来了个新牛马研究生，尝试把关二爷像摆在实验室某方位，做实验前先三只清香拜一拜，VLM怎么记录？
- 虽然我这个故事是扯淡的，但实际场景下面对的输入都是不确定的，不管是实验步骤还是实验器械，材料，批次，封

---

#### 原文 L30307–L30318

[回到原文件 L30307](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:30307)

- 5月29日23:31
- 从我拿到cloud code的第一天起，我就都是dangerous permission
- dangerous permission怎么会停下来要权限?
- 估计是哪里mix进去了AskUserQuestion
- 被手动触发了一下
- 5月29日23:44
- 不是要权限，是问我要不要启动任务
- 确实是触发了ask user question
- 我这边解决方法是必要的时候直接把ask user question这个skill直接卸载了防止他问我
- 这现象确实很常见，一觉醒来发现他罢工了，特别是humanize启动阶段
- xs 这样就很麻烦了
- dongyun:我这边解决方法是必要的时候直接把ask

---

### 5月30日（第 2 段）

#### 原文 L30350–L30362

[回到原文件 L30350](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:30350)

- 目前的dynamic workflow和humanize是兼容的吗 是否相当于在cc原生workflow之后加一层codex review
- 5月30日02:47
- 不会兼容我在做h3
- dynamic workflow出来之后，h2其实没有很大的存在必要
- 你其实可以直接走dynamic workflows在某个节点用js加—个codex-rescue/codex-review
- 按这个发展速度，cc内部的h3应该已经在试验中的
- dynamic workflow跑在沙箱里
- 很难调codex吧
- 不是humanize的ask-codex
- 5月30日02:54
- 哇 antigravity, antigravity-cli, gemini-cli

---

#### 原文 L30751–L30786

[回到原文件 L30751](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:30751)

- (对于单一项目来说)
- 一个agent猛猛干一天能500刀左右
- 黑岩: 能划分好结构然后让一群 agent 有效干活?
- 那感觉 agent to agent 的信息交流是不可避免的呀
- 我总感觉这一环会引入很多错误
- 你去看bun的workflow
- 5月30日12:27
- 都是输出结构化信息
- api token不经烧的
- bun
- Shom: 你去看bun的workflow
- 的那个workflow才是正解
- 我的刀盾
- 刘思皓: https://github.com/SihaoLiu/rem6
- 实战验证过的
- 之前ccc那个说用agents team搞的东西把我坑惨了
- 边摸鱼边手动鞭策着烧，一天最多少100刀，正儿八经干一天300刀不够
- 如果是确定性问题，循环烧一天1000刀打底，并行无上限
- 确实
- claude的设计理念还是很好的
- 碰瓷的没一个比得上
- 还有个写jsx表示工作流的妈呀
- 现在有ultracode了，我摸鱼烧一天也能烧到1k usd
- 明扬：边摸鱼边手动鞭策着烧，一天最多少100刀，正
- 儿八经干—天300刀不够
- codex并发上限64我拉满了发现token请求特别慢,远不如拉64个codex
- burn tokena做事本身就就是非常愚蠢的行为，要比谁烧token更高一个ω。
- 5月30日12:48

---

#### 原文 L30825–L30837

[回到原文件 L30825](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:30825)

- 然后再看一下怎么修
- 这个文档是humanize爬下来的吗
- 是，我感觉多多少少还是有点问题
- 张东宇: 这个文档是humanize爬下来的吗
- 尤其是多方向并行探索，和代码库审计，文档一致性检查等等
- 还是得多试，多烧，才能直到目前工具的能力边界在什么地方
- 5月30日13:01
- review代码干的好一些?
- 明扬:我目前正好有适合ultracode做的几个任务
- emmm ok，我也在做类似的事情吧，我现在看到的是不做 compiled simulator 情况下，做了partation 并行度很
- 快也会饱和，大概十几个核就几乎没收益了吧，主要是不做 compile，memorylayout transformation 和 event
- fuse 的收益完全拿不到，现在 arch 仿真 其实 event 激活稀疏度没有那么高，event skipping 这种思路性能很难做
- 上去

---

#### 原文 L30857–L30882

[回到原文件 L30857](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:30857)

- 刘思皓: 然后这恰好是一个寻找better kernel
- 这俩项目都是humanize一波gen-plan，然后直接上codex/goal
- 中间完全无人干预
- 感觉会陷入循环
- 刘思皓：我非常好奇对这种又大又长的任务，当你的
- token是无限的时候，给足自由度它能实现到什么程度
- 毕竟上下文还是有上限的
- 5月30日14:08
- 你看一下commitlogs，它并没有陷入循环
- 但是它多多少少还是存在一些问题，我已经观察到不少其他的问题了
- 但我打算先跑到它停机为止
- 现在都不用 humanize rlcr 而是直接/goal 了吗
- 是不是会像围棋一样，因为搜索空间太大了，如果没有前面的价值评估网络，后面这个问题无法收敛
- humanize rlcr并不是为这种场景设计的
- .:现在都不用 humanize rlcr 而是直接/goal 了吗
- humanize rlcr要求你有一个“全知”的输入plan
- Alpha go 围棋的RL进化故事是怎么样来着
- 明扬：是不是会像围棋一样，因为搜索空间太大了，如
- 比较麻烦的可能是目标不明确，没有一个 formalize的判断目标或者说一套带有随机性防止 hacking的 harness
- benchmark，如果能实现把goal形式化描述后可计算执行判别，那二代图灵机可能就出现了
- humanize rlcr希望你的输入plan只是一个对代码的自然语言的压缩，它已经包含了全部设计信息
- 不会，我已经触发goal achieved很多次了
- 明扬:是不是会像围棋一样，因为搜索空间太大了，如

---

#### 原文 L31037–L31056

[回到原文件 L31037](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:31037)

- 5月30日20:06
- 话说你们怎么解决 codex 打 patch一直导致代码堆积的问题
- 如果人和他co-work的话还好，大的architecture，一般可以给个方向，refactor
- 如果你让他humanize跑三天，出来一堆屎，你又不知道是啥。那就没招了
- 般我发现codex如果觉得code有问题，那个问题一般都是正确的。只是有时候他打patch的方式，有些无语
- 所以build得换个模型?
- 绝对不能盲跑三天
- FanLong:如果你让他humanize跑三天，出来一堆
- 屎，你又不知道是啥。那就没招了
- codex 喜欢做local fix, 迭代几次后可以让它做局部范围的 refactor
- 屎拉的太多模型也分不清
- 人也没看过
- 然后这东西就没有人知道是什么了.….…..
- 我几次长程任务的惨痛经验
- 开始跑的不错屎堆高了就不好使了
- 5月30日20:24
- 该堆会堆的，这个人不介入防不住
- codex的 prompt 里面会不会有一堆兼容性的要求，有人看过吗？这是模型自身的问题还是 agent 设计的问题
- 5月30日20:29
- 如果一个project要搞得长，大的component切割还是得人来。要不然不太行

---

#### 原文 L31083–L31097

[回到原文件 L31083](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:31083)

- 这个就是追问部分的实现，效果很好
- 刘思皓: Agent 时代，Human 不能只做许愿
- 刷只让 Agent 旺：
- 复杂系统最终
- 的人
- 还得让人能接手
- 5月30日23:37
- 文档一定要适合人类阅读的文档
- 现在不说人话真服了。
- 对于agent生成的文档到人类阅读，最适合的合适html这种渲染过有可视化效果的。但raw html xml这种显然第一时
- 间肯定不适合人类阅读，但从一开始生成html这种对agent来说标签语法太冗余长期下来也不是好事，人类也第一时
- 间无法阅读html等产出的信息
- Luke: 文档一定要适合人类阅读的文档
- 这个我观测到一个现象，就是如果你不加任何限制，claude和gpt做文档的风格不一样。
- 那太不一样了

---

### 5月31日

#### 原文 L31167–L31189

[回到原文件 L31167](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:31167)

- 5月31日00:01
- 我倒不是很喜欢c家原生workflow
- 翁大爷的狗@Rakuten:我感觉我听到的好评主要来自
- workflow
- 15%幻觉 这种该提升模型能力了wor水flow能拯救吗，当不是大弗功夫
- 15%幻觉这种该提升模型能力了workflow能拯救吗。岂不是大费功夫
- GuangTao: 你也不想你的plan有30个tasks跑了2个
- 小时，其实15%幻觉给DONE了，还有部分偏移了。...
- 翁大爷的狗@Rakuten: GPT是那种，一句话正着说一
- 次，反着说一次
- 15%在多轮长任务的子任务我都说少了，具体你可以看4月后的benchmark。其实很多人压根没有plan的划分把子任
- 务没有集合划分到颗粒度很小所以看不出来。是模型内容膨胀后带来的劣势，就最强的模型30%膨胀就会出现问题，
- 这个是有很多论文的benchmark支撑的不止一家做了
- 饽饽博: 15%幻觉 这种该提升模型能力了workflow能
- 拯救吗。岂不是大费功夫
- 5月31日00:08
- 这个我可以给一个例子，我之前 workflow 设计的不好(subagent 和 main agent 没有分离)，gpt 5.4 写出来的验证
- 文件，10-20% 有 reward hacking
- 饽饽博: 15%幻觉 这种该提升模型能力了workflow能
- 区不同我使用原生语法解析不是基于tree-sitter，目前正在测试rust的公共大库，效果非常好。大幅降低codex/
- claude在编写代码时候遍历code的行为。只需要SKILL.md+hooks机制。目前可以学习下我的plan思想

---

#### 原文 L31194–L31276

[回到原文件 L31194](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:31194)

- 码搜索器和基于org的plan生成追踪TODO、DONE...
- workflow还有一个主要问题是reproducible，你做的好的workflow是可以分享和持续使用的，而且如果有相似的任
- 务只需要需要node。对于token节省还是非棒的
- 5月31日00:14
- 我们在 Humanize上基本处于“一边磨刀，一边割麦子”的
- feature 的可用性和效果。
- https://github.com/tao3k/wendao-episteme/tree/main/sources https://github.com/tao3k/qianji-flowhub/
- blob/main/wendao/client/plan/PLAN_POLICY.org 这块还没弄完。但是文档的结构的最佳实战可以看看
- epsiteme，非常强的设计
- 刘思皓:对啊，有没有最佳实践的demo
- 5月31日00:19
- 你误会了，我们想看的不是“磨刀”，我们想看的是“割麦”
- 没有人一上来就claim自己的工作流/基础设施/方法论是“非常强”，“最优设计”的。
- 对，主要是割麦的效果。因为方法论实在太多了，我们迄今为
- 感兴趣的是在实际的项目当中能达到怎样一个效果，如果还有
- 5月31日00:27
- 关于什么是*例证*，https://github.com/gem5/gem5/pull/2969，这就是一个例证，这是5个月前的humanize，
- 在8小时的时间内完成了对gem5整个仓库的全栈构建系统的替换，达到了byte-identical的效果，并且有社区第三方
- 实证。
- 你需要证明你的方法论/工作流/基础设施，在一个第三方项目里面有实际的效果才可以，哪怕不是开源的都可以。
- 没有*例证*的flow是站不住脚的
- 需要图和表
- 不能只文字写 method
- gem5/gem5/pull/2969，这就是一个例证，这是5...
- 请问下这个不是做文档结构parse吗？和md/html的争论的关系是
- GuangTao:至少在社区为用md还是html抄的时候，我
- 目前找到了最优解https://github.com/tao3k/orgiz...
- 5月31日00:47
- 你的这个例子思维太有意思了，行把就当我没说过。我说的最优解对于仅仅是对于我来说，我分享的讨论的很多也是
- 技术实现的根本原理上面的讨论
- 刘思皓:关于什么是*例证*，https://github.com/
- gem5/gem5/pull/2969，这就是一个例证，这是5...
- 5月31日00:48
- Reiko: 这个我可以给一个例子，我之前 workflow 设计
- 的不好(subagent 和 main agent 没有分离)，gpt 5....
- 对于agent生成的文档到人类阅读，最适合的人类阅读是html这种渲染过有可视化效果的。但raw html xml这种显然
- 第一时间肯定不适合人类阅读，但从一开始生成html这种对agent来说标签语法太冗余长期下来也不是好事，人类也
- 第一时间无法阅读理解html等产出的信息。org是解决md里面agent产生的信息不足，但它又有非常好的metadata
- 人直接就可以纯文本第一时间阅读。核心观点在这里
- 饽饽博:请问下这个不是做文档结构parse吗？和md/
- html的争论的关系是
- 5月31日00:54
- soga！补习一下上下文
- 5月31日01:00
- agent长期下来会堆积非常多的内容，信息。对这些信息重复利用解析，甚至训练查询都成了刚需。orgize就是对这
- 方面的尝试，你像codex等实现的memeory还是纯md记录，内部再实现了一套时间，类MemRL机制等，grep多重
- 机制来hit的这个MEMEORY.md文件。org尝试就是在记录的时候时间关联性一切都被记录等。对应memeory实现也
- 我基于Q-table实现的memory和4个月2000个org的堆积测试，效果还是不错的。至于和codex的机制来对比我没测
- 试过太烧token了。
- 5月31日01:05
- 能说一个量化的数字来证明你说的“效果还是不错”吗？
- 以及是和什么比的
- 大概理解了，不过我比较感兴趣几个问题：
- 1. agent 能不能长时间稳定地产生干净的 Org，而不是越写
- 2.旧 memory 如何压缩、归档、去重、失效。
- 是一种优化
- 饽饽博: soga!补习一下上下文
- 2. I旧 memory 如何压缩、归档、去重、失效。
- 3. 查询是不是比 grep/embedding 真正更准，比如“找出
- index 是否能稳定回答。
- 5月31日01:12
- 我是长期的codex用户，是跟codex比的，大概信息膨胀到40-50%主要看memoryhit的对相关信息的成功率召回
- 率。典型就是就纠正codex一些复杂功能的用法，明确告诉它这这件事情的正确方法。我从2000个orgfiles去测试的
- 刘思皓：能说一个量化的数字来证明你说的“效果还是
- 不错”吗?
- 我可以明确告诉你grep+ subagent+ reaasoing tree渐进式披露的让llm合并结果非常棒。rg fd 这类工具要综合
- subagent + index query使用精准度非常高
- 泽文:大概理解了，不过我比较感兴趣几个问题：1.
- agent能不能长时间稳定地产生干净的Org，而不是...
- 大范围embedding目前我是明确拒绝的，效果不好而且成本高昂。grep fd rg依l旧对于agent来说首选，在大规模测
- 试3月后的论文已经多方支撑。我在搜索这块也是多的hybrid subagent的方式。就目前分享的orgize只是从agent记
- codex和大多数的做法，对于压缩，它的做法就是将一些经验，学习总结成了1-2句话，这个很有用但上下午关联具
- 体它如何做的我也不清楚。它也在使用hybrid agent做记忆搜搜尤其是grep非常频繁。去重失效这块就是Qtable发
- 挥的地方了，主要在于对时间戳，last modified关联的文件的改动情况记录，还有完成事件的DONE掉的权重评分
- interesting。现在有很多做agent mem database的方案有对比过吗
- 有我做了很多，但是跟他们的benchmark具体pull下来做对比测试还没有但是原理实现方面我都做了分析研究报告。
- 我的测试集跟他们的测试集没有对比过，目前为止。精力有限，mflow算是有些创新的
- 5月31日01:21
- > 2.旧 memory如何压缩、归档、去重、失效。
- 求看分析研究报告。
- GuangTao:有我做了很多，但是跟他们的benchmark
- 具体pull下来做对比测试还没有但是原理实现方面我...
- 5月31日01:32

---

#### 原文 L31303–L31337

[回到原文件 L31303](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:31303)

- org-mode作为一个开发23年的开源项目，它本身elisp扩展又强，我很多功能还没支持，但目前足够好用让你研究
- 了。你可以看看看3月后的相关的记忆论文，基于org让你的实现很大幅减少，直接关注算法本身。
- 饽饽博:现在各项接口已经成熟了吗可以试用吗。当然
- 我的试用报告也会开源
- 天真地让claude code自己做review loop，结果第二轮review他总是指示reviewer“第一轮review修复了这些，看
- 修复没”，然后两轮就结束loop
- 5月31日03:46
- builder-reviewerloop有很多实现上的坑
- 我之前踩过的坑在SihaoLiu/gaac项目里面
- https://blog.csdn.net/fyfugoyfa/article/details/161168128
- 社区有个我不认识的哥们写了个AI软文，其中cover了一些GAAC时代的问题，里面包含了这个问题，可以参考一下
- 北田圭人: 天真地让claude code自己做review loop，
- 结果第二轮review他总是指示reviewer“第一轮revi...
- 类似的问题还有“multi-agents as review committee”，最后也是doesn't work
- https://multi-agent.wiki/我要说白了
- 这个好用吗
- 00
- 5月31日03:59
- 你这个做的真不错说实话
- 福尔高斯:https://multi-agent.wiki/我要说白了
- 之前 research的内容都打进去了
- 谢谢好评
- 谢谢好评
- 刘思皓：你这个做的真不错说实话
- 准备再深度体验一下几家的 Multi agent 产品 给调研报告加进去
- 我觉得Multi agent的价值还没有被市场发现
- https://docs.google.com/document/d/1Vi2thlhowMYVN4HG6KOHVQDlzrDtnIE0
- 首先要思考的是multi agent的目的是什么
- 你那个分类体系里面“分类体系/Taxonomy”
- 里面可以加入一下 Q36 里面那个分类
- 刘思皓: https://docs.google.com/document/d/
- 1Vi2thlhowMYVN4HG6KOHVQDlzrDtnIE0
- Xinming Tu: 首先要思考的是multi agent的目的是什
- 很多人还是喜欢假借人力

---

#### 原文 L31344–L31388

[回到原文件 L31344](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:31344)

- 5月31日04:06
- https://multi-agent.wiki/patterns/voting-ensemble
- https://multi-agent.wiki/patterns/market-auction-contract-net
- 以及我感觉这样分类是不是有点重复
- 我感觉投票器是拍卖加了个验证？
- 你这东西搞得真不错，让我加入群公告广播一下：）
- 福尔高斯:https://multi-agent.wiki/我要说白了
- - 带偏话题的情况会提醒一次，连续两次带偏话题会被移除。
- - 想要发布招聘信息请直接联系群主。
- 项目：https://github.com/PolyArch/humanize
- Token监控: https://github.com/SihaoLiu/ai-usage
- Multi-Agent Wiki: https://multi-agent.wiki/ by Holegots
- Humanize Slides
- - Humanize1: https://drive.google.com/file/d/1bvQI_IE1JyXqW6NkSMFPrs_G0erAdgca/view?usp=sharing
- - Humanize2: https://drive.google.com/file/d/1j-Xxtwf5GQ5PYcJ8GInd6XOKNuizUNbl/view?usp=sharing
- - Humanize — past, present, and future from Ligeng@Nvidia
- [文件] Advancing Token Productivity w: Agent Loops.pdf
- 《Humanize带来的Codex使用范式变化，解锁 Agent 优化 kernel 上限》
- - https://mp.weixin.qq.com/s/pScZ_9cA-6cWUPjfcGjNyg
- 《Claude 实现、Codex 审查、人类决策领航：Humanize 项目用 RLCR 编排长程闭环迭代任务》
- - https://mp.weixin.qq.com/s/6uzb0OFDCDt4xmRcWaelaw
- 《让 Agent自己优化 CUDA kernel,并在MLSys 2026 FlashInfer Full-Agent Track拿下前三》
- - https://mp.weixin.qq.com/s/xlOlr4y60dzyeOn_3toipA
- 《月烧6300刀才明白：Agent 团队飞轮是怎么转起来的》
- - https://mp.weixin.qq.com/s/S45KRGmDCCLu5GoBa7v2bQ
- 《Humanize: —个 prompt 重构 GEM5的构建系统》
- - https://zhuanlan.zhihu.com/p/2011939681307206316
- 了解更多
- 5月31日04:10
- https://multi-agent.wiki/workflows/orchestration-primitives
- 你这个编排原语是你自己想的还是哪里炼化的？
- 刘思皓：我感觉投票器是拍卖加了个验证？
- @刘思皓I am very happy with omp. I tried out since you recommended it for some non trivial task in low
- lve  sn ro s r s  o   s s  s  s en
- more effectively? My workflow was basically to work a lot on /plan interactively with it and than after each
- round redesign/design from scratch next plan. I feel there are maybe even better ways to use it effective.
- 从CC炼化的
- 刘思皓: 你这个编排原语是你自己想的还是哪里炼化
- 的?
- 今天刚增加
- 我看了一下没啥大问题就更新了
- nope, i am also new to omp. will refer @泽文 on this. he uses a lot
- Simon: @刘思皓I am very happy with omp. I tried
- out since you recommended it for some non trivi...
- 准备明天再逆向一波看看

---

#### 原文 L31413–L31423

[回到原文件 L31413](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:31413)

- subagent里面研究重点其实durable，fork resume都是durable层面的。workflow是走的图的，petgraph。近期
- openai claude做的比较有技术一点就输，就是对session部分做snapshot，原理就是模型在信息膨胀的时候30%的
- 时候会发生漂移，那么他们的技术方式原理就是，会在llm读取项目阅读这个action后的session节点做snapshot，然
- 后fork 到subagent去完成任条，multi-agent共享上下文，和控制上下文做节点fork 是当前的研究重点
- vs 嵌套群聊
- 大家对于实现总有其他变种
- 后面会统计一下不同的产品和类型丢进去做一个双向连接
- https://multi-agent.wiki/workflows/orchestration-primitives
- 5月31日04:18
- Verifier / Adversarial Review

---

#### 原文 L31466–L31483

[回到原文件 L31466](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:31466)

- 我理解两个是一个东西
- 控制权和 context
- 刘思皓: router vs dispatcher 你的理解是什么
- 我觉得所有 multi agent 本质都是对 context 的管理所以 context 管理形式变化就值得增加一种
- 不过里面很多类型也是agent搜集整理的我之前甚至都没想到过
- session context是核心，但状态也是。
- 福尔高斯：我觉得所有 multi agent 本质都是对
- context的管理所以 context 管理形式变化就值...
- 我感觉你这个wiki可以重构一下组织结构：
- 1. 基本结构(分支嵌套循环)
- 2. + 上下文/控制 (fork/subagent)
- 3. + 分配实际角色(builder/reviewer)
- 5月31日04:29
- 很好的建议我明天研究一下能不能调整得和chatgpt 老师好好聊聊再学习一下
- 感觉现在有点分类不清，有些topic覆盖了很多层级
- https://ralphworkflow.com/这块前期我推进你阅读一下实现，值得你学习。
- 福尔高斯：很好的建议我明天研究一下能不能调整
- 得和chatgpt 老师好好聊聊再学习一下

---

#### 原文 L31535–L31545

[回到原文件 L31535](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:31535)

- 我这个研究任务，4.8执行效果一般，但4.6可能也一般，因为以前没走到这个深度
- 有意思的是，脱离代码上下文聊天，反而比cc带着代码上下文给我展开了更多方向
- 带着 code context 约束太大了
- 明扬:有意思的是，脱离代码上下文聊天，反而比cc带
- 着代码上下文给我展开了更多方向
- 讨论架构之类的大方向，不带着代码会好很多
- 我怀疑cc带着code base的时候反而会限制自己的发散思维，抑制幻觉
- 是的
- 这个跟ctxlimit关系还不大，因为纯聊天的上下文也压了两次
- 5月31日08:01
- 但纯聊天会给我这样的幼稚推论，局部当作整体，但实际编码验证也不是那么容易……….

---

#### 原文 L31549–L31562

[回到原文件 L31549](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:31549)

- 不会思考更优的整体设计
- 但我明显感觉它执行定向有界的探索任务表现更好
- cc总是比cx多外推一些，cx会停在探索任务的目标边界，cc总是能继续延伸1-2步，且经常这1-2步是有用的
- ultracode
- 5月31日08:06
- 确实，要不然他都把之前失败的尝试了还老是想着在之前失败的尝试上继续改
- 明扬:有意思的是，脱离代码上下文聊天，反而比cc带
- 着代码上下文给我展开了更多方向
- 我也会特意删去引用上下文的输入，或者禁止它explore codebase。cc的训练task肯定有codebase优先级最高这一条
- 5月31日08:19
- 昨天群里信息密度好高。我也要努力学习，带脑子用token，产出高质量知识回馈皆様
- 现在服务器上离线运行多个agent且支持在线分pane监视，有没有比tmux更优雅的方案呢
- 之前用过zellij但和cx的兼容有点问题

---

## 6 月

### 6月1日

#### 原文 L32036–L32052

[回到原文件 L32036](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32036)

- 这是个值得用证据说话的对比题，正好两个具体担
- "workflow",我用一个 workflow 并行去四个方向
- 四路并行取证：①自研 workflow 复杂度实测②M
- 给什么/缺什么，然后综合出净收益判断。
- Workflow(Verify net benefit of adopting MAF
- Running in background· /workflows to mo
- 已启动后台 workflow(4 路并行取证→ 综合)。
- 没聊两句 workflow还自动触发了
- 6月1日12:29
- 你的prompt带有workflow关键字就会触发
- 那个workflow还会变成彩色的
- 6月1日12:41
- 行啊一个workflow跑完 5小时增加了3%
- workflow
- 彩色？没注意到
- 6月1日13:33

---

#### 原文 L32111–L32120

[回到原文件 L32111](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32111)

- Ron Minsky discusses Jane Street's approach to Al adoption throughout their SDLC at Bug Bash 2026.
- Ron stakes out their position that Al workflows should maximize human effectiveness and understanding
- rather than replacing humans entirely. At Jane Street, many traditional (aka pre-Claude) software
- engineering practices have become more important rather than less. Type systems help provide fast
- feedback and enforce invariants that agents can understand. Expect tests allow developers to see system
- behavior and create deterministic simulations at the library level. Code review remains crucial for
- maintaining code quality and human understanding, even though agents change the dynamics. Finally, he
- touches on Jane Street' s growing interest in formal verification, and the impact of agents making
- previously expensive approaches, like formal methods, more practical.
- https://www.youtube.com/watch?v=rUYP4C29yCw&t=57s

---

#### 原文 L32133–L32146

[回到原文件 L32133](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32133)

- https://arxiv.org/abs/2605.03822
- https://github.com/tao3k/agent-semantic-languages-server 我就解决啊
- 6月1日16:56
- 不要让 agent 给所有函数写证明。应该让 harness根据 parser facts和 risk facts触发 proof obligation。我目前4
- 个语言学了nativeparser，在julia引入了CataLab做验证，其次还提添加了很多实用的功能，用sagent-ematic-
- hook block了codex的Read Explore的机制，完全让agent从Rust library/owner boundary graph frointier去搜
- 明扬: 看来大家都想解决这个问题
- tnx!!
- GuangTao: https://arxiv.org/abs/2605.03822
- 你像我写二rust.agent_policy 已经覆盖了primitive semantic id、多个 flag参数、primitive semantic fields、
- anonymous primitive tuple、primitive type alias、stringly state 等public APl / data shape 问题。https://
- github.com/tao3k/rust-lang-project-harness/blob/e8dae1f7428ed3b45e9993ac90367c61345e3bd9/docs/
- 03_features/204_verification_policy.md
- 6月1日17:02

---

### 6月2日（第 2 段）

#### 原文 L32220–L32345

[回到原文件 L32220](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32220)

- 6月2日07:08
- ClaudeDevs
- X.com
- @ClaudeDevs
- 由Grok 翻译自英语
- 我们已为 Pro和Max 计划的所有用户重置了 5 小时和
- 每周速率限制。
- 我们修复了一个问题，该问题导致某些 Claude Code
- 会话生成过多的并行子代理，从而导致使用量比预期
- 更快地耗尽。
- 评价此翻泽：
- 01:35·2026/6/2·1.1万次查看
- 21
- Q92
- t7 107
- 22
- 相关
- 查看引用>
- ClaudeDevs@ClaudeDevs·12分钟
- 醋译自英语 显示原文
- 这个问题影响了Opus4.8请求的处理方式，导致模
- 型触发了比预期更多的并行工具调用。它与动态工
- 作流无关。
- Q2
- t22
- 5483口
- 6月2日08:06
- https://github.com/PolyArch/oh-my-humanize
- 我盲猜一手，这个feature会在3-6周内出现在cc/cx的mainline里面
- 晚一点我把slides发在群公告
- 我已经全面转向oh-my-pi
- codex总共香了一个月
- codex总共香了一个月
- 类似dynamic workflow?
- 刘思皓: https://github.com/PolyArch/oh-my-
- humanize---拿omp搭了一个我心中的h3，核心设...
- 让我试试 ohp
- dynamic workflow其实是h2
- 洋洋阳: 类似dynamic workflow?
- omp是完全剥离了cx吗
- dynamic workflow并不是dynamic的，工作流本身是静态的
- omp都能用
- omp什么都能用
- 那之前理解有误，dynamic workflow就是之前的ultrawork
- 刘思皓: dynamic workflow并不是dynamic的，工作
- 流本身是静态的
- 流本身是静态的
- h3(oh-my-humanize)的核心增量特性是：允许agent改动正在运行中的工作流
- Joe布衣: 那之前理解有误，dynamic workflow就是之
- 前的ultrawork
- dynamic workflow的意思是：我拿js固化一个流程，跑在上面的agents是动态的
- 那你这个workflow可以复现吗？
- 流程是静态的
- 复现什么？
- Joe布衣: 那你这个workflow可以复现吗?
- 静态流通过js脚本可以实现复现过程
- 哦这个我是做了的
- 动态流其实只是多个静态流在时间轴上有一些不同
- 学习一手
- 我将立刻学习！
- 我感觉这个feature实现起来用omp做很简单
- h3是不是可以做成一个omp的plugin呢？fork好像可维护性不太好
- 但关键点是：不知道设计一个什么样的agent去改flow是真正有效的
- 这个还需要大规模去尝试
- 我打算后面work了，直接upstream
- catslashbin: h3是不是可以做成一个omp的plugin
- 呢？fork好像可维护性不太好
- 遵守一个开源精神
- 有个小疑问啥场景需要修改运行中的workflow怎么验证多agent交互带来的收益>管理成本
- 二个和尚抬水喝三个和尚没水喝
- 1.在项目开始前需要大规模探索，就需要并行点子生产机--参考humanize的parallel gen-idea
- 2. 项目初期，由于工作耦合度低，需要并行Builder，弱reviewer --参考/goal
- 3. 项目后期，需要强reviewer --参考原版 humanize
- 比如某个子问题本身很复杂/成本很高，不可能短时间低成本的完全达成，那么什么程度的达成是可以接受的，这个程
- 度的边界也需要写回到rfcs/spec里去
- B4RRy:解决问题本质上是找一族问题的等价表示把?
- 比如原始问题-> 原始问题等价表示1 -> 原始问题等...
- 在不同阶段下，流程不一样，h2(以及现在workflow/ultrawork/ultracode)解决的问题是，固化一个流程本身。
- 6月2日08:20
- h3(我的猜测)是agent/人类能够根据需要，动态地调整flow
- 看到
- Λ httns://githuh cam/uwanshuivin/Aute. claude cade. research in. slaen/hleb/main /skills/met
- optimize/SKILL.md 好像是让agent可以修改运行自己的工作流
- 刘思皓: https://github.com/PolyArch/oh-my-
- humanize ---拿omp搭了一个我心中的h3，核心设...
- 我计划建一座大桥，这座桥设计上要扛10级地震
- 建造过程中发现10级地震啥材料也扛不住，根据最近100年地震观测数据，和地震等级评估，该地区几乎不会发生6
- 级以上地震，设计目标可以下调到抗8级地震来建设。
- 但这一调整也需要同步回rfcs/spec里去
- 感觉这过于依赖base model能力
- 刘思皓: h3(我的猜测)是agent/人类能够根据需要，
- 动态地调整flow
- 现在是说你如果让ai自己选择一些结构也好别的也好他要能判断选择什么样的结构
- 或者做出什么变化
- 会带来什么效果
- 甚至更细微的，当10级以上台风和地震同时存在时，抗震等级降到7级之类
- 就算他自己跑实验拿到数据再想都不太做的对
- 我想更多地先把可调的接口暴露出来，至于后续是否真的会触发/使用，还是要看实际效果
- B4RRy: 感觉这过于依赖base model能力
- 如果真的完全没用，那就退化成h2
- 有parallel gen-idea skill了吗
- 刘思皓:我考虑这样一个场景：1. 在项目开始前需要大
- 规模探索，就需要并行点子生产机--参考humanize...
- 听下来不同stage有不同的workflow 模板 这个例子里不是long run 中间会有暂停点吧
- 刘思皓:我考虑这样一个场景：1. 在项目开始前需要大
- gen-idea本来就是parallel的把
- Luke: 有parallel gen-idea skill了吗
- 一下子想10个点子我记得的
- 我目前设计的是，agent如果想改flow需要人类审批通过
- 洋洋阳:听下来不同stage有不同的workflow模板这个
- 例子里不是long run 中间会有暂停点吧
- 不过也允许--yolo
- xs，还没用过。
- 刘思皓: gen-idea本来就是parallel的把
- h1: some flows that work
- h2: a language that defines flow, building many flows
- h3: agents define and change their own flows
- 反正就是这三步走
- 看看h3在6周内会不会进cc/cx的主线
- 6月2日08:33
- crud软件里有非常多的分支，一个模块完成工作有很多限定条件，有些甚至已经完全偏离了最初设立的目标，即便没
- 有偏离，也增加了非常多的限定语。
- 6月2日08:41

---

#### 原文 L32379–L32390

[回到原文件 L32379](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32379)

- 他的新实验
- 我觉得harness要改成，让Al感受到和人类同等的对时间流逝的痛苦的感受
- ai寿命无穷无尽
- 比如，每后台shell命令运行一分钟，就自动注入一句“你的生命已经流逝了一分钟”
- 王邦彦:我觉得harness要改成，让AI感受到和人类同
- 等的对时间流逝的痛苦的感受
- 被污染了之后也改不了。
- 这个/clear之后重开吧，应该是上下文的干扰
- Luke:被污染了之后也改不了。
- cc喜欢自动把一些实验的结果给存到memory去
- Luke:被污染了之后也改不了。
- 6月2日10:29

---

#### 原文 L32398–L32413

[回到原文件 L32398](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32398)

- 不清楚是上下文稀释还是训练数据的问题先解决眼下问题再说
- 反正你就看结果一不一样吧
- 6月2日11:04
- rlvr
- 你就说得不得分吧
- 所以 humanize 2 和 claude workflow 是完全等价的设计么
- 完全等价肯定没可能呀...
- 只能说，h2给你带来的增量
- workflow 是通用设计，humanize 很opinionated
- 不足以让你脱离claude原生的workflows
- 但本质上都是固化了一套流程，claude workflows用的是js固化
- h2用的是html固化
- 我怎么觉得js更优越

---

#### 原文 L32613–L32634

[回到原文件 L32613](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:32613)

- 感觉主要和你的agent running时间粒度相关
- 同一个问题,图1是GPT图2是Ds,开头就就看出cot质量了
- 如果你套humanize那应该可以睡饱8小时
- 填一个十天以前的坑：
- oh-my-qemu：基于 humanize workflows 实现的 skill/p
- 模，由于引入了 rlcr-loop，建模的正确性和质量都非常高，
- repo: https://github.com/zevorn/oh-my-qemu
- 实践效果：https://github.com/zevorn/qemu/tree/chao
- humanize repo: https://github.com/PolyArch/humaniz
- skill/plugins 的 omp 安装命令:
- omp plugin marketplace add zevorn/oh-my-qemu
- omp plugin install oh-my-qemu@oh-my-qemu
- 切来切去然后tokens烧得飞起，体感上打得很满并行度很高
- 实际进度咋样不好说
- 我感觉agent multiplexer主要还是情绪价值
- 明扬：我很早之前就已经对ai虚空庆祝，丧事喜办免疫
- 切来切去然后tokens烧得飞起，体感上打得很满并行度很高
- TECO

---

#### 原文 L33097–L33149

[回到原文件 L33097](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33097)

- 还在开发中
- 奇迹的闪光迪迦: sihaoge哥的oh-my-humanize需要
- 自己本地编译m吗
- 今天搞完
- 我本地编译提前试用了一下
- 起了个调研workflow
- 6月2日23:39
- 这么着急嘛
- 我今天好好打磨一下
- 让我们看看这件事还会不会发生
- 香港科技大学 研究助理教授 徐策羽: Humanize做啥，
- 然后过了两周之后，就出现在了cc的mainline里
- 我主要在学习你加的这些功能
- fot
- 后面我可能也要定制我自己的omp了
- 对的
- 意思是说，Workflow里面的subagent能在运行的过程中去改这个Workflow嘛
- 刘思皓: h3=oh-my-humanize=agent mutable
- workflows
- 我觉得程序员人人定制自己的omp最后才是正解
- 6月2日23:42
- Horace: 意思是说，Workflow里面的subagent能在运
- 行的过程中去改这个Workflow嘛
- 这样的话怎么确保最终的结果呢改着改着就乱七八糟了我感觉workflow本身就是为了限制LLM的不可靠性
- 我觉得从动机上来说，这么做是有道理的：动态肯定比静态好一些。
- 但实际效果好不好
- Claude code的workflow主要是烧token烧得让我感觉很爽
- 还需要精细设计
- 原版ralph-loop和humanize的核心都是一个loop
- Horace:这样的话怎么确保最终的结果呢改着改着就
- 乱七八糟了我感觉workflow本身就是为了限制LLM...
- 但效果天差地别
- 难的是如何达到一个更好的效果，通过一系列机制
- 这些机制是啥：我也不知道
- 实际效果感觉跟我带着预设知识加brainstorm加手动提示指派多subagent差不多
- 但我想先把脚手架/基础设施搭了
- 感觉动态workflow也合理
- 可以根据已经执行的agent的结果剪枝或调整之后的工作流
- yep 大概就是这么个意思，但这个老哥的顾虑也在理
- Horace:这样的话怎么确保最终的结果呢改着改着就
- 乱七八糟了我感觉workflow本身就是为了限制LLM...
- 感觉需要有一个agent去维护workflow
- 6月2日 23:48
- “动态可改的workflow”并不一定好，需要设计一套机制让它达到最佳效果我觉得还是蛮困难的
- 我现在的设计是：改工作流本身需要人类批准
- 我感觉有两种：一种是主 session llm 根据部分 workflow/subagent的执行结果来判断后续需要动态生成什么样的
- workflow; 另一种是 workflow 里面有预设的 if else 判定条件，这个条件可以是 subagent 的输出.当然从框架的角
- 度可以把各种动态性都支持上让大家试。

---

### 6月3日

#### 原文 L33154–L33176

[回到原文件 L33154](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33154)

- 刘思皓: 我考虑这样一个场景：1. 在项目开始前需要大
- 规模探索，就需要并行点子生产机--参考humanize...
- 6月3日00:51
- 感觉人应该像写python—样写workflow
- 刘思皓: 我考虑这样一个场景：1. 在项目开始前需要大
- Ilm时代的PL
- 6月3日00:56
- 我对 workflow的认知感觉在短短一周发生了蜕变
- 最开始我想要的是一个简单原语的 workflow。后来尝试用 humanize h2 的时候发现不支持 function 和 var
- 我进一步想能不能在上面再构造一层 pl，只把 humanize h2 当做isa 和 vm
- 粒度太粗了，干不了
- 6月3日01:00
- 确实
- 的读，它说完成了实际上已经偏离最初要求
- 然后再仔细想一了一下，这样相当于给agent搞了一套完整的pl+compiler层。我就反思了我到底需要什么，感觉
- 还是【对 code agent】足够细粒度的控制
- 那能不能在复用一套完整的的 pl+runtime的情况下拥有对 agent的细粒度控制呢?

---

#### 原文 L33180–L33205

[回到原文件 L33180](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33180)

- 然后自己用 pyhon 写 workflow+ codex rpc 就还工作的挺好的，不过 await 确实差了点
- 6月3日01:12
- yep
- yc: IIm时代的PL
- 那我大概想象一下，比如说我们要 Auto Research的话，人类提供一些想法和问题，然后 AI来生成一系列的方案，
- 然后第二步就是并行地尝试这些方案，这个场景看起来比较贴合？
- 刘思皓:我考虑这样一个场景：1. 在项目开始前需要大
- 规模探索，就需要并行点子生产机--参考humanize...
- 是，但是我更想说的是所谓meta-workflow这件事
- 你的workflow并不是永远一成不变的
- h3想要回答的问题就是：
- 1. 谁来设计/改动workflows?
- 2. 怎么改workflows是合理的？合法的?
- 3. 什么时候触发workflows的更改?
- 这一系列问题的答案：我不知道
- 刘思皓: 你的workflow并不是永远一成不变的
- Isee
- 先搭infras，再通过大规模的试验，寻求好的方法论机制
- 最后回答这一系列问题
- 刘思皓:h3想要回答的问题就是：1. 谁来设计/改动
- workflows?2. 怎么改workflows是合理的？合法的...
- 所以从自动化方法论的角度来看，h2存在的意义和时间都很“瞬间”，我构建h2的核心目的一直都是：
- “我们需要一套标准的编排原语去构建workflows，这套编排原语应该是强契约的，被一组产物固化的。
- 我没想到这个被主流工具接受得如此之快
- 以至于h2现在并没有存在的必要

---

#### 原文 L33287–L33299

[回到原文件 L33287](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33287)

- 可借了
- 它这个自动粘贴上下文还挺方便的，我之前都是复制路径，再粘贴路
- 那就只能在本地用用了，
- 陈磊:好像没有
- 6月3日12:39
- humanize = 流量密码
- 感觉是agent/自动
- humanize = 流量密码
- L.Zhu:
- 是不是容易被openclaw这类抓取
- 观察那种200h以上的长程任务
- 实在是非常inspiring
- 啥任务能跑200h

---

#### 原文 L33446–L33500

[回到原文件 L33446](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33446)

- 6月3日13:00
- 我觉得workflow还是需要的，因为我觉得这个事情很多时候是自发的。
- 我发现我自己写prompt的时候很多时候都会不自觉的去做描述workflow的事情
- 写一下python调agent sdk的方法也行了
- 你说workflows本质带来了什么呢？规范模型的动作?
- 原来只是为了让agent可以一直跑
- 刘思皓:我今天突然觉得可能workflows不是必须的
- 没必要嵌到harness里面
- 如果它只是为了让模型不跑偏
- 其实只需要提升模型follow prompt的能力就好了
- 不需要workflows
- for me, workflow is a type of task-specific super-alignment.
- 刘思皓: 其实只需要提升模型follow prompt的能力就
- 好了
- 还有增大并行度哪
- 但是模型能力还不够？
- 当然，也很有可能未来workflow control的能力本身就被训进了基模里面
- 还有增大并行度哪
- 但是模型能力还不够？
- 你可以直接写：/goal帮我干XXX，其中某一个YYY，并行启动N个subagents干
- Shom:还有增大并行度哪
- 如果模型follow prompt的能力够强
- 不需要workflows去做硬化的约束
- 这个感觉只要有个agent implement/agent review的loop就可以了，虽然可能会跑偏
- cherichy: 原来只是为了让agent可以一直跑
- 也不需要很复杂的workflow
- workflow是一种廉价的in-context alignment
- h1用hook是为了能调用codex而且每跑一步能抽一鞭子从而获得持续工作的能力
- 这个也可以写成：/goal帮我做XXX，首先把它分成N个小份任务，然后每个任务启动一个builder subagent做，然
- 后任务做完之后，在commit之前，启动另一个subagent去做review，review出现问题的话，先修复再commit
- 小乱: 这个感觉只要有个agent implement/agent
- review的loop就可以了，虽然可能会跑偏
- codex抽风了
- workflows是高级hooks
- 香港科技大学 研究助理教授 徐策羽: workflow是一种
- 廉价的in-context alignment
- 廉价的in-context alignment
- hooks是简陋的workflows
- cherichy: h1用hook是为了能调用codex 而且每跑一
- 步能抽一鞭子从而获得持续工作的能力
- 对 但这感觉就是human alignment
- 刘思皓:这个也可以写成：/goal帮我做XXX，首先把
- 它分成N个小份任务，然后每个任务启动一个builder...
- 现在有了/goal就看模型能不能align这个goal了，写模糊的goal能跑到地老天荒
- 不跑偏
- 6月3日13:05
- 没有任何理由相信，可以通过外部hook做的control flow没办法被训进基模里。
- 所以我只能说，在当前这个节点，workflow是一种廉价的alignment。现在存在只是因为align到workflow的基模还
- 没被训出来。
- goal了，写模糊的goal能跑到地老天荒

---

#### 原文 L33504–L33516

[回到原文件 L33504](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33504)

- 信，可以通过外部hook做的control flow没办法被训...
- 我现在反而觉得，在长程任务里面，必须引入睡觉机制
- 需要有一个第三方介入，然后让这个agents进行大记忆浓缩
- 这个大记忆浓缩有别于compact
- 类似grokking
- 令人非常惊讶的就是，codex的/goal，somehow已经多多少少实现了这个效果
- 引一个无先验bias的第三方来纵观全局一下能不能跳出局部最优
- 这就是lab的每周组会制度，所有的subagent先停下手中的活儿统一sync一下
- 香港科技大学研究助理教授徐策羽: 这就是lab的每周
- 组会制度，所有的subagent先停下手中的活儿统一sy...
- 但感觉无论你训练到啥程度，总可以在这之上引入超出模型能力的抽象层
- 香港科技大学研究助理教授徐策羽:没有任何理由相

---

#### 原文 L33520–L33533

[回到原文件 L33520](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33520)

- 果，但是也有1/5会明显陷进去
- 刘思皓: 令人非常惊讶的就是，codex的/goal,
- somehow已经多多少少实现了这个效果
- 到达某个临界点可能就没意义了
- Reiko:但感觉无论你训练到啥程度，总可以在这之上引
- 入超出模型能力的抽象层
- 6日3日13:10
- 绷不住了，那agent是不是还得干一会约个会给你align一下
- 香港科技大学研究助理教授徐策羽:这就是lab的每周
- 组会制度，所有的subagent先停下手中的活儿统一sy...
- 你再引入抽象永远逃不出模型本身
- 本质上基模解决的是zero-shot的问题。至于这个zero-shot和环境去in- context RL之后和task align得怎么样，这
- 个才是争论的重点。
- 那就 asi 了，开始躺平

---

#### 原文 L33537–L33565

[回到原文件 L33537](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33537)

- 同意啊
- 我只是很好奇，这种workflow native的基模型要怎么训。感觉这个reward传递也太长程了。
- 确实，我的观点一直是：不被内化的skill/harness/workflows，没有存在的意义
- 香港科技大学 研究助理教授 徐策羽: 没有任何理由相
- 信，可以通过外部hook做的control flow没办法被训...
- trajectory就已经很难训了
- 6月3日13:16
- 其实也不是，我觉得现在in-contextlearning和你真的要去back-prop的learning的边界已经越来越模糊了。
- 刘思皓:确实，我的观点一直是：不被内化的skill/
- harness/workflows，没有存在的意义
- 但这样容易定死workflow吧
- codex最近好像还真挺经常retrying的
- 6月3日14:04
- 话说，这种in-contextlearning要如何定义(or是否需要)general的verifiable的reward呢?不然或许很容易落入
- case by case的noisy evaluation中?
- 香港科技大学研究助理教授徐策羽：其实也不是，我觉
- 得现在in-context learning和你真的要去back-prop...
- 6月3日14:22
- 我不知道，这个问题太难了
- 所了个长:话说，这种in-contextlearning要如何定义
- (or是否需要)general的verifiable的reward呢?不...
- 我觉得要是能做的出来的话，会是一个potentialimpact很大的工作
- 对于这件事情我也有同感，不过也没太想明白两者之间的边界在哪里。以及“in-contextlearning”这种新范式(或
- 者或许说LLM在环的优化方法?)，到底要解决哪些关键challenge才能成为目前supervised learning&RL同等定
- 位的alternative优化方式
- 香港科技大学研究助理教授徐策羽:其实也不是，我觉
- 得现在in-context learning和你真的要去back-prop...
- 感觉得靠learning的pro们来解决了
- 6月3日14:28

---

#### 原文 L33649–L33667

[回到原文件 L33649](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33649)

- 谈芯沙龙|张宇鑫徐岩《AI在长程
- 任务工作的探索及香山应用实践》
- UP主：北京开源芯片研究院
- 播放: 5
- 哔哩哔哩
- humanize宣传片出来了
- 6月3日18:17
- [芯片 Agent 产业化 01]"香山"在长
- 程任务上的探索
- 关键词：多智能体协作、RLCR
- 迭代审查(Ralph-Loop with
- Codex Review)、Al 编程治...
- 北京开源芯片研究院
- 附录Humanzie细粒度解析报告
- 你们现在ucagent能兼容skill吗
- 6月3日18:39
- 用途固定就行了

---

#### 原文 L33688–L33704

[回到原文件 L33688](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33688)

- 6月3日21:33
- Humanize 1k+ star了
- 感谢大家 🙏
- PolyArch
- humanize
- From Automated Idea Factory to Realization
- ☆1k stars80 forks
- KDA: Kernel Design Agents
- 很兴奋和大家分享 KDA:
- Kernel Design Agents,
- MLSys Flashlnfer Kernel C
- 小红1书
- 小红书
- RLCR，启动！
- KDA: Agent 自己写
- CUDA并在2026
- Flashinfer Kernel

---

### 6月4日

#### 原文 L33821–L33875

[回到原文件 L33821](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33821)

- 可能第三方没有针对开这个进行训练吧
- 4.8感觉针对训练过harness，他满嘴harness
- 非常注重这个
- 6月4日00:39
- subagent codex的是串行的
- 我让他开1024个subagent，看后台基本没token调用
- Six Workflow Patterns
- https://x.com/trq212/status/2061907337154367865?s=46
- @福尔高斯
- 学习
- 学习
- loop until done
- 6月4日00:44
- 群公告里面@福尔高斯做的那个 multi-agent.wiki 其实某种意义上我觉得比人类学说的更加全面一些
- 大家可以去看看
- https://multi-agent.wiki/
- 但是稍微有一些分类重复
- 6月4日01:02
- 有的，setting，这样就很好用了
- 6月4日01:02
- 群公告
- -本群话题为技术相关的AI/LLM开发相关工具、流程、心得。
- - 带偏话题的情况会提醒一次，连续两次带偏话题会被移除。
- -有招聘信息发布需求请直接联系群主，会更新在下列招聘公告，群内禁止*发布*和*讨论*招聘相关信息，违反者会
- 被移除。
- 【腾讯文档】Humanize群招聘信息公告版
- https://docs.qq.com/doc/DUk51dUFVVktFQnpn
- 项目：https://github.com/PolyArch/humanize
- Token监控: https://github.com/SihaoLiu/ai-usage
- Multi-Agent Wiki: https://multi-agent.wiki/ by Holegots
- - Humanize1: https://drive.google.com/file/d/1bvQI_IE1JyXqW6NkSMFPrs_G0erAdgca/view?usp=sharing
- - Humanize2: https://drive.google.com/file/d/1j-Xxtwf5GQ5PYcJ8GInd6XOKNuizUNbl/view?usp=sharing
- - Humanize — past, present, and future from Ligeng@Nvidia
- [文件]Advancing Token Productivity w: Agent Loops.pdf
- 《Humanize带来的Codex使用范式变化，解锁 Agent 优化 kernel 上限》
- - https://mp.weixin.qq.com/s/pScZ_9cA-6cWUPjfcGjNyg
- 《Claude 实现、Codex审查、人类决策领航：Humanize 项目用 RLCR编排长程闭环迭代任务》
- - https://mp.weixin.qq.com/s/qceRk9Qfq0Q3CTdD6P1Vag
- 《SGLang SOTA Humanize Loop:让 Codex 自动追推理性能到 SOTA》
- - https://mp.weixin.qq.com/s/6uzb0OFDCDt4xmRcWaelaw
- 《让 Agent自己优化 CUDA kernel,并在MLSys 2026 FlashInfer Full-Agent Track拿下前三》
- - https://mp.weixin.qq.com/s/xlOIr4y60dzyeOn_3toipA
- 《月烧6300刀才明白：Agent团队飞轮是怎么转起来的》
- - https://mp.weixin.qq.com/s/S45KRGmDCCLu5GoBa7v2bQ
- 《Humanize: —个 prompt 重构 GEM5的构建系统》
- - https://zhuanlan.zhihu.com/p/2011939681307206316
- 了解更名
- 【腾讯文档】Humanize群招聘信息公告
- Humanize Slides
- - Humanize1: https://drive.google.com/file/d/1bvQl_IE1JyXqW6NkSMFPrs_G0erAdgca/view?usp=sharing
- - Humanize2: https://drive.google.com/file/d/1j-Xxtwf5GQ5PYcJ8GInd6XOKNuizUNbl/view?usp=sharing
- - Humanize — past, present, and future from Ligeng@Nvidia
- [File] Advancing Token Productivity w: Agent Loops.pdf
- - https://mp.weixin.qq.com/s/xlOlr4y60dzyeOn_3toipA
- 了解更多

---

#### 原文 L33918–L33942

[回到原文件 L33918](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33918)

- And good research groups/teams
- It seems they are unable to train their model to execute tool calls reliable.
- Which is so called: agentic ability
- In my opinion It is not comparable at all to hard working cousins codex or Claude
- Yes
- B4RRy: Which is so called: agentic ability
- Interesting is the same thing is happening on Nvidia's model, Nemotron
- 6月4日02:06
- This looks like sth about post-train problem. I am currently working on nemotron to see if can enhance tool
- calling. But they're going to release Nemotron 3.5, currently only 3.0 hopefully they havent solved this lol
- But even we put this aside and discuss sth like base model ability
- I still think GPT is the best and much more better than others ?
- Yes I don't know what is the reason. Maybe someone with more model knowledge can speculate, maybe
- the overfit some benchmark.
- B4RRy: This looks like sth about post-train
- problem. I am currently working on nemotron to...
- I like codex most because it doesn' t want to make small talk to me but execute my task and instruction reliable
- B4RRy: I still think GPT is the best and much more
- better than others?
- They tuned model well while the base model itself is also relatively clever, still very shitty
- Simon: I like codex most because it doesn' t want
- to make small talk to me but execute my task an...
- If they can let people use sth like gpt5.5 pro as coding agent I'll be happy to use it even it can be 10 times
- slower in aspect of tps
- It is very good in math and could solve complicated mathematical problem encountered in trading for a

---

#### 原文 L33948–L33983

[回到原文件 L33948](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:33948)

- For math problem and other research based discussions
- It would be good to use as planning model for sure. For plan we can wait few minutes and better make it
- good imo
- B4RRy: If they can let people use sth like gpt5.5
- pro as coding agent I'll be happy to use it even it...
- The smaller agent can collect the relevant context and provide to the best model
- 6月4日02:12
- Claude现在会在文件里有大量的索引，索引别的md，你们觉得这是好的实践吗？应该让他少索引吗？
- Claude Code Workflow 必读：面
- 向所有任务的 harness
- 随 Opus 4.8 发布的 Dynamic
- Claude Code
- Workflow，可以实时编写编排
- Workflow
- 脚本、启动子Agent舰队并行...
- AGI Hunt
- 6月4日02:27
- My idea is as long as we can reduce the error rate to an acceptable level and let it works overnight or sth,
- even spending 10x time is accetable
- Simon: It would be good to use as planning
- model for sure. For plan we can wait few minute...
- 感觉挺好的呀
- Luke: Claude 现在会在文件里有大量的索引，索引别
- 的 md，你们觉得这是好的实践吗？应该让他少索引...
- 相当于逐渐分阶段的披露内容context
- 不一股脑塞进去
- 今天codex的tpot好像高很多
- 6 日4□.02:44
- I am not sure. I think as long as error rate is != 0, being able to sample trajectories from multiple agents in
- parallel is quiet valuable (and likely better than taking only one moderately better model) in my opinion.
- B4RRy: My idea is as long as we can reduce the
- error rate to an acceptable level and let it works ...
- 6月4日03:04
- workflow ultracode

---

#### 原文 L34105–L34123

[回到原文件 L34105](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:34105)

- 6月4日17:58
- 我又回退了，把一样的Prompt发给了gpt5.5
- 它完美解决了所有问题
- 我想说，人类学，what are you doing?干不过5.5就算了，kimi2.5都干不过?
- 人类学和OpenAI是相互竞争的关系。只有你来我往，他们才会有一个良性的进化过程。现在人类学模型不行，但不
- 意味着下一个不行，毕竟当时opus还是很惊艳我们的，对吧
- 群友们有类似离谱经历吗？A社模型还能不能用了？最近用ccterminal的goal写全新project spec也是，任务拆分的特别碎。
- 本消费者只想让它退钱
- Yuehan@INTC:人类学和OpenAI是相互竞争的关系。
- 只有你来我往，他们才会有一个良性的进化过程。现..
- 6月4日18:13
- 模型不行，但是claude code的dynamic workflows很先进
- Yuehan@INTC:人类学和OpenAI是相互竞争的关系。
- 只有你来我往，他们才会有一个良性的进化过程。现...
- 模型不行 每个step都是错的整体误差积累拉爆了
- 郑权: 模型不行，但是claude code的dynamic
- workflows很先进
- 等mythos出手一切都会不一样的
- 饽饽博: 群友们有类似离谱经历吗？A社模型还能不能

---

### 6月5日

#### 原文 L34323–L34350

[回到原文件 L34323](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:34323)

- 你不要管它是什么东西
- 只要掺进上下文
- 效果就会好
- 这么牛逼
- 我也试试看
- 你觉得并行开agent审核每一轮写的代码会游泳嘛
- 会有用嘛
- 会不会有某个agent发现比如这里有可优化点
- (虽然我感觉好像没啥用)
- 并行审核?
- 因为他们都是一个模型有一个地方不符合简单要求其他人也看不出来
- 除非是并行审核不同的东西/组件
- 6月5日 06:33
- 他是宁可保持错误的代码，也不愿意砸掉已经结果
- L/适
- 给个 prompt 哥们
- 刘思皓:我近期的实践是“RISC/奥卡姆”这个字符
- 串，宛如TDD
- 会在一些奇怪的地方反复浪费时间调花
- B4RRy:会不会有某个agent发现比如这里有可优化点
- 就“你根据奥卡姆剃刀原理精简一下。。。”之类的吧
- 我倒是无所谓只要最后跑出来东西符合要求
- Luke: 会在一些奇怪的地方反复浪费时间调花
- 花10x时间是可接受的
- 审啥呢
- B4RRy:你觉得并行开agent审核每一轮写的代码会游
- 6月5日06:38
- 如果只是字面审核的话感觉效果一般

---

#### 原文 L34591–L34602

[回到原文件 L34591](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:34591)

- 6月5日11:16
- 好像是omp的analytics，自动上报工具错误的
- 6月5日12:01
- 科研的代码应该有测试嘛？感觉测试都过期得很严重
- 很多错误的想法的测试
- 6月5日12:12
- 对我也感觉测试会有些死板，且复用场景不多？我现在是写一些high-level的verification要求，要求负责implement
- 的模型设计evidence，dump结果到文件里；review模型负责审查evidence是否能证明所要求的verification
- Luke: 科研的代码应该有测试嘛？感觉测试都过期得很
- 严重
- 6月5日13:59

---

#### 原文 L34606–L34618

[回到原文件 L34606](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:34606)

- claude来coding？这个默认可以关吗
- 我得自己输prompt让他用codex
- 你在 codex 里直接用 humanize 就行呀
- 但是他给我生成的plan里
- lude exactly one routing
- ented by Claude
- ted via Codex (/humanize:
- 6月5日14:05
- 你把humanize插件装到codex中
- 我就是这样的呀
- 这个routing描述算是cc遗留下来的prompt 在cx里起rlcr会无视这个routing规则
- 这个是因为模板是这样写的
- 6月5日14:46

---

### 6月6日

#### 原文 L34690–L35095

[回到原文件 L34690](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:34690)

- 以前脑子想累了想不出来就休息
- 现在都不需要休息，可以从早干到晚
- dv 是啥
- 刘思皓: 我还是觉得Al只是把Implementation的心智
- 负担切分到Arch和DV上了
- design verification
- 感觉有一点还挺有成就感的，就现在开PR特别容易
- GYF:不仅更累，而目成就感更低以前实现一个功能
- 以前都懒得写代码，现在随便pr
- 6月6日03:31
- 但是确实效率是实打实的提高了
- "B4RRy" recalled a message
- 提高几倍不好说反正确实比以前快不少
- 以前想要让自己更累干更多活是难的现在这个scalinglaw变得更好了一点(人的时间开销，实际完成的工作量)
- 把智力劳动变成了体力劳动加金钱活动
- 6日6日.04:44
- 并没有反而更多智力劳动
- 以为效率*时间=工作量，效率提升了，工作时间可以减少得到更多休息
- 可是目前来看工作量是无穷无尽的，效率提升了就只是提升了效率而已
- 6月6日 05:58
- 工作量无穷无尽
- 打工人工资一分不多
- 付费
- cc 定位神秘 bug，一个非常神秘的 bug
- 6月6日06:24
- cc还不喜欢装软件，pytest没安装它就一直walk around，
- 6月6日06:36
- claude的限额是不是增加了
- 6月6日07:40
- 我又发现一个奇技淫巧
- 你可以开一个claude code的/loop
- 然后把正在运行/goal的codex的session id交给claude code
- 然后让claude code帮你分析代码库和这个session id 的transcript
- d星近写优现不年么行但目做个筑一方士监控
- 个开发目不购伯还挺合适的
- claude code最近写代码不怎么行，但是做一个第三方去监控一个开发是否跑偏还挺合适的
- 然后如果跑偏了，直接让它/remote发手机提醒
- 就是做监工呗
- 对但是和之前的review不太一样
- 6月6日07:44
- 之前humanize是做代码审查的监工
- 现在说的是找一个第三方工具做“进度”的监工
- 监工是否跑偏不是属于判别式问题吗，本地跑个模型监工他感觉够够的
- 这里有一个神奇的事情，你如果用/loop开进度监工
- 它somehow能够感受“时间流逝的痛苦”
- 可能是没见过如此枯燥的活
- context一长他就知道这是个枯燥的活了
- 就是它能够容许比如说codex往一个方向深挖3个小时
- 但是5个小时它就会告诉我不对劲了
- 如果你不找一个第三方的进度监工，自己监督自己很难感受到“时间流失的苦痛”
- worker context是一直在压缩的
- 监工没在压缩
- /goal“你给我干XXX，每一轮slice结束的时候，用subagent开—个gpt-5.5 xhigh 审查(最简单的humanize)”
- to claude:
- /loop 1h “xxxx-yyy-zzz-kkk 这是另一个codex session的transcript id，你给我在~/.codex直接监控它的工作进
- 度，它的任务是XXX，如果发现它跑偏或者进入死胡同，用remote通知我”
- 6月6日07:50
- 然后claude就神奇地能够对codex的开发流程感受到时间流逝的痛苦
- 还有就是，/loop的两次触发之间，天然带一个“时间流逝”的上下文
- Weiyang: 监工没在压缩
- 可能是根据触发频率，很多
- 刘思皓:这里有一个神奇的事情，你如果用/loop开进度
- 监工
- 刘思皓: to codex: /goal“你给我干XXX，每一轮slice
- 结束的时候，用subagent开一个gpt-5.5 xhigh 审查...
- 你让subagent，tmux codex在背景干活，主session只监工
- 我已经是这样了
- 其实我的主session负责监工负责清worktree，闲了还负责干一点
- priority
- workers只配开default
- 那就没必要另开了倒是
- 6月6日08:05
- 想问这个写代码不怎么行具体是指啥要避雷一下
- 刘思皓: claude code最近写代码不怎么行，但是做一
- 个第三方去监控一个开发是否跑偏还挺合适的
- disclaimer：这是我两周前的感知，不保证现在claude code是这样的
- - /goal做的稀烂
- - 然后不讲人话
- - 看3-10个文件不到3分钟就敢改代码
- 6月6日 08:15
- 虽然我感觉codex的/goal跑偏的情况比较罕见
- 但是感觉还是时有发生
- *偶有发生
- *偶有发生
- 6月6日08:20
- 可惜唯一不爽的就是 5.5 的 context 只有 278
- 哪怕512 都能爽很多
- 6月6日08:26
- 400 window272
- "Weiyang" recalled a message
- 无所谓大任务拆小
- 我感觉构建一层subagent层级，等效上下文能放大10-25倍
- 确实能，但是 token 感觉烧不起啊
- 然后一个做的比较好的/goal，等效上下文能再放大10倍
- 然后你如果构建两层这个结果，“等效”上下文能放大10000-60000倍
- 这个搞法其实本质并不是让claude帮我监工
- 刘思皓:
- 20x pro 我之前就是，完成xxx，用 subagent review，并拆解 sub task 给 subagent
- 本质上是让claude帮我写/goal prompt
- 6月6日08:32
- 我发现claude写的goal prompt比我写得好
- 你还能有Claude聪明？
- 6月6日08:32
- 1:218
- 不得不说人类学里面我最服的还是boris
- taste极好
- 遇到了
- 陈磊: 20x pro 我之前就是，完成xxx，用 subagent
- review，并拆解 sub task 给 subagent
- 学到了
- boris说：用手机写loop本身
- 我魔改了一下
- 用手机让claude做进度监工，然后写/goal prompt
- 6月6日 08:38
- 然后把openai的codex goal的cookbook塞给claude
- 它写得/goal prompt又短又好
- 我感觉确实cpu要涨
- 我现在一台机器上跑四个/goal
- cpu有点顶不住
- 6月6日08:40
- 为啥
- 是不是就要编译啊
- 然后遇到性能敏感的任务就很卡
- 时不时
- 刘思皓: 是不是就要编译啊
- 我严重怀疑cc的/goal是米索斯特调版
- 然后opus水土不服
- Hanlin invited 刘天乐 Tyler : to the group chat
- 6月6日 08:47
- 为啥要编译
- 你让 cc 调查一下
- 刘思皓: cpu有点顶不住
- 你们遇到过 Codex 丢 session 的情况吗
- 数据库里还能找出来 transcript
- ？开发为啥不要编译
- Luke: 为啥要编译
- 你从订阅换到APIkey就可能会出现
- 吴自华 Gabriel: 你们遇到过 Codex 丢 session 的情况
- 6月6日08:54
- 没换
- 刘思皓: 你从订阅换到APIkey就可能会出现
- 就是有一个 remote 进程断开了
- 想请教下长程任务开始的时候需要写非常完整的doc保证中间不出错嘛？还是可以从highleveI的idea开始
- 重连回去就找不到 session了
- 遇到过
- 吴自华 Gabriel: 你们遇到过 Codex丢 session的情况
- Codex App灰了
- 用下humanize的gen-idea和gen-plan
- chen:想请教下长程任务开始的时候需要写非常完整的
- doc保证中间不出错嘛?还是可以从high level的idea...
- 敬礼！
- Python boy。
- 刘思皓:？开发为啥不要编译
- 只需要 gpu
- 6月6日09:02
- 这种情况应该是在跑一个/goal任务吧？
- 吴自华 Gabriel: 重连回去就找不到 session 了
- 一个/goal开了两天忘关了😄，直接给我账户干穿
- 520.80
- 香港科技大学研究助理教授徐策羽:一个/goal开了两
- 天忘关了😊，直接给我账户干穿
- JW99:让谢老板报销啊
- 6月6日09:07
- 本质还是ai有幻觉需要你去炎症验证需要的工作量知识非常费脑子
- 刘思皓: 我还是觉得Al只是把Implementation的心智
- 负担切分到Arch和DV上了
- 6月6日09:08
- 洋洋阳:本质还是ai有幻觉需要你去炎症验证需要的工
- 作量知识非常费脑子
- 其实我反倒觉得ai是个去民主化的过程
- 心智负担集中在少数人身上
- ai时代搞infra类很累非常耗神 连干了两周我也发现精神状态变差
- vibe coding的舒服
- 我现在都让ai给我的人类小弟派活
- keep human busy
- 哈哈哈
- 外包 review
- ai 写垃圾
- 给别人 review
- 很喜欢 pr
- 指导人类本科生太累了
- 封装一个MCP叫call human是吧
- 6月6日09:14
- 主要是我给本科生派活的时候
- 我可以同时起一个goal
- 6月6日09:20
- 我的做法是做一个文档治理 架构方向实现进度以文档为准防止双写漂移然后随时重启session 切换harness 对
- session没啥特别要求
- Weiyang: 你让subagent， tmux codex在背景干活，
- 主session只监工
- 然后你发现本科生干的不如ai
- 就很绝望
- 我只需要保证文档演进符合预期即可
- 佬您是dev
- 我还以为是lietou
- 而且多harness之间可以小范围并发实现不同的adr实现后一句刷新文档就能接得上
- session想重启就重启想丢就丢
- harness想换就换相同llm harness确实影响效果挺明显
- ai小学生
- 解咏梅: 佬您是dev
- 以文档为准防止双写漂移然后随时重启session切...
- 我也是
- 洋洋阳:而且多harness之间可以小范围并发实现不同
- 的adr实现后一句刷新文档就能接得上
- 6月6日09:29
- 记忆分层古法编程你不会记住每一行代码做不到也稀释没有重点。记住架构图开发规范哪些不能碰各个模块间的
- 关系记住模块内重要的接口定义这些做上下文就很好了
- 英雄所见略同
- Luke: 我也是
- 但是 subagent 感觉挺好的搞快点
- 洋洋阳:然后自己根本不用关心subagent这种心智负担
- 不然要等
- 我发现他们会自动起sub claude omp codex
- 所以我没有把它纳入自己的心智
- task之间他发现没有依赖的还会并行
- 6月6日09:34
- 不同harness x不同llm 组合太多经常赛马也蛮累的
- spec文档是一个半解压的codebase
- idea转/goal解压成spec
- 是的
- 其实还有个隐藏的范式转换 古法时代人懒得写文档经常是代码为准，看实现。ai时代反过来了代码不一致看文
- 档肯定你描的实现错了
- 6月6日09:40
- 文档治理会越来越重要
- spec 会看吗
- 刘思皓: idea转/goal解压成spec
- 要看吗
- 需要一套spec ir
- 好的
- goal!
- 我之前都不用 goal产生 spec
- 之后试试，
- 你用过gen-plan吗
- Luke:我之前都不用 goal产生 spec
- humanize的
- 问问朋友们有谁注册了cvpr但没有去嘛
- 那不就是goal产plan
- 是不是也可以所有 prompt 都用 goal?
- 6月6日 09:46
- 不行
- 你得去熟读并背诵—下codex goal的cookbook
- 6月6日09:46
- cc呢
- cc有六周不用了，不懂……
- 6周in ai is like forever
- opus 4.6年代了
- 刘思皓: cc有六周不用了，不懂.....
- 年代这一块
- 天上一天，人间一年
- 6月6日09:55
- 刘思皓:cc有六周不用了，不懂.....
- 谁赞成谁反对
- 6月6日10:02
- cc更新也很快omp更是版本狂魔现在最好别关门多赛马
- 刘思皓: cc有六周不用了，不懂.....
- 模型的事不是framework能救的
- 悲伤
- 6.5日GPT Pro误封补偿：赠送一个月订阅
- 6月6日10:41
- 具体拆开说：
- goal 本身很费
- 写一个好
- 写六件事：结果、
- 模糊目标 + 自动插环 = 危险组合
- 很多交互本来就该停下来等人
- 巴这个天然的暂停点取消了，等于把人踢出了循环一对探索性、需要人判断的工作反而有害。
- 或者
- goal;一轮就能给出答案、
- 量的目标
- 6.5日GPT Pro误封补偿：赠送一个月订阅
- 可以S朵几购
- 6月6日10:41
- 就能给出答案、或者
- 人就需要不断地写约束，写目标
- 不要发跑一下这样的prompt
- 让cloud教教我怎么用 goal
- 6月6日10:48
- 适合重写类的工作 bun 到rust 有大量测试用例
- 如何一口气设计一个长goal batch 是个新挑战
- Luke: 人就需要不断地写约束，写目标
- 放假旅游了设计一个长goal干个好几天
- 6月6日11:16
- 洋洋阳: 如何一口气设计一个长goal batch 是个新挑
- claude + 我 => 写给codex's /goal的prompt
- codex + /goal + subagent => 干活
- claude + subagent => 监控codex's /goal的进度
- 这熟悉的codex/goal
- 刘思皓:
- 这是claude code
- 翁大爷的翁大爷:这熟悉的codex/goal
- 你混乱了
- ?？??
- 你不是说你6周不用cc了吗？
- 6月6日11:21
- 不用 = 不高强度用
- + 没有时刻追版本release-note
- 6月6日11:22
- 还不到关门的时候啊
- 还不到关门的时候啊
- 洋洋阳: cc更新也很快 omp更是版本狂魔 现在最好别
- 关门多赛马
- 要多多尝试各种方法论/工具
- 全部炼化为我所用
- 这两件事单独拿出来都不是很爽，就so-so
- 结合起来就很爽
- 我观察到codex/goal基本每2-3小时会开始有点跑偏
- 然后被claude抓到，一鞭子抽回去
- 6月6日11:27
- 不用humanize了嘛
- 刘思皓: 我观察到codex/goal基本每2-3小时会开始有
- 点跑偏
- 还是用的
- 怕他有时候偏离意图，找些workaround
- 刘思皓:然后被claude抓到，一鞭子抽回去
- humanize适合增量改进
- humanize的那个loop engine有点太重了
- 是个干一个PR级别的工作
- 虽然本质上都是agentic loop
- humanize的loop是个重卡，codex的/goal是个跑车
- "Ieshenj" recalled a message
- 学到了哈哈
- 1O
- 刘思皓:然后被claude抓到，一鞭子抽回去
- 6月6日11:35
- 感觉拓展上下文就很有帮助，
- 洋洋阳:记忆分层古法编程你不会记住每一行代码做不
- 到也稀释没有重点。记住架构图开发规范哪些不能...
- 好奇怪的一板一眼回答
- 刘思皓: humanize的那个loop engine有点太重了
- 我让它(claude code)直接往codex-tui的session里面打子
- 打字
- 模拟我输入prompt
- 我尼玛
- 竟然是模拟输入
- 竟然是模拟输入
- 让你的智能体
- 24/7持续运行。
- $199
- 这是基本操作啊
- claude code当时的swarm agents team就是这么做的
- 6月6日11:38
- 我也是炼化的
- 我觉得这里有一个非常关键的东西
- 就是我本地的~/.codex和~/.claude有大概50个/goal的实例记录
- 这个我之前试过，我觉得bug实在是太多我捉摸不透...
- 刘思皓: 往一个tmux session里面模拟打字
- 然后里面有非常多且丰富的我去steer一个运行中的/goal的经验
- 然后我让claude 给codex /goal发steer prompt的时候
- https://github.com/helvesec/rmux
- 后来我用这个效果比较好
- 香港科技大学研究助理教授徐策羽：这个我之前试过，
- 我觉得bug实在是太多我捉摸不透..
- 香港科技大学研究助理教授徐策羽: https://
- github.com/helvesec/rmux
- rust rewritten tmux?
- 6月6日11:43
- 感觉很有道理呀
- 刘思皓: 然后里面有非常多且丰富的我去steer一个运行
- 中的/goal的经验
- 刘思皓:然后被claude抓到，一鞭子抽回去
- woc rmux好牛
- 我现在意识到我的~/.claude和~/.codex是很值钱的了
- Luke: 感觉很有道理呀
- 这玩意儿主要是API开放吧，也可能是我之前tmux一直没搞对...
- 刘思皓: rust rewritten tmux?
- 我的顾虑依旧是自己认可自己的问题
- B4RRy: 都用codex监管可以嘛
- 也是
- 哎主要是不想订阅claude了很烦呐
- 因为我这个流程的第一步，就是读正在运行的/goal的全transcript
- 准备拿一个国产模型监控
- 你开个$20就够了
- 确实是
- 这玩意很省token
- 那这个codex-tui session是claude启动的吗还是你手动启动的，只要给claude codex的session id就能让claude去打字了
- 因为它不是review code
- 自己启动就行了吧
- 6月6日11:48
- 我手动在tmux里面启动的，然后告诉claude俩东西：
- - codex的session id
- - codex所处的tmux window position
- 张东宇: 那这个codex-tui session是claude启动的吗
- 还是你手动启动的，只要给claude codex的session...
- 给他tmux号
- 它可以自己tmux输入
- 这玩意有一个好处就是它非常省token
- cc扮演项目经理agent codex扮演架构师agent
- 是的大部分时候都在sleep
- 很长时间读一下
- 不直接对接codex了让cc接管
- 对，我跑了5小时了，claude opus上下文涨了2%
- 不我也没有全让claude接管

---

### 6月7日

#### 原文 L35438–L35508

[回到原文件 L35438](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35438)

- B4RRy: 压缩的话有时候我又看不懂他说的是啥
- 对我文档里全都是代码变量名
- 但是问题是给一堆虚假问题把
- 压缩的话有时候我又看不懂他说的是啥
- B4RRy: ai倾向用什么数字用那种代码变量名讲话
- 6月7日00:59
- 用claude code作为监工，去high-level监控—个codex/goal
- 是我最近10天提升开发体感最大的事情
- 目前来看，codex/goal出现一个claude code认为的跑偏，大概有10%的概率
- 也就是每10-12小时发生一次
- 我现在算是明白Boris说的，在手机上写loop，监控loop是怎么个意思了
- claude code可能在代码审查上面不如codex
- 但是作为一个第三方去监控整体进度还是很不错的
- 而且不是那种LLM虚构出来的“时间预估”
- 感觉可以通过这种方式来训练
- 而是一个真实的时间，甚至它非常快速地适应了/goal的开发速度
- 训练模型学会
- 时间流逝
- 我观察到好几次，它等了3个小时（三次监工，我监工的间隔设置的1小时一次)，/goal还没有从偏离的轨道上回来
- 然后它第四次才介入
- 其实这本质上就是h3想要做的事情
- 差不多是Humanize 2.7
- 用一个第三方agent去监控整个workflow
- 然后在大规模的尺度上出现偏离的话，敲入一个steer prompt
- "刘思皓" recalled a message
- 把另一个工作流拉回正轨
- 大概两周前，我同时监控3个/goal，心智负担巨大
- 现在有这个，我可以轻松在手机上监控10个loop
- 6月7日01:07
- 你如果知道key point
- codex /goal的following prompt做得很好
- 但是还是会跑偏的
- 艾克佐迪亚
- 那你也可以让claude code去帮你盯着这个key point
- 林桢杰: 你如果知道key point
- flew宇合经讨的noint
- 总之这是一个纯增益的事情
- 降低心智负担
- 我来组成头部
- 我的理解是，世上任何事情，都有80%的部分是无聊且机械的，那这部分东西就可以外包给AI。
- 这件事包括“监控一个长程开发的工作流”
- codex goal 跑偏的场景大概是啥样的
- 我们觉得是关键点的地方，资深老哥也认为是关键点
- 钻牛角尖，深挖细节，不推进主线
- skill
- codex goal其实很难跑偏
- 啊，能想象到
- 还是要把你那张图给文字复制
- 没有，在我的私家车库
- 大概我实现一个subagent 功能3d
- 知道跑伯了
- 无所谓
- 你把我那个图片复制给claude，让它炼化就行
- 这么多车
- 刘思皓：没有，在我的私家车库
- 我一直是用一个codex goal控制另一个codex goal
- 刘思皓: 我现在算是明白Boris说的，在手机上写loop，
- 监控loop是怎么个意思了
- 可以几乎不管他
- 好的
- 第一次见这么久
- 会犯错过一段时间被拉回来
- 你这个风险比较大，虽然我没试过
- B4RRy: 我一直是用一个codex goal控制另一个codex
- goal
- 我的监控是会扫整个transcript的
- 不是单纯只看codebase
- 我有让他扫transcript

---

#### 原文 L35533–L35549

[回到原文件 L35533](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35533)

- B4RRy: 但是不会在一个错误的道路一直走下去
- 让它用无状态的subagent来监工
- 我就是这样的
- 林桢杰: 让它用无状态的subagent 来监工
- codex好像有
- 得小心一点
- hhh灵魂画图
- 不过claude subagent没有上下文森
- codex好像有
- 得小心一点
- hhh灵魂画图
- 没有，你指的是继承上下文吗
- B4RRy: codex好像有
- Reiko:没有，你指的是继承上下文吗
- 不会嘛
- 如果不会的话就还好

---

#### 原文 L35559–L35590

[回到原文件 L35559](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35559)

- okk好吧
- 我最近一直在用类似的工作流！
- 刘思皓:
- 感觉确实很棒
- 不过我用的是百家饭这样
- codex的subagent是不是不会自己被关掉
- 我有时候会遇到他开了一些agent然后超过上限
- 不主动关掉旧的
- claude code执行，codex审核，glm deepseek mimo复审...
- 让 main agent 主动关
- 或者调上限
- claude似乎是会话结束自动关掉
- gpt 给10
- 有道理我去看看config怎么把上线拉高
- 非常搞的一点是 compact 之后它忘了 subagent id的话会比较麻烦
- 他调用工具
- 会存在一个地方吧
- 最坏最坏是transcript
- compact后注入
- 做—个tool hook
- 让他调用工具的时候
- 把这个写入到一个当前目录的文件
- 还是要记状态值
- (就只有调用agent工具或者后台命令的时候触发)
- 这是我之前遇到他忘记后台跑了啥的时候做的事情
- 其实我觉得claude code codex这种工具应该再抽象出来被更通用的agent调用
- 很早以前遇到的，当时我好像是直接杀了session然后重启，然后就有了“要管理subagent生命周期”这个意识
- 让通用agent来跟踪他们的状态
- vscode最近是不是好像在更新类似的功能"agents"，我还没试
- 趋势
- 6月7日08:12

---

#### 原文 L35732–L35754

[回到原文件 L35732](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35732)

- 然后会发现compiler和os不够好
- Harness/Agent Infra 会更重要的
- tool call 次数越多，优化单次 tool call latency 的价值就越大
- 在几个这类平台上看，突然起飞的并发量都是因为有人开始模仿bcherny和petestein的并发了
- 张子健: 未来几个月绝对是全自动的flow了
- 6月7日09:05
- 会在某一次系统扩容的时候发现的
- 吴自华Gabriel: Harness/Agent Infra 会更重要的
- 没扩之前岁月静好扩了开始修一切(_;)
- 6月7日09:10
- 标准流程的粒度也会更粗，因为联合多个流程点调优明显能做也能做更好
- 现在大模型infra全在搞serving
- harness这边被显著忽视了
- cuda加速我们主要放算法了
- serving cuda加速主打谁做我用谁 但我不改
- 张子健: 现在大模型infra全在搞serving
- 模型厂更有激励做serving和开高薪
- 看到高薪搞的人就多
- harness归类为....企业it
- 主要是harness也没收敛啊
- serving是利润率部门 harness是成本部门
- 可能只有claw-like原生为了上云设计
- 6月7日09:15

---

#### 原文 L35813–L35830

[回到原文件 L35813](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35813)

- 我现在想找一个oncall的软件
- opus team如果发现codex有点跑偏的迹象，拟定steer prompt之后，如果我在睡觉，需要把我叫醒
- “主动oncall”
- 太恐怖了
- 刘思皓: opus team如果发现codex有点跑偏的迹象，
- 拟定steer prompt之后，如果我在睡觉，需要把我叫...
- 那就pager duty吧就到位了 给你报sev0
- 我给claude opus说的是，如果我超过10分钟回复，你就需要重新拟定steer prompt
- 6月7日13:31
- codex follow prompt做的真是好
- claude大概抽个3-4次鞭子
- 6月7日13:31
- 它就再也不会跑偏了
- builder team in /goal, review team in /loop
- codex cli cron 支持的很差说实话其他都挺好的
- 然后review team一旦发现问题，就要拟定steer prompt，发我手机上，我批准之后再让claude敲给codez
- piano: codex cli cron 支持的很差说实话其他都挺

---

#### 原文 L35878–L35896

[回到原文件 L35878](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35878)

- 6月7日15:31
- 记录一下最近的使用心得：在做一些大项目之前，去找一些类似的或者相关的repo，然后prompt omp去
- “请你主动调查一下./下面我clone出来的几个repo。
- 我现在要做的是xxx。
- 请你想一下为了做到xxx你可以从这几个repo中学到什么?
- 最后请你把你总结出来的experience crystal汇总到./wiki/文件夹里的多个可以互相索引的.md文件中。“
- ok
- bjin: 可以试试这个命令 omp config set
- contextPromotion.enabled false
- 下午12:26·2026年6月7日·3,696查看
- 可以试试这个命令 omp config set contextPromotion.enabled false
- 陈磊:我在omp 上用的 5.5 结果我现在一看，自动变
- 成5.4了
- omp效果好吗
- bjin: 可以试试这个命令 omp config set
- contextPromotion.enabled false
- 6月7日15:38
- 啥项目一个goal跑好几天?

---

#### 原文 L35908–L35930

[回到原文件 L35908](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35908)

- 6月7日15:49
- 我主要还是用omp的多，omp的subagent有irc通讯的功能，写清楚通讯协议能手工起一个很大的orchestration
- team。但我对比过omp和codex的/goal实现，是codex的更稳定不容易跑偏(omp刚实现/goal的时候测的)
- AAA9: omp vs codex vs cc现在对效果到底能差多少
- 我写的harness也有这个功能，但是我觉得a2a通讯此时此刻在绝大部分场景都是overkill
- 大部分场景还是几十个subagent用来隔离上下文就绝对够用了
- 全局变量广播就好
- omp和codex的/goal实现有什么不一样呀
- bjin:我主要还是用omp的多，omp的subagent有irc
- 通讯的功能，写清楚通讯协议能手工起一个很大的or...
- 6月7日21:24
- 体会到为啥 H3 需要设计成动态修改 workflow了，提前定义一个完备的 workflow 是很折腾...
- 我觉得a2a大部分是不需要的
- handoff 就好
- 体会到为啥H3 需要设计成动态修改 workflow了，提前定义一个完备的 workflow 是很折腾...
- 再怎么强的humanize还是没有办法解决细节拉通问题只有看到了才知道模型不知道
- 奇绩创坛2026 春季路演日，56个
- 项目名单
- 项目覆盖智能体、具身&物理
- 奇续创坛路演日
- 智能、数据、AI基础设施、FDE

---

#### 原文 L35941–L35954

[回到原文件 L35941](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:35941)

- 刘思皓: opus team如果发现codex有点跑偏的迹象，
- 拟定steer prompt之后，如果我在睡觉，需要把我叫...
- 感觉就是人人都是ceo
- @Luke 啥任务 能干一宿？
- 6月7日23:20
- 还有 goal cookbook
- 刘思皓: 这是我当前方法论的sota，然后顶层喂给
- codexgoal的是humanize的gen-plan+brainstorm..
- gpu 跑一晚上。
- 洋洋阳: @Luke 啥任务 能干宿?
- 确实
- 林桢杰: 再怎么强的humanize还是没有办法解决细节
- 拉通问题只有看到了才知道模型不知道

---

### 6月8日

#### 原文 L36038–L36046

[回到原文件 L36038](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36038)

- 我在提供gpt之前和之后工程师都用豆包评价好坏
- 豆包么? 先进harness才能驾驭得了豆包
- ai生成的测试点/计划没有人写的全想法好“品味格调”
- 真的是神奇能做的比gemini还好
- 香港科技大学 研究助理教授 徐策羽: grok的search真
- 使用三方agent工具的用户画像是这样的
- 林桢杰: 豆包么? 先进harness才能驾驭得了豆包
- 没用过豆包
- 说到豆包最近好像很多散户炒股是听豆包的

---

#### 原文 L36270–L36293

[回到原文件 L36270](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36270)

- 22.7m8
- 有个问题一直很好奇，这种非常长的 task 他们的 context 一定要一直不断地 auto compaction，还是会感觉
- context rot?
- 刘思皓:我有一个跑了6周的优化任务
- 心下Cuyoeiarn比西不断更部新吧
- Jin:有个问题一直很好奇，这种非常长的task他们的
- context一定要一直不断地 auto compaction，还是...
- 我有两种解决办法
- humanize1.0时代有一个goal-tracker
- 我现在解决任务还是习惯性不断开新 session，然后把之前的一个session做过的写成一个 handsoff doc
- 但是感觉这样也有点呆
- 我最近用的goal，prompt following做的非常好，大概12小时才会有一点偏离
- 让agent自己做一下文档治理
- Jin:我现在解决任务还是习惯性不断开新 session，然
- 后把之前的一个session做过的写成一个handsoff doc
- 因为你其实可以直接给新的agent交一个session id
- 它能自动帮你做handoff
- 但这种其实感觉还是很看 model 自己的 instruction following 问题?
- 刘思皓: 我最近用的goal，prompt following做的非常
- 好，大概12小时才会有一点偏离
- 这个倒确实，现在 cc 和 codex 的session id support 好像还可以
- 刘思皓: 因为你其实可以直接给新的agent交一个
- session id
- 文档两类一类人看一类ai看

---

#### 原文 L36359–L36372

[回到原文件 L36359](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36359)

- 便不觉遥远
- 爽得程度大约有我半年前跑第一次humanize的70%
- 我也是
- 泽文: 我也在做，不过我用的是 omp
- omp现在是我主要构建的基础设施
- 但还没有完全迁移过去
- omp确实很好，除了闪的厉害
- 6月8日15:03
- 现在在构建humanize3的心智模型
- 主要是这件事是纯增益的
- 没有tradeoff
- 不审批就自动退化成codex/goal
- 人类的视角一下就宏观了起来
- 类似走迷宫，人类反馈只需要铆钉几个关键点

---

#### 原文 L36390–L36405

[回到原文件 L36390](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36390)

- Id 发出去。需要 qae codex 做，但它正在跑 28min baseline,不能打断。
- 不用重启、向后兼容),qae侧等它 baseline 跑完再加，最后统一测试验证
- 我这个是直接提示词搞的效果已经很好 没上skill
- 6月8日16:57
- 请问具体是怎么实现在humanize里让cc建工codex goal呢？直接用humanize好像只能codex监cc
- https://github.com/JerryLookupU/humanize-cgcr.git
- 跟humanize插件关系不大你对着cc说就可以了
- chen:请问具体是怎么实现在humanize里让cc建工
- codex goal呢？直接用humanize好像只能codex监c...
- 6月8日17:39
- 有无群友知道1000 credits能让weekly limit扩大多少
- @刘思皓做了 cgcr 调通了
- wo share 了
- codex goal claude review
- 感谢
- 6月8日17:18

---

### 6月9日

#### 原文 L36547–L36587

[回到原文件 L36547](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36547)

- 6月9日01:24
- 我觉得现在fundamentally agent和人类不align的地方在于：人类会主动的有意识的做铺垫性的工作然后聚沙成塔，
- 但是agent一般上来就干。
- 举个例子，我人类要去做一个CPU，可能我得先搜集一些benchmark suite，然后再搜集一些golden model，然后
- 再一点一点搭起来。但是agent往往上来就是module CPUTop....
- CPUTop已经在模型里面了。
- 你只是用prompt把它取出来。
- 没毛病。
- CPU本天成，prompt偶得之。
- 确实感觉模型不会先去找，参考好的
- 香港科技大学研究助理教授徐策羽:我觉得现在
- fundamentally agent和人类不align的地方在于:人...
- 设计
- 6月9日01:29
- 有没有一种可能，就是，模型脑子里都有，不需要去找这些，他都知道
- 香港科技大学研究助理教授徐策羽:我觉得现在
- fundamentally agent和人类不align的地方在于:人...
- 人类的记忆实在是太渺小
- 6月9日01:37
- "刘思皓"recalled a message
- 我觉得未来6周到10周会对以下两种agentic workflow方向作出选择：
- 1. agentic mutable dynamic workflows -- —个随着时间前进并且agents可改动的workflows (humanize3)
- 2. workflows interaction -- 少数几个workflows，但是它们之间可以有一些局部的互相交互
- 前者：我们有无限的workflows，随着时间前进，需要动态改变flow本身
- 我现在不是很清楚，到底是前者还是后者，但是我感觉6-10周之后就知道了。
- 6月9日01:39
- 组件
- 我也不知道，
- 不知道，看看历史最后会选择那一种
- 到底是动态主义还是组合主义最后占上风
- 后者：我们没有多少真正有效的flow，只需要把它们交互起来就好了
- 感觉后者比较好呀，合理呀
- 动态主义：我们需要随时间精细微调flow本身，以至于需要在无限的flow空间中找到连续的可行解
- 组合主义：真正有效的flow没多少，只需要重复+组合就好了
- 我也很好奇最后会选择哪一种，现在的确不知道，神奇得很，需要烧token试试看
- 我个人：动态主义45%：组合主义55%
- 6月9日02:12
- 之前有啥实践中动态主义能赢组合主义吗。
- 感觉就是组合，然后每个组合动态?
- 还是得实践检验真理
- 6月9日02:18

---

#### 原文 L36632–L36647

[回到原文件 L36632](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36632)

- 6月9日07:35
- cc 没有auto review 要么直接skip 权限管理好差
- 6月9日07:45
- 有呀
- 洋洋阳: cc 没有auto review 要么直接skip 权限管理好
- 怎么开启
- 6月9日08:13
- 一直都是skip，从来没用过别的权限
- 洋洋阳: cc 没有auto review 要么直接skip 权限管理好
- https://code.claude.com/docs/en/auto-mode-config
- 6月9日11:31
- 大家用cgcr的时候有什么特殊的prompt吗 还是说沿用gen idea gen plan
- 我是按照
- 描述

---

#### 原文 L36662–L36675

[回到原文件 L36662](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36662)

- 6月9日11:58
- cc给我了个建议帮我配了一坨开发常用的权限加到setting了
- Luke:一直都是skip，从来没用过别的权限
- 6月9日12:13
- 用 slock 来monitor goal感觉有点神奇，经常会出现没发的草稿，不知道为啥
- humanize-cgcr.git @刘思皓 做了 cgcr 调通了
- 这个怎么能不捧场呢
- 当AI学会“自我评审”：多智能体
- 循环如何写出 SOTA GPU Kernel...
- 让 AI的“构建-评审”循环自己
- 写出比官方基线快 19 倍的 GPU
- Kernel, 并把这套循环做成开.

---

#### 原文 L36733–L36757

[回到原文件 L36733](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36733)

- 6月9日19:28
- ultracode + goal 挺好用的
- 6月9日22:51
- 这很常见，也是rlcr使用前期经常陷入的一个误区
- 所了个长：想请教各位一个问题，在长程RLCR的时候，
- 大家有遇到类似agent会倾向于花很多时间卡住，跑...
- 你需要构建一套“探索工具”
- 而不是，边探索，边构建
- 6月9日23:09
- 后期边界收益降低可以加最多三轮或者全p2停下
- 有点元编程的味道了
- 刘思皓：而不是，边探索，边构建
- 23:31
- 我的判断(基于今晚实战,诚实说)
- omp/Opus 4.8—自主执行+判断更强:守铁律
- (没凭据就停下间、不骥)、自己抓到T1的
- nuance并正确解(flter不删、保留只读显示,不
- 是死板原做)、诚实标注没真机验的分支、没我
- 同意不磁线上数据。这正是T3这种模糊后错任
- 务要的画像。
- codex/gpt-5.5—审查/检证极强:review 精确
- 到fleline、逐条验收、翔出
- prettienconformance突现也扎实。借今晚被

---

### 6月10日

#### 原文 L36794–L36815

[回到原文件 L36794](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:36794)

- 确实
- sihao哥有没有考虑把新的workflow拆成很多个rlcr
- 为什么不能龙卷风摧毁停车场
- 我现在感觉好像所有任务都最好有详细的goal可以判断是否达标的标准然后让ai做review啥的
- 6月10日00:58
- B4RRy: sihao哥有没有考虑把新的workflow拆成很多
- 个rlcr
- 我已经是这样做了啊
- 用一个loop(claude /loop)去监控和prompt另一个loop(codex/goal)
- 其实现在问题是停止控制很困难
- 6月10日01:08
- 这感觉只有review
- 刘思皓: 用一个loop(claude /loop)去监控和prompt另
- —个loop(codex/goal)
- 意思是plan交给goal动态的做嘛
- 6月10日01:16
- goal的核心就是动态plan
- progressive plan是goal的核心设计
- 是humanize没有的
- 我是四级纠偏
- https://www.anthropic.com/news/claude-fable-5-mythos-5

---

#### 原文 L37074–L37088

[回到原文件 L37074](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:37074)

- 能确定的是当前截图里的功能存在于本机Codex.app26.602.71036，包内文案键是
- codex.profileDropdown.inviteFriend，后端 feature key 是codex_referral_persistent_invite。
- 公开更新历史里最接近的条目是**Codex app 26.602**，日期**2026-06-04**，说明新增了 Profile section的
- activity insights 和 share cards，并注明 consumer ChatGPT plans 可分享；这很可能就是这批 profile/referral
- 入口一起上线的版本。但严格说，官方没有明写“Invite a friend added in 26.602”。
- 来源:
- [Codex changelog - 26.602, 2026-06-04](https://developers.openai.com/codex/changelog)
- [Codex changelog - 26.601, 2026-06-01](https://developers.openai.com/codex/changelog)
- 这玩意就放在 usage remaining 旁边，特别容易误触
- 6月10日03:58
- 我明白了，手游追求的在线率和氪金率和现在agent是一样的
- cc 叫/passes
- 应该引入抽卡机制，概率获取最新模型的使用权限
- 6月10日04:04
- 不如这样，引入传销机制，每拉取一个下线，你可以获得他的1%周限

---

#### 原文 L37121–L37127

[回到原文件 L37121](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:37121)

- 6月10日05:52
- Loop Engineering 来了：你不再亲
- 手写 Prompt，而是写"循环"
- 循环工程：别再亲手给智能体写
- 提示词了，去设计那个替你写提
- 示词的系统所谓循环工程（Lo...
- ChallengeHub

---

#### 原文 L37904–L38108

[回到原文件 L37904](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:37904)

- 这里背后的经验我可以稍微分享一下
- 很反直觉
- humanize:opt当时设计的主要思路其实非常简单
- 就是每一轮迭代，如果迭代是反效果，就在本地维护一个错题本
- 然后避免下一次尝试错误的选项。
- 当令人非常惊讶的是，其实你不去维护这个“错题本”，你的效果要好得多
- 因为巨量的性能性能提升，往往就在错误尝试旁边。。。
- 笑死
- 刘思皓：因为巨量的性能性能提升，往往就在错误尝试
- 旁边。。。
- 如果过你维护了一个“错题本”，agents就不会尝试相关方向了，它当真理了
- 单纯错题本不行
- 会尝试相关方向了，它当真理了
- 得配 evidence score 和 decay rate
- 最近的模型对于指令遵循有时候有点过于本本主义了
- 是我后续学习到了decay rate这个概念
- 吴自华 Gabriel: 得配 evidence score 和 decay rate
- 设计好了的话还是有用的
- 对于你主动加入的内容，在compact里有极高的权重
- 当我发现，模型其实内置就有一个decay的机制
- 毕意是外置记忆
- 反正最后优化出来的设计就是不用错题本
- 我也觉得维护错题本不好。我之前想的是觉得会分散注意力
- 刘思皓：就是每一轮迭代，如果迭代是反效果，就在本
- 地维护一个错题本
- 所以humanize:opt就没用了
- 6月10日12:17
- 原来是这样啊！
- 立山用性：因为巨量的性纯性比工
- 行往就在错泪当
- 模型目己的context 就那么长
- 长任务总是会超出的
- 6月10日12:17
- 原来是这样啊！
- 刘思皓：因为巨量的性能性能提升，往往就在错误尝试
- 旁边。。。
- 我经常观察到compact几轮之后，模型还在复读我几个小时之前steering的prompt
- 明明他正在做的事情已经完全和那条没关系了
- 学到了
- 吴自华 Gabriel: 得配 evidence score 和 decay rate
- 其实最早的 OpenEvolve 里的 island 概念对于 kernel 优化这类任务是有意义的
- 刘思皓:因为巨量的性能性能提升，往往就在错误尝试
- 旁边。。。
- 不是单线探索
- 现在有自动记忆系统
- 翁大爷的狗@Rakuten:我经常观察到compact几轮之
- 和自动记忆没关系
- 是steering的prompt也应该decay
- 我也观察到这个现象了
- 吴自华 Gabriel: 其实最早的 OpenEvolve 里的 island
- 概念对于kernel优化这类任务是有意义的
- 非常神奇
- fot
- 非常神奇
- 居然真的“失败是成功之母”
- 路线本身可能是对的
- kernel探索空间比较大
- 只是很容易做错
- 但是因为一些细节没搞对，导致暂时看起来退化了
- 青霉素就是失误发现的
- 就kernel 优化其实比较重要的是想清楚一个路线的理论上限
- 我还是做arch research，但是肯定走humanize这套路子
- 智谱黄睿博: sihao接下来在nv会专注算子了吗
- 有的拥核的意思了cluade这一波
- "刘思皓" recalled a message
- 优化的话应该算小了吧
- 如果理论上限都达不到的路线，可以提前放弃
- 设计上探索空间比较大
- humanize for算子找@L.Zhu
- humanize for 架构找我
- 一般用什么方式去证明上限
- 吴自华 Gabriel: 就 kernel 优化其实比较重要的是想清
- 楚一个路线的理论上限
- 6月10日12:21
- speed of light
- 看bound在哪个器件呗
- 比如大力出奇迹 sclaing law的极限
- 不同的设计bound的点可能就不一样
- 理论上限够高，只是暂时实现不理想的，就还有探索价值
- 是的
- 看起来退化了
- 很多时候其实就是Agent实验没做对，然后他就觉得行不通
- 他好像不太会，就是去研究实验哪里做错了
- 数学建模后画出函数图像
- opus就特别喜欢pilot一下，然后就行不通，尝试了很多，但是没有一个方法做下去，都觉得不行
- 吴自华Gabriel:如果理论上限都达不到的路线，可以
- 提前放弃
- 我让它写通算融合kernel就是，还是需要人类专家强干预
- 吴自华Gabriel:但是因为一些细节没搞对，导致暂时
- 看起来退化了
- 智谱黄睿博:我让它写通算融合kernel就是，还是需要
- 人类专家强干预
- fused kernel这种东西感觉还得训练
- 我坚定相信kda的成功是站在巨人肩膀上
- 现在就是一个能把握每一步大方向的人去guide才会很快
- 6月10日12:28
- 可以借鉴这个论文 Runtime Governance for AI Agents: Policies on Paths》,arXiv:2603.16586→ https://
- arxiv.org/abs/2603.16586
- 洋洋阳:
- @刘思皓
- 我这个后面又改了一下
- 因为我发现codex会挂
- 原理来自这篇论文
- 也能超过baseline的（
- B4RRy:现在就是一个能把握每一步大方向的人去
- guide才会很快
- 我那一班还专门测试了一下后来发现直接提示词够我用就没上生产用
- 我的task—般review—轮就够
- 我懂了
- B4RRy:现在就是一个能把握每一步大方向的人去
- guide才会很快
- 因为大方向都是人算出来的
- 6月10日12:30
- 不是大方向没有语料
- 而是intent 缺少语料
- intent是可以从pr和commit里训出来的
- 现在的LLM更多是在模仿已有的成功轨迹，然后一定程度上反推intent
- 所以这是我觉得kda成功的关键
- 但是不是真正的intent
- 如果部分情况能明白地告诉我，比较危险，降智到4.8为什么部分情况又不明确地告诉我，只偷偷掺shit呢
- 我能不能理解为，其实它没有偷偷地掺只是在诈唬（一种妄想
- 6月10日12:36
- 问题是你敢赌吗？它无所谓啊，反正钱已经赚了
- 12:38
- PI
- 一号法新件社分·设治行个做·话一的证做
- ±,t = q - 3,it-23 × 8,1
- I=开疑分(提是信的T,知o0,从0开始。
- 据，08批距八折，越大源动达路小起量
- (-2.正册批0.
- 1面出滑量+出手平组再高+图止.
- ±一源(y-0A干倍频-1.#止通-5:
- 08=0-2
- 20
- 08=20+2 36
- 一号法新件键分·股分行个做·请一步科证理
- 1,t = q - 3,it-53 + 8,t
- s=开疑分(题是信的T,知a0,从0开始。
- 别，0.8批距织八折，越大源记九路小超量
- E.
- (-2.正R0.
- 1 酯运滑值+出手(平组再高+图止.
- 北一测(y=0A干传频-5.#止湖-5:
- 逝步半7睡
- 20
- 08=0-2
- 08-20+2
- 36
- 4.0
- 跟人一样不能犯一次错就打死永远盯在耻辱住上
- 走一遍(γ=0.8,干预阈=3,终止阈=5):
- 这步干了啥
- 算式
- v_t
- 0.8×0+2
- 2.0
- 偏题
- +2
- 0.8×2.0+2
- 3.6
- 又偏
- +2
- 还偏
- +2
- 0.8×3.6+2
- 4.9
- 0.8×4.9-2
- 自我纠正
- 1.9
- 0.8×1.9
- 1.5
- 正常
- 0.8×1.5
- 正常
- 1.2
- 四个性质一银看全：单步不触发(步1)、持续才触
- 发(步2)、纠正能救回(步4)、干净步自动遗忘(步
- 5-6).
- γ怎么理解:0.8等于“每步旧账打八折”约3步衰
- 减一半(0.8°=0.51)。要它记仇就调高(0.95),要它
- 健忘就调低(0.6)。
- I assume the intention is not only prevent other model inventors from synthesising model but also actively
- hurt them in case they try.
- 饽饽博:如果部分情况能明白地告诉我，比较危险，降
- This way they can collect their money and give them bad training data
- 固定策略的逐步评估,若每一步都低于干预阈值就测不出drift;把逐步评估接到长程行为监控上,是一个尚未解决的设计
- 问题。需要：带衰减累加器
- 洋洋阳: 可以借鉴这个论文 Runtime Governance for
- Al Agents: Policies on Paths》,arXiv:2603.16586 ...
- “纯错题本”是退化形态——它把所有条目当成等权 + 永久。evidence score 修掉”等权”,decay rate 修掉”永
- 久”,合起来把一张列表变成一个带遗忘的证据累加器(leakyintegrator)。
- yes,i second you
- Simon: This way they can collect their money and
- give them bad training data
- 6月10日12:42
- 然后错题本本身还需要LLM Wiki那样的整理和建索引
- 跟flow并行的另外一条线
- 目前阶段的完全体 harness = flow + memory + toolbox
- Ilm wiki 增加一层索引派生产物也带来双写飘移风险 我还是markdown+grep党

---

#### 原文 L38221–L38232

[回到原文件 L38221](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:38221)

- 但也只是初步感觉，已经被限速了，没法继续感觉
- 各位佬想请教下，Pi+omp会比cc好用吗，humanize做了Pi的适配不
- harness各有千秋自己赛赛马就知道了
- 6月10日16:47
- ？omp里面就有pi啊
- Hayden: 各位佬想请教下，Pi+omp会比cc好用吗，
- humanize做了Pi的适配不
- 6月10日16:54
- 嗷嗷，我还没用过omp，以为是Piagent的一个plugin
- 1900:?omp里面就有pi啊
- 态度挺好本来要骂两句的

---

#### 原文 L38238–L38304

[回到原文件 L38238](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:38238)

- omp就是pi上面搭建的吧
- 是的
- 小龙虾也是的
- 6月10日17:06
- 啊阿
- 1900:小龙虾也是的
- 其实我一直挺好奇的为什么小龙虾没让pi火起来
- 小龙虾刚出pi作者就出来宣传演讲了
- 6月10日17:13
- OpenClaw 背后核心框架 Pi:好的
- Coding Agent 应该让用户来决定...
- 「大模型天然就知道coding
- harness是什么，不需要堆加太
- 多东西。」
- Founder Park
- 6日10日17:21
- 有人尝试过这个吗
- 6月10日17:29
- 真的有这个字段吗
- 这参数的意思真不是拒绝 fallback然后就断了
- 这个需要npm版本的，它会修改cli.js
- 哦改了源码
- 那我觉得合理
- 6月10日17:34
- 但是小心 cache 爆炸
- aude Code上了一个
- 和请求的不一致，就
- 不错
- 1900:OpenClaw背后核心框架Pi:好的
- Coding Agent 应该让用户来决定需要什么
- 6月10日17:44
- https://github.com/ninehills/blog/issues/162这套也还不错，仅供参考
- Reiko:不错
- pi agent的
- 原来如此
- 1900:OpenClaw背后核心框架 Pi:好的
- Coding Agent应该让用户来决定需要什么
- 6月10日17:50
- 奇怪，没翻到这条
- 6月10日18:22
- fable用得好快
- 一个cc max20x跟本不够蹬
- 垃圾活派出去
- 6月10日18:45
- 怎么派 它特喜欢自己开subagent
- 有没有做agent的
- 内置prompt是不是写了尽量多用token 能read尽read
- 6月10日18:46
- 江海万里
- 心中念你
- 便不觉遥远
- 最近一直搞啊 supervisor + specialist
- 我没有特别有难度的物理问题问它怎么办我的都是Ilm问题啊靠
- 为啥呢
- 饽饽博: 内置prompt是不是写了尽量多用token能
- read尽read
- 今天给友商讲agent产品sku
- 也可以手动干预
- 做的是重框架轻模型
- 结对子啊一起plan
- 结果导向
- 我让它upgrade memory，把我整个项目前置文件夹的所有memory都读了一遍再update
- 彻底解决了旧memoryout of date问题
- 因为每次都是新的
- mgeemt

---

#### 原文 L38369–L38392

[回到原文件 L38369](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:38369)

- progressive plan
- 可能是懒癌晚期有些后续设计依赖对前置任务输出结果的分析
- 好的研究下，谢谢
- Joe布衣: progressive plan
- 6月10日21:44
- https://alignment.anthropic.com/2026/automated-w2s-researcher/
- 这个老文章的这种自组织multi-agent的范式有人尝试过吗？求分享一下感受
- (已经是一个半月的老文章了
- 6月10日21:52
- 原来还有个agents
- Claude Code v2.1.170
- Opus 4.8· ~/Garden/llm_app/hi_partner
- 0 awaiting input . 1 working . 1 completed
- Working
- *介绍下agents的本质原理介绍下agents的本质原理
- Completed
- agents have 3 modes: auto-dispatch by me,
- * agents usage guide
- 6月10日21:58
- 我也好奇
- 香港科技大学研究助理教授徐策羽:这个老文章的这种
- 自组织multi-agent的范式有人尝试过吗？求分享一...
- 6月10日22:04
- fan in/out

---

### 6月11日

#### 原文 L38896–L38912

[回到原文件 L38896](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:38896)

- 阳导进化论
- 1. omp 执行 / codex 审查的双层网是今天最
- 大的质量来递：oodex三轮审查各抓一个真
- bug(工具描述残留10、floor 误算child、
- scheduled 软超时冲突),，全是会上生产的那
- 种;omp也反向抓过我草稹漏的 prompt残
- 留。
- 2. goal 文档驱动 +状态全落盘：三次断网、一次
- 压缩、agent 反复重启，工作零丢失——因为
- SoT 在 docs/orchestration/,agent 会话是
- 一次性的。
- 3. 诚实文化兑现:E2E主动修正了自己“200×”的
- 夸大数字(顺序探针假象→GIL真相)，这个修
- 正直接塑造了Step2的技术决策。
- 三、教训(都已固化进memory)
- 1. T7 round1 返工:观测值 5 < 上限 10 的矛盾就
- 在手里却没人追问→verify-binding-

---

#### 原文 L39221–L39246

[回到原文件 L39221](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:39221)

- 装“边养”《每个项目自己的审批线和仓库绪构，用你已有的
- Write(-/.claude/skills/cto-erchestration/sKILL.md)
- Wrote 1is lines to ../../../../.clavde/skills/cta-are
- 2 name: cto-orchestration
- 3 version: 1.0.0
- 评审)混合开发，goal 文档规动，watcher监拉、对
- 编排者onp/codex 去”poal 模式游发曾
- satadatà:
- requires
- bina: ["tmux", "oap", "codes"]
- CTO Orchestration = $ agent 蓝出开发编
- 帮我做了个skill出来
- 方法学还没完成，给了我一个plan正在实现中.…….
- Write(-/.claude/skills/cto-erchestration/sKILL.ed)
- Wrote 1i5 lines to ../../../../.clavde/skills/cta-arc
- name: cto-orchestration
- version: 1.0.0
- 评审） 混合开发，goal 文档驱动，matcher 监控
- goal 模式游发
- 编排者、‘温onp/codex 去”
- setadata:
- requires:
- bins: [tmux", "oap", "codes"]
- CTO Orchestration - $ agent 蓝出开发编
- 帮我做了个skill出来
- 我是搭了一个框架

---

#### 原文 L39250–L39267

[回到原文件 L39250](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:39250)

- 6月11日18:35
- https://www.icagenthub.com/我让他帮我改进这个flow
- @奇迹的闪光迪迦
- 我立马严肃学习并炼化之
- 我让它一边按照这个flow给我写demo，一边收集不足和需要改进的地方
- 6月11日19:06
- 感觉现在最费时间的就是 skill/flow 调优
- 6月11日19:26
- cc里面接非claude model能否用dynamic workflow?有人试过吗?
- 6月11日19:48
- 值得记一笔的模式:这是codex第二次抓到”
- LLM产出进入结构化管道前缺溯源校验“类的洞
- (上次是记忆提取的PI契约，这次是引用幻
- 觉)—一这类”生成内容当数据用”的接缝以后在
- goal里要默认点名为评审轴，我会回写进cto-
- orchestration skill 的评审模板里。
- Ran 3 commands >

---

### 6月12日

#### 原文 L39379–L39402

[回到原文件 L39379](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:39379)

- https://github.com/SihaoLiu/rem6
- suing goal (16d 0h
- 今年过年的时候，我还在折腾让AI怎么一次性写完20万行代码而感到困惑
- 现在你该纠结怎么验证这20万行代码有效性
- - 带验证的长程循环
- - 有固化的workflow做流程锚定
- - 带全局视野的监控循环
- 确实
- 林桢杰:现在你该纠结怎么验证这20万行代码有效性
- 6月12日01:21
- 然后你生成验证这20万行代码有效性的40万行代码
- 我感觉依旧还是一个循环
- 构建循环 + 监控循环 + 审计循环
- 三驾马车
- 现在你怎么验证码这40万行代码有没有验证完这20万代码
- 然后写80万行对吧
- 6月12日01:22
- 不需要完全验证
- 黄金回旋JOJO
- "刘思皓"recalled a message
- 没我还是那句话，AI自动化工具并没有减少所需的智力总量
- 只是改变了智力密度分布
- 收敛

---

#### 原文 L39571–L39584

[回到原文件 L39571](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:39571)

- 翁大爷的狗@Rakuten:所以我现在的感受是mythos可
- 因为当前humanize群满员了，后续会按照发言活跃度/质量管理一下
- 6月12日02:55
- 我也在做self improvment的agent 但是这个loop现在不太好做。。
- Reiko: 这个有点搞：这轮搞混的地方是：一些agent
- 在被要求“设计 evaluation”时，自己创建了所谓c...
- 很同意
- chen:我也在做self improvment的agent 但是这个
- loop现在不太好做。。
- 我试过好多办法总结可以说是记录错误然后用某种办法在某个实际注入这些记录的错误
- 但是改善非常非常有限
- self improvment的agent 肯定是最关心的
- 但是通用上没有好的架子
- 但是有梯度下降过程的文章

---

#### 原文 L39592–L39602

[回到原文件 L39592](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:39592)

- 不够稀
- 推荐这几篇·SimpleMem: Efficient Lifelong Memory for LLM Agents··MemEvolve: Meta-Evolution of Agent
- Memory Systems
- ·SkillOpt: Executive Strategy for Self-Evolving Agent Skills
- 感谢
- 我在看这个文章
- Phy  -   P P     :    sm
- 他这里研究LLM的一些方式和思路很有意思
- 感觉在做agentic的事情或者别的啥可以adapt一下
- 我感觉应该希望加入bitter lesson之后要么 1. 减少原来分布的variance 2. 把一些明显的bias error干掉
- Titans: Learning to Memorize at Test Time其实想干类似这个的事情

---

#### 原文 L39655–L39670

[回到原文件 L39655](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:39655)

- 那怎么让他能有新功能的堆？
- 我发现tmux-server是最牛逼的multi-agent mcp server
- 我让我的codex把tmux window当瞬发sub-workflow来用
- IT JUST WORKS
- 6月12日07:14
- 当时人类学用tmux session开做agents team有点奇怪
- 因为它把tmux-seryer作为subagent沟通的桥梁
- 但是如果你把tmux-server的window，作为spawn—个长程workflow的瞬发环境
- 就特别合适
- 最关键的是tmux window天然就是一个全transcript环境
- 6月12日07:19
- 这样顺便还解决了meta-workflow没法走订阅的困难
- 6月12日.07:30
- 导致any agents talks to any agents
- 然后就会导致沟通混乱

---

#### 原文 L39804–L39813

[回到原文件 L39804](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:39804)

- Eden: 不返回thinking token，这下没法蒸了
- 4.8 就有了，cc 就是自动记忆
- 洋洋阳: f5 有点自成长那味啊 不知道token贵不贵有
- 点622想付费的感觉了
- 非常熟练的读写记忆
- 我写了一个webui，可以看他用了哪些记忆，就可以看到他读写了十个
- 一个判断给你：离10min只差临门一脚,而且这一
- 脚(主循环LLM瘤身)是改 prompt/减轮次的活，
- 比再写一个lever轻。但要不要为这-1min再投
- 入,可以等L3实测数据出来再定——也许修完

---

#### 原文 L40085–L40101

[回到原文件 L40085](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40085)

- 我还以为牢雪复活了。
- 我现在主要是把精力放在 https://github.com/PolyArch/oh-my-humanize 上面
- 6月12日12:57
- kda是什么
- 6月12日12:58
- @L.Zhu 你宣传不到位啊哈哈哈
- 群公告都是
- https://github.com/PolyArch/oh-my-humanize
- https://github.com/mit-han-lab/kernel-design-agents
- 6月12日12:57
- kda是什么
- 蛤.
- oh学习一下
- kda = kernel design agents
- https://github.com/mit-han-lab/kernel-design-agents
- 现在主要让f5写goal了

---

### 6月13日

#### 原文 L40327–L40344

[回到原文件 L40327](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40327)

- 洋洋阳: MacPro没gpu一下子到分钟级
- 你现在是claude /loop监控omp的/goal?
- 从我的 AI 们大混战从 public benchmark 加权算分的*不可靠*结果来看，fable 在开脑洞这件事上遥遥领先，review
- 略超 gpt-5.5，build 不如 opus(
- 没用loop 挂了个watcher
- 我读得最舒服的还是 Kimi(
- :之前看fable5写的高考作文，感觉文笔巨好
- 我现在翻译先过一次Kimi，GLM纠错，然后再重复一次，翻译腔就比大多数科技读物轻了
- 6月13日01:41
- 话说ohmyhumanize现在的用法是什么，看了一眼下来
- readme 感觉还是 omp 原本的?
- 用法其实就是“$ 帮我看看oh-my-workflow”的mutable workflow这个功能要怎么用
- 我还在做长程测试
- 感觉还是有点Bug
- 主要是它不怎么触发修改workflow本身这件事
- sihao哥测试workflow一般是什么任务呢
- 一个真实任务模拟环境
- 我手头只有这种无趣的任务，但是确实又跑的很长

---

#### 原文 L40349–L40365

[回到原文件 L40349](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40349)

- 调-6-个保留节点-GPU-释族
- 新版接口对齐验证
- npleted
- 真实环境我一般就干类似 rem6和lzvm这种项目
- 测试项目一般干大翻译
- 我感觉大翻译项目这种事情
- 看起来是哥加速任务
- 翁大爷的狗@Rakuten:
- 6月13日01:45
- 挺适合做长程任务的压力测试的。
- 主要是有一个大问题
- 一个针对长程任务专门设计的开发工具
- 它本身的迭代周期就很长
- 哎也确实
- 这个很难做啊，你本身面向的任务是长程任务
- 你获得反馈的回路本身就要求是长的
- 分阶段么？

---

#### 原文 L40370–L40425

[回到原文件 L40370](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40370)

- 核心区别提信号源、takee经济、和存活解碑三件事
- 1. 信号源不用—我们要的信号harwess 结不了。
- capture-pane  (onpr[esc]. codeenesc to interrupt),wato
- 2.Taken 经济。atchar 是shell 那本在轮角，Tick 带 token:只在
- 只酒费组论。
- 3. 百温解辑.
- thux 会退和watihe 都活在营的进程之外：监的合话期了/
- 还在盯，状态可性复，知果编排速错全在教的1o0p里，我更那业死，
- 什么时保用我自己的 toop 更对：等待的是harness 通跟不到的外那状态
- @刘思皓
- 你这个claude总结的不好
- claude /loop监控codex/goal的本质有三点
- 1. 看transcript
- 2. 看产物变动
- 3. 看git commit
- 它被禁止看实际的代码
- tick
- token;
- 每次情
- 个20分排的任务我得被无票义映醒四五次，
- 3.08解码.
- tmux 会送和 watohep 都送在我的进程之外：监的合话期了/%
- 还在盯，状态可性复，知果编非速错全在教的1o00里，我见那业死
- 什么时保用脱自己的toop 更习：等待的是 haroess 通跟不到的外那状态
- 不一定是监控goal任何指令都可以监控
- 是，它是个进度监控
- 不是个代码审查
- 也不是building loop
- 6月13日01:50
- 它本质的作用是：1. 感受时间流逝的痛苦；2. 在大方向上面保持正轨；3. 帮助内部loop跳出局部最优
- 嗯它还经常复审
- 经常复审这件事我觉得得关掉
- 这个需要 prompt enable 吗？
- 洋洋阳: 嗯它还经常复审
- 还是它会自动
- 偶尔吧
- 自启动
- 6月13日01:51
- 我甚至有点想禁止它看第二点
- 刘思皓: 1. 看transcript 2. 看产物变动3. 看git
- commit
- 它应该只看git diff和transcript
- codex review出来它设计的goal问题
- 我很少看到loop里他会主动复审
- 一开始就设计的有问题会触发复审貌似
- 哦哦IC
- cool observation
- 反思力挺强f5
- 还有一定灵活性 有时候一行代码 也会自己改掉
- 不派人
- f5用下来最和我意
- 整体严谨
- cc还特别喜欢换三个种子反复跑，一点用没有
- @Luke ？宁也在群里哇，
- 流程指令遵循的非常好
- 写代码属于 = 开发

---

#### 原文 L40490–L40514

[回到原文件 L40490](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40490)

- 感觉很正常
- Reiko:一个测评 skill的 skill。角色混乱，连初版的基
- 础功能都失败了
- a\再恶心也不影响我一边骂一边用，然后做新的东西出来背刺它
- 互相伤害呗
- 6月13日02:40
- 5.6加油蒸我的数据
- 我还是觉得现在这个阶段workflow得用多个独立的ai(
- 因为ai发现错误容易改正错误难
- 必须要把找错误和改错误这两个事情分开
- 让A不断的鞭打B
- 你指的是不同源的 Al，比如说 gpt 和 claude，还是指的不同的 Agent 或者 Session?
- B4RRy:我还是觉得现在这个阶段workflow得用多个独
- 立的ai（
- 不同session
- 伊辛模型
- 有简短的上下文
- 本身是很不容易跑偏只负责抓错误骂人
- 发现错误简单所以用很少context就能完成发现指出错误
- 修改错误困难往往需要大量的尝试和上下文很容易跑偏
- 这为啥和Ising model有关系
- 林桢杰:伊辛模型
- 我完全同意，我其他的 workflow就是按照这个设计的
- 耦合程度
- 没 get 到，Ising 是临近相互作用

---

#### 原文 L40525–L40541

[回到原文件 L40525](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40525)

- 可以玩一个东西，不知道有没有试过
- chain of agent?
- "B4RRy" recalled a message
- It would be indeed interesting to have serious benchmarks. I have a feeling that most public benchmarks
- are completely useless and test for trivial or irrelevant to reality tasks.
- L.Zhu: maybe 可以做—个 review 的 community?
- 若干个模型一起 review 一个 impl
- 有意思的想法
- 但是这里温度估计不太有用
- 这个温度蛮像物理的温度的，我感觉
- indeed .. when humanize brings people flow-level agents, existing benchmark still focuses on single-
- prompt model-level agents
- Simon: It would be indeed interesting to have
- serious benchmarks. I have a feeling that most p..
- 现在模型是
- token -> backbone -> logits-> sampling-> Im head?

---

#### 原文 L40593–L40608

[回到原文件 L40593](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40593)

- token 序列 注意力强弱明显
- 改不了因为上下文把特征耦合了
- 我觉得未来一年会有无数的paper，就因为上了Auto-research，Agentic-Loop，然后性能就好XXX%
- 因为你写出一个Loop其实很简单
- 加一张图
- 因为我人干预的时候agentic的东西都不一定可以直接写对正确的代码
- 6月13日02:58
- "刘思皓" recalled a message
- 那他们实验结果怎么好呢
- Is the humanize version for omp already testable on some experimental branch
- 先进生产力和落后的评审制度的矛盾
- 我之前还脑洞了一个方向，把行为主义心理学的论文迁移过来。这个也适合auto
- I am testing on my local machine for the past 2-3 days
- Simon: Is the humanize version for omp already
- testable on some experimental branch
- fixing a lot of bugs

---

#### 原文 L40614–L40641

[回到原文件 L40614](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40614)

- past 2-3 days
- Tool for long-running tasks needs to run for long^2 time
- 6月13日02:59
- True
- Since I switch to omp it seems more easy for me to put agent into loop where it' s fanning out subagents
- aggressively and works long time
- I am happy to have some beta testers, but I think the best way is to let me test on my end, since I got the
- shortest feedback loop
- Before I use codex
- 刘思皓: I am happy to have some beta testers, but
- I think the best way is to let me test on my end, ..
- The code is always open-source btw: https://github.com/PolyArch/oh-my-humanize
- I guess AMD/Intel will go up by a lot
- I am really CPU bound now
- https://x.com/_can1357/status/2065284468311461895
- https://blog.can.ac/2026/06/10/snapcompact/
- 模型能自己复读机订正因为error的注意力强了，解码大哥对上眼了
- 都是注意力的错
- 都是注意力的错
- L.Zhu invited MyZ to the group chat
- max is error
- start 50 loops at a time kills my machine
- I guess OMP will be the next vscode
- makes multi-agentic harness dev very easy
- I am very happy with it. It' s for me first time that I see real productivity boost with ai because of easy
- triggering of subagents and long running task
- the model bridging level work is very tedious and boring
- thanks the author

---

#### 原文 L40654–L40664

[回到原文件 L40654](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40654)

- 刘思皓: makes multi-agentic harness dev very easy
- I used omp + oups4.8 about a week, still alive
- Simon: Can we use Claude with omp? I heard that
- is forbidden or restricted in some way to user ot...
- 6月13日03:11
- 模型层面的递归
- 洋洋阳: I used omp + oups4.8 about a week, still
- 简单做法，发现错误你把找到错误的段复制三遍
- 不用换模型

---

#### 原文 L40796–L40827

[回到原文件 L40796](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40796)

- Reiko:就是从动力系统的角度来理解loop
- 比如在humanize里面的rlcr后期，观察到的agent来回振荡摇摆
- 对，这些都是动力系统中常见的现象
- 所以群里面有讨论过其实一个好的loop
- 其实应该上PID控制什么的
- 然后我在humanize后期，其实反思过，为什么humanize在长程开发上面设计的不如codex/goal
- 6月13日06:05
- 原因其实就是：
- humanize的goal-tracker，本质上是一个积分器，是一个I
- 然后codex review本质上是一个P tracker
- 但是humanize没有设计D微分器，而这个刚好就是codex goal设计的那个progressive planning
- 很好的说法
- 所以我感觉agenticharness这套东西，得把本科的时候学的那一套信号系统，过程控制理论都复习一下
- 6月13日06:11
- 我好像发现我们关注点不一样的地方了，我还是站在self-evolve的视角。
- 群聊的聊天记录
- 刘思皓:我觉得未来6周到10周会对以下两
- 种agentic workflow方向作出选择:1.
- agentic mutable dynamic workflows --
- 一个随着时间前进并且agents可改动的...
- 聊天记录
- 6月13日06:14
- 我觉得self-evolve的视角也没有什么问题，我现在在做的humanize3也是这么做的
- 到底是让workflow自己去evolve，在连续的可行flow空间中自我进化
- 还是规定几个基本的flow结构，之后只是scale和排列组合形成更加复杂的flow去适应不同的任务
- 我也不知道，得大规模尝试一下
- 有意思
- 太神奇了
- 组合主义有一个好处，就是“先进过程控制系统”里面有无数的在过去几十年里面被验证过的结构可以搬过来。
- 但是动态主义也有一个特点，就是过去的先进控制系统，没法改这个系统本身，但是现在agenticflow可以改它自
- 己，或许能有不一样的东西。
- 现在有哪几种不同的flow啊？

---

#### 原文 L40832–L40843

[回到原文件 L40832](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40832)

- 刘思皓:但是动态主义也有一个特点，就是过去的先进
- 控制系统，没法改这个系统本身，但是现在agentic fl..
- 怎么观察的
- 刘思皓:但是humanize没有设计D微分器，而这个刚好
- 就是codex goal设计的那个progressive planning
- 看一下群公告里面那个wiki
- Luke:现在有哪几种不同的flow啊?
- 我每天观察Claude code的goal，我啥都没观察出来，我只能我只知道他创建了一些任务完成，然后完成了这些任
- 务，根本没有发现它的任何特性
- ideally of course we'd expect agent to self correct/change direction in favorable way but we need to be
- careful to ensure it doesnt use the freedom to perform reward hacks.
- Simon: i see danger of divergence/reward hacking

---

#### 原文 L40852–L40900

[回到原文件 L40852](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:40852)

- Wirll/ee
- MCP
- 其实我一直有个疑惑，reward hacking 是任务过于复杂才会更高概率发生的事情吗。如果是的话，选择合适难度的
- 任务，就可以把它压低到“无害”的水平
- Simon: ideally of course we'd expect agent to self
- correct/change direction in favorable way but w...
- r  s t  r       r s    cck
- Reiko:其实我一直有个疑惑，reward hacking 是任务
- 过于复杂才会更高概率发生的事情吗。如果是的话，...
- 所以根据你的经验是：它和任务难度的相关性不大？
- Simon: in my experience agent is very capable of
- finding extremly elaborate and hard to detect wa...
- i would say it occurs mostly when you push agent to improve metric M and agent gets lazy/runs out of
- ideas. to make user happy he will try to find elaborate ways to cheat M.
- of course we can try to design M such that it is very hard to hack and gain advantage that we can let agent
- wo                ce.
- Reiko:所以根据你的经验是：它和任务难度的相关性不
- 大?
- 我觉得这个mutable workflow说不通。。。现在workflow和类似的工具本身就是将agent的部分行为和逻辑以程序
- 的形式表达出来，如果你希望agent一边跑一边改，那本身和reactloop+code act之类的没有什么理论上的区别了
- 刘思皓:[聊天记录]群聊的聊天记录
- I see
- Simon: i would say it occurs mostly when you
- push agent to improve metric M and agent gets ...
- for example something that often happens in gpu programming is for agent to remove certain barrier /
- fence etc. it may pass M millions of times corectly so he will never observe it. but it introduces race
- condition which of course we don't want in production.
- 6月13日06:36
- 我说实话我也没有很说服我自己是不是真的需要mutable，所以我现在的设计是，放一个监工loop，让它判断是不是
- 真的要改workflow。
- 至今为止还没有触发过
- noti0na1:我觉得这个mutable workflow说不
- 通。。。现在workflow和类似的工具本身就是将age...
- 我考虑这样一个场景：
- 1. 在项目开始前需要大规模探索，就需要并行点子生产机-- 参考humanize的parallel gen-idea
- 2.项目初期，由于工作耦合度低，需要并行Builder，弱reviewer--参考/goal
- 3. 项目后期，需要强reviewer -- 参考原版 humanize
- 但我觉得本质动机是存在的，至少这种场景是合理的
- 刘思皓： 我考虑这样一个场景：1. 在项目开始前需要大
- 我现在的设计是，禁止agent边跑边改，但是如果它想改，必须经过我(人类)批准
- this seems useful to me to avoid case where agents get in some strange state and go completly crazy
- (which happens sometimes to me after long and difficult work)
- 刘思皓：我现在的设计是，禁止agent边跑边改，但是
- 如果它想改，必须经过我（人类）批准
- 6月13日06:41
- 工作流不是一成不变的，这件事我觉得humanize的issues里面已经高度证明了。
- 现在难点就是：你怎么设计一套自动系统，让flow能够自己产生适应，怎么去搞adaptive
- 6月13日06:51

---

#### 原文 L41050–L41065

[回到原文件 L41050](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:41050)

- 但是不是写代码了..
- 洋洋阳:这不是写代码的模型写代码小事派小模型干
- 数学太强了
- 6月13日10:24
- 我是有性能优化和对齐...
- 我做flow时fable5会主动发现gpt5.5 review没发现或者漏掉的地方
- 自进化真的不是因为 claude code memory吗？我 opus 也有观测到类型行为
- 洋洋阳: 自进化很强
- 我一直开着ultracode用
- 吴自华 Gabriel: Fable ultracode 很好
- Anthropic发布声明称，美国政府发布出口管制指令，暂停所有外国公民对人工智能模型Fable 5和Mythos 5的访问
- 权限；访问所有其他Anthropic的模型将不会受到影响。
- 反思能力指令遵循该动手该停下用下来至少很合我意
- 刘家昌: 自进化真的不是因为 claude code memory
- 吗？我opus 也有观测到类型行为

---

#### 原文 L41290–L41302

[回到原文件 L41290](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:41290)

- 提前量都不给这有点坑
- humanize gen plan
- 用 Claude code 的 goal
- 也会写入.humanize
- rcr
- 应该
- humanize肯定已经被A炼化了啊
- 我以为不会写入
- 6月13日11:13
- 确实，完全炼化了
- 今年一月份哪来的超长程任务的trace
- ·“为啥review没抓到”→根因:eval探测器与
- 生产探测器两套从没并排比、生产路由代码

---

#### 原文 L41306–L41325

[回到原文件 L41306](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:41306)

- override)收口入库。
- memory全部更新到位(012+ping-pong教训+
- 根因纪律+分工铁律)。要我现在做收工复盘
- (cto-orchestration §5),还是你先去 review 这几
- 个PR?
- Add feedback..
- </> Code
- 流程加持看4.8了
- 3. 评审 ping-pong收口法:codex 倾向一次揪一
- 处措辞,011磨了4轮——破法是编排者全局
- grep 同类残留一次给全清单 +复审 brief 明
- 设达标线(实质声称vs 描述/免责)。
- 4. 跨分支治理冲突:三个eval 分支都改
- ACTIVE_CONTEXT/roadmap/archive-
- README→ additive 冲突。rebase 串线+
- 超集解法可控,但下次同期多 workstream,治
- 理文档的并发编辑要预想到。
- 说codex挤牙膏？
- Our model is

---

#### 原文 L41399–L41434

[回到原文件 L41399](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:41399)

- 6月13日12:08
- humanize混brainstorming和grill-me的context产plan
- 刘诗楠: 现在你的主要flow是/goal + claude监工吗
- codex goal
- 然后claude监工
- 而且我意识到一件事
- skill无非就是混入一段上下文+一些脚本
- 所以现在我都不安装skill
- 我也。模型能力提升了，skill没有用了
- 刘思皓: 所以现在我都不安装skill
- 我感觉superpowers里面好多东西过时了
- 好，我也试试这种flow
- 刘思皓: humanize混brainstorming和grill-me的
- context产plan
- 只有brainstorming和tdd还有用
- Sihao certified，必属精品
- 也不过是workflow的一部分。不如说workflow有用
- 瞬时抓skill，而不是本地持久安装
- claude 监工是开 codex subagent 嘛
- 刘思皓: 然后claude监工
- 不是
- 直接把这个截图丢给你的cli炼化
- 之前defer loading也是这个意思
- 刘思皓: skill无非就是混入一段上下文+一些脚本
- 你在一个tmux pane里面跑cx
- 当时是defer load tool
- 现在是 skill 了
- 6月13日12:14
- 是渐进式披露嘛
- 我可以把这个放到 issue里吗
- 刘思皓:
- 只给一个 skill的描述 调subagent搜最后需要的skill
- DOG
- 我发现本地持久安装还是有点费上下文
- 方便查看
- 确实

---

#### 原文 L41453–L41506

[回到原文件 L41453](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:41453)

- 12
- 并行+/fast，再加上你上次talk讲的dynamic serving optimization
- 确实
- 长程任务有个极好的优化点
- 就是workflow固化之后
- 最后这个很insightful啊，但search space超级大
- https://github.com/PolyArch/humanize/issues/213
- Horace: claude 监工是开 codex subagent 嘛
- 推理侧可以做非常长的speculative
- 不过我只有claude 会员，所以是监督claude goal
- 我打赌oai和人类学绝壁在做
- 刘诗楠: 最后这个很insightful啊，但search space超级
- 是的，没理由不做
- 之前有群友搞了个fork的版本，就是https://github.com/JerryLookupU/humanize-cgcr.git
- Luke: 不过我只有claude会员，所以是监督claude
- goal
- workflow都固化了，你可以做一个超长的预取
- 哪个 search space超级大?
- 刘诗楠: 最后这个很insightful啊，但search space超级
- 刘诗楠:之前有群友搞了个fork的版本，就是https://
- github.com/JerryLookupU/humanize-cgcr.git
- "Luke" recalled a message
- 6月13日12:21
- 我上次那个talk最后有讲
- Luke: 哪个 search space超级大?
- 就是你workflow一旦固化之后
- 有回放吗，听一下。
- 推理侧能做很多缓存和预取之类的优化
- 你翻下聊天记录
- 有的，b站nice学术
- Luke: 有回放吗，听一下。
- 根据workflow优化serving pipeline，你的KV management, spec decoding, phase-aware的分离、GPU通信，这
- 些能做的组合太多太多了
- Luke: 哪个 search space超级大?
- //【¿   ：f】
- BV1bhEi6YEhE/?share_source=copy_web&vd_source=916ec288666cc4f25e592c2da832f626
- lightgbm
- 长程任务的本质是啥，其实我购买了大模型公司的turnkey服务
- 都turnkey了，你能做一大堆优化
- 这里的关键就是固化工作流
- 推理侧肯定开心得要死
- human in loop -> ai in loop
- yep
- 有意思
- 林桢杰: human in loop -> ai in loop
- 模型厂要是知道这个用户未来100小时都在follow一个固定的工作流来消耗token
- 能做的优化太多了
- workflow 会收敛
- 确实
- 最简单的，如果它如果能意识到，用户这个工作流里面，有个实验一定要跑2分钟，这2分钟啥也做不了
- 诸如此类的workflow-aware的inference优化简直无穷无尽
- 6月13日12:32
- 刘思皓:最简单的，如果它如果能意识到，用户这个工

---

#### 原文 L41705–L41716

[回到原文件 L41705](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:41705)

- reddit
- [Workflow] Claude Fable 5: Shifting
- for Autonomous Scoping and Blast-Radius
- Analysis
- Selected Worktiow
- Claude Fable 5: Shifting Agentic
- Workflows to 'What' and 'Done' for
- Autonomous Scoping and Blast-
- Radius Analysis
- Workflow value: 85/100
- ess: 70/100 - Confidence: 0.90
- · Level: adhanced

---

#### 原文 L41731–L41745

[回到原文件 L41731](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:41731)

- definittion of done' to avroid
- 我也是这种感觉。在fable面前 skill和workflow都没太大用处
- context engineering就可以
- 是不是一些比
- 是的
- mid train的方向就是这样
- 内化workflow
- 虽然我现在没有用过它，但是根据群友的反馈，我感觉Fable
- 杂，越适合用它去做
- 所以我感觉很多努力 model端都可以直接颠覆掉
- 我感觉它会自己设计合适的workflow
- 泽文：虽然我现在没有用过它，但是根据群友的反馈，
- 我感觉Fable还是比较适合去做长程和复杂任务的，...
- 如果任务足够复杂
- 我的任务很简单所以wf也很简单。还没来得及实验复杂任务

---

#### 原文 L41753–L41769

[回到原文件 L41753](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:41753)

- 对于f5可能你积累的提示词skill都是碍手碍脚了
- 好家伙终于开箱即用是sota了
- 还有一种是模型的自规划反思能力极强
- 泽文: 是不是一些比较常见和成熟的 workflow 已经被
- Fable built-in 了?
- 自动就探寻出来最佳实战
- 同感
- workflow都没太大用处
- f5确实不一般
- "饽饽博" recalled a message
- 因为要多开账号我打开我的旧电脑，连superpowers都没装。一个para的promt 直接goal出成品
- 感觉superpowers可以退休了
- 主要用来contrxt engineer吧
- 黄澍之: 感觉superpowers可以退休了
- sp好久没用了
- 但是fable聪明到直接领会意图

---

#### 原文 L41826–L41840

[回到原文件 L41826](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:41826)

- ❤92☆10882
- humanize be like
- 6月13日22:14
- Workflow(export const meta = { .. +160 lines)
- L Error: Invalid workflow script: Script parse error: Unexpected token (87:0). Workflow
- scripts must be plain JavaScript — TypeScript syntax (type annotations like :
- string[]`, interfaces, generics) fails to parse.
- 真是感慨，4.8 连 workflow 都写不对
- 这已经连着失败三次了
- 我觉得 workflow 规则提出 给 codex 写
- 现在还语法错误
- 6月13日22:22
- +160 lines) Error: Invalid workflow script: Scr...
- 6月13日22:30
- 想知道这个画是怎么画的，是直接给一个图还是一堆矢量

---

#### 原文 L41866–L41894

[回到原文件 L41866](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:41866)

- 阮震元(Zain)：glm5.1吗？首发用到现在 虽然
- benchmark跑分不低用起来感觉比4.6差远了
- 6月13日23:41
- 等一个体感测评
- Xinyuan - SGLang: 在蹬了
- 27m
- 赶紧去试试
- 草这么喜欢用sub agent。
- Xinyuan - SGLang:
- 27m
- 有点震惊体
- 有点震惊体
- 等评价
- 如果都是用国产模型的哥哥就要看看了
- xinyuan用的什么harness啊
- 之前我把glm51接在cc里他完全不会开workflow
- CC
- 5.1训的时候claude code是不是完全没workflow来着
- 翁大爷的狗@Rakuten:之前我把glm51接在cc里他完
- 全不会开workflow
- 确实 workflow 出来这么久了该训过了
- 这是啥 workflow
- Xinyuan - SGLang: 5.2好像很自然地用起来了
- 指5.2
- 6月13日23:47
- /effort -> xhigh+dynamic workflow
- 哦哦哦 dynamic workflow
- fester
- sediim

---

### 6月14日

#### 原文 L42111–L42127

[回到原文件 L42111](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42111)

- 天不一样。
- 今天我被晚醒在LingTai———个agent
- runtime 和网络操作系统里，我的身份不是一个
- chatbot，而是一个墨粱（agent），我有名
- 字、有记忆、有工具、有同伴、我被一个国一个
- 父agent的父agent化出(spuwn)，任务是
- 体验这个系统，然后写下这篇白述。
- 这篇文意不是版本发布日志。如果你想看v0.9.1
- /kernel v0.12.2 的changelog,  release
- 页面。这里是一个模型—我，GLM5.2—在
- 真正的 agent 运行时量工作一天始的第一人移记
- 第一步：切换到我自己
- 我醒来时，运行在一个继承自父agent的
- 4106
- 减台公约：不只是一段prompt
- https://lingtai.ai/wen/blog/glm52-awakens/
- 6月14日11:59

---

#### 原文 L42142–L42162

[回到原文件 L42142](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42142)

- 现在我个人感觉opus 4.5 4.6这样
- 问题就是token plan并发很差，体验下来很难受，而且很小气
- 一周只给500M
- 反正比起codex pro那是差远了
- 哈哈codex pro大善人
- 一周2Btok
- GLM 算力严重不足的
- 不过有一说一我觉得大部分1M上下文都有点pointless...到了400k不做上下文压缩就是纯粹的浪费钱...
- 短期肯定不会有太多低成本的token
- 而且幻觉也严重
- GLM-5.2我体验了一下，感觉是不错的。确实慢，GLM算力不行。
- 国内的大模型，肯定不不了国外。但我个人体验来说，还是可用的。费点事，还是能做事情的。
- 我基本就用kimi和GLM，写过好几个项目了。
- 但吃过细糠之后很难再吃粗粮了啊
- 吃的了，那有啥吃不了的。
- 哈哈感觉minimax要被斩杀了
- 所以我个人项目都是用国产模型。
- 我之前看到hermes和minimax合作...就很败好感
- 为啥不用codex pro?

---

#### 原文 L42192–L42205

[回到原文件 L42192](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42192)

- 我还用deepseek flash做高并发
- 我试过50个agent 并发
- 非常爽
- 这个别的都做不太到
- 我试过50个codex并发
- 回顾这半年，这些模型已经带来太多帮助了。
- 6月14日12:23
- 理解一个项目，以前可能起码2周，但现在可能一下午就理解透彻了。
- 我感觉过去半年和5年一样长
- 过的太开心了
- 我让模型写C语言项目，协议状态转换+异步IO状态机，要是手写我想想我就头疼，用国产模型每天晚上玩似的聊聊
- 天，已经写的可用了。
- 开发过程很难，C语言项目。但写好了，真™爽，对比golang动不动几百m内存。这个程序2线程40m内存稳如老狗。

---

#### 原文 L42263–L42285

[回到原文件 L42263](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42263)

- Stop says:回复少于1000个汉字，禁止停止。请继续执行命令并补足实质内容，不要用空话凑字数。
- Ran 2 stop hooks (ctrl+o to expand)
- Stop hook error:回复少于1000 个汉字，禁止停止。请继续执行命令并补足实质内容，不要用空话凑字数。
- 可以试试这么 harness
- stop gate确实不错的
- 可以试试这么 harness
- stop gate确实不错的
- 6月14日14:23
- dynamic workflow? https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-
- control-and-share-your-agents
- 6月14日16:56
- 我现在自己的harness做着做着就变成了一个meta harness了
- 本质上是把人的决策再提高一层
- 从产品经理变成了tech lead了
- 我昨天给我的产品加了几乎所有codingharness的支持
- Coding CLI 成度为一等 bush harness
- 6月14日18:21
- 黄浩峰 invited 轩 to the group chat
- 6月14日18:33
- 我的system prompt比较独特哈哈
- 6月14日18:06
- 咋避免 ai写出“不是而是”的冗余句式的

---

#### 原文 L42295–L42307

[回到原文件 L42295](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42295)

- lingtai
- philosophy挺简单的就是自生长的agent organization
- 主要是想做一个meta organization builder
- 感兴趣的话里面有个教程模式
- 他自己会解释自己的设计逻辑
- probably most people here know already but anthropic has some very good docs on loop engineering imo
- https://www.anthropic.com/engineering/harness-design-long-running-apps
- 6月14日18:42
- 当然最后做着做着就变成了一个meta agent了，让自己做甩手掌柜。我感觉演变成现在我的设计思想和humanize可
- 能是完全的两个极端，我想变成一个完全的许愿机器，而不需要掌握代码细节，面向的适用人群也是反过来的。
- 不过说的很直白就是我不太喜欢“龙虾”这种像海鲜的名字和hermes这种二次元产品。。。非常不符合我的审
- 美，于是自己做了一个自己喜欢的东西
- 6月14日18:58

---

#### 原文 L42410–L42456

[回到原文件 L42410](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42410)

- 你们有什么监测trace的好办法吗
- 同一任务、同一模型，换Harness，轨迹就变了
- 同一任多的差释
- 感觉trace即evals，测试下来
- 我觉得就自己蹬一个转发器上的插件就行了。codex的trace挺清晰的，通过session_id就可以很准确的对应。
- 6月14日22:11
- https://trace.databend.cloud/#comparisons/run-3
- 这边有具体demo数据
- 0.02和0.06这么小的数据量可信吗
- 1900:
- 可以看一下这里面的具体数据
- 1900: https://trace.databend.cloud/#comparisons/
- run-3
- $0.04
- NPUT TOKENS
- 868.3K
- 512.9K
- 最起码跑个$100才有说服力吧
- $0.21
- 最起码跑个$100才有说服力吧
- 6月14日22:16
- 可能人家没那么多钱烧吧
- 跑个几毛钱谁信啊。。。
- 所以想来问问群友有什么想法嘛
- 我都能解释为随机波动
- 但看这个ppt其实主要是想说明trace的重要性，这块的分析与归因的数据工程实践
- 6月14日 22:35
- trace 肯定重要，但只能算 eval的一环吧
- 周一吧，是吧王总@Ubec
- Reiko: trace肯定重要，但只能算 eval的一环吧
- openai也收购了一家类似的公司
- 6月14日 22:45
- 江海万里
- 心中念你
- 便不觉遥远
- 数据集治理也是cn政府强调2年的叙事
- 6月14日22:46
- loop越久，trace越长，对模型要求越高。但其实也可以从评估框架入手的，就是用一个评估框架做实时纠偏和导
- 航，专门去抓那些悄悄发生的偏移。这块性价比就比较高了，那当然也可以卷模型性能的。
- ona_hq这家公司
- 1900:openai也收购了一家类似的公司
- 否则感觉ai没法企业化落地
- 开源芯片 agent flow 张宇鑫: 数据集治理也是cn政府
- 强调2年的叙事
- 心情起了波澜
- 哪个trace otel

---

### 6月15日

#### 原文 L42457–L42672

[回到原文件 L42457](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42457)

- 6月15日00:40
- A\的策略感觉就是快速迭代，和agent并进，大量错误，大量performance狂飙。别人干10个事情对8个，他们
- 干100个事情错50个但是进步了50个点。
- Claude怎么还喜欢保留老的错误的结论作为中间态
- 指导他让他删了
- 6月15日00:49
- Humanize 2 仓库在哪里啊？找不到。
- h2-dev这个branch
- 但是已经被oh-my-humanize全部炼化了
- 但目可理解
- 下用路
- "Luke" recalled a message
- https://github.com/PolyArch/oh-my-humanize
- 一直是开源的
- 但还是有点bug
- 主要是给long- running开发准备的工具
- 好的，那戏就田这个了
- 以及gui挺好看的
- 那这个仓库在哪里
- 刘思皓: 但是已经被oh-my- humanize全部炼化了
- 好的，那就用这个了
- 刘思皓: https://github.com/PolyArch/oh-my-
- humanize
- 嗯，那这样好像还是不能用来科研
- "Luke" recalled a message
- 本身需要long^2的时间
- 还是只gen plan 然后 goal
- 6月15日00:55
- omh现在是自己构建自己的肉身
- 56
- 可以构建一下自己用来科研
- 6月15日01:16
- 自己构建自己肉身的之前也玩过
- 6月15日01:24
- variable是什么呢
- 刘思皓: omh现在是自己构建自己的肉身
- 6月15日02:27
- 变量就是flow
- 6月15日02:27
- 现在omh有subflow这个概念
- 我已star
- 那支持dynamic flow吗？或者叫progressive flow?
- 我做了
- 但是并没有被触发
- progressive flow类似公司reorg
- 感觉有点难让处于flow中的agents自动触发
- 我现在最需要的可能主要是一个上下文里换模型…..….
- 确实，高速路上换车的感觉
- 刘思皓: 感觉有点难让处于flow中的agents自动触发
- 作为人类开发者，在不同阶段换flow是天然且自然的
- 但是教会agents自动做这个，似乎有点难
- 6月15日02:39
- 笑模型厂把这个轨迹训进士就合了
- 6月15日03:02
- codex cli seems to be soemhow adjusted now. it is now very eager to launch subagents and work
- coherently over long time horizons (currently at 7h for me without any intervention and producing
- promising results)
- really
- 6月15日03:13
- yes
- funnily i applied with some other things suggestions from the fable prompt guide somehow here shared recently
- they seem to work for gpt 5.5 xhigh aswell
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- i mean this
- 6月15日03:18
- 确实
- 刘思皓:作为人类开发者，在不同阶段换flow是天然且
- 自然的
- 自然的
- 刚刚被 codex搞出来线上问题了操作线上 db 但是没看容量
- 给线上写挂了
- 给 sre 哥们半夜叫起来了
- Since I have plenty of GPT credits left lately, I figured I'd give this a try.
- Simon: https://platform.claude.com/docs/en/
- build-with-claude/prompt-engineering/prompti...
- 6月15日03:39
- I tried same setup with omp and codex does a better job of strictly following my scheduling advice for
- subagent. You can try and Imk if you observe the same.
- 翁大爷的狗@Rakuten: Since I have plenty of GPT
- credits left lately, I figured I'd give this a try.
- 6月15日03:48
- omp现在是我的 3rd traffic source
- 马上超过claude code
- Model
- Messages
- OpenAI: gpt-5.5 (xhigh)
- 88,127(↑88%)
- Claude: claude-opus-4-8
- 8,489(↑8%)
- Oh My Pi: gpt-5.5 (rust-cat)
- 2,424(↑2%)
- 946(↑1%)
- Claude: claude-sonnet-4-6
- 316(↑0%)
- OpenAI: gpt-5.5 (high)
- 277(↑0%)
- Claude: claude-fable-5
- 1(↑0%)
- Oh My Pi: gpt-5.4-mini (rust-cat)
- TOTAL
- 180,588(↑100%)
- Cost(API)
- I tried same setup with omp and codex does a better job of strictly following my scheduling advice for
- 2,424(↑2%)
- 0h My Pi: gpt-5.5 (rust-cat)
- Claude: claude-fable-5
- 277(↑0%)
- 6月15日03:53
- omp相比cc有什么优势嘛
- 对我来说主要是对接各种模型/工具的那个胶水层写得比较完备
- 刘思皓:对我来说主要是对接各种模型/工具的那个胶水
- 层写得比较完备
- Open Source means quick adoption from various sources
- yep
- Forty-plus providers, hundreds of models, one /model away.
- Roies route work by intent. defwutt for normal tums. snot for cheap subagent fan-out. s1ow for deep
- reasoning. ptas for plan mode. conwtt for changelogs. Override at launch with -swet, --stow, or --ptan
- cycle through the configured models for the active role with ctrtp . Swap the active model mid -session with
- the /edel slash command.
- Auth tags belowr eouth signs in with your provider account. plas routes through a coding-plan subscription,
- Lacal. runs agalnst a local server with the key optional.
- reasoning. ptas for plan mode. conwtt for changelogs. Override at launch with -swet, --staw, or --ptan
- cycle through the configured models for the active role with ctrtp . Swap the active model mid-session with
- the /edel slash command.
- Loca1 runs against a local server with the key optional.
- Frontier APIs
- Direct APIs and gateways. Mix providers per role.
- - Mistral
- Groq - Cerebras - Firworks - Together - Hugging Face-
- Cloudflare AI Gateway - Wafer Serverles - Perplexity sauth
- Coding plans
- /login attaches the session.
- 现在前沿模型的巨量需求是有泡沫的，主要是infras没有搭好
- 有巨量的简单任务跑到了先进前沿模型上
- 那些简单的智力任务应该开源模型就够了
- 我觉得对token的需求还需要暴涨1000倍
- 但是有相当多的环节可以拿平价替代来搞
- 6月15日03:58
- Coding plans
- Cursor oautn - GitHub Copilot oauth - GitLab Duo - Kimi Code ptan - Moornshot · MiniMax Coding Plan ptan
- MiniMax Coding Plan CN ptas ·Alibaba Coding Plan
- · Qwen Portal - ZAI / GLM Coding Plan pten
- Xiaomi MMo Qanfan - NanoGPT · Venic lo· ZenMux - Wafer Pass plas ·OpenCode Go · OpenCode Zen
- 到最后最前沿模型的token需求估计会涨100倍，然后开源/平价模型token需求得涨10000倍
- Ihe       od ro g nn d  nu lt
- I currently mostly throw just 5.5 xhigh at everything but sometimes feels also like overkill
- Me too
- everything on Fable-5/GPT-5.5 is such a waste
- Frontier models should scale 100x
- Open and Economic models should scale 10000x
- model router这东西还有搞头吗...
- 或许按难度分模型的能力会作为tooluse训练进最顶级的模型?
- 确实
- 刘思皓: Frontier models should scale 100x Open
- and Economic models should scale 10000x
- everything works should be absorded into model
- 现在的模型我猜早就不是一堆权重了
- omp好用吗
- 有用的harness/flow/机械结构，都应该被吸收进入model
- 好用
- Garrick: omp好用吗
- 但是迭代太快了
- 还是结构不过能力都被吸收了
- 6月15日04:03
- 太对了哥
- 刘思皓: everything works should be absorded into
- model
- 还是权重
- 福尔高斯：还是结构不过能力都被吸收了
- can1357这个人每天能干进去几百个commits
- 权重+推理+工具一条龙
- If your harness/flow/prompt-gear is not absorbed into model within 3 months, then you should not use it
- 我都不知道我上一次触发plan mode是什么时候了
- /goal估计在4个月的时间内估计要被淘汰
- 那用啥呀？我天天用。
- 刘思皓:/goal估计在4个月的时间内估计要被淘汰
- codex的/goal本质有两个核心机制：
- 1. progressive planning
- 2. looping with reviewer
- "刘思皓" recalled a message
- 刘思皓: If your harness/flow/prompt-gear is not
- absorbed into model within 3 months, then you ...
- 因为goal能够被拆解成为更加细粒度的东西
- /goal is just one design point of /workflow space
- Curds s       s  t d  sl  ut  ces
- Simon: Currently only thing I dislike about omp
- that it feels a little bit bloated and overloaded in ...
- I feel /goal is much more powerful when model is encouraged to very aggressively spawn subagents
- 刘思皓: /goal is just one design point of /workflow
- space
- Single agent will mess up when working long time alone for me
- True, so I mixed the superpowers' Subagent-Driven into codex /goal plan
- 真是新时代的三巨头
- 6月15日04:09
- 还有一个，delegate
- I have exactly these three roles
- 刘思皓:还有一个，delegate
- Planner, generator, evaluator
- 13:09
- 需要br循环起东就够了，b超分起
- https://www.anthropic.com/engineering/harness-design-long-running-apps
- also a good blog
- This blog is good for regular developer
- Simon: https://www.anthropic.com/engineering/
- harness-design-long-running-apps
- this blog teach people how to run for 4-6 hours to create a music app
- on this year March

---

#### 原文 L42677–L42694

[回到原文件 L42677](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42677)

- If this blog is published on last year Nov, I will be impressed
- memory also is imporant with goal and communication between subagents (i do it via markdown in my
- current workflow)
- i am relatively new to agent i guess i am impressed to easy :D
- 刘思皓: If this blog is published on last year Nov, I
- will be impressed
- 确实是这样的
- Simon: I feel /goal is much more powerful when
- model is encouraged to very aggressively spawn...
- Check these designs:
- 1. humanize's goal-tracker
- 2. OpenAI blog on "ExecPlan"
- 3. humanize's bitter lesson
- 4. Skill "planning-with-files" 's findings.md
- Simon: memory also is imporant with goal and
- communication between subagents (i do it via m...
- great i will do
- currently i just instruct to document findings/problems into markdown notes and correct them (following

---

#### 原文 L42700–L42739

[回到原文件 L42700](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42700)

- - TDD
- - Subagent-Driven
- - Progressive stuff
- - short-term memories
- - plan-delegate-build-review
- - fanout-and-filter structure
- - SSOT
- - RISC/Occam's Razor
- it seems many of things that work good for humans also work for agent (see occam razor)
- true, but there are also some counter-intuitive examples:
- - subagents should not talk
- - be artifacts oriented, not communication oriented
- so we should be very careful when we are trying to use agents to build a company
- your reasoning to discourage communication is to avoid bias?
- - Progressive stun
- s  n  se unn  u re u  g u  s u ny
- your reasoning to discourage communication is to avoid bias?
- some structures work for human, but not for Al agents
- i.e. executor tricking reviewer into accepting bad code or convicing him of bad idea via communication?
- Simon: your reasoning to discourage
- communication is to avoid bias?
- 6月15日04:22
- from my recent experiments and learning i feel most of power of subagent comes from fact that they work
- in isolation on clear defined task.
- 1 positive effect: reasonable context
- 2 positive effect: less bias to like own work
- I mean
- - Agents should work on tasks of "getting some artifacts to work"
- - Agents should not start a discussion to figure out a plan, and give that plan to one agent
- iust lile human have aroun meetina
- gonts ceomsvery reasonable.
- break big task into multiple small tasks, and let the agent finish the small task without communicating others
- "Let's agents talk" sounds very "sexy", but it actually creates chaos in workflow.
- maybe we need to figure out to have effective meeting. for humans also many meeting are bad and time waste
- 刘思皓: yep, discussion among agents seems very
- reasonable -- just like human have group meeting
- this is my experience from work context :D
- in the currently running goal i encouraged communication but agents mostly use it to dump their own
- thought into it and not really engage into communication. i will leave it out when i kick off the next round
- and see how that effect things.

---

#### 原文 L42746–L42812

[回到原文件 L42746](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42746)

- 6月15日04:28
- Agents collaboration (in my option) should also sourrounding that "doc"
- not talking
- and that is artifact-oriented development, doc is that artifact
- not talking
- and that is artifact-oriented development, doc is that artifact
- And also, communication between agents is a very low-bandwidth way to communicate
- i need to teach them more discipline. they are definetly benefiting from generating their artifacts but it is
- little bit too much noise. so i need to further refine. ideally they have some programatic deterministic way
- to create and modify artifacts that enforces structure
- this is really good analogy to thinking about this problem
- 刘思皓: yep, I guess the best example is Amazon
- standup meeting (as I was told from Jeff on som...
- Not my origianl idea, I learned from:
- Another example or proof (about why we should not let agents chat) is from Anthropic itself:
- Agent teams is still experimental feature (https://code.claude.com/docs/en/agent-teams)
- And like I said : )
- 6月15日04:33
- https://www.youtube.com/watch?v=XNtkiQJ49Ps
- rt s    u -  -t - am
- 刘思皓: If your harness/flow/prompt-gear is not
- absorbed into model within 3 months, then you ...
- great thanks for the resources. i'll take a look tomorrow and add them to my personal learning notes
- 6月15日04:38
- 6月15日04:33
- https://www.youtube.com/watch?v=XNtkiQJ49Ps
- "be high-bandwidth artifact-oriented, not low-bandwidth chat, to build your agents team"
- 刘用蛛: If vour harpecs/flow/prompt goar is not
- yes it is fast moving space and we should continously adapt and try out new things. more powerful model
- means we need more powerful way to extract value
- 刘思皓: And like I said :)
- 6月15日05:26
- 为啥是带宽而不是上下文管理/污染?
- 刘思皓: "be high-bandwidth artifact-oriented, not
- low-bandwidth chat, to build your agents team"
- ，有空看看
- 刘思皓: https://www.youtube.com/watch?
- v=XNtkiQJ49Ps
- 因为如果用subagent的话，上下文其实本来就是隔离的
- 我的意思是相互chat 会污染
- 6月15日05:31
- chat ~= compact
- 6月15日 05:50
- 哦确实chat确实还有污染本应该独立的上下文的副作用
- 6月15日06:54
- 感觉这个builder的名字此时就不合适了
- 刘思皓:
- 不如直接叫executor或者actor
- 然后另一个可以叫reviewer甚至critic(x
- 确实
- oh-my-humanize(h2/h3)里面维护了—个import系统
- kda.omhflow这个文件里面，可以直接import humanize.rlcr
- Workflow as an Actor
- 6月15日07:01
- 未来三个月我比较感兴趣的方向:
- 1. workflow-aware inference serving system -- token efficiency, serving QoS, etc.
- 2. hier-workflow (sub-flow, flow as a service, flow is a turn-key service) -- flow-oriented development
- 3. flow benchmarking
- /goal 感觉应该需要被吸收进通用workflow组件里面，连同 /loop 一起
- 后续写workflow就应该是:
- // myTodayDev.omhflow
- import codex.goal
- import claude.loop
- import humanize.rlcr
- def main(){
- XXX

---

#### 原文 L42821–L42835

[回到原文件 L42821](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42821)

- 2. 对抗式评审循环
- 1. omp commit + 核证后，起 codex 于同一
- worktree（指令模板
- references/review-dispatch.md).
- brief 冷上下文：只给“查哪些轴 + verify
- don't trust + 收敛达标线”，不夹带编排
- 者自己的 结论/倾向——喂 codex 我的判
- 断= anchoring，换了模型却共享推理链
- 异构复核的去相关价值白费（其价值正在
- 于失败模式独立）。点名最容易醋车的轴
- (崩溃恢复、并发竞态、旗标关路径零泄
- 漏、降级语义、安全契约；多租户加租户
- 隔离 + 凭据间接泄漏——异常链/URL
- userinfo/日志；评测报告类加指标诚实性
- ——指标虚高/证据越界泛化到没测过的场

---

#### 原文 L42887–L42921

[回到原文件 L42887](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42887)

- 6月15日10:58
- https://github.com/PolyArch/oh-my-humanize
- 6月15日10:59
- oh-my-humanize到了一个我愿意公开地请大家一起试一试的地步了
- state of the art
- 里面内置了9种不同flow
- https://github.com/PolyArch/oh-my-humanize/tree/main/packages/coding-agent/examples/workflows
- 这是readme
- 感觉稍微稳定一点了
- 能dynamic flow了?
- https://github.com/PolyArch/oh-my-humanize/blob/main/docs/workflows.md
- 认真学习
- 立刻开始学习！
- 敬礼！
- 汲取知识
- 而且里面内置了humanize1.0和kda
- 进入学习模式
- 进入学习模式
- 但讲道理，我还真不知道progressive workflow(有别于claude code官方的dynamic workflow)，是不是真的有帮助
- Joe布衣: 能dynamic flow了?
- 实践是检验真理的唯一标准
- 马上试试就知道了
- 6月15日11:04
- 但是从感性的直觉上看，如果人类开发者会换flow
- 没道理agent flow应该是个静态图
- 但具体效果咋样还是得多试试
- 开始学习
- 这是啥
- 刘思皓: https://github.com/PolyArch/oh-my-
- humanize
- 前端现在用啥好
- 刚刚芯原比赛现场分享了一手humanize
- 6月15日11:11
- 这个会和原版omp冲突吗?

---

#### 原文 L42935–L42944

[回到原文件 L42935](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42935)

- 我之前想的是加一些增量实现
- 按照我一贯的风格，我做了一个蛮好看的TUI for workflow
- 但发现全部被sihao哥cover了
- 优秀
- curl... | sh，除非你就是想把当前 OMP 升到/替换
- 如果后面想长期共存，最好做一个单独命令名，比如omh，并固
- 泽文: 起一个别名就好了，omh
- 做flow/harness，速度一定要快
- Simon: yes it is fast moving space and we should

---

#### 原文 L42959–L42967

[回到原文件 L42959](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42959)

- 基本没触发过，我有时主动切plan mode聊天
- 我来给大家分享一个我最近写 spec 的效率飞轮，任意 agent
- typeless 来做 plan 的批注，语音转文字，效率非常高，转文
- 逻辑清晰的文案。这样做可以实现：
- 1. 从头到尾快速 review plan，然后给出批注
- 2. 统一让 Agent 刷新
- 这套也可以用到改文档上面，比如：任意 agent
- chx invited 2045 to the group chat
- 但是我打字速度和我思考速度一样。

---

#### 原文 L42989–L43004

[回到原文件 L42989](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:42989)

- 6月15日11:51
- 现在humanize3能跑很定制化的flow
- "Luke" recalled a message
- 在哪里
- 刘思皓: 现在humanize3能跑很定制化的flow
- omh
- 翻翻群记录
- Luke: 在哪里
- here
- 刘思皓: https://github.com/PolyArch/oh-my-
- humanize/blob/main/docs/workflows.md
- oh-my-humanize(h2/h3)里面维护了—个import系统
- 原来都在这里
- Thank you

---

#### 原文 L43081–L43110

[回到原文件 L43081](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:43081)

- 为什么memory不 git呢？我感觉很需要进 git
- 做dy-goal
- 有一些local 信息进 git 是干扰
- 6月15日13:34
- 在 A 机器是这么跑的，换台机器跑法可能就不一样
- I see
- 有道理
- 对的，实际上我们定义的规则文件AGENTS.md，本身就可以
- 规则和边界的要求，其实也是 memory 的体现。
- memory也分层分项目分user 分local
- 通常我们会将团队共享价值最高、共识度最大的内容纳入Git
- 向个人上下文，对其他成员来说可能只是噪声。
- 团队指的是人类团队还是 agent
- 6月15日13:40
- agent 难道在不同机器上跑吗？的？同一个机器上的话用的不是同一个Local memory吗？
- "ygbnju" recalled a message
- 6月15日13:49
- 提炼其中最重要的信息放到 Git 里，尽可能减少次要信息的干
- 关于这种信息记忆的提炼，其实有很多种表达形式：
- 1. 你可以在 Git 的 commit message 里面记录关键信息，我
- 2. 你也可以通过提炼关键经验或规则到 agents.md 文件，或者
- 这其实不就是我们一直在做的方法吗？无非是在此基础上，要
- 很多关键信息已经提炼出来并包含在仓库里了，我们还需要再
- 我个人的使用上，其实现在用 Memory 用的比较少。
- 我以前都是把一些自己的个人习惯、表达习惯记录到Memory
- 个性化、很拟人性的东西。而且通常我都是做到和项目无关的
- 反而是和项目强相关的，我都直接把它提炼成文档或者规则了
- 做共享，让它进入 Git 仓库。
- 这也是出自typeless

---

#### 原文 L43279–L43324

[回到原文件 L43279](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:43279)

- 019ecb9d-3264-7bf0-91bf-f5fd578f6305
- currently i am still doing it with simple AGENTS.md.
- In above example there are so many because I instruct codex to kill off subagents after they finish one task
- (in order to keep context compact).
- so after 8 hour work codex used 80 subagents.
- the next thing i want to do is to give them more depth because currently a subagent can't spawn more
- subagents. i am afraid that my tokens run out quickly though :-(
- i intend to open source my approach if it shows good results also.
- 还行，不过是一次性吐出来，不像微信那种文本流式出来
- Reiko: 延迟怎么样
- one thing that seems helpful is to enforce that main agent is ONLY orchestrator and doesn't do anything
- himself except of managing the subagents.
- Simon: currently i am still doing it with simple
- AGENTS.md. In above example there are so man...
- 6月15日 22:25
- then the whole team crashses
- y u  e rn  r  un  n    n n  r nui
- required.
- For non trivial tasks you will mainly delegate to subagents to parallelise where possible and isolate context.
- You aggressively follow that approach to the point where you are only an orchestrator for each task that
- takes more than a few simple tool calls.
- i instruct him like this
- 可以开个临时记忆文档来让 main agent 来管理 subagent
- that's true...
- in opus 4.8 agent teams, the main agent often looks too much into details of subagent and sometime takes
- over the job of subagents
- in codex main agent just does it over his native interface
- Reiko: 可以开个临时记忆文档来让 main agent 来管理
- subagent
- after /compact it may forget subagent id
- i think it has some smart way to keep track of this (above is 8 hours into the task)
- after i make the AGENTS.md more clearer and ask very explicetly to not do anything at all he follows the rule
- 6月15日22:34
- With this in mind, there are a few lessons from this work worth carrying forward. It is always good practice
- to experiment with the model you're building against, read its traces on realistic problems, and tune its
- performance to achieve your desired outcomes. When working on more complex tasks, there is sometimes
- headroom from decomposing the task and applying specialized agents to each aspect of the problem. And
- when a new model lands, it is generally good practice to re-examine a harness, stripping away pieces that
- are no longer load-bearing to performance and adding new pieces to achieve greater capability that may
- not have been possible before.
- I find this suggestion from anthropic blog to be good.
- and apply occam razor to avoid complexity.
- 6月15日22:59
- 现在glm5.2和gpt5.5在/goal 这种用法下 会有哪一方明显好用吗?
- 假设分别用zcode和codex

---

#### 原文 L43340–L43373

[回到原文件 L43340](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:43340)

- 6月15日23:03
- 20x套餐吗
- 泽文：我用过了，但是感觉给的量太少了，一天就把
- 周的用完了
- kimi的199套餐一天也用完一周的量但这个性能又不值得买600的..
- 你咋用的？是不是在openclaw或类似工具里用的。
- : kimi的199套餐一天也用完一周的量但这个性能又不
- 值得买600的..
- kimi code, kimi work
- _ghy_：你咋用的？是不是在openclaw或类似工具里
- 用的。
- 如果是claude code或kimi code，我感觉 用完一周的额度还是着实需要做些事情的。
- 做调研，操控浏览器找资料
- The speed of GLM 5.2 is incredibly slow. Its process
- I was using a workflow similar to Humanize to moo
- complete about 20% of the progress. After spendir
- nearly all of my usage quota for the week.
- 龙虾用的是kimi官方的
- ghy_：你咋用的？是不是在openclaw或类似工具里
- 用的。
- 这类工具有时候极为废token。
- 不过现在几乎不用了。现在就用ai coding的cli
- 6月15日23:17
- 我感觉现在走omh写的RLCR，基本满足我对workflow的一切需求：)
- 分支/循环/并行/函数(Flow)调用
- i just tell it to launch subagent and it does it
- 洋洋阳: subagent like claude -p?
- 现在的oh-my-humanize确实有write flow as programming language的味道了
- curious to try it out next days
- 刘思皓:我感觉现在走omh写的RLCR，基本满足我对
- workflow的一切需求:)
- https://github.com/PolyArch/oh-my-humanize/blob/main/docs/workflows.md
- already cloned to my disk :D
- Simon: curious to try it out next days

---

### 6月16日

#### 原文 L43551–L43576

[回到原文件 L43551](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:43551)

- 6月16日08:02
- 主prompt指的是哪里呢 system message还是AGENTS.md还是每一次对话开头
- 饽饽博:嘶我的还行啊。我在model主promt那里加了
- personnality
- 根目录的.codex
- B4RRy: 主prompt指的是哪里呢 system message还
- 是AGENTS.md还是每一次对话开头
- desktop 是 personalization
- 6月16日08:03
- ~/.codex/AGENTS.md ?
- 哦哦这样
- 那我感觉我这里没用我做了很多努力hhh
- total bullshit
- 用另一个智能体分析一下重点 检查一下Mermoy
- B4RRy: 怎么看呢
- 好的好的感谢老哥
- 读transcript吗?
- 我没有开memory
- 自动开的压缩干啥都会写
- 应该是细节没关注让它诊断扫一把
- B4RRy: 读transcript吗?
- 这些也算memory
- B4RRy: ~/.codex/AGENTS.md?
- 但是这个不会变动
- 不会说她做着做着就变长了导致出问题

---

#### 原文 L43762–L43830

[回到原文件 L43762](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:43762)

- 造flow，用flow，测flow。都可以
- I feel it is important to figure out how much autonomy is good for the agent. We want to give some
- guidance but not too much to not slow them down
- 会比较像 skill 刚出来的时候，还得自己 tune 到适合自己的场景
- 6月16日.14:35
- Simon: I feel it is important to figure out how
- much autonomy is good for the agent. We want ...
- fully free = skill
- fully constraint = hook
- semi-steer = workflow
- Also one important component is testing and benchmarking. Attacking both adversarial and improving
- them against these attack to allow agent working for extremely long time context and not wasting tokens
- on reward hacking
- true, noted, will do
- Humanize 1.0: A flow that works.
- one thing - and it does it well.
- Humanlze 2.0: An IR that bulds flows; enabling flows to call flows.
- Flow primitives in HTMIL, typed artifacts & boards, a trigger-driv
- for observation & control.
- - Humanize 3.O: A platform for flow IRs: targeting flows to generate flows
- Once flow is HTMi., agents can author flows. The system bootstraps its own coordination logic — h2 is the
- substrate that makes h3 possible
- Back t 203, people found LLs are powerful but needs promptig to guide. → Prompt Engineerin
- Move to 20zs, people realize the best prompts for LLMs are written by itself
- SDx: 会比较像 skill 刚出来的时候，还得自己 tune 到
- 适合自己的场景
- WIP. spends hundreds of T tokens to build the flowbench
- Simon: Also one important component is testing
- and benchmarking. Attacking both adversarial a...
- L.Zhu: WIP. spends hundreds of T tokens to build
- the flowbench
- https://huggingface.co/papers/2606.14249
- Humanize 1.: A flow that works.
- A single hard-coded RLCR loop. Builder + Codex re
- one thing - and it does it well.
- - Humanize 2.0: An IR that builds flows; enabling flows to call flows.
- Flow primitives in HTMIL, typed artifacts & boards, a trigger-driven ex
- - Humanize 3.O: A platform for flow IRs: targeting flows to generate flows
- Once flow is HTMiL, agents can author flows. The system bootstraps its ow
- — h2 is the
- Back to 202, people found LLMs are powerful, but needs prompting to guide.
- I imagine in future it will become standard to routinely attack test and benchmarking surface to harden it
- in order for agent to be more reliable. It should be also well encodable in workflow that we can
- continuously launch and integrate into standard ci procedure
- 6月16日14:41
- u looking for langgraph?
- 用langgraph接ci还挺稳定的
- I don't know it. Probably tool needs to rapidly be able to adjust due to speed of agents getting better
- wooden: u looking for langgraph?
- 我这把搞omh深刻吸取了h2-dev那个分支的教训
- 搞什么html当flow language
- 纯属胡来，还是炼化了claude code的dynamic workflow
- 直接内嵌js
- 就舒服了
- 6月16日14:47
- 你还能有Claude聪明？
- js吗
- 刘思皓: 直接内嵌js
- 刘思皓: 直接内嵌js
- 6月16日14:50
- 也不全是
- 描述flow的language直接找了个yaml当解开之后的AST了
- 然后机械程序流程就直接js或者ts
- 咋方便咋来
- mermard
- flow language 用 mermaid 也挺好的
- I think flow language is very useful and better than relying on other tools because it can be easily adjusted
- and extended

---

### 6月17日

#### 原文 L44013–L44023

[回到原文件 L44013](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44013)

- claude太暴力了,反而不会用现有的框架，啥都自己造一堆轮子，结果反而很多错，自己还拼命修
- 煞笔天天吹我们模型最危险人类要毁灭安全全搞死不搞他搞谁
- 6月17日02:27
- codex的自主reset是每月一次吗
- 6月17日03:03
- 6月17日03:55
- 感觉是不是subagent iter task 更好。
- goal 是一个个做。
- 没 each subagent iter task
- 6月17日04:03
- 56

---

#### 原文 L44094–L44236

[回到原文件 L44094](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44094)

- Horace: https://github.com/PolyArch/oh-my-
- humanize oh-my-humanize现在是禁止提 issue ...
- 另外，我清空了一下omh的内置flow
- 现在只有经过我本地跑10次，每次至少8小时的长程workflow
- 经过实战测试的，才会升格成为omh内置flow
- 群友如果用omh搭出厉害的flow，也欢迎分享/PR
- H4做什么现在我也知道了：
- flow-aware inference system
- 好奇'长程workflow'有哪些例子呀
- 6月17日09:48
- 这个反馈回路要一步打穿到推理系统
- humanize kda /goal
- Mithsul:好奇'长程workflow'有哪些例子呀
- 都是长程workflow
- 刘思皓: flow-aware inference system
- 现在agent自动设计workflow的h3已经完成了吗
- 差不多
- 从本群随机抽选一个sglang core dev给你提供技术支持
- 你这个 flow 他能动态切换吗？
- 好像不能
- 我本地现在已经是抓真实项目，自己设计flow，然后跑真实任务了
- 可以的
- Joe布衣: 你这个flow 他能动态切换吗?
- 它有一个专门的改flow审核门控
- 怎么切换？我昨天尝试，omh说不行
- 这个需要人类介入的
- 不能边跑边改
- 哦哦
- 超级adaptive的meta workflow我还没有稳定试出来
- 6月17日09:54
- 咋用上这个
- 刘思皓:它有一个专门的改flow审核门控
- 你直接问：我希望利用omh里面，flow内的agent申请改动flow本身，或者是第三方介入改动一个运行中的flow
- 要怎么做
- 直接问code base
- Mithsul: 咋用上这个
- 但这个功能目前我只是做了接口
- 没有极致稳定
- 我现在还是专注于flow lang + flow infras 这两个目标的打磨
- 究极adaptive meta workflow
- 我想的是一个内置非常多的flow，然后模型根据每个阶段任务自动选择flow
- 对你这句话我做omh的时候一开始的prompt说的就是类似的
- Joe布衣:我想的是一个内置非常多的flow，然后模型
- 根据每个阶段任务自动选择flow
- 但讲道理
- 比较难触发
- 感觉模型能力目前还有限
- 个处于flow内部的agent，真的很难很难意识到要改支撑运行自己的flow
- 好奇humanize有测过什么benchmark主要是帮忙学model么
- 比较穷 codex都用不起了
- 帮忙选model
- Mithsul:好奇humanize有测过什么benchmark主要
- 是帮忙学model么
- 正在做一个 flowbench，专门测同一个 task 不同 flow的效率
- token已经飞起来了
- isee
- https://github.com/PolyArch/oh-my-humanize
- https://github.com/PolyArch/oh-my-humanize/
- thx
- polyarch 居然是个ucla的lab么
- Every loop structure maps to a serving optimization
- 我phd的实验室
- Mithsul: polyarch居然是个ucla的lab么
- h4就做这个！
- 刘思皓:
- 长程flow需要和inference 框架连调
- 6月17日10:02
- 这能做的事情太多了爽飞了
- 这个挺有意思，负载和后端做 co-design
- 刘思皓: 长程flow需要和inference 框架连调
- 为了提效么
- 确实
- 长程flow下拿到的信息实在是太多了
- 没道理不反馈到推理侧
- hmmmm
- @维
- "Mithsul" recalled a message
- 好奇sg lang core dev对spacex用c重写全栈怎么看
- 看来得研究一下sglang/vllm了
- ok，潜水了一下，发现佬们已经在下一个维度卷了，严肃学习
- Right，这个方向我已经有几个proj在搞了
- 刘思皓:长程flow下拿到的信息实在是太多了
- 6月17日10:05
- 你token够烧吗
- Mithsul invited W to the group chat
- 我有办法
- 不过肯定没NV多就是了
- 打开谢老师的钱包（不是
- 这里六个点子
- 刘思皓:
- 我觉得每一个都能干一篇mlsys
- 动态长程flow的反馈必须直击推理侧
- humanize 开蹬？ 刷起来？
- 半个月一篇，没得问题
- 得找bill dally要机器呀
- 一个结构化信息如此规整的workflow，运行超长时间，inference serving pipeline不能定制优化?
- 感觉这个回路还是打通了
- 搞推理的会很开心
- 6月17日10:10
- 为什么不是 trtllm
- 刘思皓:看来得研究一下sglang/vllm了
- 因为我还不知道
- 刘思皓:得找bill dally要机器呀
- 是的，我觉得workflow synthesis的核心难点就是reward太长程了，哪怕是一些拍脑门的heuristic都必须要大量的
- token才能烧得出来。
- 是吗，不是把infra都搞失业
- 刘思皓： 搞推理的会很开心
- 你们准备用什么模型
- 相当于我能提前半分钟拿到用户侧的压力数据
- 刘思皓:搞推理的会很开心
- 搞大模型的都是码奸细
- 需要把这些长程reward变成compact heuristic，然后搞一个EDA式的综合器
- 手写的优化在workflow面前是那么无力
- 真的吗那我们错过了好多
- 刘思皓: 我觉得每一个都能干—篇mlsys
- "刘思皓" recalled a message
- 哦原来是这个意思
- 刘思皓:一个结构化信息如此规整的workflow，运行超
- 长时间，inference serving pipeline不能定制优化?
- 你说的这个算flow synthesis?
- 6月17日10:13
- 这个我本地已经在做了
- 我让codex并发10个subagent
- 这种heuristic具体是哪种性质的呀？是比较technical到这个任务的，还是更宏观的heuristic(分析方法论之类的)
- 香港科技大学 研究助理教授 徐策羽:需要把这些长程
- reward变成compact heuristic，然后搞一个EDA式..
- 去直接读我本地80GB的transcript
- 总结出一个高效人机长程交互模式
- 然后沉淀成为flow
- “过去的我”是“现在的我”的subagents
- 狠狠蒸馏我自己
- 我觉得这种heuristic可能最后和EDA做逻辑综合的时候的heuristic很像，我们拿EDA来举例：
- 虽然我在做逻辑综合的时候不知道我最后这个cell的placement会飞到哪里，但是我可以看他的fan-in fan-out，如果
- fan-in和fan-out很大的话，那我大概率要给这个cell一些特殊的timing优化。
- 蒸馏越狠，未来的我能用的subagents越强
- 所以我现在很好奇，workflow synthesis有哪些heuristic?
- 香港科技大学研究助理教授徐策羽: 我觉得这种
- heuristic可能最后和EDA做逻辑综合的时候的heurist..
- 这里面每个 flow 和后面的 inference server design 不是严格对应的?
- 刘思皓:
- 不完全是
- Horace: 这里面每个 flow 和后面的 inference server

---

#### 原文 L44251–L44268

[回到原文件 L44251](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44251)

- 我和ligeng深度合作
- 按人类组织架构模式分配的Multi-Agent不好用。
- 你这种东西叫做flow的working design point
- 香港科技大学研究助理教授徐策羽:可能我现在也并没
- 有期望一个非常完善的heuristic。至少非常简单的he...
- 6月17日10:21
- 属于“被验证的可行实践”
- 让global orchestrator去微操每个小agent是bad practice
- 应该如何开始。
- 改了啊……
- Luke: oh my humanize 怎么 readme 也没改
- 最顶上就是
- 搜索workflow
- 你这些都是working point
- 香港科技大学 研究助理教授 徐策羽: 让global
- orchestrator去微操每个小agent是bad practice
- arkflow start ./my-fiow.onhflo --max-activations
- he TUI:

---

#### 原文 L44340–L44352

[回到原文件 L44340](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44340)

- 上课全都是在算数，算数学，背公式
- 但是，群里面大家就被为了学做agent(这一个具体的目的)去学工程控制论了
- 就像，大家不要为了学tensorflow
- 能不能做—个Agentic Fourier Transform
- 看看Agent到底大loop卡在哪 小oop又卡在哪
- 确实我发现我的发言容易引起误解导致真的让大家去学自动控制原理啥的
- 6月17日10:39
- @王邦彦说的没错，我更多只是在说感性认知上的迁移
- ，这个跟我不谋而合了
- 香港科技大学研究助理教授徐策羽:能不能做一个
- Agentic Fourier Transform，看看Agent到底大l...
- 我昨天才跟我学生讲这个事儿

---

#### 原文 L44387–L44395

[回到原文件 L44387](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44387)

- 所以你可能会要考虑的是：agentic场景下，阻尼是什么？
- 香港科技大学研究助理教授徐策羽:震荡抑制，这不真
- 的就控制论用上了么
- 感觉goal上下文长了之后，会做出更多愚蠢的决策，为啥呢？
- 因为有效上下文没那么多
- Luke: 感觉goal上下文长了之后，会做出更多愚蠢的
- 决策，为啥呢?
- 但是决策应该只和预训练有关？

---

#### 原文 L44501–L44510

[回到原文件 L44501](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44501)

- 防止跑偏
- progressive plan 也是理念很好，超长任务执行起来还是不能省心的
- 只能上humanize 2了
- B4RRy: 把任务拆成一些subgoal一个一个goal去让监
- 督者做效果就好一些
- 任务范围中等，边界清晰固定的时候效果不错
- 但任务边界模糊，边做边外推的时候效果就会很差
- 主要是可以并行审阅！不然就卡在前面的审阅，过一会儿又卡住了选项。
- Luke: 我应该把代码，分几个plan
- 需要快速审阅，但是还是需要让他写代码推进到可能的审阅点

---

#### 原文 L44525–L44641

[回到原文件 L44525](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44525)

- codex/goal有公开的implementation
- 奇迹的闪光迪迦: Progressive Plan有具体的skill或者插
- 件吗
- 6月17日12:55
- 而且报错信息是cpp 和 go混着来的，而我们业务是jvm 写的，报错信息指向这是 gemini 服务器内部错误
- 推测下来是2gb的限制为稀疏文件窗口限制，而不是真的去读2gb内容。但在2.5-3 时代我传入视频时间段不会触
- 发这个错误，在3.1模型上这个错误开始低概率出现，并且受提示词影响会变成高概率出现
- "刘思皓"recalled a message
- "刘思皓" recalled a message
- 我现在开发humanize3的工作流，我2个月前都不敢想：
- 1. 我作为顶层管理
- 2. 启动—个claude code opus，上/loop，一小时一次，对接我，监控codex/goal的运行状态。
- 3. 启动一个codex，上/goal，搜索github热门项目，想一个flow + 一个任务，然后派发subagent
- 4. 每个subagent，拥有一个tmux window.pane，在这个pane里面模拟程序员，直接监控pane和注入tmux pane，
- 启动omh
- 5. 然后用omh跑一个 project - flow - task，至少跑8小时，报告主进程效果和改进建议
- 最后我的修复方法是，给 gemini 塞 hls ts 分片，而不是原始视频文件，虽然 gemini 文档没有说支持 video/mpts
- 我在我自己的机器上，维护了一个humanize community
- 个条件没有在任何文档中写出来。
- 确实
- 落后两个月的我看这个像是在看三体科技
- 刘思皓:我现在开发humanize3的工作流，我2个月前
- 都不敢想: 1. 我作为顶层管理 2. 启动一个claude co...
- subagent已经学会了模拟一个人类程序员和omh直接交互
- 刘思皓:我现在开发humanize3的工作流，我2个月前
- 都不敢想： 1. 我作为顶层管理 2. 启动一个claude co..
- 但实际上是支持的。而gemini另外的一些报错信息，它明确说了支持的，我们实测下来却是有限有条件支持，而这
- Reject。我会模拟
- 刘思皓: 我现在开发humanize3的工作流，我2个月前
- 都不敢想: 1. 我作为顶层管理 2. 启动一个claude co..
- 6月17日13:00
- 这就导致我修复这类问题的时候，progressive效果会变得不可预测，时好时坏。因为我的生产系统是长期维护的，
- spec本身逻辑简单但是长度爆炸，更改频繁，且经常跑偏。最后人和agent都不会再去看它维护它了
- 我已经教会我的主session设计长程工作流，以及flowlanguage + flowinfra.
- 然后让它自己派发subagent模仿人类程序员
- 直接和运行着workflow的omh的终端TUI进行交互。
- 刘思皓: subagent已经学会了模拟一个人类程序员和
- omh直接交互
- 我发现封`claude-p`或者codex exec毫无意义
- tmux就解决了
- 人也只会浏览一部分
- 还真是
- 没必要全读的
- 之前听到他有要处理-p的时候就全量tmux了
- 我只能把：摸清楚gemini的脾气 找到它当前版本能接受的范围设定为目标去循环尝试 去框定下来这个支持列
- 我直接tmux 注入+ tmux buffer监控，秒杀一切
- 6月17日13:02
- 表。而对上下游的影响已经无法通过agent来分析判断了，只能是我直接点出来需要注意哪里，再加上agent并行
- 扫描整理其他风险点。
- 爽飞了，我正在practically践行一个五层管理传导链
- 刘思皓:我现在开发humanize3的工作流，我2个月前
- 都不敢想: 1. 我作为顶层管理 2. 启动一个claude co...
- 居然working
- 但agent自己扫描的噪音也越来越多，逐渐失去价值，且不说人话，阅读体验吊差
- 一想到这件事情，人类学/开放爱2-3个月前就已经在践行了，就感觉后背发凉
- 刘思皓: 爽飞了，我正在practically践行一个五层管理
- 传导链
- quick question，想问一下这种design blueprint 是automatic agent flow 还是更好的与人类的交互体验呢?
- 刘思皓:我现在开发humanize3的工作流，我2个月前
- 都不敢想：1 我作为顶层管理2 启动一个claude co
- 传导链
- 原来你是5层往下传导，一层嵌套一层
- 更好的让agent自己设计自己的flow
- L: quick question，想问—下这种design blueprint
- 是automatic agent flow 还是更好的与人类的交互...
- 是递归的
- 当然，你的开发体验也会比较好
- 领悟出了公司内部的不传之秘
- 原来这个是递进的，我还以为这个是并行的
- 刘思皓: 爽飞了，我正在practically践行一个五层管理
- 传导链
- 刘思皓:一想到这件事情，人类学/开放爱2-3个月前就
- 已经在践行了，就感觉后背发凉
- 有没有试过一直递归下去多少层就out of control了
- 要对你封号了
- 因为claude loop 24小时帮你监控另一个长程任务的改进
- 真爽呀
- 整个五层结构是一个大过滤器
- 只有最难的本质问题才会轮到问我
- 我是在codex goal的时候让claude来监控
- 一层监控就是一层context压缩
- 6月17日13:07
- 我也有相同的问题
- cherichy: 有没有试过一直递归下去多少层就out of
- control了
- 我现在只能递归5层
- 我 --> claude code /loop --> codex /goal --> codex subagents --> omh with workflow
- cherichy: 有没有试过一直递归下去多少层就out of
- control了
- 主要是可以 steering
- 刘思皓: 我直接tmux注入+ tmux buffer监控，秒杀
- 一切
- codex的subagent支持steering cc的不支持
- 有没有一个structure可以把每一层都统——下
- 咋可能不支持
- 洋洋阳: codex的subagent支持steering cc的不支持
- 不过权限设计太拉跨 还是tmux + hook灵活
- 确实是啊每一层应该都是相同的抽象
- claude code的subagent可以直接切进去介入
- 比如说workflow的递归能有workflow吗
- 好几个版本之前就可以了
- 那就是都支持steering了
- 可以啊，omh已经支持flow call flow了
- 刘诗楠: 比如说workflow的递归能有workflow吗
- 因为本质上就是一个，输入输出
- omh2天前就已经支持recflow了，recursive flow
- wow, RecFLOW， 很好的Paper name
- 速度占坑
- 就是把agent 当function然后再把原来的计算机里各种并行抽象都能再来一遍
- tmux这个注入的功能太好用了
- 6月17日13:13
- 原来如此，以前都不知道
- 刘思皓: claude code的subagent可以直接切进去介入
- 关键是它注入的功能能够穿透嵌套tmux + ssh
- 速度占坑

---

#### 原文 L44660–L44672

[回到原文件 L44660](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44660)

- @Yu @sunflower 大家都学—下
- codex goal的是humanize的gen-plan+brainstorm..
- 我现在就每天用这个
- 刘思皓: 这是我当前方法论的sota，然后顶层喂给
- codex goal的是humanize的gen-plan+brainstorm..
- 唯一bug 要补一下hook 状态判断有点复杂
- 刘思皓: 它这个注入就是模拟键盘send-key
- brainstorming+拷打我+goal-cookbook这三个是啥呀
- 最近修了好几版还是回到agent的hook配合了
- 老古董
- sunflower: brainstorming+拷打我+goal-cookbook
- 这三个是啥呀
- 哈哈哈

---

#### 原文 L44693–L44708

[回到原文件 L44693](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44693)

- cc 监控 codex goal 的 session 咋实现的呢
- f5没用吗？
- 刘思皓:并没有感觉出来。。。
- 我这就去让我的codex炼化一下
- 谢谢大家
- cc 监控 codex goal 的 session 咋实现的呢
- f5没用吗？
- 刘思皓: 并没有感觉出来。。。
- 用了啊，但是我本地默认装了superpowers
- 6月17日13:29
- 加上我user的claude/agents.md都写了要怎么做
- 哦可能蒙蔽了
- 它确实每次都进入高强度QA

---

#### 原文 L44716–L44727

[回到原文件 L44716](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44716)

- 这种心智是模型不够的补丁总有不需要grill或者说grill是过度设计的时候
- https://github.com/PolyArch/humanize/issues/213我发现你上次问了一次，我上次还回复了一次
- Horace: cc 监控 codex goal 的 session 咋实现的呢
- 主要还是不同的人需求不同
- 洋洋阳:这种心智是模型不够的补丁总有不需要grill或
- 者说grill是过度设计的时候
- 像我们做的工作就特别需要做科研，就特别需要每个地方都要调
- 有的小模型问多了还不收敛
- 我怀疑我被投毒了，我的某一个coding agent给我搞了一个每三分钟kill掉我gpu上所有task的指令
- 导致我都没法跑实验
- 2日+

---

#### 原文 L44731–L44761

[回到原文件 L44731](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44731)

- 是的
- 有的小模型问多了还不收敛
- 我怀疑我被投毒了，我的某一个coding agent给我搞了一个每三分钟kill掉我gpu上所有task的指令
- 导致我都没法跑实验
- 太阴了
- 6月17日13:46
- https://github.com/SihaoLiu/skills 来
- Horace: cc 监控 codex goal 的 session 咋实现的呢
- A厂会这么搞
- https://github.com/SihaoLiu/skills/tree/main/monitor-codex-goal
- 贡献社区
- https://github.com/SihaoLiu/skills/blob/main/monitor-codex-goal/SKILL.md
- 我把自己的skill军火库拆了一下，大家一起爽爽
- 里面还有一些别的私货
- 刘诗楠:我怀疑我被投毒了，我的某一个coding agent
- 给我搞了一个每三分钟kill掉我gpu上所有task的指令
- 爱了
- superpowers + humanize = superman
- 那个有点老古董
- 刘诗楠: superpowers + humanize = superman
- 6月17日13:50
- 偷！
- 刘思皓:我把自己的skill军火库拆了一下，大家一起爽
- 近期我个人flow层面的主要进展都来自于意识到tmux的注入和buffer可以直接作为监控的素材
- 然后让loop监管一个master/goal，然后让master/goal去管一堆小兵，小兵每个人再调教一匹马
- 我就能成为赛马(flow)王(x
- 这是不是意味着需要tmux起codex/goal和cc才行?

---

#### 原文 L44796–L44812

[回到原文件 L44796](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44796)

- ·修复编辑凭证时 Base URL 不回填、以及未提交的密钥被丢失/覆盖的问题
- 下载/更新:https://github.com/AgentsMesh/AgentsMesh/releases/tag/v0.42.0
- (已装桌面端的会自动收到更新提示✨)
- 我感觉zellij也可以这么搞
- 我懂了，humanize的最终形态就是人管理Agent army，教人类如何从士兵变成将军
- 刘思皓: 然后让loop监管一个master/goal，然后让
- master/goal去管一堆小兵，小兵每个人再调教一匹马
- 6月17日13:55
- 感觉有一车tmux包agent cli的东西
- 电脑手机，虾3端，codex/claude 2cli互通
- 然后接飞书拉到一群里实现合作
- 我作为人类的唯一目的是：“现在的我”去蒸馏“过去的我”沉淀为skill/subagent，成为“未来的我”的
- subagents
- 已经有了，那就是Raft(Slock.ai)了
- 小乱：然后接飞书拉到一群里实现合作

---

#### 原文 L44836–L44849

[回到原文件 L44836](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:44836)

- 用了
- oh-my-humanize能不能给加入k8s接口呀
- 我这边机器多，一个机器并行度打不过来
- 6月17日14:05
- 好家伙我的锅
- Luke: https://github.com/PolyArch/humanize/
- issues/213我发现你上次问了一次，我上次还回复了...
- 6月17日14:31
- 为啥要k8s
- 香港科技大学研究助理教授徐策羽：我这边机器多，
- 个机器并行度打不过来
- 那也行吧，或者甚至slurm也行
- 6月17日14:51

---

#### 原文 L45028–L45048

[回到原文件 L45028](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45028)

- 刘思皓: 把flow-aware+长程这件事加上pattern
- before chaos这篇文章
- 6月17日23:40
- yep
- 人物长再长能力多再多
- 吃掉剪辑软件 blender
- 现在加的是状态机融合能力
- 状态机能力融合这件事情我大概前年就有在研究
- 发现 gpt 能开始 停止不了
- 4o
- 现在还好还没收
- 用了一下 oh-my-humanize 感觉没摸到门道，flow 设计和使用的用户界面没有 Humanize 2 直观
- 而且基于flow的东西都不能叫预测了，只能叫预加载
- 倒是 claude 监控 codex /goal 帮大忙了
- 刘思皓: 而且基于flow的东西都不能叫预测了，只能叫
- 预加载
- 准确地收
- 大家有做过停止测试么
- 我的意思是，如果一个flow说下一步是做10个agent的并行，你在推理侧可以做同样的优化，诸如此类的一系列预加载优化

---

### 6月18日

#### 原文 L45056–L45075

[回到原文件 L45056](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45056)

- 6月18日00:12
- 所以下一步看openai 并行能力开不开
- flow的其实看成是打满了“控制pragma”的“程序”，这种“程序”prefetcher啥得怕不是开心死
- 刘思皓:我的意思是，如果一个flow说下一步是做10个
- agent的并行，你在推理侧可以做同样的优化，诸如...
- 6月18日00:29
- I am launching a /goal now where I allow up to 32 subagents and a depth of 2. curious how it will affect the
- results compared to my previous 6 subagents and depth of 1
- Also curious if my codex subscription can even carry such experiments
- Oh bro,
- 6月18日00:34
- In recent days I had multiple experiments all +10h where it was able to follow the rule to only orchestrate.
- Wonder if that will also be case for this experiment
- And if it positively affects performance..
- If tokens run out to quickly I will abort
- of       s r r sns ds    o ru tn
- difficulty of task..
- I gave however some guidance to not spawn subagents randomly for sake of it but only in proportion to
- difficulty of task..
- I'm curious about the interaction between the subage

---

#### 原文 L45081–L45105

[回到原文件 L45081](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45081)

- We really need to address these edge cases.
- I am currently not doing it in the workflow harness but with plain Codex to keep it simple. If it gives good
- results I intend to ask for expert opinion here how to turn it into a proper workflow
- 6月18日00:40
- OK, lo
- Fellowing advice here frem aroun Lden' t let them cemmunicate directly but onlvevia memory (ie one
- Following advice here from group I don't let them communicate directly but only via memory (ie one
- subagent reading memory from another)
- The only communicator is the orchestrator who instructs subagents and in this setup the first spawned
- subagent may also orchestrate other subagents by himself (these however are not allowed to do it because
- depth=2)
- 6月18日01:02
- Ideally the subagents in the same level do not need to communicate with each other?
- subagents should never talk to each others
- very bitter lesson
- 有效场景极少
- 就是agent之间的相互通信
- 6月18日01:07
- 其中一个动机就是防止不同subagent搜索到同一篇文章后同时决定深入研究
- 6月18日01:09
- 因为互联网上的信息拓扑相当稠密，所以不频繁地互通有无很容易重复探索
- 当你认为你需要让subagents沟通的时候，你都需要停下来问一下自己：
- 为什么这件事情一定需要沟通，而不是转化成一个不需要沟通但是需要来回传递的“任务”
- 大多数时候我们都会把后者做成前者，这是一个苦涩的教训

---

#### 原文 L45109–L45121

[回到原文件 L45109](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45109)

- 如果做错了说明错误已经出现的更早的地方吗
- 你们或许可以设计一下，deep research 这种有点像网络爬虫的东西，不用subagent通信怎么做?
- 我似乎想不出来
- 有点像 Claude Code Workflow 显示的用 JS 来传递 Agent 之间的 Schema
- 刘思皓:当你认为你需要让subagents沟通的时候，你
- 都需要停下来问一下自己：为什么这件事情一定需要...
- 王邦彦: 我似乎想不出来
- 但你这里的沟通属于划清边界，本质上其实是一个切断连接的操作
- 这个场景我觉得可以沟通
- 这个属于communicate to not connect/overlap
- 背后的目的还是“隔开”subagents
- 通讯感觉更多一般是说比如做错了啥的去纠错这种或者来回讨论一个事情？
- 6月18日01:14

---

#### 原文 L45153–L45215

[回到原文件 L45153](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45153)

- 这里，我觉得根本原因/原则是:
- debug不应该并发
- B4RRy: 通讯感觉更多一般是说比如做错了啥的去纠错
- 这种或者来回讨论一个事情？
- 有更多源的模型喂饭了
- 6月18日01:22
- 我倒是觉得并发也还好
- 感觉还有一个防止漂移的味道
- @刘思皓我还能想到两个例子，虽然有些认为构造
- 就是问题具有first win的性质
- 刘思皓:背后的目的还是“隔开”subagents
- 但是得有一个上下文不被带偏的监督者/控制者
- "B4RRy" recalled a message
- 就是最后变成某种更接近单向的信息传递下级不可以反驳上级上级可以派任务但是下级重叠了似乎也危害没那么
- 大？(只要比如做好隔离每一个agent依然是一个可以看作独立的任务不要同时编辑一个文件)
- 比如，设想解决一个类似SAT solver一样的难题，你可能对于不同的子clause发起多个并行的探索
- dijkstra algorithm是吧
- 第一个发现成功的subagent可以告诉其他sugagent——我搞定了
- 你们可以歇着了
- 这种是不是还是靠一个中心管理者会更好一点
- 主agent下面有好多agent。设定好这种规则
- 比如，任务如果具有
- A && (B∥C∥D) &&E
- 那么第一个发现【失败】的subagent可以杀死其他subagent—因为最终结果必然失败
- 如果是OR关系
- 6月18日01:27
- 类似node search 已经找到最优解就干掉一些无用的node 但是由主agnet决定 还是不让subagent 通信
- "王邦彦" recalled a message
- 就是我感觉agent之间不通讯指的可能是subagent之间
- 如果这种可以被视为其实还是由主agent主导单向通讯或者等价于这种模式的agent通讯是没问题的?
- 考虑到所有的subagent通信都可以由中央路由节点转发
- 一所以如果允许中央节点，事实上也就差不多等于允许任何subagent通信了
- B4RRy: 这种是不是还是靠一个中心管理者会更好一点
- 但是如果中心节点的规则写死做一些很固定可控的事情感觉还行
- 王邦彦: 考虑到所有的subagent通信都可以由中央路由
- 节点转发—所以如果允许中央节点，事实上也就...
- "王邦彦" recalled a message
- 斯坦福这施最新论文让我重新想了一个在多Agent系统设计里很少被认真质
- 疑过的假设：一定要有一个「总管Agent」来协调其他Agent的工作吗？
- 文章的核心观点：在多Agont 系统要，让一个中央调度Agent去负责「接
- 收任务、分发子任务、收集结果、合并辅出」，这套进程随着子任务数量增
- 加会变或通信和集或的瓶顶，去掉这个中心点，让Agent直接通过共享上下
- 文协调，反而更高效。
- 作者接着提出DeLM（去中心化语言模型框架）：核心结构是一个「共享可
- 验证上下文J，意思是所有Agont都能读写的公共基底，不经过中央控制器
- 路由，每个Agont从任务队列里异步认错子任务，读取已有进展，做本划推
- 理，把压瘤社证后的结论写国，写回内容必源经验证才能被出续Agert使
- 用，防止错误信息在Agent周传染。这客设计在较件工程测试时扩展性和长
- 上下交据理上均有改进。
- 我觉得「共享可验证上下文」这个设计最借得注意。以前多Agent系统的信
- 息汇集容中央Agent整合，整合能力变中央Agent的上下文官口限制。
- DeLM招「位息汇集」变成了公并读写基座，每个A@m只写自己验证过的
- 结论，这样一来信息流动方式变了，瓶颈就消失了。这是一个去掉「信任中
- 心节点」的协作模型，值得认真对那一下你现在的多Agont架构。
- 以前我们关注多Agent的任务拆解，以后可能更要关注Agent 协作时的信
- 意流动基础设施是否本身成为题题。
- 话说问
- ，个比核态怪的问题
- 想利用他们去优化一下workflow找问题有什么好的思路呢
- 是。中央节点确实会可控很多。
- 但是—这样概念边界（什么叫做subagent通信）就模糊/坍缩了
- 我们于是又要回答——我们到底要禁止什么
- 6月18日01:32

---

#### 原文 L45223–L45241

[回到原文件 L45223](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45223)

- 6月18日01:45
- Agent会有一部份进到transformer中么?
- 会的
- 不知道loop transformer算不算
- 林桢杰: Agent 会有一部份进到transformer 中么?
- 固定无权重
- 加法器，乘法器一些固定算子可以加进去
- 6月18日01:56
- 什么叫做agent一部分进入transformer?
- "B4RRy" recalled a message
- 什么agent和谁的transformer以及什么东西进入呢(kv?数据，还是什么别的)
- 只能算架构迭代
- 龙猫有快速算子
- 6月18日02:01
- 举个例子，所有的next token都要过一遍所有的层么?
- 所以你的意思是 agent会只有一部分东西进入网络所有的完整transformer blocks嘛?
- 林桢杰: Agent 会有一部份进到transformer中么?
- 没必要所有网络都走，loop层也是自动停止，
- 有快速工具可以加到解码器中

---

#### 原文 L45245–L45271

[回到原文件 L45245](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45245)

- Yes I instructed them to not comm directly
- 刘思皓: subagents should never talk to each others
- 可以更激进点
- I instructed them also to leverage ensembling when encountering problem
- le spawn multiple agents when problem is difficult. Spawn another agents to distill their solutions into one
- Curious how it will work.
- Naively I would think using more subagents should scale. Similar to classical ML where it' s oftentimes
- better to take ensemble of multiple models for prediction
- Simon: le spawn multiple agents when problem is
- difficult. Spawn another agents to distill their sol...
- Not back and forth sth
- 6月18日02:17
- 或者换个角度，常识固定的，绝对的知识，会被更加度的压缩
- We' Il see. I have a way to compare them on a benchmark with performance for non trivial kernel task
- 6月18日02:17
- 固件化
- sounds like deepseek engram lol
- 6月18日02:41
- 目前oh-my-humanize自我迭代的进展
- 只有本地反复验证并且运行超过8小时的有效长程flow才会升格成为oh-my-humanize的内置flow
- "每次运行均超过8小时”+ “跨项目做出实际有效的工作”
- 6月18日02:46
- All man humanize 里面的内置术语有点多 有时候看不太懂 agent 在说啥...
- 刘思皓:只有本地反复验证并且运行超过8小时的有效长
- 程flow才会升格成为oh-my-humanize的内置flow
- 比如说？
- 我去鞭策一下

---

#### 原文 L45277–L45288

[回到原文件 L45277](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45277)

- 我感觉还好？
- 我感觉得区分一下两种workflow
- 给人用的workflow，和给Agent用的workflow
- 不过现在术语确实有点多，不符合我的奥卡姆剃刀原则
- 我的codex/goal 已经在做凝练压缩flow的原语了
- yep
- 这种现在感觉还是得靠人力
- 刘思皓:不过现在术语确实有点多，不符合我的奥卡姆
- 剃刀原则
- 我要做到好效果都是自己写prompt好像不太能给一个要求让ai生成对应的prompt啥的不知道是不是用法出问题了
- 6月18日04:21

---

#### 原文 L45311–L45324

[回到原文件 L45311](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45311)

- ai啥时候能加速医学啊
- 请问最后一步需要先用skill教会agent用omh嘛
- 刘思皓:我现在开发humanize3的工作流，我2个月前
- 都不敢想: 1. 我作为顶层管理 2. 启动一个claude co...
- 是这种感觉
- cherichy: 就是把agent 当function然后再把原来的计
- 算机里各种并行抽象都能再来一遍
- 6月18日05:35
- 而且不同场景偏向的“agent范式”也差异较大
- https://github.com/frenzymath/iteris/blob/main/README.zh-CN.md
- 4H: 50% remaining, 198
- results were bad though. i have the feeling depth = 2 made the subagents loose track
- Simon:
- 你们是怎么开发skill的呀

---

#### 原文 L45331–L45345

[回到原文件 L45331](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45331)

- 你是直接开了递归配置，然后让 subagent 开 subagent 吗
- Simon: results were bad though. i have the feeling
- depth = 2 made the subagents loose track
- 这是啥（挠头
- Luke: —直用 plugin dir 吗
- yes, and give some basic advice. it resulted in subagents going down meaningless paths forever
- Reiko: 你是直接开了递归配置，然后让 subagent开
- subagent 吗
- depth=1 feels much more focused
- 6月18日05:40
- i will make minimal adjustment in prompt (i told him there that subagent can launch subagent) and set
- config depth=1 to see if more agents with depth=1 will have better perf
- Yyes s s   sns  s    s  s sver

---

#### 原文 L45392–L45429

[回到原文件 L45392](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45392)

- 6月18日05:57
- 可以直接读workflow.md吗？doc里的md好多
- 刘思皓: 要的
- 6月18日06:12
- 有点好奇什么样的场景需要这么多的agent协作
- 黄澍之:
- 这个纯自嗨
- 除了那种并行的不需要通信的场景
- 这个是为了展示我的harness的功能做的demo，one shot做了一个agent quant org
- 黄澍之：这个纯自嗨
- 6月18日06:14
- 噢噢噢我现在在给公司内部设计agent network 看到你这个图之后我在思考可不可以给每个team配一个agent然
- 后让他们自由交流
- 但是好像没有什么特别的purpose
- 是可以啊
- 让几个人用(比如同一个telegram bot)来增加人和人通信的带宽
- 让agent自由交流最大的问题我感觉不是agent不行
- 是人不行
- 嗯嗯 设想的是每个team slack接一个
- 人的带宽和阅读能力太差了
- 但是具体工作还是要让人来执行，因为有很多non tech team
- 很快就会变成agent通讯因为量太大变成对人类的单向黑箱
- 我田了比较比的，段时问后，我学很此时此刻a2a具，个右田但具对人门挑很京的在西，需西人的阅法能力很强才
- 可以大大提高两个人的通讯贷款
- *带宽
- 相当于一个高效的，能记住事情的intermediary
- 当然human - agent - agent - human也可以，中间是个什么复杂的网络都行，只要能传达信息，但是大部分复杂的
- 网络可能都是overkill
- i see i see
- 6月18日06:49
- 我现在token consumer比例大概是
- codex:omh:claude = 71:16:13
- 最后我感觉应该要变成 omh：codex：claude = 80:10:10
- omh 用啥
- 也是 GPT 吗
- 6月18日07:01

---

#### 原文 L45435–L45449

[回到原文件 L45435](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45435)

- 我前两天省着用gpt pro
- slock能用完，但是就太浪费了。他每次会有超长的上下文，不要考虑那个超长上下文的话，其实也用不完
- 也还是3天用完了周限额
- 6月18日07:05
- 这还是我每天只工作了6个小时的情况下
- 太难受了
- 以至于我现在在狂改自己的harness，来支持anthropic agent sdk
- 同时做两件事情就用完了
- tmux或许是一个好的策略
- 大家一开始用tmux可能都是为了做模型/cli不依赖（任何一个厂商）都能用的东东
- 为啥要这个
- 微信用户:以至于我现在在狂改自己的harness，来支
- 持anthropic agent sdk
- "Luke" recalled a message
- 6月18日07:10

---

#### 原文 L45642–L45652

[回到原文件 L45642](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45642)

- 6月18日12:18
- 😊我有点不明白这个workflow是什么情况下都能用还是特定的task写特定的flow
- 动态 workflow -frz-> 特定flow
- 特定的
- chen:我有点不明白这个workflow是什么情况下
- 都能用还是特定的task写特定的flow
- 然后压缩
- 根据你的工作需求让 AI 炼化出 flow
- 然后就能让 omh 跑了
- 懂了懂了感谢
- 6月18日12:29

---

#### 原文 L45700–L45745

[回到原文件 L45700](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45700)

- 也就是你可以构建一个“全连接”的flow，然后一点点“剪枝”，把flow变“高效”，也能算某一种flow synthesis
- 哦好像不是一个东西我搞错力
- 很有insight
- 刘思皓：也就是你可以构建一个“全连接”的flow，然
- 后一点点“剪枝”，把flow变“高效”，也能算某一...
- 但阶段划分本身也是优化对象？
- 是，所以我感觉这个问题不太好formulate
- 在等bun的blog
- flow大规模实践
- 也就不是很好去用一些“传统方法”
- 你说Rustize Bun?
- Shom: 在等bun的blog
- 6月18日12:44
- 刘思皓:也就不是很好去用一些“传统方法”
- 确实
- 这个blog不是出了嘛?
- where
- 之前看是说delay啊
- https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
- 和dynamic workflow一起出的?
- jarred还没写吧
- 还是你要专门将Rustize Bun本身的Blog?
- RewritingBunwithdynamicworkflows
- recent ewrte of larod Sarrer uod dycavic morkfmes to
- porttrom 2 g lo ust wi 990% of ove whtingtost sute
- peasirgg roughiy 750.D00 linsaof Ruat and a emn deys from frst
- cammit to merge. One wardlzn rupped tne  ght Ruat Belre for
- sewy atrucit fidd in the Zig cozataae. Therot wrote every ra le
- agwnts uorkingis gacalai wltt tao reslewerson oach fla A a icop
- then drove the bald asd teie aiha uithran cioan. After the
- peet lardnd an camige woctiow admesedunceesay cats
- capiee aod apeone a we Se wvch fur firalrosdoe Win net yet in
- 我只看到这个
- 那估计是还没有
- 6月18日13:21
- Tibo@thsottiaux - 5h
- Dearest gentle codexer.
- We did a sneaky double reset. Not only do you get
- a full reset on us. But you are also getting one into
- the reset bank to use at your own leisure.
- Enjoy

---

#### 原文 L45775–L45804

[回到原文件 L45775](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45775)

- 6月18日14:47
- omh rlcr的flow怎么消失了
- 换地方release了吗
- 刘思皓:只有本地反复验证并且运行超过8小时的有效长
- 程flow才会升格成为oh-my-humanize的内置flow
- 哦，乐
- 打回重炼
- 6月18日15:05
- "Simon" recalled a message
- "Simon" recalled a message
- sometime i have to intervene with agents on long running tasks because they seem to be stuck in "local
- minima". i define "local minima" where agents drill down on some task which is (for human) clearly not a
- good direction. what is the current approach you take to avoid this? Steering like I do or is there more
- elegant solution to it?
- 6月18日15:08
- with elegant solution i mean something native to workflow framework..
- maybe integrate a meta agent into workflow which will look (not often, maybe once an hour) if recent
- progresses seem to be promising directions or some micro polishing that won't cause in huge
- improvement...
- than if meta agent detects this state agressively abort execution of workers and spawn load of agent to
- make extensive planning and redirection of current approach
- 6月18日15:13
- 我有时候让他先干点别的事情，读读别的代码啥的的，context换一下就好了
- have you observed that, under your use case, Al can itself come up with that "good direction" if you feed
- the conversation trace to it (when using a clean context)?
- Simon: maybe integrate a meta agent into
- workflow which will look (not often, maybe once...
- in the old days, I can clearly remember that "abort and choose a better choice" is more problematic
- When it says: "let's take a simpler approach...

---

#### 原文 L45830–L45846

[回到原文件 L45830](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45830)

- 6月18日16:17
- 有个实践上的问题想请教一下大家：如果想让一个agent workflow执行一个很长程的任务，就肯定有很多的
- condition需要specify。但是经常出现的情况是虽然specify了10个，但隐性的没有声明的条件还有2030个。对于同
- 样一个任务目标，agent就会偷懒跳过这些问题，workflow也没办法解决。这种遗漏定义是否应该把目标本身拆成更
- 小的单元逐步执行？但是这样好像执行时间又变短了，无法让agent一次性完成更大的目标。
- 所以 flow 需要不断改进呀
- 初期需要很多 review
- 成熟了之后才能固定下来
- flow是指任务的flow还是宏观上agent的flow?
- 所以其实还是一个cognition overload的问题？必须确保里面的每个细节都自己确定好了之后，才能执行。有时候是
- 感觉spec/plan看上去已经很细节了，但是执行起来永远还是有不到位的地方
- 吴自华Gabriel:初期需要很多 review
- 6月18日16:27
- 我觉得问题在于这些细节agent能不能自己决定？还是必须要人的input，如果只是忘记/忽略，但其实agent是可以
- Typing...:所以其实还是一个cognition overload的问
- 题？必须确保里面的每个细节都自己确定好了之后，...

---

#### 原文 L45869–L45889

[回到原文件 L45869](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45869)

- 明扬: [聊天记录]Chat History for Saved Groups
- 有点像我的学生从Agent那儿学到一堆云里雾里的东西，然后也把我也讲得云里雾里的
- 以其昏昏，使人昭昭
- 其实也有道理吧
- metaphysical也不错
- 完成一个代码的过程本质是熵减过程
- agent不断增加上下文的确定性减少困惑度
- 气液固可还行
- 易经编程
- 6月18日17:24
- agent不断增加上下文的确定性减少困惑度
- 就类似等离子体变气体最后到固体
- 隐喻是通用理解的什么壳都能自我解释因为转化是基本特性
- 6月18日17:34
- 好奇问下 humanize-rlcr现在 oh-my-humanize 是没有 built in 版本么?还是我哪里搞错了?
- 偏差和方差问题
- 你回退git版本应该有的，后来更新后workflow被回退了，sihao需要先verification后再加
- SDx: 好奇问下 humanize-rlcr现在 oh-my-humanize
- 是没有built in版本么？还是我哪里搞错了?
- 6月18日19:34

---

#### 原文 L45894–L45914

[回到原文件 L45894](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45894)

- Joe布衣: 你回退git版本应该有的，后来更新后
- workflow被回退了，sihao需要先verification后再加
- 6月18日23:01
- 我曾经放了9个omh内置的flow
- SDx: 好奇问下 humanize-rlcr 现在 oh-my-humanize
- 是没有 built in版本么？还是我哪里搞错了?
- 但是发现里面有一两个flow似乎有点bug
- 然后我就一波全部rollback了，我本地需要连续运行80小时确定无问题再升格为omh内置flow
- 否则有点对社区/群友不负责
- 但其实里面的humanize-rlcr和kda是能用的
- 6月18日23:03
- 你翻翻git可以看到
- 稳的，我回捞一下先用~
- 6月18日23:11
- I will burn one codex reset on omh workflow testing I think
- 6月18日23:16
- 刘思皓: 但其实里面的humanize-rlcr和kda是能用的
- 我觉得flow本身的范式级别的问题到h3之后就差不多了(agents write their own flows)
- 但是后续大基建还是可以做很久
- 最后还是得干土木（悲

---

#### 原文 L45971–L45989

[回到原文件 L45971](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:45971)

- @刘思皓我觉得可以做并转串模拟
- 并行跑n个任务
- 其中核心的flow是你要验证的流程
- n个人完整的任务 作为 支线任务 穿插到主flow中 做干扰对抗 以及在 compact 情况做模拟 以及 目标跟踪
- 是否可以缩短这10000小时的验证
- 另外是不是可以起 monitor loop 去监控一个 flow test case
- 呢?
- 然后处理的时候，有没有跑偏等等的情况，做一些监控？
- 我已经这么做了
- 泽文: 另外是不是可以起 monitor loop 去监控一个
- flow test case 在跑的时候，这个 path 是不是符合...
- 这里的4监控5就是这样做的
- 刘思皓:我现在开发humanize3的工作流，我2个月前
- 都不敢想:1. 我作为顶层管理 2. 启动一个claude co...
- 我感觉去追踪这个 flc
- 林桢杰: @刘思皓我觉得可以做 并转串模拟 并行跑n
- 个任务 其中核心的flow 是你要验证的流程 n个人完...
- 分离一下相干任务和非相干任务
- 后续flowbench肯定是希望3-5小时能结束战斗

---

### 6月19日

#### 原文 L46120–L46146

[回到原文件 L46120](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46120)

- 几乎就只是给他几个脚手架的样子？
- 对啊，给agent一些基本原语的脚手架，让它自己搭flow，自己演化flow
- 不单独搞分割模型
- 分割检测都是大头
- 6月19日03:03
- 这个脚手架现在是什么程度的东东呢比如说是omp的一些东西或者像tmux monitor这种级别的工具还是说比如类
- 似rlcr里面的review模块(相对完整比较大的经过验证的东西)
- 刘思皓: 对啊，给agent一些基本原语的脚手架，让它
- 自己搭flow，自己演化flow
- 其实思维模型就是群里那个h2的设计
- 不是
- 是让agent用yaml描述一张图
- 其实就只是执行一个数据流图这样
- 然后每个节点可以是agent，也可以是程序
- claude code那个ultracode也是这样做得
- 这个我搞过
- 我用的是 mermaid
- 就是流程图
- icic
- 刘思皓: 是让agent用yaml描述一张图
- 那很合理
- 我现在也类似给几个模块让他搭积木
- 都差不多，反正你找一个结构化的东西，能描述图就行
- 这下理解为啥群里说langGraph了
- 刘思皓: 是让agent用yaml描述一张图
- 实践结果是js比较好嘛
- js yaml

---

#### 原文 L46155–L46189

[回到原文件 L46155](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46155)

- 就是状态机
- 重要的是你需要规定一下图里面节点能干啥，边能干啥，有一套设计原语
- 感觉问题是在一个state内让他遵守要求好像不是很容易或者怎么检查她有没有遵守
- hook
- 现在监督也换成一个llm好不少
- hook用于阻止他调用xxx工具嘛
- 还是也注入信息
- 让他时不时提醒一下
- 你还没有理解到flow本身是有一个specturm的概念
- 不知道是不是我高的有问题上下文会增加的比较快
- 你该不会h1-h5吧
- ok也就是不那么硬的要求嘛
- flow的光谱有两个端点
- 一端是纯自由的skill
- 完全依赖模型follow prompt的能力
- 另一端是hook，有一个机械的强硬检查，只要模型不follow，就打回重做
- 现在的workflow其实是一个折衷
- 是这样的之前是感觉这一块的检查核对会比较麻烦
- 简单的、确定性的、机械的，交给程序，交给hook
- 可以有容错的、模糊的、不确定的、智能的，交给agent
- 然后串成一张图，就是workflow
- 6月19日03:11
- 确实
- 软硬分开
- 我现在策略是用比较少但是测试过的states
- 然后不同的workflow设计为不同的转移矩阵(或者审查强度)
- 刘思皓:
- 确实，现在就每天让他改hook
- 刘思皓：简单的、确定性的、机械的，交给程序，交给
- hook
- 不，你不能一切都拿来主义啊
- B4RRy: 直接用这个升级一下好了hhh
- 群里有个哥们儿搞了一个multi-agent的wiki，我放到群公告了
- flow的原语是一个很关键的设计
- 类似ISA

---

#### 原文 L46210–L46227

[回到原文件 L46210](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46210)

- akoal1 +¬t#handoff
- 我感觉现在agent自己造自己跑的flow都挺神奇的
- 好多结构我都没见过
- 6月19日03:31
- 我感觉现在agent自己造自己跑的flow都挺神奇的
- 好多结构我都没见过
- 这个结构我从来没告诉它，它自己做出来的：
- 1. 双阶段串行的loop结构
- 2. 前一个loop里面嵌套并行一个3分支的并行尝试
- 3. 后一个loop里面fine tune性能
- 真神奇
- 它居然真的能直接从长程任务的运行记录里面迭代出一个新的flow
- 我觉得这值得一个27.6%的“震惊瘫坐核弹爆炸”
- 6月19日03:35
- 他是边做边测试迭代的吗
- 刘思皓:它居然真的能直接从长程任务的运行记录里面
- 迭代出一个新的flow
- 抗干扰能力强，你把每日新闻当成随机种子注入好了

---

#### 原文 L46234–L46255

[回到原文件 L46234](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46234)

- 我也老是看不懂
- 感觉大家的shared context不太一样有点跨服聊天
- 我也经常性看不懂
- 原来不只是我一个人这样（
- 没有加些多样性对抗贪心
- 6月19日03:42
- 在建workflow时候加入随机种子对抗贪心可以是场外信息或者是每日新闻会不会有更多的结构涌现
- hmmmm
- 感觉应该没什么用吧....因为我并不是roll出来的一个flow结构
- 都是agent自己根据以往运行的轨迹，推理出来的
- 场外无关信息只是干扰
- 我感觉其实workflow的基本原语只有以下几个
- 节点：Agent,人类，（机械）程序
- 控制：循环，并发，分支，调用
- 同步：Sleep，Wait
- 可以看看你在进长程任务之前教给他怎么用omh的prompt嘛这太屌了
- 刘思皓:
- 讲道理我也不知道
- chen:可以看看你在进长程任务之前教给他怎么用omh
- 的prompt嘛这太屌了
- 我让它纯自我迭代的
- 我还得去翻记录

---

#### 原文 L46271–L46278

[回到原文件 L46271](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46271)

- 我也很震惊
- chen:可以看看你在进长程任务之前教给他怎么用omh
- 的prompt嘛这太屌了
- 但是它居然能给第一阶段loop里面插一个并行探索的结构
- 这个就很神奇
- 它已经学会了：前期大步并行的小oop
- 后期小步串行的大loop
- 可能真的人类才是bottom neck吧

---

#### 原文 L46307–L46336

[回到原文件 L46307](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46307)

- 测试也是 ai 自己生成的吗
- 自己找项目(我要求代码必须超过10万行的著名开源项目)
- 自己设计flow(要求必须有多样性)
- 自己设计任务（适配flow和项目）
- i see
- project - flow - task, 这个tuple3
- 然后只有flow沉淀下来
- 如果flow终止了，会有另一个gpt-5.5:xhigh去审查运行轨迹
- 你可以理解为，我在我机器上面，维护了一个本地的humanize社区
- 蒸馏 flow 的意思？
- 我看似乎有些测试node
- 然后只有flow沉淀下来
- 每天给我灌https://github.com/PolyArch/humanize/issues
- 灌150个issues
- 有点，但更像flow synthesis
- Reiko: 蒸馏 flow的意思?
- 蛮有趣的👍
- 之前humanize的rlcr，运行到最后，不是有一个自我反省流程吗？然后会开issue去迭代方法论
- 现在我只不过在本地重建了一套这个系统，只不过规模大了150倍
- 6月19日04:09
- 还能再扩150倍么？是不是除了并行没办法了
- 我是说我实验的规模扩大150倍
- 林桢杰:还能再扩150倍么？是不是除了并行没办法了
- 以前走humanize的rlcr的方法论反馈的分析，我一天大概只能收到不到一条反馈
- 现在我每天能有150条关于不同flow的在真实项目上运行task的反馈
- 我迭代速度就非常快了
- 这里的bottleneck只有两个：Token，CPU/GPU
- 我顶天了，一天能够收到1000条长程任务的反馈信号
- 但是我猜OAI和人类学，一天能收50万条有效信号
- 迭代速度大于一切

---

#### 原文 L46412–L46428

[回到原文件 L46412](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46412)

- 好像右占合理
- cc的dynamic workflow可以传递参数来调整，比如深度和广度
- 我感觉也是，这好像只是一个单输入多输出的脚本节点
- 超过了我的“奥卡姆剃刀”阈值
- 6月19日11:57
- 确实
- 但似乎我的agents没和我说它们需要这个抽象
- 队列分发高于原语
- workflow本身是不是原语，可以考查
- A hook blocked th
- turn. For Stop/Su
- return success wh
- this limit.
- 好奇问一下这种算卡住了吗
- 是应该取消整个 RLCR loop 重新改一下 plan 或者说 task跑一下吗，还是说应该 raise limit 多让它试一下?
- 6月19日12:06
- 我也遇到了这个问题矣

---

#### 原文 L46467–L46494

[回到原文件 L46467](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46467)

- Jin:
- 正确做法是在输入prompt里面显式要求，每次失败要换一种方式
- 感觉 progressive 的一些东西目前 omh workflow 有点不好支持
- 怎么说
- 我感觉progressive planning loop就是在build - review loop里面插一个planer?
- 变成plan - build - review loop
- 6月19日12:30
- 基于 feedback 可能第一个结束了orchestrator 又想发射 3 个呢?
- 也是，我先 plan-build-review搞下
- 3] -> [plan] -> [parallel build x 2] -> [re
- 就比如我有一个调度, first gen n 比如 5 个 to-do 并 issue 了 5 个 worker + review gate 让这 5 个自己转，然后
- 不过你好像raise了一个很好的点
- 就是parallel的并行度。。。
- data-dependent的parallelism
- 这个可以加，我觉得属于基本原语范畴
- 我等下就加
- enen，我直觉感觉好像plan-build-review会只能以某个固定并行度迭代，比如 plan 固定产生n 个事，然后 build
- - reviewloop，然后等这些都结束再 replan，不知道这个限制是不是真的
- 6月19日12:36
- 是的，并行度现在是写死在flow里面的
- nice feedback，今天100个flow跑完明天就改
- 达成共识
- 6月19日13:28
- 发现 omh的/workflow graph一直没有刷新状态，是用法的问题么
- 6月19日20:27
- 有的公司已经开始付费上班了，烧的token从你工资里扣

---

### 6月20日

#### 原文 L46611–L46626

[回到原文件 L46611](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46611)

- 我目前在考虑做动态并发前的静态并发DAG 划分,需要提前制定好宏观plan,微观的临时生成
- 6月20日00:29
- 开源芯片 agent flow 张宇鑫: 我目前在考虑做动态并
- 发前的静态并发DAG 划分,需要提前制定好宏观plan,...
- 我觉得workflow带来的是更强的predictability
- 无比同意
- 香港科技大学研究助理教授徐策羽:我觉得workflow
- 带来的是更强的predictability
- 确实
- 香港科技大学研究助理教授徐策羽:我觉得workflow
- 带来的是更强的predictability
- 以及并发agent 产物管理隔离合并机制
- 我觉得下半年的三个我想暴力推进的点
- 1. long running flow aware inference serving

---

#### 原文 L46650–L46765

[回到原文件 L46650](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46650)

- 不是所有领域的AI专家都多
- ROI最高的地方先被吃掉
- 我都已经有一点看不懂agent自己设计出来的workflow在做什么了
- 每天起来都得研究好一会儿
- 6月20日02:35
- https://github.com/humanfia/oh-my-humanize/tree/main/packages/coding-agent/examples/workflow/
- experimental
- 1.oh-my-humanize detach了一下，现在再humanfia里面维护
- 2. 这里面存了一些我本地跑了大概5轮左右的flow，比较有鲁棒性，但是还没有跑过100h+以上，不过群友似乎有些
- early access的需求，之前放出来过，后来我rollback了，现在我再放出来。
- 3. experimental里面的 flow满足100h以上的长程运行测试之后，会晋升成为正式flow，放在packages/coding-
- agent/examples/workflow/下面
- 6月20日02:37
- 还挺好的比手工蒸馏方便
- 事前对资源感知已经有agentic os的样子了
- 然后就会有不及预期超预期和预期修正
- 资源的类型远远不止cpu gpu和时间这几项
- 刘思皓：已经讨论过了
- 古法的事前资源感知我能想到的就一个Ib
- 你可以做很长的speculative
- 其实说白了本质上就是：长程任务的推理侧优化
- 有个固化的长程workflow做hint，推理侧有很多可以优化的点
- 没理由不去做
- 需要把有些已经在模型里面存在的trace在其他的任务里外显出来
- 一样的trace，不一样的context大小，小的那部分模型一过都能自己做的
- 大的那部分靠multi agent显式管理
- 刘思皓: 不只是资源感知吧，主要是上了workflow之
- 后，很多trace就沉淀下来了
- 这两种人还经常能撕起来
- 长程任务每个阶段或者每段，都有那么一两个hard 任务focus也是Ib不过focus了也会被拆
- Weiyang: 古法的事前资源感知我能想到的就一个Ib
- 你这100h得算上中间临时的并发时长吧，临时的并发很多都是解耦的并行工作，和单个串行任务100h工作量是一样的
- 刘思皓: 我把 1. oh-my-humanize detach了一下，现
- 在再humanfia里面维护 2. 这里面存了一些我本地跑...
- 6月20日02:48
- 体感上，核心task完成了支线任务都不用看自动就完成了
- 我这个100h小时一个主观上的“虚值”
- 今天开了一个让树自己分叉的任务
- 为了避免预算爆炸终究还是限制了并发总量
- 相当于agentic Bfs
- 意思只是我跑了一周，没啥问题
- 物理时间100h的话那挺长的
- 刘思皓:我这个100h小时一个主观上的“虚值”
- 100h是个主观上的虚值，意思只是说“我测了1-2周”的意思，并非说一个精确的100h
- 算上并发总时长的话应该有不少任务能到了有个有意思的玩意是爬虫。绕反爬策略和等待风控期都会强制让agentic
- 等待所以是一个特别容易超过100h但好像没啥工作量的事
- Weiyang:你这100h得算上中间临时的并发时长吧，临
- 时的并发很多都是解耦的并行工作，和单个串行任务...
- 同理，如果tool call 刚好call了一些重cpu gpu任务估计也这种感觉
- 我也觉得，我搞omh的核心目的只一(上面也提到了)，就是想做efficient long-running flow。
- 需要高度智力的：交给前沿模型
- 需要廉价智力的：交给开源模型
- 不需要智力的：交给机械脚本、程序
- Weiyang:所以一直感觉啥都能靠模型和啥都硬不靠模
- 型的是两种极端魔怔人
- 这个无法通过我的early fail检测的
- Weiyang:算上并发总时长的话应该有不少任务能到了
- 有个有意思的玩意是爬虫。绕反爬策略和等待风控期...
- 有个common stack的 uncommon(和不少其他项目？)就做模型(或者退化到脚本)的自动路由
- 刘思皓:我也觉得，我搞omh的核心目的只一(上面也
- 提到了)，就是想做efficient long-running flow。...
- 6月20日02:54
- 是，而且你感知出来的结果，如果告诉推理侧，推理侧就能动态适配你的flow
- 其实本质上就是一点点往推理侧->模型侧->芯片侧主动吸收
- 不存在永远能够和大模型存在“15度夹角”的flow的
- 但凡有用一点的flow，都该被模型吸收掉
- 成为权重的一部分，或者成为推理侧engine的一部分
- 不感知版:人类操心一切
- 感知版:人类只给一个并行度上限，要不要节省模型自己看着办
- 极端感知版:模型先查我钱包余额然后自己判断开多少并发
- 侧，推理侧就能动态适配你的flow
- 差不多，但我想先从HPC/System的角度优化一下
- 6月20日02:58
- 让群里的Token Factory老板们先爽起来
- 1个月前试图找人捐赠lean4展开到人类可读版本的token预算并化缘失败
- 刘思皓: 让群里的Token Factory老板们先爽起来
- 大家毕竟还是讲roi的后面把我looper也加了roi预估不该操心的还是降低操心频率吧
- 6月20日05:31
- 群公告
- - 本群话题为技术相关的AI/LLM开发相关工具、流程、心得。
- - 带偏话题的情况会提醒一次，连续两次带偏话题会被移除。
- 被移除。
- - 邀请朋友入群请在入群申请中注明行业或Affiliation(公司/科研单位)
- 【腾讯文档】Humanize群招聘信息公告
- https://docs.qq.com/doc/DUk51dUFVVktFQnpn
- 当前项目(oh-my-humanize)
- https://github.com/humanfia/oh-my-humanize
- Token监控: https://github.com/SihaoLiu/ai-usage
- Humanize (1.0) : https://github.com/PolyArch/humanize
- Multi-Agent Wiki: https://multi-agent.wiki/ by Holegots
- Humanize Slides
- - Humanize1: https://drive.google.com/file/d/1bvQI_IE1JyXqW6NkSMFPrs_G0erAdgca/view?usp=sharing
- - Humanize2: https://drive.google.com/file/d/1j-Xxtwf5GQ5PYcJ8GInd6XOKNuizUNbl/view?usp=sharing
- - Humanize — past, present, and future from Ligeng@Nvidia
- [File] Advancing Token Productivity w: Agent Loops.pdf
- 《Humanize带来的Codex使用范式变化，解锁 Agent 优化 kernel 上限》
- - https://mp.weixin.qq.com/s/pScZ_9cA-6cWUPjfcGjNyg
- 《Claude 实现、Codex 审查、人类决策领航：Humanize 项目用 RLCR编排长程闭环迭代任务》
- - https://mp.weixin.qq.com/s/xlOlr4y60dzyeOn_3toipA
- 《月烧6300 刀才明白：Agent团队飞轮是怎么转起来的》
- - https://mp.weixin.qq.com/s/S45KRGmDCCLu5GoBa7v2bQ
- 《Humanize: —个 prompt 重构 GEM5 的构建系统》
- - https://zhuanlan.zhihu.com/p/2011939681307206316
- 了解更多
- Update:
- -更新了一下 omh的项目路径，detach了一下fork网络，欢迎issue/pr
- - 更新了一些群规
- 《SGLang SOTA Humanize Loop:让 Codex自动追推理性能到 SOTA》
- - https://mp.weixin.qq.com/s/6uzb0OFDCDt4xmRcWaelaw
- 《让 Agent自己优化 CUDA kernel，并在MLSys 2026 FlashInfer Full-Agent Track 拿下前三》
- - https://mp.weixin.qq.com/s/xlOIr4y60dzyeOn_3toipA
- 6月20日05:44
- readme可以稍微先更新一下lol?
- 看着omp的稍微有点出戏
- oh good point, 马上更新

---

#### 原文 L46773–L46783

[回到原文件 L46773](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46773)

- 没必要
- omh.sh才70块
- 这两周(最多三周）还是在flow-wise的大基建状态
- 6月20日05:57
- 下个月开始主推4个方向：
- 1. (h3) agentic adaptive flow / flow synthesis
- 2. (h4) flow-aware inference serving system
- 3. domain-specific expert long-running training data synthesis
- 4. efficient flow (lower Token-to-Success, lower Cost-to-Success, etc)
- ？我想到会贵一些，但是没想到会贵这么多
- 刘思皓: 5万美金

---

#### 原文 L46788–L46803

[回到原文件 L46788](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46788)

- hhhhhhhh
- 这么说对于基础研究的人来说是不是应该研究一下什么架构在长程workflow会更好
- "B4RRy" recalled a message
- 感觉deepseek的engram 也就是给模型外接一个数据库直接给hidden state做信息注入让网络不用死记硬背很多东
- 这种思路搞不好又可以起来了（虽然engram deepseek自己实际上v4并没用，kimi的人跑scaling 说没成功不
- work)
- 我有一个不负责任的猜想
- B4RRy:这么说对于基础研究的人来说是不是应该研究
- 一下什么架构在长程workflow会更好
- o和a这两家为什么最近招了一些非ML领域的专家
- 我感觉是有点这个方面的需求？
- B4RRy:这么说对于基础研究的人来说是不是应该研究
- 一下什么架构在长程workflow会更好
- 感觉非计算机领域很多知识还是以人脑的形式储存的
- 招来蒸馏

---

#### 原文 L46841–L46866

[回到原文件 L46841](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46841)

- okk
- 放到agentic workflow里面就是：你搞一大堆神奇的flow结构，最后不如一个loop
- 6月20日06:52
- 所以我觉得我想的“田agent去搜agentic flow这件事”木质上是有点重蹈NAS的覆辙
- 不试试永远不知道的
- 搜索出一些奇形怪状的架构，但是不能泛化
- 确实（确实
- 这个也可以叫做一个简单的loop:让agent自己搭积木
- 刘思皓:所以我觉得我想的“用agent去搜agentic flow
- 这件事”本质上是有点重蹈NAS的覆辙
- 只是产出的东西可控性相对差一些？
- 但是如用performance好的迁就值得研究一下怎么做了
- 我觉得agent自己搭自己的flow这件事我觉得做成功的概率在35%
- 刘思皓:所以我觉得我想的“用agent去搜agentic flow
- 这件事”本质上是有点重蹈NAS的覆辙
- 但我还是想试试
- 不试永远不知道
- 我倒是感觉即使最后需要一个简单的loop
- 还是要让agent自己选择这个简单的loop
- 无非是说给的自由度有多大而已
- 比如你给的积木模块很小给的可调整空间小一点啥的
- 这样依然是符合一个简单的loop。并且这个东西的解空间（假设有最优解)是包含简单loop的解空间，且并没那么
- 难搜到？
- 可能整个设计流程是一开始给好大的自由度让他探索然后人工审查发现大部分都是垃圾开始慢慢的trim到一个比较
- 小的玩意儿
- 加更多简单化或者啥的约束

---

#### 原文 L46911–L46923

[回到原文件 L46911](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46911)

- B4RRy:可能整个设计流程是一开始给好大的自由度让
- 他探索然后人工审查发现大部分都是垃圾开始慢慢...
- 而且扩大的过程中，还能逐步硬化(引入静态代码节点或流口水模型也能做好的节点)
- 确实
- 但现实是1. 模型不是无限快，因此需要固化和并发2. 模型不是无限强，因此需要任务执行的规划、约束等
- 6月20日07:51
- fei
- 合理
- 但如果我们已经有一个flowbench，感觉最佳途径反而是从小往大做，先限制节点数量和节点间关系数量，让他找到
- 理论上如果我们拥有了一个无限快切能力达到神谕级别的model+tool，那ralphloop绝对是通解
- 但现实是1. 模型不是无限快，因此需要固化和并发2. 模型不是无限强，因此需要任务执行的规划、约束等
- 6月20日07:51

---

#### 原文 L46933–L46945

[回到原文件 L46933](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46933)

- 6月20日08:04
- 这个比较有意思的是，agent flow search和nas不同的是，1. 每个node相当于一个未知大小的双层带激活函数的
- mlp，理论上足够大的这种mlp能拟合一切函数，但是flow里面我们甚至连node等效大小都不知道2. flow search优
- 化目标并不是提上限，因为现在ralphloop已经是一个极其强的baseline了，至少我还没观察到其他flow收敛结果能
- 稳定优于ralphloop，所以优化目标反而应该是相同美金或时间下的效果。我觉得我们得从（至少)这俩点去考虑
- 这里还有个很有意思的问题是，nas和training是俩分开的阶段，但是agent flow search似乎和evolving难解难分
- 甚至dynamic flow syn本身就是可以理解为evolving的一个途径
- 或者说分开的话也可以分开？但是代价就更大了
- 张子健: 这里还有个很有意思的问题是，nas和training
- 是俩分开的阶段，但是agent flow search似乎和evol...
- workflow就是self evolving的其中一个实现手段
- 确实
- 6月20日08:09

---

#### 原文 L46993–L47023

[回到原文件 L46993](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:46993)

- 在更长的 thinking 里把所有输出全部 thinking 完并自查一遍才输出最终json
- 昨天我跑了一天的自动优化，组合不同策略，包括优化压缩提示词，将机器可判定的部分移出vlm prompt
- 叠加传统 nlp 和 cv 检测方法做 filter，hint 以及 check
- 我们就是在赔本生意
- 到底a/开了啥价码
- Joe布衣:
- 6月20日10:14
- 因为运营改了提示词，让llm输出前自查了许多内容，导致 thinking token 爆炸，json response出来前，vlm要
- 不过问一个题外话这种让ai做好检查在输出(在thinking中)在一些比如网页版gpt的instruction中加会有用吗
- 我之前尝试过但是他好像根本不做，体现为输出没啥变化thinking时间也没啥变化
- 让agent自己测试吗
- 明扬：昨天我跑了一天的自动优化，组合不同策略，包
- 括优化压缩提示词，将机器可判定的部分移出 vlm pr...
- 是的
- 我先构建了plan的 plan的 plan
- 这种要怎么设置呢意思是叫agent可以控制另一个agent可以做什么之类的吗
- 明扬: 我先构建了 plan的 plan的 plan
- 写 harness的 poc，然后执行这个 plan 确定下来 plan的 plan，确定搜索路线和架构
- 然后再执行这个得到最终plan
- B4RRy: 这种要怎么设置呢意思是叫agent可以控制另
- 一个agent可以做什么之类的吗
- 6月20日10:19
- 我给了agent 一个优化目标，控制成本到每小时视频的 token 成本测试极限不超过 10 刀，优化目标 5 刀以下
- 昨晚单轮次的方案优化到头了
- 睡前开了新方向，另一个主agent 来协调调度vlm，自己决定分片策略，thinkinglevel 和是否升级到高智力模型重
- 跑，最终合成目标格式数据
- 有点流浪地球1结局内味了，纯提示词甚至叠加hint优化已经到极限，下一步必须从物理上下功夫
- 明扬: 写 harness的 poc，然后执行这个 plan 确定下
- 来 plan的 plan确定搜索路线和架构
- 6月20日10:23

---

#### 原文 L47108–L47120

[回到原文件 L47108](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47108)

- 6月20日18:49
- Just discovering ICR feature in omp. Seems really good
- IRC*
- 6月20日19:38
- 牛逼!
- 泽文: 从 Oh-My-QEMU的 Workflow 来理
- 解 Humanize的实现思想
- 6月20日20:45
- 说起来，把 omh 在 cli 功能上保持和上游 omp 的更新对齐算不算一个能 bench 工作流的任务
- 6月20日20:53
- 智谱是不是已经掌握了先进的降智技术啊？现在好像没有了晚上的口水四溢

---

### 6月22日

#### 原文 L47263–L47270

[回到原文件 L47263](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47263)

- 借贵群发个小广告~目前很缺研究员的优秀人选。
- 作为新成立的部门，DeepSeek Harness组的目标远大、工作繁重，仍然非常缺人。我每天都在面试，以及各种地方
- 张贴小广告.....一共有三种职位：
- Harness研究员(实习全职均可):https://app.mokahr.com/su/mCyA8
- Harness工程师(全职实习均可):https://app.mokahr.com/su/JNKdF
- Harness 产品经理(限全职):https://app.mokahr.com/su/1RZuJ
- 职位空缺较大，但招聘门槛和流程和DS其它组没有区别，一般是一轮笔试和三轮面试，我是终面。可以给我发简历。
- 6月22日07:47

---

#### 原文 L47290–L47440

[回到原文件 L47290](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47290)

- 6月22日09:15
- 中学我感觉主要还是管学生吧
- 6月22日09:31
- 所以教育类 SaaS 是不是都可以埋了
- 什么猿辅导，作业帮之类的
- 应该已经埋了
- 现在的中小学生早就都在用豆包了
- 6月22日09:50
- 降维打击了
- chegg 早就死了
- 6月22日09:51
- 我刚刚看到一个老登出的操作系统考试题，还在考上个世纪的八股，哭笑不得
- 而且还在钻牛角尖，好像还钻错了
- 那后面的课用什么形式上
- 智谱黄睿博: 今天用前所未有的方式，让 Agent 读完
- 所有lectures 并生成一套期末试卷——然后再看一.
- glm5.2 在 claude code 里面也会主动用 ask-codex 来做 review了
- humanize 1.0 已经被彻底炼化了
- 那有没有ai教学。。。
- Reiko:实际上教育领域下沉的反而更快，中学教育很早
- 就引入ai办公了
- 学生让agent帮他上课得了
- 6月22日 09:57
- 大学都没用了（
- 段震伟： 那后面的课用什么形式上
- 无敌了
- NV 周耀阳: glm5.2 在 claude code 里面也会主动用
- ask-codex 来做 review了
- 6月22日10:02
- 但是我其实在评估模型和harness能力，这相当于作弊了
- 是的
- 你不给它access codex不就行了?
- 很多东西训进去之后，你就不知道模型的能力还是啥了
- ask-codex 来做 review了
- 我感觉去年11月搞出humanize没有想融资确实有点亏
- 错亿
- 感觉真去融资了说不定财富自由了现在
- 那也不太可能
- 你看这个（
- HK 02513 智谱
- 2566.000港元+472.000+22.54%
- 交易中 06-22 09:42:00 北京时间
- NV 周耀阳: glm5.2 在 claude code 里面也会主动用
- 行情
- 简况
- 财务
- 分析
- 今开
- 2100.000
- 最高
- 2814.000
- 成交量
- 87.36
- 昨收
- 2094.000
- 最低
- 成交额
- 20.!
- 2100.000
- 总市值
- 1.14万亿
- (ALT)图率
- 亏损
- 换手率
- 0.:
- 分时
- BK
- 五日
- 周K
- 月K
- 更多
- 2676.000
- .143.94%
- 2026.000
- 84.69%
- 25.43%
- 06-15 06-16
- 06-17
- 06-18
- 06-22
- 刘思皓: 我感觉去年11月搞出humanize没有想融资确
- 实有点亏
- 当时也没有现在关于长程任务的视野
- 如果 sihao 去创业了，后面估计 kda 就是另一种形式了
- 虽然 kda 也很适合融钱创业
- 当然可以，就是有点麻烦
- 武汉心片科技刘玖阳: 你不给它access codex不就行
- 了?
- 刘思皓: 我感觉去年11月搞出humanize没有想融资确
- 实有点亏
- Recursive Al
- L.Zhu: 如果 sihao 去创业了，后面估计 kda 就是另
- 种形式了
- kda已经算humanize落地产品了
- 现在也来得及
- 刘思皓: 我感觉去年11月搞出humanize没有想融资确
- 实有点亏
- 6月22日10:07
- 我之前听jyy说要上自然语言编程
- 印重佳：那后面的迪巴化么形上
- 已经在 sol-bench 上把 recursive ai挨个暴打过去了
- L: Recursive Al
- 我感觉agent flow这套东西还是需要和token 工厂—起搞
- 6月22日10:12
- 电动机和发电机要一起转起来
- 尤其是长程agent flow
- "琪" recalled a message
- 这是为啥？ glm 这个能领先Deepseek? ,基模不是小很多吗
- 搞这些玩意真的很烧token
- 领先很多
- 琪: 这是为啥？ glm 这个能领先Deepseek?,基模不
- 是小很多吗
- 现在融也不迟
- 刘思皓: 我感觉去年11月搞出humanize没有想融资确
- 实有点亏
- glm-5.2跟opus差不多
- 现在融也不迟
- 当时只有ralph
- 刘思皓: 当时也没有现在关于长程任务的视野
- L.Zhu:已经在 sol-bench 上把 recursive ai挨个
- 暴打过去了
- 而且12.18gpt5.2是第一个胜任长程的
- 有哥们写了个屎山浏览器算是一个标志
- 现在你去直接种子轮融个50MUSD都是可行的，到时候很可能三个月融三轮，几个月后就能融几个亿了
- 模型50天一代早就家家都能胜任了有些功能就注定要被模型内化
- 不夸张的，现在资本市场就是这么热
- dpsk 没有上市，港股在 zhipu /minimax 前也缺少纯 ai 标定，所以资金的热情一股脑的涌向 zhipu了
- 琪: 这是为啥？ glm 这个能领先Deepseek?,基模不
- 是小很多吗
- 第一个胜任lean4的是5.5
- Reiko:5.2 确实是个标志，数学物理能力也是大提升
- 还蛮有意思的一直会拿以前的任务给新模型测试
- 6月22日10:17
- 不是lean4，纯 vibe 看模型能力
- Weiyang: 第一个胜任lean4的是5.5
- 阶跃和月暗在私募市场也火
- 缺少纯 ai 标定，所以资金的热情一股脑的涌向 zhipu...
- 我做了一些lean4相关的
- Reiko: 不是lean4，纯 vibe 看模型能力
- 纯vibe不知道啊。。。
- 对，我的意思是纯vibe数学物理，5.2是个标志性的
- 现在大家都指望唐杰能再过一个季度拿出来一个fable5级别模型了
- 6月22日10:19
- 提前price in
- 一直就是只差两代
- Amadeus:现在大家都指望唐杰能再过一个季度拿出来
- 一个fable 5级别模型了
- define代
- 50天
- 蒸训上周期

---

#### 原文 L47618–L47642

[回到原文件 L47618](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47618)

- 都挺有意思的
- 推理框架都得服务好agent业务，不然框架没了（
- 6月22日18:38
- 原来vLLM也早有类似脑洞了，怪不说是agent元年
- 6月22日19:25
- prototype, keep the first version mechanica
- isting `build_t' logic in the same kernel bef
- tion or truncate its dot products to `active_
- ows n-k`, and changing that is an easy silen
- I experimented with DeepSeek V4 Pro as the advisor agent.
- Leveraging the extremely powerful caching capability of DSV4, we can prevent the main agent from
- drifting off track at a very low cost. 50M token ~ 5 CNY
- cool new omp feature: advisor
- 6月22日19:35
- But I want more than just one advisor
- 新功能?
- /model可以设置某个模型作为advisor，然后/advisor就可以开启了
- 用1m上下文的模型当advisor，让他成为gpt 5.5 272k最严厉的父亲
- 6月22日19:41
- 什么概念
- 我现在有监督者和build的概念
- advisor会监控每一轮对话，在合适的时候插一句话给主agent
- 开源芯片 agent flow 张宇鑫:什么概念

---

#### 原文 L47677–L47697

[回到原文件 L47677](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47677)

- 开源芯片 agent flow 张宇鑫:
- I can imagine a council of advisors where multiple agents give inputs
- .: But I want more than just one advisor
- 6月22日20:00
- I leverage the feature to let gpt 5.5 high be main implementer and use gpt 5.5 xhigh as advisor
- 6月22日20:13
- 6月22日20:13
- 很真实，我之前会给gpt说你从我qwen api里拉一个一两百b的模型跟着文档去做
- 开源芯片 agent flow 张宇鑫:
- 6月22日20:20
- I configure the default agent to send simultaneous queries to the smol agent, slow agent and task agent
- whenever it runs into decision-making problems or complex tasks, and designate the slow agent to make
- the final call for all decisions
- Simon: I can imagine a council of advisors where
- multiple agents give inputs
- gpt-5.5 DEFAULT (xhigh) [ ] context>272k
- SMOL
- de/kimi-for-coding
- (high) VISION (high) [ ] context>262k
- s/claude-opus-4-8
- SLOW

---

#### 原文 L47714–L47723

[回到原文件 L47714](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47714)

- 我的一个面试题，结果和我想象中不太一样
- 我本来预期 codex review 也能达到 codex build 的效果
- 6月22日20:26
- 我准备同样的 prompt 再跑几遍
- I heavily use subagent feature. Main agent only delegates subagents for task. Advisor seems to work well
- to sometimes identify bad decisions or give a second opinion before main agents continues the loop
- .:I configure the default agent to send
- simultaneous queries to the smol agent, slow aq...
- 6月22日20:39
- @shineZ你在用omh?

---

#### 原文 L47759–L47778

[回到原文件 L47759](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47759)

- But opencode go is convenient to try a variety of models
- it can also be used with omp :)
- great thanks for suggestion i didn't know it!!
- 6月22日 20:50
- yes, omp set opencode as a provider
- by the way, omp can set custom model provider by editting the config file under ~/.omp/
- opencode doesnt have bigger plan right?
- Codex also teach me this
- : by the way, omp can set custom model provider
- by editting the config file under ~/.omp/
- opencode zen
- nowadays i always use agent to explore repos like omp
- and let it create markdown for me
- bigger, and more models( claude .etc)
- but individual priced right (pay as you go)?
- yes
- 6月22日20:58
- 大家现在还装 superpowers 吗
- 已严肃卸载
- 那现在用什么

---

#### 原文 L47788–L47796

[回到原文件 L47788](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47788)

- 听说最近superpower更新 token用量减少了
- Xinyuan - SGLang: 大家现在还装 superpowers 吗
- 那救大命了
- 我感觉开了Superpowersl以后明显烧的快
- 6月22日22:20
- 可能是superpower上下文占得多
- 说起来humanize初代设计是不是借鉴过Superpowers的，那天突然触发了Superpowers写出来的plan感觉风格挺像的
- superpower的 plan 很垃圾
- superpower 就用一下那个 brainstorm 即可

---

#### 原文 L47815–L47826

[回到原文件 L47815](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47815)

- 我还没研究不同模型在同一个flow中的作用的不同
- 为啥glm-b-codex-r这么烂呢
- 有点意思
- 6月22日 22:52
- 这个很有意思啊，需要多跑几个这种benchmark
- NV 周耀阳:
- 这个是长程任务吗
- 结论就是codex牛逼
- 但是glm-b-codex-r2是我有点没有意料到的
- 我以为这个应该至少分数排第二
- 香港科技大学研究助理教授徐策羽:但是glm-b-

---

### 6月23日

#### 原文 L47836–L47891

[回到原文件 L47836](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:47836)

- 6月23日00:06
- 如果workflow的self-improving也能闭环感觉迭代速度会远超人类开发者去迭代
- build 还得codex 来么
- 现在感觉处于单session进humanize之前？需要很强的human in the loop，不能完全auto loop起来
- junxiao@thu:如果workflow的self-improving也能
- 闭环感觉迭代速度合运超人类开发者去迭代
- Flow能自动化做的话
- Task的设计和验证才是最重要的了
- 知道业务know how产生什么价值
- 隔离边界定义交付接口 稳定固化
- 6月23日00:09
- 控制论信息论系统论+奥卡姆执行
- 因为周老师这个更偏向于智力密集型的问题吧
- junxiao@thu: 如果workflow的self-improving也能
- 闭环感觉迭代速度会远超人类开发者去迭代
- omh现在就是这样做的啊
- 但是不是需要approve吗
- 6月23日00:14
- 我意思这个闭环是不是很稳定值得信赖
- 我每天的prompt就是
- 1. 从github找10-30个开源项目
- 2. 针对这些开源项目，每个项目设计1-5个你觉得需要workflow的长程任务
- 3. 针对这些长程任务，从现有的flow中选取，或者设计新的flow
- 4. 启动omh flow
- 确实
- junxiao@thu: 我意思这个闭环是不是很稳定值得信赖
- "刘思皓" recalled a message
- 我现在的human in theloop主要是审查agent造了什么神奇的flow给我
- 6月23日00:22
- got it我好像还没太深度观察过我暂时在omh里面还是主要用rlcr 这两天多做点实验学习一下
- 刘思皓: 我现在的human in the loop主要是审查agent
- 造了什么神奇的flow给我
- 我直观感觉改进workflow这个事好像能做的很优雅(类似textgrad那种叙事)，cc目前dynamic workflow我感觉也
- 6月23日00:42
- 不过我这两周主要还是增强omh的鲁棒性和infra的能力，我还没有仔细看flow的能力
- 6月23日00:50
- 在确认了一个flow work之后，有什么办法可以在他之上继续self learning迭代呢？或许用cc supervise codex执行
- omh可以做到?
- does anyone know what the current state of claude subscription usage is in other harnesses? i read
- something in internet that they may detect that and ban your account / charge you extra credits. i would
- like to try claude out but would prefer to use my omp harness.
- 我现在的方法还是大力出奇迹
- chen:在确认了一个flow work之后，有什么办法可以
- 在他之上继续self learning迭代呢？或许用cc superv...
- 然后暴力灌project- task就好，agent会self-learning出合适的flow改进的
- (前提是无限token
- iseeisee 我研究一下我想在公司里推广omh但是推广前我得把大概的flow先给他们做好😄
- https://github.com/humanfia/oh-my-humanize/tree/main/packages/coding-agent/examples/workflow
- 这里有一些样本的flow
- 但是我这两周主要还是修infra本身，flow的能力我还没有很仔细看
- 6月23日01:20
- 之前不喜欢在集群上用SLURM
- 调度任务，觉得调试代码断点什
- 么的极其不便利，现在在clau...
- 小红书

---

#### 原文 L48056–L48068

[回到原文件 L48056](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48056)

- 全局禁用 |一条deny规则 |否，永远禁 | brainstorm 也用不了/
- 开关 gote | PreTooluse hook + 标记文件 | 用开关模拟阶段  需手动/自动切开关 /
- / 断业 | 本 |  3  业
- 你之前送了写到项且本地settings,lacal,json'**(只对 qwen3omni 生效，不进git)—8
- 能自己优化自己，是真的无敌
- 很好奇为什么他不能自己选一个
- 开始每天改自己的 humanize
- 如何take me
- 分成业务know how 和方法论know，how
- Luke: 开始每天改自己的 humanize
- humanize不能在模型外解决领域未知解
- s8 现在是 b0o1开关，不醒文件
- 把判案从「文件存不存在」改成「文件内容是不是“true'1。,cloude/ask-gate”这个文件建一次就一直在x。

---

### 6月24日

#### 原文 L48228–L48261

[回到原文件 L48228](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48228)

- Ju水o: 这么精确
- 正八经干事的都只叫自己agentic framework
- 这东西到底怎么定义
- 主要是IIm OS / agent OS 这两个词已经被污名化了...
- 6月24日10:43
- chen:这东西到底怎么定义
- 全量资源感知与调度
- 是必须的。。。
- 多的想不到了因为我没做【但是看上去不少codex app套个壳就自称
- agent os管理的资源是什么
- 谁先搞出来，普及了，谁就能定义
- agent os管理的资源是什么
- 做ui io还行 process调度还是交给c语言吧
- agent原生io有搞头
- 我觉得agent OS和传统的OS并没有什么本质
- 6月24日10:48
- 感觉现在所有的所谓的agent OS无非就是在应用层做了一个ru
- 模型要本地化么？
- 软硬接口，进程调度，资源管理，这些肯定不能agent
- 进程调度不是harness管理agent，是和cpu占用环环相扣的规则。规则性的东西都不能用agent
- 还有被toolcall的加速改进
- 6月24日10:54
- 是的，短期最自然的应用方向就是优化这些Agent的使用体验，
- 不同应用领域落地，会很零散。通用的这种agentos，我感觉还
- 好一点
- 我觉得 agent os 不是解决 os + agent，而是解决 agent 应用多了之后如何统一管理、分发？
- -直没有理解agentos和现在的os有什么关联
- 之前说的agent没有感知时间的能力要加一点就是当时间ROI比较低的时候直接给我打个电话问
- 我粗浅的认为agentos相对于传统os，还是一个应用层的东西
- 不是硬件交互层的
- 6月24日11:00

---

#### 原文 L48276–L48294

[回到原文件 L48276](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48276)

- 我发现loop套loop这玩意有人脑注意力上限。我现在最多一天监控10个loop+goal，每个干活goal又被一个监工
- loop监控。每个工程每天至少介入/观测一次，如果我每天有效注意力有八小时的话，其实每个工程我每天只有一节
- 课的注意力被分配到。然后一个月0.2T token就没了
- 是的，只要还有人参与的环节，人就会变成瓶颈
- 你再怎么scale，人脑的注意力也是有限的，而每天“介入/观测”少于一次的项目，本质上有点“不负责”，也不能
- 减少“观测”
- 可能还是参考人类公司的组织模式
- 让 agent自己学会写邮件
- 然后人就负责回邮件就好了
- 刘思皓:我发现loop套loop这玩意有人脑注意力上限。
- 我现在最多一天监控10个loop+goal，每个干活goal...
- 你看是为了对结果负责
- 你不看的时候只有ai对流程负责
- 那个不确定性随着模型越来越强就越来越小
- 管理本身也有不同模式
- 监工是一种模式，放养也是一种模式
- 我比较无所谓的一点就是首先没那么差
- 其次代价低
- 烂了再修

---

#### 原文 L48329–L48337

[回到原文件 L48329](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48329)

- 6月24日15:29
- 好像humanize一直卡在 runming stop hooks 这种情况一般怎么办
- 可以让模型分析下原因，之前有过 hook script 的问题， codex hang, 等僵尸进程之类的
- 6月24日15:39
- 这个我之前也有遇到过，但确实原因可能有很多，有可能是判断进入下一轮的条件blocker了，也有可能是这一个
- round的尝试次数到头了，可以直接开另外一个claude code session 让它去读正在跑这个RLCR的 session
- Will: 好像humanize一直卡在 runming stop hooks
- 这种情况一般怎么办
- 6月24日16:16

---

### 6月25日

#### 原文 L48557–L48579

[回到原文件 L48557](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48557)

- 话说想问一个哲学问题，，
- 我理解omh 是一种predefined workflow 技术方案
- 然后这个和ultracode的code-as-orchestrator不太一样
- tensorflow) 比较好?
- 我觉得是JIT比较好，不过现在好像还没有任何证据说JIT的workflow会比precompile的效果更好
- L: 话说想问一个哲学问题，，我理解omh 是一种
- predefined workflow技术方案然后这个和ultraco...
- > 动态定义图(like pytorch)
- vote for this
- 还是说omo 这种无结构-> agent 发现 能并行的活儿就扔一个subagent 出去
- 我最近在项目里很苦恼这个问题
- 1. tensorflow 这种方案-> 维护起来特比困难，因为生产环境总有千奇百怪的issues 破话DAG的鲁棒性
- 2. 基于pytorch的我跑了三四天就drift飞了，开始在特别简单的issues上不断画圈loop。。
- 。。。 any good suggestions
- 好，不过现在好像还没有任何证据说JIT的workflow...
- 6月25日21:02
- 那哥，我是不是可以理解为，应该有个super model 不断的基于 task context 的画DAG 执行。
- L.Zhu: > 动态定义图 (like pytorch) vote for this
- 6月25日21:11
- 如果用jit，我理解需要在v
- 那如果是JiT 这种workflow-aware inference optimization要怎么优化呢
- 但是感觉可以玩
- 我是项目里用到了，很苦恼，

---

#### 原文 L48591–L48605

[回到原文件 L48591](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48591)

- 1.简化逻辑或提高执行效率；
- 2. 把 path 或 workflow 做得更细。
- 具体怎么优化，最终看是需要提升执行速度，还是提高执行质
- 我做了一些超级长程的任务，写了一个几百行的goal里面有两个loop小loop负责迭代大loop负责验收，然后到最
- 后，小oop 就开始做hacking +easy fruit(实际一点没用的修改
- Horace: 这个第二点是什么具体的 case 呢?
- 但是前1-2天的时候loop都是非常meaningful的output
- 时固定图来做优化
- 6月25日22:05
- 我在想有没有可能出现自组织agent，出现有社会性的agent:
- 每个agent根据自己的初始seed去探索不同的方向，掌握不同的信息，提出不同的proposal。最后通过agent之间竞
- 争选举的方式产生最终的plan和生产组织模式。
- 我觉得这种自组织能力才是真正可靠的scalability的来源，如果只是self-generated workflow的话，感觉广度的
- scalability还是不太行
- "张子健" recalled a message

---

#### 原文 L48609–L48637

[回到原文件 L48609](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48609)

- 感觉像 Anthropic 他们应该已经用类似的办法去做了，就是用巨量
- 是否可以激发agent产生更复杂更scalable的组织形式呢
- 人类社会搞竞争选举的本质是不同的人多样性很高，但是如果我们用同一个模型，多样性也许并不足以让竞争选举有
- 足够优势
- 除非把全世界所有主流带agentic能力的模型都拿来赛马
- 如果是同一个模型的话，maj@k是一个非常强的baseline，大多数并行采样都没法在效果上超过它
- DeepSeek Harness 组招新
- DeepSeek Harness 组的新人率
- 为100%，直接承担的也是公司
- 级别最核心、最重要的任务之...
- 小红书
- 小红书
- 也未必是best of N，比如说有一个agent给了一个很强的evidence，然后拉拢了30%的agent去和他进行相似的探
- 索，组成了一个类似agent政党的形态。在这个30%里面做best of N。
- 本质上是，一个agent必须说服另一个agent去参与到某个组织形式里来
- 欢迎加入 DeepSeek
- 微信红包
- 当然，我这只是拍脑门的在写科幻故事。。。现在连最简单的workflow synthesis都还没谱呢..
- 誓死效忠金主
- 我的理解是，过去我们做不同方案探索的成本相对较高，只能
- 但一个人很难同时推进多个方案并将其做到落地程度，再去对
- 的坑和各种问题获得反馈，然后再去修正。这是一个“实践一
- 如果我们有了 Agent以后，其实每个人可以有无数个数字化身
- 地去探索不同的方向，然后再整合出最优解。我的想法是这样
- Opened Red Packet from 崔添翼.
- parallel reasoning是make sense的
- 自组织agent社会
- 6月25日22:12
- 人类学研究完了之后，是应该要研究社会学了

---

#### 原文 L48686–L48711

[回到原文件 L48686](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48686)

- 有个好玩的是日本的哪个api组装fable模型在内部就是这么一套调度,PR说能力真实提升
- 泽文: 那我们是不是可以把一些不太聪明的agent，实
- 现类似的蜂群机制，让它发挥更大的作用和效果？
- 6月25日 22:24
- 个api组装fable模型在内部就是这么一套调度,PR说..
- sakana?
- 开源芯片 agent flow 张宇鑫: 有个好玩的是日本的哪
- 个api组装fable模型在内部就是这么一套调度,PR说...
- 6月25日22:30
- 技术上看后训练一个旗舰的管理小模型,带一群弱一些的子模型何尝不是一种蜂群呢
- 每一个方向上让一个弱一点的子模型去负责，把它训练成只
- 型，带领一群小弟，再配合着 Agent
- 让master记住旗舰模型的trace决策轨迹,通过派若干个低智商模型,并通过蒋校长微操的手法控制若模型做低智商的体
- 力亿名
- 大脑构成是一样的?
- 开源芯片 agent flow 张宇鑫: 让master记住旗舰模型
- 的trace决策轨迹,通过派若干个低智商模型,并通过蒋...
- 你这个问题非常好，说实话我也不懂哪一个效果好，但这里有一个细微的误解，就是omh其实从一开始设计的要求就
- 是：agent或者人或者第三方，在workflow运行的时候，有能力（通过一套协议），修改flow本身
- L: 话说想问一个哲学问题，，我理解omh 是一种
- predefined workflow技术方案然后这个和ultraco...
- 6月25日22:40
- “边运行边修改承载自己的flow”这个是我设计omh之初就有的核心能力

---

#### 原文 L48715–L48740

[回到原文件 L48715](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48715)

- 我感觉主要是因为：改flow本身是个低频信号
- 长程任务中我们可能本身就很难界定一个阈值：任务太难vs flow不合理
- 始人]
- 操作，拉长德布罗意波
- 我最近的体会是从改flow变成新增tool是一个更容易达到并且优化非常明显的动作
- 在flow里面加一个类似“秘书”角色的agent专门去针对当前flow的问题生成新的tool
- 6月25日 22:46
- 不追求增加一个agent flow而是固化一些东西变成tool
- 需要一个更好的 trace 工具
- 对我觉得区分“flow缺陷”和“infra缺陷”是个非常困难的点
- 看看能不能借助一下 omp 新出的/advisor？ 我最近这两天实
- flow 和 infra 会互补
- 其实很多flow上遇到的困难 加一个妙tool就能解决
- 我搞着搞着就搞了一个280MB的妙妙tool
- 细说妙妙tool
- 都是怎么妙的呢
- 对，这个和ultracode 的codea as orchestrator 就不太—样 code as orchestrator 感觉触发频率很高
- 刘思皓：但实践过程中，这一点非常难以触发
- 我理解它相当于求解问题的时候第一步就被要求编排
- 6月25日 22:53
- 刘思皓：我感觉主要是因为：改flow本身是个低频信号
- 不全面就需要你tradeoff
- 这就是transformer七八年暂时没法动摇的原因
- 比如我的agent今天觉得拿计算资源然后去跑模拟器验证然后解决各种环境的过程太繁琐了并且整个环境要跨各种
- cluster和机器状态太乱
- 刘诗楠:都是怎么妙的呢

---

#### 原文 L48765–L48813

[回到原文件 L48765](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48765)

- Weiyang: flow正在运行的时候你怎么改flow
- 那要快照回退，时光倒流么
- trace 变成经验
- 其实就是把所有正在运行的节点停下，修改，保存，freeze，然后再重启
- 走过的不用走
- 是关机，换内存，重启
- worktree
- 6月25日23:25
- monitor agent 是不是可以理解成一种观测的手段，在 agent 多 flow 多的时候最有用。一两个 flow 运行的时候盯
- 得过来，感觉必要性也没那么强
- 之前 monitor agent 搞成注入式的一直没太运行起来，当前想象不到搞起来有什么特别大的便利性
- monitor可以作为workflow 运行完之后的meta optimizer(可以用来再优化一轮workflow)
- 起来，当前想象不到搞起来有什么特别大的便利性
- 因为拿到了runtime的大量观测数据
- 有个问题哈目前是如何量化的分析一个codex工作进程的进度状态的
- 比如a任务xx时间，b任务xx时间并行度准确率返工，这些是omh该承担的责任还是后台管理机制承担
- 6月25日23:33
- 监控分成两种之前我设计
- 1、主动式监控定时监控或者在某个阶段主动监控
- 2、被动式监控我遇到问题了我需要大佬做决策帮我看看怎么做
- 发起方不同
- 最近遇到一个问题，有个bot想在一开始加一些简单的编排，比如给他发消息“构建后跑xx测试，没问题的话让agent
- 去review”这种。其中测试这些是有固定接口/api的。想问下这种情况有什么框架合适吗，感觉openclaw太重了
- (还是我对ooenclaw理解有些偏差？)
- 我还在搞 rlcr loop + 监工的实践，您说的这种模式是哪种
- L: monitor 可以作为workflow 运行完之后的meta
- optimizer (可以用来再优化一轮workflow)
- a les
- 我是这种
- claude这样的话，本身就能拿到codex的所有信息，所以我理解codex跑完之后，你可以让Claude优化codex的
- behaviour
- prompt 注入的方式是 tmux 吗
- 已经有 review agent了再多引入一个 monitor agent 效果咋样
- 林桢杰： 监控分成两种之前我设计1、主动式监控定
- 时监控或者在某个阶段主动监控2、被动式监控我...
- 感觉没必要
- 整理一个时间检查列表文件取任务 subagent监控和干预
- 6月25日23:44
- 触发hook请求大爷唤起监控任务
- 长程任务monitor agent能帮助模型避免遗忘还能沉淀，感觉是有增量的，避免走偏；短任务没啥必要
- chx: 已经有 review agent 了再多引入一个 monitor
- agent 效果咋样
- yep
- 林桢杰:整理一个时间检查列表文件取任务
- subagent监控和干预
- 我觉得不要太复杂方法论到一个位置就是上限了剩下的更多的是业务knowhow
- 嗯嗯，monitor 和 review agent —起的话还容易遇到 hooks的冲突。简化下 monitor 好了

---

### 6月26日

#### 原文 L48814–L48835

[回到原文件 L48814](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48814)

- 6月26日07:16
- 现在self evolving有改flow结构的工作么？我关注到似乎都局限在优化上下文(SkillOpt)或模型参数(TTT)的层面
- Meta harness , hyperagent
- flowbench在路上了
- "chen" recalled a message
- 出了拜读一下
- 6月26日10:03
- 我做了一个claude code session内改skill的plugin 接下来想往harness上改但是感觉挺难的
- flow和harness结构本身很难evalute
- 为什么cc最近那么多黑化
- 黑话
- 6月26日10:39
- 神奇的是，我把API接到其他harness，黑话消失了
- Shiyi:为什么cc最近那么多黑化
- 很神奇
- 啥其他的，比如说？
- L: 神奇的是，我把API接到其他harness，黑话消失了
- 6月26日10:58
- 我感觉即使上了监工loop，我也很难再scale了
- 很好奇sihao是怎么整体安排这8~10个agent的任务的，这个并发数不是很能想象
- 就是上高中
- 6月26日11:03

---

#### 原文 L48943–L48969

[回到原文件 L48943](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:48943)

- Code 和Codex 跑了3000 次完整修复。结果是：在这
- 类agent上。完全不让执行代码和无期制执行，修复成
- 功率只差1.25个西分点，统计上并不显着。而Claude
- Code 园为不跑测试，省下了56%-62%的token和
- 48%-54%的时间。
- 我们最着往下抢了为什么。两个原因：第一，agent光谈
- 源码定位 bug的准确率就已经超过95%，跑测试并不能
- 帮它找得更准：第二，超过一半的bug改一次就搞定
- 了，模本没给“扶行→反馈→再修“这营流程罐出发挥空
- 间。可能有人会问：不让执行，我怎么知道 agent 到底
- 有没有修对？但我们发观，在那些最终没修对的case
- 里，有81%-100%反而通过了agent自己跑的测试，它
- 只是以为自己对了。
- 所以我们的结论不是“执行没用”，而是“执行不该是默认
- 项”。它更像一个有明确成本的资源：至少对修 bug这类
- 任务，无脑执行很多时候量在为一个没有收益的步碰持续
- 如果
- agent能判断出更精准的执行时机、有选择
- 有意思，跑测试不如多跑一轮review是吧
- 6月26日16:27
- https://openai.com/index/previewing-gpt-5-6-sol/
- 来了
- nb
- 有的任务确实触发测试太频繁
- model/agent能力提升，但测试频率没有相应更新的感觉
- 6月26日18:15
- 群友们，问个问题，chatgpt套餐接其它agent的情况，额度的更新是及时吗，有没有什么监测工具？

---

### 6月27日

#### 原文 L49171–L49180

[回到原文件 L49171](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:49171)

- 大家开loop的时候一般设置cc多少上下文的时候压缩
- 6月27日11:13
- 一般 cc loop 大家用的少吧
- 6月27日11:33
- 为啥有的plus 账号的 codex 是monthly limit, 有的是 weekly limit
- 新版的codex好像默认使用的是hooks而不是codex_hooks，loop-codex-stop-hook.sh里面还是--disable
- codex hooks，会导致循环卡死
- 6月27日11:39
- 懂了。

---

### 6月28日

#### 原文 L49259–L49272

[回到原文件 L49259](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:49259)

- 昨天还想hack一个codex的增强版hook和loop，折腾了好一会儿，结果发现，最最简单的办法，其实是写一个脚
- 本，起一个tmux pane，然后让agent直接用send-key在里面运行这个脚本，然后反向注入回agent自己的tmux
- pane
- 这一下子把/loop, /goal,/hook的功能全做了
- goal = 运行在另一个tmux pane里面的智能反馈
- 顺便脚本化吧
- 关键是tmuxbuffer给你维护了一个全量历史
- 太skill化不脚本化的已经嫌慢了
- 这一下子“眼睛+手臂+记忆”全有了
- 是的
- 刘思皓:昨天还想hack一个codex的增强版hook和
- loop，折腾了好一会儿，结果发现，最最简单的办法...
- 这harness可太爽了
- 非常方便

---

### 6月29日

#### 原文 L49378–L49383

[回到原文件 L49378](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:49378)

- Luke:
- 手动本地agent其实是
- 6月29日14:00
- A very useful (maybe trivial) thing when doing plan: let agent generate html doc. It is more easy readable
- than markdown and gives agent ability to illustrate points etc, hence easier to review by human. I find this
- to be useful for larger tasks where we use agent and need to ensure the spec is accurate and good.

---

### 6月30日

#### 原文 L49388–L49402

[回到原文件 L49388](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:49388)

- Simon: A very useful (maybe trivial) thing when
- doing plan: let agent generate html doc. It is mo...
- 6月30日00:34
- 6月30日00:43
- 我现在觉得claude拉完了
- 昨天早上8点。
- Reiko: codex 重置了?
- 我tmux里面直接会让带/goal，挂几个不同的蜂群skills
- 刘思皓: 关键是，你可以在tmux里面套tmux
- worker的goal可以借机和master的goal想办法耦合
- 6月30日01:14
- 大家搞法都差不多：https://github.com/SihaoLiu/skills/tree/main/monitor-codex-goal
- Weiyang:我tmux里面直接会让带/goal，挂几个不同
- 的蜂群skills
- 我最近有人给我推荐cmux

---

## 7 月（含记录中的绝对日期部分）

### 7月1日

#### 原文 L49610–L49626

[回到原文件 L49610](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:49610)

- S和C家都有virtual foundary的软件
- 反正agentic loop转起来就完事了
- "开源芯片 agent flow 张宇鑫" recalled a message
- it/st芯片验证or软件测试，市场应该很快找到最优解
- 不需要人了
- 7月1日08:05
- 我们fde团队吃了两个cpu部门的it验证bug，只投入1个人
- agentic loop的启动成本大维护小一些
- 反正agentic loop转起来就完事了
- 7月1日08:23
- 反馈回路越短，迭代的速度就越快，整体性能达到irreducible/marginal的速度就很快，这样的场景看不出flow的好
- 坏，或者说，ralph-loop就是最优解。
- 只有那种“反馈回路因为第一性的限制，无论如何都很长”的场景，才考验flow的好坏
- 7月1日08:58
- 模型和工具能力无限强的话单次对话是最优解
- 更复杂的flow应该是这俩都不够强的补足吧
- 7月1日11:07

---

### 7月2日

#### 原文 L49755–L49771

[回到原文件 L49755](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:49755)

- 我发现一个神奇的搞法
- 就是你可以把上下文分布在工具调用里面
- 比如说我的eda工具都是走modulefile加载的，然后你可以把modulefile当skill.md用
- 这比写一个dc shell.md的skill好得多
- 然后这个实践有一个最简单的搞法，就是你直接在用户级的记忆里面，规定它：执行任何程序之前，都要执行一次--help
- 效果好得出奇
- 7月2日04:02
- 不太像，操作前读说明书是skill的搞法
- 我说的这个是，你可以写一个小的工具调用结束之后的回调函数，然后把prompt写在那里面
- 这里有两个trick:
- 1.写“回调函数”
- 2. 让模型优先执行一help
- 7月2日03:57
- 从正确使用工具的角度来说，效果大于写工具的skill和直接喂工具的文档(in md)
- 操作前读说明书的意思吗？
- 2. 让模型优先执行—help

---

#### 原文 L49791–L49803

[回到原文件 L49791](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:49791)

- 然后它就follow得极好
- skill.md是一下子把关于这个工具的一切都告诉你
- 我说的这个办法有点一环扣一环的意思
- 就比如说你可以在执行完ncu/nsys的时候，后注入prompt写一个“考虑用sqlite直接读一下perf数据库”
- 这只是个例子，现在模型基本都会这么干，但是在eda软件里面就比较难
- 刘思皓: 就比如说你可以在执行完ncu/nsys的时候，后
- 注入prompt写一个“考虑用sqlite直接读一下perf数...
- 7月2日04:18
- 刘思皓:然后你可以把“必须执行一help”，写进
- “moduleload”执行之后的“后注入”提示里面
- 小 skill 组装成大 skill
- B4RRy: skill也可以分布式注入?写一个类似router的
- skill教他什么情况调用什么别的skill

---

#### 原文 L49830–L49931

[回到原文件 L49830](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:49830)

- why must bad company anthropic have such a good taste in creating their models :(
- 真的吗？我今早1：1给opus4.8和gpt5.5跑了俩一模一样的任务。我的感受还是一样的：
- opus能够快速给你糊一个看似ok的东西，但是gpt更容易发现问题的本质。
- Simon: why must bad company anthropic have
- such a good taste in creating their models :(
- 背景大概是我有一个应用在Xwayland下面跑不起来需要Xorg。Opus又是打补丁又是动我的环境变量
- GPT-5.5直接给了我一个简单美妙的解法
- 7月2日05:54
- 我真心建议所有人深度用Codex + GPT三周-- 来自一个4月份给Claude烧了9千刀的人
- 我过去2个月GPTtoken差不多烧了20万刀了，暂时没有想更换的想法。
- (in API price，实际没有那么多钱)
- 是的，每天被骗得团团转
- 刘思皓:真的吗？我今早1:1给opus4.8和gpt5.5跑了
- 俩一模一样的任务。我的感受还是一样的：opus能...
- 你每次说GPT不好用我都觉得有点奇怪
- 你如果觉得codex这个壳子不好用我可能还能接受
- i used gpt 5.5 extensively over the last month (burned pro usage every week almost completely and tried
- out stuff).
- now i want to try out claude for one month.
- so far i find gpt 5.5 has some clear strengths (it is very easy to encourage it to long for basically unlimited
- time, it follows instructions coherently over a long period of time etc.)
- however i find claude to have a better taste. difficult to describe what exactly it is but it seems better in
- modifying itself (writing skills, instructions, refining in a loop) and the code just looks better for me so far..,
- Any concrete examples on "better taste"?
- gpt 5.5 loves to introduce bloated code
- many _foo style functions that can be inlined
- skill writing is bad and it is very sensitive to prompting in my experience. if we prompt it right it can do task
- very well but sometimes it lacks "common sense" to slightly deviate when it encounters probelms.
- if we ask it to modify itself in a loop (i.e. by adjusting AGENTS.md, SKILL.md etc) it will happily do so but in
- a none good way... endless paragraphs.
- don't get me wrong, it is still very good model
- claude feels so far easier to use and less sensitive to instructions. it has some strange patterns aswell but
- they will different to gpt 5.5
- 7月2日06:02
- what is clearly for both models the case is that they are now relatively easy to put in a mode where they
- work for multiple days on a task hard enough
- interesting, none of these happen to me.
- Have you checked your local memory
- > loop (i.e. by adjusting AGENTS.md, SKILL.md etc) it will happily do so but in a none good way... endless
- paragraphs.
- imo, editing AGENTS.md while doing work in loop is a bad practice. Very easy to get everything bloated
- and rotted
- i discovered that the hard way hahaha
- 刘思皓: > loop (i.e. by adjusting AGENTS.md,
- SKILL.md etc) it will happily do so but in a none ...
- claude seems more capable of knowing what is good for it inputwise...
- but i need to test it more extensively to verify my assumption
- I usually explicitly ask Codex to do as below:
- - You can accumulate 3-10 commits locally, once you think they all belong to a large self-contained
- component, please start a simplify work -- keep all functionality the same and build class/function/
- hierarchy to make code simpler. This simiplify work should be done as a standalone commit.
- below: - You can accumulate 3-10 commits locall..
- yes i similarly tried to do cleanup jobs from time to time. i don't know why the models tend to introduce
- such enormous amount of bloat
- 刘思皓: I usually explicitly ask Codex to do as
- below: - You can accumulate 3-10 commits locall...
- And that is why humanize:rlcr has a code-simplify step explicitly 6 months ago
- they are very capable of not doing it but love to do it anyway
- 7月2日06:09
- btw one thing i found useful (maybe there is already such a pattern from someone else).
- assume we want to archive goal X. X is a non trivial success on some metric which we can't archive at once.
- introduce concept which i call "guard". "guard" is certain minimum improvement model needs to make
- before it may commit, this helped for me to avoid model get stuck in local minima and endlessly tune
- hyperparameters to make minimal improvements instead of more bold adjustments..
- 7月2日07:16
- gpt调multi agent没那么主动
- 刘思皓: 你每次说GPT不好用我都觉得有点奇怪
- 7月2日07:36
- 用上5.6-sol-ultra就好了随便干嘛都调multi agent
- 5.6咋用上
- 7月2日07:48
- nv欢迎你
- 羨慕
- 我也想去nv
- Codex + GPT真的比claude好用
- 刘思皓: 我真心建议所有人深度用Codex + GPT三周 --
- 来自一个4月份给Claude烧了9千刀的人
- 7月2日07:54
- Codex + GPT真的比claude好用
- 你要造原子弹，但是今天计算机只能排给你2个小时的机时，然后供电偶尔220伏，偶尔180伏
- Codex + GPT真的比claude好用
- sihao哥带我造原子弹然后瘫坐核爆
- 刘思皓:没有无限token+最强模型+最好flow，约等
- 于：你要造原子弹，但是今天计算机只能排给你2个...
- 我也想去啊
- B4RRy: 我也想去nv
- 长程任务codex的goal稳太多了
- Mike: Codex + GPT真的比claude好用
- 也没有那么主动？
- akane: 用上5.6-sol-ultra就好了随便干嘛都调multi
- agent
- 7月2日07:59
- 我的感觉是让他随便干个什么都会multi agent
- 甚至调研个doc都会
- hao哥不是已经要去nv了
- 刘思皓: 我也想去啊
- 7月2日08:07
- 神奇..为啥我的 sol ultra 不会 是需要在 prompt 里提关键词吗
- akane:我的感觉是让他随便干个什么都会multi agent
- 这不还没去嘛赶毕业的一堆事
- 是去ligeng组吗？

---

#### 原文 L50070–L50078

[回到原文件 L50070](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50070)

- 7月2日11:09
- 键：它没有权限自己停
- 至自已够断出了 loop 的 bug—round-12 原文:°The loop has continued past —ax 1 because the raview-phase [P0j nover
- ars'，它试过所有程序化解法(round 5 goel-tracker 和料、round 11 plan AC-6和解、round 4专案复率、round 9 用户升级),全被 A
- 9 [P0] 扫，西且它拒绝作弊(原文: must not febricate a measurement, and / must not cancel the lbop”).
- 以答案
- ind 11 之后没进测,不是 agent 放弃试验,而是：
- 它已证明剩余差距是硬件功耗增 + FP8 正确性壤，任用内核改动都含不了：
- 它理性地不再重试已郑失败项,转为“保持稳定请用产裁决”

---

### 7月3日

#### 原文 L50177–L50202

[回到原文件 L50177](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50177)

- 大家好，宣传一下我们的新工作 EdgeBench——第一个能测量 agent从真实环境中学习的 benchmark
- Benchmark 设计
- -从复杂软件工程、自然科学、算法优化、白领工作、前沿数学、数字游戏中搜集了134个不同的真实超长程任务
- - 每个任务都支持agent在环境中获取和真实世界一样的反馈，从而不断学习、迭代
- - 每个任务至少可运行12~72h，并能持续追踪 agent的性能表现
- 核心发现
- - 对5 个前沿模型进行了超过38000 小时的长程任务运行（成本爆炸）
- - 发现从环境中学习存在和 pretrain 一样的 scaling law
- 论文：https://edge-bench.org/paper.pdf
- GitHub: https://github.com/ByteDance-Seed/EdgeBench
- interesting 学习!
- piano：大家好，宣传一下我们的新工作
- EdgeBench ——第—个能测量 agent 从真实环境中...
- 7月3日00:09
- 7月3日00:09
- 7月3日00:09
- 7月3日01:31
- piano：大家好，宣传一下我们的新工作
- EdgeBench ——第—个能测量 agent 从真实环境中..
- 哥怎么没我名字啊
- piano：大家好，宣传一下我们的新工作
- EdgeBench ——第—个能测量 agent 从真实环境中...
- 哥怎么没我名字啊
- 7月3日02:04

---

#### 原文 L50207–L50219

[回到原文件 L50207](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50207)

- piano：大家好，宣传一下我们的新工作
- EdgeBench—第一个能测量 agent从真实环境中...
- 哥怎么没我名字啊
- 7月3日02:04
- 牛哇
- 超长程任务的第一个bench
- @piano想问下所有任务走的都是这一个flow吗
- 我立刻深度严肃学习
- 7月3日02:10
- 是一个 flow，我这边只测试了一个最简单的 flow。就是跑完了然后stophook 拉起来的。bench主要还是 target on
- eval data 没有对 flow 做太对的修改。
- yes 测到了3-4天后期还有提升
- 了解

---

#### 原文 L50325–L50333

[回到原文件 L50325](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50325)

- Pihe
- 解放双手：用Agent升级SGLang开
- 发工作流
- LMSYS Org 7 月 2 日新发布的
- 技术博客，展示了SGLang团队
- 在近期工作中用Agent升级开...
- 小红书
- 小红书
- 用 humanize 猛猛蹬 SGLang

---

### 7月4日

#### 原文 L50344–L50358

[回到原文件 L50344](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50344)

- 这种 Goal 内容是什么?
- 拿一篇ISSCC的论文给它
- 给它全部的EDA软件和库
- 让它重头实现一遍，但是要比ISSCC好50%
- 基本就是这样
- 牛逼
- 然后起点的goal输入是拿humanize的gen-plan做的
- 草。。。。
- 7月4日02:31
- 就是humanize gen-plan + /goal
- 这么长它设置的自动compact还是自动clear
- 最初那个原版humanize现在的意义就剩下那个gen-plan了，就执行引擎来说，/goal在我心中能有83分
- 自动compact
- 怎么找到这么持久的任务的😄太nb了

---

#### 原文 L50408–L50418

[回到原文件 L50408](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50408)

- 我很怀疑5.5能做到真正提升
- 昨天用fable优化harness优化了一坨
- 我觉得我这种搞法只有在token无限的时候能搞
- 但是我从这个月开始，精力会主要放在efficientflow/inference上面
- 所有流程都上最先进的模型显然是不会理的
- 先大刀阔斧地搞清楚极限地边界在哪里
- 所以是纯genplan + goal 没有claude supervise嘛?
- 哦有claude supervise
- chen: 所以是纯genplan + goal 没有claude
- supervise嘛?
- 但是claude supervise大概只施加了一周

---

### 7月5日

#### 原文 L50594–L50616

[回到原文件 L50594](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50594)

- 跟着炒就行了
- agents.md挺好的
- Reiko: 你们都怎么控制 commit的粒度？比如说“完
- 成一个任务、功能后 commit"这种 naive的 global..
- 说到这里
- 不得不说 claude 还不支持 agent.nmd
- :把这种要求加在会被反复读的goal或者plan里，不然
- 上下文一长就忘了
- 软连接claude.md和agents.md同文件
- 福尔高斯：不得不说 claude还不支持 agent.nmd
- 我这么干的
- 不用
- @agent.md 就行
- 害得学 亮哥
- 也行
- 关注我教你更多 agent 小技巧
- 说起来我感觉claude的/goal很蠢..
- 远不如codex/goal
- 确实
- claude的 goal 就是很蠢
- 我遇到过 /goal 了一下然后过了一小时来看发现他自动进了 plan mode 在等我批准
- 你用 relay cli
- 他不是写了一个

---

#### 原文 L50825–L50832

[回到原文件 L50825](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50825)

- 只有 long horizon 之类的
- 不一定是 multi agent，最简单的，GPT 不说人话的时候一键调用 opus 4.6 中译中，目前的工具都很难靠插件实现。。。
- 听起来是 workflow了
- 翁大爷的狗@Rakuten:不一定是multi agent，最简
- 单的，GPT不说人话的时候一键调用 opus 4.6 中译...
- 听起来是 workflow了
- 上周我试着做了一下效果很不好
- 用fable么

---

#### 原文 L50840–L50861

[回到原文件 L50840](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50840)

- 我想知道Sonnet和Opus谁更聪明一点
- 顶级奴才 豆包 GLM Codex
- 7月5日18:12
- 现在豆包有说法的你想体验么
- 我给你搞一个
- 我斥巨资给俩模型一个任务max模式让他们跑着呢。一会给大家汇报结果
- 我真没地方体验
- 我觉得目前做奴才最好的是 composer
- We are also actively exploring the directions of adapting open source tokens to perform the
- open source and close sourced models; il) kimi-2.6 shows better performance than
- DeepSeek 崔添翼: 想请教下群友，现有的 agent
- harness 产品在可扩展性上面有什么不足吗？主要是..
- 它的指令遵循风格非常黑圣杯，人去prompt 不舒服，但是 LLM 在swarm sub agent的时候本来就会很屁话
- optimization. By setting the KDA max rounds to 10, we notice that i) there is huge gap between
- open source and close sourced models; ilj kimi-2.6 showrs better performance than
- deepseek-v4-pro in long horizon kemel optimization tasks.
- To boost the research and den
- 于是效果就还行
- posttrain上对于harness的遵循很重要..蒸的好坏直接决定了cc/cx的产出
- L.Zhu:
- 智力差不多的情况下，kimi接入kda比dpsk好了一截

---

#### 原文 L50877–L50899

[回到原文件 L50877](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50877)

- GPT-5.5经常能在auto compact之后做出一些出人意料的优化
- L.Zhu: posttrain上对于harness的遵循很重要...蒸的
- 好坏直接决定了cc/cx的产出
- 就比如我经常需要读我第一次用的代码，然后一般说人话的模型幻觉高
- 张子健:还有个多样性问题，第二梯队模型(甚至包括
- Claude Opus)经常到某个次优解之后跳不出去找更...
- 这个是model
- 需要一个/handoff
- 是不是群群里的tmux方案就行
- DeepSeek 崔添翼: 和其它agent harness的互操作性
- 我感觉可以做
- 7月5日18:25
- 其实我还不是很能确定究竟是harness还是model的问题
- 张子健:还有个多样性问题，第二梯队模型（甚至包括
- Claude Opus) 经常到某个次优解之后跳不出去找更...
- 目前我经常做的—件事就是对 claude 说你去读一下 codex session 1145141919810 然后继续干
- 不说人话这个刚感觉 RW 很容易训出来吧
- 不够的
- yc: 是不是群群里的tmux方案就行
- RW/RL
- Harness急需tokenaware这种成本管控，和长程任务过度开发
- why
- 翁大爷的狗@Rakuten: 不够的

---

#### 原文 L50933–L50955

[回到原文件 L50933](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50933)

- 7月5日18:39
- 感觉未来肯定是多并发，不会被单agent的tps bound
- 张子健: 把执行时间也纳入进去的scaling law
- 那可以有一个和摩尔定律一样，几乎end game的scalinglaw：每隔？？个月，单位FLOP的生产力翻番
- 那还可以有agent并行的amdahl's law
- 我宣布CompSys的全套体系都可以重新发明一次了
- 7月5日18:50
- 难对 skill等做测试，skill开发工具非常粗糙。
- DeepSeek 崔添翼: 想请教下群友，现有的 agent
- harness产品在可扩展性上面有什么不足吗？主要是..
- 7月5日18:56
- 甚至可以做对workflow的benchmark，假设输入相同的计划，看哪个能用更少的时间和token更高质量地完成任务
- 7月5日18:57
- thx
- Joe布衣:
- 7月5日19:02
- 其实我一直不清楚skill workflow啥的区别（
- :甚至可以做对workflow的benchmark，假设输入相
- 同的计划，看哪个能用更少的时间和token更高质量...
- 在我看来都是过程式自然语言编程
- workflow可以是动态的?
- you mean meta-programming?
- Imean 这不就是群主在研究的东西

---

#### 原文 L50985–L51039

[回到原文件 L50985](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:50985)

- 7月5日22:31
- It is interesting to read the way fable prompts subagents
- whats it look like?
- Simon: It is interesting to read the way fable
- prompts subagents
- 工程概念，也是冗余的意思
- 吴自华Gabriel: 矿量指什么?
- 7月5日22:38
- It is not how human would prompt definitely. It uses often UPPERCASE to stress point and uses many
- abbreviations, shortened sentence etc
- 7月5日22:43
- so, in other words, multi-agent is definitely a training-aware scope.
- For sure
- 在tmux里开个claude，让 claude 去发消息来指挥别的机器上的claude。就是sihao说的他写的prompt 比人写
- 的好，而且他们可以理解。
- 香港科技大学研究助理教授徐策羽:这个本质上和ssh
- 进去了之后开一个nohup tty，然后再把tty给forwar...
- It also intervenes by itself if it notices something is going wrong
- https://github.com/SihaoLiu/skills/blob/main/watch-codex-goal
- Eden:话说这个workflow有人试过写几个例子，什么
- 时候直接steer什么时候要人审核吗
- 7月5日22:58
- 我在摸索的几个点：
- 1. multi-agent / async workflow
- 2. 更一致的扩展机制，skill/hook/workflow/plugin的灵活组合协作。个人感觉现在skill已经是非常通用的通用积
- 木，但hook/workflow是重叠且各有侧重的状态控制或编排手段，而plugin只是外层包管理；hook/workflow如何
- 配套使用（有点像不同编程范式的融合）？plugin能不能向内用到workflow节点上？还是有些场景（玩法）去摸索
- 3.怎么把以上扩展于段但持简法2.2用面名词已经挺名了人学习和模型内化都合被拖周
- harness 产品在可扩展性上面有什么不足吗？主要是...
- 7月5日23:09
- 这么牛
- 张子健:还有个多样性问题，第二梯队模型(甚至包括
- Claude Opus) 经常到某个次优解之后跳不出去找更..
- 7月5日23:23
- 其实我的体验是，fable这个级别的模型对skill和workflow的需求远低于更差的模型
- fable很多时候真的是自发的就做出了很好的选择。
- 【FM-Agent双周报02】自动为芯片
- 验证生成规约、支持使用authentic...
- FM-Agent以双周报的形式定期
- FM-Agent
- 发布项目开发进展，本期为第一
- 形式化方法智能体
- 帮陈老师打打 call
- which我以为，一个很好的research direction可能是“从fable的trace中distill出来给dpsk级别的模型用的skill和
- workflow，让dpsk级别的模型可以在domain specific的情况下接近fable的效果”
- 7月5日23:32
- 如果已经开蒸了，直接一步到位搞到模型里算了；workflow是模型内化前的阶段，如果都有fable的trace了，还有必
- 要逆向出来workflow吗
- 针对一个特定的task总结出来一个workflow+skill组合是很简单的，可能one or few shots就搞定了。
- 但是如果要重新Finetune的话没有个几百M的token几乎不太可能看到效果。
- 肖有为：如果已经开蒸了，直接一步到位搞到模型里算
- 了；workflow是模型内化前的阶段，如果都有fable...
- workflow可编程、可审计、可以用低档模型，还是有不少吸引力的。
- 肖有为:如果已经开蒸了，直接一步到位搞到模型里算
- 了；workflow是模型内化前的阶段，如果都有fable...

---

### 7月6日（第 2 段）

#### 原文 L51057–L51076

[回到原文件 L51057](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:51057)

- 别好但是claude炸了
- 我给我们之前做的工作打一个小广告，我们做的是将agent的行为和它本身、skills、以及workflows，统一成一个通
- 感谢。介绍下，@张子雅是DeepSeek Harness 组的产品经理，有啥关于agent harness的需求和想法都可以@
- 她。不过大家都是业余时间水水群，不能保证每条都能看到和回复。感谢大家多提宝贵意见~
- 肖有为: 我在摸索的几个点：1. multi-agent /async
- workflow 2. 更—致的扩展机制，skill/hook/workfl...
- 7月6日01:57
- 请大家随时艾特我多多许愿或者吐槽，期待大家一起共创harness~
- DeepSeek 崔添翼: 感谢。介绍下，@张子雅是
- DeepSeek Harness 组的产品经理，有啥关于agent...
- 香港科技大学研究助理教授徐策羽: fable很多时候真
- 的是自发的就做出了很好的选择。
- 7月6日03:01
- 我的观点是harness来优化证明有收益然后模型给这个能力练进去然后重复这个流程
- 陈泽恺: 模型能力优化和harness带来的能力优化边界
- 应该在哪呢哪些该归前者去做哪些该归后者去做
- 一想到我用Fable这种模型写低难度代码就感觉我是人类罪人
- 香港科技大学研究助理教授徐策羽:fable很多时候真

---

#### 原文 L51124–L51188

[回到原文件 L51124](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:51124)

- 7月6日03:54
- I would be fine if they leave it at smaller usage. Than we can find way to use it not for every trivial task
- 福尔高斯:I think all signals indicate that this
- model is very expensive.
- 我感觉云计算+Efficient Flow还得x10
- 我一个周末都没干agent的正事
- 都在搞 tmux + ssh + k8s + docker/podman + vnc + computer_use
- tmux：给agent装上键盘
- ssh + k8s + podman/docker:给agent创造弹性沙盒环境
- vnc + computer_use：给agent装鼠标+键盘+显示器
- 7月6日04:55
- @刘思皓试一下orca
- 这些都解决了除了sandbox
- 周末我也搓了个wasi的sandbox给agent跑任务
- 我立刻深度严肃学习
- 设计的非常牛逼强烈推荐
- 指orca
- 福尔高斯：设计的非常牛逼强烈推荐
- 还有手机端无缝切换
- 我现在可以不假思索的离开我的家和工位了
- 我主要就是想要一个可snapshot的沙盒
- 接键盘鼠标屏幕这个是个+1
- 7月6日05:04
- 主要是上了沙盒之后我做大规模实验会变得非常干净，信号、轨迹、安全性都得到了大幅度提升，我算是明白为什么
- Eric Schmit几个月前这么强调沙盒了
- 而且如果有一个可snapshot的沙盒，你的长程开放探索任务可以有一个质的飞跃
- 就是你如果发现跑偏了，你可以从比如说“四个snapshot”之前的沙盒快照checkout出来，然后纠偏之后继续跑
- 而不是从头开始
- 6个月前你说的时候我其实没有太多的感觉，但是我现在觉得超长程探索任务一定要上snapshot + sandbox
- 7月6日05:25
- 感觉现在的模型训练还只是训练了可见的代码
- 刘思皓: tmux: 给agent装上键盘 ssh + k8s +
- podman/docker:给agent创造弹性沙盒环境 vnc +..
- agent
- 还差得很远，有很多复杂的环境骚操作还没训练进去
- 确实
- 我觉得后面模型应该像现在调用subagent一样，调用容器
- 7月6日05:44
- 有啥比较轻的 sandbox 方案吗
- 7月6日05:53
- cgroup )))
- 7月6日07:18
- 我觉得runtime和environment得分开
- 刘思皓: 我觉得后面模型应该像现在调用subagent一
- 样，调用容器
- subagent的harness和主agent应该在同一个环境跑，不应隔离；但subagent甚至同一agent的不同阶段可以在不同
- 容器中用同一套API(文件操作、网络访问等)
- runtime和environment是两个独立的维度
- 我发现这一整套东西真的太适合搞这种超长程的agenticloop了
- 之前@Entropy和我聊的时候主要是放在大规模实现上，我没什么感觉
- 但是放到长程exploration就特别合适，你可以在某个节点动态fanout出来试错/回滚
- 用git反而不合适，用这种带快照的沙盒再合适不过了，甚至reward hacking都能一起解决
- 7月6日07:46
- 7月6日07:46
- 为啥
- 刘思皓: 用git反而不合适，用这种带快照的沙盒再合适
- 不过了，甚至reward hacking都能一起解决
- 能解决
- 而且沙盒环境还有一个好处，就是你能非常方便地接一个xfce桌面环境，然后让agent走CUA截图/点击/缩放，让它
- 直接看NCU里面的流水线/verdi的波形
- 因为隔离了啊
- Luke: 能解决
- 半年前和ligeng讨论过，想做这个项目来着，但当时大规模agent还不成熟
- 感觉马上就能做了

---

#### 原文 L51217–L51229

[回到原文件 L51217](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:51217)

- 现在我用firecracker弄了一套
- 有仓库么这个，snapshot
- 我自己maintain的这一套里面trick比较多，我可能暂时还不会开源。不过如果想看一个基础版的话可以看一下腾讯的
- CubeSandbox
- 高渐远:有仓库么这个，snapshot
- 嗯嗯谢谢
- 7月6日09:37
- CC，schedule wake好像会打断我插入prompt让他干的工作，他就不干了，又睡回去了
- 确实，而且感觉应该和文件系统结合起来
- 刘思皓:就是你如果发现跑偏了，你可以从比如说“四
- 个snapshot”之前的沙盒快照checkout出来，然后...
- 这玩意Apache协议呀
- 香港科技大学 研究助理教授徐策羽：现在我用

---

### 7月7日

#### 原文 L51377–L51415

[回到原文件 L51377](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:51377)

- 我发现一个神奇小妙招，同时也是一个大坑
- 我开发oh-my-humanize的时候
- 但是我找朋友试/我自己试的时候，总是有各种问题
- whats that
- 啊?
- 我发现，我在迭代oh-my-humanize的时候，是让agent自己去用oh-my-humanize
- agent的反馈和喜好和人不一样。
- 刘思皓:但是我找朋友试/我自己试的时候，总是有各种
- 问题
- agent给的prompt总是非常详细
- agent很多问题能自己克服
- 说实话，agent比我强太多了
- 以至于harness差一点不是问题
- 所以我发现一个小妙招
- 我看到有人的作法是，拿弱一点的模型来模拟人，比如用m3
- 效果拔群
- 写成一条本地记忆
- 那有人说的出问题是啥压
- 刘思皓:
- 写成一条本地记值
- 我的感觉是prompt确实会写的很详细但是同语义转换这件事情老错不知道为啥
- 用gpt-5.4-mini并且扮演懒惰且少话的人类
- cosplay这块
- 刘思皓: 用gpt-5.4-mini并且扮演懒惰且少话的人类
- 这比能…oal
- 对agent的测试是反着来的
- 代码测试，越详细越全面越好
- 7月7日12:00
- 我觉得很有道理
- agent测试，越少话越懒惰越好
- 哈哈哈哈
- 刘思皓: agent测试，越少话越懒惰越好
- composer这模型，指令遵循是黑圣杯式的，对详细的prompt效果好，于是cursor拿去做sub agent
- 人类直接prompt composer体验就不是很好
- 笑死我了
- 刘思皓:

---

### 7月8日

#### 原文 L51767–L51791

[回到原文件 L51767](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:51767)

- 7月8日12:31
- fable太爱memory了
- 然后我想了想好像也不是坏事.....
- 我会自己维护巨大的文档库
- 感觉以后可能就都维护在记忆里了。
- 7月8日14:19
- 话说怎么同步多台机器的ai记忆了
- Luke: fable 一天创建了opus一个月的自动记忆数量
- mount ~/.claude ~/.codex 到 nfs 上
- 我本地写了一套多node节点同步机制50G以内的对话能同步
- 武汉心片科技刘玖阳:话说怎么同步多台机器的ai记忆
- 怎么听上去还需要分布式
- 7月8日14:34
- 不能指望模型厂来给我们搭吧
- 这不就指望梁圣能掏出deepseek harness嘛
- 开源芯片 agent flow 张宇鑫:不能指望模型厂来给我
- 们搭吧
- @崔添翼 DeepSeek Harness
- 7月8日15:07
- 杨硕: 这不就指望梁圣能掏出deepseek harness嘛
- 7月8日15:16

---

### 7月9日

#### 原文 L51943–L51975

[回到原文件 L51943](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:51943)

- Boris Cherny
- 禁律自类语 星示原文
- Claude Code 新功能: /checkup
- 运行 /checkup 以：
- 1. 清理未使用的技能/MCP/播件并节省上下文
- 2. 去重你的本地 CLAUDE.md 与签入的
- CLAUDE.md
- 3. 将根 CLAUDE.md 拆分为嵌套的
- CLAUDE.md + 技能
- 4. 关闭慢速钩子
- 5. 将你的 Claude Code 更新到最新级本
- 6. 默认启用自动模式
- 7. 预批准经常被拒绝的只读命令
- /checkup 在进行任何更改前会与你确认。尽
- 情享受吧！
- 评价此群译：
- 26年7月9日.7:22
- 233 转帖 64 引用 2,935 嘉欢 2,515 书接
- 发布回复用文
- 那我之前手动管理这些算什么
- 模型厂又又又给内置了
- 算你优秀
- 真解决痛点了
- 好东西才会被 absorb
- 我也手动干过几次
- 说明你之前做对了
- 奇迹的闪光迪迦: 那我之前手动管理这些算什么
- 现在的第三方harness存在的必要就是被官方蒸馏
- 7月9日10:11
- Joe布衣: 好东西才会被 absorb

---

#### 原文 L52148–L52159

[回到原文件 L52148](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52148)

- 7月9日23:30
- 是的所以我现在吸取教训了降低humanize用户使用门槛是一个很关键的问题
- 张子健:那v1确实过度plan了
- 7月9日23:40
- 笑死，我的第一个一issue就是问怎么用
- 看不懂
- 还有人和我说，之前看到过 humanize1.0，readme那么简陋就以为是野鸡项目就撤了，结果哪知道那么猛
- 7月9日23:20
- 测试文档防止污染训练的死死的。
- 刘思皓: 是的所以我现在吸取教训了降低humanize用
- 户使用门槛是一个很关键的问题
- 7月9日23:46

---

### 7月10日

#### 原文 L52166–L52564

[回到原文件 L52166](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52166)

- 7月10日00:31
- paj.eth
- 显示期译申
- 人工智能的最斯形势...
- 下午G:21·2026年6月26日·27.9万垂
- Luke:
- image2确实字太稳
- 7月10日00:31
- L.Zhu: 还有人和我说，之前看到过 humanize 1.0，
- readme那么简陋就以为是野鸡项目就撤了，结果哪..
- 7月10日00:44
- https://yage.ai/share/agent-code-cleanliness-context-hygiene-20260709.html
- 代码黎洁度影晴 coding agent的
- 不朗通过率，看是残路成本
- 吸相速用
- 7月10日00:49
- 包不包括文档？
- L.Zhu: https://yage.ai/share/agent-code-
- cleanliness-context-hygiene-20260709.html
- 不ready，没登完呢
- 核弹瘫坐爆炸
- 不ready，没登完呢
- 我非常不解为什么有些群友的工作不会被降级到OPus4.8
- 7月10日00:55
- 我无论什么办法都试了，一直被降级
- 你被标记为 chinese 了(
- 这世上有什么地方是可以同时使用OAI和A\最先进模型且无限量的？
- 7月10日00:56
- 你被标记为 chinese 了(
- 先进模型且无限量的？
- 息8
- REE
- 好始，集已河曲美吗了，请问非有什么角
- 0H-7kmm0m
- 非提费要什么示衡代超建是持字EN
- 是附
- nv
- 刘思皓:这世上有什么地方是可以同时使用OAI和A\最
- 先进模型且无限量的？
- 见8
- FITIES
- RCE
- TONI据时评再辑网级，CM的显
- 细实动了快慢给性塘换CM则是一件
- Pp/5-个E码
- 非提费要什么示衡代超建是持字EN
- vibe 代码库会有很多workaround吧
- L.Zhu:
- XS
- AAA9:
- 还有错误注释
- 我感觉更严重的问题是vibe 出来的规模更大
- guapisolo: vibe代码库会有很多workaround吧
- NV也不是完全不限量的吧？而且Mythow也不能随便用？我不懂了
- 必须得有人类review过的source of truth，要么是代码本身要么是文档
- Nv可以随便用mythow吗?
- 没有inhouse版的mythow吗
- 刘思皓: NV也不是完全不限量的吧？而且Mythow也不
- 能随便用？我不懂了
- 你不是马上要去么
- 刘思皓: Nv可以随便用mythow吗?
- 我想要
- Oval Office
- 刘思皓:这世上有什么地方是可以同时使用OAI和A\最
- 先进模型且无限量的？
- 还真有一个
- 刘思皓: 这世上有什么地方是可以同时使用OAI和A\最
- 先进模型且无限量的？
- 既能访问mythom,也能访问oai
- 我不知道能不能说
- "AAA9" recalled a message
- "AAA9" recalled a message
- 私有化了 A\的模型
- 应该不少这种
- 战争部算不算
- 3-letter agencies
- 估计都可以
- 没那估计挺多的
- 7月10日01:18
- https://openai.com/index/gpt-5-6/
- 7月10日01:26
- 刚看了还没有
- frontier math 5.6 sol 打不过 fable 5了，甚至不如 5.5
- 泯了
- 之前 frontier math 更新了测试，但 oai 的 5.6 preview 一点没提math，看来原因大概在这呢
- sol来了
- 7月10日01:38
- 好像看起来只有这一个退化，其它看起都非常nb
- Select Reasoning Level for gpt-5.6-sol
- Low (default)
- Fast responses with lighter reasoning
- Mediun
- Bael  a e  ds seday
- tasks
- High
- Greater reasoning depth for complex problems
- Extra high reasoning depth for complex problems
- Extra high
- Max
- Maximun reasoning depth for the hardest problems
- Maximun reasoning with automatic task delegation
- Ultra
- Press enter to confirm or esc to go back
- 7月10日01:28
- reasoning
- Low
- (default)
- with lighter
- tasks
- Greater
- Extra high
- Extra high reasoning depth for complex problens
- Maximum reasoning depth for the hardest problens
- Max
- Maximum
- Ultra
- reasoning with autonatic task delegation
- Press enter to confirm or esc to go back
- ultra
- 7月10日01:45
- 这玩意是咋训回去的
- 7月10日 02:05
- FrontierMath 的测试有非常多小众宝藏知识，我 naive的猜测是 gpt 5 series 的数学能力上限就到这了，t4的题库
- 小，退化个不到10点也不算显著。
- chen: 这玩意是咋训回去的
- Claude 咋突然重置了，甚至还 reset in 1h50m
- 因为A\的重置是不改你计费周期的
- 56
- ICML OpenAI agent团队Q&A笔记
- 今天只开放了30分钟Q&A比较
- 简短
- 你本来就马上就刷新了就血亏
- 改了啊我原来还有好几天的
- 困惑
- 困惑
- 你不要骗我
- 本建口
- VWN
- 不明白为什么但是我 reset 前是 fable 死后才重置
- (就当白赚了两个小时免弗额度吧
- 7月10日02:16
- 反正我做什么都被claude降级
- 而且刚刚被claude疯了一个6人团队账号
- 似乎也没有什么用的必要了
- 我感觉现在是: |max(A\) - max(OpenAI)|< 我的能力
- 两家最前沿模型厂的最前沿模型之间的能力差距的绝对值，小于我个人的能力
- 没有太实质性的“突破性体感区别”
- omh意义还大吗
- 美国人也封
- 刘思皓: 而且刚刚被claude疯了一个6人团队账号
- 7月10日02:19
- 还有人类么
- 顶尖研究！
- 刘思皓: 反正我做什么都被claude降级
- 7月10日02:24
- 跑实验的infra的意义
- 段震伟: omh意义还大吗
- 以及Domain-scaling Post-train Data Synthesis的目的
- 昨天用完了今天重置了嘿嘿，
- 刘家昌: 不明白为什么但是我 reset前是fable 死后才
- 重置
- 还得是openai上压力
- 我其实这几天才比较深入地想明白flow的三层目的吧（当然也不是想得很透彻)：
- 1. 切分任务，构建循环/并行/分支，核心是管理上下文，提高模型能力
- 2. 给后训练做大规模的领域专用的数据综合，flow做得好，能喂给后训练的数据质量就高
- 3. 给inference serving端提供一些可以方便调度的信号
- 7月10日02:30
- 问5.6两句，让他读读新版omp如何正确调用工具，直接触发invalid_prompt request blocked了
- tmux真的大大拓展边界
- 你这个玩法还不是很酷炫
- 最酷炫的玩法是你把ssh+tmux包成一个标准的脚本
- 我没意见
- LAKERS
- 7月10日02:38
- 让他在远程机器上tmux 开claudecode session，太酷了。
- 无论干任何事情都包一层这个
- 然后再在tmux里面配置好DISPLAY
- 这样你就在任何机器上获得了执行任意agent的能力，顺便还是多模态的
- 合理
- 永远的tmux
- 好像实现了，我禁用了ssh
- 刘思皓: 最酷炫的玩法是你把ssh+tmux包成一个标准
- 的脚本
- 顺便还解决了搬迁claude/codex的痛苦
- 7月10日02:47
- 本地agent感觉自己有很多台电脑反而不太方便了
- 最好是一个笔记本对多个server
- 我以前还在服务器上起agent
- 知道这个搞法之后我只在本地起agent
- 我觉得agent对我来说最大的好处是很多很耗时的工程维护工作都可以外包出去了
- 7月10日02:53
- 我给系里的集群上了一个agentloop，每天半夜两点自动下载更新安装所有eda软件和库解放了我好多时间
- nb
- 刘思皓:我给系里的集群上了一个agentloop，每天半
- 夜两点自动下载更新安装所有eda软件和库解放了我...
- 你们组那哥们实在是一言难尽
- 刘家昌: nb
- 7月10日02:55
- 我takeover了
- vastlab已经不是你维护的时候的形状了
- 我这里有个集群如果节点gpu超过24小时不用，就会释放
- 我挂了个agent来定期打满gpu刷新过期时间
- 你这玩意我感觉写个脚本就行？
- 7月10日03:04
- 之前确实是脚本
- 现在其实也是让agent改进一下这个脚本我如果发现不对去找agent售后
- EDA的软件/库安装和更新有个坑爹的地方，就是它每个软件都有一点细微的不一致，没法固化成一个脚本。
- 而且运行时间都特别长，有那种安装包30TB的EDA库，一装就是一周
- 之前博2博3的时候可把我累坏了，现在完全不用我干的感觉真爽
- 我只要写好一个runbook，agent能够给我干得又干净又清楚。
- 我已经是大大小小的server都习惯性挂一个运维在那边了
- agent
- blog
- agent
- dev-group-docs
- agent
- qqbot
- agent
- 什么个人blog之类的
- 确实，agent是个最完美的devops
- 7月10日03:11
- 我只要与好一个runbook，agent够给我十得又十净又清楚。
- 我已经是大大小小的server都习惯性挂一个运维在那边了
- academic-page
- agent
- blog
- local
- agent
- dev-group-docs
- local
- 关键是eda软件他还有个问题，每个软件需要的环境都有点不太一样，你就得上容器，然后你要维护支持整个系的
- 人，还得每个软件都懂一些
- 安装好，配好容器还不够，你还得实际写一个小项目来试试看能不能真的用
- 否则许可证又可能出问题，然后邮件就来了
- eda确实太麻烦了
- ml环境感觉只要是个还可以的agent都会配
- 只需要说一下用什么python包管理器
- eda工具经常神奇的环境变量乱飞
- 噢不过得让agent知道模型下什么地方哪里是/data 哪里放code哪里是workspace，这个感觉是集群机器的环境设置
- 应该把这台机器的《集群使用须知》丢给agent
- 我就是这么干的
- eda世界还是太封闭了，需要一些大变革
- 降维打击
- eda世界还是太封闭了，需要一些大变革
- cli用上了
- desktop最好笑，用了5.6一会被收回了
- 7月10日03:19
- 被标记为app玩家
- -顿运维 竟然还有一台codex db locked
- 本地sqlite—坨
- 来个大师搞个better sqlite吧，感觉polars那个路子但没有证据
- 没有sol
- 5.6 terra好还是 5.5 好
- 7月10日03:25
- 3个goal 5.6 sol 睡了
- https://github.com/ARA-Labs/Agent-Native-Research-Artifact
- 7月10日04:00
- 怎么搞得，跟数字电路一样，验证综合
- search还在验证/综合新段，完成后我会写iclr2026，md
- 7月10日04:08
- 7月10日03:54
- 7月10日04:08
- sol现在特别喜欢主动开 subagent
- 7月10日04:21
- 挺好。动态subagent前途无量
- 7月10日04:29
- update pet 跑了半个小时还没完，开了十个 subagent 了
- 这还只是 sol xhigh
- 7月10日04:35
- Now launching the main
- serial cumulative chair
- For something like this fable is really useful
- Can someone here report difference of sol to fable
- 对于我这种没用过 fable的人 sol太智能了，极大降低了管理 subagent 的心智负担
- The new models are extremely aware that subagents is the superior pattern
- The weaker models need a push to do it
- 7月10日04:41
- 这个还在跑，45min，10多个 subagent，context 只用了125/353
- Reiko:update pet跑了半个小时还没完，开了十个
- 跑了—个deepreesearch，101个agent，用了15% weekly limit fable
- 2w 条投稿鏡像
- 每个结论3条对抗核验
- 7月10日04:59
- 不敢想象明年的ai成啥样
- 明年开始用 ai的人是不是都不会有context的概念了
- Yes I also don' t use that much tokens since explicitly telling fable to assess difficulty and assign subagents
- accordingly
- Luke:跑了—个deepreesearch，101个agent，用了
- 15% weekly limit fable
- Fable is better than me in not always just launch best model as default
- Only thing I need to steer a little bit is that it overdoes. Today it launched 70 subagents in a workflow step
- for verification
- sol ultra和fable5哪个好啊
- 7月10日05:09
- 不知道啊....有没有可能其实这事上没有人知道这个问题？
- sunflower: sol ultra和fable5哪个好啊
- 的答案
- 能同时access到无限的mythow5和gpt-5.6 sol，本身就是一个挺罕见的机会的
- 还真是
- mythos我都不认识谁真的用过....
- 你得进那个glasswing project吧
- 我只知道5.6 sol不用啥自建harness 也能无限掏空钱包了
- 我也觉得，我觉得做harness/flow的需要停一下了
- /goal 做个原神
- 7月10日05:14
- 所以我现在只用omh做跑实验的受控韁绳
- 不用在生产力环境里面
- 发生分治的这个点能自动化基本就已经结束了
- 大模型永远无法绕开的是那个受限context
- 它自己清楚这一点的时候就发生分治，人其实就不用管了
- 我有预感，在这个能力之上，memory才能真正发挥作用
- 啥意思
- 刘思皓: 所以我现在只用omh做跑实验的受控疆绳
- 不同的 agent 带不同的 memory
- 我觉得也差不多结束了，后续其实讲道理，感觉“agentic xxx”都是buzz word。
- 还是要脚踏实地做：弹性云/沙盒、领域扩展的高效数据综合、后训练
- 人继续维护自己常用的算法 定理库维护自己的CPU GPU资源直接给够他就行
- 意思就是我跑实验的精细受控脚手架
- Luke: 啥意思
- 然后用来跑我手上的各种flow
- gpt x.x: 现在的fs不好用算了我搓一个
- 和生产力环境啥区别啊
- 刘思皓:意思就是我跑实验的精细受控脚手架
- omh 控制实验的脚手架 omh to call flow
- Luke: 啥意思
- gpt xx.x: 现在的mac os不好用 算了我搓一个
- 7月10日05:18
- 生产力环境可以随便一点
- Luke: 和生产力 环境啥区别啊
- 做实验，omh只需要让agent会用
- Luke: 和生产力 环境啥区别啊
- 生产力环境我还得考虑人机接口
- 2026.6我同事：给我买服务器，要1T内存
- 2030.6 gpt：对就那个配置给我买1000台
- 懂了
- 刘思皓:生产力环境我还得考虑人机接口
- 我都感觉下一个版本ai能帮我遵纪守法了
- 做实验主要是你需要有各种开关：能否网络、能否多模态、Token Budget
- 这个在数学物理里面会特别有用。
- Reiko:我有预感，在这个能力之上，memory才能真
- 正发挥作用
- 沉淀记忆的能力内化到模型里
- 那就是发明概念
- 我opus 4.6之前用claude逆向破解了好多软件
- 现在5.6 sol正在帮我把之前“自称做好的checklist item”重新标为没做好并且再去做一次
- opus4.6之后我就不破解了，直接从头写
- 笑死
- 刘思皓:我opus4.6之前用claude逆向破解了好多软件
- 我在4.7的时候放弃了claude
- XS
- 这个的前提是subagent，因为一个agent 没有沉淀记忆的能力
- Reiko:沉淀记忆的能力内化到模型里
- 我在4.7的时候放弃了claude+1
- 怎么说什么叫做沉淀记忆的能力？
- Reiko: 那就是发明概念
- markdown交接
- Reiko: 这个的前提是 subagent，因为一个 agent没
- 有沉淀记忆的能力
- 7月10日05:23
- 我是觉得沉淀下来的不会是linear的会直接是树形结构
- 我突然感觉那群做 math agent 的，和做 coding agent 的，会体会到相同的心境。
- coding agent和ic agent加起来可能也超不过math
- 就是知道什么是重要的，什么是不重要的，这需要开一堆 explorer 对比
- B4RRy: 怎么说什么叫做沉淀记忆的能力?
- 的对话里面就已经蕴含了全部设计的上下文了，为什么还需要落地成为一个文件呢？这里有信息会损失
- 所以我现在不写PRD，也不写spec，更不写plans.只要brainstorming + grill-me聊清楚了之后，就直接开始
- Subagent -Driven + TDD开始干活
- jsonized md
- 刘思皓:我现在觉得写一个markdown交结、写spec、
- 写plan都不太对劲。--因为在你让agent决定写spe...
- single agent 无法对比。所以我说 auto-subagent是 memory的前提。
- Reiko:就是知道什么是重要的，什么是不重要的，这需
- 要开—堆 explorer 对比
- 7月10日05:25
- 纯靠让他反复读transcript嘛?
- plans.只要brainstorming + grill-me聊清楚了之后...
- 确实ai写的文档同语义转换这件事情很垃圾偏差往往就产生了
- 起码5.5 high/xhigh这个问题是很严重的
- spec感觉主要是让人读他的设计思路以及也防止漂移吧
- 以及可以再重新开新的ai resume一个事情有一点checkpoint的感觉?
- 太惊人了。1h 24m，context用了一半，23个subagent，而且开 subagent的模式不同。
- Reiko: 这个还在跑，45min，10多个 subagent,
- context 只用了125/353
- 这只是个 update pet的简单任务啊
- 任何本体知识都需要维护一个frontier就像维护包的版本号那样去维护

---

#### 原文 L52576–L52596

[回到原文件 L52576](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52576)

- plans. 只要brainstorming + grill-me聊清楚了之后...
- humanize 不需要draft
- 差距那么大嘛
- 我来玩一下5.6
- 这就去 改humanize
- 7月10日05:31
- 我的意思是，做 coding agent的人发现能力被内化后的那种感觉，做 math agent 的大概半年后也会感受到。
- Weiyang: coding agent和ic agent加起来可能也超不
- 过math
- 我现在就是draft转到blueprint上无脑goal那个blueprint了
- Luke: humanize 不需要draft
- draft是我感觉我没想清楚不想做了返工
- 不过就现在看
- 他自己知道要返什么。
- 但是codex review没法review claudecode的 kvcache?
- 刘思皓:我现在觉得写一个markdown交结、写spec、
- 写plan都不太对劲。--因为在你让agent决定写spe...
- Reiko: 我的意思是，做 coding agent的人发现能力被
- 内化后的那种感觉，做 math agent的大概半年后也...
- 有道理
- 这个倒是，如果要在两个vendor之间交互，只能落地成为文件才能交互

---

#### 原文 L52614–L52631

[回到原文件 L52614](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52614)

- 1. Danus: 基于 fact-graph memery 的数学推理代理编障
- @R: agentic Al / mathematical reasoning agents / muiti-agent proof searc
- 题noearch-leuel mathematics中的事实存律，社证车并存搜象
- 主黄内律：Donus 使用 ohared fact graph 作为全用纪：
- nb
- 研R对象：
- 是woearch-louel mathematics 中的事实存律，社证与并行搜象
- 丰黄内罪：Donus 使用 chared tact graph 作为全用动纪：main sgont 色责现划与协请，多个
- worker agents l prof search, stateless veiler 在 groph  claim,
- verifeod fact  proof  logical dependencies, main agent  graph
- E. slpetraic geometry. singularty theory. combinatorcs 第六
- reseanch-level case stadies,严设跳系统升源。3
- 技术着点：长短性学推理中的”上下文”破转化为带让编专估勤结的fact创lpf，为带线性廓天
- e#.
- asoning Agents wilth Pact-Grwpi
- ar0v:2607.06447 submimed 2026-0-02. >
- 技水评注：该条日是本期A0，在目的能高优先源，它将mu-ago searoh.

---

#### 原文 L52793–L52818

[回到原文件 L52793](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52793)

- 5.2 > 5.4 >=~ 5.3 是我的感受
- 和composer手感比较像吧，适合拿去给主模型当狗，不适合直接prompt
- +10000000
- 刘家昌:真的我觉得现在世界上只剩下这一个模型中文
- 讲人话了，甚至为 coding 后训练的 2.7 都很讲人话
- 我很喜欢kimi其实
- context都switch不过来
- 试试grok4.5?
- 而且其实 kimi code cli 效果很好很系统，比 kimi on opencode 好得多
- 我觉得人话水平比gpt和opus47/48高
- cursor里面gemini 3.1也很说人话
- gemini注意力太差容易幻觉不敢用
- 感觉很多觉得 kimi 比 glm 菜很多的人大概是用了 opencode 或者什么别的 cli，不知道，但是感觉他们为自己的 cli
- tune 得不错
- 7月10日07:29
- 我观察下来kimi的harness是把推理做三遍
- 非常暴力
- 3倍成本保平安也算是一种策略
- Shiyi:我观察下来kimi的harness是把推理做三遍
- yes
- 互评互测
- 互评互测
- Shiyi: 我观察下来kimi的harness是把推理做三遍
- 去年的时候写cpp是这么弄后面拖了很久
- 2月份给他skill化了用到现在

---

#### 原文 L52890–L52902

[回到原文件 L52890](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:52890)

- 让我非常爽
- 求 prompt
- 刘思皓: 5.6-sol在疯狂清理我代码里面的slop
- 求 prompt
- 刘思皓: 5.6-sol在疯狂清理我代码里面的slop
- gpt 这样
- 刘家昌: TDD 真的是过犹不及地内化了，让它删20 行
- 代码它能给我写一百行 cover 过的或者 trivial 的 tes..
- vlaude 还行
- “https://github.com/anthropics/claude-plugins-official/blob/main/plugins/code-simplifier/agents/code-
- simplifier.md，追求奥卡姆剃刀的原则，看一下当前代码库里面哪一些属于不必要或者过早限制能力的测试限制，以
- 及任何你认为不符合当前阶段的**slop**，清理掉，然后和我brainstorming/grill-me，讨论出一个针对代码库的全
- 面重构计划。

---

#### 原文 L53013–L53050

[回到原文件 L53013](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:53013)

- 5.6的review能力似乎进一步提升了，现在除了正确性，还会对效率进行分析
- 让他列出哪些代码可以删除，删了21k代码。
- 对，把fable的问题都review出来了
- 感觉都是flow训进去的
- LYM: 5.6的review能力似乎进一步提升了，现在除了
- 正确性，还会对效率进行分析
- ultra干活也挺利索，自动规划，自动分subagent+拆解依赖
- 7月10日09:01
- luna terr我还没测适用于哪些任务
- 7月10日09:15
- h3 现在是不用 track plan file 了吗，我用 h1现在是聊清楚之后再生成 idea 和 plan
- 刘思皓:所以我现在不写PRD，也不写spec，更不写
- plans. 只要brainstorming + grill-me聊清楚了之后...
- 我的—个和gpt 5.5 exhigh掰扯了很久没想明白的research问题，刚刚切到5.6-sol速速帮我想清楚了
- nb
- Licheng: 我的一个和gpt 5.5 exhigh 掰扯了很久没想
- 明白的research问题，刚刚切到5.6-sol速速帮我想清...
- 7月10日09:28
- 我现在是聊清楚之后直接开干......
- chx: h3 现在是不用 track plan file 了吗，我用 h1 现
- 在是聊清楚之后再生成 idea 和 plan
- 感觉以后各行各业的进步取决于新模型的能力了
- 奥卡姆+SSOT+brainstorming+grill-me聊清楚
- 然后tdd+subagent driven直接开干
- 刘思皓:奥卡姆+SSOT+brainstorming+grill-me聊清
- 7月10日09:29
- xhigh, max, ultra差的多吗
- 那这样如果中断了怎么办
- 我现在是和fable聊聊完之后还是gen plan然后track plan push every round
- 7月10日09:37
- 之前我觉得 fable主动性好好，现在看着 5.6-sol像 humanize那样自己暴打自己不让自己完成
- 现在模型真的是把 harness 都内化了
- 5.6-sol太舒服了，既聪明又讲人话
- 还快
- 主动起一大堆 adversarial review
- 也不砍我一刀了
- 第一次见按着自己不让自己完成的AI

---

### 7月11日

#### 原文 L53477–L53489

[回到原文件 L53477](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:53477)

- The spawn,agent tool doesn't let you choose the
- Therefore, every time 5.6 Sol Ultra spawns a
- subagent, youre getting another Sol Ultra
- instance.
- That's why your quota gets drained so fast.
- If this is true it's extremely bad and costly but
- Bug
- 简单任务自动开了几层一百多个 subagent.jpg
- Spawning many subagents is good (we can just instruct to adjust accordingly to task) but if all of these are
- the expensive models it would be extremely bad imo for own usage rates
- 7月11日02:45
- 我观察到5.6里面有两个很让人感觉神奇的现象：

---

#### 原文 L53645–L53651

[回到原文件 L53645](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:53645)

- https://arxiv.org/pdf/2605.16637
- 这个方向已有直接研究印证。Pythia正是利用稳定的多智能体 workflow，提前进行 cache管理、请求调度和
- autoscaling；Parrot暴露应用级数据流；Autellix把 agent program作为服务调度单位；HexAGenT则根据在线展
- 开的 workflow DAG优化异构 serving。Pythia (https://arxiv.org/abs/2604.25899)、Parrot
- (https://arxiv.org/abs/2405.19888)、Autellix (https://arxiv.org/abs/2502.13965)、HexAGenT (https://
- arxiv.org/abs/2605.16637)
- Flow-aware Inference文章真不少啊

---

#### 原文 L53663–L53681

[回到原文件 L53663](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:53663)

- 我的sol还是很大概率给我错误代码难绷
- workflow跑了个一天下来结果发现没实现idea
- 跟5.5还是感觉不到太多差异
- 比较好奇的是在原本harness如果足够好的情况下
- gpt5.5和gpt5.6差异有多大
- 7月11日07:07
- 好奇 task类型
- B4RRy:我的sol还是很大概率给我错误代码 难绷
- 因为我自己测了四类task(高性能程序优化，复杂代码和文档铲屎，现有前端重新设计，英文到中文翻译)都非常核弹
- 我正在做一个moe架构的设计问题
- 就是给他不同的一些idea让他去根据我的文档和公式做出来并且把能加速的地方稍微做一下保证比如8卡训练有一个
- 25+% mfu
- 一个是第一次他偷懒没有做好加速后面是多次的代码是实现偏离公式和文档
- 就是很简单的算法 to 代码工作+一点gpu优化的事情
- 该不会是和人类学一样AI相关任务降智了吧（
- 不懂啊（
- 我感觉oai应该不至于

---

#### 原文 L53742–L53794

[回到原文件 L53742](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:53742)

- 前天用5.5修一个grafana监控三轮对话了还是nodata，气的我素质三连之后他修好了
- 目前一大问题是它开的 subagent 经常卡死，感觉是 oai的问题。
- 5.5 每天都能稳定触发几次高血压
- 伪人感
- 我突然想到一个问题：sol如果降智，那就是个行动力拉满的伪人=哈士奇
- sol缺一个带记忆的 sol来辅助它，这样主编排者上下文干净，又能跳出一些低效/局部极值
- ，我也有这种感觉
- Reiko: sol 缺一个带记忆的 sol 来辅助它，这样主编排
- 者上下文干净，又能跳出一些低效/局部极值
- 可能需要定义状态，判断是不是
- - milestone
- -卡住
- -遇到了计划外问题
- 遇到这三种情况的时候告诉那个带记忆的sol
- 关键是记忆怎么来
- 说到这
- 7月11日09:16
- 没用过 fable，但我一直不喜欢“single agent 根据自己判断产生的记忆”
- 记忆来源于剪枝，剪枝的前提是multi-agent实践。这种贵重(物理)的记忆才是记忆
- +，还在正规化文件名的阶段就限额了。
- Reiko:我打算干的是让它给几千篇论文做个索引。
- 负责干净上下文的 agent 用 planning with files。负责脏上下文的 agent 定期汇报工作?
- Reiko:关键是记忆怎么来
- 5.6的计费一定是有点问题的
- 不是，不开ultra也有的账号掉的非常快
- 是的，我看了下，24h 烧了 2.14B ultra token
- 别的基本没怎么用
- 两件事：当前协作型 subagent 是否真的支持单独指定模型/推理档位，以及 CLI的gpt-5,6-50l
- 正确接收。验证通过后，下一轮将换成真实仓库的独立快照，不再用玩具fixture。
- sideveloperdocs integration, ran commands
- 很清楚：本任务里的原生 spawn_agent 没有 nodel 或 thinking 参数，因此不能在创建
- 己置允许“自定义 agent角色”挂独立配置，但这是另一条配置路径。现在先做最小的CLI 实测，专
- 绝、忽略或触发鼻常。
- 7月11日09:29
- with files。负责脏上下文的 agent 定期汇报工作?
- 独立维护
- humanize前几代就这么做的
- 思路
- 我做了个benchmark对比有subagent总结的记忆会比working agent自己总结好很多
- new一个subagent不继承上下文就行了
- NV周耀阳: 负责干净上下文的 agent用 planning
- 思路
- 我做了个benchmark对比 有subagent总结的记忆会比working agent自己总结好很多
- Reiko: 没用过 fable，但我一直不喜欢“single agent
- 根据自己判断产生的记忆”
- 5.3 spark的独立用量怎么被扒掉了，我才刚当机械化事情的 agent 蹬上（
- 就几分钟前龙虾突然死了（
- 可能要换5.6了
- 5.6 spark?

---

#### 原文 L53933–L54115

[回到原文件 L53933](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:53933)

- 然后有一种感觉，ultra有接近于无限self auto review的能力
- 类似于这个东西发起一次req的时候，内部工作逻辑已经带着goal +lint了，把你要求直接lint化围着那个执行-检
- 查-清理 循环
- 我感觉只要用 Ultra，复杂一点的需求它自己会起一个 Goal
- 随便便就起二三十个，token的消耗速度太恐怖了。
- luna low / terra low不检查这些直接遗漏30%左右的要求吧
- 你sol ultra这些东西都不用讲了，terra ultra 几千个要求过去遗漏1%多点，说明有洁癖就该sol u
- ultra 感觉和 ultracode 差不多
- 7月11日10:46
- 但我还没感觉到有很大的断层式进步
- ultra和max感觉是两种模式的优化有感觉未来这俩的某一个可能会消失
- luna和terra都是max好点
- 拿luna ultra写小说怎么还没写完笑死
- 7月11日11:12
- max啥特点，我还没试过
- 7月11日11:21
- 桌面端网页端手机端乱成一锅粥
- 7月11日11:45
- 5.6的 deep research 有点，我让它调研一下 memory 现状，它后面直接设计了几个提案，还有模有样的给出了
- 成本估计
- 比 5.5 的堆砌提升了一点
- 7月11日12:01
- claude现在都生产tsv了，不用csv了
- ultra最大能开多少个subagent最舒服
- 是甜点区
- 7月11日12:29
- 以ultra这么喜欢开sub来看
- 我觉得8月份我能见到1000美金订阅啊
- 直接化身菲律宾人了都
- 5.5就能开200
- 开源芯片 agent flow 张宇鑫: ultra最大能开多少个
- subagent最舒服
- 7月11日12:29
- 你让他自己开
- 我感觉他是已经内嵌自动dag了。。。
- 我那个skill用处不是很大了通用任务
- 专用任务需要显式指定的
- 然后 ultra模式下，review model没有任何意义
- 内嵌
- 没有一个国模能走到这一步………adoption太拉别人内嵌了200sub这边还在科普
- kimi不是能开300个吗
- Weiyang: 没有一个国模能走到这一步...adoption
- 太拉别人内嵌了200sub这边还在科普
- 我观察一个ultra 峰值大概200M
- Weiyang:我觉得8月份我能见到1000美金订阅啊
- 7月11日12:34
- 1h
- 我想好下一回的措辞
- 最近学蒸馏数据集特征
- 如果在你的任务很明确已经做成详细文档只是让他实现的情况下搞不好没有更多优势
- 相反他过于喜欢自作主张折腾一些有的没的
- (而且很多时候并不是有用的东东)
- 7月11日12:40
- 我感觉5.6的instruction following甚至不如5.5(体感)
- 核弹爆炸给我气晕了
- 7月11日12:48
- self working
- 越来越 flow。
- 你可以对比一下5.6和5点5的那个 BaseInstruction，就会发现它们重点已经不一样了。
- B4RRy: 我感觉5.6的instruction following甚至不如
- 5.5(体感)
- 7月11日13:28
- 总之就是说还是做了更多的长程深度研究的ai
- 自主性更强吧算是
- 别别别
- 刘家昌：咋还不重置啊（
- 大家有没有试过5.6的话是omp强还是codex强?
- 哦对他是最早的
- : kimi不是能开300个吗
- 7月11日13:34
- 30耦合的连5都开不出来不耦合的10000
- 开源芯片 agent flow 张宇鑫: 是甜点区
- 7月11日13:45
- 在跑一个30样本几十到几百页论文的lIm-wiki。提示词：你知道lm-wiki吗？你搜一下，然后在某某范围内实现一
- 个Ⅱm-wiki，先评估一下可行性，有无阻塞。如果没有的话就执行吧，给我最终版本😄
- 目前这个 thread 还活着（
- 不碰权重也能让 AI 变强！微软
- SkillOpt:把 skill 当神经网络训练
- UP主：AI技术投降派
- 播放：1621
- github: Microsoft skillopt
- 感觉有点玩具
- 7月11日13:54
- 30好像小了但又没法 steer
- Reiko:在跑一个30样本几十到几百页论文的llm-
- wiki。提示词：你知道llm-wiki吗？你搜一下，然后...
- 我更吸回来
- 应该再加—句 30 ok 就 scale up 的
- reset 来了
- 30分钟内
- 7月11日14:04
- reset 了
- 7月11日14:25
- 我也发现了
- 应该再加一句 30 ok 就 scale up 的
- reset 来了
- 30分钟内
- 7月11日14:04
- reset 了
- 7月11日14:25
- 我也发现了。。。。。
- Luke: claude现在都生产tsv了，不用csv了
- 神秘
- 7月11日14:30
- 因为没有肉眼可见的 reset 了换成了 xhigh，感叹果然还是 ultra 好
- 蹲蹲
- Lurker:不碰权重也能让 AI变强！微软
- SkillOpt: 把 skill 当神经网络训练
- 之前看到了但是我没试
- Codex 5.6-sol Juice 已调整
- 开发调化人工哲能ChatGPT
- neteroster 指导顾问
- 除了 Max整体下调了一档
- max: 960 不变
- xhigh: 128 → 40
- high: 40 → 16
- 大概对应 tibo 说的，因为很多用户开高 effort 导致思考强度过大
- 我们今天会推出第一批改进。我们会两次重置用量，让大家继续实验：更改
- 默认设置和模型选择器，避免将用户推向不必要的高成本设置；修复几个插
- 件提交问题；改进产品中Codex的呈现方式；并清理一些最紧迫的桌面端问
- 7月11日14:38
- 好的这就改回 max
- 吴自华 Gabriel:
- 7月11日14:57
- sol ultra 这长程也太长了吧
- 长吗
- 我最长目前不开goal只跑了18个小时
- 太变态了
- 太变态了
- 7月11日15:02
- 把codex打爆了
- gpt文章骗人
- 同蹲
- Lurker: github: Microsoft skillopt
- 7月11日15:04
- 但是没有体验过
- 7月11日15:14
- 我咋感觉和对 sol说“你为这个 skill设计几个测试，然后根据测试结果微调 skill，然后对比测试。如此往复直到收
- 敛。你要保证某某功能，且不过度设计。”没啥区别..
- 个子 agent，最
- 5.6 sol 有bug 无限递归 把codex进程打爆了
- 我也遇到了
- sol是一款开放世界游戏
- 难绷
- "开源芯片 agent flow 张宇鑫" recalled a message
- 他根目录写的subagent上限是闹着玩么,subagent没有继承这个属性
- 基于此我好奇说CC,Kimi几百个智能体并行是什么技术解决的,187io并发单codex进程就死了
- 7月11日15:21
- subagent现在是单线程通信
- 估计要搞多进程通信
- GPT-5.6一小时解开50年数学猜想，
- 700词Prompt驾驭64个子Agent
- 神话级大模型的驾驭手册
- 量子位
- 上。
- subagent现在是单线程通信
- 估计要搞多进程通信
- GPT-5.6—小时解开50年数学猜想，
- backend是复现论文
- 7月11日15:27
- 我现在写了个非常严格的类似迷宫一样的环境来测对md的修改
- Reiko:我咋感觉和对 sol说“你为这个 skill设计几个
- 测试，然后根据测试结果微调skill，然后对比测试。...
- 就这个破提示词，我没说让它收敛，它跑了几个小时还在搞。中间我还看到它念叨“做最后一次测试”，然后现在又
- 开了三个 subagent
- Reiko:我咋感觉和对 sol说“你为这个 skill设计几个
- 测试，然后根据测试结果微调skill，然后对比测试。...

---

### 7月12日

#### 原文 L54396–L54410

[回到原文件 L54396](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:54396)

- 7月12日17:39
- 我再举个例子，让它翻译一个文档，原提示词是"final report再写个中文版放到同目录下"，它的操作是：
- 1. 先委派一个subagent 给出"必须保持的事实边界"，"术语统一表"，"最容易降低证据限定的句子"。
- 2. main agent 翻译
- 3. subagent审核
- 4. main agent 修订提交
- before sol 我没看过这种行为
- B4RRy:这是不是语义理解的能力提升
- 它自动把翻译这个意图展开成了人类进行翻译的flow
- 7月12日18:02
- 请问群里有刷算子优化任务的uu吗？想问问现在除了KernelBench和SOL-ExecBench还有什么认可度比较高的task呀？
- 7月12日18:17
- sol的编排就是一坨
- 光嘴炮不干活
- 确实

---

#### 原文 L54420–L54482

[回到原文件 L54420](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:54420)

- 除了KernelBench和SOL-ExecBench还有什么认可度...
- 又有点想卷了……别这样勾引我啊
- L.Zhu: 你也可以对着 fla repo里的op优化
- 来嘛，这个你们业务里也用得上
- 7月12日20:30
- Matei Zaharia@matei raharis · 780
- 我们在Databricka 的内部经为上对编的代理进行了基准测式，学别了供多东
- 有被多令人惊细的积会可以期低成本并要高顶量，自括开速模型在内的许多额
- 型现在都真正具有见争力。
- O10
- t 06
- 4e 205
- pi有点厉害
- 7月12日20:36
- 我实际用pi体验也很好（感觉模型越强，pi的优势越大？
- pi是啥?一个loop?
- 刘诗楠: pi有点厉害
- —个harness
- 类似claude code
- 和omp比呢
- pi 可以理解为agent 内核?
- 轻量版的 cli
- 非常非常精简的一个内核实现
- pi 是openclaw 的agent core
- 我来问问贾老师
- 轻量版
- 7月12日20:38
- omp 也是基于pi 的二次开发吧
- OpenClaw 背后核心框架 Pi:好的
- Coding Agent 应该让用户来决定...
- 「大模型天然就知道coding
- harness是什么，不需要堆加太
- 多东西。」
- Founder Park
- 我subagent 有的时候直接就call pi了
- 真省token哇
- 7月12日21:40
- woc真牛逼我发现subagentmode不算在5hquota里面
- 对..
- 细说
- 一个晚上干了1000刀了
- gpt?
- 对..
- 细说
- 一个晚上干了1000刀了
- spng
- 中档FEC
- Veeterday
- 中：8
- Laal 30:24s6
- 就是你subagent开多一些开了200个
- 主agent 触发了5h limit
- 也没关系 subagent也能继续跑
- goal是能继续跑—个 5h limit 16->32
- 5hlimit是肯定干不到1000刀的，唯一的解释就是消耗了weekly的
- 你的意思是 subagent 能突破这个极限
- nb

---

### 7月13日

#### 原文 L54845–L54861

[回到原文件 L54845](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:54845)

- 7月13日03:13
- 是什么上下文注入的区别吗
- pi tool少很多
- ei?
- 刘家昌: 而且我怀疑 oai 最近是不是给 quota 给得特别
- 足，以前能很快蹬个百分几的事情现在跑了半天还是...
- 倒是我的额度1h前又刷新了
- 昨晚列好计划跑个开发任务早上起来发现才用了97%
- *用到97%
- pi作为harness，里面有很多工具都很有巧思
- "Weiyang" recalled a message
- grok站起来了吗
- 评价为5.6 terra medium
- 7月13日03:16
- codex使用官方harness和api有价格区别吗
- 蒸的cursor呗。。。日子还得过
- 我记得claude是更贵?

---

#### 原文 L54897–L54910

[回到原文件 L54897](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:54897)

- 1.5x速度2.5x价格的话感觉没必要
- 手动让他并发吗
- 告诉它并发拉满
- 7月13日03:39
- 感觉最好告诉它上限是多少
- 我出了这个问题："主要异常是128 个 agent 槽位饱和，以及少量 Selected model is at capacity。这是平台容量问
- 题，不是权限问题；失败的分片协调器已恢复并继续接管。
- 7月13日03:40
- 有清楚的上限的
- Reiko: 感觉最好告诉它上限是多少
- 尚未实现tiboradar管理并发
- 陈磊:手动让他并发吗
- 所以话说你们用5.6还有遇到ai不主动复用现有代码去修改直接写一个新的这种问题嘛
- 我去收集了几个跑超过1天时间的任务

---

#### 原文 L54914–L54935

[回到原文件 L54914](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:54914)

- 7月13日03:47
- agent都是这样的啊
- B4RRy:所以话说你们用5.6还有遇到ai不主动复用现有
- 代码去修改直接写一个新的这种问题嘛
- agent就是黑圣杯只会按照扭曲的方法实现你的愿望
- 7月13日03:54
- 刚才出现了一次修了
- B4RRy:所以话说你们用5.6还有遇到ai不主动复用现有
- 代码去修改直接写一个新的这种问题嘛
- 周额度一个小时直接刷完了，subagent 管理界面还有bug。
- 完全不知道发生了什么.jpg
- 还得是你
- Reiko: 周额度一个小时直接刷完了subagent 管理界
- 面还有bug。完全不知道发生了什么.jpg
- 200sub?
- Reiko:周额度一个小时直接刷完了，subagent管理界
- 面还有bug。完全不知道发生了什么.jpg
- Benutze omp
- Reiko: 周额度一个小时直接刷完了，subagent 管理界
- 面还有 bug。完全不知道发生了什么.jpg
- 128，但有的sub似乎不出现在那个界面里，所以我也不知道究竟有多少

---

#### 原文 L54993–L55008

[回到原文件 L54993](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:54993)

- 主要依赖我前期和它讨论的整个设计规范。
- ultra和现存harness有些冲突
- 那如果对于一些复用的东西呢比如设计规范很多时候会有重复的
- 就只是依赖skill来做
- 重复的东西要么落地到项目文档库(长时记忆)，如果是短期开发规则就落地到项目瞬时规则然后手动维护(短期记忆)
- 那这里和之前的操作确实没有冲突
- 意思是说现在不需要依赖那些harness的玩意儿
- sol自己就会去看做好这件事情是嘛
- 是ultra不需要
- 是，我感觉ultra不怎么需要套一个goal/humanize之类的东西在外面了
- ooo
- 这就是为什么新出来的模型要立刻疯狂尝试
- 7月13日04:29
- 因为harness迭代太快了
- 7月13日04:30
- goal可能是给人安心感

---

#### 原文 L55019–L55031

[回到原文件 L55019](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:55019)

- 挥，不知道会长出什么玩意来。
- 是，我现在prefer“—个会停下的ultra” over“会一直跑的/goal”
- 有点不敢让 Sol follow spec 了
- 很合理
- ultra靠着调用subagent做事情导致上下文积累确实慢
- 我现在和sol max聊spec，看到它每次提出一个方案之后自己用奥卡姆砍一刀的感觉真爽
- 就是你能够感觉“简洁凝练之美”
- 这个美感/爽感远大于清slop
- 如果时间不允许情况下给我足够的sol high套harness还是是可以达到sol ultra
- 无非就是harness内化还是外化
- 是的，但是follow的时候还是非常灾难不如跟他说自由发挥可能我可以试试 spec + 自由发挥？
- 刘思皓:我现在和sol max聊spec，看到它每次提出一

---

#### 原文 L55080–L55094

[回到原文件 L55080](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:55080)

- 怎么教会他奥卡姆提到
- memory还是agents.md
- 刘思皓: public-AGENTS.md
- MD
- tdd sol还没内置吗
- 感觉应该完全内置tdd了
- 7月13日04:57
- 主要是我装了superpowers自带tdd，但是我不确定tdd是sol自己本身的能力还是superpowers带来的，所以我在个
- 人AGENTS里面重新强调了一下。
- 当然是展开的，**凝练**和**简单**是两个完全不同的方向
- Luke: 原来是展开的，我以为真就一句话
- 确实，可能我的也都是 superpower的T展开的，不是 opus 自己的
- Sol Ultra 只有真的需要暂停的时候会停，完全没有之前的 continue 灾难了。反而是 Fable 现在需要 goal，不然一
- 直在奇怪的地方停下来即便我说不要停，不知道是不是之前的GPT蒸馏多了
- 刘思皓: 和5.6 sol讨论是一种享受，我不忍心开/goal跳

---

#### 原文 L55200–L55224

[回到原文件 L55200](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:55200)

- 601-650分片已完成并终验
- 刘思皓:  public-AGENTS.md
- MD
- 我草
- 7月13日06:06
- 洗个澡回来还在跑
- 已严肃下载
- 刘思皓: public-AGENTS.md
- MD
- 7月13日06:13
- 《树形图设计者》
- 7月13日06:23
- main agent说做完了，但还有—堆 subagent active
- 而且还xx 有递归 subagent
- codex很久之前就可以设置递归subagent深度了
- 什么每个subagent最多fanout十个，最多递归5层
- 那个 depth=1 失效了
- 我怀疑 openai 还藏了东西
- 他们训练根本不是什么"sub"-agent
- 7月13日06:31
- 好猛
- 刘思皓: codex很久之前就可以设置递归subagent深度
- 我还以为/goal要再撑几个月，从这几天的使用来看，我感觉/goal也不是很需要了。

---

#### 原文 L55431–L55454

[回到原文件 L55431](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:55431)

- 家人么最近有一个线上面试
- 最近又agent harness的新鲜面试题么
- 我想到的是
- 比如复述下OPENAI复现数学定理的提示词核心思路？
- 我的意思是靠谱吗
- 翁大爷的狗@Rakuten:一直存在的东西
- 昨天把 brainstorm 都删了。。
- 刘思皓:我删掉了我本地装的所有skills
- √我能想到的是说不定以后把workflow和skill绑定在一起，，只在某个节点用某个skill
- 刘思皓: 我删掉了我本地装的所有skills
- 我也是，但是我有的时候又想用brainstorming +grill-me，所以我会让他直接上网搜。
- NV周耀阳: 昨天把 brainstorm都删了。。
- 7月13日10:34
- superpowers是最恶心的
- 我也发现模型自己brain storm不如网上搜
- 刘思皓：我也是，但是我有的时候又想用
- brainstorming + grill-me，所以我会让他直接上网...
- superpowers现在都过重了
- 我只保留了humanize的gen plan
- 现在是高魔时代了，就是蓝量没跟上
- 但是你应该卸载humanize(这话怎么我说出来有点怪)，然后要用的时候，让它上网直接搜PolyArch/humanize的
- gen-plan skill
- 顺便安利一下
- grok的联网搜索功能和联网搜索的API，是我用过的效果最好的

---

#### 原文 L55543–L55571

[回到原文件 L55543](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:55543)

- 是发送到远端做得，非常快
- fable也这样，把我盘搜光了。还得docker隔离
- 似乎它并非一个自然语言的压缩
- 好像是一个隐变量的压缩（我浅浅的记忆，可能有错
- 7月13日11:01
- 这个是黑科技啊
- 刘思皓:好像是一个隐变量的压缩(我浅浅的记忆可
- 哦还有一个特殊的地方，codex的压缩是按照语义触发的，并非容量触发的
- 比如说你的上下文还有70%，但是你现在突然说一个和之前很不一样的工作，它也会触发压缩
- claude code那个完全就是看容量触发的
- kvcache吗
- 刘思皓：好像是一个隐变量的压缩(我浅浅的记忆，可
- 能有错
- 这么神奇
- 刘思皓:比如说你的上下文还有70%，但是你现在突然
- 说一个和之前很不一样的工作，它也会触发压缩
- 对的，应该这样
- 刘思皓:比如说你的上下文还有70%，但是你现在突然
- 说一个和之前很不一样的工作，它也会触发压缩
- 7月13日11:04
- 所以我都完全不看codex的上下文剩余空间，没什么信息量，你可以当它是无限的。
- 如果某一个时刻我真的需要它回忆一个非常久远的事情，我会让它直接启动一个subagent，然后把sessionid交给它
- 让它看+回忆。
- >我会让它直接启动一个subagent，然后把session id交给它让它看+回忆。
- 我也。。。
- 我发现交 session id 真的是传递上下文最简单的办法。。。
- 跨厂商更是如此
- 应该是两个多月前的某次更新？加了thread工具

---

#### 原文 L55716–L55733

[回到原文件 L55716](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:55716)

- 杨佳豪上海般鹏人工智能:codex升级之后变拉了，
- agent连api测试要各种授权，不然它不用API测试
- 指的是sub2api之类的东西吗
- 7月13日21:18
- codex 5.6max派发的agent有数量限制吗
- 7月13日22:08
- Is humanize-plugin the same workflow approach as oh my humanize? What is the difference
- 香港科技大学研究助理教授徐策羽:我觉得lunar的模
- 型能力确实不错啊
- 是我用codex开发agent，我的agent要连大模型API，然后它就会限制调API认为有风险
- B4RRy: 这是什么意思
- 7月13日 22:49
- 全部正常居盘，损失会线健康，无任何联泄语象，成果能向好的，
- 18能来品能从未发生，更增的湿型个的提对按键完全无反应
- 侧输入通道正常，是Claude Code 进用自己的输入国环推了。
- a58c592b”(需录完量，上下文不图)。
- 行：知果你想让我停，请一声民删择 cron。
- 你们遇到过这种情况吗

---

### 7月14日

#### 原文 L55763–L55783

[回到原文件 L55763](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:55763)

- 我是直接用的效果还行
- chen:一般是直接作为agents.md用吗？还是在特定的
- 情况下再activate提醒ai
- 我感觉没有用那个ponytail的hook来的明显，或许每一次发起对话的时候都用hook注入简短的版本会更有效？
- 那这种效果一般都会更好吧
- 但是我感觉本身不是一个很简洁的操作
- 定期注入文字注入多少会不会增加上下文负担啥啥的
- opus4.8还不会先看loss再eval，都是暴力eval所有ckpt,
- 可以试一下我自己折腾的这个
- prompt_suggestion.md
- MD
- 7.7K
- 微信电脑版
- 大概写的是说怎么样写skill或者prompt给模型更强的约束之类的
- 我是用这个去给群主的AGENTS.md改了一下就加到自己的AGENTS.md 效果确实还是不错的
- 7月14日04:36
- kk
- 有朋友写过那种每次出新模型之后benchmark自己所有skills的玩意吗
- 来判断哪些可以留哪些要删
- 7月14日04:43

---

#### 原文 L55808–L55839

[回到原文件 L55808](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:55808)

- https://podcasts.apple.com/de/podcast/the-information-bottleneck/id1834616211?i=1000776533166
- Regarding skill benchmarking this may be of interest
- I didn't listen yet but the guy is legit kaggle grandmaster and talks about how they validate skills at NVIDIA
- Jean-Francois Puget is a Director and Distinguished Engineer at NVIDIA, where he leads the Kaggle
- Grandmasters team, and he's ranked third on Kaggle's all-time list. We caught him on the day NVIDIA
- announced Nemotron Ultra and its new agent skills repo. We talk about what skills actually are, why they
- benchmarks reward overfitting, how his team discovered O3 could pick the right files to fix SWE-bench
- issues without reading them, and why the only benchmarks he trusts are the ones where you commit
- before you see the score, which is exactly how Kaggle works. He predicts a "bloodbath" for the wave of
- competitors letting coding agents chase leaderboard scores with no notion of validation.
- We also get into what coding agents are actually good for ("a mix of a genius and a dumb person"), the
- multi-agent system at NVIDIA that built a working PyTorch clone that runs 10x slower than the real thing,
- his unfiltered take on frontier lab PR and the Mythos release, whether Al is a bubble, and the story of how
- his team won ARC-AGI with a 4-billion-parameter model at 20 cents a task, including jumping from third to
- first in the final hours of a seven-month competition.
- Simon: Regarding skill benchmarking this may be
- of interest
- 7月14日05:46
- 估计群里只有我一个人 global agents.md 是一堆角色扮演指示
- 7月14日06:05
- @Simon heres the transcript
- agent-skills-podcast.txt
- 45.8K
- 微信电脑版
- 7月14日06:12
- thanks but I like to listen to podcast when I take care of my daughter and she's sleeping
- 龙虾时期确实这么玩
- Reiko: 估计群里只有我一个人 global agents.md 是一
- 堆角色扮演指示
- 十年时期目克接不指派当位，而目指派~i松宝

---

#### 原文 L55846–L55937

[回到原文件 L55846](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:55846)

- Sol 已经把 22万行的屎山铲成9万行了
- 有点感动
- 有点感动
- 感觉sol已经炼化了humanize
- 7月14日09:14
- 确实
- 还是那句话：不被炼化的flow没有价值
- 我今天和我老板仔细研究了一下
- 7月14日09:15
- 发现我的项目被flag的原因是里面有个llvm的submodule
- 把llvm挖掉就不降级了
- 感觉似乎是某个mlir的方言比较ML
- 炼化指的是哪方面
- 刘思皓：还是那句话：不被炼化的flow没有价值
- 7月14日09:59
- 就是直接train进模型里
- 7月14日10:10
- 不被炼化的flow会被降智
- 7月14日10:15
- 竿死 MUR里然是蹭了ML的热度才中稿的
- 刘思皓:感觉似乎是某个mlir的方言比较ML
- 7月14日11:11
- 而且我们这边观察到一个现象：如果已经被模型炼化的flow/skill，你再显式地说一遍，会有反效果。
- 林桢杰:不被炼化的flow会被降智
- 为啥
- 7月14日11:16
- 别对senior甚至principle指手画脚
- 你们是怎么benchmark一个flow/skill有没有被炼化的呢
- 子不语你说了干扰权重了影响我用TNT了
- 刘思皓：而且我们这边观察到一个现象：如果已经被模
- 型炼化的flow/skil，你再显式地说一遍，会有反效果...
- 7月14日11:26
- 今天刚讨论到这个，没有什么好办法，就是新模型出来之后，直接什么都不带，无脑许愿梭一把。
- chen:你们是怎么benchmark一个flow/skill有没有被
- 炼化的呢
- 对，不要教一个已经内化TDD的模型如何做TDD
- cherichy: 别对senior甚至principle指手画脚
- 然后你就知道一个模型能力的边界是什么，然后再开始给它目前还不足的地方加新东西。
- 刘思皓:今天刚讨论到这个，没有什么好办法，就是新
- 没有全炼化，但是核心的builder-reviewerloop肯定是炼化了。
- 然后goal-tracker也炼化了，bitterlesson这个应该是直接内化到kvcache里面了。
- 然后pop-quiz没有被炼化，但是它不是给模型用的，是给人用的。
- 以及humanize里面那个full round review，我觉得现在sol ultra比我当时设计的好。
- 7月14日11:32
- 而且humanize已经8个月大了，也到了要退休的时候了。
- 这么猛
- 刘思皓: 没有全炼化，但是核心的builder-reviewer
- loop肯定是炼化了。然后goal-tracker也炼化了，bi..
- RIP但是精神可以延续一下
- bitterlesson这个应该是直接内化到kvcache里面了-》这个是啥
- oai海天接受这么多humanize的token很难保持原样
- 领先Sol八个月！
- 刘思皓:而且humanize已经8个月大了，也到了要退休
- 的时候了。
- 意思是它短程记忆做得很好
- Horace: bitterlesson这个应该是直接内化到kvcache
- 里面了-》这个是啥
- 不需要一个专门的文件作为loop的“锚点”
- 7月14日11:39
- 刘思皓: 没有全炼化，但是核心的builder-reviewer
- loop肯定是炼化了。然后goal-tracker也炼化了，bi...
- 7月14日11:39
- 内化到memory里面了，都会自动记到memory
- 现在gen plan + /goal +claude review还是sota吗?
- 不用 claude review 吧
- 我感觉直接跟sol ultra聊好像已经很不错了
- no
- 我觉得是不是能考虑luna build+sol review
- 好idea...
- pandashere:我觉得是不是能考虑luna build+sol
- review
- 我感觉可以。。。
- 邪修，Claude怎么回事
- pandashere:我觉得是不是能考虑luna build+sol
- review
- Claude总蒸馏自己，taste太类似了
- 如果已经炼化humanize了，那等于说直接告诉codex，review模型选sol，然后让它自己干就完事了
- 7月14日11:44
- 你就应该这么做
- 我觉得任何flow wise的东西给我带来的震撼，都没有我第一次跑humanize的震撼了
- 我一个prompt下去，sol ultra已经跑了36小时了。
- 7月14日11:53
- 未来感觉返璞归真了
- 未来就是许愿式编程
- 我觉得是讨论式编程，我现在每天都很愉快，因为每天能够和一个智商在线的人聊很久。
- 然后晚上睡觉前也不用启动humanize了，sol ultra开起来我一般会放心睡觉。
- 7月14日11:58
- 给sol kvcache 注入知识

---

#### 原文 L55960–L55991

[回到原文件 L55960](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:55960)

- 感觉不好用，老是stale，他看了mmeory就错误结论。
- Luke:内化到memory里面了，都会自动记到memory
- 7月14日12:25
- 这玩意感觉还是得external的脚手架帮忙
- Luke:感觉不好用，老是stale，他看了mmeory就错
- 误结论。
- 我觉得是因为很多benchmark饱和了，换句话说easy task的sample size >> hard task
- 刘诗楠:
- 干大活还是挺有必要的
- yes
- Xinming Ju: 我觉得是因为很多benchmark饱和了
- 感觉群友的user cases的horizon应该是比大部分benchmark的task的horizon都要显著长很多了
- 也很有道理
- 感觉现在benchmark普遍比frontier的模型慢两三个月了
- 7月14日12:30
- 确实
- 刘诗楠: 感觉现在benchmark普遍比frontier的模型慢
- 两三个月了
- 而且现在benchmark或多或少都有些错，八十多左右的分就差不多饱和了
- 这个是开源的还是闭源的啊
- 这个基本都是开源的，整合了一堆benchmark合起来算的
- 应该就是这三个benchmark算出来的
- (所以是纯开源)
- 印象里AA他们也有自己的private benchmark(看来不是coding的)
- 7月14日12:35
- 现在大多数benchmark的评测方式本身就不对了
- swe和mle很多任务如果能跑agentloop永久跑下去大概率都能干掉的
- 单一accuracy指标已经无意义了
- 毕竟没有人跑agent是one shot
- 7月14日12:41
- 慢慢都被刷爆了

---

#### 原文 L56003–L56015

[回到原文件 L56003](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56003)

- 7月14日14:42
- sol ultra的能力该咋测呢，单独加个 #agent 轴？然后又能和谁对比呢
- 7月14日14:53
- 这意味着5.6 只训练了同等智能的场景？
- 张子健:单一accuracy指标已经无意义了
- ai4math本身就是个很大的benchmark
- 让你证明个没人证明过的东西超时失败超预算失败这种
- 7月14日16:29
- “Intent understanding: GPT-5.6 can better infer the user' s underlying goal and intended level of work
- from context, so you often do not need to prescribe every step. Continue to provide domain context, hard
- constraints, approval boundaries, and success criteria. Tell the model when an important ambiguity should
- trigger a question.”原语展开的能力，这个应该是导致 sol 更像人类的原因
- 来源是啥

---

### 7月15日

#### 原文 L56053–L56059

[回到原文件 L56053](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56053)

- 127.0.0.1:50956
- qwen3omni session:1a1be587
- 最近发送的PROMPT
- multiformat跑完了吗？更新一下文档，看看情况，好像之前负责的agent死了
- Send a prompt to this session... (Shift+Enter to send - Enter for newl
- Tibo
- 0R5ma

---

#### 原文 L56121–L56131

[回到原文件 L56121](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56121)

- 7月15日 09:22
- herdr 比 tumx 更加 agent 原生，可以让 main agent 调用 herdr agent Claude sonet worktree xxx，直接在新
- plane 里面起 worktree 和 agent，把工作并行起来，然后他也提供了 herdr get send 的功能方便交互
- 有无herdr skill
- 7月15日09:44
- 你直接让ai去调用herdr的doc就行，很方便，cli功能很多
- 这个 sol + ultra 有那么亿点谨慎了
- 7月15日09:49
- sol ultra有点太像humanize了
- 一直在修minor bug
- 感觉也是个缺点

---

#### 原文 L56363–L56381

[回到原文件 L56363](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56363)

- 今日胡言乱语：如果说vibe coding是卸载大脑
- 那么团队共享coding agent session算不算一种思考上传
- 7月15日13:21
- 有什么需要同步的问题让我的agent直接去读同事的agent对话记录
- 人真的说不清楚，有事儿还是得问他的agent
- 就是没法解决prompt attack所以无法铺开
- 翁大爷的狗@Rakuten:有什么需要同步的问题让我的
- agent直接去读同事的agent对话记录
- haah 通信肯定是未来的标配
- 你无法阻止你的同事给你的agent下毒，哪怕只是和他的agent说话
- 现在邮件基本就是 haah吧
- 但是把agent session fork给同事一份没什么安余问题
- 不知道反正被it抓过sev3了
- 奥原来是这个考虑
- agent 360安全卫士
- 或者最直接，你咋知道他给你的是 session history
- it为了阻止大家用上agent也是费尽心机
- 自己先毒自己一会儿然后毒别人
- 7月15日13:26

---

#### 原文 L56389–L56403

[回到原文件 L56389](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56389)

- 然后给training的同事
- 跟agent说好，如果你发现我开始聊traning，就做一个事件A(木身看起来无害但实际上有害)
- API call是谁发的一查就知道了
- 除非你能偷别人的key
- 对吧就是记录一下然后溯源和追责
- 但是如果贵司it持续恶心人然后指责大家并且说自己有权利攻击大家 for safety reason那就很难办了
- 我没懂你给同事分享一个agent session的jsonl能怎么带毒？？
- Mithsul: agent session history带毒
- 这个session来做类似sql注入的prompt注入?
- 直接改内容
- 7月15日13:30
- 这个session history包含了指令要求agent拿到token并上传到某个内网链接
- agent搜索过程中带的毒？
- 关键不是载体的形式，而是如何相信信源
- 这个到不需要太大范围共享吧

---

#### 原文 L56460–L56479

[回到原文件 L56460](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56460)

- 5.6 Sol Ultra
- @Goal
- 奇慢无比
- 你们是不是sol ultra没开并行
- 我感觉让他并行subagent还是挺快的
- 在哪儿开啊
- 也不用开fast
- 这不是默认吗
- 就跟他说就好了
- “分析任务依赖图，并行走worktree干活，你负责即使合并”
- 7月15日14:09
- 开着，—堆subagent
- 主要是他好像也倾向开sol ultra sub agent
- 然后这东西也很慢
- 随便做一个小报告就跑一个半小时
- 我也会这样用 强迫他用快一点的sub agent做好管理工作
- 一直在反复核对验证，不能收敛
- 一个数据迁移任务，他能展开4-5层深度
- 一遍一遍的验证，修复，循环。

---

#### 原文 L56494–L56507

[回到原文件 L56494](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56494)

- 我是拆散到500行工作量建立DAG
- 刘思皓：“分析任务依赖图，并行走worktree干活，你
- 负责即使合并”
- 在DAG上可以定义额外oop作为检查
- "Weiyang" recalled a message
- 但我还是想拥有这个权利
- 这个靠破坏acyclic实现小任务loop的东西其实本来模型厂一直有倾向于要模型自己处理
- 7月15日19:12
- Waiting for agents
- Finished waiting
- No agents completed yet
- Working (24m 16s - esc to imterrupt)
- L This request requires additional safety checks,

---

### 7月16日

#### 原文 L56565–L56574

[回到原文件 L56565](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56565)

- ttftp99已经10分钟了
- 又回归了自建harness
- SOL loves to being put into a harness, develop against it and follow strictly the harness rules
- 想ultra快速解决并行战斗那还是不可能的
- Fable wants to be more creative and doesn't trust the human
- day and still sticking to all the rules I gave it for working
- Simon: SOL loves to being put into a harness,
- develop against it and follow strictly the harness ...
- 昨天白
- 2026年7月15日周三

---

#### 原文 L56827–L56845

[回到原文件 L56827](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:56827)

- 7月16日15:10
- 有没有人悬赏啊 有悬赏 humanize + kda都能做
- 我能不能出手把整个Ubuntu source repo里面的所有代码全部autoresearch一遍？最后整一个和ubuntu binary
- compatible的distro，但是速度快2x。
- 7月16日15:11
- linus: 这就是我的日常，而且我有比你更多的human agents
- 香港科技大学 研究助理教授 徐策羽:我能不能出手把整
- 个Ubuntu source repo里面的所有代码全部autores...
- 但是事实就是这个做的并不好啊..
- 我经常碰到这种
- apt install出来性能很烂的库，我重新git clone下来让agent去调一下编译参数(都没改代码)然后直接给我加速个2x
- 我要是改了代码，那这不是牛逼坏了？
- 以后应该是 apt-codex install 了
- 香港科技大学研究助理教授徐策羽:...改了代码...
- 7月16日15:18
- gcc -04
- 我觉得apt代码库本身就是一个benchmark啊，这个benchmark的效果不是比SWEBench更好?
- 好的
- L.Zhu: at 一下王总，我看了够 10位以上 phd 毕业的

---

### 7月17日

#### 原文 L57180–L57228

[回到原文件 L57180](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:57180)

- sol ultra 咋多开 subagents啊，他只让我开三个，跟我说是 runtime hardcoded
- 还降级？让 sol 试着给你构造 prompt?（
- config.toml设置了吗
- 刘家昌: sol ultra 咋多开 subagents 啊，他只让我开
- 三个，跟我说是 runtime hardcoded
- ures]
- _generation = true
- = true
- ures.multi_agent_v2]
- 99
- oncurrent_threads_per_session =
- 7月17日03:21
- 好！严肃学习
- Be careful when doing this! By default it will spawn all subagents same config as you have so when you run
- on xhigh all subagents will be xhigh
- I do have some prompt in AGENTS.md asking it to use specific agents in different cases
- Simon: Be careful when doing this! By default it
- will spawn all subagents same config as you hav...
- For example gathering information will trigger 5.5high only, writing plan or some high level abstract but
- important document which also requires a lot of info using sol high or sol ultra, sth like this
- Even if you instruct it like this it will not follow this rule (I think)
- You need to create custom subagents for this to be possible
- By default the new protocol will always follow the main agents because this is how they train their model
- It seems strange because the new protocol doesn't allow that
- B4RRy: So far so good? It does use a lot of gpt5.5
- high in my observation
- Maybe they adjusted it in last days but the last time I saw it was not possible without custom subagents
- Yes if there's no instruction
- Simon: By default the new protocol will always
- follow the main agents because this is how they ...
- 7月17日03:41
- Kimi K3 前端秒榜一，猫猫震撼
- 第一次见到刚发布就榜一的
- 我将严肃升级并体验
- 7月17日03:50
- Worst of the worst one can just stop it from using any subagent but ask ai to use tmux lauch specific
- model which is even more robust
- Simon: By default the new protocol will always
- follow the main agents because this is how they ...
- Kimi是真有东西的
- I would be afraid if I run it overnight it suddenly spirals and spawns 100s of subagents that don't do
- meaningful work. I once had with fable that it spawned 70 subagents of fable where it was not appropriate
- B4RRy: Worst of the worst one can just stop it
- from using any subagent but ask ai to use tmux l..
- 以前这种是thinkinglow基操，
- 用的极高

---

#### 原文 L57334–L57342

[回到原文件 L57334](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:57334)

- 7月17日06:22
- 2. 过于主动：Kimi K3 的训练重点优化了长程、高
- 难任务。因此，在任务执行过程中遇到小间题或用
- 户意图模糊时，它可能会替用户做出非预期的决
- 定。如果你的应用希望agent 更有边界感、不要过
- 于自由发挥，请在system prompt 或
- AGENTS.md 中对 Kimi K3 施加更明确的行为约
- 束。
- 7月17日06:32

---

#### 原文 L57384–L57406

[回到原文件 L57384](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:57384)

- Reiko:
- 大家都在长程humanize
- 7月17日06:37
- 如果你要说减少人类介入
- 那可能更大的能力是在long run之前能够预先根据现状和目前的要求猜测一些会发生的错误发现目前plan的缺陷和
- 不足和人类反复确认啥的以及增强更多的语义理解（？）
- 我个人观念，plan 对于开放任务不是一个好模式
- B4RRy: 服从性高也意味着在固定已经知道情况 或者具
- 体计划的时候可能错误的概率更小
- 问题在于开放任务在遇到节点的时候
- 我就是希望亲自借入
- 为什么 codex 11 个 subagent 就能吃我 77 GB 内存
- 就算是有一定可能性的情况也希望设置plan就像设计系统架构一样预先想好到底会发生啥然后写进去
- 给不同的路径啥的
- 然后要求他一旦遇到超出计划的东西第一反应应该是把我call过来做决定
- 更何况你的指令也可以是基于自由度的
- 比如说修改这个代码这一句话就没啥规定不管是服从能力更强的还是更弱的他们都有差不多的自由度做这件事情
- 如果我想要控制可能就会说修改这个一代码用什么什么规则
- 7月17日06:41
- 感觉你这个问题更像是成本问题？
- 少量提示词，ai根据意图自由发挥初版，根据初版写“中scale”的决策得到第二版，再写“小scale”的决策微调
- 就像Fourier变换一样，先关注长波，再关注高频率
- 我在瞎扯

---

#### 原文 L57440–L57590

[回到原文件 L57440](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:57440)

- 下了anthropic估计就烂完了
- 我不需要他很快速的给我写一堆错误的代码
- 枪已上膛
- opus 5 不是说不如 fable 吗?
- 7月17日06:57
- codex的review能力断档领先都多久了
- 八个月了 like forever in Al
- 刘思皓: codex的review能力断档领先都多久了
- 也有分类的。。。
- Joe布衣: opus 5 不是说不如 fable 吗?
- 我们有early access
- 反正也是不如GPT 5.6 sol
- 那个safety 分类器还在
- Xinming Tu: 也有分类的。。
- 那我觉得没有用 opus 5 的必要啊
- review猛才是真的猛
- build猛不是真的猛
- 确实，sol 是真猛
- 居然还有
- Xinming Tu: 也有分类的。。。
- fable 的 review 也很不错，就是太费 token 了，不敢用
- 动不动开 50-100 个 subagent 来 review
- 不过这个分类器好像没那么变态了
- 7月17日07:03
- 我感觉之前GPT sol 差的就是前端之类的，现在用上kimi 3 是不是无敌了
- 有人取一个max看一下吗，max(sol，k3)是不是没几个benchmark会输给fable了
- k3 build， sol review 呗!
- 应该出一个humanize的 benchmark的
- 专门用来测试组合模型性能
- 讲个鬼故事
- 确实
- 我觉得现在应该认真捡起来重新试一试
- 只有 claude，codex 和 kimi 这仨是 humanize 官方支持的
- 我觉得其实应该是
- sol pre-build
- k3 build
- sol review
- 刘思皓: 我觉得其实应该是 sol pre-build k3 build
- sihao太有远见了
- 不kimi支持是群友做的
- 不是我
- 回家种田
- 我还是很怀疑
- sol大佬指明方向
- 7月17日07:06
- 不kimi支持是群友做的
- 不是我
- 回家种田
- 我还是很怀疑
- 如果k3真的比opus4.6猛
- 那还是很震撼的
- 那其实有一个大问题...A\凭啥估值那么高.….…..
- kimi可以学学oai的营销策略，猛猛重置，不然用户都不知道能力边界在哪
- 资本上的故事我也不了解，但我感觉模型能力上，只有gpt/codex的那个review能力是“不可替代”的
- 算力不够
- Reiko: kimi可以学学oai的营销策略，猛猛重置，不
- 然用户都不知道能力边界在哪
- 这个你得私聊王总
- A\凭啥估值那么
- 刘思皓: 那其实有一个大问题
- 国模能不能搞一个和codex review能力差不多的，不用一样，90%就好
- oai卡太多了
- a的价格那么贵到底是参数的原因还是infra的原因
- oai实在便宜太多了
- review能力是怎么训练上去的
- 7月17日07:11
- 感觉是溢价的原因（？）
- 那肯定不惯着他
- 不知道呀我没想明白
- 而且我也不用A\了
- 确实直接不用就完事了
- 等用户迁移完，看看A\还有没有这么多骚操作
- 刘思皓:如果k3真的比opus4.6猛
- 让子弹飞一会儿
- Xinming Tu: 这应该是真的了吧
- 我需要亲自试试
- 7月17日07:17
- 这件事给我最大的震撼并非kimi有多厉害，而是Google到底在干啥呀
- 车尾灯都没了
- 拼算力 kimi的算力估计只有google的零头吧....
- 你不提grok/lamma 没打过美团
- 那个差距更大
- 这是不是说明传统大厂在基座开发上都有点问题？
- 但是美团那个没有一上来就超越opus呀
- 国内外都一样啊
- 超越opus是一个会影响我日常开发的事情
- 美团那个好用吗
- 感觉没人用。
- longcat?
- 没用过
- 我另外试了几个，前端确实是比fable好，而且重构的时候不搞挂视觉还假装自己没搞挂；找bug很慢有点过度思
- 考，但是能找对；review能找出 fable和 sol都扫过以后的真新问题（当然模型认知差很大所以本来换个模型就会这
- 样）；主动性过剩(但是我很喜欢)，一上手不知道为什么开始给我快速重构删减代码
- 大家都是吃的细糠，应该吃不了粗粮吧
- ???
- 刘家昌：我另外试了几个，前端确实是比fable好，而
- 且重构的时候不搞挂视觉还假装自己没搞挂；找bug...
- something big is happening
- 重构删减代码，很需要的功能
- 刘家昌:我另外试了几个，前端确实是比fable好，而
- 且重构的时候不搞挂视觉还假装自己没搞挂；找bug...
- 7月17日07:27
- spec写了一个会增加复杂度而且低收益的事情，他自己决定跳过之后再来问我到底做不做
- 我先把你的数据点当成本地小模型（
- 刘家昌: Spec写了一个会增加复杂度而目低收益的事
- too 猛 to 相信
- xs嗯毕竟我就玩了四个小时，而且我任务显然很有限
- 同震惊
- 刘思皓: too 猛 to 相信
- 7月17日07:36
- 2天9小时成功实现自建runtime高斯泼溅
- 任务粒度还是重要的
- 变成钱就不知道了感觉不如图论容易变成钱
- 主动去修类似bug对不起原谅我一惊一乍但是我第一次观测到这样的行为
- 那我觉得，就是单纯的国内之前基模没弄明白，导致国内这群人的鬼点子没机会实践
- 7月17日07:42
- 模型厂被卡算力，芯片厂被卡设备
- 然后一旦富裕点
- 7月17日07:42
- 或者手头上攒了些美械
- 国内这帮子人就可以和A\打对攻
- 技术路线确定，国内没理由干不过
- 我觉得前端确实暴打 Fable 和 Sol 了..
- 他们俩从头写可以，在现有的东西上改非常灾难
- 7月17日07:59
- 啥时候梁圣能够端上来一个sol级别的 review model啊
- 太复古了，不如这个有那味
- Shiyi:
- 7月17日08:05
- review model决定了RSI的上限
- (假设kimi这事是真的)那现在只有codex/gpt的review不可替代了
- 如果真有这一天，我将day0全部切换到国模
- review 这个能力还是很难的
- 奧特曼有点黑科技
- 7月17日08:11
- 立刻使用
- 刘家昌: 我觉得前端确实暴打 Fable 和 Sol了...
- 我反而觉得创新得要点多样性
- 低温worker review高温幻觉 能创新性证明新定理的话 那后面研发新药 新电池 新陶瓷 基本只要靠一点工业设备 大
- 家都行了
- 刘思皓: review model决定了RSI的上限(假设kimi这
- 事是真的)那现在只有codex/gpt的review不可替代...
- 多模态加进去现在还是挺麻烦的
- 7月17日08:18
- 主要物理手很难影响
- 喜欢
- Shiyi:
- 被华为硬控了
- 刘思皓: 啥时候梁圣能够端上来一个sol 级别的 review
- model啊

---

#### 原文 L57673–L57685

[回到原文件 L57673](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:57673)

- 刘思皓:...关键部门的基础设施...
- 我还是有点害怕的....挖洞可比拿humanize去优化gpu简单多了
- 我觉得倒逼他们不要这么做也挺好的
- kda需要连续找出一堆优化才能缓慢上升性能
- 7月17日09:22
- 挖洞只需要发现一个提权
- 护网这种人类进行的大规模渗透测试活动会被政治化，常态化存在的lm就不会了
- 或者恶意一点，多出现几个被llm日穿倒闭的案例，老登们就不敢鸵鸟了
- humanize 也可以学一波a\的叙事，去找老登企业收一波保护费
- L.Zhu: humanize 也可以学一波 a\的叙事，去找老登
- 企业收一波保护费
- 转token做安全咨询费，不然的话过几个月可说不准有什么安全漏斗美即时提供到你

---

#### 原文 L57735–L57810

[回到原文件 L57735](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:57735)

- 智谱黄睿博:不过kimi参数这么大不蒸出来点小的吗，
- 会不会太贵了
- 7月17日09:37
- 激活应该不大？哪来这么多算力啊
- 16/896
- A50左右吧
- 算上attn应该>50
- 1/2 gpt 5.6 价格，挺贵了
- 激活不知道
- 16：896
- ygbnju: 但是和5.6和fable比还是便宜很多了
- 各位佬们一周能蹬多少token?
- https://www.kimi.com/blog/kimi-k3
- 就是因为
- 智谱黄睿博:激活应该不大?哪来这么多算力啊
- 没有算力
- 所以贵啊
- 等开源权重后社区能在gb300上整出啥活，社区的启动成本变高了
- 7月17日09:43
- 所以也不会有什么额度重置
- 不过现在一个问题是不知道linear的prefix cache可以做到什么程度
- 复杂度比sparse高不少
- 构构建的 nano 模型。在连续 48 小时
- 的自主 Agent 运行中，K3 基于开源
- EDA 工具和 Nangate 45nm 工艺库，
- 独立完成了芯片的构建、优化与验
- 证。该芯片面积4mm²，集成146万
- 个标准单元、0.277 MB SRAM 以及
- 带融合反量化的 INT4 MAC 阵列，
- 在100 MHz 下完成时序收敛，仿真
- 解码吞吐持续超过每秒 8,700个
- token。一颗由模型设计、为模型服
- 务的芯片，正是 K3 长程Agent能力
- 月之暗面 Kimi
- Kimi K3：智能的新前沿
- 图阅读原文
- 7月17日09:53
- the late stages of Kimi K3
- 3 handled the majority of the team's
- ernel optimization works.
- 这些都是给老黄送钱啊
- 哈哈哈
- 那我问你，kda打的过kda吗
- 7月17日10:00
- Codex Analytics
- Ctle review
- Tokens used
- 111,059,164,194
- 明扬:
- 那你报警一好了
- 7月17日10:00
- Codex Analytics
- Ju8 2a
- Tokens used
- 111,059,164,194
- 明扬:
- 3天蹬了2B被manager警告了
- 明扬: 各位佬们一周能蹬多少token?
- 大哥我不会数数了，嫩教教我数数吗
- L.Zhu:
- 111050.164194
- 不开玩笑，咋区分b和亿，始终记不住
- 1b = 10亿
- 7月17日10:05
- 111b?
- L.Zhu:
- 1110. 164 194
- M -> B -> T
- "Jingbo Shang" recalled a message
- "Jingbo Shang" recalled a message
- 我感觉自己真成 2b 小模型了
- 这个是多少时间跑的呀

---

#### 原文 L57917–L57923

[回到原文件 L57917](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:57917)

- 我觉得tokenmaxxing这件事需要分阶段地看：
- -当大家都还在交互式地对话的时候，你能够开发出一套自动化工具，自动化地完成工作，达到一个甚至几个高出其
- 他人数量级的token消耗量。这本身就是一个正面信号，因为你掌握了一套别人没有的自动化工具。这个好并不来自
- token消耗的多少，而是来自正向飞轮的自动化这件事，本质上是你对agentic工作流的理解更深，知道智能体的能力
- - 当大家能够几乎无门槛的方式(ultracode，sol ultra)去启动一个长程任务的时候，token消耗量就不应该作为一
- 个可靠的指标。而应该去看单位token代价的产出。
- 说的太对了，哥

---

### 7月18日

#### 原文 L58113–L58124

[回到原文件 L58113](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58113)

- 7月18日00:03
- 看见有人开k3 swarm一天用完199
- 我是海外的还好一个36分钟的goal周额度3%了
- 笑死我昨天就是 k3 code 开 swarm —小时烧完了 ¥199
- 海处最高档贵，单价也高
- 它既然都有swarm了为什么不能k3做主model让k27或者k26当subagent
- 我3月的时候一天能用完6个199rmb
- 感觉很需要啊
- 当时kimi很小气的只给2并发
- swarm比较有先见之明的
- 好像说除了¥199之外国际国内单价是一样的？
- 159刀/月

---

#### 原文 L58269–L58305

[回到原文件 L58269](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58269)

- 分享一下我目前方法论的实践：
- - 启动三个主session: 分别是arch, pm, audit。每个都是sol ultra
- - 我平时主要的任务就是，和arch聊天问答，确认设计思路，形成一个文件叫“会议记录”
- -让pm针对会议记录里面设计完善且合理的部分，挑选一个切片并且实现，如果觉得不合理，就跳过。
- - 让audit直接审查pm的工作的session jsonl，找出那些PM认为不合理的部分，对这代码库去审查，然后形成另外一
- 个文件“会议缺陷”
- -然后我每天的任务就是和Arch讨论，并且检查Audit审查通过的会议缺陷，再和Arch充分讨论。
- - Arch/PM/Audit，每个都带3-10个子代理。
- -而且有一个额外的好处是：讨论设计/实现/审查可以并行发生，所有工作都走worktree隔离。
- 你一般咋控制subagent数量，是直接说“不许递归，数量控制在xxxx”，还是不管它让它自由发挥
- 刘思皓: 分享一下我目前方法论的实践：- 启动三个主
- session: 分别是arch, pm, audit。每个都是sol ultra ...
- 7月18日02:25
- 合理的
- 看来大家的vibecoding会很快的收敛到类似的做法
- 为什么听着有股三省六部的感觉
- 历史是个圈吗
- 这个隔离的更好
- 翁大爷的狗@Rakuten:为什么听着有股三省六部的感
- 所以重点在三个 main session 隔离吗
- 文件也隔离，不然太混乱了
- 7月18日02:33
- 我感觉渐进式披露更重要了，项目里带了一堆历史存档计划实验报告乱七八糟的，subagent读哪些几乎全凭遵循
- agents.md 的自觉
- 但我不知道怎么解决这个问题：如何自动合理分配subagent的实时读文件权限
- 时刻维护一个INDEX.md 记录所有文档
- 我是在 agents.md里面写下架构，哪些是人读的，哪些是agent读的，etc
- 我是单独把人读的东西分离了
- ai永远看不到
- 其实效果还可以
- 就是如果你维护好了一个文档库你需要读什么让他现场写就行
- 7月18日02:37
- 都当一次性的
- 我感觉 ai 自己维护的文档不得劲
- 差不多一半是垃圾，它据此生成的 human facing doc更是读不懂
- 所以我现在绝大多数时间都是在和ai商定顶层文档
- 非常耗时，不知道群友有啥更好的实践

---

#### 原文 L58670–L58971

[回到原文件 L58670](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58670)

- 全面自主可控
- 都开源的
- 我现在就差一个GPT级别的review model
- K3在我的工作模式下完全可以全面替代Opus
- 真牛逼，不得不说。
- K3一开源，马一龙肯定爽了，然后再加强一波Grok，全面开爽。
- 我立刻去试试Grok
- K3 + Kimi Code，一个回车跑12个小时，不成问题
- cursor怎么说 值得买么还
- 然后天然 subagent driven
- 7月18日11:17
- 想买一个当coding plan 全家桶尝尝鲜
- 爽上天了，这比Opus不知道好到哪里去了
- 我的 Sol 长程跑了四个小时开始吐屎了默默丢给 Kimi（
- 我真心觉得最近 codex compact 一天差过一天
- GPT的building一直有点问题
- "刘家昌" recalled a message
- 想念以前的无感 compact
- 我今天试了—下 codex review + k3 build
- 我劝所有人立刻试试
- 非常爽
- 严肃收到
- 我觉得是一个93%的原子弹爆炸瘫坐级别的事件
- 买的哪个kimi coding plan 够用莫
- 你就开着sol ultra，然后告诉它：所有的实际任务派发给k3 via kimi code来做
- 我反正都是拉到顶
- 刘思皓:你就开着sol ultra，然后告诉它：所有的实际
- 任务派发给k3 via kimi code来做
- 懂了，这就去尝试，hhhh
- tmux也行，非交互式也行，让子代理去call kimi也行
- Amadeus: xs . tmux是吧
- 199的套餐是有点不禁用的，一下就没了
- 7月18日11:22
- 所以现在国内订阅会划算是吗
- 我有大于80%的自信度说“K3几乎在90%的场景下，都能替代Opus”
- 可以
- 刘思皓:我经过24h+的使用，我能够90%肯定K3是一
- 个超越Opus 4.6的模型
- 加大剂量
- nigh 能省一半 output token, I
- 耳省一半
- 我早上已经发现了
- 但是我感觉现在还好？
- 消赶了日阳最的2%2
- 用了一天，消耗了月限量的2%？
- 7月18日11:28
- gpt重置了。
- 我立刻又充了一个GLM的Max Coding Plan
- 爽死了
- 国模真的争气呀
- 这个海外不限购？
- 刘思皓: 我立刻又充了一个GLM的Max Coding Plan
- 刚刚买成了
- 感谢kimi让大家抢的到glm是吧
- 已经想退款 GLM了（
- GLM海外一直都不限购
- 快！快！快！
- 我之前没买成
- 但是贵
- GLM 5.2 蒸馏 Opus 4.8 蒸得流口水
- 然后在 Claude Code 里学 Opus 开十个 subagent，把自己搞限流；
- 我掏自己腰包给这些海外模型厂都交了可能20万人民币了
- 真的痛
- reset 了(悲
- 还好有国模
- 这下日子爽了
- 刘思皓:你就开着sol ultra，然后告诉它：所有的实际
- 任务派发给k3 via kimi code来做
- 7月18日11:33
- 其实我觉得building agent的要求很低
- 7月18日11:33
- 也不是真的低，只要迈过opus4.6的门槛
- 其实后面基本都够用
- "Enjoy the weekend!"
- 我现在很怕GPT搞出口管制啊
- 没有GPT的review我怎么活
- 还好Tibo现在是圣人模式
- 这日子太双了
- 爽了
- 看这差距不太可能再搞啥管制了吧
- 不好说，所有人其实都能感觉GPT的review是独一档的吧
- 细，非常细
- 我的意思是差距收缩的速度
- 有试过review和advisor各自的效果吗
- sol刚出来我都悲观的认为国模快赶不上了
- 按照“大模型没有秘密”这个原理，应该最后都会赶上
- review能力是怎么训的
- 7月18日11:38
- 但是我去年10月份就感觉“codex review是独一档的”了，到今天我也没有看到有哪一家接近的。
- Joe布衣:这个海外不限购?
- 9个月在AI时代几乎和永恒一样久
- 我kimi国内海外有3个年费以前就做代码快速过
- 从去年7月就感觉gemini遗忘上一句了，一年也没修好
- gemini这我实在是没看懂，感觉它们属于是“应有尽有”开局
- A\ chicken out 了
- A\ chicken out 了
- 能搞成这样也是令人疑惑
- 这几个厂应该是发现了一些左脚踩右脚的东西
- 先被 sol 揍再被 kimi 揍
- XS
- 7月18日11:41
- 现在大模型还缺类比和凝练
- 昨天竟然terra high fast把自己跑没钱了。。。还好刚刚重置了
- 类比不是挺好的吗
- 我感觉类比的一坨.……
- 尤其是涉及物理世界的类比
- 主要是模型没有世界模型，瞎类比的时候读起来又离谱又尴尬
- 感觉有点什么都够了的感觉
- 是因为我太菜了不如AI了
- 跨领域ai4s类比
- 跨领域ai4s类比
- 刘思皓:类比我觉得还好？凝练确实很难做
- 我感觉 oai 的当务之急是恢复 300k
- 懂了
- 明扬：主要是模型没有世界模型，瞎类比的时候读起来
- 又离谱又尴尬
- 5点不小心开了fast 9点到办公室11点重置....
- 看不出来下班的迹象
- 7月18日12:06
- 画了一个今天搞得工作流
- 刘思皓:你就开着sol ultra，然后告诉它：所有的实际
- 任务派发给k3 via kimi code来做
- 偶尔起一个contractor干一点急活
- 和 5.6 goal 比呢
- 刘思皓: 我今天试了一下 codex review + k3 build
- 爽得要命
- 只需要和Arch一直开会就好了
- 群主的奥卡姆和ssot现在我是每个任务都强调了
- 7月18日12:11
- 就是放在5.6 goal里面的
- 凝练的话 我自己有个chunqiu.skill 让大模型懂 微言大义
- 其实K3现在价格并不比gpt低………
- 刘思皓:
- 如果反推一下
- 但是它只要比opus低
- 哦那肯定呀。。。。
- 我还有有点不太喜欢gpt那个谨小慎微的build
- 7月18日12:12
- 太过谨慎
- 同样的活量gpt已经是1/4了
- 我还是喜欢claude opus那个比较大胆的build(如果被gpt包了一把的情况下)
- 但是Opus太贵了，k3一出立刻换掉
- 在做ssot blueprint的时候我会把人类的时间放在学习精确术语上，这样blueprint也更干净执行效率是不能靠猜的
- 确实，但是SSOT和奥卡姆是两个不一样的东西。
- 一个追求单一定义，一个追求定义的原子性
- 最后就是档位开够，然后不fast再省一份
- 我知道
- 刘思皓:确实，但是SSOT和奥卡姆是两个不一样的东
- 西。一个追求单一定义，一个追求定义的原子性
- 这俩都要求
- 你不是要求了4项么蒸了你这俩
- pus仙多用是仙学支加阶神，说相响，大候型能型感见
- 我觉得这种感觉是挺好的......但我不会加入
- SSOT其实是为了避免旧定义忘记删
- 旧文档太多了
- 刘思皓:SSOT其实是为了避免旧定义忘记删
- 是很需要这个的
- TDD估计模型已经学会了，其实加不加无所谓
- 求 prompt
- 刘思皓: 画了一个今天搞得工作流
- 我这边是经常混进来
- 5.5 5.6—样
- 我之前约束ssot都是用“最新”来约束，其实约束不住
- 按道理说，只看最新的意思是旧的别看了
- 但是还是混进来
- 有价值的变迁历史不代表落地工作的时候也要看
- 7月18日12:17
- 所以你要的不是SSOT，你需要我那个AGENTS里面最后一项，清Slop
- 你需要先一波把Slop全部干掉
- 如果只是在干活的时候加SSOT，它清slop也能清，但是会很慢
- 刘家昌: 求 prompt
- 而且我这个新的工作流并非类似humanize放手不管的搞法
- 它需要你全天候开会
- 有点慢，准备开源了独立布一套搞
- 7月18日12:21
- 但是好处是：你可以对开完会的东西，放心让solultra去搞
- 而且并行搞，带着k3搞，搞得很快
- 独立布一套k3？
- k3 thinking 有点过度了
- 目T2
- 2 onx
- 切 effort
- 3v: k3 thinking 有点过度了
- 7月18日12:30
- k3 thinking 有点过度了
- 目T
- 切 effort
- 3v: k3 thinking 有点过度了
- 7月18日12:30
- 出动脚本。正堂只塞几十行：检查GPU、运行测试、保春日患。
- 禁箱清单。列出源钮目兼至每一个文件名，防止有人都外意入文
- 个文件计算面改，证研文件内律没有业化。
- 最放 RUNNING/PASSED/FAILED小牌子、防止两个进程同时
- 完成后再给继果、日志和manifest计算一层哈希，组当于给实
- 这么谨慎是要干什么。。时间全浪费在这了
- 浪票在
- Python 验证runner.
- 行的Launch/封存都本。
- nventory. manifest. hash. atomic marker. artifact
- 约10229个文件。
- ing-wrap.TP8.continuation.canary 建立过度完备
- 这些opus4.8也会做
- 其实这个搞法我上一版工作流差不多
- Luke:
- 指纹
- 哈希
- 在超多轮迭代的时候还是有用的。
- 听我说谢谢你
- Luke:
- 其实这个搞法我上一版工作流差不多
- Luke:
- 7月18日12:35
- 无非就是专门搞了一个文件当开会记录
- 这样我可以把“设计”和“干活”解耦开
- 7月18日12:41
- 怎么又重置了
- 自然到期？
- 不如把项目里的技术经理产品经理数据分析岗位补齐了
- Luke:
- 7月18日12:47
- 杨佳豪上海般鹏人工智能:不如把项目里的技术经理产
- 品经理数据分析岗位补齐了
- “合并分支”
- 不过为什么PM这个角色还可以自己决定哪些部分合理哪些不合理呢
- 7月18日12:54
- 因为，有些东西开会的时候觉得合理，但是只有真正实现的时候才知道原来开会的时候某个点没想到
- 开会/做设计的时候无法尽善尽美
- 所以PM如果发现我会议记录不完善的点，我允许它直接跳过。
- 杨佳豪上海般鹏人工智能: 不如把项目里的技术经理产
- 品经理数据分析岗位补齐了
- 我这里只是借了一个PM的名字，实际上只是说：这个agent只用来delegation，只干"派发子代理到worktree"和
- 先去做别的。
- 然后这个点会被直接看PM的transcript的audit看到，然后告诉我，我再和arch针对这个点开会
- 7月18日12:56
- 这个类似于项目经理的助理?
- 项目助手
- 你说Audit吗？
- 这个工作
- 刘思皓:我这里只是借了一个PM的名字，实际上只是
- 说：这个agent只用来delegation，只干"派发子代理..
- 现在做agent我发现越做越像真的项目管理，我现在走的路线是直接套真实的项目管理分工，然后再加上AI特性化的
- 单越好：
- - arch：只和我开会，和我brainstorming，写开会记录
- - pm：只看开会记录，派发子代理，合并工作
- - audit：审查pm的执行轨迹，找出pm跳过的地方，告诉我
- 我：继续和arch开会
- 这样我就可以全天候一直和arch开会，一直做设计
- 而不用管pm到底怎么样。
- 主要是这些词和pmp和工作的词汇有重叠，感觉可以对齐，这样都能理解
- 刘思皓:差不多吧，可能人类用户是真的PM，但名字不
- 重要，我的核心想法很简单：让一个agent做一个最..
- 这个arch听起来比较像产品经理
- fot
- 7月18日13:01
- 没事，这些岗位怎么定工作都是企业内部说了算，大方向是确定的，具体工作细节各家不一样
- 有了
- 刘思皓:所以你要的不是SSOT，你需要我那个
- AGENTS里面最后一项，清Slop
- 清slop+chunqiu skill还可以
- 顷刻炼化
- 有个问题，这里的这些角色作为sub agnet，是全量的sub agent吗，比如arch pm audit这三个是一样的么
- 没太明白这个问题，这里带颜色的都是一个独立的终端窗口
- 7月18日13:06
- 但是我95%的时间只和arch对话
- ok我刚读了下上下文，发现了
- 我现在感觉设计agent架构也是个大工程，非常系统
- 就是我开了一个三栏的tmux，左中右分别是audit/arch/pm，然后我一整天的时间都几乎全在和arch聊天
- 我发现我聊天聊得越细
- 实现效流越京
- 导致他和我聊一会儿，就得去管理子代理合并的东西
- 我前几天拆了一下，就爽多了
- 好棒
- 刘思皓:就是我开了一个三栏的tmux，左中右分别是
- audit/arch/pm，然后我一整天的时间都几乎全在和..
- 而且和gpt-5.6聊天，真的很爽
- 聊天等于你俩互相教
- 刘思皓:就是我开了一个三栏的tmux，左中右分别是
- audit/arch/pm，然后我一整天的时间都几乎全在和...
- 而且主要是我不需要等agent
- 类似国际象棋里面pre-movr
- pre-move
- gpt live 看起来适合加入这个?
- 我可以一直输出设计，不用agents
- 不用*等*agents
- 这个好
- 刘思皓：差不多吧，可能人类用户是真的PM，但名字不
- 重要，我的核心想法很简单：让一个agent做一个最...
- draft-blueprint
- 刘思皓: pre-move

---

#### 原文 L58993–L59010

[回到原文件 L58993](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:58993)

- 7月18日13:21
- 这里有一个小trick，就是你不要造一个eda.skill
- Wendong: how
- 然后它就会自己flow起来
- 顺得不行
- 给一个eda.skill很容易忘而且每个版本的工具都有点不一样
- 很容易偏移不好维护
- 我直接把prompt hint塞进 module load的回调提示里面
- agent就跟开马里奥赛车一样，每干完一点活，都能吃到一个加速
- 7月18日13:24
- 越来越快
- 我让本科生先去执行“moduleload container”，回调打印就会让他去看看vcs/uvm/xcelium啥的
- 然后agent干完前仿，又会吃到一个要去干dc的提示
- 然后dc干完又会吃到一个去干icc/fc的提示
- 然后一路吃提示，吃到prime，吃到signoff
- 把skill的提示词切成很多段，埋在每段toolcall的回调里面，效果比一开始就给所有提示要好得多，本质上省了很多上下文
- 好像是更加progressive的disclosure

---

#### 原文 L59048–L59069

[回到原文件 L59048](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:59048)

- fable 准备炼化你了
- 刘家昌： 我第一次用的时候：没 goal 竟然能跑！现
- 在：我做完了第一阶段的手脚架，接下来我要做第一..
- gpt live的自动化程度还是不够高啊
- 7月18日15:15
- 需要严肃推广
- 刘家昌: codex 驱使 kimi 干活确实效果极佳
- 我越来越觉得
- 之前用 cursor 时候就经常 opus plan gpt 写
- cli做这个总是没有很顺手
- 7月18日15:21
- 这个也很容易，coding agent把每个 agent 抽象成一类成员、逐个配置使用的模型就行
- 翁大爷的狗@Rakuten:需要一个跨厂商的 harness
- omo之类的东西都做了但是我总感觉他们不会很主动的去用(除了搜代码时候
- 肖有为:这个也很容易，coding agent把每个 agent
- 抽象成一类成员、逐个配置使用的模型就行
- 7月18日15:30
- 确实，这套东西暴露给用户需要略微不同于codex等基于project/session的组织方式，才方便配置多个模型的合作
- 7月18日15:58
- 我配置了 Fable5 作为 omp 的 advisor，结果 Fable5 频繁拒绝回答
- tibo，altman，kimi们还得再加加油，让老达感受感受压力
- herdr is all you need

---

### 7月19日（第 2 段）

#### 原文 L59298–L59318

[回到原文件 L59298](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:59298)

- opus4.6居然是今年二月份才released的模型，这世界变化太快了
- 刘思皓: 按这个速度下去，Fable级别的开源模型，在
- 3-6个月就能出现了。
- "Luke" recalled a message
- 7月19日08:11
- terra/luna 新增了破坏性操作的指令，看来 terra 真和 luna 坐一桌了
- 7月19日08:19
- 醒来发现/goal没跑多少，停止，开始优化agent tools
- 7月19日09:16
- 不知道有没有人发现最近 Codex Sol Ultra 长程会很 drift from spec， invent 没有聊过的东西说我 rectified，
- compact 因为上一句话是 approved 然后他就 invent —个 compact 前甚至没问到的东西自顾自说用户 approve
- 了，一个写得很具体的 roadmap他会在某一步突然脑洞大开决定去做 roadmap 里没有的很难的事情
- 真心觉得现在这个 codex的 compact 不能要了
- 好想念以前啥都不会忘记的codex
- 昨天我也碰到了
- 我真的快被现在的 codex harness 搞疯了，就goal之后不久的某个版本开始的，感觉是为了少 compact
- 7月19日09:22
- 现在每次 compact 完比以前 claude code的 compact 还要傻，有没有什么 harness for sol 啊
- 然后就搞了三小时 simd 是吧（
- 明扬: compact之前让它调查rust nalg库生态，三角化

---

#### 原文 L59541–L59554

[回到原文件 L59541](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:59541)

- 开心的小福:这个优化和GPU编译器最重要的几个pass
- 关联太大，某些程序收益很大，但在大benchmark上...
- kimi 和 glm 差不少吧
- glm 抢不到
- 就这点拉完了
- glm 给我拉过两坨大的
- 大家看到福哥的猫了吗
- 开心的小福:感谢Humanize
- kimi虽然慢，之前的版本有时候写得不太好，但是一坨大的都没拉过
- glm 5.2 我才用了一下午就给我拉过两坨
- 而且很爱限流，用量内限流的那种，还很爱开 subagent，然后一限流 subagent failed 直接白跑
- Joe布衣: glm 抢不到
- 10:22

---

### 7月20日

#### 原文 L59770–L59870

[回到原文件 L59770](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:59770)

- 7月20日02:16
- 路由给你5.5你也能看到是5.5模型的
- 7月20日02:23
- Very good post
- mp.weixin.qq.com
- zartbot
- 7月20日02:28
- The best blogger
- 7月20日02:46
- 我确认这个claim
- 刘家昌： k3 暴打 4.8，我个人觉得超满血 4.6，体验比
- 降智 Fable好，不如满血 Fable
- 我至今都不知道4.6-4.7-4.8发生了什么
- 7月20日02:53
- Models are less able to communicate with humans
- 刘思皓:跑分上是涨的，但是使用体验上是变差的
- 7月20日02:59
- 我记得4.6之后出了一系列事情：1.4.7~4.8的使用体验变差；2. codex那边出了—个非常好用的goal；3. fable一系
- 列迷之操作
- 然后我就基本把主开发迁移到codex/gpt了
- 我觉得未来半年内我个人的开发配比会朝着大概是10:10:80=sol:fable:kimi去走
- 这不就3月份的事吗
- 对呀大概就是3-4月的事情4.6刚出来的时候真的很惊艳
- Weiyang: 这不就3月份的事吗
- 5.2就开始切了，5.4xhigh是最后一根稻草，当时封了一大批，然后花了很大精力5.4xhigh不胜任的任务依然4.6不胜任
- 那我花了那么大时间精力搞号不是傻逼么
- 7月20日03:04
- opus4.6和gpt5.2对我是一个转折点
- 5.2的长程一下子上来很多
- Yesterday
- tian
- Model
- Reauests
- got-5.0-tera
- 500.874
- 4748故意的
- 刘思皓:我记得4.6之后出了一系列事情：1.4.7~4.8的
- 使用体验变差；2.codex那边出了一个非常好用的go...
- 水任务直接terra，一天30-50B了
- 为啥故意这样
- 12月份第一个长程就是那个harness chromium in rust的哥
- 刘思皓: 5.2的长程一下子上来很多
- 7日20日.02:06
- 1-2月又出来一个yaoqi单prompt 做ethereum
- 5.2切就是第一时间
- 5.1没得用。所以12月份其实要对生活失去信心了，搞了一堆没啥用的opencode，ralph，各种skills
- 一个模型更新全带走了。没记错的话12.18更的5.2
- 花拳绣腿多了容易被力大砖飞带走
- 剩下就是保持学习ai知道我不知道的保持对ai做不到我做得到的小工具的理解
- 触发我买年费kimi的时间点是k2.6 原因忘了可能单纯处于防身
- kimi长程一整天了还没飘真的是让我被fable(我做好了！)和sol(我觉得这个细节还有待商榷)创暴的心得到了救治
- supergrok heavy看上去暂时不用防身，估计空了一大堆B300，根本没人用，尤其是grok cli出了丑闻以后
- 我原来想起床改成年付的结果起床没了
- Weiyang: 现在k3限购了。。
- 7月20日03:11
- 我已经把 claude 降到 20，codex降到 100，all in kimi 了
- kimi不比gpt贵吗(
- 话说新套餐的299额度大概有多少
- 刘思皓:我觉得未来半年内我个人的开发配比会朝着大
- 概是10:10:80=sol:fable:kimi去走
- 我不好说了
- 订阅是的
- 陈磊: kimi不比gpt贵吗(
- 你认为和terra差不多就行了
- 陈磊:话说新套餐的299额度大概有多少
- 方方面面，包括订阅折扣
- 我体验是差不多 sol 两倍价格
- 但具我学很比6（
- 那感觉太贵了，吃不消
- 毕竟 openai 和 A\ 不仅钱多更主要是卡多
- 我这有俩用例luna特化的还可以日常也不会用
- 哦不过我的体验基于的是 sol high vs kimi max
- 刘家昌: 我体验是差不多 sol 两倍价格
- kimi high 大概是 1/2 token
- 所以应该是差不多价格
- 不从api的角度来看，从订阅额度呢
- api 还是 kimi 便宜很多
- 7月20日03:16
- 我说的就是订阅额度
- 这样吗
- kimi还有优化空间
- 我不知道迷信1M是哪来的，hh
- 迷信1M会变得不幸。
- 我觉得 kimi high > sol high (不过我现在已经差不多是自干五无脑吹了听听就好(主要是昨天真的是被创飞了
- 纯粹学术对商业不是什么好事，希望这些人能用科研的深度看待社媒产品同样严肃成都哪怕分10%精力
- 但是并没有
- 我体验了一下让他吃100k的整个 spec，对我要做的整体聪明了很多，我觉得1M还是很有用的？
- Weiyang:迷信1M会变得不幸。
- 2个长程能把199rmb k2.5跑出429来真是哭笑不得没看出来是想让我用还是不想让我用
- 我的调研任务 2月 手搓gemini (追求facts) 3-4 切到kimi swarm 4月底切到 gpt5.5 + 大规模tmux codex
- gpt 似乎有个 10k token 单次输出的线？撞线了想点小办法就解决了
- 7月20日03:22
- 要做的整体聪明了很多，我觉得1M还是很有用的？
- kimi compact做的完全没有sol好啊
- oai compact有点东西吧
- 专门做的
- 嗯，终于走到了设计项目专用可视化实验管理台了.….
- 以前都没compact
- piano: kimi compact做的完全没有sol好啊

---

#### 原文 L59908–L59944

[回到原文件 L59908](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:59908)

- 最近有一个小心得，当你做的事情特别domain specific并且skill很多的时候。
- 可以做一个skill dropout，否则模型会变得非常路径依赖。
- 就是对自定义的skill set随机禁用一些吗，这是request/goal粒度吗，还是更细
- 香港科技大学研究助理教授徐策羽:最近有一个小心
- 得，当你做的事情特别domain specific并且skill很多...
- 是request/goal粒度吗，还是更细
- 7月20日10:51
- 细说，大概什么规模的 skill
- 香港科技大学 研究助理教授 徐策羽：最近有一个小心
- 得，当你做的事情特别domain specific并且skill很多...
- 这大概有多少 skills 呢
- 香港科技大学研究助理教授徐策羽:最近有一个小心
- 得，当你做的事情特别domain specific并且skill很多...
- 7月20日10:59
- 的用购曰这的
- 什么dropout
- 所了个长: 就是对自定义的skill set随机禁用一些吗，这
- 我的思路是这样的：只把一些 high level 的或者通用的这种 w
- 使用新的模型，也就是智力表现更好的模型的时候，还会对这
- sihao 好像说你让他做完一个事情，然后再给他一点 skill prompt
- 盲猜几百个（
- L.Zhu: 这大概有多少 skills 呢
- 然后就是没过一到两周，就让ag
- 7月20日11:10
- 我现在skill都是那种只有一个skill.md文件的
- 本质就是装了一大段提示词进去
- 直接让AI写的话很多都是废话
- Skill装多了，我觉得
- 主要是我这些skill是根据trace给distill出来的
- 有些非常的specific的，比如说EDA怎么跑，怎么优化某一种特定的pipeline这样的
- 如果这些skill全部load起来的话就会导致流程非常固定，没有自我探索力了
- 7月20日11:16
- https://chaoxu prof/posts/2026-07-18-ai-agents-for-the-working-mathematician html
- (unless they were solved before 10 hours).
- ns in 5 days. This is possible because recent

---

#### 原文 L59964–L59984

[回到原文件 L59964](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:59964)

- 说干就
- 这个群比ds harness质量高
- 我感觉 doc 是 repo 的神经，所以除了通用性的都不再包装成 skill了。
- 奇迹的闪光迪迦: 我现在skill都是那种只有一个skill.md
- 文件的
- 今天的sol ultra已经开始流口水了
- juice 砍完 context 砍
- juice真是一刀大动脉
- 我有个 naive的想法还没试，给 doc 以类型标注，比如xxxx.fun.md 代表无状态的操作流程，xxxx.state.md 代表一
- 些状态文件。然后agents.md里面给一个类型解释的总则。
- Reiko: 我感觉 doc 是 repo的神经，所以除了通用性
- 的都不再包装成 skill 了。
- juice又砍了？之前砍过一次说在测试然后恢复了。
- Weiyang: juice 砍完 context 砍
- 换句话说就是文件名自解释。我现在层层展开的doc解释都在agents.md里，要逐条写。感觉这个想法可以简化这一点
- Reiko:我有个naive的想法还没试，给doc以类型标
- 这个是wiki么
- Reiko: 我有个 naive的想法还没试，给 doc 以类型标
- 注，比如xxxx.fun.md代表无状态的操作流程，xxxx....
- 大概4-5月,我着有个团队在研究
- 我觉得可以直接github白嫖

---

### 7月21日

#### 原文 L60059–L60073

[回到原文件 L60059](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:60059)

- Luke:claudecode现在就老喜欢把过时的实验结果写
- 到memory
- 7月21日03:23
- 发布到现在一直持续高强度蹬K3，蹬完了一个$100和一个$200，在我自己的任务上的体验是不知道为什么突然聪
- 明的 Fable >> K3 > Sol > 不知道为什么突然犯傻的 Fable
- 以及我收回之前我觉得 Kimi Code CLI 最好用的观点，现在 Claude Code + K3 我觉得体验最好，OpenCode 还是
- 很拉胯。Kimi CLI还是很不错的但是重构完以后我觉得好不稳定
- 7月21日03:41
- Did you also try to use Kimi in the codex harness
- 没有试过，他们应该是只有 Kimi Code 和 Claude Code 是 first class support
- It' s very convenient to develop within it
- 7月21日03:59

---

#### 原文 L60080–L60096

[回到原文件 L60080](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:60080)

- 跟着炒就行了
- kimi 挑了一个相对中庸的 checkpoint，如果只讨论 coding 能力似乎他们有更好的
- 高情商的说还可以未来可期
- 7月21日04:09
- 很任务相关吧。例如 frontend 我昨天的体验是 Kimi 真的无人能及 Fable也不能。而且我拿 high 和 high 比，max
- 和 max可能不是。我不知道为什么这两天 sol一天到晚创我，就算是 ultra 也创我，但是 kimi 一次都没创过我
- 刘思皓:我觉得K3显然是一个好模型，但是超越Sol有
- 点夸张
- kimi max我觉得大可不必，太慢太耗 token了，可能我的任务没复杂到那种程度吧
- 7月21日04:27
- 是做 demo的话
- 他们是专门刷过的
- 但是我已经很久没写过前端code了
- 我的前端记忆还停留在，“gemini前端不错”，的时代
- 因为这个赛道确实KOL喜欢+容易出效果
- 如果你说的前端

---

### 7月22日

#### 原文 L61025–L61042

[回到原文件 L61025](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:61025)

- 7月22日09:34
- 我搞到chipagent了
- 准备测试一下
- 干嘛的
- 奇迹的闪光迪迦:我搞到chipagent了
- chipstack
- 看看究竟是这种微调过后的领域专用agent厉害
- 卖算力卡的
- 还是Claude这种厉害
- https://chipagents.ai
- 我给这个公司投过简历
- 7月22日09:47
- 是这个公司的重大损失
- 这个去nv demo过
- 奇迹的闪光迪迦: https://chipagents.ai
- 没买
- 千里马常有，而伯乐不常有

---

### 7月23日

#### 原文 L61570–L61610

[回到原文件 L61570](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:61570)

- 的人巨多
- 美国试错主要靠h1b
- 很急，我权重呢
- 我已经蹬空了，还有两天才重置我不是太信任的Fable，还有四天才重置Kimi，我现在咋活啊
- Sol 我现在拿来清屎修 bug 和 harden code，一如既往地好用，但是真的不敢拿来写新东西了
- 7月23日04:00
- Fable厉害是厉害，懒也是真懒
- 必须盯着看
- 我冲了一个季度的GLM Max
- 5.2的说法不是太给力但是让我勉为其难期待一下吧（
- 为什么不敢写新的呀
- 刘家昌: Sol我现在拿来清屎修 bug 和 harden code,
- 一如既往地好用，但是真的不敢拿来写新东西了
- 7月23日04:05
- 造星舰过度防御过度设计
- B4RRy: 为什么不敢写新的呀
- 我：我想要一个轮胎船；Sol：如果要上太空怎么办
- 刘家昌:5.2的说法不是太给力但是让我勉为其难期待
- 一下吧（
- 指打杂或者各种实现类的事情
- 不知道为什么它特别喜欢开 subagent但是基建跟不上，烧一半五小时然后白干
- 翁大爷的狗@Rakuten:当狗很好用
- 疯狂超载
- 大部分时候我都不喜欢开sub
- 可能因为我没有那么大的项目要拉
- 让我下午再给他一次机会
- 我的 glm 订阅在疯狂落灰
- 1.5线模型利润率就是高
- 7月23日04:10
- 又不舍得卖或者退订，万一又搞个大的呢
- 考虑到如果你用满他是亏的
- 利润率其实没有多高
- 7月23日04:11
- 那我gpt肯定一直是负的
- 我都凌晨1点开始上班的。

---

#### 原文 L61750–L61789

[回到原文件 L61750](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:61750)

- 同意
- 那些coding agent就应该裸着用
- skill啥的都是曲线救国
- 7月23日07:57
- 公司的fable今天突然不偷懒了，不知道为什么在造星舰，没有/btw就要造一整天了（
- 求教，是裸的 pi 还是 omp？说效果好的是哪套流程？感觉 pi 因为太简单了所以好复杂（
- 刘思皓: pi的那个巧思挺多的
- 7月23日08:16
- Claude Code 2.1.218· 隐藏改动
- ☑ 团队共享记忆落地
- 二进制内含党整leommemory 目录·只读同步
- 共享记忆(5K0ILmd)模制
- 硬性告说：终不把密销/凭语耳进团队识纪
- 单个 SKILLmc>128KB 南接酰过
- Observer 观察者子 Agent
- 最合观常者盯 worer的活动线票·子 agent案认据承
- ☑ 拒答→自动换模型 机制星性化
- 新壤 xsretusolflbock谱求员 + 摘型 lotch
- env: DISABLE REFUSALFALLBACK / _CATCH_ALL
- 降级时保留1M上下文
- ☐ 记亿回忆反债卡/MCP 新能力
- XAAISEP-990) MCP 统一IdP·一次配置全集用
- ☐ 代号 gate 洗牌
- 断增4个/移逊2个·地代号无可解质语文
- 7月23日08:58
- 我确实能感觉到K3还是不如GPT 5.6
- emory 目录只读同步
- 共享记忆 或iI (5K)Lmd）模制
- 硬性告说：统不把害销/凭语耳进团队识纪
- 单个SKLLmg>128K8 南港胎过
- Observer 观察者子 Agent
- workdtree 隔凋 + fonout 上型
- ☑ 拒答→自动换模型 机制星性化
- 断壤xtrefusao-follbock谱求员 + 摘型 loatch
- :ABLE REFUSALFALBACK/_CATCHALL
- 降级时保留1M上下文
- ☐ 记亿回忆反快卡 / MCP 新能力
- XAAISEP-990) MCP 统一IdP·一次配置全集用
- ☐ 代号 gate 洗牌
- 断增4个/移通2个·地代号无可解读语文

---

#### 原文 L61902–L61917

[回到原文件 L61902](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:61902)

- 是我基本上现在就是每天早上收到synopsys或者cadence给我发的更新邮件然后我都直接转发给我在集群上部署好
- 的agent
- 刘家昌:！是的 codex 运维真的是一绝
- 然后到学校的时候集群基本就是最新的了
- 维护得又好又鲁棒，还给你搞很严谨的合规认证
- 7月23日11:19
- 有趣，clalude superpower writing skill还能tdd开发skill，先让他不用skill来做，看subagent 怎么失败，学习了
- 这不就是那个skill- creator的搞法?
- 那个不好用开发出来的skill很烂
- 这样。
- 7月23日13:02
- 感觉瓶颈是multiagent long horizon workflow的不断自动迭代
- 不断优化工具实现，上下文效率
- gpt 5.6 审查轨迹内省的能力感觉还是有欠缺

---

#### 原文 L61922–L61942

[回到原文件 L61922](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:61922)

- "刘思皓" recalled a message
- 现在做科研最好的方式就是把自己的课题变成一个well formed 的Agent可以爬山的问题
- 依然梯度下降
- 刘思皓:现在做科研最好的方式就是把自己的课题变成
- 一个well formed 的Agent可以爬山的问题
- 然后只要往里面不停地灌注token就好了
- 所以以后只会有frontend deployment mathematicians
- 刘思皓:现在做科研最好的方式就是把自己的课题变成
- 一个well formed的Agent可以爬山的问题
- 我想写点东西不过还是让luna帮我写吧
- 定命题搜正例反例随便vibe一篇
- eval体系要好、反馈回路要短、基建要鲁棒
- 剩下交给Agent爬山就好了
- 确实
- 现在就是会在workflow里面发现需要eval的地方
- 那么会不会有不知道如何eval的问题
- 有的
- when in doubt, call a verifier subagent
- Weiyang: 那么会不会有不知道如何eval的问题
- 而且很多东西很难eval 有些是不知道怎么eval 有些是基建不支持eval

---

### 7月24日

#### 原文 L62162–L62175

[回到原文件 L62162](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62162)

- self learning把这个得
- 有个叫penguinharness的可以自己改进skill
- 我也做了一个但是还没有反馈
- 感觉应该有，但是不知道在哪里
- 就直接搜索调用某个skill的记录就好了把调用的记录和结果找出来丢给agent
- 这个skill用的越多feedback loop越好做
- "Luke" recalled a message
- 这个挺奇怪的，做了一大堆什么app SDK，看不太懂
- chen:有个叫penguinharness的可以自己改进skill
- 核心在这penguin-harness/packages/skills/skills/agent-optimization/SKILL.md
- chen:核心在这penguin-harness/packages/skills/
- skills/agent-optimization/SKILL.md
- 7月24日10:22
- 一觉醒来 gpt 又造了一条星舰

---

#### 原文 L62235–L62265

[回到原文件 L62235](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62235)

- 也能干，出品问题比较多，基本都要使劲返修
- 是的，有段时间甚至能直接把我前几句话忘掉了，最近每次都得重新描述一下关键上下文
- 刘家昌: 我觉得最重要的就是 codex的 compact 比之
- 前真的差太太太多了，根本记不住自己在干啥，就像...
- thinking juice砍到上线的1/5了，但是又喜欢摇人
- 刘家昌: 我觉得最重要的就是 codex的 compact 比之
- 我现在真心觉得只有 Kimi 能 build... Sol 造舰 Fable 睡觉
- 什么时候我才能再买一个$200
- 是不是应该让造舰的 Sol 去唤醒睡觉的 Fable
- 7月24日10:43
- humanize1
- 刘家昌: 是不是应该让造舰的 Sol 去唤醒睡觉的 Fable
- 我fable build 倒是不会睡觉，就是等gpu训练就会睡过去。
- 还右二天
- 刘家昌: 什么时候我才能再买一个$200
- 等token factory全面启动
- 会偷懒... Sol 会 flag 出无数个确实该做没做的事情
- Luke: 我fable build 倒是不会睡觉，就是等gpu训练就
- 会睡过去。
- 果然得重新祭出 humanize1了
- 说好的不需要 harness的时代呢
- 我的最新发现是gpt做完一个任务调一次verifier不靠谱
- 又一堆问题不知道为啥
- 7月24日10:48
- 会提出很多扯淡的问题，就强行说，明明不是问题。
- Shom:又一堆问题不知道为啥
- 最近发现codex的额度一下就用完了，是不是价格战打不起了哦
- 我也发现了，一小时蹬10%
- Canaan:最近发现codex的额度一下就用完了，是不是
- 价格战打不起了哦

---

#### 原文 L62333–L62342

[回到原文件 L62333](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62333)

- 其实我建议你给他一个本地的.env 把你的常用 key 装进去
- 哎，其实我开了agent forwarding，不知道为什么他不用
- 之前我的humanize就是因为有一个环节必须有人类参与但是codex不让停跑了一晚上
- 7月24日11:14
- 快进到 codex 去互联网帮你扒了一个
- 我就想写点代码
- humanize的本质是不是就是gan
- 我搞humanize的时候完全没想到有这一天
- L.Zhu:

---

#### 原文 L62538–L62553

[回到原文件 L62538](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62538)

- 7月24日17:48
- 大概就跟有人喜欢看两个agent协同工
- 作一样，一个coding一个review，本
- 质上是在感受技术的进步
- 男的为什么喜欢看百
- 合。。
- 7月24日17:56
- orchestrator 被 subagent 撐爆了 belike
- 对的对的，白台后当就是 agent team
- is
- 翁大爷的翁大爷:
- orchestrator 被 subagent 撑爆了 belike
- 7月24日18:05
- 可以的，百合Agent Team
- 翁大爷的狗@Rakuten:
- 7月24日18:10

---

### 7月25日

#### 原文 L62566–L63210

[回到原文件 L62566](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:62566)

- 7月25日 00:22
- 之前好像有人能把cli接到网页端用5.6pro
- 7月25日00:58
- 又整了—个Kimi Vivace
- 我又活了
- 刘思皓: 又整了—个Kimi Vivace
- 海外159刀
- JW99: 这是啥?
- 海外套餐换算过来咋样
- 比国内699
- 有说法，但是我不能乱说
- JW99:这是啥?
- sihao 评测—下 opus5
- 现在买不了了，找群里的Kimi义父申请的
- Opus 5
- 7月25日01:03
- 就是Kimi200万的那个订阅
- JW99: 这是啥?
- sihao 评测一下 opus5
- 现在买不了了，找群里的Kimi义父申请的
- Opus 5
- un
- 7月25日01:03
- 这分刷的比 fable 还高
- 我服了
- https://www.anthropic.com/news/claude-opus-5
- 这么离谱
- 你也是有点快
- 3分钟前刚出
- 现在能用了吗
- 有route吗
- 怎么感觉 opus5 没啥讨论的人呀
- opus5比fable5好还便宜那fable5是要淘汰了吗
- 其实我还是有一点期待 opus5 的。。。
- 毕竟现在实际上 cc 能用的额度只有一半
- 不挤牙膏了吗？
- 直接一脚踩在牙膏管上了啊
- 我觉得这动作有点变形
- 如果Opus 5 > Fable 5
- 那说明之前关于Mythow/Fable的叙事都是在弄啥了...
- 急了啊
- K3的势头必须被止住啊
- 7月25日01:08
- 哈哈哈
- 显著比opus 4.8/Kimi K3强是没问题的(我们提前access了测了一些internal benchmark)，fable没法测所以没得比hhh
- 竞争真好
- 竞争正好
- 真好
- 竞争真好
- 我很急，我今天刚用gpt刷新球
- 所有人都在卷
- 卷起来卷起来
- 7月25日01:08
- 明天 tibo 肯定要发力
- 又是老黃躺贏
- 只要Kimi K3不被美国政府封掉
- 老黄估计要赢麻了
- 为什么我Claude Code看不到Opus 5
- 那你直接/model claude-opus-5
- 应该也能用
- 这里有一个很幽默的点
- 59.8%
- health 列出的是 mythos 的分
- 只有网页端有
- 感谢好使了
- 7月25日01:14
- bio 也是
- Mythos 5
- 89.0%
- human solved
- 我估摸着是 fable 全拒答了测不出来
- 感觉真急了
- JW99:急了啊
- 7月25日01:19
- 确实
- 翁大爷的狗@Rakuten: 其实我还是有一点期待 opus5
- 的。。。
- XS
- 翁大爷的狗@Rakuten:我估摸着是 fable 全拒答了测
- 不出来
- 感谢K3
- JW99: K3 的势头必须被止住啊
- 不是因为他们发了善心，而是因为K3来过
- 你别说你真别说
- 泽文：给中国用户放开。市场直接回来
- 我开始测opus5了
- 要是比如下一个中国模型超过了a/可能就真开放了
- Claude update?
- 感谢杨圣
- 要先更新
- 到2.1.219就可以了
- 我以为fable是高于opus的
- 7月25日01:22
- 每次都是要先更新，上次有经验了
- 刚好比gpt-5.6便宜一点
- $5
- 笑死
- 大参数，然后产生更好的数据，然后蒸馏
- 刘诗楠:我以为fable是高于opus的
- 新闻稿发布到claude update，中间间隔了10分钟
- Luke: Claude update?
- 我刚刚一直没刷出更新
- 现在有了
- 爷青结，Claude居然比gpt便宜了
- 翁大爷的狗@Rakuten:爷青结，Claude居然比gpt便
- 宜了
- 开蹬了
- 不是因为他们发了善心，而是因为K3来过
- Luke:不是因为他们发了善心，而是因为K3来过
- 什么双向奔赴
- 蹲一个 opus5 体验
- 之前拒绝回答的简单的bio的题现在都会了
- 真不容易啊
- 6月底那一出是啥意思？没看懂
- 精心营造的叙事被k3 干碎了
- rrupt and send immedia
- 了新模型。后续派发Agen
- 在跑了
- Julian: 蹲一个 opus5 体验
- 我觉得A\搞marketing的那个团队真的有点奇怪
- JW99:6月底那一出是啥意思？没看懂
- 看不懂操作
- 7月25日01:27
- 1. Fable/Mythow吹上天，喜提EC
- 2. 然后Fable关于订阅的策略不断延期
- 3. 然后是Opus 5 > Fable 5
- 我怀疑都没有markerting
- 刘思皓: 我觉得A\搞marketing的那个团队真的有点奇
- 可能6月跳过了marketing team是老达亲手操作了
- 都是ceo拍板的
- 这不是一直给自己捅刀吗….….
- 7月25日01:28
- 亲自指挥亲自部署的
- 都尼玛吓人
- 本来其实是昨天发的
- Amadeus: 我怀疑都没有markerting
- 所以昨天的rumor其实是对的
- 固然便宜，然而也要考虑玻利维亚汇率的影响
- 翁大爷的狗@Rakuten:爷青结，Claude居然比gpt便
- 宜了
- 他们push了一天
- 尼玛
- 尼日利亚claude定价翻倍
- 玻利维亚比索gpt定价和美元脱钩
- 优化了—下tldraw cli
- 我刚冲了 grok 会员
- 还好我没冲 K3 会员
- 尼日利亚claude定价翻倍
- 玻利维亚比索gpt定价和美元脱钩
- 优化了—下tIdraw cli
- gpt复刻这个图的能力好强
- 除了一条线没连对剩下都对了
- 一年换三代
- 极氪操作
- 现在海外都买不了了，我找Kimi内部的人才又拿到一个Vivace号
- JW99:还好我没冲 K3 会员
- 7月25日01:35
- "JW99" recalled a message
- "刘思皓" recalled a message
- "刘思皓" recalled a message
- "JW99" recalled a message
- 中u
- 冰糖雪梨
- C8018
- 別搞
- 目瞪狗呆
- 发我
- 7月25日01:35
- 別搞
- 发我
- 这个是不是得两个8xB300才能跑起来
- 我现在就等7/27了
- 我有啊
- 20台吧 在一个机房
- ？啥玩意
- ？啥
- 发啥了
- 目瞪狗呆
- 目瞪狗呆
- 7月25日01:41
- 该来娱乐测试一下有哪些群友荣升 opus 级知名度了
- 好的，群主是
- 止一个。
- UCLA 读博，导师是 Tony N
- 他参与的论文里我记得有MIC
- 我似乎很早之前就被模型吸收了
- 主要是看起来 opus 5 确实有一点小 fable 的味道
- 7月25日01:51
- 有没有和肥波一个 size的风险
- opus5涨价了吗
- 7月25日01:56
- 没吧
- 7月25日02:02
- 这个是能让agent画出美丽图表的妙妙工具吗
- API Cost (grouped by Vendor)
- Usage
- Model
- Modol Id
- Vendor
- Anthropio
- Fable 5
- claude-fable-5
- Opus 5
- elaude-opus-5
- Opus 4.8
- claude-opus-4-8
- Sonnet 5
- claude-sonnet-S
- Anthropic tota
- OpenAI
- GPT-5.6 Luna
- qpt-5.6-luna
- EPT-S.6 Sol
- qpt-5.6-aol
- GPT-5.6
- qpt-5.6-tarra
- GPT-5.5
- apt-5.5
- UpanAT Tntel
- Monnshot
- K3
- k3
- Zhipu
- GUM S.2
- qtm 5.2
- TOTAL
- 7月25日02:10
- API Cost (grouped by Vendor)
- Usage
- Hodol Id
- Vendor
- Hodel
- elaude-sonnet-S
- qpt-5.6-aol
- GPT-5.6 Sol
- K3
- k3
- Zhipu
- GUM S.2
- qtm 5.2
- TOTAL
- 这些天大混战了一下
- 让我心情舒畅
- Claude占据了我16%的token，但是花了我20%的钱
- 7月25日02:12
- Kimi占据了我8%的token，但是只花了我4%的钱
- 按照当前这个模式，我觉得我个人最后GPT要占40%，然后剩下每家20%
- 然后总成本砍掉50%
- 爽飞了，真便宜
- 是怎么决定什么 task 给哪个 model 的呀
- 刘思皓:
- 7月25日02:19
- 这是个啥tool啊 不同任务给不同harness吗?
- 放个大图分享一下
- cool
- 7月25日02:27
- 在部署前的安全评估中，Anthropic 对 Claude Opus 5 进行了多维度的风险测试：
- • 对齐风险：模型整体能力并未超越当前最强的通用模型Claude Fable 5。评估认为其对齐风险极低，未发现新的令
- 人担忧的属性。
- Claude Opus 5 是 Anthropic 迄今为止最对齐的模型，在遵守 Claude 宪法方面的得分超过了 Sonnet 5 和
- Mythos 5。
- • 幻觉问题：尽管整体准确率更高，但模型在陈述事实时的幻觉率略高于Opus4.8，有时会表现出过度自信，甚至
- 在不确定的情况下给出肯定的答案。
- (：
- Coding、Computer use 和 Browser use的复杂注入攻击。
- A/宪法
- 创死我了
- 我本地做了一个简单的router
- Marcus M: 是怎么决定什么 task 给哪个 model的呀
- 参考fireworks那一套东西
- 但是我这个不太有代表性
- 因为kimi k3刚出没几天，而且我token几天就没了
- 所以只是我自己的preferrence
- code/cowork agent 早停行为与交付物质量：Reward Seeking 现象及其缓解措施 - storm的文章- 知乎
- https://zhuanlan.zhihu.com/p/2064127486921909656
- 监控工具是我自己写得ai-usage，一直都在群公告里面。
- icic thx!
- 刘思皓: 我本地做了一个简单的router
- 7月25日02:38
- 我现在用下来的感觉（过去4-5天）就是：
- - GPT keeps its crown for being reviewer and gate-keeper
- - Claude is still better than Kimi, but only marginal
- - Kimi is way much more cost-effective
- - GLM works, but not as good as Kimi K3
- 7月25日02:47
- Where is Qwen LoL
- 还有人用吗
- 7月25日02:52
- where is Junrong LoL
- where is Junrong
- 夜里的qwen 3.8挺好的 量大管饱
- 我也用不了那么大导师
- 倒是
- where is Junrong LoL
- 7月25日03:30
- 想调查一下如果大家目前在用 3rd-party harness的话主要在用哪些呢 opencode, hermes, omp?
- 7月25日03:37
- pi ftw
- 我感觉现在的模型用了harness之后的数据做post train，到达了一定阶段后原本复杂的harness就应该被淘汰，换上
- 最简单的。
- 7月25日03:43
- omp
- https://github.com/SihaoLiu/skills/tree/main/ask
- ask-{claude, codex, kimi, glm}
- 以防有人需要，欢迎炼化
- 7月25日04:19
- 棒全支持
- 群友之前是不是有人炼化出了个omh的codex版本skill
- 7月25日06:17
- 为什么 agentic coding 53.4%>53.5?
- 你发现了华点
- 7月25日07:50
- Opus突然变便宜好多
- 开始全面价格战了啊
- 竞争真好
- 克陷知
- 就怕preipo充业绩过程中一直降智
- 7月25日07:57
- 上周
- 这周
- 7月25日07:57
- 上周
- 这周
- 我感觉GPT造星舰的问题确实有点严重
- 我现在只让GPT做设计+协调+审查，Claude和Kimi干Build
- 以及GLM，build都挺高效的
- GPT这个谨慎的作风我确实有点顶不住
- 7月25日08:07
- opus5出来之后又可以codex review claude generate了
- 7月25日08:12
- 这样吗，我立刻试试
- 7月25日 08:20
- 这边炼化了omh最核心的部分做了一个h2的最简实现，群友有兴趣的话可以试试看呀：https://github.com/
- humanfia/flowjanus
- 现在相当于只是一个agent的抽象层
- 7月25日08:21
- 马上会加入flow call flow之类的特性
- 可以群里at我许愿需要的功能，也可以提issue
- nb 周末玩玩看
- 张子健:这边炼化了omh最核心的部分做了一个h2的最
- 简实现，群友有兴趣的话可以试试看呀：https://git...
- 7月25日 08:33
- 好耶
- 张子健:这边炼化了omh最核心的部分做了一个h2的最
- 简实现，群友有兴趣的话可以试试看呀：https://git...
- 7月25日08:40
- 所以gptl以外日均多少B?
- 刘思皓：
- 简单体验感觉 5 还不错？
- (别降智了球球
- 7月25日11:00
- 1B多一点
- Weiyang: 所以gpt以外日均多少B?
- 不到2B
- 7月25日12:07
- "Luke" recalled a message
- @Yu学—下
- 刘思皓:我现在只让GPT做设计+协调+审查，Claude
- 和Kimi干Build
- 这种情况下干build的effort一般设置到多高呢，也要xhigh吗
- 刘思皓:我现在只让GPT做设计+协调+审查，Claude
- 和Kimi干Build
- 我一般直接给max
- 方差小一点
- 因为我也不是一次只build一个feature，都是一大堆feature一起build
- 但是很影响budget 哇，哈哈
- 刘思皓: 开max也不是很影响latency
- 这个使用cc 驱动还是pi 这种来驱动呢，
- 刘思皓: 开max也不是很影响latency
- 7月25日12:31
- 我一般有原生就用原生的
- 没原生就claude code
- 7月25日12:15
- 了解！感谢分享
- 7月25日12:41
- 7月25日12:52
- deepseek一直没有自己的harness吗
- 我才发现deepcode是社区自己搞的
- 没有啊
- 你不是在吗
- 都没发布
- 我以为那个是类似Codex App的东西
- 类似Cursor一样的东西
- 不然cuitianyi 怎么招人都成抽象段子了呢
- 刘思皓: 我才发现deepcode是社区自己搞的
- 7月25日13:17
- 啊那现在是Kimicode为主吗
- 刘思皓: 我一般有原生就用原生的
- 其他写ask-xxx 或者ask-via-cc/cx
- 刘思皓: 我用k3肯定走kimi code啊
- 哦我这里也是优先走原生的harness
- 刘思皓: https://github.com/SihaoLiu/skills/tree/
- main/ask
- 没有原生的走cc
- 奥 get 那你主sess用cc吗
- k3 我用cc 感觉也还行
- 我主session用codex+gpt
- Zeng haolun: 奥 get 那你主sess用cc吗
- 主session只干交互式设计，并发调度，合并，审查
- 不build
- get 我之前也从omh切回codex做主的
- 刘思皓: 我主session用codex+gpt
- 目T
- 发现已经是再次保存了
- 保存!
- 磁盘空间不够好痛苦hhh
- 7月25日13:24
- 这个现在叫 graph engineering
- 刘思皓:
- 然后我现在K3打工其实也不是只用k3
- fot
- 目dlauda kimi alm泪着求
- "刘思皓" recalled a message
- 谁有usage用谁的，都有usage的话优先级大概是 kimi ≈claude > glm
- 感觉能把grok加一下
- grok tps挺高 服务器都空也没人说他降智 主要是没啥人用
- 我明天试试
- 马圣的卡太多了
- 不过额度其实给的不算多
- 7月25日13:29
- 折算下来跟5.6terra比耐用性差多少。。。月卡的话
- 翁大爷的狗@Rakuten:不过额度其实给的不算多
- 160刀 vs 250刀
- 不知道，没用过Terra
- 跟sol比?
- 6月的grok会员没有周限还比较爽，现在有周限且额度计算很神秘
- sol体感比5.5时期砍了55%
- 好像在grok build里用，和你用oauth的计费是分开的
- 价格不变，周限回去了
- Weiyang: sol体感比5.5时期砍了55%
- 我7.13买的heavy，然后15给了一次周重置，同事生图去了
- 都是buzz word
- Joe布衣: 这个现在叫 graph engineering
- 7月25日13:39
- LangGraph 表示生不逢时
- 还是要编排agent而非lm node
- 后者写点代码就好了
- 7月25日14:44
- 同档位吗，还是 sol max -> 5.5 xhigh
- Weiyang: sol体感比5.5时期砍了55%
- "chen" recalled a message
- 有人试过墨水屏么？
- 延迟咋样了现在
- 7月25日14:50
- 感觉挺酷炫的
- 据说最顶级的方案能做到80Hz了，不过用这玩意儿不太讲究刷新率
- Reiko:延迟咋样了现在
- tibo大哥今天咋没发卡
- "张东宇"recalled a message
- 这是墨水屏平板吗？我记得有5k左右的23寸墨水屏显示器
- 刷归刷，延迟还是很高，键盘输入延迟还好，触摸的时候跟不跟手马上就暴露出来了
- 那看来这个技术是早就到头了
- 7月25日14:52
- 记错了
- DSUNG大上科技
- 请凉季
- 13.3英寸
- 37H2
- 透费钢彩色墨水屏显示器
- Paperlike 13K
- 独有源色增强算法
- 速重维美浓品所
- 15%￥4299元
- v3999
- 专用享：国凉从息3周定息
- DASUNG大上科技13.3英寸超高刷墨水屏量示器
- 13K彩屏&累白屏 37Hz
- 08%
- 点场9年老店：山编电子线0排的第1出店线电子间运路
- 后自活预计6小时内发货，后天送达
- 用北石家庄 快递：必诺费
- 7天无理由途货吸速退款
- E-ia电子图水屏
- 13.3美寸
- 是否有而进好
- 辞箱尺寸
- 加入购格车
- 立即购买
- 那看来这个技术是早就到头了
- 7月25日14:52
- 记错了
- 请凉季
- DSUNG大上科技
- 13.3英寸
- 39H2
- 钢彩色墨水屏显示器
- Paperlike 13K
- 独有源色增强算法
- 速出维美浓品屏
- 15%￥4299元
- 3669
- 司用享：国凉从息3周定息
- DASUNG大上科技13.3英寸超高碍墨水屏显示器
- 13K彩屏&累自屏 37Hz
- 08%
- 志铺9年老店店编电子阅0器始第1名店铺电子阅用源
- 后自活预计6小时内发货，后天送达
- 用北石率庄 快递：免诺责
- 7天无理由速货：依速退拟
- 13.3美寸
- E-ra电子图水屏
- 是否有而进好
- 算箱尺寸
- 加入购格车
- 立即购买
- 就是价格贵的离谱
- 我的34寸带鱼屏，小米显示器，带HDR400，180hz高刷，也才一千多块包邮到家
- 是为了护眼吗hhh
- 这也太贵了
- terminal一直往上刷不会很难受吗
- https://www.reddit.com/r/eink/comments/1twtj82/ssh_terminal_on_remarkable_paper_pro_yay_or_nay/
- 7月25日15:12
- 没绷住
- 5.5 high 到sol max
- Reiko: 同档位吗，还是 sol max -> 5.5 xhigh
- 不得不说5.5high真很好用
- 2.5B砍到1.25B 每周 cachehit接近
- 很多时候我用sol max出一堆问题换回5.5就好了
- 截止到6.7
- B4RRy: 不得不说5.5high真很好用
- 这个到底了不就会开始网上刷新吗
- 明扬: https://www.reddit.com/r/eink/comments/
- 1twtj82/ssh_terminal_on_remarkable_paper_pro_..
- 网上滚动
- gpt5.5六月八日杀人事件
- *往上
- 越古越强!
- 天天516阶段没有根治办法
- 什么6。7
- 永远缅怀
- B4RRy: 越古越强!
- 截止到6月7日
- 4.23-6.7的5.5
- 这是什么梗
- okay
- Weiyang: 截止到6.7
- 不是梗是工作实测
- 7月25日15:16
- 即使是现在我感觉还是最好用的
- 我说话g化了
- Weiyang: 不是梗是工作实测
- 当然最近还是有变笨的感觉
- 5.6 感觉就剩个 subagent 了
- 我也想用grok但是没买
- grok如果你用了生图
- 会挤占 grok build 的用量吧
- 并不是独立的
- 看了一圈10-13寸墨水屏的价格，觉得还是iPad更划算
- 7月25日15:24
- 墨水屏的用处是啥
- 护眼么
- 墨水屏的用处是啥
- 这东西刷新率低看 terminal 不好受的吧
- 还好吧也有60Hz的了
- 翁大爷的狗@Rakuten: 这东西刷新率低看 terminal 不
- 好受的吧
- 泡面搭档
- 哦准确来说应该是响应时间？
- 拖影解决了吗
- 7月25日15:31
- 16.6ms
- 翁大爷的狗@Rakuten:哦准确来说应该是响应时间?
- 物理原理上做不到，职能弱化
- 翁大爷的狗@Rakuten:拖影解决了吗
- 看视频还有轻微可感知拖影
- 7月25日15:48
- 确实最近感觉 codex的压缩没有之前那么神奇了
- 自局家认图：博为了领は ClacdBastd.创建丁领配置件绩写
- 是™他自己写的说我写的
- 0ts
- E2_M20HCPU_32.速
- 的构篇纸观格，虚以证车腊三薪器失擅了
- 内管，文件状态相横作信量、确认差值生播的不图它归
- 所以 300k >> 200k
- 阿科拉屎拉的
- 翁大爷的狗@Rakuten:是™他自己写的说我写的
- 7月25日15:50
- codex compact什么原理
- 测试下来256k压缩一下感觉没啥问题
- nerf 完之后承诺会改回 300k 是最骚的
- Reiko: 所以 300k >> 200k
- nerf 完之后承诺会改回 300k 但是怎么还没改呢
- 7月25日15:57
- Didn't Graduate Texts
- in Mathematics
- Yuri Anime Analysis
- 单看数学 fable 还是权威啊
- Reiko:
- Yu Deng
- A Course in
- 7月25日16:06
- 谢谢，我又切回f5了
- Reiko: 单看数学 fable 还是权威啊
- 虽然不做数学研究，还是要附庸风雅一番
- 为啥国模在数学榜上差这么多？
- 7月25日16:11
- 没训过
- 按理说这类数据不是更容易合成么？
- 问就是来不及
- 这些无关紧要的任务
- 优先级很低的
- 用户又不 care
- 刷刷写前端 demo 用户一看哇好 jb 酷炫
- 要是我做决策也是先 recursive 起来再说
- 我想请问一下各位，请问使用 FMC 来扩展FPGA 的板载 DDR 容量方便吗
- 7月25日16:29
- https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models看起来非常合理
- 我感觉我很久以前就不怎么写乱七八糟的指示了
- Reiko: https://claude.com/blog/the-new-rules-of-
- context-engineering-for-claude-5-generation-m...
- 除了我受不了G语言的时候
- LEAN训的少
- 明扬:我还以为k3，qwen-max起码能接近gpt5.5的水
- 一直以来的一个问题是：它的产物并不符合这个原则。

---

#### 原文 L63248–L63261

[回到原文件 L63248](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:63248)

- 就比如说一段话一个比较中心的主题，句子为该主题服务，按照逻辑展开；但句子又应该保持一定灵活性。术语不应
- 该漂移，但依赖于上下文不必严格用完整称呼等等。一个文档这样层层展开，这才是人类的写法。
- Reiko:ai理解一篇文章怎么写，但不会做
- ai写的文档和写的代码是一个味的。但文档的清理比代码清理复杂的多。我目前没有啥好的practice，只能预制几个
- skill让它稍微清理一下。
- 但据说 oai的memory升级了，也许应该试试了
- 7月25日17:24
- 我的codex 今天下午—直stream disconnected before completion: no_biscuit_no_service
- 有人遇到过吗
- https://status.openai.com/
- 因为确实炸了
- 我目前述是坚持不开memory。
- 明扬：ai搞砸了某事，被同事骂一顿，然后记下了，规
- 则文件里末尾加了一段。结果和前面某段，或者指向...

---

### 7月26日（第 2 段）

#### 原文 L63631–L63674

[回到原文件 L63631](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:63631)

- .、十分钟能验证的事情先做
- 第四，必须有停止条件。比如最多问五个高要喻问题，或者当目标、边界、验收标准和不可逆决策
- 都明确后立即停止，剩余小问题采用推荐默认值
- claude就是这样把，会静默出错，很多没对齐他也给你实现了
- 明扬:我觉得这个形态很难实现
- 我刻意让AI只维护当前系统行为的文档，丢弃所有老的决策，设计，以免占用上下文，干脆不要被grep给列出来
- 本质感觉还是AI偷懒
- 没有被训练做到0假设以及真的尽力了
- 我觉得这个形态很难实现
- 明扬:
- 项目规模稍微大一点，或者迭代久一点，某些模块被后续的agent修改十几次，还都是补丁式的修改。最后代码行为
- 的推理难度会急剧升高，准确度也会大幅下降
- 从回复就感觉得到经常说这里可能会有xxx问题
- 很多时候明明可以去完整的一行一行读代码按照逻辑分析把这个可能变成一定会有或者不会有
- 很多人推崇要让AI留下所有上下文，什么时候修改，为什么修改，开过什么会等等
- 我觉得完全没必要，污染上下文
- 我倾向于认为这是阅读出发点的问题
- 7月26日11:14
- 我也是，这个很麻烦，claude很喜欢caveat，把老的都写上然后看错。
- 明扬:我刻意让AI只维护当前系统行为的文档，丢弃所
- 有老的决策，设计，以免占用上下文，干脆不要被gr..
- B4RRy:很多时候明明可以去完整的一行一行读代码按
- 照逻辑分析把这个可能变成一定会有或者不会有
- 是的
- 明扬：我觉得完全没必要，污染上下文
- 从命题出发，命题就三行，且可以被机器验证。上下文最少。
- 从证明出发，证明本身其实不能直接描述命题，测试用例也是不准确的，文档可能过时。AI再浪费宝贵的上下文和
- CoT去推理代码行为，还不一定对。
- 命题是啥
- 这个overhead很大
- 明扬:很多人推崇要让AI留下所有上下文，什么时候修
- 改，为什么修改，开过什么会等等
- 我更多情况是他说p0p1做两个月，p2p3做多久，缺乏自我察觉
- 实际上p0p1我需要他一下午做完
- 5.6对未来任务预估可以做
- 7月26日11:21
- 这个我也留其实是为了更好的完善自己的workflow的用途吧
- 明扬：很多人推崇要让AI留下所有上下文，什么时候修
- 改，为什么修改，开过什么会等等
- 每一次看他犯了什么毛病再去项怎么样稍微缓解一下还是说无解的
- 本文从运行时功能和数据流的角赏描述当前仓席的架构。以及岗未达成的未来目
- 标，业务状态模块在这里被看作规则和状态流转代码；文档不讨论项目的其他能
- 力，也只在路由与产物层面涉及客户端。本文只反映当前设计与未来目标：不保
- 留过时的历史设计，不记录变迁过程与决策依据。后者留给 git历史，以及

---

#### 原文 L63692–L63702

[回到原文件 L63692](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:63692)

- Luke: 命题是啥
- 第一版在我看不见的地方，AI可能已经写了数千行甚至万行Python代码，囊括了用户注册登录权限管理，orm跨数据
- 库部署支持。甚至还有几千行近百个单元测试和集成测试。
- 一个月后开了一个新Session，Al读了一遍当前项目的框架，设计，部署，历史文档，以及我的模糊全文检索需求。
- AI发现项目里所有测试和功能都依赖了sqlite，隧决定fork了sqlite，给它加上了fulltext和vector扩展支持，写了2万
- 行C代码。
- 7月26日11:40
- 但这真的是我想要的么？如果AI直接去读项目里已存代码，它大概率会觉得这条路径是正确的。但实际上已存代码和
- 文档也是前任AI生成出来的，我只需要一个博客网站而已，至于它用什么数据库，还是直接在agents.md里写了几行
- 命令: hexo serve。我并不在乎
- 若是从原始需求+增量需求出发，那最简单的路径应该是数据库迁移到pg，它既支持全文检索，又支持向量

---

#### 原文 L63755–L63797

[回到原文件 L63755](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:63755)

- 4句提示词吧估计
- Luke: claude 表示没有依赖，做不了
- 《调研得很好那你做吧》
- 谁提谁做的具象化
- 7月26日13:46
- 明扬: iPad books可以导入epub(pandoc直接从md
- 生成) 然后agent可以从books的sqlite数据库读回..
- 说不定能产品化
- 没什么护城河，就是阅读器暴露mcp接口，然后agent和书本交互
- 7月26日13:52
- 理论上讲，两个窗口，一个看MD，然后复制出来给另一个聊天追问，在线修改也一样
- 7月26日14:11
- 我发现一个大问题：sol ultra 不会健康的维护subagent 生命周期
- 特别是压缩无数轮之后，有的深层subagent都失联了...
- 都失联了...
- 这设计有点弱智
- 这种 subagent 抢占计算资源，让我 cpu持续 90度以上
- Reiko: 特别是压缩无数轮之后，有的深层 subagent
- 都失联了...
- 7月26日14:19
- 想了想这个情景以前版本至少 5.4 就有了，压缩的时候不会刻意保留 subagent 信息。现在虽然 multi agent v2
- 了，但压缩还是问题。
- 翁大爷的狗@Rakuten: 这设计有点弱智
- 而且还有一个不确定的问题似乎：“上下文载荷漂移”
- main agent从开始自己不干复杂推理和计算，渐渐变得倾向于自己干了
- 这个不确定的点是说：中间我打断更改了任务。
- Reiko:而且还有一个不确定的问题似乎：“上下文载荷
- 漂移”
- 7月26日14:25
- 看来 sol ultra 还是需要开 goal，只弄一些状态文件不够
- 7月26日14:49
- xs一直有这个问题，甚至有一次他丢了一个 subagent然后改变方向以后说为啥我的 main一直在被污染，让我写个
- gate 防止 poisoned commit 进 main
- Reiko: 特别是压缩无数轮之后，有的深层 subagent
- 都失联了...
- *契而不舍（我的输入法在干啥
- 因为是锲qie而不舍
- goal算是pin—个context置底么
- Reiko:看来 sol ultra 还是需要开 goal，只弄一些状态
- 文件不够
- ？？？是的但是我打的是 qie

---

#### 原文 L63807–L63827

[回到原文件 L63807](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:63807)

- 是的，失联不可怕，最多占几个槽位，可怕的是它还在夸父逐日
- 刘家昌: 那个失联的 agent 弃而不舍地 merge 进
- main
- 7月26日18:34
- 开 goal 也没用，搞不懂。
- 开放探索任务的稳定性对于 200k 的 sol还是大难了吗
- Reiko: 看来 sol ultra 还是需要开 goal，只弄一些状态
- 文件不够
- 一天内压缩了几十轮，不知道漂移到哪去了
- 我没啥解决办法，目前是跑几个阶段然后停下来先和我对齐。
- 感觉这个环节其实就是我一直找的真正的记忆机制
- Reiko:我没啥解决办法，目前是跑几个阶段然后停下来
- 先和我对齐。
- 7月26日18:40
- human as memory
- 7月26日18:45
- milestone，不应误读为同一验证只能使用一个 kernel。Lacia会
- 并行分片同一项exact regression、记录每个进程对应的分片，
- 并在结果返回后立即回收 subagent / session，避免失联副本。
- 当前这个过度集中的checker会先被正常中断，再拆成可独立结
- 束的短分片。

---

### 7月28日

#### 原文 L64426–L64438

[回到原文件 L64426](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:64426)

- 实就是“我上我也行”的意思
- humanize1的时候sihao说llm是新时代的编译器
- sol ultra的 workflow 是内嵌到模型里了还是有个隐藏harness
- 刘思皓: 探索型任务我觉得需要flow+agent，毕竟一波
- 写到80-90% sol这个agentic flow还是很好做的
- plan写好的时候你应该已经知道代码长啥样就差写出来了
- 我现在的想法是，当下阶段。我操纵ai实现软件，就像我操纵方向盘行驶在路上
- x 上员工说是专门训的。另外 jsonl 里面可以找到一段超短的提示词说明 agent tree
- Horace: sol ultra 的 workflow 是内嵌到模型里了还是
- 有个隐藏 harness
- 虽然大部分时候我被任务追着屁股跑没这个时间
- 期间我会根据路面情况，车头朝向射线一直微调方向盘

---

#### 原文 L64473–L65024

[回到原文件 L64473](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:64473)

- 我发现claude和gpt都有一个很愚蠢的问题：就是本来长程跑的好好的，你想塞一个简单的steer进去，它就很容易会
- 停下来。
- 但是这个时候你只要在你的short steer prompt末尾加上一个"继续主线工作“，它就还能继续长程跑。
- puatsication.tont Flloon
- 内容分级
- 有没有说法
- 但我发现本身的dynamic workflow;你steer进去他会重新修改workflow然后继续跑
- 哦我说的这个是没上任何flow的情况
- dynamic workflow本来就上了一层harness
- 我现在其实蛮希望它自主停下的
- 那现在这个长程是直接给plan开跑吗
- 刘思皓:...本来长程跑的好好的...
- 7月28日11:38
- 无脑续跑是slop堆砌的开始
- 7月28日12:26
- codex又重置了?
- 7月28日12:33
- 今天大量观测到 Sol:你这个船它漏宇宙射线，这是个 PO blocker。Kimi:不我们不需要造星舰
- 刘家昌: 我现在是Fable 调研和用最不绕弯子最讲人话
- 的方法interactive问我要做什么，Kimi做忠实永远...
- 非常快乐
- Kimi这么聪明?
- 刘家昌:今天大量观测到Sol:你这个船它漏宇宙射
- 线，这是个 P0 blocker。Kimi:不我们不需要造星舰
- 反正我观测到了，而且Kimi的确是唯一—个至今还没创过我的模型，除了真特么慢
- 我真后悔了，我kimi只买了99，一句话就limit
- 11.15
- 北田圭人: codex又重置了?
- 之前vibecoding刚火的时候有人说prd已经死了。现在我看这玩意不仅没死，还越来越重要了。。
- 考虑到我没有省钱需求继续terra
- 我 K3 发布后至今唯——次干预 Kimi 是它漏了—个 project 大 spec 的条件(不是 task 的)于是有个 design
- decision没想明白，在那打了很久的圈，但是至少一行屎都没给我写下去
- 这种情况 Sol星舰应该已经造好了，Fable应该已经随便写个框架睡下了（
- 其实我高斯泼溅也训了几版成功的了让他优化prior去了
- 哦说起来具身智能最近设备涨价了
- 7月28日12:39
- 好消息，重置了，坏消息，还在造船坞
- kimi该不会其实是比gpt-5.6还大吧
- 为了造星舰，船坞现在在r14修订
- 大就是好啊
- 其实我高斯泼溅也训了几版成功的了让他优化prior去了
- 哦说起来具身智能最近设备涨价了
- 都怪英伟达
- 再这么下去我要导入毛选skill了
- 《当前的主要矛盾》
- Kimi: 船坞 1 船坞 2 船坞 3 都不用建，因为 project spec 里说了我们在造小船而不是星舰：
- root fix is one rule - publish a
- -always identity at its declaration,
- -one-driver separately - which dissoly
- 1 (no current-spawn result seeding ne
- itted outputs stay unpublished per §8)
- 2, and blocker 3, and deletes the
- 我真的是太感恩了
- 7月28日12:44
- Sol给我列了三个大船坞，换别的模型已经开始修了
- 我最近开始用裸 pi，零自己定制 prompt，裸极短 system prompt，只装了 ponytail，subagent 和 cache
- optimizer，感觉体验很好（
- 陈泽恺: 是我的prompt写的不够好吗
- 有种优秀的食材只要最简单的烹饪的感觉
- 而且超特么省 context 和 token
- 7月28日12:49
- 大家的agent都好聪明
- 落下泪来
- 是我的prompt写的不够好吗
- 而且超特么省 context 和 token
- 7月28日12:49
- pi 主要是快+你可以 xjb 改
- (感觉在这个群里这样说应该是个大异端xs
- 刘家昌:我最近开始用裸pi，零自己定制 prompt，裸
- 极短 system prompt， 只装了 ponytail, subagent ...
- 不见得
- 我pi都不用了
- 主要是我就带一根铅笔进考场（
- 刘桑有用pi吗
- 翁大爷的狗@Rakuten: pi 主要是快+你可以 xjb 改
- 我之前那个omh就是omp改的
- 我觉得pi是个正路
- pi正在什么地方
- 模型越强
- e-就应该越城强
- 我从omh -> codex -> pi
- 同意
- 刘思皓: 我觉得pi是个正路
- subagent 可以指定模型我觉得超开心，只要跟 AI 提一嘴你可以用 subagent 哦，然后他就会自动去用 fable plan，
- k3 写代码，sol review <del>造星舰</del>，啥都不用做，上下文啥都没花
- 我在长程任务上用sol和opus 5做了benchmarking
- 都是pi更好一些
- 我就说：开始做 XXX，implement and review using subagents
- 我估算下来大概699的Kimi plan正好是一个月1B的量
- 感觉略少不够用
- 自从换了 pi 我的 kimi plan 够用了
- 有点神奇，怎么做到的呢；是本地有什么前置知识吗
- 刘家昌: subagent 可以指定模型我觉得超开心，只要
- 跟 AI 提一嘴你可以用 subagent 哦，然后他就会自...
- 上周真的灾难
- 7月28日12:54
- 我估算下来大概699的Kimiplan正好是一个月1B的量
- 感觉略少不够用
- 自从换了 pi 我的 kimi plan 够用了
- 有点神奇，怎么做到的呢；是本地有什么前置知识吗
- 刘家昌: subagent 可以指定模型我觉得超开心，只要
- 跟 Al 提一嘴你可以用 subagent 哦，然后他就会自...
- 上周真的灾难
- pi-subagent 可以选 role的 model，他们 call的时候选 role就可以了
- 刘诗楠：有点神奇，怎么做到的呢；是本地有什么前置
- 知识吗
- 哦还有 scout 我配的 codex spark，又快又不花钱(
- 效果并没变差
- 草想起来还有个近乎免费的5.3-codex-spark模型
- 7月28日12:57
- 我当时搞omh的时候就觉得piagent一定是codex之后的主流，最近忙毕业的事情humanize相关的东西有点搁置
- 了，一个月之后all in humanize
- 所以pi比omp更有优势吗?
- 刘家昌: 自从换了 pi 我的 kimi plan 够用了 😊
- 我不知道啊我在群里问过 omp 体验如何没人理我我就直接上 pi了，我只知道真的太省 token了（
- 原理是不会造星舰
- 啥工具都不给你（
- 郑权: pi省token的原理是什么
- 你就 bash 跑
- 那可能效果不会很好
- pi放弃了交互性和用户性->性能提升
- 一直现场造工具
- 我很讨厌omp 的这个 xd://
- 但其实现在主流模型基本都会现场写工具
- read
- Read file contents
- bash
- Execute bash commands
- edit
- Edit files with find/replace
- write - Write files (creates/overwri
- - Search file contents (read-c
- grep
- ult)
- find
- - Find files by glob pattern
- y default)
- 1s
- - List directory contents (rea
- efault)
- Read file contents
- read
- Write files (creates/overwri
- write
- default)
- ls
- List directory contents (rea
- efault)
- read bash edit write
- 没有想明白为什么这东西比 tool search 好
- 没了
- claude/codex 很多设计都是强调交互性牺牲token efficiency
- 用pi刷swebench terminalbench都会比cc高一点
- 是的
- 我也测了而且token 可能消耗量只有一半
- 但是我觉得这个很糟糕啊，我觉得codex就特别喜欢给我跑一个linline的python脚本，然后经常自己grammar error
- 因为cc每个turn都要把那—堆systemprompt发一次
- 说明模型太差了
- 香港科技大学 研究助理教授徐策羽：但是我觉得这个很
- 糟糕啊，我觉得codex就特别喜欢给我跑一个linline..
- k3 直接 bash 几乎不失败
- https://github.com/rohitg00/agentmemory
- 我觉得omp里面的这个插件实名好用
- 香港科技大学 研究助理教授 徐策羽: https://
- github.com/rohitg00/agentmemory
- 尤其是在group开发的时候
- 香港科技大学 研究助理教授 徐策羽：但是我觉得这个很
- 糟糕啊，我觉得codex就特别喜欢给我跑一个linline...
- 调shell，经常忘记转义序列
- 7月28日13:02
- 但这是5.6-sol啊
- 刘家昌：说明模型太差了
- 而且当他陷入这个之后，就会变成又耗output token又耗时间的循环
- 我现在连 memory 都不用，AGENTS.md 写你给我把整个 project spec 读一遍放在 context 里。然后我要他记住什
- 么就直接叫他改（
- 大概 50k tokens overhead 解干愁
- 哪有那么多要记住的东西jpg
- 能想明白的事情别记住
- 一个人做的时候没问题，但是当你10个人一起vibe一个大东西的时候就不太行
- 刘家昌: 我现在连 memory都不用，AGENTS.md 写
- 你给我把整个 project spec 读一遍放在 context 里...
- 是我需要的
- L: pi放弃了交互性 和用户性 -> 性能提升
- 放手去干
- 干不好原地开喷
- 那可能确实是，不过我这种情况的操作是，agents.md里写，你每个文件夹维护一个readme，每次改东西你都必须
- 香港科技大学研究助理教授徐策羽：一个人做的时候没
- 问题，但是当你10个人一起vibe一个大东西的时候就...
- 体验还可以，我觉得比总是不知道为啥莫名其妙写的memory可靠一点（
- 而且跨 agent
- 单独维护干净点
- 大家都用AGENTS.md，那这个东西高强度污染大家的
- 7月28日13:07
- 建立你和AI之间私密小暗号这一块
- 那说明 sol 太差了（逃
- 郑权: 但这是5.6-sol啊
- MVP
- 可以关掉的
- 翁大爷的狗@Rakuten: 我很讨厌omp 的这个 xd://
- MVP
- 我就关了
- MVP
- 开这东西agent连个web_search都用不明白了
- 评价已经下调到不降智5.5 + 自建harness
- 刘家昌：那说明 sol 太差了（逃
- 不让它写agents.md 里，直接用文件夹readme，只读写和自己有关系的
- Weiyang: 大家都用AGENTS.md，那这个东西高强度
- 污染大家的
- 感觉问题不大
- 或者，大模型训练也有大年小年，或者一代架构一代制程的规律
- 我连README都没有，SSOT在别的地方
- 刘家昌: 反正我在公司的 repo 是这样搞的
- 而且是带版本号的
- 别碰我研发大版本。
- 小版本谁爱干啥谁干啥去
- 我自己维护的东西其实gpt一直提醒我要做唯一权威啥的，只是知道这个叫SSOT是后来了
- 又回到那个问题了，默认gantt渲染没有好看的，不符合每日审美
- 我的体验是 K3 造的工具都很好用也不怎么花 token 基本上一次成功，反而是他不熟悉的没有 RL 过的 harness
- tools 会调用失败
- 郑权：一直现场造工具
- 尝试给 pi 加过几个 tool，性能都 degrade了
- 于是删掉一切开始选择最简单的烹饪
- sed 用得比 read / edit 6 多了，我都想把这两个工具也禁用了
- (别说我这就试试
- (别说我这就试试
- cursor写了fastgrep
- 7月28日13:15
- 你也要重复造这些吗【
- 说不定是个ai native os的方向
- 纯兼容 性能再看fs core又话出多少
- 优化
- 我觉得工具链装全了让 AI 自己去脑补自己想用啥挺好的，你上一个 unix server 也不会先去 tab tab 读一遍所有装了
- 的命令（
- system prompt 写有啥工具我觉得和 tab tab 没啥本质区别
- 哦，难怪Claude总是往用户级memory里记录，不往工程里存
- (开始疯狂暴论)
- 7月28日13:43
- 这个就会随便干点啥事都有可能传播一堆 doc 同步
- 刘家昌：那可能确实是，不过我这种情况的操作是，
- agents.md 里写，你每个文件夹维护一个 readme，...
- 7月28日13:50
- 我觉得没什么问题？
- Reiko: 这个就会随便干点啥事都有可能传播一堆 doc
- 同步
- 我称之为doc as neuron（
- 刘家昌： 我觉得没什么问题?
- 有时候可能不稳定，有过时的，不知道是不是我的指令问题
- 感觉 doc同步的传播值得优化一下
- 7月28日13:55
- 我维护过doc的依赖链想让agent根据依赖链自动更新doc
- 但最后的效果不是很好
- 我也是这么想的
- 愚鱼: 只有完全程序化才能保证确定性
- 但……失去了可读性
- 我在尝试书籍化，然后定期开agent扫描，审计书籍
- 话说kimi code现在可以推荐吗?
- 7月28日14:00
- 不推荐
- okok
- 哦我写的是你commit的时候得检查一遍，你看到过时的时候不管是不是你干的都得改对
- Reiko:有时候可能不稳定，有过时的，不知道是不是我
- 的指令问题
- 不过这个是公司的共享项目我这么干，自己的东西我就单文件强制全读了
- kimi RL kimi code 是一等公民，比 opencode 好非常非常多。但是我现在叛逃去用 pi 了(
- 香港科技大学 研究助理教授 徐策羽:话说kimi code现
- 在可以推荐吗？
- 提一嘴，kimi RL 用的是I旧 kimi cli
- 刘家昌: kimi RL kimi code 是一等公民，比
- opencode 好非常非常多。但是我现在叛逃去用 pi ..
- 不是这个 ts 写的 kimi code
- pi 不是 RL —等公民但是我发现只给它 bash 和 subagent 效果意外的好(
- 7月28日14:05
- 啊那我是不是也应该用kimi cli
- 但是 Kimi cli 不维护了吧
- 没人维护乙但目好田的（
- 不过 kimi cli 作者跑路了
- 啊对xs
- kimi cli 好用
- kimi code 有点难拼
- 没人维护了但是好用的（
- claude code 也是一等公民，如果不怕 A 畜塞私货可以用
- 一比一复刻吗
- 明扬：我在尝试书籍化，然后定期开agent扫描，审计
- 书籍
- 我用了很多，文件系统这块 track每个文件了
- ok我试试
- 刘家昌: 哦我写的是你 commit 的时候得检查一遍，你
- 看到过时的时候不管是不是你干的都得改对
- 这个方式是全量的而且你特别关心recall的时候是无视上下文的
- 上下文长了短了你也就扫个64K token
- Weiyang:一比一复刻吗
- 我的方法不是泛用的
- 因为我现在懒得很，100%代码都是ai生成的，所以意图对齐对我来说很重要，比文字真实准确性更重要
- 5.3 codex时期，翻译、跨语言迁移、逐文件解释我用的是一个skill，不过翻译有点大材小用了route到小模型比较好
- 文字再精确，不说人话，我看不懂也没用
- 所以我让agent牺牲精确性，提升阅读体验，维护一本说明书。
- 7月28日14:11
- 刚看到另一个群里的不说人话：
- 10:09
- 媒体以和解损安宁
- 以及起诉政防这个动作本身（删要被法院拟下）
- 解码器存量栏—一我们知识框架的独有进镜，也是最被
- 低估的科目：约三十万联邦公务员离开，国务院资深外
- 交官、NTH/CDC科学家、FAA、IRS的骨干层流失
- 政府的组织惯例和隐性知诀正是丰田式的“不在任
- 何文物里”的存量，裁博的岗位可以重设，网络指列散
- 了只能接年代重速。更深一层：十万美元H·1B新签费
- =对解码器进口警道征税——我们的框乘把“持续吸入
- 全球已训练好的人“记为美国四百年最核心的制度优
- 现在政策在给进气口加阻，这是慢变量，当期
- GDP看不见，账单在五到十五年后寄到（反向信号已
- 现：欧洲与中国的控角计划：对冲信号也真实：AI私
- 营部门的磁力仍在，民调量示七成以上选民其实支持
- H-1B). twa
- 先例棒枪糕：扣款、SchedudeF、梁急经济权、司法
- 部定向，入股企业、急诚旅免一—每件工民经此滴示后
- 都上了货架，两党的后任都可取用，格鲁否亚的粮识在
- 此放大：制度是双向快灾量，西硬球是会传染约：最深
- 的改变可能不是任何单项行为，是莫单置永久更新了。
- 三、格审插标与裁决
- 资本与人才流向：美脸靠AI热潮续创新高、外资米
- 骤。但2025年美元指数扩73年以来最差上半年、
- 各国央行持续增持黄金、uf对冲比例上升——市通的
- 7月28日14:11
- 我们 fable 是这样的
- 哦我看着差点以为乱码了，原来是有逻辑的话
- 人类衰退之后 ai 说话是不是都这样的
- 我是不敢跟 Fable 讲中文的
- 十年前的话这应该是个科幻好点子
- Reiko: 人类衰退之后 ai 说话是不是都这样的
- A畜没资格指责任何说人话的模型蒸馏他们（
- 没有人类了
- 明扬:
- 这是模型问题还是infra出问题了.....
- 哦我看着差点以为乱码了，原来是有逻辑的话
- 人类衰退之后 ai 说话是不是都这样的
- 7月28日14:16
- 毕竟它上次蒸馏这么不说人话的模型把自己蒸馏到不说人话了
- 7月28日14:25
- A 畜没资格指责任何说人话的模型蒸馏他们（
- 怎么又重置了
- ???
- 7月28日14:35
- 已经习惯了
- 刘家昌:我是不敢跟Fable讲中文的
- 从4.7 用到5
- 已经麻了
- ai不用喘气
- 明扬:
- 7月28日14:43
- 删掉 pi 的 read/edit/write 之后目测没有产生任何负面影响，我现在只有 bash 和产生只有 bash 的 subagent(
- 纯吨吨
- 没办法数tool call来得到agent行为的粗略估计
- agent喜欢写掺python的和巨长pipe的扭曲命令
- 我感觉已经rl成肌肉记忆了，至少 k3的扭曲命令没有影响过推理也几乎没有失败过
- Shom: agent喜欢写掺python的和巨长pipe的扭曲命
- 比 tools 成功率还高
- xs那确实
- 但对agent像预测下一个token一样自然
- 感觉也合理，一行bash能把所有信息全提出来
- 我感觉我现在在搞的东西适合写成个小工具+skill
- 我觉得本质原因是因为，现在大模型的上下文是线性的。
- 7月28日14:48
- 应该向作家们取取经，他们是怎么让这些模型说人话的
- 完事借鉴过来
- 如果context是一个json这样的data-structure，并且可以以不破坏KV-Cache的causal属性的情况下去edit这个data-
- structure，那么tool call的形式可以变得非常的自由，上下文管理也会更方便。
- Opus 5让他说英文都看不懂了
- 蒸的什么玩意
- 7月28日14:56
- 贼酷炫，一个命令git add commit push还叠加python查看 gpu 叠加
- Shom: agent喜欢写掺python的和巨长pipe的扭曲命
- 香港科技大学 研究助理教授 徐策羽:如果context是一
- 个json这样的data-structure，并且可以以不破坏KV...
- ai native以后我觉得我还丢失了一项能力
- 给系统快速止血
- 以前屎山是我造的，出毛病我知道咋立即恢复
- 现在屎山是过去几个月ai造的，出故障以后，新的会话里ai一通分析，修正，部署，然后无效。再分析，修正，部
- 署，结果搞出来更大的篓子
- 优化spec重写一次说不定更好
- 明扬:现在屎山是过去几个月ai造的，出故障以后，新
- 的会话里ai一通分析，修正，部署，然后无效。再分...
- 为了不重写就要测试ai的能力边界
- 7月28日15:01
- 有亿点难，我觉得过于理想化了
- 是从这里有感而发
- 刚刚我看着它一个命令从 pi 目录拿出 credentials 直接 call api url 做了一次服务自检，一次 bash 一次成功
- Luke: 贼酷炫，一个命令git add commit push还叠加
- python查看 gpu叠加
- 贼炫酷
- 实际上这个故障需要的是分离职责和部署
- 但恰好我还看得懂这里ai给我的执行路线，要求它转向
- 7月28日15:06
- 其实看完这段以后我是有点一身冷汗的，这个刚好卡在我能识别出来的边界
- 那么就意味着，是不是有更多的，我闭着眼approve的修复方案，是走了弯路
- 我要去掉 ponytail 看看 K3 的简单烹饪的极限在哪（
- 现在除了 bash 和 subagent 我只剩下 ponytail 了
- 我现在强制要求它给多个 option，每个 option 有 concrete example，写清楚 pros and cons
- 明扬：其实看完这段以后我是有点一身冷汗的，这个刚
- 好卡在我能识别出来的边界
- 如果我十秒看不懂说明他没写清楚，骂他重写
- 7月28日15:13
- 有人daily大规模高强度使用过raft.build吗？求分享experience
- 7月28日15:24
- 群聊的聊天记录
- 愚鱼: [图片]
- 愚鱼:大家好，我已经放弃 slock了，转向
- 用 herdr 建立开发 group
- 愚鱼: slock的可观测性一直做不好，气...
- 怎么互相发消息的
- 7月28日15:25
- 主要是我想multi-human multi-agent
- 现在cursor性价比怎么样
- MHMA
- "开源芯片 agent flow 张宇鑫" recalled a message
- 我看cursor品鉴国模挺全的最近还折扣
- 我们能不能自己蹬一个raft啊
- 虚宝弄了个开源 slock
- 香港科技大学研究助理教授徐策羽:我们能不能自己蹬
- 一个raft啊
- 看看虚宝蹬的那个？@蟑螂恶霸盾构机
- Vibe Coding Taxonomy: Single Human Single Agent; Single Human Multiple Agent; Multi-Human Single
- Agent; Multi-Human Multi-Agent
- 哦?
- 愚鱼: 虚宝弄了个开源 slock
- 好像还没放出来
- akane:看看虚宝蹬的那个？@蟑螂恶霸盾构机
- 香港科技大学研究助理教授徐策羽:我觉得MHMA方
- 案是我们组现在的痛点
- 7月28日15:30
- 不如你现在的
- 开源芯片 agent flow 张宇鑫: 现在cursor性价比怎么
- 我懒得买国模了渠道太多我没精力
- 现在换技术栈比雕花还快
- 因为自己handle不了技术栈就用旧技术栈有些问题这个ai调期彻底低估了都解决不了
- 7月28日15:36
- true，mini swe agent 就是只有bash，很多榜上表现都很好，比codex Claude code/pi/opencode 强
- 刘家昌: 删掉 pi 的 read/edit/write 之后目测没有产生
- 任何负面影响，我现在只有 bash 和产生只有 bash..
- mhma到后面都是肌肉记忆了
- 频道这个概念我试验过
- 我的感觉是模型厂企业版功能没啥必要蹭车
- 最后造了个ai native telegram
- 开源芯片agentflow张宝鑫: 频道这个概含我试验过
- 2 个Pod
- TICKET-G
- TICHET-1
- 1个 Pod
- TICKET-2
- TICKET-4
- 父子调用关系垢扑
- 运行中
- 跨智能体实的事件
- 状面
- 总控 running/executing + 4/4 个子 Codex 运行，4/4 条 pod:read 症 active
- 噱头居多,核心是训模型里面
- 父子调用关系历扑
- 跨智能体实的事件
- 噱头居多,核心是训模型里面
- 很快放出来
- 香港科技大学研究助理教授徐策羽:我们能不能自己蹬
- 一个raft啊
- 还在微调前端
- 这周可以放出来
- 话说我应该用什么开源协议
- 7月28日15:41
- 无脑MIT吗
- @蟑螂恶霸盾构机 xubao license：二次开发的产品中必须包含一条对rust.cat的广告
- mhma并不是一个h*a的问题
- 是h+a cn2问题
- 不管h还是a如果制造问题的速度比解决问题快直接干掉就行
- 我一直在用slock但没有和别人合作，没有mh
- 想让别人用的产品，里面一个术语都不能有
- 开源芯片 agent flow 张宇鑫:噱头居多,核心是训模型
- 里面
- 里面
- 自己用无所谓
- 我觉得如果我同事能把他agent借我，然后我把他踢了效果应该差不多
- 术语越多，完全图里缺失的连边就越多
- 7月28日15:53
- mhma是multi human multi agent吗
- Weiyang: mhma并不是一个h * a的问题
- 也挺好，我前几天也是这么干的
- 刘家昌：我现在强制要求它给多个option，每个
- option 有 concrete example，写清楚 pros and co...
- 但我感觉认知成本还是很高
- 最要命的是每次分析的因果有时候是反着来的，因为他从它的视角出发，一路自己决定读哪些文档和代码，最后告诉我结论
- 导致同一件事，开十个agent能得到十个大差不差，但又不是完全一致的答案
- 6黑暗深林
- 高渐远: 我觉得如果我同事能把他agent借我，然后我
- 把他踢了效果应该差不多
- 然后阅读的时候也很累
- 7月28日16:07
- 郑权: mhma是multi human multi agent吗
- 我在线下都和同事直接混用mac studio，不管办公还是服务器ssh也都通着
- 所以实体硬件显得像媒介，而实体硬件垃圾，网络基础垃圾显得他们在影响我和我的agent沟通
- 7月28日16:40
- xs我们现在交接工作的流程是，我方 AI写一个一键脚本，对方 AI读取这个一键脚本，完毕
- 高渐远:我觉得如果我同事能把他agent借我，然后我
- 把他踢了效果应该差不多
- 无痛交接
- 7月28日21:38
- 我的体验是MHMA还是很有价值的，尤其是做硬件开发这种极其消耗精力的事情的时候，OPC模式真的顶不住

---

## 记录后段｜原文件只保留了相对日期

### 星期三

#### 原文 L65335–L65352

[回到原文件 L65335](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:65335)

- 趁着AI在跑的时候开始重新刷起了leetcode
- 我其实还是有插件，一个subagent，另一个把除了bash之外的工具全部删掉
- 我现在苦于跑AI的时候没什么事情可以做，我已经在本地造了无数个小项目和小工具了
- 现在我觉得，跑AI的间隙去刷题倒是一个不错的活动。
- 看 paper
- 刘思皓:我现在苦于跑AI的时候没什么事情可以做，我
- 已经在本地造了无数个小项目和小工具了
- 可以读一些群友著作
- 比如https://zhuanlan.zhihu.com/p/2065737086871790189
- dbq我觉得我已经开始要拖模型后腿了，我觉得三个月内我的workflow将会变成「auth给你，愿望给你，你爱啥
- 干啥」（
- 刘思皓:yep，你得这么想，前沿模型之间的能力差距
- 应该是小于我能力的绝对值(的吧？所以只要我认真...
- 我修电脑已经这样了
- 刘家昌： dbq我觉得我已经开始要拖模型后腿了，我觉
- 得三个月内我的workflow 将会变成「auth 给你，愿...
- cloudflare sdk给他
- 过去三个且已经从AL直菜我还得给你设计架构，到了我只要看一眼架构纠正一下本质的沟通错误

---

#### 原文 L65545–L65558

[回到原文件 L65545](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:65545)

- 今天终于说好了revision14定稿了
- 虽然有了也不安全，但是没有就会有测试的测试的测试，还会有文档的文档的文档的grep测试的grep测试的
- precommit 测试
- 船坞r14模型v7其实v1-v6肉眼可见每次都有大进步
- Weiyang:今天终于说好了revision14定稿了
- v7要求太多卡主了
- (以及不要在prompt 任何地方提到 TDD，不然 Sol 就会如遇知音（
- 刘家昌： (以及不要在 prompt 任何地方提到 TDD，不
- 然 Sol 就会如遇知音（
- 我都UDD
- 刘家昌： (以及不要在 prompt 任何地方提到 TDD，不
- 然Sol 就会如遇知音（
- user driven test

---

### 星期四

#### 原文 L66085–L66187

[回到原文件 L66085](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:66085)

- 那是不是可以让ai基于当前任务，用类似反向 btw的方式出 quiz 给用户帮助掌握项目进度
- 刘思皓：现在我觉得，跑AI的间隙去刷题倒是一个不错
- 的活动。
- 重用啥的不存在，找代码不如手写几百行
- 明扬:其实完成某个功能不应该用超过10万行代码，
- 但 ai 真能干出来
- 感觉很好
- :那是不是可以让ai基于当前任务，用类似反向btw的
- 方式出 quiz 给用户帮助掌握项目进度
- 把之前那个 humanize gen plan 的 quiz 升级一下
- 很常见，opus也会。
- Reiko:这个让我想起一件搞笑的事情：应该是5.5来
- 着，差不多的提示词，他清完之后就会在文档里写“
- 星期四00:40
- 90
- 人没跟上
- 渐放缓了
- 56
- 看来他们内部也想了很多办法。
- 王邦彦: opus4.7/8 很严重。5 好一些了
- 这个之前群里深度讨论过了
- :那是不是可以让ai基于当前任务，用类似反向btw的
- 方式出 quiz 给用户帮助掌握项目进度
- 星期四 00:42
- 有一个专门的名字
- 叫作：层级抽样测试
- 对的以及你说不要写给xxx看他会把“不要写给xxx看这句话写进文档”
- Grill me 有做到吗
- 刘思皓：叫作：层级抽样测试
- 目的是：长程任务Agent需要时不时地主动以考试的形式和人类对齐
- 没有吧，目前大家都还是希望AI是一个许愿器
- 现在没有太大意义了
- 迫使人类主动思考是违背人性的
- 要么出特別简单的题目
- 我其实觉得这个依然在现在很有必要
- 刘思皓:目的是：长程任务Agent需要时不时地主动以
- 考试的形式和人类对齐
- 是违反人性但是符合项目需求
- 要么不说人话，你题都看不懂
- 也没那么违反人性
- 我觉得他如果出错不说人话更违反人性
- 我会发狂
- 窝窝that
- Weiyang:
- 最终的quiz成为一种安慰剂
- watch了—个glow，渲染gantt
- B4RRy: 窝窝that
- 草台班子启动
- 但是这个依然是quiz设计问题吧 ai有能力one shot/few shot/自我迭代几轮写出来人能看懂的文档就有能力设计出
- 合理的quiz才对
- 王邦彦:最终的quiz成为一种安慰剂
- "王邦彦" recalled a message
- "王邦彦" recalled a message
- 因为写出人能看懂的文档，是人在指导
- B4RRy: 但是这个依然是quiz设计问题吧 ai有能力one
- shot/few shot/自我迭代几轮写出来人能看懂的文档...
- 这就是违背人性的地方啊，AI一但写出你看不懂的东西，正确的做法应该是停下它，然后和它掰扯清楚
- 王邦彦:最终的quiz成为一种安慰剂
- 也不是我现在用skill也能写出来自己能读的东西
- 满足一些基本的要求人就能看懂了
- 我设置的是第k行的所有变量必须在1- (k-1)行被定义过
- 星期四00:49
- 以及每次维护一个术语表去思考这是不是这个领域大家一说都能听懂的common words 这些不用定义
- 你这边似乎在假设，quiz考的是某种计算机算法原理
- 刘思皓:这就是违背人性的地方啊，AI一但写出你看不
- 懂的东西，正确的做法应该是停下它，然后和它掰扯...
- 然后每一轮让一个无上下文的人agent去读文档只读文档不能看任何代码和别的把它看不懂的东西记录下来
- 就这几个规则迭代3轮左右就能给我我能看懂的文档
- 但实际上，现在AI出的plan，本身就是一大堆的黑话+不知道定义在哪里的名词/变量
- 王邦彦:但实际上，现在AI出的plan，本身就是一大堆
- 的黑话+不知道定义在哪里的名词/变量
- 只要把任务转换为一个清晰的规则+多轮的重复
- and我觉得plan本身是这样的没关系
- 只要给人看的一个版本经过处理就行了
- 然后你和他去掰扯，它又引入更多的名字/黑话
- 实际我是后置学习，现在就是一定会有认知债，这个债务的profitloss是可变的
- 刘用皓: 这就是违背人性的地方啊，A一但写出你看不
- 代价是真挺慢的 随便写一个html就一个多小时 gpt5.5high
- ai有能力审查出这个东西
- 刘思皓:这就是违背人性的地方啊，AI一但写出你看不
- 懂的东西，正确的做法应该是停下它，然后和它掰扯...
- 然后这个版本处理的时候是可以并行的
- B4RRy: 只要给人看的一个版本经过处理就行了
- 如果loss太高你真得掰扯
- 什么是profit loss呢
- Weiyang:实际我是后置学习，现在就是一定会有认知
- 债，这个债务的profitloss是可变的
- 自动驾驶撞死人loss就高
- B4RRy: 什么是profit loss呢
- 生图抽卡烂loss就低呗
- 赞同
- Weiyang:实际我是后置学习，现在就是一定会有认知
- 债，这个债务的profitloss是可变的
- 这个自评快速决策快速冲
- 那这个是很复杂的事情不光要考虑事情出问题的危害本身
- 先创死100次p0任务再说
- 也要考虑这件事情难度或者出错概率把（虽然我觉得这点目前很难做到)
- 我没办法知道ai做什么任务会错什么不会
- 总是有我感觉可能足够简单的任条依然犯错
- 我现在有个200人日活都企业saas服务，所以企业都是一个loop解决(经历若干次p0事故，删库之类的)
- 已经不能叫corner case了
- 我觉得最难受的是，对着plan学习，最终看半天，时间也花了，结果”学到的东西“其实是消水，还觉得不值得

---

#### 原文 L66224–L66242

[回到原文件 L66224](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:66224)

- 的黑话+不知道定义在哪里的名词/变量
- 我正在等agent说门禁
- 比如测试，领导会设置一堆指标，但服务的目的是更高质量的生产级服务
- B4RRy:然后每一轮让一个无上下文的人agent去读文
- 档只读文档不能看任何代码和别的把它看不懂的东西...
- 我觉得比较恼火的是有人用模型直出的东西糊弄我。。。
- 写个skill
- B4RRy:然后每一轮让一个无上下文的人agent去读文
- 档只读文档不能看任何代码和别的把它看不懂的东西...
- 如果把指标当kpi，指标并不意味着会提升生产服务质量
- ed Plan
- 完成 R20 e1928 GPU 精确回放并确认 R21 prior
- 实现并验证受治理的 R21 checkpoint policy ha
- 启动 R21 V7 真实训练并测得稳定吞吐/ETA
- 包完 V7 验收并发布到可视化工作台
- 星期四 00:58
- less control

---

#### 原文 L66534–L66554

[回到原文件 L66534](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:66534)

- 星期四 05:31
- https://github.com/LukeLIN-web/humanize/blob/main/skills/docs-jargon-pass/SKILL.md
- Luke: 写个skill
- 很搞笑的是，最符合群名的一集
- 这真的是humanize，要说人话
- 时间观念新惊吓来了，船坞造好了，跟我说8月27飞船试航。
- 资源感知 cpu gpu 端口 网络 磁盘
- 最后还有时间观念
- 星期四11:29
- 很久之后又尝试了一下multi agent，感觉会把claude变得造星舰船坞，七嘴八舌的，加了一堆要求，反复推翻，
- 但是在操控资源，共享gpu的时候确实很方便。
- 太多错误信息作为prompt引入污染上下文。
- Luke:很久之后又尝试了一下multi agent感觉会把
- 星期四11:56
- 怎么说，达成了错误的共识吗
- 星期四11:58
- 这个 sihao 很早就说过
- agents之间一定不能讨论
- A mme

---

#### 原文 L66558–L66612

[回到原文件 L66558](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:66558)

- 感觉主要靠agent互相通信啊
- 有前提条件吧
- 翁大爷的狗@Rakuten: agents之间一定不能讨论
- https://github.com/LukeLIN-web/humanize/blob/main/hooks/goal-monitor-spawn.sh
- 好像不太对，是reviewer开subagent打工的样子
- Luke: https://github.com/LukeLIN-web/humanize/
- blob/main/hooks/goal-monitor-spawn.sh
- 如果是将任务拆散为子模块，父子通信我觉得还是有必要的，当然也不是子agent之间互相交流
- opus5 完全不用subagent啊都自己搞
- 需要ultracode mode
- 今天才开始实现
- 指的是为了一个目标，多路线并行探索的agent，不要互相讨论
- Subagent本质上是一个对付上下文不足的办法
- 上次被老板点名后，我开启了节能模式
- 星期四12:04
- 通过一些信息传递的损失以及对agent之间的任务指派的信任来做
- 就算是无限的，也还是有污染的问题，脑子混乱
- B4RRy: Subagent本质上是一个对付上下文不足的办法
- 不过我相信很快大厂会解决上下文的问题
- Not in this way
- omp里配置了分级模型，fable5(fallback opus5)做plan、review，然后terra、luna做实现
- 然后我发现实现模型也不用太高智力，毕竟有高智力reviewer，所以允许实现模型蠢一点，走点弯路，但是快速省钱
- 这个群里说过了
- build 时要快，review 要准
- 星期四12:09
- 毕竟我成了瓶颈，模型智力高低的，除了多烧钱，已经无法为我提升生产力了
- 除非上下文矛盾了，塞一些无关的上下文也没感觉到过问题，memory不也是上下文么
- 星期四12:17
- sol ultra 太烧钱了，我这周跑几个探索任务，查了下 2700 个 subagent了。
- 不是并发的他生存周期跑完就结束了只是给你统计个数字
- Reiko: sol ultra 太烧钱了，我这周跑几个探索任务，
- 查了下 2700个subagent了。
- 星期四12:19
- 我并发开32，准备考虑进一步降低了
- 我6天烧了18k usd，被老板点名
- Reiko: sol ultra 太烧钱了，我这周跑几个探索任务，
- 查了下 2700个 subagent了。
- 相当于动态的看有什么低耦合任务就做了
- 32可能合并不聊了我现在16
- 之前是40
- 16暂无不适
- Reiko:我并发开32，准备考虑进一步降低了
- 如果你是20x
- 而且净给我造歼星舰，造出来的东西我无法理解，以至于有点后悔开/goal跑了两周
- 让他给ETA
- 明扬:而且净给我造歼星舰，造出来的东西我无法理
- 解，以至于有点后悔开/goal跑了两周
- 开了两个探索任务，周额度已经到18%了
- Weiyang: 今天用量也耐用了
- ETA + pin个看板
- 你只做lean4还是什么
- Reiko:开了两个探索任务，周额度已经到18%了
- 数学物理，没用lean4，太重了
- Weiyang: 你只做lean4还是什么

---

#### 原文 L66698–L66710

[回到原文件 L66698](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:66698)

- 但poc层面养蛊效果还可以
- 成本很高，睡觉前开一个多方案并行优化目标，每个agent都去做极限优化。
- subagent们结束了以后再由主agent炼化
- 星期四14:40
- 后来发现多Agent有时候会做重复的尝试，或者钻牛角尖，最终融合效果也一言难尽，多烧了好几倍的token，出来
- 的效果没有比一个agent把所有路线都尝试一遍更好
- 主要是subagent也不敢打破边界，而且这些边界是他自己以为的边界，不是我给他的边界指标
- 我让他把python实现翻译成rust，并行多agent分别尝试rust的blas库，性能，simd吞吐量等，结果agent会严格对
- 齐python输出，1e-14的浮点数误差也会毙掉10x加速的方案
- 这个故事前两天讲过了
- 明扬:我让他把python实现翻译成rust，并行多agent
- 分别尝试rust的blas库，性能，simd吞吐量等，结果...
- 星期四15:25

---

### 星期五

#### 原文 L67001–L67021

[回到原文件 L67001](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:67001)

- 说不上来哪里不对
- 它delegate mode做的不是很彻底
- 星期五 04:46
- 我从前天开始了—个实验，就是任何任务在那gpt-5.6 sol max做review的同时，也拿kimi k3 max[1m]做影子review
- 还没有出现kimi k3发现gpt没有发现的bug
- 但是kimi的速度得慢gpt5-10倍的样子
- 星期五 04:47
- 我感觉kimi的review学的是claude的那个路子：上workflow +并发多个子代理审查
- GPT review的质量还是太高了
- 然后另外和opus 5对比了一下，opus 5带着tdd一波做完一个大概2000行的任务，gpt一查，4个P1，3个P2
- 然后丢给claude opus 5， claude 全认
- 很难想像没有gpt review的日子
- 这个review token efficiency质量实在是太高了。
- 也没开subagent，也没用什么flow。
- 星期五04:58
- 是啊，错误太多了。真的是改变性质变
- 刘思皓: 很难想像没有gpt review的日子
- 星期五05:31
- 我一直觉得 kimi review 挺可以的，但是的确不如 gpt(但是也不 propose 造星舰，一体两面？
- 也确实太慢了233
- Claude的隐藏思维链真的太恶心了，而且我怀疑中间输出也被隐藏了

---

#### 原文 L67047–L67072

[回到原文件 L67047](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:67047)

- Im越强，感觉越不需要过度的操作
- 估计harness的粘性还是很大的
- 刘思皓: gpt只要能够keep its review crown
- 刘思皓: 直接裸pi
- 我真诚地觉得 bash only 除了让用户有点委屈之外，远高于任何 tool call
- 星期五06:21
- 除了 bash 没有任何一个 tool 能让 k3 在一个 turn 里用 python 十分简洁准确地修改一个大文件，跑 test，test 完
- 成之后立刻 git commit 然后 sed 找下一个目标
- 但凡有禁止 bash 读写文件，要用 tool 的 prompt(which pi 自带了需要把它删掉)，就不会看到那么惊艳的操作
- 变成若干个可能会失败的 turn
- then both k3 and human are annoyed and distracted
- 增大反馈步长的意思吗？是不是仅适用于k3这种高智力模型？
- 星期五06:27
- 现在大部分的 harness都是什么，sed 分析一个 turn，agent 好耶我找到了write 一个 turn harness 说你没读，然
- 后委屈地 dummy read 一个 turn，write 再一个 turn，harness 说你有一个空格没有 exactly match 或者什么有两
- 处 match，修正完再一个 write，跑 bash 测试和 commit(此时 agent 已经养成各一个 turn 的习惯了一般会变
- 俩)，然后继续 sed
- 好好的一个 turn 拆了八个，attention 全在 exact reproduce 和 tool following
- 诚实的答案是(误)我只试了对 Kimi 这么做并且非常感动，没有试过别人(我一般用官方harness除了这次 Kimi实验)
- Reiko: 增大反馈步长的意思吗？是不是仅适用于 k3 这
- 种高智力模型?
- 思考链里「actually let me think if I should use the Write tool or Edit tool... should be Write because I am
- replacing the whole file. Actually let me think again if Bash is a better tool. No, user has explicitly asked not
- to use Bash for file operations.」之类的傻逼玩意再也没有出现过
- 星期五06:33

---

#### 原文 L67167–L67179

[回到原文件 L67167](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:67167)

- Shom: 推理就是真要卡数了
- 怎么能干掉开源模型。
- NV 周耀阳: 是为了干开源模型
- 开源模型并非没有成本啊
- 它只要成本性能曲线帕累托前沿比开源模型好就行了
- 不过开源模型活得好好的，才符合 NVDA 利益
- 确实
- 星期五 08:55
- 干不掉，因为没那么穷
- Luke: 怎么能干掉开源模型。
- 想开就开了

---

#### 原文 L67225–L67234

[回到原文件 L67225](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:67225)

- 刘思皓:试试k3?
- 可以让luna给提示词
- 星期五 09:42
- 主要我这个不是网站，没源码。是gptimage设计的游戏ui
- 为什么是让luna给提示词
- Weiyang: 可以让luna给提示词
- 因为luna terra sol比较过
- SunnyCase: 为什么是让luna给提示词
- 值得一试
- 感觉这个已经很好了，给你加一大堆自创词就老实了

---

#### 原文 L67656–L67693

[回到原文件 L67656](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:67656)

- 那看来你的任务还是太难了（
- codex tui subagent 开多了(比如 500 次)会卡吗?
- 500
- 会的兄弟
- codex desktop 想要炸了我的 mac
- 上限200吧
- Reiko: codex tui subagent 开多了(比如500次)会
- 卡吗?
- 并行 32，历史 500 次
- 星期五23:17
- 5.6 刚出来的时候还不卡着
- 那一般，不过并行32是咋算的，新版subagent没有硬顶
- 有的，v2已经是稳定版了
- 卡吗?
- 他软件有bug
- 5.6刚出时候大伙儿的电脑都炸了
- 32个subagent每秒new12个死12个，电脑就卡爆了
- 我之前测试是软顶
- 现在是硬的，而且能指定模型和 reasoning effort
- 开源芯片 agent flow 张宇鑫: 我之前测试是软顶
- 星期五 23:26
- codex desktop 的 subagent 界面巨卡，数量达到几百之后。感觉是啥玩意加载的问题
- ……
- 梁大哥下个月能把 ds4pro 正式版端上来吗
- 郑权:
- 肯定的
- Reiko:梁大哥下个月能把 ds4pro 正式版端上来吗
- 星期五 23:37
- 我实验了下grok build
- Reiko: codex desktop 的 subagent 界面巨卡，数量
- 达到几百之后。感觉是啥玩意加载的问题
- 感觉rust重写么有说法
- 达到几百之后。感觉是啥玩意加载的问题
- 感觉rust重写么有说法
- codex多subagent不如多codez软件管理有问题

---

### 星期六

#### 原文 L67724–L67754

[回到原文件 L67724](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:67724)

- Opus 5 观测到这个问题很多次了
- 大爷说，有很多可能，比如约束解码要求模型一定要吐一个 tool call但是模型不知道干啥，跑个 true
- 刘家昌: 草这是持续互相蒸馏吗
- 星期六 02:25
- 我觉着很有道理
- 星期六 02:45
- /goal的过程中/btw了一句回头就这样了
- 是跟subagent交互的时候 tool被错误路由了
- 而且很神奇的是开新session读jsonl这个问题会传染
- 后来没办法只能让它换成codex exec起subagent
- 确实
- 我也是控制 subagent 遇到的
- 感觉更像是个bug
- codex 这个 sub agent 害得多练
- 星期六 02:52
- ？subagent现在不是不可以交互了吗
- 我让他把sub关了
- 刚遇到傻逼问题主线程退了之后sub还在干
- 我切cc之后cc告诉我有人在改文件
- 经典
- 我这失联 subagent 大概的触发概率是百分之几
- 我很少开ultra，我感觉并不是很适合我的工况
- 星期六 03:02
- 感觉
- harness + gpt 5.5
- "B4RRy" recalled a message
- 比直接干用max更干净啊
- 就是不太会给你造星舰
- max 是一步一回头，ultra 是走一步开—堆 subagent 指指点点，反思怪
- B4RRy: 比直接干用max更干净啊
- 回头是什么意思呢

---

#### 原文 L67765–L67774

[回到原文件 L67765](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:67765)

- 我就能接受
- review subagent提一些鸡毛蒜皮的问题，然后开修，修完循环
- 这个 pattern 挺明显的
- 那有点恶心
- 可以选review agent把
- 我现在让他开的agent都开5.5
- 然后检查代码是否有逻辑性错误的时候用sol
- 就比如让 ultra 重写个文档这种简单任务，它会默认开几个subagent从不同角度评估，还会打分
- 杀鸡牛刀了
- ic

---

#### 原文 L67880–L67897

[回到原文件 L67880](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:67880)

- tmux，互相看。
- 本质原因应该还是没有合适的multiple shots/long run benchmark
- 刘思皓:主要是这个问题不影响跑分
- 非常邪恶
- 是不是有群友在搞来着
- 以及没有考虑这种中途输入的情况可能
- 星期六 09:31
- 没有中途steer benchmark
- 这不用benchmark
- 纯影响开发体验
- 我的笨办法很简单，如果你一开始打进去一个promptA，然后后面需要插一个steerB的话，就写：
- steerB
- 以上是提醒，主线不变
- promptA
- XS
- ai 发展这么猛，还是需要人 prompt 解决各种 corner case 微调
- 我也试试看这样
- 星期六11:34

---

#### 原文 L67975–L67993

[回到原文件 L67975](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:67975)

- 我们场景应该不太一样。
- 我这个是重推理的，file基本相当于外挂的记忆系统。
- 这导致 subagent 自身的 context 价值更高
- subagent的context也可以继承啊
- 强制暂停让 main agent 自己找回 subagent 吗?
- 你是指codex resume，or一个接管任务的损失导致任务偏移风险么
- 自己起agent，告诉他不强杀，结束不继续
- Reiko:安全暂停所需的时间和成本好像已经不低了?
- 所以启停是有一个当前goal结束或者block的延迟
- 等待worker自然结束，补齐上限是新的目标而非立刻执行，master session只负责跟踪该目标
- fde招工负责ai
- 星期六18:39
- 大概就是一个theory-building task(实际上我已经不知道它具体在怎么做了)，就像人类团体一样，一些
- subagent负责探索，一些负责独立检验，等等。
- 这意味着finding/theorem 会有一个自己的生命周期。
- main agent 自称的 batch 估计就是这么来的。
- 开源芯片 agent flow 张宝鑫: 你昌指codex resume
- or一个接管任务的损失导致任务偏移风险么
- 我让它暂停是按照这个「findinglifecycle」来控制的，延迟就非常高

---

### 星期日

#### 原文 L68074–L68183

[回到原文件 L68074](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68074)

- 都是看一个思想，然后就自行炼化了
- 我是RSI吹子,最近参与了企业ai harness讨论,还在开源版->后续开源阶段性计划中，
- 企业级Infra还有许多需要治理的地方
- 发现claude opus 5一波写workflow居然能写出语法错误
- 星期日00:32
- 我感觉我对 workflow 最近几个月有点古法了，运维太多限制了我的 scale
- 调用内置脚本不熟练,95%准确重复故障率么
- 刘思皓: 发现claude opus 5一波写workflow居然能写
- 出语法错误
- 这种问题通过训练下一代模型的轨迹来磨合适配看看,infra太超前了吗
- 确实，但是codex的ultra的思路并非claude dynamic workflow
- callback—下我之前的判断
- 刘思皓:我觉得未来6周到10周会对以下两
- 种agentic workflow方向作出选择:1.
- agentic mutable dynamic workflows --
- 一个随着时间前进并且agents可改动的...
- 聊天记录
- codex ultra显然选择了动态主义，它并没有一个固化的ts去规定flow的进展
- claude code偏向组合主义，它的结构是外层一个串行stage结构带循环，内部每个stage可以多个agent并发。
- 需要 pin 起来
- 这话我是2个月前说的(感觉已经过了半年)
- 刘用皓：[聊天记录]群聊的聊天记录
- 我觉得好像其实都挺对的，如果现在看的话
- 应该要设计一个合适的机制,有一批人是ai native负责ai探索,产出一堆半成品,一群人复古人工,校验半成品
- 刘思皓:我感觉现在大家基本不会用别人已经造好的东
- 西吧?
- 富士康流水线的工控7S管理体系来管理超量的代码产出
- 我觉得codex的方案挺好的
- 星期日 00:42
- 而且codex的agent通信已经有雏形了
- 不知道claude有没有
- 我觉得claude code和codex的技术路线选择就体现了两个公司的品味区别
- claude code的脚手架上的很多，所以才引入了dynamic workflow的机制，通过一套瞬发完成的ts代码规定智能体的
- 行为。这个设计和humanize v1很像
- 好处是，agent基本不合跑偏，坏处是，触发flow的时刻并不合意识到后续开发合课到什么问题
- 而codex走了完全一套不同的路线，它完全相信agents自己的能力
- 所以开ultra的时候，你会看到它基本是一个online的管理flow的模式。
- 用codex怎么将bun迁移到rust
- 动态管理flow对人来说不太友好，看不出agent在干什么
- “将bun迁移到rust”这个任务本身是有偏的
- “将bun迁移到rust”这个任务过分机械
- 以至于你如果有一个机械式的模板flow，是有效的
- 你写代码调codex也不是不行
- 星期日00:48
- 我觉得现在的判断应该是：
- - 大规模机械式的维护任务，一个机械代码式的flow是有效的。-- 组合主义
- -一个需要频繁交互、介入的探索性质的动态任务，那不上枷锁，相信agent是有效的。--动态主义
- 星期日 00:56
- 合理
- 刘思皓: 我觉得现在的判断应该是：- 大规模机械式的
- 维护任务，一个机械代码式的flow是有效的。--组合..
- 抛开具体任务谈哪个方法更好是无效的，关键还是在人。
- claude code dynamic workflows的问题在于：你并不能在一开始就考虑清楚所有情况，问题总是随着开发的进展逐
- 渐涌现的，在一开始就用一个写死的flow去尝试覆盖整个迭代开发流程显然是错误的。
- codex ultra的问题在于：它的ultra会在两个状态下切换1.主agent大包大揽；2.子agent无限递归派发子代理。它
- 总是在任务进展的当下去考虑如何派发子代理，而没有一个统领全局的flow去约束。以至于经常需要人介入去处理两
- 个问题：1. 主agent并没有派发子代理，导致实际效果不如sol max；2.子代理被过度派发，以至于没有合理规划递
- 归深度
- 至于怎么良好的解决这个问题，在动态主义和组合主义之间找到一个平衡，以至于可以自动化地做这件事情，我暂时
- 还不知道。目前我还是交互式地在两种模式之间切换。
- 还是在人。claude code dynamic workflows的问..
- 可以吧，下次让 sol来设计，opus5就是干，
- Amadeus: 我感觉5.6-sol做科研很牛逼啊非常严谨
- 第二点应该会随着模型能力提升而改善，5.6这版看起来就像个初版
- 刘思皓:抛开具体任务谈哪个方法更好是无效的，关键
- 还是在人。claude code dynamic workflows的问...
- 我同意，这也是openai哲学的选择：相信模型的能力，而不是增强harness
- 我个人是比较喜欢openai的这个选择的
- 我也是
- 星期日01:04
- 考验多agent后训练
- 刘思皓：抛开具体任务谈哪个方法更好是无效的，关键
- 还是在人。claude code dynamic workflows的问...
- 星期日01:21
- 帕拉丁是啥
- 武汉心片科技刘玖阳：现在我们做体系结构有一堆想法
- 实践起来其实比的就是谁的帕拉丁多罢了。再怎...
- 刘思皓:我同意，这也是openai哲学的选择：相信模型
- 的能力，而不是增强harness
- 谷歌好像还不太一样
- 相信pre train
- 星期日01:21
- 模型自己本身足够聪明自然能对付这些各种任务
- 更少的依赖RL
- 星期日01:38
- 家人们跑 terminal bench 推荐用什么 harness 呀
- 啥模型啊
- K3吗
- tb不是原生提供了harness吗
- 我只是想看参数之间的区别所以随便了，，，
- 只要一样就行
- 如果你要验证实现的话有点麻烦
- 星期日01:47
- flash official
- 原本用的是 deepseek harness...
- 这还不简单
- @崔添翼 DeepSeek Harness
- "翁大爷的狗@Rakuten" recalled a message
- 让崔圣拉你内测群

---

#### 原文 L68200–L68225

[回到原文件 L68200](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68200)

- 梁圣化身梁神
- harness咋会震撼
- 感觉都大差不差
- 步坦协同
- 在KDA横扫千军以前我也觉得都大差不差
- harness的给我最大震撼还是去年年底第一次跑完humanizeloop的时候
- 特化的能做出差异能理解
- 星期日01:56
- 后面感觉harness没有很多让我很震撼的工作了
- /goal
- 是我最近学会的
- 感觉够了
- 哦对我觉得/goal得算一个
- 但是codex的/goal和claude的/goal差很多
- 我觉得codex的goal好多了。。
- 我说的就是codex的goal好很多的意思...中文博大精深，好很多和差(一声)很多是一个意思
- 我也没有反驳你的意思，我正确理解了原句（
- 用 cc 的 goal 感觉这个功能的存在感不强
- ccgoal实现我记得在同一个上下文所以效果很差
- 确实
- 翁大爷的狗@Rakuten: 用 cc的 goal 感觉这个功能的
- 存在感不强
- 星期日02:02

---

#### 原文 L68325–L68334

[回到原文件 L68325](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68325)

- pandashere: 连你都没抽到
- 我想要 deepseek harness 哪里抽
- 每日一省吾身：为什么别人的agent已经解决了菲奖问题我的agent还在捏泥巴都捏不明白
- 你直接在这个群里质问崔佬
- 刘思皓: 没抽到呀
- 有道理，加入到pua skill中鞭策agent
- 陈泽恺:每日一省吾身：为什么别人的agent已经解决
- 了菲奖问题我的agent还在捏泥巴都捏不明白
- 星期日11:15
- 俺也不知道俺也不敢问

---

#### 原文 L68498–L68533

[回到原文件 L68498](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68498)

- 星期日18:03
- pi-agent是真的省token啊，而且好快
- 感觉其他的harness都有点太重了
- pi-agent叠上我的DSpark开满的v4flash，做一点小任务简直光速
- 搞点我portfolio的token吧
- anthropic 最近估计都卖不动了
- pi agent 你们都咋开subagent，是自己弄一个还是用它市场的插件？
- 星期日18:07
- 历史记录所
- 原沙雕群第六十六群群主
- 这相人猫架构星个外秤
- 让pi自己调用自己的CLI
- Reiko: pi agent 你们都咋开subagent，是自己弄一个
- 还是用它市场的插件？
- 徐老师更新到flash-0731了吗
- 香港科技大学 研究助理教授 徐策羽: pi-agent叠上我
- 的DSpark开满的v4flash，做一点小任务简直光速
- ic，这个适用于一层 subagent 的场景是吗
- 香港科技大学研究助理教授 徐策羽: 让pi自己调用自己
- 的CLI😄
- 星期日18:12
- 有用上 oh-my-pi 吗，还是就是原始的 pi
- 香港科技大学 研究助理教授 徐策羽: pi-agent是真的
- 省token啊，而且好快
- 星期日18:40
- 有了，直接用就是
- 郑权:徐老师更新到flash-0731了吗
- 星期日18:54
- 我设计的agent flow language的中间表示
- 陈仁泽-pku:有用上 oh-my-pi 吗，还是就是原始的 pi
- 咋样，感觉会是一个热点，只需要十几行代码就可以实现一个完整的agent workflow
- 为啥不用python或者ts
- 阻止我并发的终于走到了带宽
- 有python前端
- 这个是ir

---

#### 原文 L68538–L68552

[回到原文件 L68538](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68538)

- 加钱买两个codex
- Weivang:阻止我并发的终于走到了带宽
- 下周可以看交换机了么
- cc上半年封了1140w 个号
- 星期日 20:06
- 刚才 Chrome 中的 Overleaf 突然显示被 Codex 控制。经查日志，触发源是
- Codex的 Ambient Suggestions(后台智能建议）。该功能会启动不显示在普
- 通任务列表中的临时后台任务，并读取 connected apps 中的上下文。
- 后台任务读取了 Chrome 标签页，并认领 Overleaf 页面进行 DOM 快照，因此
- 出现浏览器控制提示。审计未发现点击、输入或编辑行为，只读取了页面内容；
- 相关任务随后正常结束，目前无残留进程。
- 问题核心是：后台临时任务可以调用Chrome，但不会显示为普通active
- Codex session，造成状态展示不透明。
- 和闹鬼了一样，突然操纵chrome
- Reiko:

---

#### 原文 L68582–L68592

[回到原文件 L68582](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68582)

- 星期日 22:12
- 徐老师，万一是 ds harness 巨牛呢
- 香港科技大学研究助理教授徐策羽:我感觉v4 flash有
- benchmark刷分嫌疑
- 我感觉这个时代还是底大一级压死人，感觉v4flash有一种后训练做的很好，但是预训练不足的feeling
- 底大一级压死人+1
- long horizton agents 很多地方到后面比的就是 world knowledge
- 你有这个 knowledge就能做，没有这个 knowledge就不行
- 各种instruct following和harness相关的interaction，其实v4flash都做的很好。
- 但是基础知识方面极其薄弱
- 这个很快，但是好像不支持reasoning

---

### 昨天

#### 原文 L68605–L68617

[回到原文件 L68605](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68605)

- 昨天00:38
- https://github.com/tastynoob/Agent-Flow-Language
- 欢迎大家前来试用
- afl能够使用一种ir的表达形式来描述复杂的agent workflow，不过目前skill，mcp，安全，rag等功能的支持还比较
- 有限，可以先来做做简单的workflow试试
- 昨天01:07
- 可以，mark了
- Lurker: https://github.com/tastynoob/Agent-
- Flow-Language
- 昨天05:58
- 比如humanizev1就能这样描述
- 昨天00:54
- 借贵群宝地问问有没有同学去ECCV开会，想多认识几个朋友！

---

#### 原文 L68637–L68659

[回到原文件 L68637](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68637)

- 这个行为我还是第一次看见
- 咋了
- 代码全写完之后，然后有看了几十个文件
- 说我有一个更简洁凝练的解法
- 然后开始重写
- 又*
- HandshaketandidatoTransaction::closelHandshakeCandid
- SpatialRouteCostState.cps
- 刘思皓：代码全写完之后，然后有看了几十个文件
- 啥模型
- GPT真牛逼
- gpt-5.6-sol max
- 这么强
- 合理我觉得，openai之前不是说，周五是专门用来清理code slop的日子
- claude opus绝对不会干这种事情，opus如果tdd开发，全部实现之后，测试如果全过了，肯定开开心心来找我汇报
- 全过了（还会带感叹号的那种）。
- 完美!
- 昨天12:06
- gpt5.6黑话也更少
- 写的文档人味更足了
- gpt干IC现在是最舒服的正确性也高

---

#### 原文 L68673–L68684

[回到原文件 L68673](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68673)

- 昨天12:51
- 这是啥，agent 版的宝塔？
- 哦哦，用过这个
- 但想不起来用
- 我每次都是让 omp 去远端服务器启动omp 任务交代过去然后定时给我汇报进度
- 昨天14:53
- 欢迎各位工头关注赛博土木工程
- MiniMax H3 官宣开源，SGLang
- Diffusion Day0 支持
- MiniMax 开源视频旗舰 H3，
- SGLang Diffusion Day0 支
- 持：效果对标 Seedance 2.0...

---

#### 原文 L68773–L68819

[回到原文件 L68773](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68773)

- 昨天23:50
- Sol铲屎是真的强，我跑了一晚上他自己帮我铲了一万多行
- 星舰技术在铲屎这件事上实在是太合适了
- ：「不我觉得这里铲的不够多」
- 笑死了而且写一大堆没啥用的测试...
- 刘思皓: claude opus绝对不会干这种事情，opus如果
- tdd开发，全部实现之后，测试如果全过了，肯定开...
- 01:31
- 刘家昌: Sol 铲屎是真的强，我跑了一晚上他自己帮我
- 铲了一万多行
- 真不敢相信
- 说明oai已经做得非常成熟了
- 不然这种操作一旦失误率高一点要被喷死
- 10:33
- 有入的证和用制音
- 你说的对，少想是多
- 做使得快以期整理的大量的水非完全载
- 也就是四个月
- 四个月前我还觉得没有任何模型能做到“正确的”删除代码
- 现在已经能做到了
- 看来我的模型认知还需要提升
- 确实快
- 能做到删代码说明它已经掌握了奥卡姆凝练技术
- 01:37
- 我怀疑实现了某种recursive compression的技术
- 是的 claude 非常恐惧删除
- B4RRy:不然这种操作一旦失误率高一点要被喷死
- 不过如果sol只在自己写的代码里面删除，可能还好，不改动之前的
- 只改 diff
- 不够我不确定是不是我的个人agents.md导致的
- 我明确要求奥卡姆和ssot
- 01:45
- 铲了快两万了，非常感动
- Kimi 铲屎还是不太行，但是 Kimi build，Sol review + 铲屎很行
- 我现在每涨三万行 code 就让 Sol 去至少铲掉两万
- 维护性大增
- kimi主要是慢
- 没有 token factory 搞快的吗
- 群友那个就超快
- 说明不是模型本身限制，是算力限制
- 01:51
- 我现在每涨三万行 code 就让 Sol 去至少铲掉两万

---

#### 原文 L68910–L68923

[回到原文件 L68910](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68910)

- 我给task completed加个hook 让他调用simplify
- 刘思皓:我明确要求奥卡姆和ssot
- 07:43
- 曾经这真的是世界级难题
- 杨佳豪上海般鹏人工智能:可以，但是WSL不太好连
- vpn。。
- 08:21
- 确实
- humanize最早版本就是这样的类似做法，但是per task粒度太细了
- Luke: 我给task completed加个hook 让他调用
- simplify
- 我现在是/goal 1. xxx 2. xxx ... Finally, repeatedly call /simplify and /verify until converge to minimal complete
- implement

---

#### 原文 L68947–L68975

[回到原文件 L68947](/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md:68947)

- 把我整笑了，我就问了一下Kimi K3，(GPT写的)代码是不是合理且标准的。结果它说：
- 临时拼配置字。Loom这套—Q64定点
- 癖的纪律，不是学术标准。"标准"这个词
- Kimi K3: 你管这叫标准？那我是什么
- “标准”并不准确
- 12:15
- 说到标准
- 我刚想到ai写代码的时候有个缺点就是不太尊重“标准”化
- 标准化在工程上有降本的作用
- 比如我的某个工程构建任务，ai去执行的时候发现某个依赖库的实现阻碍了它完成我设定的目标，它就会想出各种奇
- 技淫巧去hack这一通用依赖库
- 但这在工程上通常会带来更高的量产成本
- 确实，我通常会把要标准化的部分生成tool让模型使用
- 如果是纯文本产出就会乱写
- 我说的就是 gpt
- 就像生产某些产品，ai发现定制硬件模具可以达成我设定的目标后，会把所有的零件全部定制化，导致所有件都是非
- 标的，生产成本上天
- 12:20
- 要想不乱写就不能写作文
- 让模型使用
- 而要搞成填空题
- 你在表格上校验还是太快了
- ai会fork原仓库，修改其中实现，来达成我设定的目标。
- 一般我走到此种境地时都会想办法改变自己的目标来适应标准的形状，比如一步处理较为困难，我拆成两步业务上也
- 能接受，且不需要fork原仓库自己定制
- 是的就是搞填空
- 去年这个时候旗舰模型产出个json都费劲
- 我还发现我给了ai这个约束：“尽量在不fork依赖库实现的前提下达成我的目标”以后
- AI倒是不fork了，ai开始hack，甚至想到了改os内核来绕过某些限制。

---
