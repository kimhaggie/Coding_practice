#14501
import sys

def func(T,P,start):
    for idx in range(start,len(T)):
        if idx + T[idx] == len(T):
            ans.append(idx)
            tmp = 0
            for i in ans:
                tmp += P[i]
            ans.pop()
            if x[0] < tmp:
                x[0] = tmp
        elif idx + T[idx] > len(T):
            tmp = 0
            for i in ans:
                tmp += P[i]
            if x[0] < tmp:
                x[0] = tmp
        else:
            ans.append(idx)
            func(T,P,idx+T[idx])
            ans.pop()

N = int(sys.stdin.readline().rstrip('\n'))
T = []
P = []
ans = []
x = [0]
for _ in range(N):
    t, p = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    T.append(t)
    P.append(p)
func(T,P,0)
print(x[0])