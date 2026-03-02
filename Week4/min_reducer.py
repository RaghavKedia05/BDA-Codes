#!/usr/bin/env python3
import sys

min_dict = {}

for line in sys.stdin:
    k, v = line.strip().split()
    v = int(v)

    if k not in min_dict or v < min_dict[k]:
        min_dict[k] = v

for k in min_dict:
    print(k, min_dict[k])
