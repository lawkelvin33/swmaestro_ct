def solution(answers):
    answer = []
    scores = [0,0,0]
    supo = [[1,2,3,4,5],
            [2,1,2,3,2,4,2,5],
            [3,3,1,1,2,2,4,4,5,5]
           ]
    
    for i in range(len(answers)):
        scores[0] += int(supo[0][i%5] == answers[i])
        scores[1] += int(supo[1][i%8] == answers[i])
        scores[2] += int(supo[2][i%10] == answers[i])
    
    for i in range(3):
        if scores[i] == max(scores):
            answer.append(i+1)
    answer.sort()
    
    return answer
print(solution([1,3,2,4,2]))