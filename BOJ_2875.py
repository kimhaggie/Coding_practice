#2875
import sys
from collections import deque
import math
import copy
import heapq

N, M, K = map(int,sys.stdin.readline().rstrip('\n').split(' '))
if M==0:
    print(0)
    sys.exit()
team = min(int(N/2),M)
N -= 2*team
M -= team
K -= (N+M)
if K > 0:
    x = math.ceil(K/3)
    print(team-x)
else:
    print(team)