#10824
import sys
from collections import deque

num = sys.stdin.readline().rstrip('\n').split(' ')
print(int(num[0]+num[1])+int(num[2]+num[3]))