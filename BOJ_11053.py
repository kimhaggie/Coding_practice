#11053
import sys
import math

N = int(sys.stdin.readline().rstrip('\n'))
A = [0]+list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
ans = [0]*(N+1) # i 포함해서 최대로 긴 수열 길이
num = [0]*(N+1)
ans[1] = 1
for i in range(2,N+1):
    tmp = 1
    for j in range(1,i+1):
        if A[j] < A[i] and tmp < ans[j] + 1:
            tmp = ans[j] + 1
    ans[i] = tmp
    
print(max(ans))