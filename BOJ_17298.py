#17298
import sys
from collections import deque
n = int(sys.stdin.readline().rstrip('\n'))
elements = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
deq = deque([])
ans = [-1 for _ in range(n)]

for idx, val in enumerate(elements):
    if len(deq) == 0:
        deq.append(idx)
    else:
        while (len(deq) != 0 and elements[deq[-1]] < val):
            x = deq.pop()
            ans[x] = val
        deq.append(idx)
answer = ''
for idx, val in enumerate(ans):
    if idx == len(ans)-1:
        answer += str(val)
    else:
        answer += (str(val)+' ')
print(answer)