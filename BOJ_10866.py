#10866
import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque([])

for i in range(n):
    command = sys.stdin.readline().split(' ')
    if len(command) == 1:
        command = command[0].rstrip('\n')
        if command == 'empty':
            if len(deq) == 0:
                print(1)
            else:
                print(0)
        if command == 'size':
            print(len(deq))
        if command == 'pop_front':
            if len(deq) == 0:
                print(-1)
            else:
                print(deq.popleft())
        if command == 'pop_back':
            if len(deq) == 0:
                print(-1)
            else:
                print(deq.pop())
        if command == 'back':
            if len(deq) != 0:
                print(deq[-1])
            else:
                print(-1)
        if command == 'front':
            if len(deq) != 0:
                print(deq[0])
            else:
                print(-1)
    else:
        push_n = int(command[-1])
        if command[0] == 'push_front':
            deq.appendleft(push_n)
        if command[0] == 'push_back':
            deq.append(push_n)