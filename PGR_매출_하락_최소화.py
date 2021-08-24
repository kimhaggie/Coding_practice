from collections import deque
import heapq

def travel(x,child,sales):
    global dp
    for y in child[x]:
        travel(y,child,sales)
    if not child[x]:
        dp[x][0]=sales[x]
        dp[x][1]=0
    else:
        sub = [float('inf'),float('inf')]
        tmp1 = 0
        for y in child[x]:
            tmp1+=min(dp[y][0],dp[y][1])
        if tmp1+sales[x]<sub[0]:
            sub[0] = tmp1+sales[x]
                
        for i in range(2**len(child[x])):
            tmp2 = 0
            if i==0:
                for y in child[x]:
                    tmp2+=dp[y][1]
                rest = float('inf')
                for y in child[x]:
                    if not child[y]:
                        if sales[y]<rest:
                            rest = sales[y]
                tmp2+=rest
            else:
                for idx,y in enumerate(child[x]):
                    if 1<<idx & i:
                        tmp2+=dp[y][0]
                    else:
                        tmp2+=dp[y][1]
            if tmp2<sub[1]:
                sub[1] = tmp2
        dp[x][0] = sub[0]
        dp[x][1] = sub[1]

def solution(sales, links):
    global dp
    sales = deque(sales)
    sales.appendleft(float('inf'))
    child = [[] for _ in range(len(sales))]
    for link in links:
        child[link[0]].append(link[1])
    dp = [[float('inf') for _ in range(2)] for _ in range(len(sales))]
    travel(1,child,sales)
    return min(dp[1][0],dp[1][1])

sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
print(solution(sales,links))