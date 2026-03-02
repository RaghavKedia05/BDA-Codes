#!/usr/bin/env python3
import sys

data = {}

for line in sys.stdin:
    k, v = line.strip().split()
    v = int(v)

    if k not in data:
        data[k] = [0, 0]

    data[k][0] += v
    data[k][1] += 1

for k in data:
    total, count = data[k]
    print(k, total / count)
