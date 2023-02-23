from functools import cmp_to_key


def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers.sort(key=cmp_to_key(compare))
    answer = str(int("".join(numbers)))
    return answer


def compare(a,b):
    s1 = int(a+b)
    s2 = int(b+a)
    
    if s1 < s2:
        return 1
    elif s1 > s2:
        return -1
    else:
        return 0

print(solution([3, 30, 34, 5, 9]))