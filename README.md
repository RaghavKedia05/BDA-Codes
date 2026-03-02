# BDA-Codes
🔵 WEEK 3
1️⃣ Word Count
reducer.py
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
2️⃣ Count Total Lines
#!/usr/bin/env python3
import sys

count = 0
for line in sys.stdin:
    count += 1

print("Total Lines:", count)
3️⃣ Count Total Words
#!/usr/bin/env python3
import sys

total = 0
for line in sys.stdin:
    total += len(line.strip().split())

print("Total Words:", total)
🔵 WEEK 4

Assume input format:

City Value

Example:

Delhi 35
Delhi 40
Mumbai 30
4️⃣ Maximum Per Key
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
5️⃣ Minimum Per Key
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
6️⃣ Sum Per Key
#!/usr/bin/env python3
import sys

sum_dict = {}

for line in sys.stdin:
    k, v = line.strip().split()
    v = int(v)

    sum_dict[k] = sum_dict.get(k, 0) + v

for k in sum_dict:
    print(k, sum_dict[k])
7️⃣ Average Per Key
#!/usr/bin/env python3
import sys

data = {}

for line in sys.stdin:
    k, v = line.strip().split()
    v = int(v)

    if k not in data:
        data[k] = [0, 0]  # sum, count

    data[k][0] += v
    data[k][1] += 1

for k in data:
    total, count = data[k]
    print(k, total / count)
8️⃣ Sort By Value (Descending)
#!/usr/bin/env python3
import sys

records = []

for line in sys.stdin:
    k, v = line.strip().split()
    records.append((k, int(v)))

records.sort(key=lambda x: x[1], reverse=True)

for r in records:
    print(r[0], r[1])
🚀 Same Run Command For ALL
chmod +x mapper.py reducer.py
dos2unix mapper.py reducer.py
hdfs dfs -rm -r /output

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
-files mapper.py,reducer.py \
-mapper "python3 mapper.py" \
-reducer "python3 reducer.py" \
-input /inputfile \
-output /output
