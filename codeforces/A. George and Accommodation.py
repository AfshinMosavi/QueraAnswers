# Name   :   George and Accommodation
# URL    :   https://codeforces.com/problemset/problem/467/A
# Github :   https://github.com/AfshinMoussavi

count_test = int(input())

result = 0
for _ in range(count_test):
    count, Capacity = map(int, input().split())
    if count + 2 <= Capacity:
        result += 1
print(result)
