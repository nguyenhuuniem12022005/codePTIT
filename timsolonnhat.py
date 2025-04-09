import re


T = int(input())

for _ in range(T):
    s = input().strip()

    numbers = re.findall(r'\d+', s)
 
    max_number = max(int(num) for num in numbers)
    print(max_number)
