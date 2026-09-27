import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/redesign_step2.html", encoding="utf-8") as f:
    html = f.read()

pos1 = html.find("${adminHubTab === 'pdf' ? `")
print("pos1:", pos1)

for i in range(500, 30000, 500):
    chunk = html[pos1 + i : pos1 + i + 100]
    if "adminHubTab" in chunk or "adminTarget" in chunk or "adminTargetChapter" in chunk or "admin-pipeline" in chunk or "pending.map" in chunk:
        print(f"Offset {i}: {repr(chunk[:80])}")
