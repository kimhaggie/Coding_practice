#1697
import sys
from collections import deque

N, K = map(int,sys.stdin.readline().rstrip('\n').split(' '))
visit = [False for _ in range(100001)]
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
                visit[val] = True
                next_position.append(val)
    position = next_position
    time += 1
print(ans)