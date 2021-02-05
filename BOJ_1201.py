#1201
import sys
from collections import deque
import math
import copy
import heapq

N, M, K = map(int,sys.stdin.readline().rstrip('\n').split(' '))
if N<M+K-1 or N>M*K:
    print(-1)
    sys.exit()
total = list(range(1,N+1))
if M==1:
    print(' '.join(map(str,list(reversed(range(1,N+1))))))
    sys.exit()
ans = []
ans.append(list(reversed(total[:K])))
#N-K
batch = [(N-K)//(M-1) for _ in range(M-1)]
for idx in range((N-K)%(M-1)):
    batch[idx]+=1
start = K
for x in batch:
    ans.append(list(reversed(total[start:start+x])))
    start+=x
A=[]
for x in ans:
    A.extend(x)
print(' '.join(map(str,A)))