"""video_captions.py — Trend-style funny captions for "Caught being Cute".

Each video gets a caption written for WHAT IS ACTUALLY IN IT (baby-POV voice,
the format trending on reels right now), plus a comment-driving question,
hashtags and follow signoff. Clean family fun: no medical, political, or risky content.
"""

import random

# Per-video hooks, keyed by filename. Written for the actual clip content.
CAPTIONS = {
    # --- original pack (baby-1..32) ---
    "baby-1.mp4": "POV: dinner is served AND the dog is my bodyguard 🍼🐶",
    "baby-2.mp4": "New bike day hits different when you're 2 😎🚲",
    "baby-3.mp4": "That giggle that fixes everything 🥹😂",
    "baby-4.mp4": "Eating with my best friend watching 👀🐶",
    "baby-5.mp4": "Playtime with mom = best time 💛",
    "baby-6.mp4": "Mom's arms = my happy place 😂💛",
    "baby-7.mp4": "Me, mom, and the dog. The dream team 🐶👶",
    "baby-8.mp4": "Vroom vroom! Licensed driver (almost) 🏍️😂",
    "baby-9.mp4": "Milk drunk and feeling myself 🍼💃",
    "baby-10.mp4": "Bedtime squad assemble! 🛏️🐶",
    "baby-11.mp4": "Toy review by your favorite critic 🧸⭐",
    "baby-12.mp4": "That laugh is pure medicine 😂💛",
    "baby-13.mp4": "Just hanging with my humans 🐶👶",
    "baby-14.mp4": "Toys > everything. Don't @ me 🧸",
    "baby-15.mp4": "Bouncy castle? I AM the bouncy castle 😂",
    "baby-16.mp4": "Kisses from mom hit different 🥹💋",
    "baby-17.mp4": "Dad's gym = lifting me 🏋️😂",
    "baby-18.mp4": "Fashion show starring yours truly ✨",
    "baby-19.mp4": "Snack time with an audience 🍼🐶",
    "baby-20.mp4": "Dad's little sidekick 💛",
    "baby-21.mp4": "Smile for the camera 📸😊",
    "baby-22.mp4": "Same dog, same cuteness, different day 🐶",
    "baby-23.mp4": "Mom's my favorite playmate 💛",
    "baby-24.mp4": "Yellow bib = main character energy 💛✨",
    "baby-25.mp4": "Selfie with mom! Say cheese 📸😂",
    "baby-26.mp4": "Book club meeting in session 📚👶👶",
    "baby-27.mp4": "Family game night champions 🏆",
    "baby-28.mp4": "Those eyes see everything 👀✨",
    "baby-29.mp4": "Safe in dad's arms 🥹💛",
    "baby-30.mp4": "New here. Be nice 🥹👶",
    "baby-31.mp4": "Dad and me against the world 💛",
    "baby-32.mp4": "Princess mode: ON 👸✨",
    # --- funny pack (baby-33..42) ---
    "baby-33.mp4": "Mickey Mouse is TIRED 😴🐭",
    "baby-34.mp4": "That side-eye when mom says 'one more bite' 🙄😂",
    "baby-35.mp4": "Getting dressed is a full workout 😅👕",
    "baby-36.mp4": "Got milk? 🥛😂",
    "baby-37.mp4": "DJ Baby in the house! 🎧😂",
    "baby-38.mp4": "Fish face Friday 🐟😂",
    "baby-39.mp4": "When you hear the snack bag open 😳🍪",
    "baby-40.mp4": "Pure happiness is a balloon 🎈💛",
    "baby-41.mp4": "Crawling + giggling = cardio 😂",
    "baby-42.mp4": "That grin says 'I did it and I'd do it again' 😏😂",
}

GENERIC_HOOKS = [
    "This little one is pure comedy gold! 👶😂",
    "Nobody does funny like a toddler! 👶🤣",
    "Watch till the end — the giggle got me! 👶💛",
    "Tag someone who was exactly like this as a baby! 👶😅",
    "Toddlers: 0% coordination, 100% entertainment 👶🎬",
    "If cuteness was a crime, this one's guilty! 🥺👶",
]

QUESTIONS = [
    "Which moment made you laugh the most? 😂👇",
    "Rate this cuteness from 1 to 10! 🥺",
    "Tag a friend who needs this laugh today! 👇",
    "What should this little star do next? Tell us! 💬",
    "Team Grumpy or Team Giggles? Pick a side! 😂",
    "Where are you watching from? 🌍",
    "Have you ever seen anything cuter? 😍",
    "Should we post one of these every day? Say YES! 👶",
]

HASHTAG_SETS = [
    "#funnybabies #viral #fyp #cutebaby #memes",
    "#babyreels #funnyvideos #comedy #lol #trending",
    "#funny #toddler #cutenessoverload #viralvideo #fyp",
    "#lol #baby #funnyreels #memes #dailylaugh",
    "#cutebaby #funnykids #comedyreels #viral #wholesome",
]

SIGNOFFS = [
    "Follow Caught being Cute for daily giggles! 👶💛",
    "New funny clips daily — follow so you don't miss it! 🔔👶",
    "Follow for your daily dose of cute! 🥺👶",
]

MUSIC_CREDIT = "🎵 Music: Kevin MacLeod (incompetech.com)"


def get_hook(filename: str, episode: int) -> str:
    """Per-video hook if we have one, else a stable generic fallback."""
    if filename in CAPTIONS:
        return CAPTIONS[filename]
    rng = random.Random(episode)
    return rng.choice(GENERIC_HOOKS)


def make_title(filename: str, episode: int) -> str:
    return get_hook(filename, episode)


def make_caption(filename: str, episode: int, music_credit: bool = True) -> str:
    """Build one full caption for a specific video file."""
    rng = random.Random(hash(filename) % (10 ** 8))
    hook = get_hook(filename, episode)
    question = rng.choice(QUESTIONS)
    tags = rng.choice(HASHTAG_SETS)
    signoff = rng.choice(SIGNOFFS)
    credit = f"\n{MUSIC_CREDIT}\n" if music_credit else "\n"
    return (
        f"{hook}\n\n"
        f"{question}\n\n"
        f"{signoff}"
        f"{credit}\n"
        f"{tags}"
    )
