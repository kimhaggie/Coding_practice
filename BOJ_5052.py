import sys

t = int(sys.stdin.readline().rstrip('\n'))
for _ in range(t):
    n = int(sys.stdin.readline().rstrip('\n'))
    A = []
    for _ in range(n):
        x = sys.stdin.readline().rstrip('\n')
        A.append(x)
    A = sorted(A)
    answer = "YES"
    for idx in range(len(A)-1):
        a = A[idx]
        b = A[idx+1]
        if len(a)<=len(b):
            if a==b[:len(a)]:
                answer='NO'
                break
        else:
            if b==a[:len(b)]:
                answer='NO'
                break
    print(answer)