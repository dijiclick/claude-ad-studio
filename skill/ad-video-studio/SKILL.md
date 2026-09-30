---
name: ad-video-studio
description: The one master skill for ANY ad or promo creative in any project — Reels/TikTok/Meta video ads, motion-graphic and real-data promos, AI UGC (AI talking creator/presenter, Veo 3.1 and Kling clips, consistent AI characters, multi-clip Veo ads), two-host AI podcast ads, talking-photo and AI-animation ads, motion transfer, static image ads at scale, ad copy, captions, advertorials, hook variations and cloning/deconstructing a winning ad. Encodes the owner's workflow and taste (story shape, real-data rules, typography, voice, music, QA, delivery) plus the full "Anti-Slop AI UGC System" course method (ugc/ module). Starts by asking which kind of ad to make, then routes to the right pipeline.
---

# Ad Video Studio

The owner's way of making ads. Follow it in order. Everything here was learned from the owner's
direct corrections — treat the **Hard rules** as requirements, not suggestions.

Reply to the owner in **English** (they may write Persian/Turkish); ad copy stays in the ad's market
language (Turkish for Turkey).

## Start here — which ad? (ask first, then route)

Unless the request already makes it obvious, ask ONE question (AskUserQuestion, multiple choice) before anything else:
**"Which kind of ad should I make?"**
| Option | Route |
|---|---|
| Motion-graphic / real-data ad (no AI person) — the default | this file, sections 0–5 |
| AI UGC — an AI person talks to camera (hook or full ad) | sections 0–1 here, then `ugc/UGC.md` for the creative, then back to Pipeline steps 5–9 (compose, QA, deliver) |
| AI podcast / two hosts, talking photo, AI animation, motion copy | `ugc/UGC.md` → `ugc/references/formats.md` picks the lesson |
| Static image ads (batch) | `ugc/references/formats.md` → "Winner-import statics" (lesson 53) |
| Copy only — captions, primary text, advertorial | Pipeline step 9 here + `ugc/references/copy-principles.md` + `ugc/references/master-prompts/` (copywriting / Meta captions / advertorial gems; advertorial skeleton in `advertorial-patterns.md`) |
Offer "5 hook variants" as the default deliverable for every video type. If the owner already said which type, skip the question.

The UGC module (`ugc/`) holds the whole course: `UGC.md` (workflow), `references/` (formats, hooks, realism checklist,
prompt formula, scenario catalog, verbatim master prompts, lesson notes 01–70, course digest) and `scripts/`
(`deconstruct_video.py` — frames + timed transcript of a reference ad; `check_prompt.py` — the realism/safety gate).
For ANY ad type, the hook and script follow `ugc/references/copy-principles.md` (awareness level → lead type, one idea, flag the buyer, real numbers).

## 0. Load the project first (2 minutes, before any creative)

Look for, in this order, and read what exists:
1. Brand system — `docs/marketing/BRAND.md`, `packages/tokens/`, a design-system doc. Palette, faces, colour rules.
2. Positioning — `docs/marketing/POSITIONING.md` or similar: what the product is, the pitch in the owner's words.
3. Audience — project memory / docs. (e.g. **women 18–45, Turkey**.)
4. Real data source — DB (`.env` `DATABASE_URL`), API, catalogue. Ads are built from REAL numbers.
5. Assets — app icon, store badges, logos, existing footage, music beds, prior ads' manifests.

If brand/audience are missing, ask at most 3 questions (audience, brand colours+fonts, where real data lives).
Never invent a palette or face when the project has one.

## 1. Hard rules (owner's taste — every one came from a rejection)

**Honesty**
- Every price, %, date on screen is real, from the project's data, checked today. Never fabricate.
- A "dropped, then dropped again" story must come from the event log with **no price rise in between**
  (a 2.699 → 799 → **1.999** → 479 item is NOT "two drops"). Quote the real dates and step percentages.
