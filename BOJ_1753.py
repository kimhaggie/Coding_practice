#1753
import sys
import math
import heapq as h

V, E = map(int,sys.stdin.readline().rstrip('\n').split())
start = int(input())-1
edge = [[] for _ in range(V)]
for v in range(E):
    a,b,c = map(int,sys.stdin.readline().rstrip('\n').split())
    a-=1
    b-=1
    edge[a].append([b,c])
heap = []
h.heappush(heap,[0,start])
d = [float('inf') for _ in range(V)]
while heap:
    cur_d, cur_next = h.heappop(heap)
    if d[cur_next]!=float('inf'):
        continue
    if cur_d<d[cur_next]:
        d[cur_next] = cur_d
    for x,y in edge[cur_next]:
        h.heappush(heap,[y+cur_d,x])
for x in d:
    if x==float('inf'):
        print('INF')
    else:
        print(x)