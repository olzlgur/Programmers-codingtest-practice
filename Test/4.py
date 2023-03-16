def solution(n, m, k):
    answer = -1
    dp = []
    for i in range(n):    
        dp.append([0]*(m+1))
    for i in range(1, k+1):
        dp[0][i] = 1

    for w in range(1, n):
        for i in range(1, k+1):
            for j in range(1, len(dp[0])):
                if j+i < len(dp[0]):
                    dp[w][j+i] += dp[w-1][j]
    return dp[n-1][-1] % 1000007


solution(3, 6, 3)