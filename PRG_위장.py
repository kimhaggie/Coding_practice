import sys

def solution(clothes):
    D = dict()
    for item, kind in clothes:
        if kind in D.keys():
            D[kind] += 1
        else:
            D[kind] = 1
    answer = 1
    for kind in D.keys():
        answer*=(D[kind]+1)
    return answer-1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))