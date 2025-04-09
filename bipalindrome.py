def is_palindrome(s):
    return s == s[::-1]

def convert_to_base(n, base):
    if n == 0:
        return '0'
    digits = []
    while n > 0:
        digits.append(n % base)
        n = n // base
    return ''.join(map(str, reversed(digits)))

while True:
    line = input().strip()
    if line == '-1':
        break
    x, a, b = map(int, line.split())
    x_str_a = convert_to_base(x, a)
    x_str_b = convert_to_base(x, b)
    if is_palindrome(x_str_a) and is_palindrome(x_str_b):
        print("YES")
    else:
        print("NO")