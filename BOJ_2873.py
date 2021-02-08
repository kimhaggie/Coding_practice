#2873
import sys
from collections import deque
import math
import copy
import heapq

R, C = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
min_val = float('inf')
min_idx = []
for i in range(R):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    for j in range(C):
        if x[j] < min_val and (i+j)%2==1:
            min_idx = [i,j]
            min_val = x[j]
    m.append(x)
ans = ''
if R%2==0 and C%2==0:
    cur = [0,0]
    if min_idx[1] == C-1:
        flag = True
        ans+=('D'*(R-1)+'R'+'U'*(R-1)+'R')*(C//2-1)
        cmd = ['R','D','L','D']
        move = [[0,1],[1,0],[0,-1],[1,0]]
        cur = [0,C-2]
        idx =0
        while cur != [R-1,C-1]:
                if cur[0]+move[idx%4][0] == min_idx[0] and cur[1]+move[idx%4][1] == min_idx[1]:
                    idx-=1
                else:
                    cur[0]+=move[idx%4][0]
                    cur[1]+=move[idx%4][1]
                    ans += cmd[idx%4]
                    idx+=1
        print(ans)
    else: #normal
        flag = True
        flag = True
        for j in range(min_idx[1]):
            if flag:
                ans+='D'*(R-1)
            else:
                ans+='U'*(R-1)
            ans+='R'
            flag = not flag
        #flag == True면 아래로 내려갈 차례
        if flag:
            cmd = ['R','D','L','D']
            move = [[0,1],[1,0],[0,-1],[1,0]]
            idx = 0
            cur = [0,min_idx[1]]
            while cur != [R-1,min_idx[1]+1]:
                if cur[0]+move[idx%4][0] == min_idx[0] and cur[1]+move[idx%4][1] == min_idx[1]:
                    idx-=1
                else:
                    cur[0]+=move[idx%4][0]
                    cur[1]+=move[idx%4][1]
                    ans += cmd[idx%4]
                    idx+=1
            ans+='R'
        else:
            cmd = ['R','U','L','U']
            move = [[0,1],[-1,0],[0,-1],[-1,0]]
            idx = 0
            cur = [R-1,min_idx[1]]
            while cur != [0,min_idx[1]+1]:
                if cur[0]+move[idx%4][0] == min_idx[0] and cur[1]+move[idx%4][1] == min_idx[1]:
                    idx-=1
                else:
                    cur[0]+=move[idx%4][0]
                    cur[1]+=move[idx%4][1]
                    ans += cmd[idx%4]
                    idx+=1
            ans+='R'
        flag = not flag
        for j in range(min_idx[1]+2,C):
            if flag:
                ans+='D'*(R-1)
            else:
                ans+='U'*(R-1)
            ans+='R'
            flag = not flag
        print(ans[:-1])
else:
    if R%2==0:
        flag = True
        for j in range(C):
            if flag:
                ans+='D'*(R-1)
            else:
                ans+='U'*(R-1)
            ans+='R'
            flag = not flag
    else:
        flag = True
        for i in range(R):
            if flag:
                ans+='R'*(C-1)
            else:
                ans+='L'*(C-1)
            ans+='D'
            flag = not flag
    print(ans[:-1])    