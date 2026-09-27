import json

with open('assets/data/ncert_sst_geo_ch1.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

ex = [q for q in qs if 'exercise' in q.get('exercise', '').lower()]
it = [q for q in qs if 'in-text' in q.get('exercise', '').lower()]

print(f"Total Questions Generated: {len(qs)}")
print(f"1. End-of-Chapter EXERCISES (Pages 11-12): {len(ex)} Questions")
for i, q in enumerate(ex):
    print(f"   {i+1}. Q{q.get('questionNumber')}: {q.get('text')[:75]}")

print(f"\n2. In-Text QUESTIONS & PROMPTS (Pages 1-10): {len(it)} Questions")
for i, q in enumerate(it):
    print(f"   {i+1}. [{q.get('exercise')}] {q.get('text')[:75]}")
