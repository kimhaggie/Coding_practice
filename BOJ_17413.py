#17413
import sys
from collections import deque

sentence = sys.stdin.readline().rstrip('\n')
word = deque([])
flag = False
for idx, val in enumerate(sentence):
    if len(word)==0:
        word.append(val)
        if val == '<':
            flag = True
    else:
        if flag:
            word.append(val)
            if val == '>':
                x=''
                for i in word:
                    x += i
                print(x, end = '')
                word = deque([])
                flag = False
        else:
            if val == ' ' and not flag:
                x=''
                for i in word:
                    x += i
                print(x[::-1],end = ' ')
                word = deque([])
            elif val == '<':
                x=''
                for i in word:
                    x += i
                print(x[::-1],end = '')
                word = deque(['<'])
                flag = True
            else:
                word.append(val)
    if idx == len(sentence)-1 and len(word) != 0:
        if flag:
            x=''
            for i in word:
                x += i
            print(x, end = '')
        else:
            x=''
            for i in word:
                x += i
            print(x[::-1],end = '')