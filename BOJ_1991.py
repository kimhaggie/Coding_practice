#1991
import sys
from collections import deque

def preorder(Tree,cur):
    print(chr(cur+65),end='')
    if Tree[cur][0]>=0:
        preorder(Tree,Tree[cur][0])
    if Tree[cur][1]>=0:
        preorder(Tree,Tree[cur][1])

def midorder(Tree,cur):
    if Tree[cur][0]>=0:
        midorder(Tree,Tree[cur][0])
    print(chr(cur+65),end='')
    if Tree[cur][1]>=0:
        midorder(Tree,Tree[cur][1])

def postorder(Tree,cur):
    if Tree[cur][0]>=0:
        postorder(Tree,Tree[cur][0])
    if Tree[cur][1]>=0:
        postorder(Tree,Tree[cur][1])
    print(chr(cur+65),end='')

N = int(sys.stdin.readline().rstrip('\n'))
Tree = [[] for _ in range(26)]
for _ in range(N):
    p,c1,c2 = map(ord,sys.stdin.readline().rstrip('\n').split(' '))
    p-=65
    c1-=65
    c2-=65
    if c1>=0:
        Tree[p].append(c1)
    else:
        Tree[p].append(-1)
    if c2>=0:
        Tree[p].append(c2)
    else:
        Tree[p].append(-1)
#pre
preorder(Tree,0)
print()
#mid
midorder(Tree,0)
print()
#post
postorder(Tree,0)
print()