import sys

N = int(sys.stdin.readline().rstrip('\n'))
A = list(map(int,sys.stdin.readline().rstrip('\n').split()))
B, C = map(int,sys.stdin.readline().rstrip('\n').split())
ans = N
for i in range(N):
    cur = A[i]-B
    if cur<=0:
        continue
    else:
        if cur%C==0:
            ans+=cur//C
        else:
            ans+=(cur//C+1)
print(ans)