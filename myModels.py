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
    #{
        #"url": "https://civitai.com/api/download/models/1609607?type=Model&format=SafeTensor&size=pruned&fp=fp16",
        #"path": "models/checkpoints/realstic_v6.safetensors"
    #},
    #{
        #"url": "https://civitai.com/api/download/models/709468?type=Model&format=SafeTensor&size=pruned&fp=fp32",
        #"path": "models/checkpoints/halCylon.safetensors"
    #},
    {
        "url": "https://huggingface.co/ntc-ai/SDXL-LoRA-slider.cinematic-lighting/resolve/main/cinematic%20lighting.safetensors",
        "path": "models/loras/cinematic_Loras_hFace.safetensors"
    },
    {
	"url": "https://civitai.com/api/download/models/1386847?type=Model&format=SafeTensor",
        "path": "models/loras/budy_weight.safetensors"
    },
    {
        "url": "https://huggingface.co/ntc-ai/SDXL-LoRA-slider.color-grading/resolve/main/color%20grading.safetensors",
        "path": "models/loras/Color_Grading_hFace.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/145907?type=Model&format=SafeTensor",
        "path": "models/loras/Detailed_Eye.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/534952?type=Model&format=SafeTensor",
        "path": "models/loras/breast_size_control.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/1242203?type=Model&format=SafeTensor",
        "path": "models/loras/Dramadic_Light.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/827325?type=Model&format=SafeTensor",
        "path": "models/loras/realskin.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/466120?type=Model&format=SafeTensor",
        "path": "models/loras/RawLight.safetensors"
    },
    {
        "url": "https://civitai.com/api/download/models/1037669?type=Model&format=SafeTensor",
        "path": "models/loras/Pony_Realism_enhencher.safetensors"
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
