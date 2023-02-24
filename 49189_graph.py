from collections import deque
def solution(n, edge):
    distances = dict([])
    max_ = 0
    graph = dict([])
    visited = [0]*(n+1)
    queue = deque([])
    for i in edge: #graph를 dictionary:set의 형태로 만들기
        if i[0] in graph:
            graph[i[0]].add(i[1])
        else:
            graph[i[0]] = set([i[1]])
        if i[1] in graph:
            graph[i[1]].add(i[0])
        else:
            graph[i[1]] = set([i[0]])
    queue.append((1,0))
    visited[1] = 1
    while queue:
        curr,dist = queue.popleft()
        if dist in distances:
            distances[dist] += 1
        else:
            distances[dist] = 1
        if max_ < dist:
            max_ = dist
        for i in graph[curr]:
            if visited[i] == 0:
                queue.append((i,dist+1))
                visited[i] = 1
    return distances[max_]