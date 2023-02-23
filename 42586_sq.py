import math
from collections import deque


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    while progresses:
        ans = 1
        front = progresses.popleft()
        speed = speeds.popleft()
        time = math.ceil((100 - front) / speed)
        for i in range(len(progresses)):
            progresses[i] += speeds[i]*time #progresses 갱신
        while progresses:
            if progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                ans += 1
            else:
                break
        answer.append(ans)
    return answer