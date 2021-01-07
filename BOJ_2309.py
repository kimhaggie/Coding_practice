#2309
import sys
import math
from itertools import permutations as P

a = []
for _ in range(9):
    a.append(int(sys.stdin.readline().rstrip('\n')))
total = list(P(range(9),7))
for c in total:
    tmp = []
    for i in c:
        tmp.append(a[i])
    if sum(tmp)==100:
        print('\n'.join(map(str,sorted(tmp))))
        break
