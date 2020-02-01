#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
    with open(sys.argv[1]) as fb:
        for line in fb:
            print(line, end=' ')
else:
    sys.exit(-1)

