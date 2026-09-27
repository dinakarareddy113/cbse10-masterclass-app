with open('mobile_test/index.html', encoding='utf-8') as f:
    html = f.read()

import json

start_pos = html.find("const questions = [")
if start_pos == -1:
    start_pos = html.find("questions = [")
    arr_str = html[start_pos + len("questions = "):]
else:
    arr_str = html[start_pos + len("const questions = "):]

end_bracket = arr_str.find("];")
json_str = arr_str[:end_bracket+1]

questions = json.loads(json_str)
print("Total questions in index.html:", len(questions))
print("Sample math question keys:", list(questions[0].keys()))
print("Sample math question:", json.dumps(questions[0], indent=2)[:500])

for q in questions:
    if q.get('subject') == 'science':
        print("Existing science question:", json.dumps(q, indent=2))
