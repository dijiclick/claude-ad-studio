# Finding winning ads (course Module 2 + static-ads lesson + member call)

Rule zero: **never start from your own idea.** An ad that someone keeps paying for is proof of a working hook, angle and pacing. Copy its *structure*; the words, footage and brand assets stay yours.

## Where to look (in this order)
| Source | How | Winner signal |
|---|---|---|
| **Your own past winners** | Your ad account: sort by spend / cost per result | Best reference of all — already proven on your audience, ~1/50th the cost to remake with AI |
| **Meta Ad Library** (facebook.com/ads/library) | Search competitors' pages → "All ads" → video. Automated: `scripts/research.py <out> --country XX --page "<competitor>" --query "<words>"` (free, no key) | **Running 30+ days** ("90% of these are winners" — course). Several copies of the same creative running = they're scaling it |
| **Kalo Data** (kalodata.com) | Search the product category → sort by **highest spend** → filter **UGC** format → download the top videos | Spend rank |
| **TikTok** | Scroll for raw, creator-style videos (not polished brand ads) in your niche; save anything with very high engagement | Views/likes/comments far above the account's normal |
| **Spy tools** | AdSpy, Tyver (tyver.io) | Longevity + reach |
| **Twitter/X + Ad Library for statics** | For image ads: high impressions, active **1–2+ weeks** | Collect 100, not 10 (`100-winning-static-ads/` folder) |

Where to aim: aggressive direct-response advertisers (affiliate-heavy brands) teach more than brand-led ones — they only keep what converts. Copy the *mechanics*, not their claims (see guardrails).

## Green flags → easy to clone, high hit rate
One clear idea · clear face in the first frame · natural lived-in lighting · visible product interaction · conversational delivery · simple relatable background · direct eye contact · iPhone quality.

## Red flags → skip
Professional production · no visible face · overly scripted · complex scenes or fast cuts · product hard to see.

## Log each winner (Video Analysis Template)
```
● Video ID / link · Duration (s) · Platform (TikTok / FB / IG) · Days running
● The Big Idea: the single core message
● Lead type: Promise / Problem-Solution / Secret / Story / Objection / Live proof
● Setting: location · lighting (window / overhead / golden hour)
● Character: age/gender · energy (calm / excited / casual)
● Product interaction: how held · when shown (throughout / at 3 s …)
● Delivery: tone (conversational / energetic / relaxed)
● Hook (first 3 s): exact words + action
● Why it works: raw authenticity? bold promise? relatable problem?
```
Then run `ugc/scripts/deconstruct_video.py` on the top 1–3 for the beat timing (when the hook lands, when the product/proof appears, time to CTA).

## Turn 10–20 winners into a template
Write one pattern summary across your top 10–20 references — dominant lead type, setting, lighting, energy, talking speed, when the product appears, time to CTA. Example shape:
> "Most winning [category] UGC uses a Problem-Solution lead. It opens on a relatable complaint in the first 2 s, in a [setting] with [light]. The creator holds the product at chest level, calm and conversational, and shows the label at the 3-second mark."

That summary is the default template for the first batch of tests.

## Smart shortcuts (member call)
- **Clone big-brand winners into other markets:** take a winner that's proven in the US/UK, adapt and translate it (Turkish, Arabic, German…) — the same creative is often untested there.
- Low budget → avoid the most saturated market; start where CPMs are lower.
- Re-check the winners list every week — UGC fatigues in ~7–8 days, so the pipeline of references never stops.
