import sys
from utils.file import exists
from configs.structure import PROCESSED_DATA_DIR
from utils.model import Pretrained
import argparse

parser = argparse.ArgumentParser(
    prog='Fine tune',
    description='Fine tune a pretrained model',
    epilog='Specify task, processed folder name, source')

parser.add_argument('task', help='Task to fine tune [detect, classify, pose]')
parser.add_argument('processed_folder_name', help='Processed folder name')
parser.add_argument('source', help='Source to fine tune')
parser.add_argument('--epochs', help='Number of epochs', default=300)
args = parser.parse_args()

task = args.task
processed_folder_name = args.processed_folder_name
source = args.source
epochs = int(args.epochs)

if not exists(f"{PROCESSED_DATA_DIR}/{processed_folder_name}"):
    print(f"Error: Folder {processed_folder_name} does not exist")
    exit()
if task.upper() == Pretrained.DETECT.value:
    Pretrained.fine_tune_detection(
        processed_folder_name, source, epochs=epochs)
else:
    print(f"Error: Task {task} is not supported")
    exit()
