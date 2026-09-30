# 29 — Prompt Patterns (Cross-Cutting Formula)

**One line:** All 19 example prompts (Grüns, Goli/NŌKT, GRWM, man-in-car, expert podcast) share one skeleton: fake-phone opening line, then an exhaustive character, then six cinematography fields, then beat-by-beat performance, then an exact ~45-word script, then diegetic-only audio, then keywords and negatives. The template below uses only fields that appear in those files.

Sources: notes 20–24.

## Master template (fill in the blanks)

The labels and phrasing come from the source prompts. `[…]` are blanks. `{optional}` blocks appear in some prompts only, and the note after each one says where.

```text
A casual, selfie-style [iPhone 13 Pro / 14 / 14 Pro / 15 / 15 Pro] front-camera vertical video (9:16) filmed [inside a parked car / in a residential kitchen / in a modern apartment bathroom / inside a well-lit bedroom] during [bright daytime], titled "IMG_[####].MOV".
Character: [Name], a [age]-year-old [ethnicity] [woman/man] with [hair: length, colour, style + one imperfection e.g. damp / flyaways], [eye colour + shape], [brows], [face shape], [nose], [lips], [skin tone + undertone] with natural skin texture showing visible pores, [build], wearing [casual wardrobe], [nails / jewelry], with [posture], [emotional baseline], and a [pitch/pace] voice with authentic speech patterns including natural filler words like "[like]" and "[literally]".
[He/She] [sits in the driver's seat / stands in front of the counter], holding [his/her] phone at arm's length at slightly high angle {or: with phone mounted on the dashboard / on a tripod}, speaking directly to the camera. In [his/her] [right/left] hand [he/she] holds [product: container type, size, colours, exact label text, logo/icon]. [Lived-in background detail].
[His/Her] tone is [conversational but persuasive], delivering [a product review / testimonial / objection-handling monologue] for [product]. The atmosphere feels [intimate and authentic] — like [situational simile].

Cinematography (Simulating UGC):
Camera Shot: Medium close-up from [slightly above eye level], [slightly off-center], framed from mid-chest up.
Lens & DOF: [phone model] front camera (~24 mm equivalent), deep depth of field keeping [subject] and [background] in focus.
Camera Motion: Subtle handheld sway and micro-jitter consistent with a selfie grip; more pronounced movement when [he/she] gestures with the product. {or: Static … consistent with a [dashboard phone mount / tripod]; subtle micro-shifts from breathing}
Lighting: [one light source that makes sense for the location, plus where its highlights and shadows fall].
Color & Grade: [phone model] HDR auto-tone; [palette]; natural skin texture with visible pores; no filters.
Resolution & Aspect Ratio: 720x1280, 30 fps, vertical. Filename realism: "IMG_[####].MOV" metadata visible on internal capture simulation

Subject Action & Performance:
- Opens [already holding product / with direct eye contact, eyebrows raised]
- [Deliberately angles product so "[logo]" is clearly legible and in sharp focus]
- [Gesture/expression tied to a word: on the word "[X]" …]
- Maintains direct eye contact, natural blinks; occasional glance [down at product / to the side] then back
- [Leans in on key line]
- Finishes with [knowing half-smile + nod / trailing off expression]

Dialogue (Exact Script):
"[~30–55 words: hook first line, casual fillers, may end on '...' or include (pause)]"

Audio & Ambience (Diegetic Only):
Recorded through [phone model] mic — clear front-facing voice with [room acoustics: bathroom echo / "boxy" car interior / kitchen reverb]. Faint background ambience: [2–3 location sounds]. No music, no cuts; one-take natural pacing.

{Skin Texture & Realism Requirements: CRITICAL: … Absolutely NO artificial smoothing, NO beauty filter look, NO plastic/porcelain/waxy skin appearance, NO AI-typical over-smoothed skin.}   ← Grüns V2–V4
{Color Consistency Requirements: [product colour] WITHOUT casting [colour] reflected light onto subject's face … No color drift …}   ← Grüns V4, strongly coloured product

UGC Authenticity Keywords:
smartphone selfie, handheld realism, [setting], [lighting], influencer-style monologue, direct-to-camera, product review, raw unfiltered TikTok aesthetic, real voice, micro hand jitters, single-take.

{Quality Control Negatives: subtitles, captions, watermark, text overlays, words on screen, … distorted hands, … professional color grading, cinematic look, studio lighting, makeup artist styling, scripted stiffness, …}   ← Goli Emma, man-in-car V2
{API parameters from the course (Sora-era, ignore for Veo 3.1): size 720x1280 / seconds 8 / style raw / stylize 0}   ← man-in-car V2
```

