def solution(n, lost, reserve):
    answer = 0
    
    # total 계산
    total = [1 for _ in range(n+1)]
    for l in lost:
        total[l] -= 1
    for r in reserve:
        total[r] += 1
    
    # 빌려주기
    for i in range(2,n+1):
        if total[i] == 2 and total[i-1] == 0:
            total[i] -= 1
            total[i-1] += 1
        if total[i-1]==2 and total[i] == 0:
            total[i-1] -= 1
            total[i] += 1

    for i in range(1,n+1):
        if total[i] > 0:
            answer += 1
            
    return answer