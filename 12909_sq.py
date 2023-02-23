from collections import deque
def solution(s):
    
    s = deque(s)
    if not s:
        return True
    stack = deque([s.popleft()])
    while s:
        t = s.popleft()
        if t == '(':
            stack.append(t)
        else:
            if stack:
                if stack[-1] == '(':
                    stack.pop()
            else:
                return False
    if stack:
        return False
    return True
solution('()())(()')