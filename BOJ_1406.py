#1406
import sys
from collections import deque

sentence = list(sys.stdin.readline().rstrip('\n'))
left = deque(sentence)
right = deque([])
n = int(sys.stdin.readline().rstrip('\n'))
for _ in range(n):
    command = sys.stdin.readline().rstrip('\n').split(' ')
    if len(command) == 1:
        if command[0] == 'L':
            if len(left) != 0:
                x = left.pop()
                right.appendleft(x)
        if command[0] == 'D':
            if len(right) != 0:
                x = right.popleft()
                left.append(x)
        if command[0] == 'B':
            if len(left) != 0:
                left.pop()
    else:
        x = command[1]
        left.append(x)
final = ''
while(len(left)!=0):
    final += left.popleft()
while(len(right)!=0):
    final += right.popleft()
print(final)
