
t=int(input())
while t>0:
    t-=1
    s=input()
    kt = True
    for i in s:
        if i!='4' and i!='7':
            kt = False
            break
    if kt == True:
        print('YES')
    else :
        print('NO')
