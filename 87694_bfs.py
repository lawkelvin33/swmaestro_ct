from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    maps = [[0 for _ in range(102)] for _ in range(102)]
    #creating map
    for r in rectangle: # 전체 범위 추가
        x1,y1,x2,y2 = r
        for i in range(2*x1,2*x2+1):
            for j in range(2*y1,2*y2+1):
                maps[i][j] = 1
    for r in rectangle: # 내부 범위 삭제
        x1,y1,x2,y2 = r
        for i in range(2*x1+1,2*x2):
            for j in range(2*y1+1,2*y2):
                maps[i][j] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    queue = deque([(characterX*2,characterY*2,0)])
    maps[characterX*2][characterY*2] = 0
    while queue:
        x,y,d = queue.popleft()
        if x == itemX*2 and y == itemY*2:
            answer = d//2
            break
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if maps[tx][ty] == 1:
                queue.append((tx,ty,d+1))
                maps[tx][ty] = 0
    return answer
                