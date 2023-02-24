def solution(clothes):
    answer = 1
    cloth = dict([])
    for c in clothes:
        if c[1] in cloth:
            cloth[c[1]] += 1
        else:
            cloth[c[1]] = 1
    for c in cloth:
        answer *= (cloth[c]+1)
    answer -= 1
    return answer