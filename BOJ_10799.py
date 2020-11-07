#10799
import sys

line = sys.stdin.readline().rstrip('\n')
cur = -1
ans = 0
for idx,val in enumerate(line):
    if val == ')' and line[idx-1] == '(':
        cur -= 1
        continue
    if val == '(' and line[idx+1] == ')':
        cur += 1
        ans += cur
        continue
    if val == '(':
        cur += 1
        continue
    if val == ')':
        cur -= 1
        ans += 1
        continue
print(ans)