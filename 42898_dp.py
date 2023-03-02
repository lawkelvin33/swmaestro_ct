def solution(m, n, puddles):
    answer = 0
    pud = set([])
    for p in puddles:
        pud.add((p[0],p[1]))
    dp = [[0 for _ in range(n+2)] for _ in range(m+2)] ## m+1,n+1자리를 0으로 처리하여 계산을 하면 한번에 처리 가능!
    dp[m][n] = 1
    
        
    for p in pud:
        dp[p[0]][p[1]] = 0 # puddles => 0
    pud.add((m,n))
    for i in range(n,0,-1):
        for j in range(m,0,-1):
            if (j,i) not in pud:
                dp[j][i] = (dp[j+1][i] + dp[j][i+1]) % 1000000007 #dp
    answer = dp[1][1]
                
    return answer

## n,m의 자리를 전부 1로 처리하면 n,m에 있느 puddle 앞에 있는 dp들이 0이 아닌 1로 계산을 하게 됨