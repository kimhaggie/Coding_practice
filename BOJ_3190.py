import sys

#우 상 좌 하
dy = [0,-1,0,1]
dx = [1,0,-1,0]

N = int(sys.stdin.readline().rstrip('\n'))
K = int(sys.stdin.readline().rstrip('\n'))
apple = []
for _ in range(K):
    apple.append(list(map(int,sys.stdin.readline().rstrip('\n').split())))
L = int (sys.stdin.readline().rstrip('\n'))
cmd = []
for _ in range(L):
    x = sys.stdin.readline().rstrip('\n').split()
    cmd.append([int(x[0]),x[1]])
m = [[[0,-1] for _ in range(N)] for _ in range(N)]
for i,j in apple:
    m[i-1][j-1] = [1,-1]
m[0][0] = [2,0]
snake = [[0,0]]
time = 0
while True:
    next_snake = []
    #뒤부터 머리 0번째가 꼬리
    head = snake.pop()
    way = m[head[0]][head[1]][1]
    original_way = way
    for x,y in cmd:
        if time==x:
            if y=='L':
                way = (way+1)%4
            elif y=='D':
                way = (way-1)%4
            break
    next_head = [head[0]+dy[way],head[1]+dx[way]]
    #벽에 부딪힘
    if not (0<=next_head[0]<N and 0<=next_head[1]<N):
        time+=1
        break
    #자기 몸에 부딪힘
    if m[next_head[0]][next_head[1]][0]==2:
        time+=1
        break
    #사과 먹음
    eat = False
    if m[next_head[0]][next_head[1]][0]==1:
        eat = True
    m[next_head[0]][next_head[1]] = [2,way]
    if snake:
        m[head[0]][head[1]] = [0,way]
    else:
        if eat:
            m[head[0]][head[1]] = [2,way]
        else:
            m[head[0]][head[1]] = [0,-1]
    next_snake.append(next_head)
    if eat:
        next_snake.append(head)
    while snake:
        cur = snake.pop()
        way = m[cur[0]][cur[1]][1]
        next_ = [cur[0]+dy[way],cur[1]+dx[way]]
        next_way = m[next_[0]][next_[1]][1]
        m[next_[0]][next_[1]] = [2,next_way]
        next_snake.append(next_)
        if snake:
            m[cur[0]][cur[1]] = [0,way]
        #꼬리인 경우
        else:
            if eat:
                m[cur[0]][cur[1]] = [2,way]   
                next_snake.append(cur)             
            else:
                m[cur[0]][cur[1]] = [0,-1]
    snake = next_snake[::-1]
    time+=1
print(time)