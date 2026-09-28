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
repo = "dinakarareddy113/cbse10-masterclass-app"
tag_name = "v1.0.0"
release_name = "CBSE Class 10 Masterclass Exam Prep v1.0.0"
body = """### CBSE Class 10 Masterclass Exam Prep - Android APK Release

Official verified build compiled via GitHub Actions CI/CD.

#### Included Packages:
- **`app-release.apk` (23.8 MB)**: Optimized release build (Recommended for student devices).
- **`app-debug.apk` (147.6 MB)**: Debug build with symbol tables for inspection.

#### Features Included:
- Rigorous NCERT question isolation (exercises and questions sections only).
- Formula and chemical notation rendering (LaTeX / subscript formatting).
- Offline-first SQLite local persistence.
- Role-based views (Student Exam Mode & Admin Hub).
"""

headers = {
    "Authorization": f"token {token}",
    "User-Agent": "Antigravity-Agent",
    "Accept": "application/vnd.github.v3+json"
}

# 1. Create or get Release
release_url = f"https://api.github.com/repos/{repo}/releases"
payload = {
    "tag_name": tag_name,
    "target_commitish": "main",
    "name": release_name,
    "body": body,
    "draft": False,
    "prerelease": False
}

try:
    req = urllib.request.Request(release_url, data=json.dumps(payload).encode("utf-8"), headers=headers)
    with urllib.request.urlopen(req) as resp:
        rel_data = json.load(resp)
        print(f"Release created successfully: {rel_data['html_url']}")
        upload_url_template = rel_data['upload_url']
except urllib.error.HTTPError as e:
    if e.code == 422: # Already exists
        print("Release already exists, fetching existing release...")
        req = urllib.request.Request(f"https://api.github.com/repos/{repo}/releases/tags/{tag_name}", headers=headers)
        with urllib.request.urlopen(req) as resp:
            rel_data = json.load(resp)
            upload_url_template = rel_data['upload_url']
    else:
        raise e

# Upload URL cleans the '{?name,label}' template suffix
base_upload_url = upload_url_template.split('{')[0]

def upload_asset(file_path, asset_name):
    print(f"Uploading {asset_name} ({os.path.getsize(file_path) / (1024*1024):.2f} MB)...")
    url = f"{base_upload_url}?name={asset_name}"
    with open(file_path, "rb") as f:
        file_bytes = f.read()
    
    up_headers = {
        "Authorization": f"token {token}",
        "User-Agent": "Antigravity-Agent",
        "Content-Type": "application/vnd.android.package-archive",
        "Content-Length": str(len(file_bytes))
    }
    up_req = urllib.request.Request(url, data=file_bytes, headers=up_headers)
    with urllib.request.urlopen(up_req, timeout=300) as up_resp:
        asset_info = json.load(up_resp)
        print(f"Uploaded {asset_name}: {asset_info['browser_download_url']}")
        return asset_info['browser_download_url']

release_apk_path = os.path.join(os.path.dirname(__file__), "..", "build_artifacts", "cbse10-masterclass-release-apk", "app-release.apk")
debug_apk_path = os.path.join(os.path.dirname(__file__), "..", "build_artifacts", "cbse10-masterclass-debug-apk", "app-debug.apk")

if os.path.exists(release_apk_path):
    dl1 = upload_asset(release_apk_path, "app-release.apk")
    print(f"Release APK Direct Link: {dl1}")

if os.path.exists(debug_apk_path):
    dl2 = upload_asset(debug_apk_path, "app-debug.apk")
    print(f"Debug APK Direct Link: {dl2}")


