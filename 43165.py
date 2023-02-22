def solution(numbers, target):
    
    return dfs(numbers,0,target,0)

def dfs(numbers, index, target, total):
    if index == len(numbers):
        if total == target:
            return 1
        else:
            return 0
    return dfs(numbers, index + 1, target, total + numbers[index]) + dfs(numbers, index + 1, target, total - numbers[index])

## 전형적인 dfs 문제 ##
## 200만 정도의 iteration