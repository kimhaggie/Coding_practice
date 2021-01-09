#6064
import sys
import math

def func(m,n,x,y):
    if m<n:#무조건 m이 큰 거
        m,n=n,m
        x,y=y,x
    for i in range(n):
        tmp = m*i+x
        if y==n:
            y=0
        if tmp%n == y:
            return tmp
    return -1

t = int(sys.stdin.readline().rstrip('\n'))
for _ in range(t):
    m,n,x,y = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    print(func(m,n,x,y))