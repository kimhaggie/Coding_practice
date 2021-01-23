#14225
import sys
from collections import deque
import math

def cal(bit, S, full):
    ans = 0
    for idx in range(len(S)):
        if (1<<idx)&bit > 0:
            ans += S[idx]
    return ans

N = int(sys.stdin.readline().rstrip('\n'))
S = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
bit = (1<<N) 
start = 1
ans = set()
while start!=bit:
    ans.add(cal(start,S,bit))
    start+=1
ans = sorted(list(ans))
for idx,val in enumerate(ans):
    if idx+1!=val:
        print(idx+1)
        sys.exit()
print(len(ans)+1)