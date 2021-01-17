#7576
import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(m,N,M,deq):
    sub_ans = 0
    while len(deq):
        sub_ans+=1
        i,j,d = deq.popleft()
        m[i][j] = '2'
        for x in range(4):
            next_i = i+dy[x]
            next_j = j+dx[x]
            if 0<=next_i<N and 0<=next_j<M and m[next_i][next_j]=='0':
                deq.append([next_i,next_j,d+1])
                m[next_i][next_j]='1'
    return [sub_ans,d]

M, N =map(int,sys.stdin.readline().rstrip().split(' '))
m = []
for _ in range(N):
    m.append(list(sys.stdin.readline().rstrip('\n').split(' ')))
num = 0
for i in range(N):
    for j in range(M):
        if m[i][j]=='0' or m[i][j]=='1':
            num+=1
ans = []
deq = deque()
for i in range(N):
    for j in range(M):
        if m[i][j]=='1':
            deq.append([i,j,0])
sub_ans,d = BFS(m,N,M,deq)
num-=sub_ans
ans.append(d)
if num==0:
    print(max(ans))
else:
    print(-1)