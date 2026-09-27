import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/redesign_step2.html", encoding="utf-8") as f:
    html = f.read()

pos1 = html.find("${adminHubTab === 'pdf' ? `")
p_pipe = html.find(": adminHubTab === 'pipeline' ? `", pos1)
print("pos1:", pos1)
print("p_pipe:", p_pipe)
print("Snippet before p_pipe:", repr(html[p_pipe-100:p_pipe+50]))
