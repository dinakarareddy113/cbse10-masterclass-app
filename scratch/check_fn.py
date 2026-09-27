with open("mobile_test/index.html", encoding="utf-8") as f:
    html = f.read()

pos = html.find("function handleAdminPdfFileSelect(event) {")
print("handleAdminPdfFileSelect found at:", pos)
if pos != -1:
    print("Snippet:")
    print(repr(html[pos:pos+500]))
