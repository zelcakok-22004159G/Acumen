from ultralytics.utils.plotting import Annotator, colors
from PIL import Image
import cv2
from setup import setup
from utils.infer import FineTuned
from configs.structure import RAW_DATA_DIR, MODELS_DIR
import numpy as np


def handler(stream):
    for fid, frame in enumerate(stream):
        pass
        # if not frame.boxes:
        #     continue
        # boxes = frame.boxes.cpu()
        # classes = frame.boxes.cls.int().cpu().tolist()

        # orig_img = np.copy(frame.orig_img)
        # annotator = Annotator(orig_img, line_width=2)
        # frame_img = Image.fromarray(cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB))


# Pretrained.infer(
#     Pretrained.DETECT,
#     f"{RAW_DATA_DIR}/youtube_videos/video_0.mp4",
#     stream_handler=handler,
#     conf=0.7,
#     max_det=3
# )
FineTuned.infer(
    f"{MODELS_DIR}/identify_players/model.pt",
    f"{RAW_DATA_DIR}/youtube_videos/abe.mp4",
    stream_handler=handler,
    # conf=0.7,
    max_det=3
)
