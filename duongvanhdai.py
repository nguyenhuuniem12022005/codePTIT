# Nhập dữ liệu từ bàn phím

m = int(input())

v = int(input())

t = float(input())

d = input().strip()

# Tính quãng đường đi được
s = v * t

# Xác định vị trí dừng
if d == 'A':
    position = (m - int(s) % m) % m
elif d == 'C':
    position = int(s) % m
else:
    position = -1  # Trường hợp chiều không hợp lệ

# In kết quả
print("Result =", position)