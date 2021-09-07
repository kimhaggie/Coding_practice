def check(col,relation):
    key = []
    for idx in range(len(relation)):
        cur = ''
        for j in col:
            cur+=relation[idx][j]
        key.append(cur)
    return len(key) == len(set(key))

def poss(col,relation):
    if not check(col,relation):
        return False
    for idx in range(len(col)):
        tmp = col.copy()
        tmp.pop(idx)
        if check(tmp,relation):
            return False
    return True

def solution(relation):
    global answer
    answer = 0
    # DFS([],0,relation)
    for case in range(1,2**len(relation[0])):
        cur = []
        for i in range(len(relation[0])):
            if case& 1<<i:
                cur.append(i)
        # print(case,cur)
        if poss(cur,relation):
            answer+=1
    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
relation = [['1','1','a'],['1','1','b']]
print(solution(relation))