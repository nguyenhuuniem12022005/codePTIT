def remaining_elements(n, arr):
    stack = []
    
    for num in arr:
        if stack and (stack[-1] + num) % 2 == 0:
            stack.pop() 
        else:
            stack.append(num)  
    
    return len(stack)

n = int(input())
arr = list(map(int, input().split()))


print(remaining_elements(n, arr))
