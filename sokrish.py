from math import factorial

for _ in range(int(input())):
    n = input()
    print("Yes" if int(n) == sum(factorial(int(i)) for i in n) else "No")
