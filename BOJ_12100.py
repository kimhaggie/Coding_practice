#12100
import sys
from collections import deque
import math

def up(m, N):
    new_m = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):#각 행 마다 체크
        cur = []
        for i in range(N):
            if m[i][j]!=0:
                cur.append(m[i][j])
        t = 1
        while True:
            if t>=len(cur):
                break
            if cur[t-1] == cur[t]:#합침
                cur[t-1] *= 2
                del cur[t]
                t += 1
                continue
            else: 
                t += 1
                continue
        while len(cur) != N:
            cur.append(0)
        for i in range(N):
            new_m[i][j] = cur[i]
    return new_m

def down(m, N):
    new_m = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        cur = []
        for i in range(N):
            if m[N-i-1][j]!=0:
                cur.append(m[N-i-1][j])
        t=1
        while True:
            if t>=len(cur):
                break
            if cur[t-1] == cur[t]:
                cur[t-1] *= 2
                del cur[t]
                t += 1
                continue
            else:
                t+=1
                continue
        while len(cur) != N:
            cur.append(0)
        for i in range(N):
            new_m[N-i-1][j] = cur[i]
    return new_m

def left(m, N):
    new_m = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        cur = []
        for j in range(N):
            if m[i][j]!=0:
                cur.append(m[i][j])
        t=1
        while True:
            if t>=len(cur):
                break
            if cur[t-1] == cur[t]:
                cur[t-1] *= 2
                del cur[t]
                t += 1
                continue
            else:
                t+=1
                continue
        while len(cur) != N:
            cur.append(0)
        for j in range(N):
            new_m[i][j] = cur[j]
    return new_m

def right(m, N):
    new_m = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        cur = []
        for j in range(N):
            if m[i][N-j-1]!=0:
                cur.append(m[i][N-j-1])
        t=1
        while True:
            if t>=len(cur):
                break
            if cur[t-1] == cur[t]:
                cur[t-1] *= 2
                del cur[t]
                t += 1
                continue
            else:
                t+=1
                continue
        while len(cur) != N:
            cur.append(0)
        for j in range(N):
            new_m[i][N-j-1] = cur[j]
    return new_m

def cal(m, N):
    MAX = []
    for i in m:
        MAX.append(max(i))
    return max(MAX)

def BFS(m, N):
    step = 0
    target = [m]
    while target:
        if step == 5:
            MAX = 0
            for val in target:
                MAX = max(MAX, cal(val, N))
            print(MAX)
            sys.exit()
        new_target = []
        while target:
            cur_m = target.pop()
            new_target.append(up(cur_m, N))
            new_target.append(down(cur_m, N))
            new_target.append(left(cur_m, N))
            new_target.append(right(cur_m, N))
            pass
        target = new_target
        step += 1
    pass

N = int(sys.stdin.readline().rstrip('\n'))
m = []
for _ in range(N):
    m.append(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
BFS(m, N)