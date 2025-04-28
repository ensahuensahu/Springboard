import requests
import gzip
import shutil
import os

# Dataset source: AWS Open Data - Amazon Customer Reviews (Electronics)
url = "https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Electronics_v1_00.tsv.gz"
destination = "./chosen_dataset"

# Ensure destination exists
os.makedirs(destination, exist_ok=True)

gz_file = os.path.join(destination, "amazon_reviews_us_Electronics.tsv.gz")
tsv_file = os.path.join(destination, "amazon_reviews_us_Electronics.tsv")

# Download
print("Downloading Amazon Reviews dataset...")
response = requests.get(url, stream=True)
with open(gz_file, 'wb') as f:
    shutil.copyfileobj(response.raw, f)
print("Download complete.")

# Extract
print("Extracting dataset...")
with gzip.open(gz_file, 'rb') as f_in:
    with open(tsv_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
print("Extraction complete.")
