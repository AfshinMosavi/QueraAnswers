# Name   :   Petya and Strings
# URL    :   https://codeforces.com/problemset/problem/112/A
# Github :   https://github.com/AfshinMoussavi

database = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
string_1 = input().lower()
string_2 = input().lower()


if string_1 == string_2:
    print(0)
else:
    count_1 = 0
    count_2 = 0
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            char_1 = string_1[i]
            char_2 = string_2[i]
            index_1 = database.index(char_1)
            index_2 = database.index(char_2)
            if index_1 < index_2:
                print(-1)
                break
            else:
                print(1)
                break
