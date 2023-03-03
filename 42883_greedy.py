def solution(number, k):
    stack = []
    for num in number:
        if stack and int(stack[-1]) < int(num) and k>0:
            while stack and k > 0:
                if int(stack[-1]) < int(num):
                    stack.pop()
                    k -= 1
                else:
                    break
        stack.append(num)
    if k!=0:
        stack = stack[:-k]
    return ''.join(stack)
        