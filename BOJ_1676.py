#1676
import sys

def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

def zero(n):
    n = list(str(n))
    ans=0
    for i in reversed(n):
        if i == '0':
            ans+=1
        else:
            break
    return ans

n = int(sys.stdin.readline().rstrip('\n'))
print(zero(factorial(n)))