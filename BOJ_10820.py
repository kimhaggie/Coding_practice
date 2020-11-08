#10820
import sys
from collections import deque

for line in sys.stdin:
    if line == '\n':
        break
    A = 0
    a = 0
    space = 0
    num = 0
    line = line.rstrip('\n')
    for val in line:
        if 97<=ord(val)<97+26:
            a += 1
        elif 65<=ord(val)<65+27:
            A += 1
        elif  val == ' ':
            space += 1
        else:
            num += 1
    print(a,A,num,space)