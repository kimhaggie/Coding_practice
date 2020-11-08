#1918
import sys
from collections import deque

line = '(' + sys.stdin.readline().rstrip('\n') + ')'
stack = []
operation = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0, ')' : 0}
ans = ''
for val in line:
    if val == '(':
        stack.append(val)
        continue
    if val == ')':
        while stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
        continue
    if val in operation.keys():
        while stack and operation[stack[-1]] >= operation[val]:
            ans += stack.pop()
        stack.append(val)
    if val not in operation.keys():
        ans += val
print(ans)