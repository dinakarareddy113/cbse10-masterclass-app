import os
import urllib.request
import json

def get_token():
    if os.environ.get("GITHUB_TOKEN"):
        return os.environ["GITHUB_TOKEN"]
    token_file = os.path.join(os.path.dirname(__file__), "..", ".git", "token")
    if os.path.exists(token_file):
        with open(token_file, "r") as f:
            return f.read().strip()
    return ""

token = get_token()
url = "https://api.github.com/repos/dinakarareddy113/cbse10-masterclass-app/actions/runs"

req = urllib.request.Request(url, headers={
    "Authorization": f"token {token}",
    "User-Agent": "Antigravity-Agent",
    "Accept": "application/vnd.github.v3+json"
})

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.load(resp)
        runs = data.get("workflow_runs", [])
        if not runs:
            print("No runs found")
            exit(0)
        latest = runs[0]
        print(f"Latest Run #{latest['run_number']} (ID: {latest['id']}):")
        print(f"  Status: {latest['status']} | Conclusion: {latest['conclusion']}")
        print(f"  URL: {latest['html_url']}")

        # Fetch jobs for latest run
        jobs_url = latest['jobs_url']
        req_jobs = urllib.request.Request(jobs_url, headers={
            "Authorization": f"token {token}",
            "User-Agent": "Antigravity-Agent",
            "Accept": "application/vnd.github.v3+json"
        })
        with urllib.request.urlopen(req_jobs, timeout=10) as jresp:
            jdata = json.load(jresp)
            for j in jdata.get("jobs", []):
                print(f"Job: {j['name']} | Status: {j['status']} | Conclusion: {j['conclusion']}")
                for s in j.get("steps", []):
                    if s['status'] == 'in_progress' or s['conclusion'] is not None:
                        print(f"  - Step: {s['name']} | Status: {s['status']} | Conclusion: {s['conclusion']}")

        # Fetch artifacts
        artifacts_url = latest['artifacts_url']
        req_art = urllib.request.Request(artifacts_url, headers={
            "Authorization": f"token {token}",
            "User-Agent": "Antigravity-Agent",
            "Accept": "application/vnd.github.v3+json"
        })
        with urllib.request.urlopen(req_art, timeout=10) as aresp:
            adata = json.load(aresp)
            artifacts = adata.get("artifacts", [])
            print(f"\nArtifacts Available ({len(artifacts)}):")
            for a in artifacts:
                size_mb = a['size_in_bytes'] / (1024 * 1024)
                print(f"  * {a['name']} ({size_mb:.2f} MB)")
                print(f"    Download URL: {a['archive_download_url']}")

except Exception as e:
    print(f"Error checking actions: {e}")
