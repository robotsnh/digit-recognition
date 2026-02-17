# Source - https://stackoverflow.com/a/5137509
# Posted by Russell Dias, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-16, License - CC BY-SA 3.0

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# This part is by me
from pathlib import Path
srctree = str(Path(dir_path).parent)

import requests

zip_link = "https://drive.usercontent.google.com/u/0/uc?id=1eEKzfmEu6WKdRlohBQiqi3PhW_uIVJVP&export=download"
zip_location = Path(f"{srctree}/data/data_zip.zip")

zip_location.parent.mkdir(parents=True, exist_ok=True)

Path(zip_location).touch()

with open(f"{srctree}/data/data_zip.zip", "wb") as zip_file:
    content = requests.get(zip_link, stream=True).content
    zip_file.write(content)

# Source - https://stackoverflow.com/a/12886818
# Posted by phihag, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-16, License - CC BY-SA 3.0

import zipfile, os.path
def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        for member in zf.infolist():
            # Path traversal defense copied from
            # http://hg.python.org/cpython/file/tip/Lib/http/server.py#l789
            words = member.filename.split('/')
            path = dest_dir
            for word in words[:-1]:
                while True:
                    drive, word = os.path.splitdrive(word)
                    head, word = os.path.split(word)
                    if not drive:
                        break
                if word in (os.curdir, os.pardir, ''):
                    continue
                path = os.path.join(path, word)
            zf.extract(member, path)

#this is my code again
unzip(zip_location, f"{srctree}/data")
os.remove(zip_location)
os.remove(f"{srctree}/data/generate_mnist_csv.py")
os.remove(f"{srctree}/data/readme.md")
