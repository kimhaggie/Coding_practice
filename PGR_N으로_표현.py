def solution(N, number):
    if N==number:
        return 1
    answer = -1
    dp = [[0], [N]]
    while len(dp)!=9:
        next_ = set()
        for idx in range(1,len(dp)):
            cur_a = dp[idx]
            cur_b = dp[-idx]
            for x in cur_a:
                for y in cur_b:
                    if y!=0 and number in [x+y,x-y,x*y,x//y]:
                        answer = len(dp)
                    if y==0 and number in [x+y,x-y,x*y]:
                        answer = len(dp)
                    next_.add(x+y)
                    next_.add(x-y)
                    next_.add(x*y)
                    if y!=0:
                        next_.add(x//y)
        if answer!=-1:
            break
        next_=list(next_)
        next_.append(dp[-1][0]*10+N)
        dp.append(list(reversed(next_)))
    return answer

N = 5
number = 5
print(solution(N, number))