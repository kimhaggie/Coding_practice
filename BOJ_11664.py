#11664
import sys
from collections import deque
import math
import copy
import heapq

def func():
    a = [C[0]-A[0],C[1]-A[1],C[2]-A[2]]
    c = [B[0]-A[0],B[1]-A[1],B[2]-A[2]]
    ans = 0
    x = 0
    y = 0
    for i,j in zip(a,c):
        ans += i*j
        x += i*i
        y += j*j
    cos = ans/math.sqrt(x*y)
    return cos,math.sqrt(1-cos*cos)

x = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
A = []
B = []
C = []
for i in range(3):
    A.append(x[0+i])
    B.append(x[3+i])
    C.append(x[6+i])
a=0
b=0
c=0
for x,y,z in zip(A,B,C):
    a += (x-z)*(x-z)
    b += (y-z)*(y-z)
    c += (x-y)*(x-y)
a = math.sqrt(a)
b = math.sqrt(b)
c = math.sqrt(c)
cos,sin = func()
w = a*cos
h = a*sin
left = h
right = min(a,b)
mid = (left+right)/2
prev=mid
while True:
    x1,x2 = w-math.sqrt(mid*mid-h*h), w+math.sqrt(mid*mid-h*h)
    if 0<=x1<=c and 0<=x2<=c:
        right=mid
        mid = (left+right)/2
    elif (x1<0 or x1>c) and (x2<0 or x2>c):
        left = mid
        mid = (left+right)/2
    if abs(prev-mid)<0.000001:
        print('%.10f'%mid)
        break
    prev = mid