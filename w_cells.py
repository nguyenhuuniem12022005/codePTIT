def max_visible_white_cells(n, k):
    # Trường hợp đặc biệt khi n = 1
    if n == 1:
        return min(k, 1)

    # Tính số ô bề mặt tối đa
    surface_cells = 6 * n * n - 12 * n + 8

    # Số ô trắng hiển thị tối đa là min(k, surface_cells)
    return min(k, surface_cells)

# Đọc dữ liệu vào
n, k = map(int, input().split())

# Tính và in kết quả
print(max_visible_white_cells(n, k))
