"""Every model-specific value for this list. The other scripts are generic and read from here."""
import os

ORIGIN = os.environ.get('LAB_ORIGIN', 'https://www.sandbase.ai').rstrip('/')
SITE = 'https://www.sandbase.ai'  # public links in READMEs and docs always use the canonical host

SLUG = 'magi-2'
REPO = 'sandbase-lab/awesome-magi-2'

CFG = dict(
    slug=SLUG,
    kind='video',
    cli_tool='sandbase_sandai_magi_2_text_to_video',
    name='MAGI-2',
    short='MAGI-2',
    vendor='Sand.ai',
    model_id='sandai/magi-2/text-to-video',
    repo=REPO,
    repo_url=f'https://github.com/{REPO}',
    campaign='awesome-magi-2',
    lab_collection=f'{SITE}/lab/ai-videos/{SLUG}',
    lab_data=f'{ORIGIN}/lab/data/ai-videos/{SLUG}.json',
    media_prefix=f'{SITE}/lab/media/x/{SLUG}/',
    model_page=f'{SITE}/model/sandai/magi-2/text-to-video',
    arena=f'{SITE}/arena/text-to-video?models=sandai%2Fmagi-2%2Ftext-to-video',
    evals=f'{SITE}/leaderboards',
    pelican=f'{SITE}/arena/pelican-test',
    keys=f'{SITE}/console/keys',
    sandbox=f'{SITE}/landing/sandbox',
    lab_home=f'{SITE}/lab/',
    all_collections=f'{SITE}/lab/ai-videos',
    user_agent=f'awesome-magi-2-sync/1.0 (+https://github.com/{REPO})',
    guide_patterns=7,  # numbered sections in docs/prompt-guide.md
    banner_title='Awesome MAGI-2',
    banner_sub='Videos · prompts · tutorial · model comparison',
    # Finished pieces only on the banner: no comparisons or other models' names.
    banner_skip=('vs', 'versus', 'comparison', 'compar', 'benchmark', 'test', 'opus', 'claude', 'sonnet',
                 'haiku', 'gpt', 'gemini', 'argon', 'deepseek', 'kimi', 'grok', 'qwen', 'glm', 'seedance',
                 'magi'),
    not_affiliated={'en': 'Not affiliated with or endorsed by Sand.ai.', 'zh-CN': '与 Sand.ai 无隶属或背书关系。'},
    # No SandBase blog post on this model is recorded yet. build_readme.py skips the reading
    # section while this is empty; do not invent links here.
    reading=[],
)

