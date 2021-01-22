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
        # print(cur,n)
        if n == 0:#마지막 점
            if ans < distance:#업데이트
                # print(stack,distance)
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
                    # print(val[0])
                    stack.append(val[0])
                    distance += val[1]
                    break
    return [ans,dest]

N = int(sys.stdin.readline().rstrip('\n'))
E = [[] for _ in range(N+1)]
for _ in range(N):
    line = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    start = line[0]
    for idx in range(int((len(line)-2)/2)):
        x = 2 * idx + 1
        E[start].append([line[x],line[x+1]])
# print('Edge:',E)
ans = []
already = []
_,x = diameter(1,E,N)
ans,_ = diameter(x,E,N)
print(ans)