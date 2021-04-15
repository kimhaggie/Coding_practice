from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights[::-1]
    n = len(truck_weights)
    out = []
    time = 0
    bridge = 0
    mid = deque()
    while len(out) != n:
        time += 1
        for idx, val in enumerate(mid):
            mid[idx] = [val[0]-1,val[1]]
        for idx in range(len(mid)):
            cur = mid[0]
            if cur[0]==0:
                bridge-=cur[1]
                out.append(cur[1])
                mid.popleft()
            else:
                break
        if not truck_weights:
            continue
        cur = truck_weights[-1]
        if cur+bridge<=weight:
            cur = truck_weights.pop()
            bridge += cur
            mid.append([bridge_length,cur])
    return time

# bridge_length=2
# weight=10
# truck_weights=[7,4,5,6]
bridge_length=100
weight=100
truck_weights=[10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))