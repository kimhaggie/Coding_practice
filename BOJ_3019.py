#3019
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations

C, P = map(int,sys.stdin.readline().rstrip('\n').split())
m = list(map(int,sys.stdin.readline().rstrip('\n').split()))
if P==1:
    ans = C
    for i in range(C-3):
        if m[i]==m[i+1]==m[i+2]==m[i+3]:
            ans+=1
elif P==2:
    ans = 0
    for i in range(C-1):
        if m[i]==m[i+1]:
            ans+=1
elif P==3:
    ans = 0
    for i in range(C-2):
        if m[i] == m[i+1] == m[i+2]-1:
            ans+=1
    for i in range(C-1):
        if m[i]-1==m[i+1]:
            ans+=1
elif P==4:
    ans = 0
    for i in range(C-2):
        if m[i]-1 == m[i+1] == m[i+2]:
            ans+=1
    for i in range(C-1):
        if m[i]==m[i+1]-1:
            ans+=1
elif P==5:
    ans = 0
    for i in range(C-2):
        if m[i]==m[i+1]==m[i+2] or m[i]-1==m[i+1]==m[i+2]-1:
            ans+=1
    for i in range(C-1):
        if m[i]==m[i+1]-1 or m[i]-1==m[i+1]:
            ans+=1
elif P==6:
    ans = 0
    for i in range(C-2):
        if m[i]==m[i+1]==m[i+2] or m[i]==m[i+1]-1==m[i+2]-1:
            ans+=1
    for i in range(C-1):
        if m[i]-2==m[i+1] or m[i]==m[i+1]:
            ans+=1
else:
    ans = 0
    for i in range(C-2):
        if m[i]==m[i+1]==m[i+2] or m[i]-1==m[i+1]-1==m[i+2]:
            ans+=1
    for i in range(C-1):
        if m[i]==m[i+1]-2 or m[i]==m[i+1]:
            ans+=1
print(ans)
