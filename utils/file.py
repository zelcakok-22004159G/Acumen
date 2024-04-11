import os, shutil

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

def rmdir(path):
    shutil.rmtree(path, ignore_errors=True)


