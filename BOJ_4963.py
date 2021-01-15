#4963
import sys
from collections import deque

def check(i,j,m,w,h):#상하좌우 순서대로 1,2,3,4 
    #print(i,j)
    #상
    if i==0:
        up=False
    else:
        if (not visit[i-1][j]) and m[i-1][j] == '1':
            up=True
        else:
            up=False
    #하
    if i==h-1:
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
    if j==w-1:
        right = False
    else:
        if (not visit[i][j+1]) and m[i][j+1] == '1':
            right = True
        else:
            right = False
    #1
    if not(i>0 and j>0):
        lu = False
    else:
        if (not visit[i-1][j-1]) and m[i-1][j-1] == '1':
            lu = True
        else:
            lu = False
    #2
    if not(i>0 and j<w-1):
        ru = False
    else:
        if (not visit[i-1][j+1]) and m[i-1][j+1] == '1':
            ru = True
        else:
            ru = False
    #3
    if not(i<h-1 and j>0):
        ld = False
    else:
        if (not visit[i+1][j-1]) and m[i+1][j-1] == '1':
            ld = True
        else:
            ld = False
    #4
    if not(i<h-1 and j<w-1):
        rd = False
    else:
        if (not visit[i+1][j+1]) and m[i+1][j+1] == '1':
            rd = True
        else:
            rd = False
    return [up,down,left,right,lu,ru,ld,rd]

def BFS(i,j,m,w,h):
    num = 0
    deq = deque()
    deq.append([i,j])
    visit[i][j]=True
    num += 1
    while len(deq)!=0:
        a, b = deq.popleft()
        up,down,left,right,lu,ru,ld,rd = check(a,b,m,w,h)
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
        if lu:
            num+=1
            visit[a-1][b-1]=True
            deq.append([a-1,b-1])
        if ru:
            num+=1
            visit[a-1][b+1]=True
            deq.append([a-1,b+1])
        if ld:
            num+=1
            visit[a+1][b-1]=True
            deq.append([a+1,b-1])
        if rd:
            num+=1
            visit[a+1][b+1]=True
            deq.append([a+1,b+1])
    return num
A = []
while(True):
    w,h = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    if w==0 and h==0:
        break
    m = []
    for _ in range(h):
        m.append(sys.stdin.readline().rstrip('\n').split(' '))
    visit = [[False for _ in range(w)] for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if (not visit[i][j]) and m[i][j]=='1':
                ans += 1
                BFS(i,j,m,w,h)
    A.append(ans)
print('\n'.join(map(str,A)))