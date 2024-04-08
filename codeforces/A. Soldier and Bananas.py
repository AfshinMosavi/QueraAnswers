# Name   :   Soldier and Bananas
# URL    :   https://codeforces.com/problemset/problem/546/A
# Github :   https://github.com/AfshinMoussavi

cost_of_the_first_banana, dollars, count = map(int, input().split())

result = 0
for i in range(1, count+1):
    result += i*cost_of_the_first_banana

if result - dollars > 0:
    print(result - dollars)
else:
    print(0)
