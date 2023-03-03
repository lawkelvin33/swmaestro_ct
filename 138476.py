def solution(k, tangerine):
    answer = 0
    cnt = 0
    counts = dict([])
    size_cnt = []
    #create counter
    for t in tangerine:
        if t in counts:
            counts[t] += 1
        else:
            counts[t] = 1
    for t in counts:
        size_cnt.append((counts[t],t)) #(개수,size)
    size_cnt.sort(reverse=True) #내림차순
    for i in range(len(size_cnt)):
        cnt += size_cnt[i][0]
        if cnt >= k:
            return i+1