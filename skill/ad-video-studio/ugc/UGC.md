
# UGC module — AI UGC ads (Anti-Slop course method)

Part of `ad-video-studio`. Read this when the ad has an AI person or AI-generated footage. The parent SKILL.md's hard rules win on conflict;
after the creative is generated, return to the parent pipeline for compose, QA, finish and delivery.

Goal: an ad a scroller mistakes for a real creator's phone video, built on the structure of an ad that is already winning, shipped as several hook variants so the data picks the winner.

Three beliefs drive every choice here:
1. **Clone, don't invent.** An ad running 30+ days is proof of a working hook, lead type and pacing. Keep those; swap product, audience, benefit.
2. **Realism comes from specificity.** Each prompt field (phone model, light source, pores, hand jitter, room sound, gestures on words) removes one AI tell. One-line prompts give slop.
3. **Concept and volume beat polish.** The instructor's own conclusion: offer + concept decide winners; clearly-AI videos with a strong concept still scale. So ship 5 hooks on one body rather than version 8 of one ad.

## Workflow — do all steps without being asked

### 0. Load the project's house rules first
Before any creative, read the project's ad rules if they exist (e.g. `docs/marketing/*` brand/positioning/ad-rules, `AI-UGC-PLAYBOOK.md`, a UGC spec, the parent `SKILL.md` hard rules). **House rules override this skill** where they conflict — typical ones: AI person must *present, not testify*; mandatory AI label; banned words; no brand names spoken; real prices only; owner approves the character still before any video credits; no paid API switch without asking. Note which ones apply in one line.

### 1. Pick the format
Map the request to a format with `references/formats.md` (talking UGC, storyboard, podcast, talking photo, motion transfer, animation, statics, copy). Open that format's lesson and master prompts before writing anything.

### 2. Get inputs (ask only for what's missing; otherwise choose and mark `[assumed]`)
- **Product**: name, exact label/screen text, container/colours/size, the one benefit, audience, market language.
- **Reference ad**: a winning video. None given → find one with `references/finding-winners.md` (own past winners, Meta Ad Library 30+ days via `../scripts/research.py`, Kalo Data by spend, raw TikToks), or pick from `references/scenario-catalog.md`.
- **Length**: default 15 s. **Engine**: logged-in accounts only (parent SKILL.md → "Accounts, not APIs"): Veo 3.1 + Nano Banana via `gflow` (Google Flow). No Sora (not available) and never a generation API.

### 3. Deconstruct the reference (replaces the course's Gemini Gem)
```bash
python3 ~/.claude/skills/ad-video-studio/ugc/scripts/deconstruct_video.py VIDEO [OUT_DIR] --every 1   # add --engine parakeet for faster English-only transcripts
```
Read `info.txt`, `transcript.srt`, `contact_sheet.jpg`, then write:
```
Full script (word-for-word, (pause), [emotion], fillers) · Lead type · Hook (first 3 s: words + action)
Character · Setting + one motivated light source (+K) · Camera (shot, angle, handheld vs propped)
Product interaction (how held, when the label is legible) · Performance timeline (gesture ↔ word, with seconds)
Audio (mic, room, 2–3 sounds, music?) · Why it works (1–3 lines)
```
Trust the frames over course example prompts (a propped phone stays propped). Full Gem logic: `references/master-prompts/gem-ugc-deconstructor-v2.md`.

### 4. Write the hooks and the script
- Tag the viewer's awareness level first (most aware → product → solution → problem → unaware); it decides the lead type (`references/copy-principles.md`).
- Pick the lead type and **5 hooks** from `references/hooks.md` (presenter-safe versions when the house rules forbid testimony). Only the first line + first gesture change between variants; the body is shared.
- Script pace: English ≈ 3 words/s, Turkish ≈ 2.4 words/s → 15 s ≈ 45 EN / 36 TR words; one 8 s clip ≈ 20–24 EN / 16–19 TR words. Hook first, fillers, real numbers only.
- If the project routes copy through another model/process (e.g. ChatGPT writes lines, Claude checks), follow it and feed it the hooks + rules as the brief.

### 5. Character still (for image-to-video routes — spend ~50% of the effort here)
One prompt, regenerate until right (multi-step edits smooth the skin). Must include: phone-selfie framing matching the planned camera, one motivated light source without blown highlights, natural skin texture with visible pores + one small imperfection, 1–2 personal details (hoops, one AirPod, hair clip), an audio-logic prop if the clip has clean sound (wired earphones, clip-on mic, phone close), a lived-in but calm background. Beautiful is allowed (respect house taste); flawless/airbrushed is the tell. Details: `references/realism-checklist.md`.

