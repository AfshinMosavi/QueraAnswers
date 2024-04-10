# Name   :   Wrong Subtraction
# URL    :   https://codeforces.com/problemset/problem/977/A
# Github :   https://github.com/AfshinMoussavi

number, count = map(int, input().split())

for _ in range(count):
    digit = number % 10
    
    if digit > 0 :
        number -= 1
    else:
        number //= 10
print(number)