**Format variants that change the defaults:**

- **GRWM / tutorial:** static tripod, ring light plus window light, "subtle smoothing" allowed, and timestamped application steps (`0-1s … 8-9s`).
- **Expert podcast:** a pro mirrorless camera "cropped" to 9:16, eyeline to the mic rather than the lens, three-point light, "2-3 jump cuts", and a music bed at -25dB. This is the only format that allows music and cuts.

## Recurring realism phrases (verbatim)

**Capture and device**
- `A casual, selfie-style iPhone [model] front-camera vertical video (9:16)`
- `titled "IMG_4812.MOV"` / `Filename realism: "IMG_8234.MOV" metadata visible on internal capture simulation`
- `(~24 mm equivalent)`
- `720x1280, 30 fps, vertical`
- `iPhone 14 HDR auto-tone` / `authentic smartphone color science`
- `with subtle natural compression artifacts characteristic of phone camera recording`
- `Posted on TikTok in 2025` / `raw unfiltered TikTok aesthetic posted on TikTok in 2024`
- `--stylize 0` / `--style raw` (no evidence of any effect; Veo ignores them)

**Camera and framing**
- `Subtle handheld sway and jitter consistent with a selfie grip`
- `Constant subtle handheld sway and micro-jitter consistent with arm's-length selfie grip`
- `more pronounced movements when she gestures with the product`
- `The framing is centered but occasionally drifts slightly off-center as she moves.`
- `slightly off-center right in a rule-of-thirds composition`
- `occasional minor vertical drift as arm naturally tires`
- `Static with minimal vibration, consistent with a dashboard phone mount; subtle micro-shifts from his breathing or the car settling.`

**Skin and look**
- `natural skin texture with visible pores … no filters`
- `natural skin texture with visible pores and realistic dewy shine; no filters`
- `Absolutely NO artificial smoothing, NO beauty filter look, NO plastic/porcelain/waxy skin appearance, NO AI-typical over-smoothed skin.`
- `very subtle natural blemishes` / `natural flyaways and slightly messy texture` / `nude lip color with slightly uneven application`
- `LOCKED white balance throughout entire clip preventing any color drift`

**Performance**
- `She maintains direct, engaging eye contact with the camera lens, blinking naturally.`
- `Occasional glances down at product then back to camera`
- `occasionally shifts his gaze slightly left or right and tilts his head for emphasis, reinforcing the unscripted feel`
- `Raises eyebrows dramatically on the word "expensive"`
- `Mid-sentence, he leans slightly closer to the … camera`
- `finishes … with a knowing half-smile and a conclusive nod`
- `hands entering frame from bottom` / `hands moving in and out of the bottom of the frame`
- `slight hand tremor from arm fatigue`
- `Deliberately angles and holds the packet steady … clearly legible and in sharp focus for several seconds`

**Audio**
- `Audio & Ambience (Diegetic Only)`
- `No music, no cuts; one-take natural pacing.`
- `noticeable, realistic room echo and reverb from the hard bathroom surfaces`
- `slightly contained, "boxy" acoustic quality of a car interior`
- `very low-level ambient hum of car cabin with electronics in accessory mode, no engine noise`
- `a distant muffled traffic hum, an occasional bird chirp from outside, and the subtle sound of air movement from a cracked window`
- `Very faint ambient kitchen hum barely audible in background (refrigerator or HVAC)`
- `occasional soft rustle of fabric from … shirt movement or hair shifting`

