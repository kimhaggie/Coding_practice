#2138
import sys
from collections import deque
import math
import copy

def change(i):
    if 0<=i-1:
        if A[i-1]==0:
            A[i-1]=1
        else:
            A[i-1]=0
    if A[i]==0:
        A[i]=1
    else:
        A[i]=0
    if i+1<len(A):
        if A[i+1]==0:
            A[i+1]=1
        else:
            A[i+1]=0

def count(i):
    ans = 0
    if i-1>=0 and A[i-1]!=B[i-1]:
        ans+=1
    if A[i]!=B[i]:
        ans+=1
    if i+1<len(A) and A[i+1]!=B[i+1]:
        ans+=1
    return ans

N = int(sys.stdin.readline().rstrip('\n'))
A = sys.stdin.readline().rstrip('\n')
B = sys.stdin.readline().rstrip('\n')
tmp = []
for val in A:
    tmp.append(int(val))
A = tmp
tmp = []
for val in B:
    tmp.append(int(val))
B = tmp
C = A.copy()
ans_A = 0
for idx in range(1,len(A)):
    if A[idx-1]!=B[idx-1]:
        change(idx)
        ans_A+=1
flag_A=False
if A==B:
    flag_A=True
ans_C = 1
A = C
change(0)
for idx in range(1,len(A)):
    if A[idx-1]!=B[idx-1]:
        change(idx)
        ans_C+=1
flag_C=False
if A==B:
    flag_C=True
if flag_A and flag_C:
    print(min(ans_A,ans_C))
elif flag_A:
    print(ans_A)
elif flag_C:
    print(ans_C)
else:
    print(-1)