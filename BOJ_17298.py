#17298
import sys
from collections import deque
n = int(sys.stdin.readline().rstrip('\n'))
elements = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
deq = deque([])
ans = ['-1'] * n

for idx, val in enumerate(elements):
    if len(deq) == 0:
        deq.append(idx)
    else:
        while (len(deq) != 0 and elements[deq[-1]] < val):
            x = deq.pop()
            ans[x] = str(val)
        deq.append(idx)
print(' '.join(ans))