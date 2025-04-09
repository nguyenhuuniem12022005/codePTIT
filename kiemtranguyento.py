import math


for t in range (int(input())):
        def nto(n):
            if n<2: 
                return 'NO'
            else:
                for i in range(2,int(math.sqrt(n))+1):
                    if n%i==0: return 'NO'
            return 'YES'
        print(nto(int(input()[-4:])))