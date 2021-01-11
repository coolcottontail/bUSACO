#!/usr/bin/env python
import re
import urllib.request
import sys
from tqdm import tqdm
import requests

import sys

def find(webpage):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://embed-ssl.|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, webpage)
    return list(filter(lambda x: '.bin' in x, [x[0] for x in url]))



url = "https://fast.wistia.net/embed/iframe/[ID]?videoFoam=true"


if len(sys.argv) < 3:
    print("crawl.py ID name.mp4")
    sys.exit(0)


dUrl = url.replace('[ID]', sys.argv[1])


fid=urllib.request.urlopen(dUrl)
webpage=fid.read().decode('utf-8')
urlL = find(webpage)

u = urlL[0]
f = u.find('.bin')
tUrl = u[:f + 4]


print("Downloading file " + tUrl)

response = requests.get(tUrl, stream=True)
total_size_in_bytes= int(response.headers.get('content-length', 0))
block_size = 1024 #1 Kibibyte
progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
with open(sys.argv[2], 'wb') as file:
    for data in response.iter_content(block_size):
        progress_bar.update(len(data))
        file.write(data)
progress_bar.close()
if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
    print("ERROR, something went wrong")