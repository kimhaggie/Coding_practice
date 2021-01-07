#1476
import sys
import math

E,S,M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
val = 1
while(True):
    e=val%15
    s=val%28
    m=val%19
    if e==0: e=15
    if s==0: s=28
    if m==0: m=19
    if (e==E and s==S and m==M):
        break
    else:
        val+=1
print(val)