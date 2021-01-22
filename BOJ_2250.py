#2250
import sys
from collections import deque

class node():
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
        self.left_num = -1
        self.right_num = -1
        self.depth = -1
        self.parent = 0

N = int(sys.stdin.readline().rstrip('\n'))
Tree = [0 for _ in range(N+1)]
root = list(range(1,N+1))
end = []
for _ in range(N):
    a,b,c = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    Tree[a] = node(a,b,c)
    if b in root:
        root.remove(b)
    if c in root:
        root.remove(c)
    if b==-1 and c==-1:
        end.append(a)
root = root[0]
stack = [Tree[root]]
depth = 0
while len(stack)!=0:
    new_stack = []
    while len(stack)!=0:
        cur = stack.pop()
        cur.depth = depth
        if cur.left != -1:
            new_stack.append(Tree[cur.left])
            Tree[cur.left].parent = cur.data
        if cur.right != -1:
            new_stack.append(Tree[cur.right])
            Tree[cur.right].parent = cur.data
    stack = new_stack
    depth += 1
    
stack = [Tree[root]]
while len(stack)!=0:
    cur = stack[-1]
    if cur.left == -1 and cur.right == -1:#마지막 노드
        cur.left_num = 0
        cur.right_num = 0
        stack.pop()
    else:#마지막 노드 아님
        if cur.left_num > 0 and cur.right_num > 0:#채움
            stack.pop()
            continue
        if cur.left != -1:
            if Tree[cur.left].left_num == -1 or Tree[cur.left].right_num == -1:
                stack.append(Tree[cur.left])
                continue
            else:
                cur.left_num = Tree[cur.left].left_num + Tree[cur.left].right_num + 1
        else:
            cur.left_num = 0
        if cur.right != -1:
            if Tree[cur.right].left_num == -1 or Tree[cur.right].right_num == -1:
                stack.append(Tree[cur.right])
                continue
            else:
                cur.right_num = Tree[cur.right].left_num + Tree[cur.right].right_num + 1
        else:
            cur.right_num = 0
        stack.pop()

for idx in range(1,N+1):
    x = Tree[idx]
    # print(x.data,x.left_num,x.right_num,x.depth,x.parent)

coord = [[] for _ in range(N+1)]
coord[root] = [0,0]
stack = [root]
while len(stack) != 0:
    new_stack = []
    while len(stack) != 0:
        cur = stack.pop()
        if len(coord[cur]) == 0:
            if Tree[cur].left!=-1:
                new_stack.append(Tree[cur].left)
            if Tree[cur].right!=-1:
                new_stack.append(Tree[cur].right)
            par = Tree[cur].parent
            if Tree[par].left == cur:#왼쪽 자식일 때
                coord[cur] = [coord[par][0]-Tree[cur].right_num-1,Tree[cur].depth]
            else:#오른쪽 자식일 때
                coord[cur] = [coord[par][0]+Tree[cur].left_num+1,Tree[cur].depth]
        else:
            if Tree[cur].left_num > 0:
                new_stack.append(Tree[cur].left) 
            if Tree[cur].right_num > 0:
                new_stack.append(Tree[cur].right) 
    stack = new_stack
d = dict()
for val in coord:
    if len(val)==0:
        continue
    if val[1] in d:
        d[val[1]].append(val[0])
    else:
        d[val[1]] = [val[0]]
ans = []
for idx in range(max(d.keys())+1):
    tmp = d[idx]
    tmp = sorted(tmp)
    ans.append(tmp[-1]-tmp[0]+1)
max_val = 0
max_idx = -1
for idx, val in enumerate(ans):
    if max_val < val:
        max_idx = idx
        max_val = val
print(max_idx+1,max_val)