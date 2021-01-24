#9663
import sys
from collections import deque
import math

def check(m,i,j,N):
    #왼쪽 위
    cur_i = i
    cur_j = j
    while True:
        cur_i-=1
        cur_j-=1
        if not(0<=cur_i<N and 0<=cur_j<N):
            break
        if m[cur_i][cur_j]==1:
            return False
    #오른쪽 위
    cur_i = i
    cur_j = j
    while True:
        cur_i-=1
        cur_j+=1
        if not(0<=cur_i<N and 0<=cur_j<N):
            break
        if m[cur_i][cur_j]==1:
            return False
    #위
    cur_i = i
    cur_j = j
    while True:
        cur_i-=1
        if not(0<=cur_i<N):
            break
        if m[cur_i][cur_j]==1:
            return False
    return True

def DFS(start,m,n,N,col):
    if n==N:
        return 1
    ans = 0
    for j,val in enumerate(col):
        if val==0 and check(m,start,j,N):
            col[j]=1
            m[start][j]=1
            ans+=DFS(start+1,m,n+1,N,col)
            col[j]=0
            m[start][j]=0
    return ans

N = int(sys.stdin.readline().rstrip('\n'))
col = [0 for _ in range(N)]
m = [[0 for _ in range(N)] for _ in range(N)]
print(DFS(0,m,0,N,col))