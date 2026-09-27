import urllib.request

try:
    resp = urllib.request.urlopen("http://localhost:8080")
    content = resp.read().decode("utf-8")
    print("Server status:", resp.status)
    print("Content length:", len(content))
    print("Has KaTeX link:", "katex.min.css" in content)
    print("Has Science subject count:", content.count('"subject": "science"'))
except Exception as e:
    print("Error:", e)
