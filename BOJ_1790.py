#1790
import sys
from collections import deque
import math
import copy
import heapq

N, k = map(int,sys.stdin.readline().rstrip('\n').split(' '))
l = 0
x = 9
step = 1
while N-x>=0:
    l += step*x
    N -= x
    step += 1
    x *= 10
l += step*N
if k > l:
    print(-1)
    sys.exit()   
if k<=9:
    print(k)
elif k<=9+180:
    x = math.ceil((k - 9)/2) + 9
    x = str(x)[(k-9-1)%2]
    print(x)
elif k<=9+180+2700:
    x = math.ceil((k - 9 - 180)/3) + 9 + 90
    x = str(x)[(k-9-180-1)%3]
    print(x)
elif k<=9+180+2700+36000:
    x = math.ceil((k - 9 - 180 - 2700)/4) + 9 + 90 + 900
    x = str(x)[(k-9-180-2700-1)%4]
    print(x)
elif k<=9+180+2700+36000+450000:
    x = math.ceil((k - 9 - 180 - 2700 - 36000)/5) + 9 + 90 + 900 + 9000
    x = str(x)[(k-9-180-2700-36000-1)%5]
    print(x)
elif k<=9+180+2700+36000+450000+5400000:
    x = math.ceil((k - 9 - 180 - 2700 - 36000 - 450000)/6) + 9 + 90 + 900 + 9000 + 90000
    x = str(x)[(k-9-180-2700-36000-450000-1)%6]
    print(x)
elif k<=9+180+2700+36000+450000+5400000+63000000:
    x = math.ceil((k - 9 - 180 - 2700 - 36000 - 450000 - 5400000)/7) + 9 + 90 + 900 + 9000 + 90000 + 900000
    x = str(x)[(k-9-180-2700-36000-450000-5400000-1)%7]
    print(x)
elif k<=9+180+2700+36000+450000+5400000+63000000+720000000:
    x = math.ceil((k - 9 - 180 - 2700 - 36000 - 450000 - 5400000 - 63000000)/8) + 9 + 90 + 900 + 9000 + 90000 + 900000 + 9000000
    x = str(x)[(k-9-180-2700-36000-450000-5400000-63000000-1)%8]
    print(x)
else:
    if k == 9+180+2700+36000+450000+5400000+63000000+720000000+1:
        print(1)
    else:
        print(0)