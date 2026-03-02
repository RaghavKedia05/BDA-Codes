#!/usr/bin/env python3
import sys
from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        counts[word] += 1

for word in counts:
    print(word, counts[word])
