with open("scratch/redesign_step2.html", encoding="utf-8") as f:
    html = f.read()

pos1 = html.find("${adminHubTab === 'pdf' ? `")
pos2 = html.find("` : `\n              <!-- Raw JSON Ingestion Pipeline Tab -->", pos1)
if pos2 == -1:
    pos2 = html.find("<!-- Raw JSON Ingestion Pipeline Tab -->", pos1)

print("Found adminHubTab === 'pdf' at:", pos1)
print("Found end of pdf tab block at:", pos2)
print("Snippet around pos2:", html[pos2-50:pos2+100])
