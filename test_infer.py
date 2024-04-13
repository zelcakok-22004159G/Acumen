import sys
from utils.file import exists
from configs.structure import PROCESSED_DATA_DIR, MODELS_DIR, RAW_DATA_DIR
from utils.model import FineTuned

if len(sys.argv) > 1:
    fine_tune_model_path = sys.argv[1]
    source = sys.argv[2]
    if not exists(fine_tune_model_path):
        print(f"Error: Folder {fine_tune_model_path} does not exist")
        exit()

    def handler(stream):
        for frame in stream:
            pass

    FineTuned.infer(
        f"{fine_tune_model_path}/best.pt",
        f"{RAW_DATA_DIR}/youtube_videos/abe.mp4",
        handler
    )
