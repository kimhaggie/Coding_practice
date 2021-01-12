#10971
import sys

def tsp(a):
    if len(a) == 1:
        ans.append(a[0])
        tmp = 0
        for idx in range(len(ans)-1):
            tmp += W[ans[idx]][ans[idx+1]]
        tmp += W[ans[-1]][ans[0]]
        if W[ans[-2]][ans[-1]]!=0 and W[ans[-1]][ans[0]]!=0:
            A.append(tmp)
        ans.pop()
    for idx in range(len(a)):
        ans.append(a[idx])
        b=a.copy()
        del b[idx]
        if len(ans)==1 or W[ans[-2]][ans[-1]]!=0:
            tsp(b)
        ans.pop()

n = int(sys.stdin.readline().rstrip('\n'))
W = []
for _ in range(n):
    W.append(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
a = list(range(n))
ans = []
A = []
tsp(a)
print(min(A))