with open("scratch/redesign_step2.html", encoding="utf-8") as f:
    html = f.read()

import re

pos1 = html.find("${adminHubTab === 'pdf' ? `")
sub = html[pos1:pos1+10000]

print("Matches:")
for m in re.finditer(r'adminHubTab\s*===\s*[\'"][^\'"]+[\'"]', sub):
    print(m.group(), 'at offset', m.start())

p_pipeline = sub.find("adminHubTab === 'pipeline'")
print("Offset of pipeline:", p_pipeline)
if p_pipeline != -1:
    print("Preceding 100 chars:", repr(sub[p_pipeline-100:p_pipeline]))
