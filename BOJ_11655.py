#11655
import sys
from collections import deque

sen = sys.stdin.readline().rstrip('\n')
ans = ''
for i in sen:
    if 65<=ord(i)<65+26:
        ans += chr((ord(i)-65+13)%26+65)
    elif 97<=ord(i)<97+26:
        ans += chr((ord(i)-97+13)%26+97)
    else:
        ans += i
print(ans)