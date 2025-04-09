# Nhập số phần tử
n = int(input())

# Nhập mảng có thể trên nhiều dòng
a = []
while len(a) < n:
    a.extend(map(int, input().split()))

# Tách số chẵn và lẻ
even = [x for x in a if x % 2 == 0]
odd = [x for x in a if x % 2 == 1]

# Sắp xếp số chẵn tăng dần và số lẻ giảm dần
even.sort()
odd.sort(reverse=True)

# Tạo kết quả, giữ nguyên vị trí chẵn/lẻ
even_idx, odd_idx = 0, 0
result = []

for num in a:
    if num % 2 == 0:
        result.append(even[even_idx])
        even_idx += 1
    else:
        result.append(odd[odd_idx])
        odd_idx += 1

# In kết quả
print(' '.join(map(str, result)))
