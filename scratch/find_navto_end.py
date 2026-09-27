with open("mobile_test/index.html", encoding="utf-8") as f:
    lines = f.readlines()

start = 7090
for i in range(start, min(len(lines), start + 300)):
    if lines[i].startswith("    }") and ("admin" in lines[i-5] or "adminHubTab" in lines[i-15] or "function" in lines[i+1]):
        print(f"navTo ends around line {i+1}: {lines[i]}")
        print("Next line:", lines[i+1])
        break
