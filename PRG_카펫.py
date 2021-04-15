import sys

def solution(brown, yellow):
    total = brown+yellow
    for x in range(1,total//2):
        if total%x==0:
            y = total//x
            if yellow == (x-2)*(y-2) and total-(x-2)*(y-2)==brown:
                if x<=y:
                    return [y,x]
                else:
                    return [x,y]
    answer = []
    return answer

brown = 10
yellow = 2
brown = 8
yellow = 1
brown = 24
yellow = 24
print(solution(brown, yellow))
