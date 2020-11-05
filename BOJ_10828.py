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
        if command == 'pop':
            if len(deq) == 0:
                print(-1)
            else:
                print(deq.pop())
        if command == 'top':
            if len(deq) != 0:
                print(deq[-1])
            else:
                print(-1)
    else:
        push_n = int(command[-1])
        deq.append(push_n)