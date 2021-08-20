import heapq

def solution(jobs):
    answer = 0
    heap = []
    n = len(jobs)
    jobs = sorted(jobs)[::-1]
    current = []
    time = 0
    # print(jobs)
    while jobs or heap or current:
        # print(time, jobs, heap, sep='\t')
        if current:
            current[0]-=1
        if current and current[0]==0:
            answer+=time-current[1]
            current=[]
        while True:
            if not jobs:
                break
            cur = jobs[-1]
            if time == cur[0]:
                heapq.heappush(heap,[cur[1],cur[0]])
                jobs.pop()
            else:
                break
        if heap and not current:
            current = heapq.heappop(heap)
        # print('current',current)
        time+=1

    return answer//n

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))