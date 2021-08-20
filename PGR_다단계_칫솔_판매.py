def solution(enroll, referral, seller, amount):
    answer = []
    enroll.append('-')
    edge = dict()
    for i,j in zip(enroll,referral):
        edge[i] = j
    profit = dict()
    for i in enroll:
        profit[i]=0
    for i,j in zip(seller, amount):
        if profit[i]!=0:
            profit[i] += 100*j
        else:
            profit[i] = 100*j
    real_profit = profit.copy()
    extra = dict()
    for i in enroll:
        extra[i] = 0
    target = list(set(seller))
    # print(profit)
    # print(target)
    for cur in target:
        # print('start',cur)
        cur_money = real_profit[cur]
        while True:
            # print(cur)
            if cur!='-':
                next_ = edge[cur]
                profit[next_]+=cur_money//10
                profit[cur]-=cur_money//10
                cur_money = cur_money//10
            else:
                break
            cur = edge[cur]
    for i in enroll:
        if i == '-':
            break
        answer.append(profit[i])
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))