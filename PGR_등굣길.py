def solution(m, n, puddles):
    answer = 0
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    dp[0][0]=1
    for i in range(m):
        for j in range(n):
            if [i+1,j+1] in puddles:
                dp[i][j]=0
                continue
            if i==0 and j==0:
                continue
            if i==0:
                dp[i][j] = (dp[i][j-1])%1000000007
            elif j==0:
                dp[i][j] = (dp[i-1][j])%1000000007
            else:
                dp[i][j] = (dp[i-1][j]+dp[i][j-1])%1000000007
    return dp[m-1][n-1]

#1000000007
m=4
n=3
puddles = [[2, 2]]	
print(solution(m,n,puddles))