#1541
import sys
from collections import deque
import math
import copy
import heapq

line = list(sys.stdin.readline().rstrip('\n'))
var = []
op = []
cur = ''
for x in line:
    if x=='+' or x=='-':
        var.append(int(cur))
        op.append(x)
        cur=''
    else:
        cur+=x
var.append(int(cur))
ans = var[0]
idx = 0
while idx<len(op):
    cur = op[idx]
    if cur == '+':
        ans += var[idx+1]
        idx+=1
    elif cur == '-':
        if idx==len(op)-1:
            ans -= var[idx+1]
            idx+=1
            continue
        tmp = var[idx+1]
        idx += 1
        while idx<len(op):
            cur = op[idx]
            if cur=='-':
                break
            elif cur=='+':
                tmp+=var[idx+1]
                idx+=1
        ans-=tmp
print(ans)
