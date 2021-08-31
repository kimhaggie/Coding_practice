from collections import defaultdict

def check(cur):
    for val in cur:
        if val == 0:
            return False
    return True

def solution(gems):
    idx_dict = {}
    answer_len = float('inf')
    answer = []
    gem_set = set(gems)
    for idx,val in enumerate(gem_set):
        idx_dict[val] = idx
    for idx,val in enumerate(gems):
        gems[idx] = idx_dict[val]
    start = 0
    end = len(gem_set)-1
    cur = defaultdict(int)
    for i in range(start,end+1):
        cur[gems[i]]+=1
    while True:
        if answer_len == len(gem_set)-1:
            break
        if start>=len(gems)-len(gem_set)+1 or end>=len(gems):
            break
        if len(cur)==len(gem_set):
            while len(cur)==len(gem_set):
                if start>=len(gems)-len(gem_set)+1:
                    break
                cur[gems[start]]-=1
                if cur[gems[start]]==0:
                    del cur[gems[start]]
                start+=1
            tmp = [start-1,end]
            if tmp[1]-tmp[0]<answer_len:
                answer_len = tmp[1]-tmp[0]
                answer = tmp
        else:
            while not len(cur)==len(gem_set):
                end+=1
                if end>=len(gems):
                    break
                cur[gems[end]]+=1
            if len(cur)==len(gem_set):
                tmp = [start,end]
                if tmp[1]-tmp[0]<answer_len:
                    answer_len = tmp[1]-tmp[0]
                    answer = tmp
    return [answer[0]+1,answer[1]+1]

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems = ["AA", "AB", "AC", "AA", "AC"]
gems = ["XYZ", "XYZ", "XYZ"]
print(solution(gems))