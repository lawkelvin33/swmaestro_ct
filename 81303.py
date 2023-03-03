from collections import deque
def solution(n, k, cmd):
    answer = ''
    deleted = [] #binary search 이용해야할듯
    linked_list = {i:[i-1,i+1] for i in range(n)}
    for c in cmd:
        if c == 'C':
            deleted.append((linked_list[k][0],linked_list[k][1],k))
            #(prev,next,idx)
            prev,next = linked_list[k]
            if prev != -1:
                linked_list[prev][1] = next
            if next != n:
                linked_list[next][0] = prev
                k = next
            else:
                k = prev
        elif c == 'Z': #복원
            tmp_prev,tmp_next,tmp_idx = deleted.pop()
            if tmp_prev != -1:
                linked_list[tmp_prev][1] = tmp_idx
            if tmp_next != n:
                linked_list[tmp_next][0] = tmp_idx
        else:
            cm,num = c.split()
            num = int(num)
            if cm == 'U':
                for i in range(num):
                    k = linked_list[k][0]
            else:
                for i in range(num):
                    k = linked_list[k][1]
    while linked_list[k][0] > -1:
        k = linked_list[k][0]
    for i in range(n):
        if k > i:
            answer += 'X'
        else:
            answer += 'O'
            k = linked_list[k][1]
                
        
    return answer
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))