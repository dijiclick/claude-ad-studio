# Format menu — every workflow the course teaches

> Engines run on the owner's **logged-in accounts** only (Flow via `gflow`, Higgsfield/Kling/HeyGen web apps). **Video engine = Veo 3.1** — the course taught much of this on Sora 2; Sora is not available, so every Sora step is translated to Veo 3.1 below. Kie.ai, fal, EvoLink and other APIs appear only because the course used them — don't call them.

Pick the format from the request, then open the listed lesson + master prompt. Lessons are in `lessons/`, prompts in `master-prompts/`.

| Request sounds like | Format | Engine | Lesson | Master prompt(s) |
|---|---|---|---|---|
| "UGC ad", "creator talking about my product", "clone this ad" | **Talking selfie UGC** (15 s) | Veo 3.1 (2 × 8 s, `gflow` i2v from the approved still) | 03, 04, 05, 29 | gem-ugc-deconstructor-v2, claude-project-rewriter |
| "longer", "25 seconds", "multi-scene" | **Multi-clip Veo ad** (3–4 × 8 s; the course's 25 s storyboard, rebuilt for Veo) | Veo 3.1 — chain clips: last frame → next `initial_frame`, or `initial_frame` + `end_frame` to bridge | 10 (scene-by-scene prompt format) | claude-project-rewriter (scene format in lesson 10) |
| "same girl in every video", "series" | **Consistent character** | Veo 3.1: same still as `initial_frame` every clip, a saved Flow character (`@Name`), or `r2v` with reference images | 12 (method; translate Sora steps to Veo) | lesson 12 prompts |
| "keep my product exact" | **Exact product in every clip** | Nano Banana Pro still with the product already in hand → Veo i2v; or Veo `r2v` with the product photo as a reference image | 13 (product-prep steps) | — |
| "podcast ad", "two people talking", "expert interview" | **Two-host podcast** (8 s clips, ≤ 20–25 words each) | Veo 3.1 Fast, Frames-to-Video (host 1 first frame, host 2 last frame) → ElevenLabs Voice Changer | 41, 24 | veo-podcast-master-prompt, veo-podcast-action-template, veo-podcast-script-format, podcast-avatar-json, elevenlabs-voice-design |
| "TikTok Shop style", "talking photo" | **Image → lip-sync** | Nano Banana clone → HeyGen / Hedra / InfiniteTalk, or Kling 2.5 Turbo ("speaks continuously", 5 s) + sync.so Lip Sync 2.0 Pro | 40, 07 | nano-banana-clone |
| "copy this person's movement / dance / gesture" | **Motion transfer** | Kling 2.6 Motion Control (image must match the reference's first frame) | 43 | — |
| "cartoon", "3D character", "Pixar style", "talking organ/product" | **AI animation** | Nano Banana Pixar clone → Veo | 42 | nano-banana-pixar-clone |
| "a quick image ad first" | **Image-based UGC (1.0)** | ChatGPT JSON → Higgsfield Soul (iPhone style) → product placement → Higgsfield Speak | 06 | Prompt A/B/C in lesson 06 |
| "100 static ads", "image ads at scale" | **Winner-import statics** | Claude writes Nano Banana prompt + copy per winning ad → Nano Banana Pro | 53 | prompt in lesson 53 |
| "write ad copy / primary text" | **Copywriting gem** | Gemini Gem or you (+ `copy-principles.md`) | 50 | gem-copywriting-master |
| "Meta captions" | **Meta ad captions** | you | 52 | meta-ads-captions |
| "advertorial / presell page" | **Advertorial** (labelled "Sponsored", your own publication — never a news-brand clone) | you (+ `advertorial-patterns.md` skeleton, skip its "don't copy" list) | 51 | gem-advertorials |
| "track conversions for an affiliate/web offer" | **Conversion tracking** | Everflow / Keitaro → Meta CAPI | — | `conversion-tracking.md` (legit parts only) |
| "automate a batch", "one-minute video from a script" | **Segment pipeline** | script → split > 55 words → 8 s Veo segments → bridge frames | 44, 70 | veo-automation-examples |

## Engine quick facts
- (Course used Sora 2 — 15 s clips, 25 s storyboard, characters. Not available here; everything above maps it to Veo 3.1.) Product photos: white background beats transparent PNG.
- Veo 3.1: 8 s per clip, 9:16, first/last frame control; native audio is robotic for many voices → keep pacing, swap voice with ElevenLabs Speech-to-Speech. ~$0.17/clip via EvoLink (Fast), included in Google Ultra.
- Kling 2.5 Turbo: 5 s best, silent → lip-sync after. Kling 2.6: motion control.
- Avoid Freepik for long prompts (prompt length cap).
- Settings the course used (from its screenshots): Nano Banana product still 9:16 at 4K; statics 1:1 at 1K · Seedance 1.5 Pro product clip 9:16, 1080p, 8 s, fixed_lens off (generate_audio costs extra — or add ambience in CapCut) · Kling Motion Control 1080p, "video" orientation · Higgsfield Soul style "IPHONE", 9:16, batch 4 · HeyGen Avatar IV / Hedra Character-3 at 1080p for talking photos. Full transcriptions: `screenshot-prompts-and-settings.md` (course pack).
- Engine mixing (Veo + Kling) is itself a test variable — the member call's winners came from mixes.
