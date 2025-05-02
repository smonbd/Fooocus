import requests
from tqdm import tqdm
import os

# CivitAI API Key (Replace with your key)
API_KEY = "84222cb9ca97a6e22c7b04bc26aaad5c" #input("Insert CivitAI Api Key: ")  # Replace with your actual token

# Headers for authentication
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "User-Agent": "Mozilla/5.0"
}

# List of models to download
files = [
    {
        "url": "https://civitai.com/api/download/models/789646?type=Model&format=SafeTensor&size=full&fp=fp16",
        "path": "models/checkpoints/RealVis5.safetensors"
    }
]

# Function to download a file
def download_file(url, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Check if file already exists
    if os.path.exists(path):
        print(f"✅ [SKIP] File already exists: {path}")
        return

    print(f"⬇️ [DOWNLOAD] {url} → {path}")

    # Start request
    response = requests.get(url, headers=headers, stream=True)
    total_size = int(response.headers.get("content-length", 0))

    # Check for authentication or request failure
    if response.status_code == 401:
        print("⚠️ Error: Authentication failed. Check your API key!")
        return
    elif response.status_code != 200:
        print(f"❌ Error {response.status_code}: Failed to download {url}")
        return

    # Download file with progress bar
    with open(path, "wb") as file, tqdm(
        desc=os.path.basename(path),
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
                bar.update(len(chunk))

    print(f"✅ [SUCCESS] Download completed: {path}")

# Function to run all downloads
def myModelsRun():
    for file in files:
        download_file(file["url"], file["path"])
