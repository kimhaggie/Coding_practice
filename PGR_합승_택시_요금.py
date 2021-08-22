#12:00

import heapq as h

def solution(n, s, a, b, fares):
    answer = 0
    s-=1
    a-=1
    b-=1
    edge = [[] for _ in range(n)]
    for f in fares:
        x,y,w = f
        x-=1
        y-=1
        edge[x].append([y,w])
        edge[y].append([x,w])
    dijkstra = [[float('inf') for _ in range(n)] for _ in range(n)]
    for idx,start in enumerate(range(n)):
        heap = []
        h.heappush(heap,[0,start])
        while heap:
            cur_w, cur_node = h.heappop(heap)
            if dijkstra[idx][cur_node]==float('inf'):
                dijkstra[idx][cur_node]=cur_w
            else:
                continue
            for x,w in edge[cur_node]:
                if cur_w+w<dijkstra[idx][x]:
                    h.heappush(heap,[cur_w+w,x])
    answer =float('inf')
    for middle in range(n):
        answer = min(answer,dijkstra[s][middle]+dijkstra[middle][a]+dijkstra[middle][b])
    return answer

n=6
s=4
a=6
b=2
fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

n=6
s=4
a=5
b=6
fares=[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(n,s,a,b,fares))