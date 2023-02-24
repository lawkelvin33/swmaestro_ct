from collections import deque
import heapq
def solution(genres, plays):
    answer = []
    gen = dict([])
    gen_cnt = dict([])
    for i in range(len(genres)):
        if genres[i] in gen_cnt:
            gen_cnt[genres[i]] += plays[i]
            heapq.heappush(gen[genres[i]],(-plays[i],i))
        else:
            gen_cnt[genres[i]] = plays[i]
            gen[genres[i]] = [(-plays[i],i)]
    tmp = []
    for g in gen_cnt:
        heapq.heappush(tmp,(-gen_cnt[g],g))
    while tmp:
        _,genre = heapq.heappop(tmp)
        if len(gen[genre]) > 1:
            t = [heapq.heappop(gen[genre]),heapq.heappop(gen[genre])]
            t.sort()
            for i in t:
                answer.append(i[1])
        else:
            _,idx = heapq.heappop(gen[genre])
            answer.append(idx)
    
    
    return answer

print(solution(["classic", "pop", "classic", "classic"],[800, 600, 150, 800]))



#[0, 3, 1]
