import urllib.request
import re

with open("mobile_test/index.html", encoding="utf-8") as f:
    html = f.read()

print("HTML size:", len(html))

# Check required markers
checks = [
    ("scienceChapters defined", "const scienceChapters = [" in html),
    ("sstChapters defined", "const sstChapters = [" in html),
    ("scienceCh1MasterQuestions", "const scienceCh1MasterQuestions = " in html),
    ("scienceCh2MasterQuestions", "const scienceCh2MasterQuestions = " in html),
    ("adminTargetSubject", "adminTargetSubject" in html),
    ("adminTargetClass", "adminTargetClass" in html),
    ("adminDetectedMeta", "adminDetectedMeta" in html),
    ("setAdminCatalogTab", "function setAdminCatalogTab" in html),
    ("changeAdminTargetSubject", "function changeAdminTargetSubject" in html),
    ("changeAdminTargetClass", "function changeAdminTargetClass" in html),
    ("generateSampleQuestionsForChapter sci2", "sci_ch_02_acids_bases_salts" in html),
    ("publishPdfQuestionsLive", "function publishPdfQuestionsLive" in html),
    ("exportGeneratedJson", "function exportGeneratedJson" in html)
]

for name, passed in checks:
    print(f"  {name}: {'PASS' if passed else 'FAIL'}")

# Verify server response
try:
    resp = urllib.request.urlopen("http://localhost:8080")
    print("\nLocalhost 8080 HTTP status:", resp.status)
    content = resp.read().decode('utf-8')
    print("Localhost 8080 content size:", len(content))
except Exception as e:
    print("HTTP test notice:", e)
