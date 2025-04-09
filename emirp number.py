from math import sqrt


maxVal = int(1e6 + 5)
p = [1] * maxVal
p[0] = p[1] = 0
for i in range(2, int(sqrt(maxVal)) + 1):
    if p[i]:
        for j in range(i * i, maxVal, i):
            p[j] = 0


primes = [i for i in range(11, maxVal) if p[i]]

for _ in range(int(input())):
    n = int(input())
    if n > maxVal:
        n = maxVal 

    for i in primes:
        if i >= n:
            break
        j = int(str(i)[::-1])
        if i < j and j < n and p[j]:  
            print(i, j, end=' ')
    print()
