#11725
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip('\n'))
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    E[a].append(b)
    E[b].append(a)
visit = [False for _ in range(N+1)]
parent = [0 for _ in range(N+1)]
visit[1] = True
stack = [1]
while stack:
    cur = stack.pop()
    for val in E[cur]:
        if not visit[val]:
            parent[val] = cur
            visit[val] = True
            stack.append(val)
for val in parent[2:]:
    print(val)
    