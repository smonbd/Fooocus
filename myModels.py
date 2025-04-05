import requests
from tqdm import tqdm
import os

# CivitAI API Key (Replace with your key)
API_KEY = input("Insert CivitAI Api Key")  # Replace with your actual token

# Headers for authentication
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "User-Agent": "Mozilla/5.0"
}

# List of models to download
files = [
    {
        "url": "https://civitai.com/api/download/models/798204?type=Model&format=SafeTensor&size=full&fp=fp16",
        "path": "models/checkpoints/RealVisXL_V5.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/1522905?type=Model&format=SafeTensor&size=pruned&fp=fp16",
        "path": "models/checkpoints/epiCRealism_XL.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/294259?type=Model&format=SafeTensor",
        "path": "models/loras/hands.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/129711?type=Model&format=SafeTensor",
        "path": "models/loras/eyes.safetensors"
    }, 
    {
        "url": "https://civitai.com/api/download/models/556292?type=Model&format=SafeTensor",
        "path": "models/loras/Crazy_Girlfriend_Mix.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/911708?type=Model&format=SafeTensor",
        "path": "models/loras/Hourglass_Body_Shape.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/993780?type=Model&format=SafeTensor",
        "path": "models/loras/Perfect_Round_Ass.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/481917?type=Model&format=SafeTensor",
        "path": "models/loras/Cinematic_Shot.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/118945?type=Model&format=SafeTensor",
        "path": "models/loras/epiCRealismHelper.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/62833?type=Model&format=SafeTensor",
        "path": "models/loras/Detail_Tweaker_LoRA.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/122580?type=Model&format=SafeTensor",
        "path": "models/loras/Skin_&_Hands.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/151465?type=Model&format=SafeTensor",
        "path": "models/loras/ReaLora_Realistic_skin_texture.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/135867?type=Model&format=SafeTensor",
        "path": "models/loras/details_twiker_most_downloaded.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/177674?type=Model&format=SafeTensorl,
        "path": "models/loras/nudify_XL.safetensors"
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
