#!/usr/bin/env python3
import sys

total = 0
for line in sys.stdin:
    total += len(line.strip().split())

print("Total Words:", total)
