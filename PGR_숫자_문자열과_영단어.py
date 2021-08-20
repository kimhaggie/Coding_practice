words = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

def solution(s):
    answer = []
    idx = 0
    while idx<len(s):
        val = s[idx]
        if ord('a')<=ord(val)<=ord('z'):
            for word in words.keys():
                if word == s[idx:idx+len(word)]:
                    answer.append(words[word])
                    idx+=len(word)
                    break
        else:
            answer.append(val) 
            idx+=1
    return ''.join(answer)

s = "123"
# print(word)
print(solution(s))
