# Source - https://stackoverflow.com/a/5137509
# Posted by Russell Dias, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-16, License - CC BY-SA 3.0

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# This part is by me
print(dir_path)
srctree = f"{dir_path}/.."

import requests

zip_link = "https://drive.usercontent.google.com/u/0/uc?id=1eEKzfmEu6WKdRlohBQiqi3PhW_uIVJVP&export=download"

with open(f"{srctree}/data/data_zip.zip") as zip_file:
    content = requests.get(zip_link, stream=True).content
    zip_file.write(str(content))