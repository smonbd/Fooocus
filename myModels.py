import os
import urllib.request
from tqdm import tqdm

def download_file_with_auth(url, destination_path, headers):
    if os.path.exists(destination_path):
        print(f"✅ {destination_path} already exists.")
        return

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        total_size = int(response.getheader('Content-Length').strip())
        chunk_size = 1024  # 1 KB

        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        with open(destination_path, 'wb') as out_file, tqdm(
            total=total_size, unit='B', unit_scale=True, desc=os.path.basename(destination_path)
        ) as pbar:
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                out_file.write(chunk)
                pbar.update(len(chunk))

def main():
    # API Token (replace or load from env)
    token = "your_api_token_here"  # or os.getenv("MY_API_TOKEN")

    # URLs
    files = [
        {
            "url": "https://civitai.com/api/download/models/798204?type=Model&format=SafeTensor&size=full&fp=fp16",
            "path": "models/checkpoints/RealVisXL.safetensors"
        },
        {
            "url": "https://civitai.com/api/download/models/294259?type=Model&format=SafeTensor",
            "path": "models/loras/hands.safetensors"
        },
        {
            "url": "https://civitai.com/api/download/models/129711?type=Model&format=SafeTensor",
            "path": "models/loras/Eyes.safetensors"
        }
    ]

    # Headers
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Download all files
    for file in files:
        download_file_with_auth(file["url"], file["path"], headers)

if __name__ == "__main__":
    main()
