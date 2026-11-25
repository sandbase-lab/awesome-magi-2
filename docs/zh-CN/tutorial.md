# MAGI-2 教程：从提示词到视频片段

[English](../tutorial.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

四步把提示词变成视频片段。通过 SandBase 运行 MAGI-2，然后下载视频。

## 1. 从喜欢的视频开始

在[合集](../../README.zh-CN.md)里点任意标题，进入它在 [SandBase Lab][lab] 的页面：视频片段、原帖，以及作者公开的提示词（如果有）。复制提示词。

作者没有公开提示词？照[提示词写法](prompt-guide.md)自己写一条，里面有填空模板。

## 2. 用同一个提示词对比模型

在[视频竞技场][arena]里，可以让同一段文字分别经过 MAGI-2 和其他视频模型，并排查看结果。每个模型各跑一次，就能在你自己的任务上验证[对比页](model-comparison.md)里的说法。

## 3. 或者用 SandBase CLI 运行

MAGI-2 在 SandBase 上的模型 ID 是 `sandai/magi-2/text-to-video`。[SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli) 会读取 `SANDBASE_API_KEY`。

1. 在[控制台][keys]创建 Key 并导出：`export SANDBASE_API_KEY=<你的 Key>`
2. 查看输入字段和价格（免费）：`npx -y @sandbaseai/cli@latest inspect sandbase_sandai_magi_2_text_to_video`
3. 把输入保存为 `prompt.json`，例如 `{"prompt": "<你的提示词>", "duration": 5, "aspect_ratio": "16:9"}`。
4. 运行：

```bash
npx -y @sandbaseai/cli@latest run sandbase_sandai_magi_2_text_to_video -f prompt.json -w --timeout 900 -o result.json
```

- `-w` 会等待视频生成完成；`result.json` 里是视频地址。
- `duration` 可设 4 到 30 秒，按秒计费：每秒 0.08，默认 5 秒为 0.40（来自 SandBase inspect）。
- MAGI-2 输出 1080p，默认带原生音轨（`generate_audio`）。

## 4. 保存视频

从 `result.json` 里的地址下载视频。视频自带声音，不需要另外录制。

## 分享

把视频片段发到 X，附上提示词并 @ MAGI-2。想被收录，就[提交给我们](https://github.com/sandbase-lab/awesome-magi-2/issues/new?template=submit-video.yml)；通过后会先进入 Lab 合集，下一次每日同步时出现在本列表。

[lab]: https://www.sandbase.ai/lab/ai-videos/magi-2?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[arena]: https://www.sandbase.ai/arena/text-to-video?models=sandai%2Fmagi-2%2Ftext-to-video&utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[model]: https://www.sandbase.ai/model/sandai/magi-2/text-to-video?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
