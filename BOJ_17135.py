import sys
import copy

def distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

N, M, D = map(int,sys.stdin.readline().rstrip('\n').split())
m = []
enemy = []
for i in range(N):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split()))
    for j in range(M):
        if x[j]==1:
            enemy.append([i,j])
    m.append(x)
enemy = sorted(enemy, key = lambda x: x[1])

def play(A):
    cur = copy.deepcopy(enemy)
    archer = [[N] for _ in range(3)]
    for idx,val in enumerate(A):
        archer[idx].append(val)
    ans = 0
    while True:
        target = []
        for idx, val in enumerate(cur):
            if val[0]==N:
                target.append(idx)
        target = sorted(target, reverse=True)
        for x in target:
            cur.pop(x)
        if len(cur)==0:
            return ans
        dis = [[float('inf'),-1] for _ in range(3)]
        for num, x in enumerate(cur):
            for idx in range(3):
                tmp = distance(archer[idx], x)
                if tmp>D:
                    continue
                if tmp < dis[idx][0]:
                    dis[idx][0] = tmp
                    dis[idx][1] = num
        target = set()
        for idx in range(3):
            if dis[idx][1]!=-1:
                target.add(dis[idx][1])
        ans+=len(target)
        for x in sorted(list(target),reverse=True):
            cur.pop(x)
        for idx in range(len(cur)):
            cur[idx][0] = cur[idx][0]+1

Ans = -float('inf')

def DFS(path):
    global Ans
    if len(path)==3:
        x = play(path)
        if Ans<x:
            Ans = x
    else:
        if len(path)==0:
            for i in range(M):
                path.append(i)
                DFS(path)
                path.pop()
        else:
            prev = path[-1]
            for i in range(prev+1, M):
                path.append(i)
                DFS(path)
                path.pop()

DFS([])
print(Ans)