with open("mobile_test/index.html", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "function attemptQuestion" in l or "function resetQuestionAttempt" in l or "function toggleSolution" in l:
        print(f"Line {i+1}: {l.strip()}")
