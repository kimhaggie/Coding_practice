def solution(triangle):
    answer = 0
    dp = [[] for _ in range(len(triangle))]
    dp[0] = triangle[0]
    for level in range(1,len(triangle)):
        dp[level] = [0 for _ in range(len(triangle[level]))] 
    for level in range(1,len(triangle)):
        cur = triangle[level]
        for idx in range(len(cur)):
            if idx == 0:
                dp[level][idx] = dp[level-1][idx]+cur[idx]
            elif idx == len(cur)-1:
                dp[level][idx] = dp[level-1][idx-1]+cur[idx]
            else:
                dp[level][idx] = max(dp[level-1][idx-1],dp[level-1][idx])+cur[idx]
    return max(dp[level])

traingle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(traingle))