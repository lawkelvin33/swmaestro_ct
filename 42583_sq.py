from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 1 # time
    done = len(truck_weights)
    truck_weights = deque(truck_weights)
    curr_weight= truck_weights.popleft()
    bridge = deque([(curr_weight,1)])
    while done:
        answer += 1
        if len(bridge)>0 and bridge[0][1] == answer-bridge_length:
            we,_ = bridge.popleft()
            curr_weight -= we
            done-=1
        if len(truck_weights)>0 and curr_weight + truck_weights[0] <= weight:
            w = truck_weights.popleft()
            bridge.append((w,answer)) # 새 트럭 다리에 완전히 올라옴
            curr_weight += w
        
            
        
    return answer
# 2,10,[7,4,5,6] 8이어야하는데 3임