#1182
import sys

def func(a, start, sub_sum, S, flag):
    n = len(a)
    if start == n and sub_sum == S:
        return 1
    if start == n:
        return 0
    ans = 0
    if flag and sub_sum == S:
        ans += 1
    for idx in range(start, n):
        sub_sum += a[idx]
        ans += func(a, idx+1, sub_sum, S, True)
        sub_sum -= a[idx]
    return ans

N, S = map(int,sys.stdin.readline().rstrip('\n').split(' '))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
print(func(a, 0, 0, S, False))