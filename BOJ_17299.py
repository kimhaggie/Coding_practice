#17299
import sys
from collections import deque
n = int(sys.stdin.readline().rstrip('\n'))
elements = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
freq = dict.fromkeys(set(elements),0)
for i in elements:
    freq[i] += 1
freq_list = [0 for _ in range(n)]
for idx, val in enumerate(elements):
    freq_list[idx] = freq[val]
deq = deque([])
ans = [-1 for _ in range(n)]

for idx, val in enumerate(freq_list):
    if len(deq) == 0:
        deq.append(idx)
    else:
        while (len(deq) != 0 and freq_list[deq[-1]] < val):
            x = deq.pop()
            ans[x] = elements[idx]
        deq.append(idx)
answer = ''
for idx, val in enumerate(ans):
    if idx == len(ans)-1:
        answer += str(val)
    else:
        answer += (str(val)+' ')
print(answer)