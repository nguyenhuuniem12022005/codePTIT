n,a=int(input()),sorted(list(map(int,input().split())))
huuniem2,huuniem3=a[-2]*a[-1],a[-3]*a[-1]*a[-2]
huuniem2=max(huuniem2,a[0]*a[1])
huuniem3=max(huuniem3,a[0]*a[1]*a[-1])
print(max(huuniem2,huuniem3))