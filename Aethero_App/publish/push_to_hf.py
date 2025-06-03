import os
from huggingface_hub import HfApi, HfFolder

def publish_to_huggingface(repo_name, files, repo_type="space"):
    """
    Publishes files to a Hugging Face Space.

    Args:
        repo_name (str): Name of the Hugging Face repository.
        files (list): List of file paths to upload.
        repo_type (str): Type of repository (default: "space").
    """
    api = HfApi()
    token = HfFolder.get_token()

    if not token:
        raise ValueError("Hugging Face API token not found. Please log in using `huggingface-cli login`.")

    # Create or update the repository
    api.create_repo(repo_name, repo_type=repo_type, exist_ok=True)

    # Upload files
    for file in files:
        api.upload_file(
            path_or_fileobj=file,
            path_in_repo=os.path.basename(file),
            repo_id=repo_name,
            repo_type=repo_type
        )

if __name__ == "__main__":
    # Example usage
    repo_name = "aethero_frontinus"
    files = [
        "publish/README.md",
        "publish/index.html",
        "publish/manifest.json"
    ]
    publish_to_huggingface(repo_name, files)
