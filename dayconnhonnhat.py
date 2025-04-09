import math

def min_gcd_subarray_length(arr, n, k):
    min_len = float('inf')
    
    for i in range(n):
        current_gcd = arr[i]
        if current_gcd == k:
            min_len = min(min_len, 1)
            continue
        
        for j in range(i + 1, n):
            current_gcd = math.gcd(current_gcd, arr[j])
            
            if current_gcd == k:
                min_len = min(min_len, j - i + 1)
                break  
            elif current_gcd < k:
                break  

    return min_len if min_len != float('inf') else -1


def solve():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        
        
        has_valid = any(num % k == 0 for num in arr)
        if not has_valid:
            print(-1)
            continue
        
        result = min_gcd_subarray_length(arr, n, k)
        print(result)
if __name__ == '__main__':
    solve()