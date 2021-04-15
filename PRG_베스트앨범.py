import sys

def solution(genres, plays):
    D = dict()
    for idx, (g, p) in enumerate(zip(genres, plays)):
        if g in D.keys():
            D[g].append([idx,p])
        else:
            D[g] = [[idx,p]]
    for key in D.keys():
        D[key] = sorted(D[key], key = lambda x: x[1], reverse=True)
    total = []
    for key in D.keys():
        tmp = 0 
        for x,y in D[key]:
            tmp+=y
        total.append([key,tmp])
    total = sorted(total, key = lambda x: x[1], reverse = True)
    answer = []
    for g, _ in total:
        if len(D[g])==1:
            answer.append(D[g][0][0])
        else:
            for idx,(x,y) in enumerate(D[g]):
                if idx == 2:
                    break
                answer.append(x)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))