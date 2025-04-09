import re

a = {}  # Dictionary lưu số lần xuất hiện của từ
N = int(input())  # Nhập số dòng văn bản

# Đọc và xử lý từng dòng văn bản
for _ in range(N):
    line = input().lower()  # Chuyển thành chữ thường
    line = re.sub(r'\d', '', line)  # Loại bỏ tất cả chữ số
    words = re.split(r'[^a-z]', line)  # Tách từ, bỏ qua dấu câu và ký tự không phải chữ cái
    
    for word in words:
        if word:  # Nếu từ không rỗng
            a[word] = a.get(word, 0) + 1  # Đếm số lần xuất hiện của từ

# Sắp xếp danh sách theo số lần xuất hiện giảm dần, nếu bằng nhau thì theo thứ tự từ điển
ans = sorted(a.keys(), key=lambda x: (-a[x], x))

# In kết quả
for word in ans:
    print(word, a[word])
