with open("mobile_test/index.html", encoding="utf-8") as f:
    html = f.read()

pos = html.find("function startAdminPdfQaGeneration() {")
pos_end = html.find("const scienceCh1MasterQuestions = ", pos)
print("pos:", pos)
print("pos_end:", pos_end)
print("Snippet before pos_end:", repr(html[pos_end-50:pos_end]))
