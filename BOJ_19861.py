#19861
import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(m,N,M,visit):
    deq = deque()
    deq.append([0,0,1])
    while len(deq)!=0:
        i,j,d = deq.popleft()
        if i==N-1 and j==M-1:
            return d
        for idx in range(4):
            next_i = i + dy[idx]
            next_j = j + dx[idx]
            if 0<=next_i<N and 0<=next_j<M and m[next_i][next_j]=='1' and (not visit[next_i][next_j]):
                visit[next_i][next_j] = True
                deq.append([next_i,next_j,d+1])

N, M =map(int,sys.stdin.readline().rstrip().split(' '))
m = []
for _ in range(N):
    m.append(list(sys.stdin.readline().rstrip('\n')))
visit = [[False for _ in range(M)] for _ in range(N)]
print(BFS(m,N,M,visit))