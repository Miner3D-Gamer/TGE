import os, tempfile

temp_dir = tempfile.mktemp(prefix="tmp/tge")


python_installation = f"{os.getenv('LOCALAPPDATA')}\Programs\Python"
print(python_installation)

dirs = {f"{i.path}\Lib\site-packages" for i in os.scandir(python_installation) if os.path.exists(f"{i.path}\Lib\site-packages")}




import os
import requests

def download_github_folder(owner, repo, folder_path, local_dir):
    # GitHub API URL to get the contents of the folder
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{folder_path}"
    
    # Make the request to the GitHub API
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes

    # Parse the JSON response
    folder_contents = response.json()

    # Ensure the local directory exists
    os.makedirs(local_dir, exist_ok=True)

    for item in folder_contents:
        # Skip if it's a directory (this script only handles files)
        if item['type'] == 'dir':
            continue
        
        file_url = item['download_url']
        file_name = item['name']
        local_file_path = os.path.join(local_dir, file_name)

        # Download the file
        print(f"Downloading {file_name}...")
        file_response = requests.get(file_url)
        file_response.raise_for_status()

        # Save the file locally
        with open(local_file_path, 'wb') as file:
            file.write(file_response.content)

        print(f"Saved {file_name} to {local_file_path}")
