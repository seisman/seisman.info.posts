#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pandoc filter to deal with image and links

1. ![](/images/xxx.png) => ![](/absoulute/path/to/iamges/xxx.png)
2. [Link](/xxxx.html)   => [Link](https://seisman.info/xxxx.html)

Usage:
    pandoc -t json post.md | ./markdown-filter.py | pandoc -f json -t markdown
    pandoc post.md --filter ./markdown-filter.py -t markdown
"""

import os
import sys
from pandocfilters import toJSONFilter, Image

siteurl = "https://seisman.info"
base = os.getcwd()


def filters(key, value, format, meta):
    if key == "Image":
        if not value[2][0].startswith("http"):
           value[2][0] = base + value[2][0]

    if key == "Link":
        if value[2][0].startswith("/"):
            value[2][0] = siteurl + value[2][0]
    return None

if __name__ == "__main__":
    toJSONFilter(filters)
