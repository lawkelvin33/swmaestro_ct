def solution(participant, completion):
    answer = ''
    part = dict([])
    for p in participant:
        if p in part:
            part[p] += 1
        else:
            part[p] = 1
    for c in completion:
        if part[c] > 1:
            part[c] -= 1
        else:
            part.pop(c)
    for p in part:
        return p
#12분
#set를 쓰면 중복도 다 없어지는데, 이러면 비교가 어려워짐