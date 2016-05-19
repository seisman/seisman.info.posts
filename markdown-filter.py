#!/usr/bin/env python

"""
Pandoc filter to deal with image and links

1. ![](/images/xxx.png) => ![](/absoulute/path/to/iamges/xxx.png)
2. [Link](/xxxx.html)   => [Link](http://seisman.info/xxxx.html)
"""

import os
import sys
from pandocfilters import toJSONFilter, Image

siteurl = "http://seisman.info"
base = os.getcwd()


def filters(key, value, format, meta):
    if key == "Image":
       value[1][0] = base + value[1][0]

    if key == "Link":
        if value[1][0].startswith("/"):
            value[1][0] = siteurl + value[1][0]
    return None

if __name__ == "__main__":
    toJSONFilter(filters)
