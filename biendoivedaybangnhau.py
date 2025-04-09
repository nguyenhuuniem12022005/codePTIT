n,a=int(input()),list(map(int,input().split()))
ind,min=0,10000000000
for i in range(n):
    sum=0
    for j in range(n):
        sum+=abs(a[i]-a[j])
    if sum<min:
        ind=i
        min=sum
print(min,a[ind])
        
