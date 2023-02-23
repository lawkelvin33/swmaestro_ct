import heapq


def solution(jobs):
    answer = 0
    total = len(jobs)
    heapq.heapify(jobs)
    running = []
    time = 0
    while len(jobs)>0 or len(running)>0:
        while True:
            if len(jobs) > 0 and time >= jobs[0][0]:
                a,b = heapq.heappop(jobs)
                heapq.heappush(running,(b,a))
            else:
                break
        if len(running) == 0:
            time = jobs[0][0]
            continue
        time_taken, start_time = heapq.heappop(running)
        if time < start_time:
            time = start_time + time_taken
        else:
            time += time_taken
        answer += time - start_time
    answer /= total
    return int(answer)