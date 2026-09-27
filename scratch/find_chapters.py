with open('mobile_test/index.html', encoding='utf-8') as f:
    html = f.read()

import re
# Look for chapters or subject definitions
ch_pos = html.find("chapters =")
if ch_pos == -1:
    ch_pos = html.find("const chapters")
if ch_pos != -1:
    print(html[ch_pos:ch_pos+1000])
else:
    # search for sci_ch
    for m in re.finditer(r'sci_ch', html):
        p = m.start()
        print("Found sci_ch at", p, ":", html[p-100:p+200])
        break
