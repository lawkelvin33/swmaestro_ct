from collections import deque


def solution(begin, target, words):
    set_ = set(words)
    set__ = set([begin])
    queue = deque([(begin,0)])
    while queue:
        tmp, diff = queue.pop()
        if tmp == target:
            return diff
        for i in set_:
            if i not in set__ and diff1(i,tmp): # different only by one letter
                queue.appendleft((i,diff+1))
                set__.add(i)
    return 0

def diff1(a,b):
    result = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            result += 1
    if result == 1:
        return True
    else:
        return False