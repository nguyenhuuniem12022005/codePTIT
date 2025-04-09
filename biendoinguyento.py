from math import sqrt

# Tạo danh sách số nguyên tố bằng Sàng Eratosthenes
N = 110000
nt, NT = [], [1] * N
NT[0] = NT[1] = 0  # 0 và 1 không phải số nguyên tố

for i in range(2, int(sqrt(N)) + 1):
    if NT[i]:
        for j in range(i * i, N, i):
            NT[j] = 0

for i in range(N):
    if NT[i]:
        nt.append(i)

# Đọc input
n, a = int(input()), list(map(int, input().split()))

# Tìm khoảng cách lớn nhất đến số nguyên tố gần nhất
M = 0
for i in a:
    m = nt[-1]  # Khởi tạo khoảng cách lớn nhất
    for j in nt:
        m = min(m, abs(j - i))  # Tìm số nguyên tố gần nhất
        if j > i and abs(j - i) > m:  # Dừng sớm nếu vượt qua khoảng cách nhỏ nhất
            break
    M = max(M, m)  # Cập nhật khoảng cách lớn nhất

print(M)
