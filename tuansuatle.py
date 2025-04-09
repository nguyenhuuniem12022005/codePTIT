T = int(input())  # Số lượng test case

for _ in range(T):
    N = int(input())  # Số lượng phần tử trong dãy (lẻ)
    A = list(map(int, input().split()))  # Dãy số A[]
    
    res = 0  # Biến lưu kết quả sau các phép XOR
    for num in A:
        res ^= num  # Thực hiện phép XOR
    
    print(res)  # In ra số có tần suất lẻ
