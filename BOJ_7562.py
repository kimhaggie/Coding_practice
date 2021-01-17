#7562
import sys
from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

def BFS(m,I,deq,target_i,target_j):
    while len(deq)!=0:
        i,j,d = deq.popleft()
        if i==target_i and j==target_j:
            return d
        for idx in range(8):
            next_i = i + dy[idx]
            next_j = j + dx[idx]
            if 0<=next_i<I and 0<=next_j<I and m[next_i][next_j]==0:
                deq.append([next_i,next_j,d+1])
                m[next_i][next_j] = 1

T = int(sys.stdin.readline().rstrip('\n'))
for _ in range(T):
    I = int(sys.stdin.readline().rstrip('\n'))
    start_i,start_j = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    target_i,target_j = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    m = [[0 for _ in range(I)] for _ in range(I)]
    m[start_i][start_j] = 1
    deq = deque()
    deq.append([start_i,start_j,0])
    print(BFS(m,I,deq,target_i,target_j))