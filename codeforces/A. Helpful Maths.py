# Name   :   Anton and Danik
# URL    :   https://codeforces.com/problemset/problem/339/A
# Github :   https://github.com/AfshinMoussavi

string = input()

db = {1:0, 2:0, 3:0}

for number in string:
    if number == '1':
        db[1] += 1
    elif number == '2':
        db[2] += 1
    elif number == '3':
        db[3] += 1

result = ''
for key, value in db.items():
    for number in range(value):
        result = result + f'{key}+'
print(result[0:-1])
