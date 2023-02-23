from collections import deque
def solution(priorities, location):
    answer = 1
    max_tracker = sorted(priorities,reverse=True)
    # if max_tracker is not None:
    max_tracker = deque(max_tracker)
    priorities = deque(priorities)
    locations = [i for i in range(len(priorities))]
    locations = deque(locations)
    while priorities:
        print(priorities)
        print(max_tracker)
        print(locations)

        tmp = priorities.popleft()
        max_ = max_tracker.popleft()
        loc = locations.popleft()
        
        if max_ > tmp: # 더 중요한 것이 존재
            priorities.append(tmp)
            max_tracker.appendleft(max_)
            locations.append(loc)
        else: # 중요도가 젤 높음
            if loc == location:
                return answer
            else:
                answer += 1
            
print(solution([1,1,9,1,1,1],0))