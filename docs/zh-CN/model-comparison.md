# MAGI-2 模型对比

[English](../model-comparison.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

两类证据，分开呈现：

1. **我们测到的。** Lab 对 MAGI-2 的实测，附日期。
2. **创作者报告的。** 发在 X 上的帖子，附他们自己的提示词和说法。有参考价值，但我们没有验证。

MAGI-2 于 2026 年 11 月 24 日发布。本列表目前没有记录它的实测结果，所以第一部分是空的。第二部分来自本合集的创作者帖子，大多是发布周内发出的。

## 我们测到的

**本列表目前没有记录 MAGI-2 的实测结果。** 本页链接的 Lab Evals 榜单对比的是语言模型，Pelican Test 要求画一幅 SVG 图。两者都不直接衡量视频输出，因此都还无法给 MAGI-2 定位。本列表也没有可以放在旁边的视频模型实测对照结果。

等 Lab 对 MAGI-2 有了实测记录，这一节会新增一行带日期的数据，下面的说法也会通过常规 PR 重新检查。

## 创作者报告的

来自本合集的创作者帖子。数字和结论都按创作者自述：都是一次性测试，设置各异，没有统一方法。点进链接可以阅读完整帖子。

| 创作者 | 帖子 | 他们怎么说 | 对手 | 公布的花费 |
|---|---|---|---|---|
| [@johnAGI168][john-cmp] | 文生视频测试 | 1080p 比 Seedance 2.5 便宜很多，与 Seedance 2.5 的 480p 相差不大 | Seedance 2.5 | 无数字 |
| [@johnAGI168][john-i2v] | 图生视频测试 | 真人皮肤质感仍然怪怪的，不太自然 | — | — |
| [@criscxuan][cris] | 8 秒音乐视频，120 BPM，七次机位切换 | 画质、卡点、转场、人物连贯性和动静结合"都很完美" | — | 无数字 |
| [@joshesye][joshesye] | 15 秒服装广告，全程生成 | 适合服装上新和产品宣发 | — | 无数字 |
| [@BubbleBrain][bubble] | 发布祝贺 | 称 MAGI-2 是"非常令人印象深刻的视频模型" | — | — |
| [@Kiber_Alla][kiber] | 发布周测试 | 继续测试，未给出结论 | — | — |

本合集其余帖子展示的是成品，没有对比：[@AIwithkhan][akhan]、[@abulu8][abulu-fpv]（两条，[第二条][abulu-chase]）和 [@AIwithSynthia][synthia]。

这说明什么、不说明什么：

- **唯一的成本说法是相对的。** 1080p 那条说"便宜很多"，没有给数字。本列表没有创作者说明自己实际花了多少钱。
- **不少帖子是合作帖。** 标注为公开了提示词的帖子中，有 5 条带有 #HiggsfieldPartner 标签，提到了 Higgsfield。应把它们看作合作方的作品展示，而不是中立测试。
- **发布周意味着每人一次。** 大多数帖子是发布当天的单次尝试，没有统一方法。

## 在 SandBase 上的价格

SandBase 的标价为每秒时长 0.08，默认 5 秒，因此默认片段为 0.40（来自 SandBase inspect，`sandai/magi-2/text-to-video`）。这是标价，不是任何创作者实际花费的测量值。

---

Lab 数据：MAGI-2 目前尚无记录。创作者数据：他们本人的帖子，已附链接，未经我们独立验证。

[john-cmp]: https://x.com/johnAGI168/status/2125480417847353448
[john-i2v]: https://x.com/johnAGI168/status/2125578530272821680
[cris]: https://x.com/criscxuan/status/2125504100670530040
[joshesye]: https://x.com/joshesye/status/2125557298135245012
[bubble]: https://x.com/BubbleBrain/status/2125384722159411357
[kiber]: https://x.com/Kiber_Alla/status/2125596457604444568
[akhan]: https://x.com/AIwithkhan/status/2125522773258952776
[abulu-fpv]: https://x.com/abulu8/status/2125373412910747712
[abulu-chase]: https://x.com/abulu8/status/2125537498659225849
[synthia]: https://x.com/AIwithSynthia/status/2125574502285529485
