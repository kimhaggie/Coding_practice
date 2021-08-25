
#기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
#보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

#0은 기둥 1은 보

def check_a(n,x,y):
    global m
    if x==0:
        return True
    else:
        if 0 in m[x-1][y]:
            return True
    if y>0:
        if 1 in m[x][y-1] or 1 in m[x][y]:
            return True
    else:
        if 1 in m[x][y]:
            return True
    return False

def check_b(n,x,y):
    global m
    if x>0:
        if 0 in m[x-1][y]:
            return True
        if y<n-1:
            if 0 in m[x-1][y+1]:
                return True
    if 0<y<n-1:
        if (1 in m[x][y-1] and 1 in m[x][y+1]):
            return True
    return False

def solution(n, build_frame):
    answer = []
    global m
    m = [[set() for _ in range(n+1)] for _ in range(n+1)]
    for cmd in build_frame:
        x,y,a,b = cmd
        x,y=y,x
        if b==1:
            if a==0:
                flag = check_a(n+1,x,y)
                if flag:
                    m[x][y].add(0)
            else:
                flag = check_b(n+1,x,y)
                if flag:
                    m[x][y].add(1)
        else:
            if a in m[x][y]:
                m[x][y].remove(a)
            else:
                continue
            flag = True
            if a==0:
                check = []
                tmp = [[x+1,y-1,1],[x+1,y,0],[x+1,y,1],[x,y-1,1],[x-1,y,0],[x,y,1]]
                for X,Y,Z in tmp:
                    if 0<=X<n+1 and 0<=Y<n+1 and Z in m[X][Y]:
                        check.append([X,Y,Z])
                for sub_cmd in check:
                    if sub_cmd[2]==0:
                        if not check_a(n+1,sub_cmd[0],sub_cmd[1]):
                            flag = False
                            break
                    if sub_cmd[2]==1:
                        if not check_b(n+1,sub_cmd[0],sub_cmd[1]):
                            flag = False
                            break
            else:
                check = []
                tmp = [[x,y-1,1],[x,y,0],[x,y+1,0],[x,y+1,1],[x-1,y+1,0],[x-1,y,0]]
                for X,Y,Z in tmp:
                    if 0<=X<n+1 and 0<=Y<n+1 and Z in m[X][Y]:
                        check.append([X,Y,Z])
                for sub_cmd in check:
                    if sub_cmd[2]==0:
                        if not check_a(n+1,sub_cmd[0],sub_cmd[1]):
                            flag = False
                            break
                    if sub_cmd[2]==1:
                        if not check_b(n+1,sub_cmd[0],sub_cmd[1]):
                            flag = False
                            break
            if not flag:
                m[x][y].add(a)
        # print(cmd)
        # for l in reversed(m):
        #     print(*l)
    for i in range(n+1):
        for j in range(n+1):
            for x in m[i][j]:
                answer.append([j,i,x])
    return sorted(answer)

n =5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n,build_frame))