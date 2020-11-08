#10809
import sys
from collections import deque

word = list(sys.stdin.readline().rstrip('\n'))
ans = [-1]*26
for idx, val in enumerate(word):
    if ans[ord(val)-97] == -1:
        ans[ord(val)-97] = idx
print(' '.join(list(map(str,ans))))