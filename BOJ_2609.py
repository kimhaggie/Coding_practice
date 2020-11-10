#2609
import sys

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return int(a*b/gcd(a,b))
    
a,b = map(int,sys.stdin.readline().rstrip('\n').split(' '))
print(gcd(a,b),'\n',lcm(a,b),sep='')