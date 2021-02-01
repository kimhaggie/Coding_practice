#1285
import sys
from collections import deque
import math
import copy

ans = float('inf')
N = int(sys.stdin.readline().rstrip('\n'))
m = []
for _ in range(N):
    m.append(list(sys.stdin.readline().rstrip('\n')))
for k in range(1<<N):#k는 뒤집을 행의 조합을 의미
    cur = 0
    for i in range(N):
        tmp = 0
        for j in range(N):
            if k&(1<<j)>0:
                if m[i][j]=='H':
                    tmp+=1
            else:
                if m[i][j]=='T':
                    tmp+=1
        cur += min(tmp,N-tmp)
    ans = min(ans,cur)
print(ans)