import requests
from tqdm import tqdm
import os

# CivitAI API Key (Replace with your key)
API_KEY = input("Insert CivitAI Api Key: ")  # Replace with your actual token

# Headers for authentication
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "User-Agent": "Mozilla/5.0"
}

# List of models to download
files = [
    {
        "url": "https://civitai.com/api/download/models/1031794?type=Model&format=SafeTensor&size=pruned&fp=fp16",
        "path": "models/checkpoints/jib_mix_realstic.safetensors"
    },
    #{
        #"url": "https://civitai.com/api/download/models/1422871?type=Model&format=SafeTensor&size=pruned&fp=fp16",
        #"path": "models/checkpoints/babe_stable_yogi.safetensors"
    #},
    {
        "url": "https://civitai.com/api/download/models/1071060?type=Model&format=SafeTensor",
        "path": "models/loras/detailer_by_yogi.safetensors"
    },
    {
	"url": "https://civitai.com/api/download/models/1439429?type=Model&format=SafeTensor",
        "path": "models/loras/pony_realism_helper.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/707763?type=Model&format=SafeTensor",
        "path": "models/loras/RealIstic_Skin.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/556292?type=Model&format=SafeTensor",
        "path": "models/loras/Crazy_GF.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/135867?type=Model&format=SafeTensor",
        "path": "models/loras/most_Details_Twicker.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/1242203?type=Model&format=SafeTensor",
        "path": "models/loras/Dramadic_Light.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/131991?type=Model&format=SafeTensor",
        "path": "models/loras/jagganth_Cinematic.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/128461?type=Model&format=SafeTensor",
        "path": "models/loras/perfect_eyes.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/380544?type=Model&format=SafeTensor",
        "path": "models/loras/BEUTY.safetensors"
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
