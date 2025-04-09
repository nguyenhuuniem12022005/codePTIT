import sys

# Đọc dữ liệu đầu vào, tách thành danh sách số nguyên
numbers = list(map(int, sys.stdin.read().split()))

# Dùng set để lưu các số dư khác nhau khi chia 42
distinct_remainders = {num % 42 for num in numbers}

# In số lượng phần tử khác nhau
print(len(distinct_remainders))