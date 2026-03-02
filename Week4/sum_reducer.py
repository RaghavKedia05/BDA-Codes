#!/usr/bin/env python3
import sys

sum_dict = {}

for line in sys.stdin:
    k, v = line.strip().split()
    v = int(v)
    sum_dict[k] = sum_dict.get(k, 0) + v

for k in sum_dict:
    print(k, sum_dict[k])
