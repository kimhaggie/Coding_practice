def compute(user_id, banned_id):
    answer=0
    for user, ban in zip(user_id,banned_id):
        flag = True
        for i, j in zip(user,ban):
            if j=='*':
                continue
            elif i==j:
                continue
            else:
                flag = False
        if len(user)!=len(ban):
            flag = False
        if flag:
            answer+=1
    return answer==len(user_id)

def DFS(cur, user_id, banned_id):
    sub = set()
    if len(cur)==len(banned_id):
        if compute(cur,banned_id):
            # print('.'.join(sorted(cur)))
            return set(['.'.join(sorted(cur))])
    else:
        for idx in range(len(user_id)):
            if user_id[idx] in cur:
                continue
            cur.append(user_id[idx])
            x = DFS(cur,user_id,banned_id)
            sub = sub|x
            cur.pop()
    return sub
    

def solution(user_id, banned_id):
    answer = 0
    x = DFS([],user_id,banned_id)
    # print(x)
    answer = len(x)
    return answer

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id,banned_id)) 