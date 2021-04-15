import sys

def solution(answers):
    p = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    tmp = [0,0,0]
    for idx,a in enumerate(answers):
        if a==p[0][idx%5]:
            tmp[0]+=1
        if a==p[1][idx%8]:
            tmp[1]+=1
        if a==p[2][idx%10]:
            tmp[2]+=1
    answer=[]
    for idx in range(3):
        if tmp[idx]==max(tmp):
            answer.append(idx+1)
    return answer

answers = [1,2,3,4,5]
# answers = [1,3,2,4,2]
print(solution(answers))