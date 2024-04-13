from utils.model import FineTuned
from configs.structure import MODELS_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR

def handler(stream):
    for frame in stream:
        pass

identify_players_model = FineTuned.infer(
    f"{MODELS_DIR}/fine_tuned/identify_players-2024-04-13T14\:43\:14.374606/best.pt", 
    f"{RAW_DATA_DIR}/youtube_videos/video_1.mp4",
    handler
)
