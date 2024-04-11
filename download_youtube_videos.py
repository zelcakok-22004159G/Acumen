from utils.youtube_downloader import download_videos
from utils.file import rmdir, exists, mkdir
from configs.structure import RAW_DATA_DIR

if __name__ == '__main__':
    if exists(f"{RAW_DATA_DIR}/youtube_videos/"):
        rmdir(f"{RAW_DATA_DIR}/youtube_videos/")
        mkdir(f"{RAW_DATA_DIR}/youtube_videos/")

    download_videos()