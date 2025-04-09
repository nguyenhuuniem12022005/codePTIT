def sort_students(students):
    # Sắp xếp danh sách theo thứ tự ưu tiên: số bài đúng (giảm dần), số submit (tăng dần), họ tên (tăng dần theo từ điển)
    students.sort(key=lambda x: (-x[1], x[2], x[0]))
    return students

# Đọc dữ liệu đầu vào
N = int(input().strip())
students = []

for _ in range(N):
    name = input().strip()
    C, T = map(int, input().strip().split())
    students.append((name, C, T))

# Sắp xếp danh sách sinh viên
sorted_students = sort_students(students)

# In kết quả
for student in sorted_students:
    print(student[0], student[1], student[2])
