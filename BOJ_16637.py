#16637
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations

N = int(sys.stdin.readline().rstrip('\n'))
A = sys.stdin.readline().rstrip('\n')
var = []
op = []
for val in A:
    if val == '+' or val == '-' or val == '*':
        op.append(val)
    else:
        var.append(val)
n = (N+1) // 2 + 1
ans = -float('inf')
for num in range(0,len(var)//2+1):
    All = list(combinations(range(len(var)),num))
    refine = []
    for case in All:
        prev = -2
        flag = True
        for idx in case:
            if idx-prev < 2 or idx == len(var)-1:
                flag = False
                break
            prev = idx
        if not flag:
            continue
        refine.append(case)
    for case in refine:
        left = case
        right = []
        for i in left:
            right.append(i+1)
        target = ''
        for i in range(len(var)-1):
            if i in left:
                target+='('
            target+=var[i]
            if i in right:
                target+=')'
            target+=op[i]
        target+=var[-1]
        if len(var)-1 in right:
            target+=')'
        idx = 0
        stack = []
        while idx<len(target):
            cur = target[idx]
            if idx>=len(target):
                break
            if cur == '(':
                a = ''
                b = ''
                i = idx+1
                while True:
                    if target[i] in ['+','-','*']:
                        break
                    else:
                        a+=target[i]
                    i+=1
                c = target[i]
                i+=1
                while True:
                    if i ==len(target):
                        break
                    if target[i] in ['+','-','*',')']:
                        break
                    else:
                        b+=target[i]
                    i+=1
                if c == '+':
                    stack.append(int(a)+int(b))
                if c == '-':
                    stack.append(int(a)-int(b))
                if c == '*':
                    stack.append(int(a)*int(b))
                idx+=(3+len(a)+len(b))
                if len(stack)==1:
                    continue
            elif cur in ['+','-','*']:
                stack.append(cur)
                idx+=1
                continue
            else:
                next_int = ''
                i = idx
                while True:
                    if i==len(target):
                        break
                    if target[i] in ['+','-','*']:
                        break
                    else:
                        next_int+=target[i]
                    i += 1
                stack.append(int(next_int))
                idx+=len(next_int)
                if len(stack)==1:
                    continue
            b = int(stack.pop())
            a = stack.pop()
            c = int(stack.pop())
            if a == '+':
                stack.append(b+c)
            if a == '-':
                stack.append(c-b)
            if a == '*':
                stack.append(b*c)
        ans = max(ans,stack[0])
print(ans)
