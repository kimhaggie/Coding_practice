def solution(n, results):
    answer = 0
    forward = [[] for _ in range(n)]
    backward = [[] for _ in range(n)]
    for i,j in results:
        forward[i-1].append(j-1)
        backward[j-1].append(i-1)
    # print(forward, backward)
    for idx in range(n):
        visit = [False for _ in range(n)]
        visit[idx] = True
        target = [idx]
        while target:
            new_target = []
            while target:
                cur = target.pop()
                # print(cur)
                for x in forward[cur]:
                    # print('x',x)
                    if not visit[x]:
                        visit[x]= True
                        new_target.append(x)
            target = new_target
        sub1 = sum(visit)
        visit = [False for _ in range(n)]
        visit[idx] = True
        target = [idx]
        while target:
            new_target = []
            while target:
                cur = target.pop()
                for x in backward[cur]:
                    if not visit[x]:
                        visit[x]= True
                        new_target.append(x)
            target = new_target
        sub2 = sum(visit)
        # print(idx, sub1,sub2)
        if sub1+sub2==n+1:
            answer+=1
    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n,results))