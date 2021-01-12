#1759
import sys

def func(a,start,mask,m,L):
    if m == 0:
        tmp = []
        for idx in range(len(mask)):
            if not mask[idx]:
                tmp.append(a[idx])
        if len(tmp)==L:
            vowel = 0
            if 'a' in tmp:
                vowel += 1
            if 'e' in tmp:
                vowel += 1
            if 'i' in tmp:
                vowel += 1
            if 'o' in tmp:
                vowel += 1
            if 'u' in tmp:
                vowel += 1
            con = L-vowel
            if vowel >= 1 and con >= 2:
                print(''.join(tmp))
    for idx in range(start,len(a)):
        if mask[idx]:
            mask[idx] = False
            func(a,idx+1,mask,m-1,L)
            mask[idx] = True
        
L, C = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
a = sorted(sys.stdin.readline().rstrip('\n').split(' '))
mask = [True for _ in range(C)]
func(a,0,mask,L,L)