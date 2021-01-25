#4574
import sys
from collections import deque
import math

def check(i,j,val,m):
    block_i = i//3
    block_j = j//3
    a = list(range(1,10))
    for y in range(block_i*3,block_i*3+3):
        for x in range(block_j*3,block_j*3+3):
            if m[y][x] in a:
                a.remove(m[y][x])
    for idx in range(9):
        if m[i][idx] in a:
            a.remove(m[i][idx])
        if m[idx][j] in a:
            a.remove(m[idx][j])
    if val in a:
        return True
    else:
        return False

def DFS(domino,m,visit,n):
    target_i = -1
    target_j = -1
    for i in range(9):
        for j in range(9):
            if m[i][j]==0:
                target_i = i
                target_j = j
                break
        if target_i!=-1:
            break
    if target_i==-1:
        print('Puzzle',n)
        for x in m:
            print(*x,sep='')
        return True
    i=target_i
    j=target_j
    for idx,val in enumerate(visit):
        if val:
            continue
        block = domino[idx]
        #가로
        if j+1<9 and m[i][j+1]==0 and check(i,j,block[0],m) and check(i,j+1,block[1],m):
            m[i][j]=block[0]
            m[i][j+1]=block[1]
            visit[idx]=True
            a = DFS(domino,m,visit,n)
            if a:
                return True
            m[i][j]=0
            m[i][j+1]=0
            visit[idx]=False
        #역 가로
        if j+1<9 and m[i][j+1]==0 and check(i,j,block[1],m) and check(i,j+1,block[0],m):
            m[i][j]=block[1]
            m[i][j+1]=block[0]
            visit[idx]=True
            a = DFS(domino,m,visit,n)
            if a:
                return True
            m[i][j]=0
            m[i][j+1]=0
            visit[idx]=False
        #세로
        if i+1<9 and m[i+1][j]==0 and check(i,j,block[0],m) and check(i+1,j,block[1],m):
            m[i][j]=block[0]
            m[i+1][j]=block[1]
            visit[idx]=True
            a = DFS(domino,m,visit,n)
            if a:
                return True
            m[i][j]=0
            m[i+1][j]=0
            visit[idx]=False
        #역 세로
        if i+1<9 and m[i+1][j]==0 and check(i,j,block[1],m) and check(i+1,j,block[0],m):
            m[i][j]=block[1]
            m[i+1][j]=block[0]
            visit[idx]=True
            a = DFS(domino,m,visit,n)
            if a:
                return True
            m[i][j]=0
            m[i+1][j]=0
            visit[idx]=False
            
def change(x):
    i = ord(x[0])-ord('A')
    j = int(x[1])-1
    return [i,j]

n=1
while(True):
    N = int(sys.stdin.readline().rstrip('\n'))
    if N == 0:
        break
    m = [[0 for _ in range(9)] for _ in range(9)]
    domino = []
    for i in range(1,10):
        for j in range(i+1,10):
            domino.append([i,j])
    for _ in range(N):
        x = sys.stdin.readline().rstrip('\n').split(' ')
        pos = change(x[1])
        x[0]=int(x[0])
        x[2]=int(x[2])
        m[pos[0]][pos[1]] = x[0]
        pos = change(x[3])
        m[pos[0]][pos[1]] = x[2]
        domino.remove([min(x[0],x[2]),max(x[0],x[2])])
    x = sys.stdin.readline().rstrip('\n').split(' ')
    for idx,val in enumerate(x):
        pos = change(val)
        m[pos[0]][pos[1]] = idx+1
    visit = [False for _ in range(len(domino))]
    DFS(domino,m,visit,n)
    n+=1