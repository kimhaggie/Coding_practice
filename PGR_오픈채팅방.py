def solution(record):
    db = dict()
    answer = []
    for re in record:
        cur = re.split()
        if cur[0]=='Enter':
            db[cur[1]] = cur[2]
            answer.append([0,cur[1]])
        elif cur[0] == 'Leave':
            answer.append([1,cur[1]])
        elif cur[0] == 'Change':
            db[cur[1]] = cur[2]
    for idx, val in enumerate(answer):
        if val[0] == 0:#Enter
            answer[idx] = db[val[1]]+'님이 들어왔습니다.'
        else:
            answer[idx] = db[val[1]]+'님이 나갔습니다.'
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))