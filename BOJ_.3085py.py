#3085
import sys
import math

def find(map):
    #가로
    w = 0
    for i in range(n):
        j=0
        while(j!=n):
            if j == n-1:
                j+=1
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
            j = k
    h = 0
    for j in range(n):
        i=0
        while(i!=n):
            if i == n-1:
                i+=1
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
            i=k
    return max(w,h)

def up(map,i,j):
    if i==0 or map[i][j]==map[i-1][j]: #못 바꿈
        return 0
    map[i][j],map[i-1][j]=map[i-1][j],map[i][j]
    ans = find(map)
    #복구
    map[i][j],map[i-1][j]=map[i-1][j],map[i][j]
    return ans

def left(map,i,j):
    if j==0 or map[i][j]==map[i][j-1]: #못 바꿈
        return 0
    map[i][j],map[i][j-1]=map[i][j-1],map[i][j]
    ans = find(map)
    #복구
    map[i][j],map[i][j-1]=map[i][j-1],map[i][j]
    return ans



n = int(sys.stdin.readline().rstrip('\n'))
map = []
for _ in range(n):
    map.append(list(sys.stdin.readline().rstrip('\n')))
ans = 0
for i in range(n):
    for j in range(n):
        u=up(map,i,j)
        l=left(map,i,j)
        tmp = max(u,l)
        if tmp <= 1:
            tmp = 0
        if ans<tmp:
            ans=tmp
print(ans)