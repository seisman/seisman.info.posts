#!/usr/bin/env python
import os
import re
import subprocess

def pandoc_markdown_process(fname):
    cmd = ["pandoc", fname,
           "-t", "markdown",
           "--filter", "pandoc-filter.py",
           "--atx-headers",
           "--base-header-level={}".format(3)
          ]
    return subprocess.check_output(cmd).decode()

def combined_file(index):
    body = ""
    with open(index, "r") as main:
        for line in main:
            if line.startswith('- '):  # list
                m = re.match(r"\[(.*)]\((.*)\)", line.lstrip('- '))
                title = m.group(1)
                markdown = m.group(2).lstrip('/')

                if not os.path.exists(markdown):
                    print("{} not exists, skipped.".format(markdown))
                    continue
                slug = os.path.splitext(os.path.basename(markdown))[0][11:]

                body += "### {} {{ #{} }}\n".format(title, slug)
                body += pandoc_markdown_process(markdown)
                body += "\n"
            else:
                body += line
    return body

def markdown_to_pdf(text, pdffile):
    cmd = ["pandoc",
           "-t", "latex",
           "--pdf-engine=xelatex",
           "--top-level-division=part",
           "--template=book-template.tex",
           "--listings",
           "-o", pdffile,
          ]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    p.communicate(text.encode())


if __name__ == "__main__":
    text = combined_file("README.md")
    markdown_to_pdf(text, "seisman-blog.pdf")
