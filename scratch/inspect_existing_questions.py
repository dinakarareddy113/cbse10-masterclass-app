with open('mobile_test/index.html', encoding='utf-8') as f:
    html = f.read()

import json, re

start_marker = "const questions = "
if start_marker not in html:
    start_marker = "questions = ["
    start_pos = html.find(start_marker) + len("questions = ")
else:
    start_pos = html.find(start_marker) + len(start_marker)

# Find end of array
end_pos = html.find(";\n", start_pos)
print("Start pos:", start_pos, "End pos:", end_pos)

# Let's inspect subjects and chapters existing in questions
# Let's see some samples
import re
subjects = re.findall(r'"subject":\s*"([^"]+)"', html)
from collections import Counter
print("Subject counts:", Counter(subjects))

chapter_ids = re.findall(r'"chapterId":\s*"([^"]+)"', html)
print("Chapter counts:", Counter(chapter_ids))
