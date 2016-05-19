#!/usr/bin/env python
"""Convert markdown to PDF

Usage:
    python makepdf.py _posts/*.md
"""

import os
import re
import sys
import glob
import subprocess


siteurl = "http://seisman.info/"
pdf_dir = "_pdfs"
filter = "./markdown-filter.py"
template = "seisman.latex"


def md2pdf(md, pdf, date, permalink):
    json = subprocess.Popen(['pandoc', '-t', 'json', md], stdout=subprocess.PIPE)
    filtered = subprocess.Popen([filter], stdin=json.stdout, stdout=subprocess.PIPE)

    cmd = ["pandoc",
           "-f", "json",
           "-t", "latex",
           "-o", pdf,
           "-s",
           "--template", template,
           "--listings",
           "--number-sections",
           "--chapters",
           "--latex-engine=xelatex",
           "-Vpermalink="+permalink,
           "-Vdate="+date,
          ]
    subprocess.run(cmd, stdin=filtered.stdout)


if __name__ == '__main__':
    # create dir for PDF
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    for srcfile in sys.argv[1:]:
        path, filename = os.path.split(srcfile)
        slug, ext = os.path.splitext(filename)

        pdffile = os.path.join(pdf_dir, slug + ".pdf")
        permalink = siteurl + '-'.join(slug.split('-')[3:]) + ".html"
        date = '-'.join(slug.split('-')[0:3])

        # only when PDF not found or PDF older than source
        if not os.path.exists(pdffile):
            print("%s => %s" % (srcfile, pdffile))
            md2pdf(srcfile, pdffile, date, permalink)
        else:
            src_mtime = os.path.getmtime(srcfile)
            pdf_mtime = os.path.getmtime(pdffile)
            if src_mtime > pdf_mtime:
                print("%s => %s" % (srcfile, pdffile))
                md2pdf(srcfile, pdffile, date, permalink)
