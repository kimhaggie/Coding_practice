#2146
import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def change_map(m,N,i,j,val,dot):
    deq = []
    deq.append([i,j])
    dot.append([i,j])
    m[i][j] = val
    while len(deq)!=0:
        cur_i,cur_j = deq.pop()
        for idx in range(4):
            next_i = cur_i+dy[idx]
            next_j = cur_j+dx[idx]
            if 0<=next_i<N and 0<=next_j<N and m[next_i][next_j]=='1':
                m[next_i][next_j]=val
                deq.append([next_i,next_j])
                dot.append([next_i,next_j])

N = int(sys.stdin.readline().rstrip('\n'))
m = []
d = []
for _ in range(N):
    x = sys.stdin.readline().rstrip('\n').split(' ')
    m.append(x)
    d.append(list(map(int,x)))
deq = []
val = 1
for i in range(N):
    for j in range(N):
        if d[i][j]==0:
            d[i][j]=-1
        elif d[i][j]==1:
            d[i][j]=0
        if m[i][j]=='1':
            change_map(m,N,i,j,val,deq)
            val += 1
        elif m[i][j]=='0':
            m[i][j]=0
        else:
            continue
connect = False
step = 1
ans = float('inf')
while not connect:
    next_deq = []
    while len(deq)!=0:
        i,j=deq.pop()
        cur_val = m[i][j]
        cur_step = d[i][j]
        for idx in range(4):
            next_i = i+dy[idx]
            next_j = j+dx[idx]
            if 0<=next_i<N and 0<=next_j<N and m[next_i][next_j]==0:
                m[next_i][next_j] = cur_val
                d[next_i][next_j] = step
                next_deq.append([next_i,next_j])
            elif 0<=next_i<N and 0<=next_j<N and m[next_i][next_j]!=cur_val:
                connect=True
                if d[next_i][next_j]+cur_step<ans:
                    ans = d[next_i][next_j]+cur_step
    deq=next_deq
    step+=1
print(ans)