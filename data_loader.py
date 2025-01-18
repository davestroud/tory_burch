import boto3
import requests
from tqdm import tqdm
import os

# AWS S3 configuration
bucket_name = "tory-burch"  # Replace with your bucket name
s3_client = boto3.client("s3")

# List of Parquet file URLs for the dataset
parquet_urls = [
    "https://huggingface.co/datasets/Marqo/fashion200k/resolve/main/data/data-00000-of-00009.parquet",
    "https://huggingface.co/datasets/Marqo/fashion200k/resolve/main/data/data-00001-of-00009.parquet",
    "https://huggingface.co/datasets/Marqo/fashion200k/resolve/main/data/data-00002-of-00009.parquet",
    "https://huggingface.co/datasets/Marqo/fashion200k/resolve/main/data/data-00003-of-00009.parquet",
    "https://huggingface.co/datasets/Marqo/fashion200k/resolve/main/data/data-00004-of-00009.parquet",
    "https://huggingface.co/datasets/Marqo/fashion200k/resolve/main/data/data-00005-of-00009.parquet",
    "https://huggingface.co/datasets/Marqo/fashion200k/resolve/main/data/data-00006-of-00009.parquet",
    "https://huggingface.co/datasets/Marqo/fashion200k/resolve/main/data/data-00007-of-00009.parquet",
    "https://huggingface.co/datasets/Marqo/fashion200k/resolve/main/data/data-00008-of-00009.parquet",
]


def upload_file_to_s3(file_url, s3_bucket, s3_key):
    """Download a file from a URL and upload it to S3."""
    response = requests.get(file_url, stream=True)
    response.raise_for_status()  # Raise an exception for HTTP errors

    with tqdm(
        total=int(response.headers.get("content-length", 0)),
        unit="B",
        unit_scale=True,
        desc=s3_key,
    ) as progress:
        # Wrap response.raw in a callback-enabled file-like object
        wrapped_file = ProgressFile(response.raw, progress)
        s3_client.upload_fileobj(
            wrapped_file,
            s3_bucket,
            s3_key,
        )

    print(f"Uploaded to s3://{s3_bucket}/{s3_key}")


class ProgressFile:
    """A wrapper for a file-like object that updates a progress bar."""

    def __init__(self, fileobj, progress):
        self.fileobj = fileobj
        self.progress = progress

    def read(self, size=-1):
        data = self.fileobj.read(size)
        self.progress.update(len(data))
        return data

    def __getattr__(self, name):
        return getattr(self.fileobj, name)


def main():
    s3_prefix = "fashion200k"
    for file_url in parquet_urls:
        file_name = os.path.basename(file_url)
        s3_key = f"{s3_prefix}/{file_name}"
        print(f"Uploading {file_name} to S3...")
        upload_file_to_s3(file_url, bucket_name, s3_key)


if __name__ == "__main__":
    main()
