def solution(board):
    c = len(board)
    r = len(board[0])
    answer = 0
    dp = board
    for i in range(c):
        for j in range(r):
            if i == 0 or j == 0:
                if dp[i][j] != 1:
                    dp[i][j] = 0
            else:
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1
                else:
                    dp[i][j] = 0
            if dp[i][j] > answer:
                answer = dp[i][j]
    
    return answer*answer