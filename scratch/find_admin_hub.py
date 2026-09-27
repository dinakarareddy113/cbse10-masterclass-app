with open('mobile_test/index.html', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if "adminHubTab === 'pdf'" in line or 'adminHubTab == "pdf"' in line:
            print(f"Line {i+1}: {line.strip()[:100]}")
