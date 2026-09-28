import re

with open('mobile_test/index.html', encoding='utf-8') as f:
    content = f.read()

ids = re.findall(r'"id":\s*"(sci_ch3_[^"]+)"', content)
print(f"Total Science Ch 3 question IDs: {len(ids)}")
sections = re.findall(r'"section":\s*"([^"]+)"', content)
print(f"Unique sections in questions: {set(sections)}")

