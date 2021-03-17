#17069
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations

ans = 0

def compute(i,j):
    #가로
    if j > 0 and m[i][j]==0:
        dp[i][j][0] = dp[i][j-1][2] + dp[i][j-1][0]
    #세로
    if i > 0 and m[i][j]==0:
        dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
    #대각선
    if i > 0 and j > 0 and (m[i][j]==0 and m[i-1][j]==0 and m[i][j-1]==0):
        dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

N = int(sys.stdin.readline().rstrip('\n'))
m = []
for i in range(N):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split()))
    m.append(x)
dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1
for j in range(2,N):
    compute(0,j)
for i in range(1,N):
    for j in range(N):
        compute(i,j)
print(sum(dp[N-1][N-1]))