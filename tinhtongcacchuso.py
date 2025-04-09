for _ in range(int(input())):
    s = input()
    sum_digits = 0  # Tổng các chữ số
    letters = []  # Danh sách chữ cái

    for i in s:
        if i.isdigit():  # Kiểm tra nếu i là chữ số
            sum_digits += int(i)
        else:
            letters.append(i)

    # Sắp xếp chữ cái theo bảng chữ cái, ghép với tổng số cuối cùng
    print("".join(sorted(letters)) + str(sum_digits))
