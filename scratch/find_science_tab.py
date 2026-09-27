import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('mobile_test/index.html', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "currentTab === 'science'" in line or "currentTab == 'science'" in line or "navTo('science')" in line or "id: 'sci_" in line:
        print(f"Line {i+1}: {line.strip()[:100]}")
