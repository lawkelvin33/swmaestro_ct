from itertools import permutations
def solution(k, dungeons):
    answer = 0
    poss = permutations(dungeons)
    for p in poss:
        tmp = 0
        health = k
        for i in p:
            if i[0]<= health:
                health -= i[1]
                tmp += 1
        if answer < tmp:
            answer = tmp
    return answer