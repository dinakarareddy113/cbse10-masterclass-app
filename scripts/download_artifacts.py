import os
import urllib.request
import zipfile
import json
import shutil

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

class NoAuthRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new_req = super().redirect_request(req, fp, code, msg, headers, newurl)
        if "github.com" not in newurl:
            new_req.headers.pop("Authorization", None)
            new_req.headers.pop("authorization", None)
        return new_req

opener = urllib.request.build_opener(NoAuthRedirectHandler)

req = urllib.request.Request(run_url, headers={
    "Authorization": f"token {token}",
    "User-Agent": "Antigravity-Agent",
    "Accept": "application/vnd.github.v3+json"
})

with opener.open(req, timeout=15) as resp:
    data = json.load(resp)
    latest_run = data["workflow_runs"][0]
    artifacts_url = latest_run["artifacts_url"]

req_art = urllib.request.Request(artifacts_url, headers={
    "Authorization": f"token {token}",
    "User-Agent": "Antigravity-Agent",
    "Accept": "application/vnd.github.v3+json"
})

with opener.open(req_art, timeout=15) as resp:
    art_data = json.load(resp)
    artifacts = art_data.get("artifacts", [])

output_dir = os.path.join(os.path.dirname(__file__), "..", "build_artifacts")
os.makedirs(output_dir, exist_ok=True)

for a in artifacts:
    name = a["name"]
    download_url = a["archive_download_url"]
    zip_path = os.path.join(output_dir, f"{name}.zip")
    extract_folder = os.path.join(output_dir, name)
    os.makedirs(extract_folder, exist_ok=True)
    
    print(f"Downloading {name} ({a['size_in_bytes'] / (1024*1024):.2f} MB)...")
    req_dl = urllib.request.Request(download_url, headers={
        "Authorization": f"token {token}",
        "User-Agent": "Antigravity-Agent"
    })
    
    with opener.open(req_dl, timeout=180) as dl_resp:
        with open(zip_path, "wb") as f_out:
            shutil.copyfileobj(dl_resp, f_out)
    
    print(f"Extracting {zip_path}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
        
    print(f"Files extracted to {extract_folder}:")
    for root, dirs, files in os.walk(extract_folder):
        for file in files:
            file_path = os.path.join(root, file)
            size_mb = os.path.getsize(file_path) / (1024 * 1024)
            print(f"  -> {file} ({size_mb:.2f} MB) at {file_path}")

print("\nAll artifacts downloaded and extracted successfully!")