### 6. Write the video prompt (replaces the course's Claude Project)
Fill `references/prompt-formula.md` (opening line with phone + `IMG_####.MOV`, Character, position + product in hand, tone simile, Cinematography ×6, Subject Action & Performance, Dialogue (Exact Script), Audio & Ambience (Diegetic Only), Authenticity Keywords, Negatives). Rules:
- Only details from the deconstruction + product info; ≤ 5,000 characters.
- Camera motion matches the capture (handheld selfie → sway + micro-jitter; propped → static micro-shifts). Never "static locked-off" on an arm's-length selfie.
- Label "reads correctly left to right (not mirrored)"; strong product colour → lock white balance.
- Multi-clip: every clip is a full standalone prompt; only Action + Dialogue change. Veo 3.1 = 8 s per clip; a 15 s ad = 2 clips, 25–30 s = 3–4 clips chained (last frame of clip N → `initial_frame` of clip N+1, or set both `initial_frame` and `end_frame` to bridge). If a line sits between clip lengths, pad with throwaway words and cut them in the edit.
- If the project already has a locked prompt structure (e.g. Scene / Line / Fixed rules), keep its structure and pour these layers into it.

**Gate — run it on every prompt before generating:**
```bash
python3 ~/.claude/skills/ad-video-studio/ugc/scripts/check_prompt.py prompt.txt --seconds 8 --lang tr [--presenter]
```
Fix every FAIL; fix WARNs unless there's a reason (say it in one line).

### 7. Generate
Engine details and costs: `references/formats.md` → Engine quick facts. Respect the house approval points (typically: show the still before paying for video). Once approved, run all 5 hook clips as one batch; the body/demo is generated once and reused.
- **Veo 3.1** (`gflow_generate_video` on the owner's logged-in Flow account — `gflow_auth_status` first; `mode: "i2v"`, 9:16, `initial_frame` = approved still; stills via `gflow_generate_image`, `model: "nano-pro"`): native speech; if the voice drifts or sounds robotic, keep the timing and swap the voice with ElevenLabs Speech-to-Speech.
- **Same person in every clip (Veo)**: reuse the approved still as `initial_frame`; or save her as a Flow character and tag `@Name` (`reference_entity_names`); or `mode: "r2v"` with `reference_images` = [still, product photo] so the product stays exact. Keep the base prompt identical, change only actions + line; don't describe the location/body differently between clips.
- If ~1 in 10 stills animates badly, make a new still instead of fighting the video model.

### 8. Deliver as a test batch
Output per ad: concept line, lead type, the 5 hook variants (line + gesture), the shared body, prompts that passed the gate, cost, and the test plan:
- Launch all 5 hooks in one ad set; judge on hook rate (3-s views ÷ impressions) and cost per result, not taste.
- Kill at ~2× target CPA after a small fixed spend; scale the winner by making 5 new hooks on its body (same lead type) — iterate hooks, not polish.
- UGC fatigues in ~7–8 days: plan 3–5 fresh variants per week.
- Record lead type + hook + result in the project's manifest so the next batch starts from winners.
Hand off edit/captions/music/label/delivery to the parent pipeline (`../SKILL.md` Pipeline steps 5–9).

## Guardrails (they protect the ad account)
- No AI person as a real doctor/expert, no fake credentials or reviews; presenter framing when AI people are labelled.
- No specific/medical/speed claims ("asleep in 5 min", "lose 20 lbs", "anında"); real, current numbers only.
- No cloning a real person's face or voice (change genetics, not just styling); no other people's saved characters or likenesses.
- No watermark removal, cloaking, or fake news-site landing pages (the course's excluded module).
Mention a guardrail in one line when it changes something; don't lecture.

## References
Files marked *(course pack)* are the course's verbatim material — present in the owner's full install, absent from the shareable build. If one is missing, work from `prompt-formula.md`, `hooks.md`, `realism-checklist.md` and `formats.md`; they carry the method.
- `references/formats.md` — format menu → lesson + master prompt + engine facts. **Start here.**
- `references/hooks.md` — lead types, 12 hook patterns, presenter-safe versions.
- `references/realism-checklist.md` — the 7 AI tells and their prompt fixes.
- `references/prompt-formula.md` — master template, verbatim realism phrases, word counts. **Read before any prompt.**
- `references/finding-winners.md` — where and how to find winning ads (course Module 2 + static-ads lesson + member call).
- `references/scenario-catalog.md` — 25 proven UGC scenarios.
- `references/copy-principles.md` — hook/script/static-copy rules merged from the course's 5 books (Great Leads, Ogilvy, Hopkins, Kennedy).
- `references/advertorial-patterns.md` — the page skeleton from 19 swipe advertorials + a "don't copy" list (fake news styling, fake doctors, fabricated comments, fake programs).
- `references/screenshot-prompts-and-settings.md` *(course pack)* — prompts and tool settings the course only showed in screenshots (Nano Banana, Seedance, Kling, HeyGen, Hedra, automation app).
- `references/conversion-tracking.md` *(course pack)* — legit affiliate/web conversion tracking (Everflow → Meta CAPI, Keitaro postbacks); the news-site clone lessons are described only, never used.
- `references/master-prompts/` *(course pack)* — the course's verbatim Gem/Claude/Veo/ElevenLabs/Nano Banana/copy prompts.
- `references/lessons/` *(course pack)* — per-lesson notes 01–70 (full brand prompt examples 20–26, statics 53, member call 70).
- `references/course-digest.md` *(course pack)* — one-page course summary.
