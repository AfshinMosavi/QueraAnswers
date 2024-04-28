# Name   :   Beautiful Matrix
# URL    :   https://codeforces.com/problemset/problem/263/A
# Github :   https://github.com/AfshinMoussavi

database = []
for i in range(5):
    string = input().split(' ')
    if '1' in string:
        index = [i, string.index('1')]
    database.append(string)
    
validate_index = [2,2]

result = abs(index[0] - validate_index[0]) + abs(index[1] - validate_index[1])
print(result)
