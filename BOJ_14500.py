#14500
import sys
import math

def check1(M,n,m):
    ans = 0
    for i in range(n):
        for j in range(m-3):
            tmp = M[i][j]+M[i][j+1]+M[i][j+2]+M[i][j+3]
            if ans < tmp:
                ans = tmp
    return ans

def check2(M,n,m):
    ans = 0
    for i in range(n-1):
        for j in range(m-1):
            tmp = M[i][j]+M[i+1][j]+M[i][j+1]+M[i+1][j+1]
            if ans < tmp:
                ans = tmp
    return ans

def check3(M,n,m):
    ans = 0
    for i in range(n-2):
        for j in range(m-1):
            tmp = M[i][j]+M[i+1][j]+M[i+2][j]+M[i+2][j+1]
            if ans < tmp:
                ans = tmp
    return ans

def check4(M,n,m):
    ans = 0
    for i in range(n-2):
        for j in range(m-1):
            tmp = M[i][j]+M[i+1][j]+M[i+1][j+1]+M[i+2][j+1]
            if ans < tmp:
                ans = tmp
    return ans

def check5(M,n,m):
    ans = 0
    for i in range(n-1):
        for j in range(m-2):
            tmp = M[i][j]+M[i][j+1]+M[i+1][j+1]+M[i][j+2]
            if ans < tmp:
                ans = tmp
    return ans

def check6(M,n,m):
    ans = 0
    for i in range(n-2):
        for j in range(m-1):
            tmp = M[i][j+1]+M[i+1][j+1]+M[i+2][j+1]+M[i+2][j]
            if ans < tmp:
                ans = tmp
    return ans
    
def check7(M,n,m):
    ans = 0
    for i in range(n-2):
        for j in range(m-1):
            tmp = M[i][j+1]+M[i+1][j+1]+M[i+1][j]+M[i+2][j]
            if ans < tmp:
                ans = tmp
    return ans

n,m = map(int,sys.stdin.readline().rstrip('\n').split(' '))
M1 = []
for i in range(n):
    M1.append(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
M2 = list(zip(*M1[::-1]))
M3 = list(zip(*M2[::-1]))
M4 = list(zip(*M3[::-1]))
ans = max([check1(M1,n,m),check1(M2,m,n),
            check2(M1,n,m),
            check3(M1,n,m),check3(M2,m,n),check3(M3,n,m),check3(M4,m,n),
            check4(M1,n,m),check4(M2,m,n),
            check5(M1,n,m),check5(M2,m,n),check5(M3,n,m),check5(M4,m,n),
            check6(M1,n,m),check6(M2,m,n),check6(M3,n,m),check6(M4,m,n),
            check7(M1,n,m),check7(M2,m,n)])
print(ans)