def solution(N, number):
    answer = 0
    cnt = [set([]) for _ in range(9)]
    for i in range(1,9):
        cnt[i].add(int(str(N)*i)) ## N*i의 case를 먼저 삽입
        for j in range(1,i):
            for a in cnt[j]:
                for b in cnt[i-j]:
                    cnt[i].add(a+b)
                    cnt[i].add(a-b)
                    cnt[i].add(a*b)
                    if b!=0:
                        cnt[i].add(a//b)
                    
        if number in cnt[i]:
            return i
                    
    return -1
print(solution(2,11))