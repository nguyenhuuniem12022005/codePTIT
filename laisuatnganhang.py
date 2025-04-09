t=int(input())
for _ in range(t):
    n,x,m =map(float,input().split())
    years = 0
    while n<m:
        n+=n*(x/100)
        years += 1

    print (years)    