- Notification mock-ups use the app's REAL push format and real events only.
- Prices go stale: note the data date in the manifest; re-check before a paid run.
- Label AI: small "Seslendirme yapay zekâ ile oluşturulmuştur" (or "…karakter…" if an AI person appears).

**Typography & look** (for a fashion/consumer audience)
- Headlines and prices: **heavy UPPERCASE sans** (brand sans at 800, tight tracking) — the look of
  H&M/Mango/Bershka ads. The owner called italic high-contrast serif headlines "so bad".
- A display serif (e.g. Bodoni) only for the logo/wordmark — and never for prices (no ₺ glyph).
- No chunky rounded "button" boxes, no thick outlined/stroked TikTok captions — "amateur".
- Captions: one clean solid strip (ink bg, white 800 text), ≤ 2 lines, synced to the words.
- Follow the project palette strictly; accent colours only where the brand allows (e.g. one accent colour reserved for money saved).
- Product photos are shown **whole**: no Ken-Burns zoom on garments, no crop. Size the frame to the
  photo's aspect ratio (no letterbox bars). Get hi-res images (swap CDN width params, e.g. `w=750`→`w=1920`).
- Pick **desirable, audience-matched** products (women's pieces worn by a model, seasonal) over flat
  pack-shots or menswear. Cheap-to-cheaper drops (e.g. ~₺2–3k → under ₺1k) land hardest.

**Pacing & story**
- Not too fast, not ambiguous: ~18–24 s, ONE idea per scene, each visual synced to the spoken word.
- Default 5-beat shape (reorder only if the owner asks):
  1. **Hook 0–5 s** — the first line must land its point within **2–3 s** (a pattern interrupt, never a pitch or the brand name first); the attention-grabber first (for a deals app: the brand range + biggest real
     discount, cards landing as each brand is named, headline "%70'E VARAN İNDİRİMLER").
  2. **Problem** — the stress ("siteleri durmadan yenileme"), one product stuck at full price.
  3. **Solution** — real app footage doing the action (e.g. "Takibe al").
  4. **Proof** — real data: notifications stacking, price stepping down.
  5. **CTA end card** — brand, one strong line, "**hemen indir**", official store badges.
- Lead with the product's core promise in the owner's words, not a side feature (e.g. "add what
  you want → told when it drops, and again when it drops further"; sizes are secondary).

**Spend**
**Accounts, not APIs (owner rule, 2026-09-30)**
- Generate images and video ONLY through the owner's logged-in accounts: Google Flow via the `gflow` tools
  (run `gflow_auth_status` first; use an existing Flow project + local reference files). **Veo 3.1 is the video engine;
  Sora is not used** (the owner no longer has it) — translate any Sora step from the course to Veo 3.1.
- Never call a generation API — Gemini/Veo API, fal, Kie.ai, EvoLink, Replicate, OpenAI API — even if a key is in `.env`.
  If the logged-in route fails, stop and tell the owner; never fall back to an API.
- Approved APIs (owner, 2026-09-30) — text and voice only: **OpenAI direct** (ChatGPT lines, `scripts/gpt_lines.py`,
  default `gpt-5.6-sol`) and **ElevenLabs** (voice, `scripts/tts.py`). Keys live in the skill's local `.env`
  (`~/.claude/skills/ad-video-studio/.env`, mode 600) — never print them, never commit, push, zip or share that file.
  If a key is missing, copy it from the owner's other projects' `.env` into that file. No OpenRouter.
- Never switch to a paid API (Gemini/Veo API, fal, etc.) when a subscription route is intended — stop and ask.
- No Veo / AI presenter unless the owner asks for it. Motion graphics + real footage is the default.
- **When an AI person or AI footage IS in the ad** (UGC hook, presenter, Veo/Kling clip, AI podcast, AI statics):
  follow `ugc/UGC.md` automatically — format menu, hooks, realism layer, character-still rules,
  `check_prompt.py` gate before any paid generation. These hard rules still win where they conflict (presenter not testimony,
  AI label, real data, owner approves the still before video credits).
- Ask before posting anything publicly and before any paid campaign change.

## 2. Pipeline

Work in `video/ads/<date>-<slug>/` (or the project's video folder): `audio/ app/ hf/ manifest.json`.

0. **Research winners first** (full course method: `ugc/references/finding-winners.md` — own past winners, Meta Ad Library 30+ days, Kalo Data by spend, raw TikToks, green/red flags, analysis template) — `scripts/research.py video/research/<date>-<slug> --country TR --page "<competitor>" --query "<category words>"`
   (uses `meta-ads-collector`, installed with `uv tool install meta-ads-collector`; public Meta Ad Library, no key, no cost).
   It ranks ads by **days running** (advertisers only keep paying for what converts) and **copies running**,
   downloads the media and writes `winners.md` + a 6-frame sheet per top video — READ the sheets.
   Prefer `--page` with named competitors: broad `--query` pulls in noise (a hair clinic topped a fashion query).
   Label each top ad with: hook (first 2 s), format (ui-mimic, UGC talking head, carousel, green-screen, product
   montage, loop), message frame (how-it-works, hidden-cost, proof-stack, self-diagnosis, contrarian-take,
   feature→benefit) and offer. Pick 2–3 recurring angles and make ORIGINAL versions with our real data —
   never copy a competitor's footage, script or brand assets.
   For the top winner, also copy its **beat timing** (when the hook lands, when the proof appears, time to CTA):
   `python3 ~/.claude/skills/ad-video-studio/ugc/scripts/deconstruct_video.py <video> <out> --every 1` → read `contact_sheet.jpg` +
   `transcript.srt` and write the beat table into the brief. Structure is copied; words, footage and assets stay ours.
1. **Data** — query the real source; shortlist 4–8 products; view their photos (tile with ffmpeg and
   read the image) and pick with taste; verify each chosen number against events.
2. **Lines** — ChatGPT writes (`scripts/gpt_lines.py brief.md out.md`, OpenAI direct, `gpt-5.6-sol`; key from the skill `.env`): brief with the real
   data, beats, word limits per beat, and the rules (no first-person "I used it" for AI voices, no
   speed promises like "anında", no "ücretsiz", no implied brand partnership). Get 3 versions; Claude
   checks the rules and picks/merges.
   **Always also ask for 5 hook variants on the same body** (one per lead type from `ugc/references/hooks.md`:
   objection, secret, myth-bust, live reaction to a real number, visual A/B). Only the first line + first visual change,
   so the extra variants cost one short clip/scene each. Save the script + output in the ad folder.
3. **Voice** — `scripts/tts.py` (ElevenLabs v3, key from the skill `.env`, default Füsun Tuncer `cbqdgvVi3C6sgxIWpqIh`,
   natural speed, `[excited]` tag on the hook and CTA). Make 3 takes; `scripts/pick-take.sh 4 *.mp3`
   → most energetic opening wins. To change one line, splice a new take of just that line (`adelay` + concat).
   Build every scene/caption time from the printed word timings.
4. **App footage** (if there's an app) — release build on the simulator, status bar 9:41
   (`xcrun simctl status_bar … override`), deep-link to the exact product, drive with Maestro,
   record with `xcrun simctl io <udid> recordVideo`, convert to CFR 30 fps, find event times with
   `select='gt(scene,0.01)'`, cut segments with `-g 15` keyframes.
5. **Compose** — HyperFrames HTML (`templates/ad-9x16-example.html` is the approved reference: 1080×1920,
   `data-start/duration` clips, one paused GSAP timeline, captions as `.cap` clips). Load fonts from Google
   Fonts in the HTML. Keep scenes as full-frame `<section class="clip">`.
6. **QA loop** — `npx hyperframes render . -o draft.mp4 -q draft --video-frame-format png`, then
   `scripts/contact-sheet.sh draft.mp4 sheet.png <one time per scene>` and READ the sheet. Fix clipping,
   overflow, wrapping, overlaps, legibility before the final. Repeat until clean.
7. **Final** — render `-q delivery`, then `scripts/finish.sh raw.mp4 music.mp3 out.mp4 <dur>`
   (music looped + ducked under voice, -14 LUFS, edit lists neutralised for Meta).
8. **Deliver** — render one mp4 per hook variant (`<slug>-h1…h5.mp4`, shared body) and add a test plan to the manifest:
   launch all hooks in one ad set, judge on hook rate + cost per install, kill at ~2× target CPI after a fixed spend,
   next batch = 5 new hooks on the winner's body (iterate hooks, not polish; UGC fatigues in ~7–8 days).
   Write `manifest.json` (data + date, lines source, voice take, costs, version notes, lead type + hook per variant),
   keep old versions as `index-vN.html`, open the file (`open -R` in Finder / QuickTime), summarise.
9. **Captions & link** — ChatGPT writes TikTok (5 hashtags, search words in the sentence) + Instagram
   (7–9 hashtags) with the same real numbers; brand hashtags OK in organic posts; "Link profilde".
   Bio link = the project's own link page with `?p=<source>` attribution (e.g. `yourapp.com/link`).
   Then ask before posting.

## 3. Research tools — tested 2026-09-29 (don't re-evaluate)

| Tool | Verdict |
|---|---|
| **MetaAdsCollector** (`promisingcoder/MetaAdsCollector`, MIT, active) | ✅ USE. Worked first try on TR: 15 video ads in 41 s, HD media, start dates + copy counts, only talks to facebook.com. |
| **Winning Creative Tracker** (`TheMattBerman/winning-creative-tracker`, 1 commit) | Analysis engine works offline (demo report, 257/259 tests), but live data needs paid ScrapeCreators + Virlo keys. Use only its labels (hook/format/message-frame taxonomy above), not the tool. |
| **Meta Ads Competitor Tracker** (`kalilfagundes/meta-ads-competitor-tracker`, 1 commit) | Works: Docker stack (web+worker+Postgres+Garage) builds and serves on :8765; scheduled collection, keeps ads after they stop, "evergreen" ranking. Optional — only for ongoing competitor monitoring. Owner creates the admin in its wizard. |
| **Nalarin Agentic Ads Studio** | ❌ Skip: needs Gemini + fal + Kie AI + R2 (paid) and a real Facebook email/password for scraping (ban risk). |
| TrendTrack + Kie AI "copy winners" systems | ❌ Paid middlemen; the Ad Library + this skill do the same for free. |

## 4. Gotchas (each cost time once)

- zsh does not word-split `$VAR` — pass flags literally, don't build them in a variable.
- `gflow`/Flow: a refused option exits before spending credits — check the log before retrying.
- Maestro `takeScreenshot` only writes inside its own run folder; use `xcrun simctl io … screenshot`.
- "Host recording is already in progress" → `xcrun simctl shutdown` + `boot` the simulator.
- A tap right after a state change can miss (layout shifts) — wait ~1.3 s, prefer text selectors with regex (`"Takibe al.*"`).
- Headless Chrome windows can't go below ~500 px wide — screenshot at 500 px, not 390.
- Turkish `text-transform: uppercase` turns i→İ in brand names/emails — put `lang="en"` on those elements.
- Video sources for HyperFrames need dense keyframes (`-g 15`) or frames freeze on seek.
- Remote product images: some CDNs return transparent PNGs — flatten onto the card colour first.

## 5. Done means

A clean contact sheet of every scene, a final mp4 with music + normalised audio + no edit lists,
a manifest, captions saved, the file opened for the owner — and nothing posted without a yes.
