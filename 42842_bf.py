from math import sqrt


def solution(brown, yellow):
    answer = []
    for i in range(1,int(sqrt(yellow))+1):
        if yellow % i == 0: #나누어 떨어짐
            if 2*i + 2*yellow/i + 4 == brown:
                answer = [int(yellow/i)+2,i+2]
    return answer