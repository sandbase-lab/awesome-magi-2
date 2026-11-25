# MAGI-2 tutorial: from prompt to clip

English · [简体中文](zh-CN/tutorial.md) · [← Back to the collection](../README.md)

From a prompt to a video clip in four steps. MAGI-2 is called through the SandBase API; you save the response, then keep or record the clip.

## 1. Start from a video you like

Open any title in the [collection](../README.md) to reach its page on [SandBase Lab][lab]: the clip, the original post and, when the creator shared one, the prompt. Copy the prompt.

No prompt shared? Write one with the [prompt guide](prompt-guide.md). It has a fill-in template.

## 2. Compare models on the same prompt

In the [text arena][arena], you can run the same words through MAGI-2 and other models and see each result side by side. Run the prompt once on each model to check a claim from the [comparison page](model-comparison.md) on your own task.

## 3. Or call the API

MAGI-2 is `sandai/magi-2/text-to-video` on SandBase.

1. Create a key in the [console][keys] and export it: `export SANDBASE_API_KEY=<your key>`
2. Save your prompt as `prompt.txt`.
3. Run:

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

- `max_tokens: 128000` is the output budget this example uses. SandBase's model data does not list a limit for this model, so check the [model page][model] before raising it.
- `--max-time 900` gives a long generation room to finish.
- The price follows duration: 0.08 per second, with a default of 5 seconds, per SandBase inspect. Set the duration you need in the request.
- `usage` shows what you were billed for. Look in `message.json` for what the model returned; if it is a link to a file, download that file.

### With the SandBase CLI

The same model through the [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli), which reads `SANDBASE_API_KEY` as well:

```bash
npx -y @sandbaseai/cli@latest inspect sandai/magi-2/text-to-video   # input fields and price, free
jq -n --rawfile prompt prompt.txt '{max_tokens: 128000, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_sandai_magi_2_text_to_video -f input.json --timeout 900 -o result.json
```

`-o result.json` saves the response. Check the input fields with `inspect` before you run.

## 4. Record the clip

If the output is a clip you can save, keep the file. If it comes back as a web page instead, record that page headlessly with [`scripts/record.mjs`](../scripts/record.mjs):

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # or use your installed Chrome: export RECORD_CHANNEL=chrome
node scripts/record.mjs magi-2.html magi-2.mp4 12 1920 1080   # 12 seconds at 1080p
```

It opens the page at the size you give, records for that many seconds, and converts to H.264 MP4 with ffmpeg. For a clean result, ask in the prompt for a fixed-length shot or loop (see [prompt guide §4](prompt-guide.md#4-write-camera-rules-as-hard-constraints)), so nothing depends on a mouse.

The recording is picture only. Add audio in the edit.

## Run generated output safely

Model output is content you haven't reviewed. If you open a generated page or run code from it, use a [SandBase Sandbox][sandbox]: an isolated environment with a time limit and no access to your files or keys.

## Share it

Post your clip on X with the prompt and mention MAGI-2. To have it added here, [submit it](https://github.com/sandbase-lab/awesome-magi-2/issues/new?template=submit-video.yml); accepted posts go into the Lab collection and show up in this list on the next daily sync.

[lab]: https://www.sandbase.ai/lab/ai-videos/magi-2?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[arena]: https://www.sandbase.ai/arena/text?models=sandai%2Fmagi-2%2Ftext-to-video&utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[model]: https://www.sandbase.ai/model/sandai/magi-2/text-to-video?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
