from ultralytics import YOLO
from configs.structure import MODELS_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR
from utils.file import mkdir, cp
from enum import Enum
import datetime

PRETRAINED_MODEL_PATH = f"{MODELS_DIR}/pretrained"

default_infer_config = {
    "save": False,
    "show": False,
    "imgsz": 640,
    "batch": 32,
    "epochs": 300,
    "exist_ok": True,
}


class Pretrained(Enum):
    CLASSIFY = "CLASSIFY"
    DETECT = "DETECT"
    POSE = "POSE"

    @classmethod
    def get_pretrained_model_path(cls, task):
        if task == cls.CLASSIFY:
            return f"{PRETRAINED_MODEL_PATH}/yolov8n-cls.pt"
        elif task == cls.DETECT:
            return f"{PRETRAINED_MODEL_PATH}/yolov8n.pt"
        elif task == cls.SEGMENT:
            return f"{PRETRAINED_MODEL_PATH}/yolov8n-seg.pt"
        elif task == cls.POSE:
            return f"{PRETRAINED_MODEL_PATH}/yolov8n-pose.pt"

    @classmethod
    def get_pretrained_model(cls, task):
        model_path = cls.get_pretrained_model_path(task)
        if task == cls.CLASSIFY:
            return YOLO(model=model_path, task="classify")
        elif task == cls.DETECT:
            return YOLO(model=model_path, task="detect")
        elif task == cls.SEGMENT:
            return YOLO(model=model_path, task="segment")
        elif task == cls.POSE:
            return YOLO(model=model_path, task="pose")

    @classmethod
    def fine_tune_detection(cls, fine_tune_name, source, **kwargs):
        current_datetime = datetime.datetime.now().isoformat()
        project_folder = f"{MODELS_DIR}/train/{fine_tune_name}-{current_datetime}"
        mkdir(project_folder)
        model = cls.get_pretrained_model(cls.DETECT)
        options = {**default_infer_config,
                   "save": True, "show": False, **kwargs}
        model.train(
            **options,
            name=fine_tune_name,
            source=source,
            data=f"{PROCESSED_DATA_DIR}/{fine_tune_name}/data.yaml",
            project=project_folder,
        )
        mkdir(f"{MODELS_DIR}/fine_tune/{fine_tune_name}-{current_datetime}")
        cp(f"{project_folder}/{fine_tune_name}/weights/best.pt",
           f"{MODELS_DIR}/fine_tune/{fine_tune_name}-{current_datetime}/best.pt")
        cp(f"{project_folder}/{fine_tune_name}/weights/last.pt",
           f"{MODELS_DIR}/fine_tune/{fine_tune_name}-{current_datetime}/last.pt")

    @classmethod
    def infer(cls, task, source, stream_handler, **kwargs):
        model = cls.get_pretrained_model(task)
        options = {**default_infer_config,
                   "show": True, "stream": True, **kwargs}
        stream = model.predict(
            **options,
            source=source,
        )
        stream_handler(stream)


class FineTuned:
    @classmethod
    def infer(cls, fine_tuned_model_path, source, stream_handler, **kwargs):
        model = YOLO(model=fine_tuned_model_path)
        options = {**default_infer_config,
                   "show": True, "stream": True, **kwargs}
        stream = model.predict(
            **options,
            source=source,
        )
        stream_handler(stream)
