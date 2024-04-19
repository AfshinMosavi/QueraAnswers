# Name   :   Ultra-Fast Mathematician
# URL    :   https://codeforces.com/problemset/problem/61/A
# Github :   https://github.com/AfshinMoussavi

string_1 = input()
string_2 = input()

result = ''

for i in range(len(string_1)):
    if string_1[i] == string_2[i]:
        result += '0'
    else:
        result += '1'

print(result)
