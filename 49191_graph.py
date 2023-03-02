from collections import deque
def solution(n, results):
    answer = 0
    graph = [set([]) for _ in range(n+1)]
    n_f = [set([]) for _ in range(n+1)]
    n_t = [0 for _ in range(n+1)]
    
    for r in results:
        graph[r[0]].add(r[1])
    
    for i in range(1,n+1):
        # n_t 구하기 & n_f 만들기
        visited = [0 for _ in range(n+1)]
        stack = deque([i])
        visited[i] = 1
        
        n_t[i] = -1
        
        while stack:
            s = stack.pop()
            n_t[i] += 1
            for g in graph[s]:
                if visited[g]==0:
                    stack.append(g)
                    n_f[g].add(i)
                    visited[g] = 1
        
    # n_f 구하기
    for i in range(1,n+1):
        if len(n_f[i]) + n_t[i] == n-1:
            answer += 1
        
    return answer

## vertex A 에서 도달 가능한 vertex의 수 (n_t)
## vertex A로 도달 가능한 vertex의 수 (n_f)
## n_t + n_f == n-1의 경우에 순위가 존재

## floyd-warshall 쓰면 된다는데 그게 먼지 까먹어서 그냥 나의 방식대로 품
## 25분 소요
## 1트만에 디버깅 없이 성공한건 정말 오랜만!