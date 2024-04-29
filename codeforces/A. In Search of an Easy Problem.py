# Name   :   In Search of an Easy Problem
# URL    :   https://codeforces.com/problemset/problem/1030/A
# Github :   https://github.com/AfshinMoussavi

count_vote = int(input())

votes = list(map(int, input().split()))

if 1 in votes:
    print('HARD')
else:
    print('EASY')
