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

# Get latest run and job id
runs_url = "https://api.github.com/repos/dinakarareddy113/cbse10-masterclass-app/actions/runs"
req_runs = urllib.request.Request(runs_url, headers={
    "Authorization": f"token {token}",
    "User-Agent": "Antigravity-Agent",
    "Accept": "application/vnd.github.v3+json"
})
with urllib.request.urlopen(req_runs, timeout=10) as rresp:
    rdata = json.load(rresp)
    latest_run = rdata["workflow_runs"][0]
    jobs_url = latest_run["jobs_url"]

req_jobs = urllib.request.Request(jobs_url, headers={
    "Authorization": f"token {token}",
    "User-Agent": "Antigravity-Agent",
    "Accept": "application/vnd.github.v3+json"
})
with urllib.request.urlopen(req_jobs, timeout=10) as jresp:
    jdata = json.load(jresp)
    job = jdata["jobs"][0]
    job_id = job["id"]
    print(f"Fetching log for Job ID: {job_id} ({job['name']})...")

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
