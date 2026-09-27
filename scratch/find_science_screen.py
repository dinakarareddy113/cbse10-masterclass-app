import sys
sys.stdout.reconfigure(encoding='utf-8')
with open("mobile_test/index.html", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "screen === 'science'" in l or 'screen === "science"' in l:
        print(f"Found line {i+1}:")
        for j in range(max(0, i-5), min(len(lines), i+30)):
            print(f"{j+1}: {lines[j]}", end="")
        break
