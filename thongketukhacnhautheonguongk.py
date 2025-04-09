import re

a = {}  # Dictionary lưu số lần xuất hiện của từ
N, K = map(int, input().split())  # Nhập số dòng N và số lần tối thiểu K

# Đọc và xử lý từng dòng văn bản
for _ in range(N):
    for s in re.split("[^a-z0-9]", input().lower()):  # Chuyển thành chữ thường và tách từ
        if s != '':  
            if a.get(s) is None: 
                a[s] = 1  # Nếu từ chưa có trong dictionary, thêm vào với giá trị 1
            else: 
                a[s] += 1  # Nếu từ đã tồn tại, tăng giá trị đếm lên 1

# Lọc các từ xuất hiện ít nhất K lần và sắp xếp theo yêu cầu
ans = sorted([w for w in a if a[w] >= K], key=lambda x: (-a[x], x))

# In kết quả
for i in ans:
    print(i, a[i])
