from itertools import permutations


def solution(numbers):
    primes = [1]*10000000
    primes[0] = primes[1] = 0
    def isPrime(n): ## 에라토스테네스의 체 (이건 암기해야할듯))
        for i in range(2,n):
            if primes[i]:
                for j in range(i*2,n,i):
                    primes[j] = 0
    answer = 0
    numbers_ = []
    poss = []
    for n in numbers:
        numbers_.append(n)

    for i in range(1,len(numbers_)+1):
        poss += permutations(numbers_,i)
    poss = list(map(lambda x:int(''.join(x)), poss))
    poss = set(poss)
    max_ = max(poss)

    isPrime(max_+1)
    for p in poss:
        if primes[p]:
            print(p)
            answer += 1
    return answer