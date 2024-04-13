from utils.file import exists
from utils.model import FineTuned
import argparse

parser = argparse.ArgumentParser(
    prog='Test inference',
    description='Test inference on fine tuned model',
    epilog='Specify the fine tuned model path and the source to test inference on')

parser.add_argument('fine_tune_model_path', help='Fine tuned model path')
parser.add_argument('source', help='Source to fine tune')
args = parser.parse_args()

fine_tune_model_path = args.fine_tune_model_path
source = args.source


if not exists(fine_tune_model_path):
    print(f"Error: Folder {fine_tune_model_path} does not exist")
    exit()

def handler(stream):
    for frame in stream:
        pass

FineTuned.infer(
    f"{fine_tune_model_path}/best.pt",
    source,
    handler
)
