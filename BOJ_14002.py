#14002
import sys
import math

N = int(sys.stdin.readline().rstrip('\n'))
A = [0]+list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
ans = [0]*(N+1) # i 포함해서 최대로 긴 수열 길이
ans_list = [[] for _ in range(N+1)]
ans[1] = 1
ans_list[1] = [A[1]]
for i in range(2,N+1):
    tmp = 1
    tmp_list = [A[i]]
    for j in range(1,i+1):
        if A[j] < A[i] and tmp < ans[j] + 1:
            tmp = ans[j] + 1
            tmp_list = ans_list[j]+[A[i]]
    ans[i] = tmp
    ans_list[i] = tmp_list
max_idx=0
max_val=0
for idx in range(N+1):
    if max_val < ans[idx]:
        max_idx=idx
        max_val = ans[idx]

print(max_val)
print(' '.join(map(str,ans_list[max_idx])))