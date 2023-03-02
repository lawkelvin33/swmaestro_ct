from collections import deque
def solution(name):
    answer = 0
    min_ = len(name)
    
    for n in name:
        answer += min(ord(n)-65,91-ord(n))
    
    n = []
    dest = ['A']*len(name)
    for i in name:
        n.append(i)
    n[0] = 'A'

    queue = deque([[n,0,0]]) ###  [n, # of movements, curr]
    while queue:
        s,num,curr = queue.popleft()
        if s == dest:
            min_ = min(min_,num)
        else:
            for i in range(1,len(name)):
                r = (curr + i) % len(name)
                if s[r] != 'A':
                    r_s = []
                    for a in s:
                        r_s.append(a)
                    r_s[r] = 'A'
                    #print(r_s)
                    queue.append([r_s,i+num,r])
                    break
            for i in range(1,len(name)):
                l = (curr - i) % len(name)
                if s[l] != 'A':
                    l_s = []
                    for a in s:
                        l_s.append(a)
                    l_s[l] = 'A'  
                    #print(l_s)  
                    queue.append([l_s,i+num,l])
                    break
    return answer+ min_
print(solution('JEROEN'))


### 시간 되면 이 코드를 한번 이해해보자!
'''def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer'''