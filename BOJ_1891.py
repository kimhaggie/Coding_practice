#1891
import sys
from collections import deque
import math
import copy
import heapq

def find_loc(pos):
    d = pow(2,len(pos))
    cur = pos[0]
    if d == 2:
        if cur=='1':
            return [1,1]
        elif cur=='2':
            return [-1,1]
        elif cur=='3':
            return [-1,-1]
        else:
            return [1,-1]
    else:
        if cur=='1':
            x = [d//2,d//2]
            y = find_loc(pos[1:])
            return [x[0]+y[0],x[1]+y[1]]
        elif cur=='2':
            x = [-d//2,d//2]
            y = find_loc(pos[1:])
            return [x[0]+y[0],x[1]+y[1]]
        elif cur=='3':
            x = [-d//2,-d//2]
            y = find_loc(pos[1:])
            return [x[0]+y[0],x[1]+y[1]]
        else:
            x = [d//2,-d//2]
            y = find_loc(pos[1:])
            return [x[0]+y[0],x[1]+y[1]]

def locate(pos,d):
    x=pos[0]
    y=pos[1]
    if d==1:
        if x>0 and y>0:
            print(1)
        elif x<0 and y>0:
            print(2)
        elif x<0 and y<0:
            print(3)
        else:
            print(4)
    else:
        if x>0 and y>0:
            print(1,end='')
            locate([x-pow(2,d-1),y-pow(2,d-1)],d-1)
        elif x<0 and y>0:
            print(2,end='')
            locate([x+pow(2,d-1),y-pow(2,d-1)],d-1)
        elif x<0 and y<0:
            print(3,end='')
            locate([x+pow(2,d-1),y+pow(2,d-1)],d-1)
        else:
            print(4,end='')
            locate([x-pow(2,d-1),y+pow(2,d-1)],d-1)

d, start = map(int,sys.stdin.readline().rstrip('\n').split(' '))
x, y = map(int,sys.stdin.readline().rstrip('\n').split(' '))
pos = find_loc(str(start))
pos = [pos[0]+x*2,pos[1]+y*2]
if -(pow(2,d)-1)<=pos[0]<=(pow(2,d)-1) and -(pow(2,d)-1)<=pos[1]<=(pow(2,d)-1):
    locate(pos,d)
else:
    print(-1)