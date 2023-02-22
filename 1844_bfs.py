from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    queue = deque([])

    queue.appendleft((0,0,1)) ## (x,y,distance)
    maps[0][0] = 2
    
    while queue:
        x,y,d = queue.pop()
        if (x,y) == (n-1,m-1):
            return d
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            #if tx == n-1 and ty == m-1:
            #    return d+1
            if 0 <= tx < n and 0 <= ty < m: #맵 내부
                if maps[tx][ty] == 1:
                    maps[tx][ty] = 2 # 2 is visited
                    queue.appendleft((tx,ty,d+1))
    
    
    
    return -1

## uses bfs (implemented by queue)