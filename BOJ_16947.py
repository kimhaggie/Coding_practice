#16947
import sys
from collections import deque

sys.setrecursionlimit(10000)

def find_circle(m,start,cur,visit,depth):
    if start==cur and depth>=2:
        visit[cur] = True
        return visit
    for idx in m[cur]:
        if not visit[idx]:
            if depth<2 and idx==start:
                continue
            visit[idx] = True
            result = find_circle(m,start,idx,visit,depth+1)
            if result != 0:
                return visit 
            visit[idx] = False
    return 0

def distance(m,circle,cur,visit):
    if cur in circle:
        return 0
    ans = []
    for idx in m[cur]:
        if not visit[idx]:
            visit[idx] = True
            x = distance(m,circle,idx,visit)
        else:
            continue
        if x==-1:
            ans.append(-1)
        else:
            ans.append(x+1)
    if len(ans)==0:
        return -1
    return max(ans)


N = int(sys.stdin.readline().rstrip('\n'))
m = [[] for _ in range(N)]
for _ in range(N):
    a, b = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    a-=1
    b-=1
    m[a].append(b)
    m[b].append(a)
for idx in range(N):
    visit = [False for _ in range(N)]
    sub_ans = find_circle(m,idx,idx,visit,0)
    if sub_ans != 0:
        break
circle = []
for idx,val in enumerate(sub_ans):
    if val:
        circle.append(idx)
ans = []
for idx in range(N):
    if idx in circle:
        ans.append(0)
    else:
        visit = [False for _ in range(N)]
        visit[idx]=True
        ans.append(distance(m,circle,idx,visit))
print(' '.join(map(str,ans)))