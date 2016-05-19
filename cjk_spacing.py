#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pangu
import sys

for md in sys.argv[1:]:
    print(md)
    with open(md, "r") as f:
        lines = [pangu.spacing(line) for line in f.readlines()]
        with open(md, "w") as f:
            f.writelines(lines)
