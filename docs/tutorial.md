# MAGI-2 tutorial: from prompt to clip

English · [简体中文](zh-CN/tutorial.md) · [← Back to the collection](../README.md)

From a prompt to a video clip in four steps. You run MAGI-2 through SandBase and download the clip.

## 1. Start from a video you like

Open any title in the [collection](../README.md) to reach its page on [SandBase Lab][lab]: the clip, the original post and, when the creator shared one, the prompt. Copy the prompt.

No prompt shared? Write one with the [prompt guide](prompt-guide.md). It has a fill-in template.

## 2. Compare models on the same prompt

In the [video arena][arena], you can run the same words through MAGI-2 and other video models and see each result side by side. Run the prompt once on each model to check a claim from the [comparison page](model-comparison.md) on your own task.

## 3. Or run it with the SandBase CLI

MAGI-2 is `sandai/magi-2/text-to-video` on SandBase. The [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli) reads `SANDBASE_API_KEY`.

1. Create a key in the [console][keys] and export it: `export SANDBASE_API_KEY=<your key>`
2. Check the input fields and the price (free): `npx -y @sandbaseai/cli@latest inspect sandbase_sandai_magi_2_text_to_video`
3. Save the input as `prompt.json`, for example `{"prompt": "<your prompt>", "duration": 5, "aspect_ratio": "16:9"}`.
4. Run:

```bash
npx -y @sandbaseai/cli@latest run sandbase_sandai_magi_2_text_to_video -f prompt.json -w --timeout 900 -o result.json
```

- `-w` waits for the clip; `result.json` holds the video URL.
- `duration` is 4 to 30 seconds and billed per second: 0.08 per second, so the default 5 seconds is 0.40 (SandBase inspect).
- MAGI-2 renders 1080p and adds a native audio track by default (`generate_audio`).

## 4. Keep the clip

Download the video from the URL in `result.json`. Clips come with their own sound, so there is nothing to record.

## Share it

Post your clip on X with the prompt and mention MAGI-2. To have it added here, [submit it](https://github.com/sandbase-lab/awesome-magi-2/issues/new?template=submit-video.yml); accepted posts go into the Lab collection and show up in this list on the next daily sync.

[lab]: https://www.sandbase.ai/lab/ai-videos/magi-2?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[arena]: https://www.sandbase.ai/arena/text-to-video?models=sandai%2Fmagi-2%2Ftext-to-video&utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[model]: https://www.sandbase.ai/model/sandai/magi-2/text-to-video?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
