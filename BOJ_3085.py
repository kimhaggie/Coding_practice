#3085
import sys
import math

def find(map):
    #가로
    w = 0
    for i in range(n):
        for j in range(n):
            if j == n-1:
                continue
            tmp = 1
            k = j + 1
            while(k!=n):
                if map[i][j]==map[i][k]:
                    tmp += 1
                else:
                    break
                k += 1
            #print(i,j,tmp)
            if w < tmp:
                w = tmp
    h = 0
    for j in range(n):
        for i in range(n):
            if i == n-1:
                continue
            tmp = 1
            k = i + 1
            while(k!=n):
                if map[i][j]==map[k][j]:
                    tmp += 1
                else:
                    break
                k += 1
            #print(i,j,tmp)
            if h < tmp:
                h = tmp
    return max(w,h)

def up(map,i,j):
    if i==0 or map[i][j]==map[i-1][j]: #못 바꿈
        return 0
    tmp = map[i][j]
    map[i][j] = map[i-1][j]
    map[i-1][j] = tmp
    ans = find(map)
    #복구
    tmp = map[i][j]
    map[i][j] = map[i-1][j]
    map[i-1][j] = tmp
    return ans

def down(map,i,j):
    if i==n-1 or map[i][j]==map[i+1][j]: #못 바꿈
        return 0
    tmp = map[i][j]
    map[i][j] = map[i+1][j]
    map[i+1][j] = tmp
    ans = find(map)
    #복구
    tmp = map[i][j]
    map[i][j] = map[i+1][j]
    map[i+1][j] = tmp
    return ans

def left(map,i,j):
    if j==0 or map[i][j]==map[i][j-1]: #못 바꿈
        return 0
    tmp = map[i][j]
    map[i][j] = map[i][j-1]
    map[i][j-1] = tmp
    ans = find(map)
    #복구
    tmp = map[i][j]
    map[i][j] = map[i][j-1]
    map[i][j-1] = tmp
    return ans

def right(map,i,j):
    if j==n-1 or map[i][j]==map[i][j+1]: #못 바꿈
        return 0
    tmp = map[i][j]
    map[i][j] = map[i][j+1]
    map[i][j+1] = tmp
    ans = find(map)
    #복구
    tmp = map[i][j]
    map[i][j] = map[i][j+1]
    map[i][j+1] = tmp
    return ans


n = int(sys.stdin.readline().rstrip('\n'))
map = []
for _ in range(n):
    map.append(list(sys.stdin.readline().rstrip('\n')))
ans = []
for i in range(n):
    for j in range(n):
        u=up(map,i,j)
        d=down(map,i,j)
        l=left(map,i,j)
        r=right(map,i,j)
        tmp = max([u,d,l,r])
        if tmp <= 1:
            tmp = 0
        ans.append(tmp)
print(max(ans))