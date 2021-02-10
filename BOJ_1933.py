#1933
import sys
from collections import deque
import math
import copy
import heapq

def merge(x,y):
    i=0
    j=0
    z=[]
    while i<len(x) and j<len(y):
        cur_x = x[i]
        cur_y = y[j]
        #포함될때
        if cur_x[0]>=cur_y[0] and cur_x[1]<=cur_y[1] and cur_x[2]<=cur_y[2]:
            i+=1
            continue
        if cur_y[0]>=cur_x[0] and cur_y[1]<=cur_x[1] and cur_y[2]<=cur_x[2]:
            j+=1
            continue
        #포함 되는데 삐죽 튀어나온 경우
        if cur_x[0]<=cur_y[0] and cur_y[1]>=cur_x[1] and cur_x[2]>=cur_y[2]:
            if cur_x[0]!=cur_y[0]:
                z.append([cur_x[0],cur_x[1],cur_y[0]])
            z.append([cur_y[0],cur_y[1],cur_y[2]])
            x[i][0]=cur_y[2]
            if x[i][0]==x[i][2]:
                i+=1
            j+=1
            continue
        if cur_y[0]<=cur_x[0] and cur_x[1]>=cur_y[1] and cur_y[2]>=cur_x[2]:
            if cur_y[0]!=cur_x[0]:
                z.append([cur_y[0],cur_y[1],cur_x[0]])
            z.append([cur_x[0],cur_x[1],cur_x[2]])
            y[j][0]=cur_x[2]
            if y[j][0]==y[j][2]:
                j+=1
            i+=1
            continue
        #x가 왼쪽
        #겹칠때
        if cur_x[2]>cur_y[0] and cur_x[0]<cur_y[0]:
            if cur_x[1]>=cur_y[1]:
                z.append([cur_x[0],cur_x[1],cur_x[2]])
                i+=1
                y[j][0]=cur_x[2]
            else:
                z.append([cur_x[0],cur_x[1],cur_y[0]])
                i+=1
            continue
        #분리
        if cur_x[2]<=cur_y[0] and cur_x[0]<cur_y[0]:
            z.append(cur_x)
            i+=1
            continue
        #y가 왼쪽
        #겹칠 때
        if cur_y[2]>cur_x[0] and cur_y[0]<cur_x[0]:
            if cur_y[1]>=cur_x[1]:
                z.append([cur_y[0],cur_y[1],cur_y[2]])
                j+=1
                x[i][0]=cur_y[2]
            else:
                z.append([cur_y[0],cur_y[1],cur_x[0]])
                j+=1
            continue
        #분리
        if cur_y[2]<=cur_x[0] and cur_y[0]<cur_x[0]:
            z.append(cur_y)
            j+=1
            continue
    while i<len(x):
        z.append(x[i])
        i+=1
    while j<len(y):
        z.append(y[j])
        j+=1
    return z

def divide(left,right):
    if left == right:
        return B[left:right+1]
    else:
        mid = (left+right)//2
        x = divide(left,mid)
        y = divide(mid+1,right)
        return merge(x,y)

N = int(sys.stdin.readline().rstrip('\n'))
B = []
for _ in range(N):
    B.append(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
result = divide(0,N-1)
result = result[::-1]
prev=None
while result:
    cur = result.pop()
    if prev==None:
        print(cur[0],cur[1], end=' ')
        prev=cur
    else:
        if cur[0]==prev[2]:
            if cur[1]==prev[1]:
                prev=cur
                continue
            print(cur[0],cur[1],end=' ')
            prev=cur
        else:
            print(prev[2],0,end=' ')
            print(cur[0],cur[1],end=' ')
            prev=cur
print(cur[2],0)