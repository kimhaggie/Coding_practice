dx=[1,-1,0,0]
dy=[0,0,1,-1]

def BFS(i,j,place):
    target = [[i,j]]
    step = 0
    visit = [[False for _ in range(5)] for _ in range(5)]
    visit[i][j]=True
    while target:
        if step==2:
            break
        new_target= []
        while target:
            cur = target.pop()
            for i in range(4):
                next_x = cur[0]+dx[i]
                next_y = cur[1]+dy[i]
                if 0<=next_x<5 and 0<=next_y<5 and not visit[next_x][next_y]:
                    if place[next_x][next_y]=='P':
                        # import pdb;pdb.set_trace()
                        return False
                    if place[next_x][next_y]=='O':
                        new_target.append([next_x,next_y])
                    visit[i][j] = True
        step+=1
        target = new_target
    return True

def solution(places):
    answer = []
    for place in places:
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append([i,j])
        flag = True
        for p in people:
            if not BFS(p[0],p[1],place):
                flag = False
        answer.append(1 if flag else 0)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
# print(places[0][0][0])
print(solution(places))