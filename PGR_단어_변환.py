def difference(a,b):
    answer=0
    for i,j in zip(a,b):
        if i!=j:
            answer+=1
    return answer

def solution(begin, target, words):
    answer = 0
    visit = dict()
    for val in words:
        visit[val] = False
    tar = [begin]
    if begin in visit.keys():
        visit[begin] = True
    step = 0
    while tar:
        new_tar = []
        while tar:
            cur = tar.pop()
            if cur == target:
                return step
            for word in words:
                if not visit[word] and difference(cur,word)==1:
                    visit[word] = True
                    new_tar.append(word)
        tar = new_tar
        step+=1
    return 0

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin,target, words))