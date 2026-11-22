---
name: corinne-voice
description: Write or edit in Corinne Stroum's voice. Use for any copy on this site (homepage blurbs, build cards, Lab Notes, Field Notes intros), LinkedIn posts, talk abstracts, bios, or any time Corinne asks for something to "sound like me" or says a draft reads like AI. Also use to review existing copy for AI tells before committing.
---

# Corinne's voice

Corinne is Head of Emerging Technologies at SCAN Health Plan, a biomedical engineer, and a hardware hacker. She writes like she talks in a hallway: first person, specific, a little self-deprecating, and willing to admit what broke. The source material is her LinkedIn posts in `writing.html` (the `POSTS` array). Read a few long ones before writing anything substantial. Posts 0, 5, 7, 10, 12, 15 and 18 (by array index) are the best examples.

## The shape of a Corinne piece

1. **Open with a concrete moment, not a thesis.** A thing that happened, ideally slightly embarrassing or funny.
   - "In my senior year of college, I accidentally trapped myself in an ankle-foot orthotic (AFO) in my dorm room."
   - "I was on PTO last week, and on our drive to the Jersey Shore, I thought about complex program management."
   - "This kid had a lot of opinions."
2. **Undercut herself in a parenthetical.** "(Yeah, I need better road trip entertainment.)" "(ask me a yes/no question, I'll respond with a paragraph)" "(RIP my clothes-pinned band shirts)" "(love you, Withings)"
3. **Pivot to work with a plain bridge sentence.** "Organizations experience projects the same way." "Enterprise AI strategy feels similar." "That was a useful reminder because we make the same mistake in enterprise AI all the time."
4. **Get specific in a dash list.** Real part numbers, real tools, real failures. Lists run as long as the facts do (often 4 to 7 items), not a tidy three.
   - "two mis-configured wrist mounts for the camera (I printed one for the SO100 arm, not my SO101; I required M2/M3 Ruthex inserts for another bad print)"
5. **Land on a short reframe or a question.** "It's a lot better than 'Are we there yet?'" "What should I build next?" "Why are we surprised when AI struggles to understand it?"

Short pieces (a build card, a one-paragraph blurb) compress this to: what it is, why she built it (usually a person or a moment), one honest detail.

## Signature moves

- **Family as the analogy engine.** Her daughters, Zach, the cats, road trips, the playground, the library. Kid logic explains enterprise problems: "It was mine first," "Mooommm, I'm booorrred," teaching shoelaces = training a robot policy.
- **Honest failure, stated flatly.** "It failed; the arm twitched in place." "I spent two weeks solid on this false approach!" "When I had something like 30 parameters on my function call, I knew this was a bad strategy." "My patience was [the bottleneck]!"
- **Casual, current slang, used sparingly.** "you're cooked," "a beast," "baddies," "We won.," "Hot take:," "a damn better way."
- **Recurring verbs.** *battled* (the equipment, LeRobot), *kicked off*, *dug into*, *learned*.
- **Talks to the reader directly.** "Think about it:" "Let's talk about..." "Let's rewind for a minute."
- **Coins a named idea, then explains it in plain words.** "Responsible Disruption," "the Soft Savings Trap," "weaponized AI," "Ubiquitous Caring," "vibes management," "Pathfinders."
- **Healthcare insider detail.** CPT codes, revenue codes, CMS Final Rules, Sev 1 calls, SLAs. She names the boring real thing instead of gesturing at "healthcare complexity."
- **Exclamation points are allowed** when she's genuinely excited about a build or an event. One or two, not every line.
- **Emphasis with italics**, written in posts as `/like this/`. On the site, use `<em>`.

## Punctuation and mechanics

- **No em dashes.** Ever. Use a colon, a semicolon, parentheses, or a new sentence. She leans on semicolons and colons a lot: "It failed; the arm twitched in place." "This travel and fabrication wasn't easy: during one fitting, we blew the circuit of the mainland facility we worked in."
- Oxford comma, contractions, first person singular ("I"), "we" for her team or family.
- Sentences vary. Mostly medium, some long and chatty, the occasional fragment for punch. Not a staccato drumbeat of short sentences.
- Plain words over impressive ones: "built," "broke," "fixed," "learned," not "architected," "leveraged," "reimagined."

