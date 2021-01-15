#2667
import sys
from collections import deque

def check(i,j,m):#상하좌우 순서대로
    n = len(m)
    #상
    if i==0:
        up=False
    else:
        if (not visit[i-1][j]) and m[i-1][j] == '1':
            up=True
        else:
            up=False
    #하
    if i==n-1:
        down=False
    else:
        if (not visit[i+1][j]) and m[i+1][j] == '1':
            down = True
        else:
            down = False
    #좌
    if j==0:
        left=False
    else:
        if (not visit[i][j-1]) and m[i][j-1] == '1':
            left = True
        else:
            left = False
    #우
    if j==n-1:
        right = False
    else:
        if (not visit[i][j+1]) and m[i][j+1] == '1':
            right = True
        else:
            right = False
    return [up,down,left,right]

def BFS(i,j):
    num = 0
    deq = deque()
    deq.append([i,j])
    visit[i][j]=True
    num += 1
    while len(deq)!=0:
        a, b = deq.popleft()
        up,down,left,right = check(a,b,m)
#        print(a,b,up,down,left,right)
        if up:
            num+=1
            visit[a-1][b]=True
            deq.append([a-1,b])
        if down:
            num+=1
            visit[a+1][b]=True
            deq.append([a+1,b])
        if left:
            num+=1
            visit[a][b-1]=True
            deq.append([a,b-1])
        if right:
            num+=1
            visit[a][b+1]=True
            deq.append([a,b+1])
    return num
   
N = int(sys.stdin.readline().rstrip('\n'))
m = []
for _ in range(N):
    m.append(list(sys.stdin.readline().rstrip('\n')))
visit = [[False for _ in range(N)] for _ in range(N)]
ans = [0]
for i in range(N):
    for j in range(N):
        if (not visit[i][j]) and m[i][j]=='1':
            #print('-----',i,j)
            ans[0]+=1
            ans.append(BFS(i,j))
print(ans[0])
print('\n'.join(map(str,sorted(ans[1:]))))