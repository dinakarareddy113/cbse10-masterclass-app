import json

with open("scratch/redesign_step1.html", encoding="utf-8") as f:
    html = f.read()

with open("assets/data/ncert_science_ch1.json", encoding="utf-8") as f:
    sci_ch1_data = json.load(f)

with open("assets/data/ncert_science_ch2.json", encoding="utf-8") as f:
    sci_ch2_data = json.load(f)

print(f"Loaded Ch1 ({len(sci_ch1_data)} Qs) and Ch2 ({len(sci_ch2_data)} Qs)")

# Let's ensure the questions array in html contains both Ch1 and Ch2
q_start = html.find("let questions = [")
if q_start == -1:
    q_start = html.find("questions = [")
    q_start_len = len("questions = [")
else:
    q_start_len = len("let questions = [")

q_end = html.find("];\n", q_start)
if q_end == -1:
    q_end = html.find("];", q_start)

existing_qs = json.loads(html[q_start + q_start_len - 1 : q_end + 1])
print(f"Existing questions in HTML: {len(existing_qs)}")

# Filter out old science questions and append both Ch1 and Ch2
non_sci = [q for q in existing_qs if q.get("subject") != "science"]
all_qs = non_sci + sci_ch1_data + sci_ch2_data
print(f"New total questions: {len(all_qs)} (Non-science: {len(non_sci)}, Science: {len(sci_ch1_data) + len(sci_ch2_data)})")

new_qs_json = json.dumps(all_qs, indent=2, ensure_ascii=False)
html = html[:q_start + q_start_len - 1] + new_qs_json + html[q_end + 1:]

print("Updated questions array in HTML.")

with open("scratch/redesign_step2.html", "w", encoding="utf-8") as f:
    f.write(html)
