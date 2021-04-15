import sys

def solution(citations):
    c = [0 for _ in range(max(citations)+1)]
    for x in citations:
        c[x]+=1
    left = 0
    right = sum(c)
    for h in range(max(citations)):
        if right>=h:
            left+=c[h]
            right-=c[h]
            continue
        else:
            return h-1
    return 0

citations = [3, 0, 6, 1, 5]
citations = [0,0,0,0]
print(solution(citations))