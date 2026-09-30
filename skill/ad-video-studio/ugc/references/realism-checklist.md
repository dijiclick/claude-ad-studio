# Realism checklist (the "anti-slop" layer)

Run this on every character still and every video prompt. Each line fixes one thing viewers read as "AI" without knowing why.

## The 7 AI tells (Module 1) → the fix
| Tell | Fix in the prompt |
|---|---|
| Dead eyes / frozen face | "natural blinks, micro-expressions, eyebrows lift on '[word]', glances down then back to lens" |
| Floating product | "holds [product] in her right hand, thumb on the label, fingers wrapped naturally"; exact label text |
| Perfect lighting | ONE motivated source that fits the room ("window light from camera-left, ~5000K", "warm vanity light ~3000K") + where the shadows fall |
| Empty background | 1–2 lived-in props (clothing rack, mug, plant, car seat, tote on the chair) — not busy |
| Robot hands | keep hands simple: one holds the product/phone, the other makes one small gesture; negatives "distorted hands, extra fingers" |
| Announcer voice | fillers ("yani", "bak", "like", "literally"), (pause) marks, slightly fast friendly pace, voice described (pitch, texture) |
| Professional camera | "selfie-style iPhone 15 Pro front camera (~24 mm), 720x1280, 30 fps, titled 'IMG_8234.MOV'" |

## Skin & face
- "natural skin texture with visible pores", "slight natural shine on the T-zone" — beautiful is fine; flawless is the tell.
- One human imperfection: flyaway hairs, faint under-eye shadow, a small blemish, slightly uneven lip tint.
- Negatives: "beauty filter, skin smoothing, airbrushing, porcelain/waxy skin, pore reduction, glamour lighting".
- Stills: generate everything in ONE prompt and regenerate; multi-step edits smooth the skin and it shows once animated.
- No blown-out highlights (a white patch animates as wax).

## Camera must match the capture
- Arm's-length selfie → "subtle handheld sway and micro-jitter consistent with a selfie grip; framing drifts slightly off-center".
- Propped / mounted / tripod → "static, tiny micro-shifts from breathing".
- A selfie framing (arm visible) with "static locked-off" = uncanny. Don't mix.
- Don't list "camera shake" as a negative in a handheld prompt.

## Audio (diegetic only)
- Mic character: "recorded through the iPhone mic" / clip-on mic / wired earphones — the scene must explain clean audio.
- Room acoustics: bathroom echo, "boxy" car interior, café murmur.
- 2–3 faint location sounds (fridge hum, distant traffic, cups clinking).
- "No music, no cuts; one-take natural pacing." Music belongs in the edit, if at all (UGC usually has none).

## Product & text
- Product described like a packaging spec: container, size, colours, exact label text, logo position.
- "label text reads correctly left to right (not mirrored)".
- Strong-coloured product → "LOCKED white balance; no [colour] cast on skin".
- No on-screen text in the generation: "no subtitles, captions, watermark, text overlays, logos on screen" — captions go in the edit.

## Performance
- 5–11 beats, each tied to a word of the script ("on 'bak' she turns the phone to the lens").
- Opens already mid-action (holding the product / mid-sentence), ends on a half-smile + nod or a trailing look.

## Final pass
Run `python3 ~/.claude/skills/ad-video-studio/ugc/scripts/check_prompt.py prompt.txt --seconds N` — it flags missing layers, over-long prompts, word count vs duration and risky claims.
