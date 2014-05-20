rm result
cat Hierarchy_d2D_10000.txt | ./mapper.py | sort -t $'\t' -k1,1 -k2,2 | ./reducer.py >> result
