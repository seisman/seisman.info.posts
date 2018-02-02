#!/usr/bin/env python
#
# Extract slug from filename and add slug to frontmatter
#

import os
import sys

for fname in sys.argv[1:]:
    # extract slug from filename `YYYY-mm-dd-slug.md`
    slug = os.path.basename(fname)[11:-3]

    # read file content
    with open(fname, "r") as f:
        lines = f.readlines()

    # add slug into frontmatter
    with open(fname, "w") as f:
        for i in range(0, len(lines)):
            line = lines[i]
            if line == '---\n' and i != 0:
                f.write("slug: {}\n".format(slug))
                f.write(line)
            else:
                f.write(line)
