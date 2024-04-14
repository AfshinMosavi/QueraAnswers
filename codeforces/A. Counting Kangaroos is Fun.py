# Name   :   Counting Kangaroos is Fun
# URL    :   https://codeforces.com/problemset/problem/372/A
# Github :   https://github.com/AfshinMoussavi

import math

count_kangaroos = int(input())
kangaroos_db = []
for i in range(count_kangaroos):
    kangaroos_db.append(int(input()))

kangaroos_db = sorted(kangaroos_db)

if count_kangaroos % 2 == 0:
    mid = (count_kangaroos // 2) + 1
    left_db = kangaroos_db[0:mid]
    right_db = kangaroos_db[mid:]
else:
    mid = math.ceil(count_kangaroos // 2)
    left_db = kangaroos_db[0:mid]
    right_db = kangaroos_db[mid:]
