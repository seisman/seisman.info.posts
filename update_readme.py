#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob

f = open("README.md", "w")
f.write("# SeisMan 博客\n\n")

for year in range(2013, 2018, 1):
    f.write("## {} 年\n\n".format(year))
    for md in sorted(glob.glob("_posts/{}-*-*-*.md".format(year))):
        date = '-'.join(os.path.basename(md).split('-')[0:3])
        title = open(md, "r").readlines()[1][7:].strip(' \n"\'')
        f.write("- {0}: [{1}](/{2}) \n".format(date, title, md))
    f.write("\n")

f.close()

f = open("_pdfs/0.博文目录.txt", "w")
f.write("# SeisMan 博客博文目录\n\n")
f.write("请根据博文发布时间寻找对应的PDF文件。\n\n")

for year in range(2013, 2017, 1):
    f.write("## {} 年\n\n".format(year))
    for md in sorted(glob.glob("_posts/{}-*-*-*.md".format(year))):
        date = '-'.join(os.path.basename(md).split('-')[0:3])
        title = open(md, "r").readlines()[1][7:].strip(' \n"\'')
        f.write("- {0}: {1}\n".format(date, title))
    f.write("\n")
