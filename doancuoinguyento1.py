nt = [1 for x in range(10005)]
nt[0]=nt[1]=0
for i in range(2,10005):
    if nt[i]:
        for u in range(i,int(10005/i)): nt[i*u]=0
for t in range(int(input())):
    print('YES') if nt[int(input()[-4:])] else print('NO')