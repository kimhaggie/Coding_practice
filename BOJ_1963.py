#1963
import sys
from collections import deque
import math
import copy

def BFS():
    target = [start]
    step = 0
    while target:
        new_target = []
        while target:
            cur = target.pop()
            if cur == goal:
                return step
            for idx in range(4):
                for val in range(10):
                    tmp = list(cur)
                    tmp[idx] = str(val)
                    tmp = ''.join(tmp)
                    if not visit[int(tmp)]:
                        new_target.append(tmp)
                        visit[int(tmp)] = True
        target = new_target
        step+=1
    return 'Impossible'

prime = [True for _ in range(10000)]
prime[0]=False
prime[1]=False
for i in range(2,5000):
    if prime[i]:
        x = i + i
        while x<10000:
            prime[x] = False
            x += i
prime_num = []
for i in range(10000):
    if prime[i] and i>1000:
        prime_num.append(i)
T = int(sys.stdin.readline().rstrip('\n'))
for _ in range(T):
    visit = [True for _ in range(10000)]
    start, goal = sys.stdin.readline().rstrip('\n').split(' ')
    for x in prime_num:
        visit[x] = False
    visit[int(start)] = True
    for i in range(1000):
        visit[i]=True
    print(BFS())