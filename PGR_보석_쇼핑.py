def solution(gems):
    answer = [0, float('inf')]
    start = 0
    end = 0
    cur = dict()
    total = len(set(gems))
    idx = [start,end]
    while not (start == len(gems) and end == len(gems)):
        if len(cur.keys())!=total and end<len(gems):
            gem = gems[end]
            if gem in cur.keys():
                cur[gem]+=1
            else:
                cur[gem]=1
            idx[1]=end
            if len(cur.keys())==total:
                if idx[1]-idx[0]+1<answer[1]-answer[0]:
                    answer = idx.copy()
            end+=1
        else:
            # print(StrOrBytesPath)
            gem = gems[start]
            # print(cur)
            if cur[gem]==1:
                del cur[gem]
            else:
                cur[gem]-=1
            idx[0]=start+1
            if len(cur.keys())==total:
                if idx[1]-idx[0]<answer[1]-answer[0]:
                    answer = idx.copy()
            start+=1 
    return [answer[0]+1,answer[1]+1]

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
print(solution(gems))