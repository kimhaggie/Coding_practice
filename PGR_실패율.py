def solution(N, stages):
    answer = []
    not_clear = [0 for _ in range(N)]
    visit = [0 for _ in range(N)]
    for s in stages:
        for i in range(s):
            if i==N:
                break
            visit[i]+=1
        if s!=N+1:
            not_clear[s-1]+=1
        # print(s)
        # print(not_clear)
        # print(visit)
        # print('----')
    ratio = [[0,N-i] for i in range(N)]
    for idx,(a,b) in enumerate(zip(not_clear,visit)):
        if b==0:
            ratio[idx][0]=0
        else:
            ratio[idx][0]=a/b
    # print(ratio)
    # print(sorted(ratio,reverse=True))
    for x in sorted(ratio,reverse=True):
        answer.append(N-x[1]+1)
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))