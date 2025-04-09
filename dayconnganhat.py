import math
from sys import stdin

def find_min_subsequence_length(N, K, A):
    # Kiểm tra xem K có phải là ước của ít nhất một phần tử trong dãy không
    has_valid_element = any(a % K == 0 for a in A)
    if not has_valid_element:
        return -1
    
    min_length = float('inf')
    
    # Duyệt qua tất cả các dãy con liên tiếp
    for i in range(N):
        current_gcd = 0
        for j in range(i, N):
            current_gcd = math.gcd(current_gcd, A[j])
            if current_gcd == K:
                min_length = min(min_length, j - i + 1)
                break
            elif current_gcd < K:
                break
    
    return min_length if min_length != float('inf') else -1

def main():
    input = stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N, K = int(input[idx]), int(input[idx+1])
        idx += 2
        A = list(map(int, input[idx:idx+N]))
        idx += N
        result = find_min_subsequence_length(N, K, A)
        print(result)

if __name__ == "__main__":
    main()