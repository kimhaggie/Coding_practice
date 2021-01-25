#13460
import sys
from collections import deque
import math

dy=[-1,1,0,0]
dx=[0,0,1,-1]

def BFS(red,blue,m):
    step = 1
    target = [[red,blue]]
    while target:
        new_target=[]
        while target:
            if step>10:
                print(-1)
                sys.exit()
            cur = target.pop()
            tmp_red = cur[0]
            tmp_blue = cur[1]
            for idx in range(4):
                cur_red = tmp_red.copy()
                cur_blue = tmp_blue.copy()
                hole = 0
                while True:
                    next_red = [cur_red[0]+dy[idx],cur_red[1]+dx[idx]]
                    next_blue = [cur_blue[0]+dy[idx],cur_blue[1]+dx[idx]]
                    R = True
                    B = True
                    if m[next_red[0]][next_red[1]] == '#':
                        R = False
                        next_red = cur_red
                    elif m[next_red[0]][next_red[1]] == 'O':
                        while True:
                            if m[next_blue[0]][next_blue[1]] == '#':
                                print(step)
                                sys.exit()
                                hole = 1
                            elif m[next_blue[0]][next_blue[1]] == 'O':
                                hole = 2
                                break
                            else:
                                next_blue = [next_blue[0]+dy[idx],next_blue[1]+dx[idx]]
                    if hole > 0:
                        break
                    if m[next_blue[0]][next_blue[1]] == '#':
                        B = False
                        next_blue = cur_blue
                    elif m[next_blue[0]][next_blue[1]] == 'O':
                        hole=2
                        break
                    if not R and not B:#두 구슬 다 안 움직임
                        break
                    if next_blue == next_red:
                        if R:#빨강만 움직임
                            next_red=cur_red
                        if B:
                            next_blue=cur_blue
                        break
                    cur_red = next_red
                    cur_blue = next_blue
                if hole==0:
                    if not [next_red,next_blue] in new_target:
                        new_target.append([next_red,next_blue])
        target = new_target
        step += 1

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
for i in range(N):
    x=list(sys.stdin.readline().rstrip('\n'))
    m.append(x)
    for j, val in enumerate(x):
        if val == 'B':
            m[i][j] = '.'
            blue = [i,j]
        if val == 'R':
            m[i][j] = '.'
            red = [i,j]
BFS(red,blue,m)