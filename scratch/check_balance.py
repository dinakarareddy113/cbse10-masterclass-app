with open("mobile_test/index.html", encoding="utf-8") as f:
    html = f.read()

# Check script blocks
script_start = html.find("<script>")
script_end = html.rfind("</script>")
js_code = html[script_start + 8 : script_end]

# Basic syntax checks
braces = 0
brackets = 0
parens = 0

# Count balance outside strings
in_str = None
escape = False
errors = []

for idx, ch in enumerate(js_code):
    if escape:
        escape = False
        continue
    if ch == '\\':
        escape = True
        continue
    if in_str:
        if ch == in_str:
            in_str = None
        continue
    else:
        if ch in ["'", '"', '`']:
            in_str = ch
        elif ch == '{':
            braces += 1
        elif ch == '}':
            braces -= 1
        elif ch == '[':
            brackets += 1
        elif ch == ']':
            brackets -= 1
        elif ch == '(':
            parens += 1
        elif ch == ')':
            parens -= 1

print(f"Braces balance: {braces}")
print(f"Brackets balance: {brackets}")
print(f"Parens balance: {parens}")
print("Currently in string:", in_str)
