import heapq
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    min_heap = []
    for i in range(len(prices)):
        while min_heap and min_heap[0][0] < -prices[i]:
            price,idx = heapq.heappop(min_heap)
            answer[idx] = i-idx
        heapq.heappush(min_heap,(-prices[i],i))
    while min_heap:
        price,idx = min_heap.pop()
        answer[idx] = len(prices)-1-idx
    return answer