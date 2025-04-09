def sort_courses(courses):
    # Sắp xếp danh sách theo mã môn (thứ tự từ điển)
    courses.sort(key=lambda x: x[0])
    return courses

# Nhập số môn học
N = int(input().strip())

# Khởi tạo danh sách để lưu thông tin môn học
courses = []

# Nhập dữ liệu môn học
for _ in range(N):
    course_code = input().strip()  # Mã môn học
    course_name = input().strip()  # Tên môn học
    exam_type = input().strip()    # Hình thức thi

    # Thêm vào danh sách dưới dạng tuple
    courses.append((course_code, course_name, exam_type))

# Sắp xếp danh sách theo mã môn
sorted_courses = sort_courses(courses)

# In kết quả sau khi sắp xếp
for course in sorted_courses:
    print(course[0], course[1], course[2])
