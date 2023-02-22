from collections import deque


def solution(n, computers):
    answer = 0
    stack = deque([])
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            visited[i] = 1
            stack.append(i)
            while stack:
                tmp = stack.pop()
                for j in range(n):
                    if computers[tmp][j] == 1 and visited[j] == 0:
                        visited[j] = 1
                        stack.append(j)
    return answer

#전형적인 graph traversal dfs문제
#stack 이용하였음