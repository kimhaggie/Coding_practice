#14888
import sys
from collections import deque
import math

def cal(operand, operator, order):
    ans = operand[0]
    step = 1
    for x in order:
        cur_var = operand[step]
        step+=1
        cur_op = operator[x]
        if cur_op == 0:
            ans+=cur_var
        elif cur_op == 1:
            ans-=cur_var
        elif cur_op == 2:
            ans*=cur_var
        else:
            ans/=cur_var
            ans=int(ans)
    return ans

def DFS(visit,cnt,N,operator,cur):
    if cnt == N-1:
        x = cal(operand,operator,cur)
        return [x,x]
    min_val = float('inf')
    max_val = -float('inf')
    for x in range(N-1):
        if not visit[x]:
            visit[x]=True
            cur.append(x)
            tmp = DFS(visit,cnt+1,N,operator,cur)
            if tmp[0] < min_val:
                min_val = tmp[0]
            if max_val < tmp[1]:
                max_val = tmp[1]
            cur.pop()
            visit[x]=False
    return [min_val, max_val]

N = int(sys.stdin.readline().rstrip('\n'))
operand = deque(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
operator = deque(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
new_operator = deque()
for idx,val in enumerate(operator):
    for x in range(val):
        new_operator.append(idx)
operator = new_operator
visit = [False for _ in range(N)]
m,M=DFS(visit,0,N,operator,[])

print(M,m,sep='\n')