#2004
import sys

def func(x,div):
    ans=0
    mul = div
    while x//div != 0:
        ans += x//div
        div *= mul
    return ans

n, m = map(int,sys.stdin.readline().rstrip('\n').split(' '))
a = 0
b = 0
a+=func(n,2)
b+=func(n,5)
a-=func(m,2)
b-=func(m,5)
a-=func(n-m,2)
b-=func(n-m,5)
print(min([a,b]))