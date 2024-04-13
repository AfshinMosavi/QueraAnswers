# Name   :   Anton and Danik
# URL    :   https://codeforces.com/problemset/problem/734/A
# Github :   https://github.com/AfshinMoussavi


cp, height = map(int, input().split())
db = list(map(int, input().split()))
result = 0
for i in db:
    if i <= height:
        result += 1
    else:
        result += 2
print(result)
