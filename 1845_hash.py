def solution(nums):
    answer = 0
    unique = set(nums)
    if len(unique) <= len(nums)//2:
        return len(unique)
    else:
        return len(nums)//2