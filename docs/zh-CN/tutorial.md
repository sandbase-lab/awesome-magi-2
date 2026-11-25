# MAGI-2 教程：从提示词到视频片段

[English](../tutorial.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

四步把提示词变成视频片段。MAGI-2 通过 SandBase API 调用；你保存返回结果，再保留或录制视频片段。

## 1. 从喜欢的视频开始

在[合集](../../README.zh-CN.md)里点任意标题，进入它在 [SandBase Lab][lab] 的页面：视频片段、原帖，以及作者公开的提示词（如果有）。复制提示词。

作者没有公开提示词？照[提示词写法](prompt-guide.md)自己写一条，里面有填空模板。

## 2. 用同一个提示词对比模型

在[文本竞技场][arena]里，可以让同一段文字分别经过 MAGI-2 和其他模型，并排查看结果。每个模型各跑一次，就能在你自己的任务上验证[对比页](model-comparison.md)里的说法。

## 3. 或者直接调用 API

MAGI-2 在 SandBase 上的模型 ID 是 `sandai/magi-2/text-to-video`。

1. 在[控制台][keys]创建 Key 并导出：`export SANDBASE_API_KEY=<你的 Key>`
2. 把提示词保存为 `prompt.txt`。
3. 运行：

```bash
jq -n --rawfile prompt prompt.txt '{
  model: "sandai/magi-2/text-to-video",
  max_tokens: 128000,
  messages: [{role: "user", content: $prompt}]
}' |
curl -sS --max-time 900 https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- > response.json

jq '.usage' response.json
jq '.choices[0].message' response.json > message.json
```

- `max_tokens: 128000` 是本例使用的输出预算。SandBase 的模型数据未列出该模型的上限，提高前请先查看[模型页][model]。
- `--max-time 900` 给长时间的生成留出足够时间。
- 价格随时长变化：每秒 0.08，默认 5 秒（来自 SandBase inspect）。在请求里设置你需要的时长。
- `usage` 显示计费的用量。在 `message.json` 里查看模型返回的内容；如果是文件链接，就下载该文件。

### 用 SandBase CLI

同一个模型也可以通过 [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli) 调用，它同样读取 `SANDBASE_API_KEY`：

```bash
npx -y @sandbaseai/cli@latest inspect sandai/magi-2/text-to-video   # 输入字段和价格，免费
jq -n --rawfile prompt prompt.txt '{max_tokens: 128000, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_sandai_magi_2_text_to_video -f input.json --timeout 900 -o result.json
```

`-o result.json` 保存返回结果。运行前先用 `inspect` 确认输入字段。

## 4. 录制视频片段

如果输出是可以直接保存的视频文件，就保留该文件。如果返回的是网页，则用 [`scripts/record.mjs`](../../scripts/record.mjs) 无头录制：

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # 或使用本机 Chrome：export RECORD_CHANNEL=chrome
node scripts/record.mjs magi-2.html magi-2.mp4 12 1920 1080   # 12 秒，1080p
```

它按你给的尺寸打开页面，录指定秒数，再用 ffmpeg 转成 H.264 MP4。想要干净的效果，就在提示词里要求固定时长的镜头或循环（见[提示词写法 §4](prompt-guide.md#4-把镜头规则写成硬约束)），让画面不依赖鼠标。

录制本身只有画面，音频在剪辑里加。

## 安全运行生成的内容

模型输出是你没有审阅过的内容。如果要打开生成的网页或运行其中的代码，请使用 [SandBase Sandbox][sandbox]：一个有时限、接触不到你的文件和 Key 的隔离环境。

## 分享

把视频片段发到 X，附上提示词并 @ MAGI-2。想被收录，就[提交给我们](https://github.com/sandbase-lab/awesome-magi-2/issues/new?template=submit-video.yml)；通过后会先进入 Lab 合集，下一次每日同步时出现在本列表。

[lab]: https://www.sandbase.ai/lab/ai-videos/magi-2?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[arena]: https://www.sandbase.ai/arena/text?models=sandai%2Fmagi-2%2Ftext-to-video&utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[model]: https://www.sandbase.ai/model/sandai/magi-2/text-to-video?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
