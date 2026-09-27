import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('mobile_test/index.html', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "function renderCard" in l:
        print(f"Line {i+1}: {l.strip()}")
        for j in range(i, min(len(lines), i + 100)):
            print(f"{j+1}: {lines[j]}", end="")
        break
