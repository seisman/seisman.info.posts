#!/usr/bin/env python
#
# Update slug in frontmatter based on slug extracted from filename
#

import os
import sys

for fname in sys.argv[1:]:
    # extract slug from filename `YYYY-mm-dd-slug.md`
    slug = os.path.basename(fname)[11:-3]

    # read file content
    with open(fname, "r") as f:
        lines = f.readlines()

    # update slug into frontmatter
    with open(fname, "w") as f:
        for line in lines:
            if line.startswith('slug:'):
                f.write("slug: {}\n".format(slug))
            else:
                f.write(line)
