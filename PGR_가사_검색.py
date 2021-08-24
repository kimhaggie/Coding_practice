from copy import deepcopy

import sys
sys.setrecursionlimit(100001)

class node(object):
    def __init__(self,data):
        self.data = data
        self.end = 0
        self.child = dict()
        self.child_length = dict()

def insert(cur_node,word,start):
    if start == len(word):
        cur_node.end = 1
        return
    if word[start] in cur_node.child:
        insert(cur_node.child[word[start]],word,start+1)
        if not len(word)-start in cur_node.child_length.keys():
            cur_node.child_length[len(word)-start] = 1
        else:
            cur_node.child_length[len(word)-start] += 1
    else:
        cur_node.child[word[start]] = node(word[start])
        if not len(word)-start in cur_node.child_length.keys():
            cur_node.child_length[len(word)-start] = 1
        else:
            cur_node.child_length[len(word)-start] += 1
        insert(cur_node.child[word[start]],word,start+1)

def search(cur_node, word, start):
    if start == len(word):
        return cur_node.end
    result = 0
    cur_word = word[start]
    if cur_word == '?':
        if len(word)-start in cur_node.child_length:
            result += cur_node.child_length[len(word)-start]
    else:
        if cur_word in cur_node.child:
            result += search(cur_node.child[cur_word],word,start+1)
    return result

def solution(words, queries):
    global answer
    answer = []
    root = node(None)
    reverse_root = node(None)
    cnt = dict()
    for word in words:
        insert(root,word,0)
        insert(reverse_root,word[::-1],0)
        if len(word) in cnt.keys():
            cnt[len(word)]+=1
        else:
            cnt[len(word)] = 1
    for query in queries:
        if query[-1]=='?':
            answer.append(search(root,query,0))
        elif query[0]=='?':
            answer.append(search(reverse_root,query[::-1],0))
        else:
            answer.append(cnt[len(word)])
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?",'t?????','????????a','?????']
print(solution(words,queries))