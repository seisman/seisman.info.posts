#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pandoc filter to deal with seisman's posts

1. ![caption](/images/xxx.png) => ![caption](images/xxx.png)
2. [text](/link/) => [text](http://blog.seisman.info/link/)

Usage:
    pandoc -t json post.md | ./pandoc-filter.py | pandoc -f json -t markdown
    pandoc post.md --filter ./pandoc-filter.py -t markdown
"""
import os
import sys
import glob
from pandocfilters import toJSONFilter, Str

siteurl = "http://blog.seisman.info"

def filters(key, value, format, meta):
    # [caption](/images/xxx.png) => [caption](images/xxx.png)
    if key == 'Image':
        if value[2][0].startswith("/images/"):
            value[2][0] = value[2][0].lstrip('/')

    if key == 'Link':
        if value[2][0].startswith("/"):
            basename = value[2][0].strip('/') + ".md"
            files = glob.glob("post/" + "????-??-??-" + basename)

            if len(files) == 0:
                # Is a page, not a post
                # [text](/link/) => [text](http://blog.seisman.info/link/)
                value[2][0] = siteurl + value[2][0]
            elif len(files) == 1:
                # Is a post, convert to an internal reference
                # [text](/link/) => [text](#link)
                value[2][0] = "#" + value[2][0].strip('/')
            else:
                raise Exception("Glob return more than one file!\n")

    return None

if __name__ == "__main__":
    toJSONFilter(filters)
