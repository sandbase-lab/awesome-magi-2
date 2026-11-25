# MAGI-2 提示词写法：如何为视频提示 MAGI-2

[English](../prompt-guide.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

MAGI-2 是 Sand.ai 的视频模型，2026 年 11 月 24 日发布。下面的写法来自作者随本合集帖子公开的提示词。每条都引用作者原文并链接到原帖。合集还处于发布初期，所以目前是七条写法，会随着公开的提示词增多而扩充。

## 1. 第一句就说清格式和风格

在第一句点明格式和画风，再写主体。[@AIwithkhan][akhan] 开头写的是 "Create a heartwarming, hilarious, ultra-realistic Japanese-style 3D animated family comedy"（一部温馨、搞笑、超写实的日式 3D 动画家庭喜剧），然后才描述小女孩和早餐场景。[@criscxuan][cris] 在帖子第一句把作品定义为新潮日系 2D 赛璐璐音乐 MV 动画。

## 2. 逐项描述角色的外观

[@AIwithSynthia][synthia] 用一句话列出了人物："a miniature hand-drawn 2D young woman with long black hair, a pink hoodie, denim shorts, white sneakers, and a tiny red delivery backpack"（一个手绘 2D 风格的微缩年轻女性，长黑发，粉色连帽衫，牛仔短裤，白色运动鞋，背着一个红色小外卖背包）。每一项都是你能在每一帧里检查的东西。

## 3. 风格混用时，逐层写明

同一条帖子里，手绘人物走在写实城市中："exploring a gigantic photorealistic New York street"（探索一条巨大的写实纽约街道）（[@AIwithSynthia][synthia]）。把每一层的风格分别写明，模型就知道哪部分是画出来的，哪部分是真实的。

## 4. 把镜头规则写成硬约束

这个合集里最具体的提示词，写的是规则而不只是场景。[@abulu8][abulu-fpv] 写道："One single CONTINUOUS FPV drone shot, no cuts, one unbroken take... Only ever moves forward in time — never loops or reverses."（一个连续的 FPV 无人机长镜头，不切镜，一镜到底……时间只向前，从不循环或倒放。）同一作者的第二条帖子重复了这条规则，并写明唯一的例外及其时间点："NO slow motion except one half-second beat at the reveal"（除了揭示时刻的半秒慢动作，不用慢动作）（[@abulu8][abulu-chase]）。先写不能发生什么，再写唯一允许的例外和它出现的时刻。

## 5. 把动作绑定到节拍或时间

[@criscxuan][cris] 把片段设为 8 秒、120 BPM，安排了七次机位切换，并让镜头切换、人物动作和画面文字都落在节拍上。作者称节拍、转场和人物连贯性都做到了，这是作者的说法，不是我们的测试。给出节奏和次数，再按顺序列出事件。

## 6. 广告写成定时分镜表

[@joshesye][joshesye] 描述了一条 15 秒的服装广告，全程生成，每 1.5 秒换一套穿搭，并配有快推、慢拉和特写。开场是文字 "ONE HIT" 从模特身后放大，最后定格在品牌标识上。完整提示词在作者的回复里，所以这条帖子给出的是结构，而不是提示词原文。把节拍按时间编号，并标出每一段对应的镜头运动。

## 7. 正式生成前先测真人

写实的人体皮肤是这个合集里已知的薄弱点。在一次图生视频测试中，[@johnAGI168][john-i2v] 写道，真人的皮肤质感仍然怪怪的，不够自然。如果画面里的人物很重要，正式生成前先跑一次短片，检查皮肤和面部。

## 参数设置

- **时长。** 标价随时长变化：每秒 0.08，默认 5 秒（来自 SandBase inspect）。按你需要的长度提需求。
- **输出预算。** 本列表的 API 示例使用 `max_tokens: 128000`。SandBase 的模型数据未列出该模型的上限，提高前请先查看[模型页][model]。

## 可以直接用的提示词

```text
[一句话写明格式和风格]：[主体]，[外观和材质]。
镜头：[一镜到底，或切镜的位置]，[时长] 秒。
运动：[什么在动，按顺序写明，附时间点或每分钟节拍数]。
规则：[不能发生什么，以及唯一允许的例外和它的时间点]。
混合风格：[哪些部分是画出来的，哪些是写实的]。
```

填好以后，可以到 [Lab 文本竞技场][arena] 试一试，或按[教程](tutorial.md)用 API 调用。

---

引文均为短摘录并注明作者，完整帖子请点链接。中文、日文原文的翻译为我们所做。

[akhan]: https://x.com/AIwithkhan/status/2125522773258952776
[abulu-fpv]: https://x.com/abulu8/status/2125373412910747712
[abulu-chase]: https://x.com/abulu8/status/2125537498659225849
[synthia]: https://x.com/AIwithSynthia/status/2125574502285529485
[cris]: https://x.com/criscxuan/status/2125504100670530040
[joshesye]: https://x.com/joshesye/status/2125557298135245012
[john-i2v]: https://x.com/johnAGI168/status/2125578530272821680
[arena]: https://www.sandbase.ai/arena/text?models=sandai%2Fmagi-2%2Ftext-to-video&utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[model]: https://www.sandbase.ai/model/sandai/magi-2/text-to-video?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
