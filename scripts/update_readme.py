#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
from datetime import datetime


os.chdir("..")
with open("README.md", "w") as md:
    # header
    md.write("# SeisMan 博客\n\n")

    for year in range(2013, datetime.now().year+1):
        md.write("## {} 年\n\n".format(year))
        for file in sorted(glob.glob("post/{}-*-*-*.md".format(year))):
            date = '-'.join(os.path.basename(file).split('-')[0:3])
            title = open(file, "r").readlines()[1][7:].strip(' \n"\'')
            md.write("- {0}: [{1}](/{2}) \n".format(date, title, file))
        md.write("\n")
