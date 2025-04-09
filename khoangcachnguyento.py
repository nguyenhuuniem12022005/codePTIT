def is_prime(n):
  
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def first_n_primes(n):
   
    primes = []
    num = 2 
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


N, X = map(int, input().split())


prime_list = first_n_primes(N)


sequence = [X]  
for prime in prime_list:
    sequence.append(sequence[-1] + prime)  


print(*sequence)
