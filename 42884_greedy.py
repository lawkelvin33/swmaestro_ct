from collections import deque
def solution(routes):
    answer = 0
    x_1 = sorted(routes,key=lambda x:x[1]) #exit 기준
    x_2 = sorted(routes,key=lambda x:x[0]) #entrance 기준
    x_2 = deque(x_2)
    exited = set([])
    for _1 in x_1:
        s1,d1 = _1
        if (s1,d1) not in exited:
            exited.add((s1,d1))
            answer += 1
            while x_2:
                s2,d2 = x_2[0]
                if (s2,d2) in exited:
                    x_2.popleft()
                else:
                    if d1 >= s2:
                        x_2.popleft()
                        exited.add((s2,d2))
                    else:
                        break
    
    return answer