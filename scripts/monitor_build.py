import os
import urllib.request
import json
import time
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
run_url = "https://api.github.com/repos/dinakarareddy113/cbse10-masterclass-app/actions/runs"

def fetch_json(url):
    req = urllib.request.Request(url, headers={
        "Authorization": f"token {token}",
        "User-Agent": "Antigravity-Agent",
        "Accept": "application/vnd.github.v3+json"
    })
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp)

print("Starting GitHub Actions monitoring...", flush=True)
start_time = time.time()
last_step_reported = ""

while time.time() - start_time < 480: # max 8 minutes
    try:
        runs_data = fetch_json(run_url)
        runs = runs_data.get("workflow_runs", [])
        if not runs:
            print("No runs found.", flush=True)
            break
        latest = runs[0]
        status = latest["status"]
        conclusion = latest["conclusion"]
        run_id = latest["id"]
        
        # Check job steps
        jobs_data = fetch_json(latest["jobs_url"])
        jobs = jobs_data.get("jobs", [])
        if jobs:
            j = jobs[0]
            for s in j.get("steps", []):
                step_str = f"Step '{s['name']}': status={s['status']}, conclusion={s['conclusion']}"
                if s['status'] == 'in_progress' and step_str != last_step_reported:
                    print(f"[{int(time.time() - start_time)}s] IN PROGRESS: {s['name']}", flush=True)
                    last_step_reported = step_str
                elif s['conclusion'] is not None and s['conclusion'] != 'success' and step_str != last_step_reported:
                    print(f"[{int(time.time() - start_time)}s] FINISHED: {s['name']} -> {s['conclusion']}", flush=True)
                    last_step_reported = step_str

        if status == "completed":
            print(f"\nRun #{latest['run_number']} completed with conclusion: {conclusion}", flush=True)
            
            # Fetch artifacts
            art_data = fetch_json(latest["artifacts_url"])
            artifacts = art_data.get("artifacts", [])
            print(f"Artifacts found ({len(artifacts)}):", flush=True)
            for a in artifacts:
                mb = a['size_in_bytes'] / (1024 * 1024)
                print(f"  * {a['name']} ({mb:.2f} MB)", flush=True)
                print(f"    Download URL: {a['archive_download_url']}", flush=True)
            break

    except Exception as e:
        print(f"Transient error: {e}", flush=True)
        
    time.sleep(15)

