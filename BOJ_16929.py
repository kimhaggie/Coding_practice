#16929
import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def DFS(m,N,M,start_i,start_j,cur_i,cur_j,visit,val,depth):
    if cur_i==start_i and cur_j==start_j and depth>=4:
        return True
    for idx in range(4):
        next_i = cur_i + dy[idx]
        next_j = cur_j + dx[idx]
        if 0<=next_i<N and 0<=next_j<M and (not visit[next_i][next_j]) and m[next_i][next_j]==val:
            visit[next_i][next_j] = True
            sub_ans = DFS(m,N,M,start_i,start_j,next_i,next_j,visit,val,depth+1)
            if sub_ans:
                return True
            visit[next_i][next_j] = False
    return False


N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
for _ in range(N):
    m.append(list(sys.stdin.readline().rstrip()))
ans = False
for i in range(N):
    for j in range(M):
        visit = [[False for _ in range(M)] for _ in range(N)]
        if DFS(m,N,M,i,j,i,j,visit,m[i][j],0):
            ans = True
            print('Yes')
            break
    if ans:
        break
if not ans:
    print('No')