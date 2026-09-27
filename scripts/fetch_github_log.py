import os
import urllib.request
import json
import sys

def get_token():
    if os.environ.get("GITHUB_TOKEN"):
        return os.environ["GITHUB_TOKEN"]
    token_file = os.path.join(os.path.dirname(__file__), "..", ".git", "token")
    if os.path.exists(token_file):
        with open(token_file, "r") as f:
            return f.read().strip()
    return ""

token = get_token()
job_id = "108683685484"
log_url = f"https://api.github.com/repos/dinakarareddy113/cbse10-masterclass-app/actions/jobs/{job_id}/logs"

class NoAuthRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new_req = super().redirect_request(req, fp, code, msg, headers, newurl)
        if "github.com" not in newurl:
            new_req.headers.pop("Authorization", None)
            new_req.headers.pop("authorization", None)
        return new_req

opener = urllib.request.build_opener(NoAuthRedirectHandler)
req = urllib.request.Request(log_url, headers={
    "Authorization": f"token {token}",
    "User-Agent": "Antigravity-Agent",
})

try:
    with opener.open(req, timeout=15) as resp:
        content = resp.read().decode("utf-8", errors="replace")
        lines = content.splitlines()
        print(f"Total log lines: {len(lines)}")
        with open("build_failure.log", "w", encoding="utf-8") as out:
            out.write(content)
        print("Wrote log to build_failure.log")
except Exception as e:
    print(f"Error: {e}")
