#!/usr/bin/env python3
import sys

records = []

for line in sys.stdin:
    k, v = line.strip().split()
    records.append((k, int(v)))

records.sort(key=lambda x: x[1], reverse=True)

for r in records:
    print(r[0], r[1])
