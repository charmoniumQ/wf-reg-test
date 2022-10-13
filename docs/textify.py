#!/usr/bin/env python

import sys
import re

replace_patterns = [
    ("---.*?---", ""),
    ("```.*?```", ""),
    ("<!--.*?-->", ""),
    ("\[@.*\]", ""),
    (r"\[(.*)\]\(.*\)(?:\{.*\})?", r"\1"),
    (r"\[.*\]: http.*?\n", ""),
    (r"#+", ""),
]

doc = "".join(sys.stdin)
for pattern, repl in replace_patterns:
    doc = re.sub(pattern, repl, doc, flags=re.DOTALL)
sys.stdout.write(doc)
