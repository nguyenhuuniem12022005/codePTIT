import sys
import math

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]

def count_numbers_with_9_divisors(N):
    primes = sieve(int(math.sqrt(N)) + 1)
    count = 0
    
    # Check numbers of the form p^8
    for p in primes:
        p8 = p ** 8
        if p8 > N:
            break
        count += 1
    
    # Check numbers of the form p^2 * q^2
    prime_len = len(primes)
    for i in range(prime_len):
        p2 = primes[i] ** 2
        if p2 > N:
            break
        for j in range(i + 1, prime_len):
            q2 = primes[j] ** 2
            if p2 * q2 > N:
                break
            count += 1
    
    return count

# Đọc dữ liệu đầu vào
N = int(sys.stdin.readline().strip())
print(count_numbers_with_9_divisors(N))
