from pytube import YouTube
from json import loads
from configs.structure import RAW_DATA_DIR, YOUTUBE_VIDEOS_SPEC
from tqdm import tqdm
from utils.file import read


def download(link, path, filename):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=path, filename=filename)
        print("Downloaded", filename)
    except:
        print("An error has occurred", link)


def download_videos():
    save_to = f"{RAW_DATA_DIR}/youtube_videos/"
    content = read(YOUTUBE_VIDEOS_SPEC)
    video_specs = loads(content)
    for idx, vs in enumerate(tqdm(video_specs, desc='Downloading...')):
        download(vs['url'], save_to, f"video_{idx}.mp4")

