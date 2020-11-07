#9093
import sys

n = int(sys.stdin.readline().rstrip('\n'))
for _ in range(n):
    line = sys.stdin.readline().rstrip('\n').split(' ')
    for i in line:
        print(i[::-1],end=" ")
    print()