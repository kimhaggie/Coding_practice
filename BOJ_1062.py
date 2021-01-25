#1062
import sys
from collections import deque
import math

def DFS(start,poss,word,n,K,alpha):
    if n==K or len(poss) == len(alpha)-5:
        ans = 0
        for x in word:
            flag = True
            for t in x:
                if not t in alpha:
                    flag = False
                    break
            if flag:
                ans+=1
        return ans
    ans = 0
    for idx in range(start,len(poss)):
        cur = poss[idx]
        alpha.append(cur)
        x = DFS(idx+1,poss,word,n+1,K,alpha)
        if ans<x:
            ans = x
        alpha.pop()
    return ans

N, K = map(int, sys.stdin.readline().rstrip('\n').split(' '))
word = []
poss = set()
for _ in range(N):
    x=list(set(sys.stdin.readline().rstrip('\n')))
    tmp = set()
    for val in x:
        tmp.add(ord(val)-ord('a'))
        poss.add(ord(val)-ord('a'))
    word.append(list(tmp))
poss=list(poss)
if K<5:
    print(0)
    sys.exit()
alpha=[]
for a in ['a','n','t','i','c']:
    poss.remove(ord(a)-ord('a'))
    alpha.append(ord(a)-ord('a'))
print(DFS(0,poss,word,5,K,alpha))