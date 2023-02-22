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

##모범 답안##
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
    
    ## solutions를 앞에서부터 하나씩 줄여나가면서 동시에 target의 수도 바꿔나가 계산하는 것이 핵심 ##
