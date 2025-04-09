from math import sqrt



for t in range(int(input())):
    def nto(s):
        if s<=1:return 'NO'
        for i in range(2,int(sqrt(s))+1):
            if s%i==0: return 'NO'
        return 'YES' 
    def tcs(n):
        s=0
        for i in n:s+=int(i)
        return nto(s)
    print(tcs(input()))   
    