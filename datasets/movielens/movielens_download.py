import requests
import zipfile
import os

# Dataset source: MovieLens 20M Dataset
url = "https://files.grouplens.org/datasets/movielens/ml-20m.zip"
destination = "./datasets/movielens"

# Ensure destination exists
os.makedirs(destination, exist_ok=True)

zip_path = os.path.join(destination, "ml-20m.zip")

# Download
print("Downloading MovieLens dataset...")
response = requests.get(url)
with open(zip_path, 'wb') as f:
    f.write(response.content)
print("Download complete.")

# Extract
print("Extracting dataset...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(destination)
print("Extraction complete.")
