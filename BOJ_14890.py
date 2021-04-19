import sys

def check(line, L):
    idx = 0
    n = len(line)
    visit = [False for _ in range(n)]
    while True:
        if idx==n-1:
            return True
        #평평
        if line[idx] == line[idx+1]:
            idx+=1
            continue
        if abs(line[idx]-line[idx+1])>=2:
            return False
        #오르막길
        if line[idx]+1 ==  line[idx+1]:
            if not(idx-(L-1)>=0):
                return False
            else:
                same = line[idx]
                for i in range(L):
                    if line[idx-i]!=same:
                        return False
                for i in range(L):
                    if visit[idx-i]:
                        return False
                    visit[idx-i]=True
                idx+=1
            continue
        #내리막길
        if line[idx]-1 == line[idx+1]:
            if idx>=n-L:
                return False
            else:
                same = line[idx+1]
                for i in range(L):
                    if line[idx+1+i]!=same:
                        return False
                for i in range(L):
                    if visit[idx+1+i]:
                        return False
                    visit[idx+1+i]=True
                idx+=L
            continue

N, L = map(int,sys.stdin.readline().rstrip('\n').split())
m = []
reverse_m = [[]for _ in range(N)]
for i in range(N):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split()))
    m.append(x)
    for j in range(N):
        reverse_m[j].append(x[j])
ans=0
for a,b in zip(m,reverse_m):
    if check(a,L):
        ans+=1
    if check(b,L):
        ans+=1
print(ans)