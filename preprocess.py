import sys
from utils.process import preprocess
from utils.file import exists
from configs.structure import RAW_DATA_DIR

if len(sys.argv) > 1:
    raw_folder_name = sys.argv[1]
    labels = sys.argv[2:]
    if not exists(f"{RAW_DATA_DIR}/{raw_folder_name}"):
        print(f"Error: Folder {raw_folder_name} does not exist")
        exit()
    preprocess(raw_folder_name, labels)
