#1987
import sys
from collections import deque
import math

dy = [1,-1,0,0]
dx = [0,0,1,-1]

def DFS(R,C,i,j,m,step,alpha):
    flag=False
    for idx in range(4):
        next_i = i+dy[idx]
        next_j = j+dx[idx]
        if 0<=next_i<R and 0<=next_j<C and not alpha[m[next_i][next_j]]:
            flag = True
            alpha[m[next_i][next_j]]=True
            DFS(R,C,next_i,next_j,m,step+1,alpha)
            alpha[m[next_i][next_j]]=False
    if not flag and ans[0]<step:        
        ans[0]=step
R, C = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
ans = [0]
for _ in range(R):
    x = list(sys.stdin.readline().rstrip('\n'))
    tmp = []
    for val in x:
        tmp.append(ord(val)-ord('A')) 
    m.append(tmp)

alpha = [False for _ in range(26)]
alpha[m[0][0]]=True
DFS(R,C,0,0,m,1,alpha)
print(ans[0])