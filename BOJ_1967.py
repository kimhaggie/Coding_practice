#1967
import sys
from collections import deque

def diameter(start,E,N):
    stack = [start]
    ans = 0
    dest = -1
    visit = [False for _ in range(N+1)]
    visit[start] = True
    distance = 0
    while stack:
        cur = stack[-1]
        n = 0
        for val in E[cur]:
            if not visit[val[0]]:
                n += 1
        if n == 0:#마지막 점
            if ans < distance:#업데이트
                ans = distance
                dest = cur
                stack.pop()
                x = 0
                for val in E[cur]:
                    if val[0] == stack[-1]:
                        x=val[1]
                        break
                distance -= x
            else:
                stack.pop()
                if len(stack)==0:
                    break
                x = 0
                for val in E[cur]:
                    if val[0] == stack[-1]:
                        x=val[1]
                        break
                distance -= x
        else:
            for val in E[cur]:
                if not visit[val[0]]:
                    visit[val[0]] = True
                    stack.append(val[0])
                    distance += val[1]
                    break
    return [ans,dest]

N = int(sys.stdin.readline().rstrip('\n'))
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    line = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    E[line[0]].append([line[1],line[2]])
    E[line[1]].append([line[0],line[2]])
_,x = diameter(1,E,N)
ans,_ = diameter(x,E,N)
print(ans)