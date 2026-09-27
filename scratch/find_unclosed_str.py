with open("mobile_test/index.html", encoding="utf-8") as f:
    html = f.read()

script_start = html.find("<script>")
script_end = html.rfind("</script>")
js_code = html[script_start + 8 : script_end]

lines = js_code.split("\n")
in_str = None
escape = False
in_block_comment = False

for line_num, line in enumerate(lines, 1):
    i = 0
    while i < len(line):
        ch = line[i]
        if in_block_comment:
            if line[i:i+2] == '*/':
                in_block_comment = False
                i += 2
                continue
            i += 1
            continue
        
        if escape:
            escape = False
            i += 1
            continue

        if ch == '\\':
            escape = True
            i += 1
            continue

        if in_str:
            if ch == in_str:
                in_str = None
            i += 1
            continue
        else:
            if line[i:i+2] == '//':
                break # rest of line is comment
            if line[i:i+2] == '/*':
                in_block_comment = True
                i += 2
                continue
            if ch in ["'", '"', '`']:
                in_str = ch
            i += 1

    if in_str in ["'", '"']:
        print(f"Unclosed string {in_str} on line {line_num}: {line.strip()[:100]}")
        break

print("Finished scanning lines. in_str:", in_str)
