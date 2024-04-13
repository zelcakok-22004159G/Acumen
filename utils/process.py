from utils.file import exists, mkdir, ls, cp, rmdir
from configs.structure import RAW_DATA_DIR, PROCESSED_DATA_DIR
from tqdm import tqdm
from math import ceil
from pathlib import Path

'''
Assume the folder contains images and txt files

specify the ratio of training, validating and testing

This method will create 2 folders and a data.yaml file
- images
- labels
'''
DATASET_RATIO = [0.7, 0.2, 0.1]


def preprocess(raw_folder, labels):

    def list_handler(allfiles, statis):
        num_train = ceil(statis["numLabels"] * DATASET_RATIO[0])
        num_valid = ceil(statis["numLabels"] * DATASET_RATIO[1])
        for i, file in enumerate(tqdm(allfiles, desc="Preprocessing")):
            if file.endswith(".txt"):
                if i < num_train:
                    cp(f"{RAW_DATA_DIR}/{raw_folder}/{file}",
                       f"{PROCESSED_DATA_DIR}/{raw_folder}/train/labels")
                elif i < num_train + num_valid:
                    cp(f"{RAW_DATA_DIR}/{raw_folder}/{file}",
                       f"{PROCESSED_DATA_DIR}/{raw_folder}/valid/labels")
                else:
                    cp(f"{RAW_DATA_DIR}/{raw_folder}/{file}",
                       f"{PROCESSED_DATA_DIR}/{raw_folder}/test/labels")
            elif file.endswith(".PNG"):
                if i < num_train:
                    cp(f"{RAW_DATA_DIR}/{raw_folder}/{file}",
                       f"{PROCESSED_DATA_DIR}/{raw_folder}/train/images")
                elif i < num_train + num_valid:
                    cp(f"{RAW_DATA_DIR}/{raw_folder}/{file}",
                       f"{PROCESSED_DATA_DIR}/{raw_folder}/valid/images")
                else:
                    cp(f"{RAW_DATA_DIR}/{raw_folder}/{file}",
                       f"{PROCESSED_DATA_DIR}/{raw_folder}/test/images")


    rmdir(f"{PROCESSED_DATA_DIR}/{raw_folder}")
    mkdir(f"{PROCESSED_DATA_DIR}/{raw_folder}/train/labels")
    mkdir(f"{PROCESSED_DATA_DIR}/{raw_folder}/train/images")
    mkdir(f"{PROCESSED_DATA_DIR}/{raw_folder}/valid/labels")
    mkdir(f"{PROCESSED_DATA_DIR}/{raw_folder}/valid/images")
    mkdir(f"{PROCESSED_DATA_DIR}/{raw_folder}/test/labels")
    mkdir(f"{PROCESSED_DATA_DIR}/{raw_folder}/test/images")
    
    ls(
        f"{RAW_DATA_DIR}/{raw_folder}",
        count_handler=count_handler,
        sort_handler=sort_handler,
        list_handler=list_handler
    )

    create_data_yaml(raw_folder, labels)

def count_handler(allfiles):
    num_lbls = 0
    num_imgs = 0
    for file in allfiles:
        if file.endswith(".txt"):
            num_lbls += 1
        elif file.endswith(".jpg"):
            num_imgs += 1
    return {"numLabels": num_lbls, "numImages": num_imgs}


def sort_handler(allfiles):
    return sorted(allfiles, key=lambda key: key[6:-4], reverse=False)


def create_data_yaml(raw_folder, labels):
    content = f'''
path: {Path(PROCESSED_DATA_DIR).resolve()}/{raw_folder}
train: train/images
val: valid/images
test: test/images

nc: {len(labels)}
names: [ {", ".join(labels)} ]
'''
    with open(f"{PROCESSED_DATA_DIR}/{raw_folder}/data.yaml", "w") as f:
        f.write(content)
    print(f"Created data.yaml for {raw_folder}")