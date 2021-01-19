#13913
import sys
from collections import deque

N, K = map(int,sys.stdin.readline().rstrip('\n').split(' '))
visit = [False for _ in range(100001)]
parent = [-1 for _ in range(100001)]
visit[N] = True
find = False
position = [N]
time = 0
while not find:
    next_position = []
    while len(position)!=0:
        cur = position.pop()
        if cur == K:
            ans = time
            find = True
            break
        next_pos = [cur-1,cur+1,cur*2]
        for val in next_pos:
            if 0<=val<=100000 and (not visit[val]):
                parent[val] = cur
                visit[val] = True
                next_position.append(val)
    position = next_position
    time += 1
print(ans)
ans=[K]
cur = K
while True:
    next_idx = parent[cur]
    if next_idx==-1:
        break
    else:
        ans.append(next_idx)
        cur = next_idx
print(' '.join(map(str,reversed(ans))))