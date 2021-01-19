#13549
import sys
from collections import deque

N, K = map(int,sys.stdin.readline().rstrip('\n').split(' '))
visit = [float('inf') for _ in range(100001)]
target = []
cur = N
while True:
    if cur==0:
        target.append(0)
        visit[0] = 0
        break
    if cur<=100000:
        target.append(cur)
        visit[cur] = 0
        cur *= 2
    else:
        break
while True:
    new_target = []
    while len(target) != 0:
        cur = target.pop()
        time = visit[cur]
        if cur == K:
            print(time)
            sys.exit()
        #op1
        if 0<=cur-1<=100000 and time+1 < visit[cur-1]:
            new_target.append(cur-1)
            visit[cur-1] = time+1
            x = 2*(cur-1)
            while True:
                if 0<x<=100000 and time+1<visit[x]:
                    new_target.append(x)
                    visit[x] = time+1
                    x *= 2
                else:
                    break
        #op2
        if 0<=cur+1<=100000 and time+1 < visit[cur+1]:
            new_target.append(cur+1)
            visit[cur+1] = time+1
            x = 2*(cur+1)
            while True:
                if 0<x<=100000 and time+1<visit[x]:
                    new_target.append(x)
                    visit[x] = time+1
                    x *= 2
                else:
                    break
    target = new_target