import re


T = int(input())

for _ in range(T):
    s = input().strip()

    numbers = re.findall(r'\d+', s)
 
    min_number = min(int(num) for num in numbers)
    print(min_number)
