# BDA Lab – Hadoop & Pig Programs

This repository contains:

- Week 3 – Basic Hadoop MapReduce Programs
- Week 4 – Aggregation Programs
- Week 5 – Apache Pig Scripts

## Technologies Used
- Hadoop Streaming
- Python
- Apache Pig

## How to Run

chmod +x mapper.py reducer.py  
dos2unix mapper.py reducer.py  

hadoop jar hadoop-streaming.jar \
-files mapper.py,reducer.py \
-mapper "python3 mapper.py" \
-reducer "python3 reducer.py" \
-input /input \
-output /output
