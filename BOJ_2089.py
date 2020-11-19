#2089
import sys
import math

n = int(sys.stdin.readline().rstrip('\n'))
ans=''
if n==0:
    print(0)
while n!=0:
    ans+=str(n%2)
    n=math.ceil(n/(-2))
print(ans[::-1])