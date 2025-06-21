import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import random

# Multi-color mood mapping with explanations
mood_color_map = {
    "happy": [("yellow", "Yellow promotes joy and cheerfulness."), ("pink", "Pink adds softness and warmth.")],
    "sad": [("grey", "Grey matches reflective moods."), ("blue", "Blue offers calm for emotional balance.")],
    "angry": [("blue", "Blue cools emotional intensity."), ("white", "White helps reset mental state.")],
    "stressed": [("green", "Green creates peace and calm."), ("peach", "Peach relaxes anxious energy.")],
    "relaxed": [("sage green", "Sage green nurtures a relaxed spirit."), ("peach", "Peach complements ease.")],
    "energetic": [("orange", "Orange expresses vitality."), ("red", "Red powers momentum.")],
    "motivated": [("crimson", "Crimson reflects deep drive."), ("emerald green", "Emerald boosts courage.")],
    "calm": [("sky blue", "Sky blue keeps serenity high."), ("lavender", "Lavender supports inner peace.")],
    "peaceful": [("mint", "Mint aligns with harmony."), ("sage green", "Sage tones stabilize emotions.")],
    "professional": [("black", "Black represents authority."), ("navy", "Navy adds formal depth.")],
    "caring": [("rose pink", "Rose pink conveys affection."), ("peach", "Peach warms nurturing moods.")],
    "creative": [("purple", "Purple expands imagination."), ("aqua", "Aqua sparks ideas.")],
    "confident": [("emerald green", "Emerald builds presence."), ("red", "Red fuels boldness.")]
}

# Outfit pieces including modern styles
outfit_parts = {
    "top": {
        "casual": ["graphic tee", "strapless top", "crop top"],
        "formal": ["silk blouse", "button-down shirt", "puff sleeve shirt"],
        "trendy": ["mesh top", "halter neck", "asymmetric top"],
        "stylish": ["wrap blouse", "cold shoulder top", "balloon sleeve shirt"],
        "traditional": ["embroidered kurti", "choli", "anarkali top"]
    },
    "bottom": {
        "casual": ["shorts", "jeans", "cargo pants"],
        "formal": ["trousers", "pencil skirt", "palazzos"],
        "trendy": ["mini skirt", "layered skirt", "ripped jeans"],
        "stylish": ["flare pants", "pleated skirt", "split skirt"],
        "traditional": ["lehenga", "salwar", "long ethnic skirt"]
    },
    "dress": {
        "trendy": ["mini dress", "off-shoulder one-piece"],
        "stylish": ["strapless frock", "flowy maxi"],
        "traditional": ["saree", "anarkali gown"]
    },
    "shoes": ["sneakers", "heels", "flats", "boots", "juttis", "kolhapuri"],
    "bag": ["sling bag", "backpack", "clutch", "tote", "ethnic potli"],
    "accessory": ["bracelet", "bangles", "hoop earrings", "jhumkas", "necklace", "choker"],
    "addon": ["watch", "scarf", "sunglasses", "glasses"]
}

# Get season
def get_season():
    month = datetime.datetime.now().month
    return (
        "winter" if month in [12, 1, 2] else
        "summer" if month in [3, 4, 5] else
        "monsoon" if month in [6, 7, 8] else
        "spring"
    )

# Build complete outfit
def build_full_outfit(colors, style):
    outfit = ""
    selected_colors = random.sample(colors, min(2, len(colors)))

    # Combine pieces using different colors
    top_color = selected_colors[0]
    bottom_color = selected_colors[1] if len(selected_colors) > 1 else selected_colors[0]

    # Random dress replacement for trendy or stylish
    if style in ["trendy", "stylish"] and random.choice([True, False]):
        dress = random.choice(outfit_parts["dress"][style])
        outfit += f"👗 Dress: {dress} ({top_color})\n"
    else:
        top = random.choice(outfit_parts["top"][style])
        bottom = random.choice(outfit_parts["bottom"][style])
        outfit += f"👕 Top: {top} ({top_color})\n"
        outfit += f"👖 Bottom: {bottom} ({bottom_color})\n"

    # Shoes, bag, accessories
    outfit += f"👟 Shoes: {random.choice(outfit_parts['shoes'])}\n"
    outfit += f"👜 Bag: {random.choice(outfit_parts['bag'])}\n"
    outfit += f"✨ Accessory: {random.choice(outfit_parts['accessory'])}\n"
    outfit += f"🕶️ Add-on: {random.choice(outfit_parts['addon'])}\n"

    return outfit

# Final suggestion engine
def get_final_output(moods, style):
    season = get_season()
    full_output = f"🌤️ Season: {season.title()}\n\n"
    used_colors = []
    color_reason_lines = []

    for mood in moods:
        mood = mood.strip().lower()
        if mood in mood_color_map:
            for color, reason in mood_color_map[mood]:
                if color not in used_colors:
                    used_colors.append(color)
                    color_reason_lines.append(f"💡 {mood.title()} → {color.title()}: {reason}")

    if not used_colors:
        return "⚠️ No valid moods provided."

    full_output += "\n".join(color_reason_lines) + "\n\n"
    full_output += build_full_outfit(used_colors, style)

    return full_output


# GUI setup
root = tk.Tk()
root.title("✨ Final Color Psychology Outfit Generator")
root.geometry("770x720")
root.configure(bg="#fdf8f2")

# GUI components
tk.Label(root, text="Color Psychology Outfit Generator", font=("Helvetica", 16, "bold"), bg="#fdf8f2", fg="#4b0082").pack(pady=10)
tk.Label(root, text="Enter your mood(s): (comma-separated)", font=("Arial", 12), bg="#fdf8f2").pack()
mood_input = tk.Entry(root, width=70, font=("Arial", 12))
mood_input.pack(pady=6)

tk.Label(root, text="Select your style:", font=("Arial", 12), bg="#fdf8f2").pack()
style_var = tk.StringVar(value="casual")
style_menu = ttk.Combobox(root, textvariable=style_var, values=["casual", "formal", "trendy", "stylish", "traditional"], state="readonly", font=("Arial", 12))
style_menu.pack(pady=6)

output_box = tk.Text(root, height=28, width=85, wrap="word", font=("Arial", 11))
output_box.pack(pady=10)

# Button function
def generate_output():
    moods = mood_input.get().split(",")
    style = style_var.get().lower()
    if not moods or all(m.strip() == "" for m in moods):
        messagebox.showwarning("Missing Input", "Please enter at least one mood.")
        return
    result = get_final_output(moods, style)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, result)

tk.Button(root, text="👗 Generate Outfit", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=generate_output).pack(pady=6)

root.mainloop()
