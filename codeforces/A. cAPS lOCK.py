# Name   :   cAPS lOCK
# URL    :   https://codeforces.com/problemset/problem/131/A
# Github :   https://github.com/AfshinMoussavi

string = input()

if string == string.upper():
    print(string.lower())
else:
    if len(string) == 1:
        if string == string.lower():
            print(string.upper())
        else:
            print(string.lower())
    else:
        char_1 = string[0]
        char_n = string[1:]
        if char_1.islower() and char_n.isupper():
            print(string.title())
        else:
            print(string)
