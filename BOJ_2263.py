#2263
import sys
from collections import deque
import math
import copy
import heapq

sys.setrecursionlimit(10000000)

def func(i_start,i_end,p_start,p_end,ans):
    if i_end-i_start < 0:
        return 0
    elif i_end-i_start == 0:
        ans.append(str(inorder[i_start]))
        return 0
    root = postorder[p_end]
    idx = order[root]
    ans.append(str(root))
    func(i_start,idx-1,p_start,p_start+idx-i_start-1,ans)
    func(idx+1,i_end,p_start+idx-i_start,p_end-1,ans)

n = int(sys.stdin.readline().rstrip('\n'))
inorder = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
postorder = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
order = dict()
for idx,val in enumerate(inorder):
    order[val]=idx
ans = []
func(0,n-1,0,n-1,ans)
print(' '.join(ans))