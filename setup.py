'''
Project structure:
    configs/ <-- All configuration files, e.g. hyperparameters, etc.
        youtube_videos.json
        structure.py
    data/
        raw/ <-- All raw data files, e.g. videos, images, etc.
        processed/ 
            {task_name}/ <-- All processed data files, e.g. pngs, npys, etc.
            ...
    models/
        {task_name}/ <-- All models, e.g. identify_players.h5
    uitls/
    setup.py
    index.py
'''

from utils.file import exists, mkdir, touch, write

structure = [
    "RAW_DATA_DIR='data/raw'",
    "PROCESSED_DATA_DIR='data/processed'",
    "MODELS_DIR='models'",
    "YOUTUBE_VIDEOS_SPEC='configs/youtube_videos.json'"
]

def setup():
    '''
    Setup the project structure
    '''
    import os

    # Create the data directory
    data_dir = 'data'
    if not os.path.exists(data_dir):
        mkdir(data_dir)
        mkdir(os.path.join(data_dir, 'raw'))
        mkdir(os.path.join(data_dir, 'processed'))

    # Create the models directory
    models_dir = 'models'
    if not os.path.exists(models_dir):
        mkdir(models_dir)

    # Create the utils directory
    utils_dir = 'utils'
    if not os.path.exists(utils_dir):
        mkdir(utils_dir)

    # Create the configs directory
    configs_dir = 'configs'
    if not exists(configs_dir):
        mkdir(configs_dir)
    if not exists(os.path.join(configs_dir, 'youtube_videos.json')):
        touch(os.path.join(configs_dir, 'youtube_videos.json'))
    write(os.path.join(configs_dir, 'structure.py'), "\r\n".join(structure))

    print('Project setup complete!')


if __name__ == '__main__':
    setup()
