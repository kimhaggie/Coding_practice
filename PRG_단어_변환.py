import sys

def count(a,b):
    d = 0
    for i in range(len(a)):
        if a[i]!=b[i]:
            d+=1
    return d == 1

def solution(begin, target, words):
    visit = [False for _ in range(len(words))]
    answer = 0
    Q = [begin]
    while Q:
        new_Q = []
        while Q:
            cur = Q.pop()
            if cur == target:
                return answer
            for idx,word in enumerate(words):
                if not visit[idx] and count(cur,word):
                    visit[idx] = True
                    new_Q.append(word)
        Q = new_Q
        answer+=1
    return 0

begin = "hit"
target = "cog"
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))