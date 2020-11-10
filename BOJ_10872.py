#10872
import sys

def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

n = int(sys.stdin.readline().rstrip('\n'))
print(factorial(n))