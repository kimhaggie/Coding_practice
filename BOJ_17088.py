#17088
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations

def check(x):
    ans = 0
    flag = True
    prev = x[0]
    for idx in range(1,len(x)):
        if x[idx] == prev:
            prev = x[idx]
        elif x[idx] == prev-1:
            ans += 1
            x[idx] += 1
            if idx+1<len(x):
                x[idx+1] -= 1
            prev = x[idx]
        elif x[idx] == prev+1:
            ans += 1
            x[idx] -= 1
            if idx+1<len(x):
                x[idx+1] += 1
            prev = x[idx]
        else:
            flag = False
            break
    return [flag, ans]

N = int(sys.stdin.readline().rstrip('\n'))
B = list(map(int,sys.stdin.readline().rstrip('\n').split()))
if N<=2:
    print(0)
    sys.exit()
a = []
for i in range(len(B)-1):
    a.append(B[i+1]-B[i])
result = []
# + +
x = a.copy()
x[1]-=1
tmp = check(x)
result.append(2+tmp[1] if tmp[0] else N)
# + 0
x = a.copy()
x[0] -= 1
tmp = check(x)
result.append(1+tmp[1] if tmp[0] else N)
# + -
x = a.copy()
x[0] -= 2
x[1] += 1
tmp = check(x)
result.append(2+tmp[1] if tmp[0] else N)
# 0 +
x = a.copy()
x[0] += 1
x[1] -= 1
tmp = check(x)
result.append(1+tmp[1] if tmp[0] else N)
# 0 0
x = a.copy()
tmp = check(x)
result.append(tmp[1] if tmp[0] else N)
# 0 -
x = a.copy()
x[0] -= 1
x[1] += 1
tmp = check(x)
result.append(1+tmp[1] if tmp[0] else N)
# - + 
x = a.copy()
x[0] += 2
x[1] -= 1
tmp = check(x)
result.append(2+tmp[1] if tmp[0] else N)
# - 0
x = a.copy()
x[0] += 1
tmp = check(x)
result.append(1+tmp[1] if tmp[0] else N)
# - -
x = a.copy()
x[1] += 1
tmp = check(x)
result.append(2+tmp[1] if tmp[0] else N)
ans = min(result)
if ans==N:
    print(-1)
else:
    print(ans)