#10808
import sys
from collections import deque

word = list(sys.stdin.readline().rstrip('\n'))
ans = [0]*26
for i in word:
    ans[ord(i)-97] += 1
print(' '.join(list(map(str,ans))))