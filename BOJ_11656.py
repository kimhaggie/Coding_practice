#11656
import sys
from collections import deque

word = sys.stdin.readline().rstrip('\n')
ans = []
for i in range(len(word)):
    x = word[i:]
    ans.append(x)
print('\n'.join(sorted(ans)))