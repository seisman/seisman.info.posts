#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
from datetime import datetime


with open("README.md", "w") as md, open("_pdfs/0.博文目录.txt", "w") as txt:
    # header
    md.write("# SeisMan 博客\n\n")
    txt.write("# SeisMan 博客博文目录\n\n")
    txt.write("请根据博文发布时间寻找对应的PDF文件。\n\n")

    for year in range(2013, datetime.now().year+1):
        md.write("## {} 年\n\n".format(year))
        txt.write("## {} 年\n\n".format(year))
        for file in sorted(glob.glob("_posts/{}-*-*-*.md".format(year))):
            date = '-'.join(os.path.basename(file).split('-')[0:3])
            title = open(file, "r").readlines()[1][7:].strip(' \n"\'')
            md.write("- {0}: [{1}](/{2}) \n".format(date, title, file))
            txt.write("- {0}: {1}\n".format(date, title))
        md.write("\n")
        txt.write("\n")
