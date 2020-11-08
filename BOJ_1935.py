#1935
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip('\n'))
operation = list(sys.stdin.readline().rstrip('\n'))
alphabet = [chr(i) for i in range(65,65+26)]
alphabet = dict.fromkeys(alphabet, 0)
for i in range(n):
    x = int(sys.stdin.readline().rstrip('\n'))
    alphabet[chr(i+65)] = x
stack = []
for val in operation:
    if val not in ['+','-','*','/']:
        stack.append(alphabet[val])
    else:
        y = stack.pop()
        x = stack.pop()
        if val == '+':
            stack.append(x+y)
        if val == '-':
            stack.append(x-y)
        if val == '*':
            stack.append(x*y)
        if val == '/':
            stack.append(x/y)
print(format(stack[0],'.2f'))