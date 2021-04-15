import sys

# 동1 서2 북3 남4
dy = [0,0,-1,1]
dx = [1,-1,0,0]

def right(x):
    return [x[0], x[2], x[3], x[5], x[4], x[1]]

def left(x):
    return [x[0], x[5], x[1], x[2], x[4], x[3]]

def up(x):
    return [x[5], x[1], x[0], x[3], x[2], x[4]]

def down(x):
    return [x[2], x[1], x[4], x[3], x[5], x[0]]

N,M,x,y,K = map(int,sys.stdin.readline().rstrip('\n').split())
m = []
for _ in range(N):
    m.append(list(map(int,sys.stdin.readline().rstrip('\n').split())))
cmd = list(map(int,sys.stdin.readline().rstrip('\n').split()))
for i in range(len(cmd)):
    cmd[i]-=1
dice = [0 for _ in range(6)]
ans = []
for d in cmd:
    next_x = x+dy[d]
    next_y = y+dx[d]
    if not(0<=next_x<N and 0<=next_y<M):
        continue
    if d==0:
        dice = right(dice)
    elif d==1:
        dice = left(dice)
    elif d==2:
        dice = up(dice)
    else:
        dice = down(dice)
    if m[next_x][next_y]==0:
        m[next_x][next_y]=dice[2]
    else:
        dice[2]=m[next_x][next_y]
        m[next_x][next_y]=0
    x=next_x
    y=next_y
    ans.append(str(dice[-1]))
print('\n'.join(ans))