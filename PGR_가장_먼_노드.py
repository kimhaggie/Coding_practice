def solution(n, edge):
    answer = 0
    distance = [0 for _ in range(n+1)]
    E = [[] for _ in range(n+1)]
    visit=[False for _ in range(n+1)]
    for x in edge:
        E[x[0]].append(x[1])
        E[x[1]].append(x[0])
    target = [1]
    visit[1]=True
    step=1
    while target:
        new_target = []
        while target:
            cur = target.pop()
            for x in E[cur]:
                if not visit[x]:
                    visit[x]=True
                    distance[x]=step
                    new_target.append(x)
        target = new_target
        step+=1
    max_ans = max(distance)
    for x in distance:
        if x==max_ans:
            answer+=1
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
print(solution(n,edge))