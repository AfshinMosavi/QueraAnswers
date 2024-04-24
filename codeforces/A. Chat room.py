# Name   :   Chat room
# URL    :   https://codeforces.com/problemset/problem/58/A
# Github :   https://github.com/AfshinMoussavi
string = input()

validate = ['h', 'e', 'l', 'o']

flag = True
for char in validate:
    if char == 'l':
        if string.count(char) < 2:
           flag = False
    else:
        if char not in string:
            flag = False

if flag == False:
    print('NO')
else:
    try:
        index_h = string.index('h')
        
        string = string[index_h+1:]
        
        index_e = string.index('e')
        
        string = string[index_e+1:]
        
        index_l = string.index('l')
        
        string = string[index_l+1:] 
        
        index_l_l = string.index('l')
        
        string = string[index_l_l+1:]
        
        index_o = string.index('o')        
    except:
        print('NO')
    else:
        print('YES')
