import sys

# 0 북 1 동 2 남 3 서
dy = [-1,0,1,0]
dx = [0,1,0,-1]

N, M = map(int,sys.stdin.readline().rstrip('\n').split())
r, c, d = map(int,sys.stdin.readline().rstrip('\n').split())
m = []
for _ in range(N):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split()))
    m.append(x)
visit = [[False for _ in range(M)]for _ in range(N)]
ans = 0
while True:
    if m[r][c] == 0 and not visit[r][c]:
        visit[r][c] = True
        ans += 1
        continue
    remain = 0
    for idx in range(4):
        i = r+dy[idx]
        j = c+dx[idx]
        if m[i][j]==0 and not visit[i][j]:
            remain+=1
    if remain==0:
        back = (d+2)%4
        back_i = r+dy[back]
        back_j = c+dx[back]
        if m[back_i][back_j]==1:
            break
        else:
            r=back_i
            c=back_j
            continue
    left = (d-1)%4
    if m[r+dy[left]][c+dx[left]]==0 and not visit[r+dy[left]][c+dx[left]]:
        r+=dy[left]
        c+=dx[left]
        d=left
        continue
    if not(m[r+dy[left]][c+dx[left]]==0 and not visit[r+dy[left]][c+dx[left]]):
        d=left
        continue
print(ans)