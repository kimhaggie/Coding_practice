#16964
import sys
from collections import deque

def BFS(m,N):
    visit = [False for _ in range(N)]
    result = []
    deq = deque()
    deq.append([0,-1])
    while len(deq)!=0:
        cur,depth = deq.popleft()
        visit[cur]=True
        tmp = []
        parent = -1
        for idx in m[cur]:
            if not visit[idx]:
                deq.append([idx,depth+1])
                tmp.append(idx)
            if visit[idx]:
                parent = idx
        result.append([cur,depth+1,tmp,parent])
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
    children = []
    child_num = []
    parent = []
    for idx in range(N):
        children.append(ans[idx][2])
        child_num.append(len(ans[idx][2]))
        parent.append(ans[idx][3])
    deq = deque()
    flag = True
    for idx,val in enumerate(submit):
        if idx==0:
            deq.append(val)
            continue
        if not (val in children[deq[-1]]):
            flag=False
        else:
            if child_num[val]!=0:
                deq.append(val)
            else:
                child_num[parent[val]]-=1
                if child_num[parent[val]]==0:
                    while True:
                        cur = deq.pop()
                        if cur == -1:
                            break
                        child_num[parent[cur]] -= 1
                        if child_num[parent[cur]]==0:
                            continue
                        else:
                            break
    if flag:
        print(1)
    else:
        print(0)