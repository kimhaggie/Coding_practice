#1260
import sys
from collections import deque

def DFS(cur, visit, N, E, ans):
    ans.append(cur)
    visit[cur] = True
    poss = False
    for next in E[cur]:
        if not visit[next]:
            poss = True
            break
    if not poss:
        return 0
    for next in E[cur]:
        if visit[next]:
            continue
        DFS(next,visit,N,E,ans)

def BFS(visit, N, E, ans, deq):
    while len(deq)!=0:
        cur = deq.popleft()
        ans.append(cur)
        for val in E[cur]:
            if not visit[val]:
                deq.append(val)
                visit[val] = True
        

N, M, start = map(int,sys.stdin.readline().rstrip('\n').split(' '))
start-=1
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    a-=1
    b-=1
    E[a].append(b)
    E[b].append(a)
for idx in range(N):
    E[idx] = sorted(E[idx])
visit = [False for _ in range(N)]
ans = []
DFS(start,visit,N,E,ans)
for i in range(len(ans)):
    ans[i]+=1
print(' '.join(map(str,ans)))
visit = [False for _ in range(N)]
ans = []
deq = deque()
deq.append(start)
visit[start] = True
BFS(visit,N,E,ans,deq)
for i in range(len(ans)):
    ans[i]+=1
print(' '.join(map(str,ans)))