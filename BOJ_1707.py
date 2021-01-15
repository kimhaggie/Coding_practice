#1707
import sys
from collections import deque

def BFS(visit, N, E, deq):
    while len(deq)!=0:
        cur = deq.popleft()
        cur_col = visit[cur]
        if cur_col == 1:
            next_col = 2
        else:
            next_col = 1
        for val in E[cur]:
            if visit[val] == 0:
                visit[val] = next_col
                deq.append(val)
            else:
                if visit[val] != next_col:
                    return False
    return True 
        
K = int(sys.stdin.readline().rstrip('\n'))
for _ in range(K):
    V, E = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    visit = [0 for _ in range(V)]
    e = [[] for _ in range(V)]
    for _ in range(E):
        a, b = map(int,sys.stdin.readline().rstrip('\n').split(' '))
        a-=1
        b-=1
        e[a].append(b)
        e[b].append(a)
    ans = True
    for i in range(V):
        deq = deque()
        if visit[i] == 0:
            visit[i] = 1
            deq.append(i)
            result = BFS(visit, V, e, deq)
            if not result:
                ans = False
                print('NO')
                break
    if ans:
        print('YES')
