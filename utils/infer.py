from ultralytics import YOLO
from configs.structure import MODELS_DIR, RAW_DATA_DIR
from utils.file import exists, mkdir
from enum import Enum

PRETRAINED_MODEL_PATH = f"{MODELS_DIR}/pretrained"

default_infer_config = {
    "save": False,
    "show": False,
    # "imgsz": 640,
    "batch": 32,
    "epochs": 300,
    "exist_ok": True,
    # "data": f"{path_videos}/data.yaml",
    # "project": f"{path_videos}",
}


class Pretrained(Enum):
    CLASSIFY = 0
    DETECT = 1
    SEGMENT = 2
    POSE = 3

    @classmethod
    def get_pretrained_model_path(cls, task_num):
        if task_num == cls.CLASSIFY:
            return f"{PRETRAINED_MODEL_PATH}/yolov8n-cls.pt"
        elif task_num == cls.DETECT:
            return f"{PRETRAINED_MODEL_PATH}/yolov8n.pt"
        elif task_num == cls.SEGMENT:
            return f"{PRETRAINED_MODEL_PATH}/yolov8n-seg.pt"
        elif task_num == cls.POSE:
            return f"{PRETRAINED_MODEL_PATH}/yolov8n-pose.pt"

    @classmethod
    def get_pretrained_model(cls, task_num):
        model_path = cls.get_pretrained_model_path(task_num)
        if task_num == cls.CLASSIFY:
            return YOLO(model=model_path, task="classify")
        elif task_num == cls.DETECT:
            return YOLO(model=model_path, task="detect")
        elif task_num == cls.SEGMENT:
            return YOLO(model=model_path, task="segment")
        elif task_num == cls.POSE:
            return YOLO(model=model_path, task="pose")

    # @classmethod
    # def fine_tune_detection(cls, fine_tune_name, source, cls_labels):
    #     output = f"{MODELS_DIR}/{fine_tune_name}"
    #     if not exists(output):
    #         mkdir(output)
    #     model = cls.get_pretrained_model(cls.DETECT)
    #     model.train(
    #         **default_infer_config,
    #         source=source,
    #         project=output
    #     )

    @classmethod
    def infer(cls, task_num, source, stream_handler, **kwargs):
        model = cls.get_pretrained_model(task_num)
        options = {**default_infer_config, "show": True, "stream": True, **kwargs}
        stream = model.predict(
            **options,
            source=source,
        )
        stream_handler(stream)


class FineTuned:
    @classmethod
    def infer(cls, fine_tuned_model_path, source, stream_handler, **kwargs):
        model = YOLO(model=fine_tuned_model_path)
        options = {**default_infer_config, "show": True, "stream": True, **kwargs}
        stream = model.predict(
            **options,
            source=source,
        )
        stream_handler(stream)