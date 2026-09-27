import json
import re

with open("assets/data/ncert_science_ch1.json", encoding="utf-8") as f:
    sci_ch1_data = json.load(f)

with open("assets/data/ncert_science_ch2.json", encoding="utf-8") as f:
    sci_ch2_data = json.load(f)

with open("mobile_test/index.html", encoding="utf-8") as f:
    html = f.read()

print("Loaded master datasets:")
print(f"  - Science Ch1: {len(sci_ch1_data)} questions")
print(f"  - Science Ch2: {len(sci_ch2_data)} questions")

# Let's inspect where mathChapters is declared
math_ch_pos = html.find("const mathChapters = [")
print("mathChapters found at:", math_ch_pos)

# We will define scienceChapters and sstChapters right after mathChapters
