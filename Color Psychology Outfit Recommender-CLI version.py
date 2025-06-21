import random
import datetime
import textwrap

# Mood to color psychology mapping
mood_color_dict = {
    "happy": "yellow",
    "sad": "grey",
    "angry": "red",
    "stressed": "blue",
    "relaxed": "green",
    "energetic": "orange",
    "motivated": "crimson",
    "calm": "sky blue",
    "peaceful": "sage green",
    "professional": "black",
    "serious": "navy blue",
    "caring": "rose pink",
    "soft": "peach",
    "creative": "purple",
    "confident": "emerald green"
}

# Outfit elements per color
color_outfit_dict = {
    "yellow": ["sundress", "cropped tee", "floral top"],
    "grey": ["oversized hoodie", "sweatpants", "woolen coat"],
    "red": ["leather jacket", "bodycon dress", "statement blazer"],
    "blue": ["denim jacket", "kurti", "cool-toned tee"],
    "green": ["linen shirt", "cargo pants", "kurta"],
    "orange": ["joggers", "festival jacket", "sunset shirt"],
    "black": ["blazer", "pencil skirt", "power suit"],
    "pink": ["cropped sweater", "frill top", "heart tee"],
    "crimson": ["slim-fit shirt", "fashion blazer", "fusion outfit"],
    "sky blue": ["pastel kurta", "cotton shirt", "hoodie"],
    "sage green": ["khadi kurta", "relaxed trousers", "zen hoodie"],
    "navy blue": ["power blazer", "semi-formal dress", "turtleneck"],
    "peach": ["cardigan", "cute tee", "flowy top"],
    "rose pink": ["sweetheart top", "traditional kurti", "lace blouse"],
    "purple": ["boho dress", "graphic tee", "cape top"],
    "emerald green": ["suit", "high-fashion shirt", "formal dress"]
}

# Fashion quotes or tips
fashion_quotes = [
    "👗 'Fashion is the armor to survive the reality of everyday life.' – Bill Cunningham",
    "🧥 'Style is a way to say who you are without having to speak.' – Rachel Zoe",
    "👜 Tip: Pair bold colors with neutrals to balance your outfit!",
    "👠 Tip: Footwear defines the mood. Choose wisely.",
    "👒 Fashion Hack: Accessorize with intention, not abundance."
]

# Mood tone classifier
positive_moods = {"happy", "relaxed", "motivated", "peaceful", "caring", "calm", "creative", "confident"}
negative_moods = {"sad", "angry", "stressed", "serious"}

# Season classifier
def get_current_season():
    month = datetime.datetime.now().month
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "summer"
    elif month in [6, 7, 8]:
        return "monsoon"
    else:
        return "spring"

# Mood analysis engine
def analyze_mood(moods):
    color_scores = {}
    for mood in moods:
        mood = mood.strip().lower()
        color = mood_color_dict.get(mood)
        if color:
            color_scores[color] = color_scores.get(color, 0) + 1
    return sorted(color_scores.items(), key=lambda x: x[1], reverse=True)

# Outfit composer
def suggest_outfit(color, style, season):
    items = color_outfit_dict.get(color, ["basic shirt"])
    accessory = random.choice(["shoes", "scarf", "bag", "watch", "glasses"])
    bottom = random.choice(["jeans", "palazzos", "skirt", "trousers", "leggings"])
    
    outfit = f"{random.choice(items)} with {bottom} and matching {accessory}"
    style_note = f"{style.capitalize()} look"
    season_note = f"✔️ Season: {season.title()}"

    emoji_palette = "🎨👚👖👠🧢👜"
    return f"\n{emoji_palette} Outfit Suggestion for {color.title()}:\n- {outfit}\n- {style_note}\n- {season_note}"

# Moodboard emoji suggestion
def emoji_moodboard(moods):
    emoji_map = {
        "happy": "😊", "sad": "😢", "angry": "😡", "stressed": "😰",
        "relaxed": "😌", "energetic": "⚡", "motivated": "🚀", "calm": "🌿",
        "peaceful": "🕊️", "professional": "💼", "serious": "🤔",
        "caring": "💖", "soft": "🌸", "creative": "🎨", "confident": "🦁"
    }
    return ''.join([emoji_map.get(m.strip().lower(), '🤔') for m in moods])

# Main engine
def fashion_recommender():
    print("\n👗 Welcome to the *Color Psychology Outfit Recommender 2.0* 👠")
    print("-------------------------------------------------------------\n")
    
    while True:
        # Input mood(s)
        mood_input = input("🌟 Enter your mood(s) (comma-separated, e.g., happy, stressed): ").strip()
        if not mood_input:
            print("⚠️ Please enter at least one mood.\n")
            continue
        
        moods = [m.strip().lower() for m in mood_input.split(',')]
        print("🧠 Moodboard:", emoji_moodboard(moods))

        # Analyze mood tone
        pos = sum(1 for m in moods if m in positive_moods)
        neg = sum(1 for m in moods if m in negative_moods)
        tone = "Positive" if pos >= neg else "Grounded"
        
        # Input style preference
        style = input("👗 Preferred style? (casual/formal/traditional/trendy): ").strip().lower()
        if style not in ["casual", "formal", "traditional", "trendy"]:
            style = "casual"

        season = get_current_season()
        mood_colors = analyze_mood(moods)

        if not mood_colors:
            print("⚠️ None of the moods matched. Defaulting to blue.")
            mood_colors = [("blue", 1)]

        print(f"\n🧭 Detected Mood Tone: {tone}")
        print(f"🌸 Season: {season.title()}\n")

        # Suggest outfits for top 2 colors
        for color, _ in mood_colors[:2]:
            print(suggest_outfit(color, style, season))

        print("\n🧵 Fashion Nugget:")
        print(textwrap.fill(random.choice(fashion_quotes), width=70))
        
        again = input("\n🔁 Want to try with a different mood? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\n💫 Thank you for using the Color Psychology Outfit Recommender 2.0 💃")
            break

# Run
if __name__ == "__main__":
    fashion_recommender()
