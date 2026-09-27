import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('mobile_test/index.html', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "function navTo" in line:
        print(f"Line {i+1}: {line.strip()}")
        for j in range(i, min(len(lines), i + 80)):
            print(f"{j+1}: {lines[j]}", end="")
        break
