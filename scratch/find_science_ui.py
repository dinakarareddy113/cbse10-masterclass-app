with open('mobile_test/index.html', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'selectSubject\([^\)]*\)|filterBySubject\([^\)]*\)|renderDashboard\([^\)]*\)|loadChapters\([^\)]*\)', html)
print("Function calls:", set(matches))

# Let's search where 'science' is mentioned in the UI/JS
pos = 0
while True:
    pos = html.find("'science'", pos)
    if pos == -1:
        break
    print("Match at", pos, ":", html[max(0, pos-100):min(len(html), pos+150)])
    print("-" * 40)
    pos += len("'science'")
