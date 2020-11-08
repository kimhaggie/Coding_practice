#1158
import sys
from collections import deque

n,k = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
deq = deque(list(range(1,n+1)))
cur = 1
ans = deque([])
while len(deq)!=0:
    x = deq.popleft()
    if cur % k == 0:
        ans.append(x)
    else:
        deq.append(x)
    cur = (cur+1) % k
print('<',end='')
for idx,val in enumerate(ans):
    if idx != len(ans)-1:
        print(val,end=', ')
    else:
        print(val,end='>')