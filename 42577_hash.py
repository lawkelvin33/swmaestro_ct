def solution(phone_book):
    answer = True
    hash_ = [set([]) for _ in range(21)]
    for p in phone_book:
        hash_[len(p)].add(p)
    for i in range(20,0,-1):
        for j in hash_[i]:
            for k in range(i-1,0,-1):
                if j[:k] in hash_[k]:
                    return False
    return answer