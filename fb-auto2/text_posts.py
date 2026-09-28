"""text_posts.py — 3-4 line toddler text posts + engagement questions for "Caught being Cute"."""

import random

POSTS = [
    ("🍼 Toddler Logic 101:",
     "They'll ignore a $50 toy and play with the box for 3 hours.",
     "Then cry when you throw the 'trash' away. 😂",
     "❓ What was YOUR kid's weirdest favorite 'toy'?"),
    ("👶 Breaking News:",
     "Local toddler declares floor is lava.",
     "Entire living room now a no-go zone. 🚨",
     "❓ What silly game does YOUR little one invent?"),
    ("🍼 A toddler's day:",
     "6 AM: Wake up screaming. 7 AM: Nap time is a scam.",
     "8 PM: Suddenly full of energy. Parents: send help. 😅",
     "❓ What time does YOUR toddler turn into a night owl? 🦉"),
    ("👶 Toddler Translation Guide:",
     "'No' = Maybe. 'Mine' = Everything. 'Again!' = 47 more times.",
     "Google Translate hasn't caught up yet. 😂",
     "❓ What's the funniest word YOUR toddler says wrong?"),
    ("🍼 Science Fact:",
     "Toddlers can hear a candy wrapper from 3 rooms away.",
     "But can't hear you calling their name right next to them. 🍬",
     "❓ True or false for YOUR house?"),
    ("👶 Today's Forecast:",
     "100% chance of tantrums with a slight chance of giggles.",
     "Umbrella (and snacks) recommended. ☔🍪",
     "❓ What's YOUR toddler's #1 tantrum trigger?"),
    ("🍼 Toddler Job Interview:",
     "'Skills: Making messes, expert negotiator (for cookies),",
     "professional early riser. Salary: unlimited cuddles.' 💼",
     "❓ What job would YOUR toddler apply for?"),
    ("👶 Warning:",
     "Never say 'just one more episode' around a toddler.",
     "They WILL hold you to it. In court. With tears. ⚖️😭",
     "❓ What promise did YOUR kid never let you forget?"),
    ("🍼 Toddler Math:",
     "1 cookie + 1 cookie = 'MORE COOKIE!' 🍪",
     "Sharing is a concept for future them.",
     "❓ Does YOUR toddler share... or is it all MINE?"),
    ("👶 Milestone Unlocked:",
     "Today my toddler learned to say 'why?'",
     "Send prayers. And coffee. Mostly coffee. ☕",
     "❓ What's the funniest 'why' YOUR kid ever asked?"),
    ("🍼 Parent Hack:",
     "Want a toddler to do something? Tell them NOT to do it.",
     "Reverse psychology: the only psychology that works. 🧠",
     "❓ What trick works on YOUR little one?"),
    ("👶 Toddler Review:",
     "'Broccoli: 0/10. Floor snacks: 10/10.",
     "Mud pies: chef's kiss.' — Every toddler ever 🤌",
     "❓ What's the grossest thing YOUR kid has eaten?"),
    ("🍼 Sleep? Never heard of her.",
     "Toddlers treat bedtime like a personal insult.",
     "Negotiations begin at 8 PM sharp. 😤",
     "❓ How long is bedtime at YOUR house? ⏰"),
    ("👶 Plot Twist:",
     "Asked my toddler to clean up. They 'cleaned' by",
     "hiding everything under the couch. Genius. 🛋️",
     "❓ What's YOUR kid's sneakiest trick?"),
    ("🍼 Toddler Fashion Week:",
     "Today's look: pajama top, rain boots, superhero cape.",
     "Iconic. Unbothered. Moisturized. In their lane. 💅",
     "❓ Show us YOUR toddler's wildest outfit combo!"),
    ("👶 Deep Thoughts:",
     "If a toddler falls in the forest and no one's around,",
     "do they still dramatically cry for an audience? 🌲",
     "❓ Biggest drama performance by YOUR little actor? 🎭"),
    ("🍼 Battery Status:",
     "Toddler: 100% at 6 AM. Parents: 2%.",
     "By noon the roles have NOT reversed. 🔋",
     "❓ When does YOUR toddler finally run out of energy?"),
    ("👶 New Rule:",
     "Never ask a toddler 'who did this?' while pointing at a mess.",
     "The answer is always the dog. Even without a dog. 🐕",
     "❓ Who gets blamed at YOUR house?"),
    ("🍼 Toddler GPS:",
     "Can find the TV remote in a messy room in 10 seconds.",
     "Cannot find shoes that are literally on their feet. 🧭",
     "❓ What's YOUR toddler weirdly good at finding?"),
    ("👶 Life Lesson:",
     "A toddler's hug can fix 99% of bad days.",
     "The other 1% needs ice cream. Science. 🍨",
     "❓ What fixes a bad day at YOUR house?"),
]

HASHTAGS = "#toddler #toddlerlife #parenting #funny #cutebaby #momlife #dadlife"


def make_post(seed: int | None = None) -> str:
    """Build one 3-4 line text post. seed rotates through posts."""
    idx = (seed or 0) % len(POSTS)
    lines = POSTS[idx]
    return "\n".join(lines) + f"\n\n{HASHTAGS}"


def post_count() -> int:
    return len(POSTS)
