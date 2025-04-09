def is_palindrome(s):
    return s == s[::-1]

def has_only_even_digits(s):
    for digit in s:
        if digit not in "02468":
            return False
    return True

t = int(input()) 

for _ in range(t):
    N = int(input())  
    length_N = len(str(N))

    if length_N % 2 == 0:
        result = []
        
       
        for num in range(22, N):
            str_num = str(num)
            
            if is_palindrome(str_num) and has_only_even_digits(str_num):
                result.append(str_num)

        
        print(" ".join(result))
