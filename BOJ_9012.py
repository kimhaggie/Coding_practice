#9012
import sys
from collections import deque

n = int(sys.stdin.readline())

for _ in range(n):
    deq = deque([])
    line = sys.stdin.readline().rstrip('\n')
    Y = True
    for val in line:
        if val == '(':
            deq.append(val)
        else:
            if len(deq) == 0:
                Y = False
                break
            else:
                deq.pop()
    if len(deq) != 0:
        Y = False
    if Y:
        print('YES')
    else:
        print('NO')

