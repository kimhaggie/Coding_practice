#1517
import sys
from collections import deque
import math
import copy
import heapq

def divide(A):
    l = len(A)
    if l==1:
        return A
    else:
        mid = l//2
        x = divide(A[:mid])
        y = divide(A[mid:])
        a = 0
        b = 0
        z = []
        while a<len(x) and b<len(y):
            if x[a]>y[b]:
                z.append(y[b])
                b+=1
                ans[0]+=len(x)-a
            else:
                z.append(x[a])
                a+=1
        while a<len(x):
            z.append(x[a])
            a+=1
        while b<len(y):
            z.append(y[b])
            b+=1
        return z

N = int(sys.stdin.readline().rstrip('\n'))
A = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
ans = [0]
divide(A)
print(*ans)