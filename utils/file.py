import os
import shutil


def exists(path):
    return os.path.exists(path)


def read(path):
    with open(path, 'r') as f:
        return f.read()


def write(path, content):
    with open(path, 'w') as f:
        f.write(content)


def mkdir(path):
    os.makedirs(path, exist_ok=True)


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


def rm(path):
    shutil.rmtree(path, ignore_errors=True)


def ls(path, list_handler, count_handler=len, sort_handler=None):
    allfiles = os.listdir(path)
    if sort_handler:
        allfiles = sort_handler(allfiles)        
    statis = count_handler(allfiles)
    list_handler(allfiles, statis)


def cp(src, dst):
    shutil.copy(src, dst)