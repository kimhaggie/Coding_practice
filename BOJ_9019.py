#9019
import sys
from collections import deque
import math

def D(n):
    return (2*n)%10000

def S(n):
    if n==0:
        return 9999
    else:
        return n-1

def L(n):
    s = '0'*(4-len(str(n)))+str(n)
    s = s[1:]+s[:1]
    # while len(s)!=4:
    #     s+='0'
    return int(s)

def R(n):
    s = '0'*(4-len(str(n))) + str(n)
    s = s[-1:]+s[:-1]
    return int(s)

def BFS(start, goal, visit):
    target = [[start,[]]]
    step = 0
    visit[start] = True
    while target:
        new_target = []
        flag = False
        while target:
            cur,command = target.pop()
            next_pos = D(cur)
            if not visit[next_pos]:
                if next_pos == goal:
                    print(*command,sep='',end='')
                    print('D')
                    flag = True
                    break
                visit[next_pos] = True
                new_target.append([next_pos,command+['D']])
            next_pos = S(cur)
            if not visit[next_pos]:
                if next_pos == goal:
                    print(*command,sep='',end='')
                    print('S')
                    flag = True
                    break
                visit[next_pos] = True
                new_target.append([next_pos,command+['S']])
            next_pos = L(cur)
            if not visit[next_pos]:
                if next_pos == goal:
                    print(*command,sep='',end='')
                    print('L')
                    flag = True
                    break
                visit[next_pos] = True
                new_target.append([next_pos,command+['L']])
            next_pos = R(cur)
            if not visit[next_pos]:
                if next_pos == goal:
                    print(*command,sep='',end='')
                    print('R')
                    flag = True
                    break
                visit[next_pos] = True
                new_target.append([next_pos,command+['R']])
        target = new_target
        step += 1
        if flag:
            break

# print(L(123))
T = int(sys.stdin.readline().rstrip('\n'))
for _ in range(T):
    start, goal = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    visit = [False for _ in range(10000)]
    BFS(start, goal, visit)