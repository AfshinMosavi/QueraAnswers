# Name   :   Divisibility Problem
# URL    :   https://codeforces.com/problemset/problem/1328/A
# Github :   https://github.com/AfshinMoussavi

count_test = int(input())

for i in range(count_test):
    number_1, number_2 = map(int, input().split())
    
    if number_2 >= number_1:
        print(number_2 - number_1)
    elif number_1 % number_2 == 0:
        print(0)
    else:
        i = number_1 // number_2
        while  True:
            if number_2 * i > number_1:
                number_2 *= i
                break
            i += 1
        print(number_2 - number_1)
        
