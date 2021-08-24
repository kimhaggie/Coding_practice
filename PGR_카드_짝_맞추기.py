import sys, copy

from itertools import permutations
from collections import deque
    
def remove_card(card):
    global board_c, card_position
    for x, y in card_position[card]: 
        board_c[x][y] = 0

def restore_card(card):
    global board_c, card_position
    for x, y in card_position[card]: 
        board_c[x][y] = card
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs1(r,c,x,y):
    global board_c
    board = board_c
    stack = []
    stack.append([r,c])
    step = 0
    visit = [[False for _ in range(4)] for _ in range(4)]
    visit[r][c]=True
    while stack:
        new_stack = []
        while stack:
            cur = stack.pop()
            if cur[0]==x and cur[1]==y:
                return step
            for idx in range(4):
                next_x = cur[0]+dx[idx]
                next_y = cur[1]+dy[idx]
                if 0<=next_x<4 and 0<=next_y<4:
                    if not visit[next_x][next_y]:
                        visit[next_x][next_y] = True
                        new_stack.append([next_x,next_y])
            for idx in range(4):
                next_x = cur[0]+dx[idx]
                next_y = cur[1]+dy[idx]
                if not (0<=next_x<4 and 0<=next_y<4):
                    continue
                while True:
                    if board[next_x][next_y]!=0:
                        if not visit[next_x][next_y]:
                            visit[next_x][next_y] = True
                            new_stack.append([next_x,next_y])
                        break
                    next_x += dx[idx]
                    next_y += dy[idx]
                    if not (0<=next_x<4 and 0<=next_y<4):
                        if not visit[next_x-dx[idx]][next_y-dy[idx]]:
                            visit[next_x-dx[idx]][next_y-dy[idx]] = True
                            new_stack.append([next_x-dx[idx],next_y-dy[idx]])
                        break
        step+=1
        stack = new_stack

haggie = 0
func_call = 0

def go(sx, sy, order, card_num, count, move): 
    global answer, order_p, card_position, board_c,haggie,func_call
    print(sx,sy)
    print(count)
    func_call+=1
    if count == card_num:
        print('--')
        answer = min(answer, move)
        return
    
    card = order_p[order][count]
    
    left = card_position[card][0]
    right = card_position[card][1]
    
    d1 = bfs1(sx, sy, left[0], left[1])             # 출발 지점 -> 해당카드 왼쪽
    d2 = bfs1(left[0], left[1], right[0], right[1]) # 해당카드 왼쪽 -> 해당카드 오른쪽
    haggie+=2

    remove_card(card)
    go(right[0], right[1], order, card_num, count+1, move+d1+d2)
    restore_card(card)
    
    d1 = bfs1(sx, sy, right[0], right[1])           # 출발 지점 -> 해당카드 오른쪽
    d2 = bfs1(right[0], right[1], left[0], left[1]) # 해당카드 오른쪽 -> 해당카드 왼쪽
    haggie+=2
    
    remove_card(card)
    go(left[0], left[1], order, card_num, count+1, move+d1+d2)
    restore_card(card)
    
def solution(board, r, c):
    global answer, order_p, card_position, board_c,haggie
    for x in board:
        print(*x)
    answer = sys.maxsize
    board_c = copy.deepcopy(board)
    card_position = {}

    for i in range(4):
        for j in range(4):
            num = board[i][j]
            if num != 0:
                if num in card_position.keys():
                    card_position[num].append([i, j])
                else:
                    card_position[num] = [[i, j]]
                    
    orders = [k for k, v in card_position.items()]
    order_p = list(permutations(orders, len(orders))) # 제거 순서
    
    for i in range(len(order_p)):
        print('----',order_p[i])
        go(r, c, i, len(card_position.keys()), 0, 0)
    print(haggie)
    print(func_call)
    return answer + 2*len(card_position)

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]	
r = 1 
c = 0
print(solution(board,r,c))