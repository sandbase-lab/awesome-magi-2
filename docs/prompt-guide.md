# MAGI-2 prompt guide: how to prompt MAGI-2 for video

English · [简体中文](zh-CN/prompt-guide.md) · [← Back to the collection](../README.md)

MAGI-2 is the video model from Sand.ai, announced on November 24, 2026. The patterns below come from the prompts creators shared with their posts in this collection. Each example quotes the creator and links to the post. The collection is at launch, so the guide has seven patterns and will grow as more prompts are shared.

## 1. Open with the format and the style

Name the format and the look in the first sentence, then the subject. [@AIwithkhan][akhan] opens with "Create a heartwarming, hilarious, ultra-realistic Japanese-style 3D animated family comedy" before describing the child and the breakfast scene. [@criscxuan][cris] describes the piece as a Japanese-style 2D cel-shaded music video animation in the first line of the post.

## 2. Describe the character item by item

[@AIwithSynthia][synthia] lists the figure in one sentence: "a miniature hand-drawn 2D young woman with long black hair, a pink hoodie, denim shorts, white sneakers, and a tiny red delivery backpack". Each item is something you can check in every frame of the clip.

## 3. Name each layer when styles mix

The same post puts a hand-drawn figure inside a photorealistic city: "exploring a gigantic photorealistic New York street" ([@AIwithSynthia][synthia]). Naming the style of each layer separately tells the model what stays drawn and what stays real.

## 4. Write camera rules as hard constraints

The most specific prompts in this set state rules, not just a scene. [@abulu8][abulu-fpv] wrote: "One single CONTINUOUS FPV drone shot, no cuts, one unbroken take... Only ever moves forward in time — never loops or reverses." A second post by the same creator repeats the rule and names the one exception with its timing: "NO slow motion except one half-second beat at the reveal" ([@abulu8][abulu-chase]). State what must not happen, then the single allowed exception and when it happens.

## 5. Tie motion to a tempo or a count

[@criscxuan][cris] set the clip to 8 seconds at 120 BPM with seven camera changes, and aimed for camera cuts, character moves and on-screen text to land on the beats. The creator reports that the beats, transitions and character continuity all worked. That is the creator's account, not a test. Give the tempo and the count, then list the events in order.

## 6. Write an ad as a timed shot list

[@joshesye][joshesye] describes a 15-second clothing ad, generated end to end, with a new outfit every 1.5 seconds, a fast push, a slow pull and close-ups. It opens on the text "ONE HIT" growing from behind the model and ends on the brand mark. The full prompt sits in the creator's reply, so the post gives the structure, not the prompt text. Number the beats in time, and name the camera move for each.

## 7. Test realistic people before you commit

Realistic human skin is the known weak spot in this set. In an image-to-video test, [@johnAGI168][john-i2v] wrote that the skin texture of a real person still feels off and not quite natural. If people on screen matter, run one short test first and check skin and faces in it before the full run.

## Settings

- **Duration.** The list price scales with duration: 0.08 per second, with a default of 5 seconds, per SandBase inspect. Ask for the length you need.
- **Output budget.** The API example in this list uses `max_tokens: 128000`. SandBase's model data does not list a limit for this model, so check the [model page][model] before raising it.

## A prompt to start from

```text
[Format and style in one sentence]: [subject], [look and materials].
Shot: [one continuous take, or the cut points], [duration] seconds.
Motion: [what moves, in order, with timings or beats per minute].
Rules: [what must not happen, and the one allowed exception with its timing].
Mixed styles: [which parts are drawn, which are photoreal].
```

Fill it in, then try it on the [Lab text arena][arena] or with the API in the [tutorial](tutorial.md).

---

Quotes are short excerpts credited to their authors; follow the links for full posts. Translations from Chinese are ours.

[akhan]: https://x.com/AIwithkhan/status/2125522773258952776
[abulu-fpv]: https://x.com/abulu8/status/2125373412910747712
[abulu-chase]: https://x.com/abulu8/status/2125537498659225849
[synthia]: https://x.com/AIwithSynthia/status/2125574502285529485
[cris]: https://x.com/criscxuan/status/2125504100670530040
[joshesye]: https://x.com/joshesye/status/2125557298135245012
[john-i2v]: https://x.com/johnAGI168/status/2125578530272821680
[arena]: https://www.sandbase.ai/arena/text?models=sandai%2Fmagi-2%2Ftext-to-video&utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
[model]: https://www.sandbase.ai/model/sandai/magi-2/text-to-video?utm_source=github&utm_medium=docs&utm_campaign=awesome-magi-2
