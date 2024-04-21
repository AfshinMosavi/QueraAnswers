# Name   :   Pangram
# URL    :   https://codeforces.com/problemset/problem/520/A
# Github :   https://github.com/AfshinMoussavi

db = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

result = []

len_string = int(input())
string = input()

for char in string:
    char = char.lower()
    if char not in result:
        result.append(char)

if db == sorted(result):
    print('YES')
else:
    print('NO')
