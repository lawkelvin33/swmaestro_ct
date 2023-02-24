def solution(n, times):
    answer = 0
    min_, max_ = 1, n*max(times) #총 소요되는 시간의 min, max
    while min_ <= max_:
        mid = (min_ + max_) // 2 #binary search
        tmp = 0
        for t in times:
            tmp += mid//t # 처리한 총 인원
        if tmp >= n: #일단 조건 충족 but min 구하는 것이기 때문에 더 탐색
            answer = mid
            max_ = mid - 1
        else: #더 많은 시간 필요
            min_ = mid + 1
        
    return answer