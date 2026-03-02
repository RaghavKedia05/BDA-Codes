#!/usr/bin/env python3
import sys

max_dict = {}

for line in sys.stdin:
    k, v = line.strip().split()
    v = int(v)

    if k not in max_dict or v > max_dict[k]:
        max_dict[k] = v

for k in max_dict:
    print(k, max_dict[k])
