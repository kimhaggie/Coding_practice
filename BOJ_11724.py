#11724
import sys
from collections import deque

def BFS(visit, N, E, deq):
    while len(deq)!=0:
        cur = deq.popleft()
        for val in E[cur]:
            if not visit[val]:
                deq.append(val)
                visit[val] = True
        

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    a-=1
    b-=1
    E[a].append(b)
    E[b].append(a)
visit = [False for _ in range(N)]
ans = 0
deq = deque()
for i in range(N):
    if not visit[i]:
        deq.append(i)
        visit[i] = True
        BFS(visit,N,E,deq)
        ans+=1
print(ans)