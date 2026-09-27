with open('mobile_test/index.html', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if "screen === 'math'" in line or "screen === 'chapter_hub'" in line:
            print(f"Line {i+1}: {line.strip()[:100]}")
