from collections import deque
from itertools import permutations

def solution(n, weak, dist):
    answer = float('inf')
    D = deque(weak)
    for _ in range(len(weak)):
        # print('start',D)
        for order in permutations(dist,len(dist)):
            # print(order)
            cur_d = D.copy()
            cnt = 0
            for l in order:
                # print(l,cur_d)
                if not cur_d:
                    break
                start = cur_d[0]
                end = start+l
                if end<n:
                    while start<=cur_d[0]<=end:
                        cur_d.popleft()
                        if not cur_d:
                            break
                else:
                    while start<=cur_d[0]<n:
                        cur_d.popleft()
                        if not cur_d:
                            break
                    if cur_d:
                        while 0<=cur_d[0]<=end%n:
                            cur_d.popleft()
                            if not cur_d:
                                break
                cnt+=1
            # print('cnt',cnt)
            if not cur_d:
                answer = min(answer,cnt)
        D.append(D.popleft())
    if answer == float('inf'):
        answer = -1
    return answer

n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]
weak = [0,1,2,3]
dist = [1,1]
print(solution(n,weak,dist))