#4963
dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,1,-1,-1]
def bfs(i,j):
    queue = [[i,j]]
    matrix[i][j] = 0
    while queue:
        [a,b] = queue.pop(0)
        for k in range(8):
            x = a+dx[k]
            y = b+dy[k]
            if 0<=x<h and 0<=y<w and matrix[x][y] == 1:
                matrix[x][y] = 0
                queue.append([x,y])
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    matrix = []
    cnt = 0
    for i in range(h):
        matrix.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)