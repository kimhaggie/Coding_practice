#1874
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip('\n'))
deq = deque([1])
cur = 2
command = deque(['+'])
poss = True
for _ in range(n):
    target = int(sys.stdin.readline().rstrip('\n'))
    if not poss:
        continue
    if len(deq) == 0:
        deq.append(cur)
        cur += 1
        command.append('+')
    while (deq[-1] != target):
        if cur > n:
            poss = False
            break
        deq.append(cur)
        cur += 1
        command.append('+')
    deq.pop()
    command.append('-')
if poss:
    for i in command:
        print(i)
else:
    print('NO')