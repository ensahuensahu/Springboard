import os
from zipfile import ZipFile

# Dataset source: Kaggle Lending Club Loan Data
dataset = 'wordsforthewise/lending-club'
destination = './datasets/lending_club'

# Ensure destination exists
os.makedirs(destination, exist_ok=True)

# Download using Kaggle API
print("Downloading Lending Club dataset from Kaggle...")
os.system(f'kaggle datasets download -d {dataset} -p {destination}')

# Extract ZIP file
zip_path = os.path.join(destination, 'lending-club.zip')
if os.path.exists(zip_path):
    print("Extracting dataset...")
    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(destination)
    print("Extraction complete.")
else:
    print("Download failed or file not found. Please check Kaggle API setup.")