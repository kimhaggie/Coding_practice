#15658
import sys
from collections import deque
import math

def BFS(sub_ans,variable,operator,cur):
    if cur == N:
        return [sub_ans,sub_ans]
    #더하기
    a1 = [float('inf'),-float('inf')]
    a2 = [float('inf'),-float('inf')]
    a3 = [float('inf'),-float('inf')]
    a4 = [float('inf'),-float('inf')]
    if operator[0]>0:
        sub_ans1 = sub_ans + variable[cur]
        new_operator = operator.copy()
        new_operator[0] -= 1
        a1 = BFS(sub_ans1,variable,new_operator,cur+1)
    if operator[1]>0:
        sub_ans2 = sub_ans - variable[cur]
        new_operator = operator.copy()
        new_operator[1] -= 1
        a2 = BFS(sub_ans2,variable,new_operator,cur+1) 
    if operator[2]>0:
        sub_ans3 = sub_ans * variable[cur]
        new_operator = operator.copy()
        new_operator[2] -= 1
        a3 = BFS(sub_ans3,variable,new_operator,cur+1)
    if operator[3]>0:
        sub_ans4 = int(sub_ans / variable[cur])
        new_operator = operator.copy()
        new_operator[3] -= 1
        a4 = BFS(sub_ans4,variable,new_operator,cur+1)
    MIN = [a1[0],a2[0],a3[0],a4[0]]
    MAX = [a1[1],a2[1],a3[1],a4[1]]
    return [min(MIN),max(MAX)]

N = int(sys.stdin.readline().rstrip('\n'))
variable = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
operator =  list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
MIN,MAX = BFS(variable[0],variable,operator,1)
print(MAX,MIN,sep='\n')