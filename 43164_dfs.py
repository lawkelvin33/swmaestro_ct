#dfs로 푸는 것이 맞을듯
from collections import deque
def solution(tickets):
    #creating graph
    graph = dict([])
    for t in tickets:
        if t[0] in graph:
            graph[t[0]].append(t[1])
        else:
            graph[t[0]] = [t[1]]
    #sorting vertices
    for g in graph:
        graph[g].sort(reverse=True)
    print(graph)
    
    stack = deque([])
    for t in graph['ICN']:
        v = set([('ICN',t)])
        stack.append((1,['ICN',t],v))
    
    while stack:
        t,r,v = stack.pop()
        print(t,r,v)
        if t == len(tickets):
            return r
        else:
            if r[-1] in graph:
                for i in graph[r[-1]]:
                    if (r[-1],i) not in v:
                        stack.append((t+1,r+[i],v.union(set([(r[-1],i)]))))
print(solution([["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]]))