**Atmosphere similes**
- `like she's sharing an exciting new find with a close friend on a video call`
- `like she's sharing a personal secret or insider tip before heading to run errands`
- `like she pulled over just to record this message because she couldn't wait to share it`
- `like he's breaking the fourth wall to share a crucial family secret`
- `like she's responding directly to viewer comments and addressing concerns head-on`

**Keywords line (core, repeated almost everywhere)**
- `smartphone selfie, handheld realism, … influencer-style monologue, direct-to-camera, product review, raw unfiltered TikTok aesthetic, real voice, … micro hand jitters, single-take`

## Typical numbers

| Item | Values seen |
|---|---|
| Aspect / resolution / fps | 9:16, 720x1280, 30 fps (every prompt) |
| Lens | "~24 mm equivalent" (iPhone 13 Pro: "~23mm"; podcast: "35mm prime") |
| Clip length stated | 8 s (`seconds: 8`, man-in-car V2); 12 s ("12-second duration", Grüns V4); timelines of 0–9 s (GRWM V3) and 0–11 s (podcast V1) |
| Dialogue, phone UGC | 32 words (GRWM), 45 (Goli Emma), 46 (Ava), 48 (man-in-car), 50 (Grüns daughter), 53 (NŌKT V5). **Typical: ~45–50 words.** |
| Dialogue, podcast | 99 words (V1) → trimmed to 61 (V2) |
| Prompt length | Short form ~370–700 words (showcased Goli, Ava, man-in-car, GRWM V1, NŌKT V4/5, podcast V2); long form ~1,050–1,770 words (Grüns V2–V5, Goli Emma V1, GRWM V3, podcast V1) |
| Performance beats | 5–11 bullets or numbered steps |

## Do / Don't (from the files)

**Do** (the six Pro Tips appear verbatim in the Grüns, man-in-car and podcast files; the rest is observed practice):

- Use imperfect framing (slightly off-center).
- Include natural blinks and micro-expressions.
- Add authentic verbal fillers ("like," "um," "you know").
- Specify visible imperfections (damp hair, natural skin texture) / (flyaway hairs, natural skin texture).
- Reference specific phone models for technical accuracy.
- Keep lighting motivated and realistic to location.
- Give a fake camera-roll filename (`IMG_####.MOV`) and the 720x1280/30 fps spec.
- Describe the product like a packaging spec (size, colours, exact label text, logo), and add one beat where the logo is held up "clearly legible".
- Tie gestures and expressions to specific words in the script.
- List 2–3 quiet location sounds and state "No music, no cuts; one-take".
- Add one lived-in prop (child's car seat, sun visor down, delivery boxes).
- If the product is strongly coloured, lock white balance and forbid colour cast on skin (Grüns V4).
- Reuse one template across brands by swapping the product, the dialogue and the negatives (Goli V3 → Ballerina Farms).

**Don't** (from the negatives lists):

- Subtitles, captions, watermark, text overlays, words on screen, logo overlays, animated graphics.
- "professional color grading, cinematic look, studio lighting, makeup artist styling, scripted stiffness, unnatural pauses".
- "floating products, unnatural product placement", "distorted hands", "excessive camera shake", "oversaturation".
- BEAUTY FILTER, SKIN SMOOTHING, AIRBRUSHING, FACE TUNE, PORCELAIN SKIN, PORE REDUCTION, GLAMOUR LIGHTING.

**Watch for** (inconsistencies found in the source prompts, not instructor advice):

- Keywords that contradict the rig: "handheld realism, micro hand jitters" on a dashboard or tripod shot (fixed in man-in-car V2); "no jump cuts" next to requested jump cuts (podcast V2).
- A "Diegetic Only" header on a prompt that asks for music (podcast V2).
- A filename or format that disagrees with itself: `.HEIC` vs `.MOV`, "1080p" vs "720x1280" (GRWM V3).
- A character age that doesn't fit the script (a 23-year-old with a "teenage daughter", Grüns V2).
- A brand name in the dialogue that doesn't match the product described (Nokt vs "GOLI", showcased Goli prompt).
- A dialogue line referenced by an action beat but missing from the script (NŌKT V4).
