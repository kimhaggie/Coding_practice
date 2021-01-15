#13023
import sys

def DFS(d,visit,connection,cur):
    if d == 4:
        return True
    friend = connection[cur]
    for idx,val in enumerate(friend):
        if visit[val]:
            continue
        visit[val] = True
        result = DFS(d+1,visit,connection,val)
        visit[val] = False
        if result:
            return True
    return False

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
connection = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    connection[a].append(b)
    connection[b].append(a)
visit = [False for _ in range(N)]
poss = 0
for i in range(N):
    if poss == 1:
        break
    visit[i]=True
    poss = int(DFS(0,visit,connection,i))
    visit[i]=False
print(poss)