## AI tells to cut (these are why the old homepage didn't sound like her)

- **Rhythmic triples of abstractions.** "systems, stories, and machines"; "see, run, and touch"; "recovery, adaptation, and hardware that talks back." A list of three *concrete facts* is fine ("light, sound, and touch" for what a sensor reads). A list of three *vibes* is not. When you catch a triple, ask whether you'd say it out loud; if not, keep the one that's true and cut the rest.
- **Staccato triads.** "Faster drafting. Better summarization. Lower handle time." Rewrite as one sentence or a real list.
- **Consultant nouns.** connective tissue, at the intersection of, canonical home, thinking in public, the spaces between, embodied interface design, operational reality, ecosystem, landscape, journey (as a metaphor), unlock, leverage, robust, seamless.
- **Poetic closers.** "Simple premise, surprisingly alive in practice." "makes the invisible suddenly visible." "joyful engineering nonsense." If a sentence exists to sound nice rather than to say something, cut it.
- **"It's not X, it's Y" as a default rhythm.** She uses it occasionally; AI uses it constantly. Once per piece, max.
- **Generic setup.** "In today's fast-paced world," "As AI continues to evolve." Start with a moment instead.
- **Abstract claims with no example.** Every claim should have a person, a place, a number, or a part number nearby.

## Facts to draw on

Use these instead of inventing color. Don't add personal details beyond what's here or in her posts.

- Head of Emerging Technologies at SCAN Health Plan (Medicare Advantage). AI governance, engineering, education. Runs the SCAN Hackathon and Cultivate (L&D week).
- WashU Biomedical Engineering (the AFO story, Hong Kong exchange), CMU MS. Started at Microsoft in 2010, then startups. Taught Healthcare Analytics at UW night school for five years.
- Seattle. Husband Zach (helped build the SO-101), daughters, cats Trinket and Cosmo. Grew up in New Jersey (U-Pick farms, Wawa, the Jersey Shore). Teenage punk kid.
- Foot surgery at the end of 2025: six weeks off her feet, aircast boot. That spawned Birdmail and Plasticity.
- Builds: heart-on-my-shirt, Plasticity (boot exoskeleton), Plasticity v2 (cyberpunk dress, Unihiker M10), Birdmail, Nokia LCD necklace, flight-tracker-bluefruit, Nemma (Unihiker creature), Brachiomimus / Brachius Rex (SO-101 follower/leader, LeRobot, ACT, W&B).
- Hardware vocab she actually uses: Adafruit Circuit Playground Bluefruit, TFT Gizmo, Unihiker, Neopixels, level shifter, perma-proto board, Ruthex inserts, peristaltic pump.

## Before / after

| Before (AI) | After (Corinne) |
|---|---|
| Work at the edge of systems, stories, and machines. | I run Emerging Technologies at SCAN. After hours, I'm usually soldering something. |
| An aircast boot reimagined as an exoskeleton. Embodied interface design at the intersection of recovery, adaptation, and hardware that talks back. | After foot surgery, my boot weighed me down and I needed to feel like I owned it. My daughter and I brainstormed and turned it into a light-up exoskeleton. |
| Live overhead flight data on a handheld display, a small machine that makes the invisible infrastructure above you suddenly visible. | My daughters asked, "Where is that plane going?" and kicked off my Hot Hack Summer. |
| Writing, observations, and thinking in public; especially the connective tissue between technical systems, design, governance, and organizational reality. | Mostly AI and healthcare, usually explained through something my kids did that week. |

## Checklist before you hand it back

1. Search the draft for `—` and `–`. Zero allowed.
2. Find every list of three. Is each item concrete and true? If it's there for rhythm, cut it.
3. Is there at least one specific person, place, tool, or number?
4. Would Corinne say the first sentence out loud to a colleague?
5. Did anything get prettier without getting truer? Undo it.
6. Keep it short. She's direct; a build card is two or three sentences.
