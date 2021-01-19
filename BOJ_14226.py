#14226
import sys
from collections import deque

S = int(sys.stdin.readline().rstrip('\n'))

deq = deque([[1,0,0]]) #현재 이모티콘 수, 클립보드의 이모티콘 수, 시간
visit = [[] for _ in range(1001)]
while True:
    cur, clip, time = deq.popleft()
    if cur == S:
        print(time)
        break
    #op1 복사
    if (not cur in visit[cur]) and cur!=clip and 0<=cur<=1000:
        visit[cur].append(clip)
        deq.append([cur,cur,time+1])
    #op2 -1
    if (not clip in visit[cur-1]) and 0<=cur-1<=1000:
        visit[cur-1].append(clip)
        deq.append([cur-1,clip,time+1])
    #op3 붙여넣기
    if (cur+clip<=1000) and (not clip in visit[cur+clip]) and 0<=cur+clip<=1000 and clip!=0:
        visit[cur+clip].append(clip)
        deq.append([cur+clip,clip,time+1])
