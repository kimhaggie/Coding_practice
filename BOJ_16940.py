#16940
import sys
from collections import deque

def BFS(m,N):
    visit = [False for _ in range(N)]
    result = []
    deq = deque()
    deq.append([0,-1])
    visit[0] = True
    while len(deq)!=0:
        cur,depth = deq.popleft()
        tmp = []
        for idx in m[cur]:
            if not visit[idx]:
                deq.append([idx,depth+1])
                visit[idx] = True
                tmp.append(idx)
        result.append([cur,depth+1,tmp])
    return sorted(result)

N = int(sys.stdin.readline().rstrip('\n'))
m = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    a -= 1
    b -= 1
    m[a].append(b)
    m[b].append(a)
submit = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
for idx in range(N):
    submit[idx] -= 1
if submit[0]!=0:
    print(0)
else:
    ans = BFS(m,N)
    max_depth = 0
    for idx in range(N):
        if max_depth < ans[idx][1]:
            max_depth = ans[idx][1]
    depth_start = [0 for _ in range(max_depth+2)]
    for idx in range(N):
        depth_start[ans[idx][1]+1] += 1
    for idx in range(1,max_depth+2):
        depth_start[idx]+=depth_start[idx-1]
    cpy = deque(submit.copy())
    flag=True
    while len(cpy)!=0 and flag:
        cur = cpy.popleft()
        cur_info = ans[cur]
        start = depth_start[cur_info[1] + 1]
        w = len(cur_info[2])
        for x in submit[start:start+w]:
            if x not in cur_info[2]:
                flag=False
        depth_start[cur_info[1] + 1] += w
    if flag:
        print(1)
    else:
        print(0)