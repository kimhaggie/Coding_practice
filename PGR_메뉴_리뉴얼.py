#36분

from itertools import combinations

def common(x,y):
    x = set(list(x))
    y = set(list(y))
    z = list(x&y)
    return z

def solution(orders, course):
    answer = []
    candidate = set()
    for i in range(len(orders)):
        for j in range(i+1,len(orders)):
            tmp = ''.join(sorted(common(orders[i],orders[j])))
            if len(tmp)<2:
                continue
            for l in range(2,len(tmp)+1):
                for v in list(combinations(tmp,l)):
                    candidate.add(''.join(sorted(v)))
    for l in course:
        target = dict()
        for x in candidate:
            if len(x)==l:
                target[x]=0
        for t in target.keys():
            for o in orders:
                if set(list(o)) & set(list(t)) == set(list(t)):
                    target[t]+=1
        if not target:
            continue
        M = max(target.values())
        for k,v in target.items():
            if v==M:
                answer.append(k)
    return sorted(list(answer))

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
print(solution(orders,course))