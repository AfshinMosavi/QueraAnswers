# Name   :   Sum
# URL    :   https://codeforces.com/problemset/problem/1742/A
# Github :   https://github.com/AfshinMoussavi


def check(a:int, b:int, c:int):
    if a+b == c or a+c == b or b+c == a:
        return 'YES'
    return 'NO'
  
count_test = int(input())

for _ in range(count_test):
    a, b, c = map(int, input().split())
    print(check(a,b,c))
