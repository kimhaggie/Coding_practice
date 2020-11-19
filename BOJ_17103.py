#17103
import sys
import math
n = int(sys.stdin.readline().rstrip('\n'))
A=[]
for _ in range(n):
    A.append(int(sys.stdin.readline().rstrip('\n')))
max_A = max(A)

prime = [1,1] + [0 for _ in range(2,max_A+1)]
prime_number=[]
for i in range(2,max_A+1):
    if prime[i] == 0:
        prime[i] = 2
        prime_number.append(i)
        x = i + i
        while x < max_A+1:
            prime[x] = 1
            x += i
            
for val in A:
    ans=0
    for i in prime_number:
        if i >=int(val/2)+1:
            break
        if prime[val-i] == 2:
            ans+=1
    print(ans)