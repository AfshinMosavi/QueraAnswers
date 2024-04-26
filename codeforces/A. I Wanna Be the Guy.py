# Name   :   I Wanna Be the Guy
# URL    :   https://codeforces.com/problemset/problem/469/A
# Github :   https://github.com/AfshinMoussavi

count_mission = int(input())

result = []
q_level = list(map(int, input().split()))
p_level = list(map(int, input().split()))
q_level.pop(0)
p_level.pop(0)


for item in q_level:
    if item not in result:
        result.append(item)
for item in p_level:
    if item not in result:
        result.append(item)

result = sorted(result)
validation = [number for number in range(1,count_mission+1)]

if result == validation:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')

