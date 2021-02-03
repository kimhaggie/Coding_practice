#12904
import sys
from collections import deque
import math
import copy
import heapq

S = list(sys.stdin.readline().rstrip("\n"))
T = list(sys.stdin.readline().rstrip('\n'))
while len(S)!=len(T):
    if T[-1]=='A':
        T=T[:-1]
    else:
        T=T[:-1]
        T=T[::-1]
if S==T:
    print(1)
else:
    print(0)