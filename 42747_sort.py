def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i:
            answer = len(citations)-i
            break
    print(citations)
    return answer

# n편중 h번 이상 인용된 논문이 h편이상, 나머지는 h번 이하 인용: max(h) => H-Index

# citations 정렬 -> nlogn -> 40,000 
# traverse 하면서 index와 비교
### iteration의 순서가 index에 맞춰져있으면 중간에 빠뜨릴 일이 없기 때문에 좋음!

print(solution([4,4,4]))