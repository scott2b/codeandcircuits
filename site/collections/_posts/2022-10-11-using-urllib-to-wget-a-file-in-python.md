---
title: "Using urllib to wget a file in Python 3"
layout: post
date:   2022-10-11 16:00:00 -0500
categories:
  - python
  - io
---

I used to use [python3-wget](https://github.com/jamiejackherer/python3-wget){:target="_blank"} to fetch
remote files if I needed to save them to my filesystem from Python code.

Anymore, I am finding that urllib and shutil used together will do the trick:

```
import os
import shutil
import urllib
import urllib.request


def download(url, tofile=None):
    """Fetch a file from `url` and save it to `tofile`.
    """
    if tofile is None:
        tofile = os.path.basename(urllib.parse.urlparse(url).path)
    with urllib.request.urlopen(url) as response, open(tofile, "wb") as outfile:
        shutil.copyfileobj(response, outfile)
    return tofile
```
