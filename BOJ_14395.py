#14395
import sys
from collections import deque
import math
import copy

def BFS():
    if s==t:
        print(0)
        sys.exit()
    target = [[s,'']]
    visit=set()
    while target:
        new_target = []
        while target:
            cur = target.pop()# * + - /
            if cur[0]==t:
                print(cur[1])
                sys.exit()
            if cur[0]*cur[0]<=t and not cur[0]*cur[0] in visit:
                new_target.append([cur[0]*cur[0],cur[1]+'*'])
                visit.add(cur[0]*cur[0])
            if cur[0]+cur[0]<=t and not cur[0]+cur[0] in visit:
                new_target.append([cur[0]+cur[0],cur[1]+'+'])
                visit.add(cur[0]+cur[0])
            if not 0 in visit:
                new_target.append([0,cur[1]+'-'])
                visit.add(0)
            if not 1 in visit:
                new_target.append([1,cur[1]+'/'])
                visit.add(1)
        target = new_target[::-1]
    print(-1)

s, t = map(int,sys.stdin.readline().rstrip('\n').split(' '))
BFS()