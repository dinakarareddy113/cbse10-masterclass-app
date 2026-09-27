import json
import re

with open("mobile_test/index.html", encoding="utf-8") as f:
    html = f.read()

# Locate questions = [ ... ];
start_idx = html.find("questions = [")
if start_idx == -1:
    print("Could not find questions = [")
    exit(1)

# Find end of array
end_idx = html.find("];\n", start_idx)
if end_idx == -1:
    end_idx = html.find("];", start_idx)

json_str = html[start_idx + len("questions = "):end_idx + 1]
existing_questions = json.loads(json_str)

print(f"Existing questions count: {len(existing_questions)}")

# Filter out old science questions (there was only 1 placeholder)
filtered_questions = [q for q in existing_questions if q.get("subject") != "science"]

with open("assets/data/ncert_science_ch1.json", encoding="utf-8") as f:
    science_questions = json.load(f)

print(f"Adding {len(science_questions)} science questions.")

all_questions = filtered_questions + science_questions
print(f"New total questions count: {len(all_questions)}")

new_json_str = json.dumps(all_questions, indent=2, ensure_ascii=False)

# Replace in html
new_html = html[:start_idx + len("questions = ")] + new_json_str + html[end_idx + 1:]

with open("mobile_test/index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Successfully updated mobile_test/index.html with all 47 science questions!")
