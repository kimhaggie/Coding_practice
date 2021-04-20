import sys
import copy

N, M, H = map(int,sys.stdin.readline().rstrip('\n').split())
m =[[0 for _ in range(N)] for _ in range(H)]

def check(m):
    ans = 0
    for start in range(N):
        cur_i=0
        cur_j=start
        while cur_i!=H:
            if m[cur_i][cur_j]==0:
                cur_i+=1
            elif m[cur_i][cur_j]==1:
                cur_i+=1
                cur_j+=1
            else:
                cur_i+=1
                cur_j-=1
        if cur_j==start:
            ans+=1
        else:
            return False
    if ans==N:
        return True

def DFS(path,n):
    if len(path)==n:
        for idx, x in enumerate(path):
            i = x//(N-1)
            j = x%(N-1)
            if m[i][j]==0 and m[i][j+1]==0:
                m[i][j]=1
                m[i][j+1]=-1
            else:
                for a, b in enumerate(path):
                    if a==idx:
                        return 0
                    i = b//(N-1)
                    j = b%(N-1)
                    m[i][j]=0
                    m[i][j+1]=0
        if check(m):
            print(n)
            sys.exit()
        for x in path:
            i = x//(N-1)
            j = x%(N-1)
            m[i][j]=0
            m[i][j+1]=0
    else:
        if len(path)==0:
            for x in range((N-1)*H):
                i = x//(N-1)
                j = x%(N-1)
                if m[i][j]!=0 or m[i][j+1]!=0:
                    continue
                path.append(x)
                DFS(path,n)
                path.pop()
        else:
            cur = path[-1]
            for x in range(cur+1, (N-1)*H):
                i = x//(N-1)
                j = x%(N-1)
                if m[i][j]!=0 or m[i][j+1]!=0:
                    continue
                path.append(x)
                DFS(path,n)
                path.pop()
                
for _ in range(M):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split()))
    a = x[0]-1
    b = x[1]-1
    m[a][b]=1
    m[a][b+1]=-1
for i in range(4):
    DFS([],i)
print(-1)