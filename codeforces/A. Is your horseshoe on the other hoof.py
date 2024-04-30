# Name   :   Is your horseshoe on the other hoof?
# URL    :   https://codeforces.com/problemset/problem/228/A
# Github :   https://github.com/AfshinMoussavi

db = {}
numbers = list(map(int, input().split()))

for item in numbers:
    if item not in db.keys():
        db[item] = 1
    else:
        db[item] += 1

if len(db) >= 4:
    print(0)
else:
    print(4 - len(db))
