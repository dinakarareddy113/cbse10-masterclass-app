with open('mobile_test/index.html', encoding='utf-8') as f:
    html = f.read()

import re
print("Length of html:", len(html))
q_idx = html.find("const questions")
if q_idx == -1:
    q_idx = html.find("questions =")
print("questions found at:", q_idx)
if q_idx != -1:
    print("Snippet:", html[q_idx:q_idx+300])
