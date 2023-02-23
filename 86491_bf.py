def solution(sizes):
    max_ = []
    min_ = []
    for s in sizes:
        max_.append(max(s))
        min_.append(min(s))
    return max(max_) * max(min_)
#7분