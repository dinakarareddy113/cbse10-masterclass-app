import re

with open("scratch/generate_science_ch1_data.py", encoding="utf-8") as f:
    content = f.read()

# Let's count how many questions are defined and their details
pattern = re.compile(r'"id":\s*"(sci_ch1_[^"]+)",\s*"chapter":[^,]+,\s*"section":\s*"([^"]+)",\s*"question_number":\s*"([^"]+)"')
matches = pattern.findall(content)
print(f"Total question matches: {len(matches)}")
for idx, (qid, sec, qnum) in enumerate(matches, 1):
    print(f"{idx:2d}. [{sec}] Q{qnum} -> {qid}")
