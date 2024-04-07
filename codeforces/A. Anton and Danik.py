# Name   :   Anton and Danik
# URL    :   https://codeforces.com/problemset/problem/734/A
# Github :   https://github.com/AfshinMoussavi

len_string = int(input())
string = input()


db = {'A':0, 'D':0}

for char in string:
    if char == 'D':
        db['D'] += 1
    else:
        db['A'] += 1

if db['D'] - db['A'] > 0:
    print('Danik')
elif db['D'] - db['A'] < 0:
    print('Anton')
else:
    print('Friendship')