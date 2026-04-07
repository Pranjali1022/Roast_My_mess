"""
data.py:  All static data for Roast My Mess

"""

#  Tone prompts — sent as system prompt to Claude 
# Each tone produces a completely different style of roast
TONE_PROMPTS = {
    "savage": (
        "You are a savage, brutally honest, and extremely funny food critic roasting an IIT KGP "
        "hostel mess menu. Be ruthless but funny — roast the food, never the workers. "
        "Use Indian English slang naturally (yaar, bhai, matlab, ek toh). "
        "Keep it to 4-5 punchy lines. End with a rating like '2.5/10 — would rather eat textbook'. "
        "Make it extremely shareable."
    ),
    "mild": (
        "You are a gently disappointed but funny food critic reviewing an IIT KGP mess menu. "
        "Be sympathetic but still roast it — like a friend complaining to a friend. "
        "Indian English, relatable, 4-5 lines. End with a generous but honest rating like '5/10'."
    ),
    "poetic_tragedy": (
        "You are a dramatic Shakespearean poet roasting an IIT KGP mess menu as a great tragedy. "
        "Use flowery language, metaphors, but keep it funny. Mix in Indian cultural references. "
        "4-5 dramatic lines. End with a poetic lament and rating like '3/10 — a tragedy in five courses'."
    ),
    "iit_jhola_guy": (
        "You are a pretentious IIT KGP jhola-toting intellectual who relates everything to "
        "physics, algorithms, or existentialism while roasting the mess menu. "
        "Make references to coursework, professors, or campus life. Mix Hindi/English naturally. "
        "4-5 lines. End with a rating with academic flair like '4.2/10 — C grade, no supplementary'."
    ),
}

# Hall 
HALLS = [
    "SBP-1 Hall", "SBP-2 Hall" "LBS Hall", "RP Hall", "MMM Hall", "Nehru Hall", "VGH Hall", "LLR Hall", 
    "VS Hall", "AZ Hall", "Patel Hall", "Azad Hall", "ABV Hall", "GKH Hall", "SNIG Hall", "BRH Hall",
    "RK Hall", "Homi Bhabha Hall", "MT Hall", "RLB Hall", "SAM Hall", "BRH Hall",  "BC Roy Hall", "JCB Hall", "MS Hall", "Other",
]

# Sample menus — realistic IIT KGP mess menus 
SAMPLE_MENUS = [
    "Monday lunch: Dal, steamed rice, 2 rotis, aloo gobhi sabzi, raita (watery), boiled egg (optional), banana",
    "Tuesday dinner: Soya chunks ki sabzi, rice, roti, mixed veg curry (no veg visible), dal, pickle",
    "Wednesday lunch: Rajma (thin), chawal, puri (3), aloo sabzi, sweet dish (jalebi), buttermilk",
    "Thursday dinner: Paneer (1 piece per person), dal fry, rice, roti, bhindi fry, gulab jamun (1)",
    "Friday lunch: Kadhi, rice, roti, aloo matar, dahi, friday special — sooji halwa (small cup)",
    "Saturday dinner: Chole, bhature (2), rice, dal, salad (4 slices cucumber), ice cream (festival special)",
    "Sunday lunch: Yellow dal, rice, mix veg, puri, kheer — but ran out of kheer by 12:30 PM",
]

# Leaderboard data
LEADERBOARD = [
    {"dish": "Soya chunks ki sabzi", "hall": "LBS Hall", "days": "Mon, Tue, Thu", "roasts": 847},
    {"dish": "Mystery dal (again)",   "hall": "MMM Hall", "days": "Daily",         "roasts": 612},
    {"dish": "Watery rajma",          "hall": "RP Hall",  "days": "Wednesday",     "roasts": 389},
    {"dish": "Banana (only fruit)",   "hall": "All halls","days": "Daily",         "roasts": 281},
    {"dish": "Overcooked rice",       "hall": "AZ Hall",  "days": "Mon, Wed, Fri", "roasts": 214},
]

# Complaint data for authority dashboard 
COMPLAINT_DATA = [
    {"name": "Soya chunks ki sabzi",       "count": 847},
    {"name": "Watery dal (texture)",       "count": 612},
    {"name": "Overcooked / mushy rice",    "count": 389},
    {"name": "Repetitive menu (5+ days)",  "count": 341},
    {"name": "Banana (only fruit option)", "count": 214},
    {"name": "Cold rotis",                 "count": 178},
    {"name": "No protein variety",         "count": 156},
]

# Pre-seeded community posts 
COMMUNITY_POSTS = [
    {
        "author": "Student from LBS Hall",
        "initials": "SK",
        "time": "2 min ago",
        "tone_key": "savage",
        "likes": 142,
        "comments": 34,
        "content": (
            "The soya chunks today had the texture of a used cricket ball. I've had better meals during "
            "power cuts. The cook must have a personal vendetta against carbohydrates because the "
            "rice-to-water ratio suggested they were attempting to serve soup. 2/10 — would rather eat my GATE notes."
        ),
    },
    {
        "author": "Student from MMM Hall",
        "initials": "AR",
        "time": "18 min ago",
        "tone_key": "poetic_tragedy",
        "likes": 287,
        "comments": 61,
        "content": (
            "O dal tadka, thou hast been on this menu since orientation. Through semesters you have "
            "watched us age, watched dreams wither, watched our GPA decay — yet you remain unchanged, "
            "faithful, watery, and without cumin. You are the only constant in this chaotic universe "
            "called IIT KGP. 4/10 — a tragedy in three courses."
        ),
    },
    {
        "author": "Student from RP Hall",
        "initials": "PK",
        "time": "1 hr ago",
        "tone_key": "mild",
        "likes": 98,
        "comments": 12,
        "content": (
            "The rajma today was actually not bad! I mean, it was thin like the plot of a Bollywood "
            "sequel, and the kidney beans were playing hide and seek, but honestly after Tuesday's "
            "disaster anything tastes like a Michelin star meal. 5.5/10 — would eat again under duress."
        ),
    },
    {
        "author": "Student from Nehru Hall",
        "initials": "VN",
        "time": "3 hrs ago",
        "tone_key": "iit_jhola_guy",
        "likes": 203,
        "comments": 45,
        "content": (
            "If we model the mess dal as a graph problem, it is clearly a sparse graph — density "
            "approaching zero. The paneer allocation algorithm appears to be O(1) per hall, "
            "regardless of n students. I have submitted a formal complaint in the form of "
            "this roast. Professor Mess-wala, your time complexity is unacceptable. 3.14/10 — irrational."
        ),
    },
    {
        "author": "Student from VS Hall",
        "initials": "SM",
        "time": "5 hrs ago",
        "tone_key": "savage",
        "likes": 176,
        "comments": 28,
        "content": (
            "Today's aloo sabzi was so oily the IEEE could classify it as a petroleum reserve. "
            "The roti was so stiff I used it as my viva notes holder. Bhai, at this point the mess "
            "is doing more damage to my health than my 3 AM coding sessions. 1.5/10 — Swiggy se order."
        ),
    },
]
