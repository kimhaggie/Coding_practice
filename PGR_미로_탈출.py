import heapq as h

def solution(n, start, end, roads, traps):
    start -=1
    end -=1
    for i,j in enumerate(traps):
        traps[i]=j-1
    graphs = [[] for _ in range(2**len(traps))]
    d = [[float('inf') for _ in range(n)] for _ in range(2**len(traps))]
    trap_dict = {trap : i for i,trap in enumerate(traps)}
    for idx in range(2**len(traps)):
        target = []
        for i in range(len(traps)):
            if 1<<i & idx:
                target.append(traps[i])
        graph = [[] for _ in range(n)]
        for road in roads:
            x,y,w=road
            x-=1
            y-=1
            if x in target and y in target:
                graph[x].append([y,w])
            elif x in target:
                graph[y].append([x,w])
            elif y in target:
                graph[y].append([x,w])
            else:
                graph[x].append([y,w])
        graphs[idx] = graph
    heap = []
    h.heappush(heap,[0,start,0])
    while heap:
        cur_w, cur_node, cur_state =  h.heappop(heap)
        if cur_node == end:
            return cur_w
        if d[cur_state][cur_node] != float('inf'):
            continue
        d[cur_state][cur_node] = cur_w
        for x,y in graphs[cur_state][cur_node]:
            if x in traps:
                next_state = cur_state ^ 1<<trap_dict[x]
            else:
                next_state = cur_state
            h.heappush(heap,[cur_w+y,x,next_state])

n=3
start=1
end=3
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]

n=4
start=1
end=4
roads = 	[[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]	
print(solution(n,start,end,roads,traps))