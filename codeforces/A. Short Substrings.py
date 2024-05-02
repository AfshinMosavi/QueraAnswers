# Name   :   Short Substrings
# URL    :   https://codeforces.com/problemset/problem/1367/A
# Github :   https://github.com/AfshinMoussavi

count_string = int(input())

for _ in range(count_string):
    string = input()
    if len(string) == 2:
        print(string)
    else:
        new_string = string[2:]
        result = string[:2]
        for i in range(1,len(new_string), 2):
            result += new_string[i]
        print(result)
