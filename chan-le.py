for t in range(int(input())):
    def check(n):
        s=int(n[0])
        for i in range(1,len(n)):
            if abs(int(n[i])-int(n[i-1])) != 2: return 'NO'
            s+=int(n[i])
        if s%10==0:
           return 'YES'
        else: 
           return 'NO'
    print(check(input()))