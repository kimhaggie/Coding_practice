import sys

dy = [-1,1,0,0]
dx = [0,0,1,-1]

N,L,R = map(int,sys.stdin.readline().rstrip('\n').split())
m = [[[0,-1] for _ in range(N)]for _ in range(N)]
for i in range(N):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split()))
    for j in range(N):
        m[i][j][0]=x[j] 

def check_move():
    cnt = 0
    visit = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            m[i][j][1]=-1
    family = []
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                continue
            tmp = []
            target = [[i,j]]
            visit[i][j]=True
            while target:
                new_target = []
                while target:
                    cur = target.pop()
                    for idx in range(4):
                        if 0<=cur[0]+dy[idx]<N and 0<=cur[1]+dx[idx]<N and not visit[cur[0]+dy[idx]][cur[1]+dx[idx]]:
                            next_ = [cur[0]+dy[idx],cur[1]+dx[idx]]
                            if L<=abs(m[cur[0]][cur[1]][0]-m[next_[0]][next_[1]][0])<=R:
                                if m[cur[0]][cur[1]][1]==-1:
                                    m[cur[0]][cur[1]][1]=cnt
                                    tmp.append(cur)
                                    cnt+=1
                                m[next_[0]][next_[1]][1]=m[cur[0]][cur[1]][1]
                                visit[cur[0]+dy[idx]][cur[1]+dx[idx]]=True
                                new_target.append(next_)
                                tmp.append(next_)
                target = new_target
            if tmp:
                family.append(tmp)
    for idx in range(cnt):
        S = 0
        for i,j in family[idx]:
            S+=m[i][j][0]
        S = int(S/len(family[idx]))
        for i,j in family[idx]:
            m[i][j][0] = S
    if cnt>0:
        return True
    else:
        return False

ans = 0
while check_move():
    ans+=1
print(ans)