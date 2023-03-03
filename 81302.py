from collections import deque
def solution(places):
    answer = [1 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            places[i][j] = list(places[i][j])
            
    for p in range(len(places)):
        for i in range(5):
            for j in range(5):
                if places[p][i][j] == 'P' and bfs(places[p],i,j):#지키지 않은 경우
                    answer[p] = 0
                    break
            if answer[p] == 0:
                break
            
    return answer
def bfs(maps,i,j): #거리 2 내에 있을 경우 true를 return함
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    queue = deque([(i,j,0)]) #(x,y,distance)
    maps[i][j] = 'X'
    while queue:
        x,y,d = queue.popleft()
        if d <= 2:
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if 0<=tx<5 and 0<=ty<5:
                    if maps[tx][ty] == 'O':
                        maps[tx][ty] = 'X'
                        queue.append((tx,ty,d+1))
                    elif maps[tx][ty] == 'P' and d<=1:
                        return True
        else:
            return False
                        
                
        
        