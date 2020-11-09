#1158
import sys
from collections import deque

n,k = map(int,sys.stdin.readline().rstrip('\n').split(' '))
deq = deque(range(1,n+1))
cur = 1
answer='<'
while len(deq)!=0:
    x = deq.popleft()
    if cur % k == 0:
        answer += (str(x)+', ')
    else:
        deq.append(x)
    cur = (cur+1) % k
answer = answer[:-2]+'>'
print(answer)