from collections import deque
def solution(n, wires):
    answer = n
    
    for w in wires:
        graph = [set([]) for _ in range(n+1)]

        for w_ in wires:
            graph[w_[0]].add(w_[1])
            graph[w_[1]].add(w_[0])

        graph[w[0]].remove(w[1])
        graph[w[1]].remove(w[0])

        v = [0 for _ in range(n+1)]

        cnt = 0
        queue = deque([w[0]])
        v[w[0]] = 1

        while queue:
            curr = queue.popleft()
            cnt += 1
            for g in graph[curr]:
                if v[g]==0:
                    v[g] = 1
                    queue.append(g)
        answer = min(answer,abs(n-2*cnt))




    return answer

print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))