#16928
import sys
from collections import deque
import math

dice = [1,2,3,4,5,6]

def BFS(start,ladder,snake,visit):
    step = 1
    target = [start]
    while target:
        new_target = []
        while target:
            cur = target.pop()
            if cur == 100:
                print(step-1)
                sys.exit()
            for x in dice:
                next_pos = cur + x
                for l in ladder:
                    if next_pos == l[0]:
                        next_pos = l[1]
                        break
                for s in snake:
                    if next_pos == s[0]:
                        next_pos = s[1]
                        break
                if next_pos > 100:
                    continue
                if not visit[next_pos]:
                    visit[next_pos] = True
                    new_target.append(next_pos)
        target = new_target
        step += 1

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
ladder = []
snake = []
for _ in range(N):
    x = sys.stdin.readline().rstrip('\n').split(' ')[:2]
    ladder.append(list(map(int,x)))
for _ in range(M):
    x = sys.stdin.readline().rstrip('\n').split(' ')[:2]
    snake.append(list(map(int,x)))
visit = [False for _ in range(101)]
visit[1] = True
BFS(1,ladder,snake,visit)