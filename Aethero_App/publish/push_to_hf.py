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
    api.create_repo(repo_name, repo_type=repo_type, space_sdk="static", exist_ok=True)

    # Upload files
    for file in files:
        absolute_path = os.path.abspath(file)  # Ensure the file path is absolute
        if not os.path.isfile(absolute_path):
            raise ValueError(f"Provided path: '{absolute_path}' is not a file on the local file system")
        api.upload_file(
            path_or_fileobj=absolute_path,
            path_in_repo=os.path.basename(file),
            repo_id=repo_name,
            repo_type=repo_type
        )

if __name__ == "__main__":
    # Example usage
    base_dir = os.path.abspath(os.path.dirname(__file__))  # Get the directory of the current script
    repo_name = "aethero_frontinus"
    files = [
        os.path.join(base_dir, "README.md"),
        os.path.join(base_dir, "index.html"),
        os.path.join(base_dir, "manifest.json")
    ]
    publish_to_huggingface(repo_name, files)
