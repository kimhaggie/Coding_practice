import sys

def BFS(start, E, visit):
    target = [start]
    while target:
        new_target= []
        while target:
            cur = target.pop()
            cur_e = E[cur]
            for val in cur_e:
                if not visit[val]:
                    visit[val] = True
                    new_target.append(val)
        target = new_target


def solution(n, computers):
    E = [[] for _ in range(n)]
    for idx, val in enumerate(computers):
        tmp = []
        for i, j in enumerate(val):
            if i==idx:
                continue
            if j==1:
                tmp.append(i)
        E[idx] = tmp
    visit = [False for _ in range(n)]
    answer = 0
    for start in range(n):
        if not visit[start]:
            answer += 1
            BFS(start, E, visit)
    return answer

n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers =[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))