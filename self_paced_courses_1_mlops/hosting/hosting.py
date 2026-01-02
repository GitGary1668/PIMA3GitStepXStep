from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_PIMA3_TOKEN"))
api.upload_folder(
    folder_path="self_paced_courses_1_mlops/deployment",
    repo_id="GaryWilliams1668/PIMA3HFSpaceName",                      # enter the Hugging Face username here
    repo_type="space",
    path_in_repo="",                          # optional: subfolder path inside the repo
)
