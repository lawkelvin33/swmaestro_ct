import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    total = 0
    
    for o in operations:
        a,b = o.split()
        if a == "I":
            num = int(b)
            heapq.heappush(min_heap,num)
            heapq.heappush(max_heap,-num)
            total += 1
        else:
            if total > 0:
                if b == "1":
                    heapq.heappop(max_heap)
                else:
                    heapq.heappop(min_heap)
                total -= 1
            if total == 0: ## heap이 비었을 때 한번 refresh안해주면 오류생김
                min_heap = []
                max_heap = []
    if total == 0:
        answer = [0,0]
    elif total == 1:
        ret = heapq.heappop(min_heap)
        answer =  [ret,ret]
    else:
        max_ = heapq.heappop(max_heap)
        min_ = heapq.heappop(min_heap)
        answer = [-max_,min_]
    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))

#23분