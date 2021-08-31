import heapq

#동 북 서 남
#0  1  2  3

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def solution(board):
    N = len(board)
    answer = 0
    target = []
    visit = [[[float('inf'),float('inf'),float('inf'),float('inf')] for _ in range(N)] for _ in range(N)]
    visit[0][0] = [0,0,0,0]
    heapq.heappush(target,[0,0,0,0])
    heapq.heappush(target,[0,0,0,3])

    while target:
        cur = heapq.heappop(target)
        # print(cur)
        if cur[1]==N-1 and cur[2]==N-1:
            return cur[0]
        next_x = cur[1]+dx[cur[3]]
        next_y = cur[2]+dy[cur[3]]
        if 0<=next_x<N and 0<=next_y<N and board[next_x][next_y]==0:
            # if not visit[next_x][next_y][(cur[3]+3)%4]:
            #     visit[next_x][next_y][(cur[3]+3)%4] = True
            if cur[0]+600<visit[next_x][next_y][(cur[3]+3)%4]:
                visit[next_x][next_y][(cur[3]+3)%4]=cur[0]+600
                heapq.heappush(target,[cur[0]+600,next_x,next_y,(cur[3]+3)%4])
            # if not visit[next_x][next_y][(cur[3]+1)%4]:
            #     visit[next_x][next_y][(cur[3]+1)%4] = True
            if cur[0]+600<visit[next_x][next_y][(cur[3]+1)%4]:
                visit[next_x][next_y][(cur[3]+1)%4]=cur[0]+600
                heapq.heappush(target,[cur[0]+600,next_x,next_y,(cur[3]+1)%4])
            # if not visit[next_x][next_y][cur[3]]:            
            #     visit[next_x][next_y][cur[3]] = True
            
            if cur[0]+100<visit[next_x][next_y][cur[3]]:
                visit[next_x][next_y][cur[3]]=cur[0]+100
                heapq.heappush(target,[cur[0]+100,next_x,next_y,cur[3]])
    return answer

board = [[0,0,0],[0,0,0],[0,0,0]]
board = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
# board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
print(solution(board))