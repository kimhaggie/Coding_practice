def solution(n, computers):
    answer = 0
    E = [[]for _ in range(n)]
    visit= [False for _ in range(n)]
    for idx, edge in enumerate(computers):
        for i, val in enumerate(edge):
            if i==idx:
                continue
            if val == 1:
                E[idx].append(i)
    # print(E)
    while sum(visit) != n:
        cur=-1
        for idx, val in enumerate(visit):
            if not val:
                cur = idx
                visit[cur]=True
                break
        target = [cur]
        answer+=1
        while target:
            new_target = []
            while target:
                cur = target.pop()
                for next_ in E[cur]:
                    if not visit[next_]:
                        visit[next_] = True
                        new_target.append(next_)
            target = new_target
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))