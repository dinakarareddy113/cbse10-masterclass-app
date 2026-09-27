with open('mobile_test/index.html', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'(\b\w+\.(?:correct|is_correct|isCorrect)\b)', html)
print("Option correctness checks in JS:", set(matches))