# README and prompt-index copy. Placeholders in {braces} are filled by build_readme.py
# ({name}, {short}, {model_id}, {guide_patterns}, links such as {lab_stats} or {model_page}, counts {n}/{a}/{p}).
# Every fact here is sourced: `sandbase inspect sandai/magi-2/text-to-video`, the Lab collection's
# own posts (linked), and the creator posts in the collection (linked). No Lab Evals or Pelican row yet.
COPY = {
    'en': {
        'switch': 'English · [简体中文](README.zh-CN.md)',
        'tagline': 'A curated list of **MAGI-2 examples**: videos, prompts and clips made with MAGI-2, the video model from Sand.ai, announced on November 24, 2026. Anime, short films, action, music videos, ads and showcases, each one credited to its creator and linked to the original post, with the prompt wherever the creator shared it.',
        'alt': 'Awesome MAGI-2: videos, prompts, tutorial and model comparison',
        'stats': '**{n} videos** from **{a} creators** · **{p}** with the creator\'s prompt · synced daily from [SandBase Lab]({lab_stats})',
        'start': 'Start here',
        'start_rows': [
            ('Watch the videos', '[Browse by category](#contents) below, or [play them full-size on SandBase Lab]({lab_quickstart})'),
            ('Copy a prompt', '[Prompt index](docs/prompts.md): every video that comes with its prompt'),
            ('Write your own prompt', '[Prompt guide](docs/prompt-guide.md): {guide_patterns} patterns and a fill-in template'),
            ('Make a video', '[Tutorial](docs/tutorial.md): prompt → clip, with the SandBase CLI call'),
            ('Check the evidence', '[MAGI-2 model comparison](docs/model-comparison.md): what is measured and what creators reported'),
            ('Try it now', '[Run MAGI-2 in the Lab arena]({arena_quickstart}), next to other models'),
        ],
        'goal': 'I want to…', 'where': 'Go to',
        'how': 'Click a preview to play the video. Click a title for the post, the prompt and **Recreate** on SandBase Lab. **@handle** links to the creator\'s post on X.',
        'contents': 'Contents',
        'featured': 'Featured',
        'show_all': 'Show all {n}',
        'recreate': 'Make a video with {name}',
        'recreate_body': [
            'Every video page on [SandBase Lab]({lab_recreate}) links to the original X post and, when the creator shared one, the prompt.',
            '',
            'On SandBase, {name} is `{model_id}`. Create a key in the [console]({keys}) and export it as `SANDBASE_API_KEY`, put `{{"prompt": "…", "duration": 5}}` in `prompt.json`, and run:',
        ],
        'recreate_after': '`-w` waits for the clip and `result.json` holds its URL. Full walkthrough: [tutorial](docs/tutorial.md). Pricing: [model page]({model_page}).',
        'prompt_tag': 'prompt',
        'more': '**[See all {n} on SandBase Lab →]({lab_section})**',
        'faq': 'FAQ',
        'faq_items': [
            ('What is MAGI-2?', 'MAGI-2 is the video model from Sand.ai, announced on November 24, 2026. On SandBase it is `{model_id}`. The list price is 0.08 per second of duration, so a default 5-second clip is 0.40. Source: `sandbase inspect sandai/magi-2/text-to-video`.'),
            ('How are these MAGI-2 videos made?', 'The clips are video output, and each card is a finished piece from the creator\'s post. Five of the ten posts that shared a prompt name Higgsfield, and all five carry the #HiggsfieldPartner tag. Other posts only say they used MAGI-2. Each card links to the creator\'s original post.'),
            ('Where do I find the prompt for a video?', 'Videos tagged **prompt** come with the creator\'s prompt on their Lab page. The [prompt index](docs/prompts.md) lists all of them.'),
            ('How do I write a good MAGI-2 prompt?', 'Describe one shot or one sequence in plain terms: the format and style, the subject, the camera and the timing. Several posts state rules explicitly: one continuous take with no cuts, no reversed motion, or a timed shot list. Details and a template: [prompt guide](docs/prompt-guide.md).'),
            ('How do I use the MAGI-2 API?', 'On SandBase the model id is `{model_id}`. Run it with the SandBase CLI, as in [Make a video](#make-a-video-with-magi-2); `sandbase inspect` lists the input fields. See the [model page]({model_page}).'),
            ('Is MAGI-2 better than Seedance 2.5 or other video models?', 'Nothing is measured yet: this list has no Lab measurement of MAGI-2. One creator\'s own test found 1080p much cheaper than Seedance 2.5 and not far from Seedance 2.5 at 480p, with no figures given. Another found real-person skin in an image-to-video test less natural. Details and what is still unknown: [model comparison](docs/model-comparison.md).'),
            ('How much does one video cost?', 'The list price is 0.40 for a default 5-second clip, at 0.08 per second of duration (SandBase inspect). The creator posts in this list do not state what they paid, so no creator-reported cost range is given yet.'),
            ('Can I reuse these videos?', 'No, not by default. They belong to their creators. See [MEDIA-RIGHTS](MEDIA-RIGHTS.md).'),
        ],
        'contribute': 'Suggest a video',
        'contribute_body': 'Know a MAGI-2 creation that should be here? [Open a submission]({repo_url}/issues/new?template=submit-video.yml) with the original X post. Accepted posts are added on SandBase Lab and show up here on the next daily sync. If this list helped you, a ⭐ helps others find it.',
        'credits': 'Credits & rights',
        'credits_body': [
            'Every video, prompt and post belongs to its creator. Cards credit the author and link to the original post. The MIT license covers this repository\'s scripts only. To correct a credit or remove a video, see [MEDIA-RIGHTS](MEDIA-RIGHTS.md).',
            '{not_affiliated}',
        ],
        'footer': 'Maintained by [SandBase Lab]({lab_home}) · [All AI video collections]({all_collections})',
        'p_title': 'MAGI-2 prompts',
        'p_switch': 'English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)',
        'p_intro': '{n} MAGI-2 videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with {short} on SandBase Lab. New to prompting {short}? Start with the [prompt guide](prompt-guide.md).',
        'p_note': 'Each entry quotes the creator\'s post as published on X. Some posts put the prompt in a reply or behind a link, so open the post on X to read the full thread. Posts keep the creator\'s language.',
        'p_watch': 'Watch',
        'p_open': 'Recreate on SandBase Lab',
    },
    'zh-CN': {
        'switch': '[English](README.md) · 简体中文',
        'tagline': '精选 **MAGI-2 案例**合集：用 Sand.ai 的视频模型 MAGI-2 做出的视频、提示词和片段，2026 年 11 月 24 日发布。包括动画、短片、动作、音乐视频、广告和模型展示，每条都注明作者并链接原帖，作者公开提示词的一并列出。',
        'alt': 'Awesome MAGI-2：视频、提示词、教程和模型对比',
        'stats': '共 **{n} 条视频**，来自 **{a} 位创作者** · **{p} 条**附作者提示词 · 每天从 [SandBase Lab]({lab_stats}) 同步',
        'start': '从这里开始',
        'start_rows': [
            ('看视频', '在下方 [按分类浏览](#contents)，或 [在 SandBase Lab 大屏播放]({lab_quickstart})'),
            ('复制提示词', '[提示词索引](docs/zh-CN/prompts.md)：所有附带提示词的视频'),
            ('自己写提示词', '[提示词写法](docs/zh-CN/prompt-guide.md)：{guide_patterns} 条写法和一个填空模板'),
            ('做一个视频', '[教程](docs/zh-CN/tutorial.md)：提示词 → 视频片段，含 SandBase CLI 调用'),
            ('了解证据', '[MAGI-2 模型对比](docs/zh-CN/model-comparison.md)：哪些是实测，哪些是创作者报告'),
            ('马上试试', '[在 Lab 竞技场运行 MAGI-2]({arena_quickstart})，和其他模型并排对比'),
        ],
        'goal': '我想…', 'where': '去这里',
        'how': '点击预览图播放视频；点击标题前往 SandBase Lab 查看原帖、提示词，并一键 **复刻**；**@作者** 链接到 X 原帖。',
        'contents': '目录',
        'featured': '精选',
        'show_all': '展开全部 {n} 条',
        'recreate': '用 {name} 做视频',
        'recreate_body': [
            '[SandBase Lab]({lab_recreate}) 的每个视频页都链接到 X 原帖；作者公开了提示词的，也会附上。',
            '',
            '{name} 在 SandBase 上的模型 ID 是 `{model_id}`。在 [控制台]({keys}) 创建 Key 并导出为 `SANDBASE_API_KEY`，把 `{{"prompt": "…", "duration": 5}}` 写进 `prompt.json`，然后运行：',
        ],
        'recreate_after': '`-w` 会等待视频生成完成，`result.json` 里是视频地址。完整步骤见 [教程](docs/zh-CN/tutorial.md)，价格见 [模型页]({model_page})。',
        'prompt_tag': '提示词',
        'more': '**[在 SandBase Lab 查看全部 {n} 条 →]({lab_section})**',
        'faq': '常见问题',
        'faq_items': [
            ('MAGI-2 是什么？', 'MAGI-2 是 Sand.ai 的视频模型，2026 年 11 月 24 日发布。在 SandBase 上它是 `{model_id}`。标价为每秒时长 0.08，默认 5 秒的片段为 0.40。来源：`sandbase inspect sandai/magi-2/text-to-video`。'),
            ('这些 MAGI-2 视频是怎么做出来的？', '它们是视频输出，每张卡片都是作者帖子里的成品。标注为公开了提示词的 10 条帖子中，有 5 条提到了 Higgsfield，这 5 条都带有 #HiggsfieldPartner 标签。其他帖子只说明用了 MAGI-2。每张卡片都链接到作者的原帖。'),
            ('在哪里找到视频的提示词？', '标有 **提示词** 的视频，其 Lab 页面上有作者的提示词。[提示词索引](docs/zh-CN/prompts.md) 列出了全部。'),
            ('怎么写好 MAGI-2 提示词？', '用普通的语言描述一个镜头或一段连续画面：风格、主体、镜头和时间安排。有几条帖子明确写了规则：一镜到底、不切镜、不倒放，或给出定时的分镜表。详见 [提示词写法](docs/zh-CN/prompt-guide.md)。'),
            ('怎么调用 MAGI-2 API？', '在 SandBase 上模型 ID 是 `{model_id}`。用 SandBase CLI 运行，示例见 [做视频](#用-magi-2-做视频)；`sandbase inspect` 会列出输入字段。模型页见 [{model_page}]({model_page})。'),
            ('MAGI-2 比 Seedance 2.5 或其他视频模型更好吗？', '目前没有实测结论：本列表没有 MAGI-2 的 Lab 实测数据。一位创作者的个人测试认为 1080p 比 Seedance 2.5 便宜很多，效果与 Seedance 2.5 的 480p 相近，但没有给出数字。另一位在图生视频测试中认为真人皮肤不够自然。详见[模型对比](docs/zh-CN/model-comparison.md)。'),
            ('做一个视频要花多少钱？', '标价为 0.40（默认 5 秒片段），按每秒时长 0.08 计算（来自 SandBase inspect）。本列表中的创作者帖子没有公布实际花费，因此暂无创作者报告的费用范围。'),
            ('可以转用这些视频吗？', '默认不可以，视频归作者所有。见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。'),
        ],
        'contribute': '推荐作品',
        'contribute_body': '发现了应该收录的 MAGI-2 作品？附上 X 原帖 [提交给我们]({repo_url}/issues/new?template=submit-video.yml)。通过后会先加入 SandBase Lab，下一次每日同步时出现在这里。觉得有用的话，点个 ⭐ 能让更多人看到。',
        'credits': '致谢与权利',
        'credits_body': [
            '所有视频、提示词和帖子归作者所有。每张卡片都注明作者并链接原帖。MIT 许可证只覆盖本仓库的脚本。更正署名或下架视频请见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。',
            '{not_affiliated}',
        ],
        'footer': '由 [SandBase Lab]({lab_home}) 维护 · [全部 AI 视频合集]({all_collections})',
        'p_title': 'MAGI-2 提示词',
        'p_switch': '[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)',
        'p_intro': '共 {n} 条 MAGI-2 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 {short} 一键 **复刻**。第一次写 {short} 提示词？先看 [提示词写法](prompt-guide.md)。',
        'p_note': '每条都按 X 上发布的原文引用作者帖子。有的帖子把提示词放在回复里，或放在外部链接中，请打开 X 原帖查看完整讨论串。帖子原文保留作者语言。',
        'p_watch': '观看',
        'p_open': '在 SandBase Lab 复刻',
    },
}

# Labels mirror shared/ai-videos.ts VIDEO_CATEGORIES in the Lab repo.
CATEGORIES = {
    '3d-scene': ('3D scenes', '3D 场景'),
    'motion-graphics': ('Motion graphics', '动效'),
    'game': ('Games', '游戏'),
    'ui-demo': ('Product UI', '产品界面'),
    'particles': ('Particles & shapes', '粒子与形状'),
    'data-viz': ('Charts & diagrams', '图表图解'),
    'kinetic-type': ('Kinetic type', '文字动效'),
    'explainer': ('Explainers', '讲解'),
    'launch-film': ('Launch films', '发布片'),
    'short-film': ('Short films', '短片'),
    'music-video': ('Music videos', '音乐视频'),
    'anime': ('Anime', '动画'),
    'action': ('Action', '动作'),
    'ad': ('Ads', '广告'),
    'comparison': ('Tests & comparisons', '测试对比'),
    'showcase': ('Model showcases', '模型展示'),
}


def utm(medium, content=None):
    q = f'utm_source=github&utm_medium={medium}&utm_campaign={CFG["campaign"]}'
    return q + (f'&utm_content={content}' if content else '')
