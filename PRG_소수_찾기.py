import sys

prime_num = [True for _ in range(10000000)]
prime_num[0] = False
prime_num[1] = False
for cur in range(2,5001):
    if not prime_num[cur]:
        continue
    tmp = cur
    cur *= 2
    while cur<10000000:
        prime_num[cur] = False
        cur+=tmp

def BFS(numbers, n):
    target = [['',[False for _ in range(len(numbers))]]]
    d = 0
    while target:
        if d==n:
            ans = set()
            for x in target:
                if prime_num[int(x[0])] and len(str(int(x[0])))==len(x[0]):
                    ans.add(x[0])
            return len(ans)
        new_target = []
        while target:
            cur = target.pop()
            visit = cur[1]
            for i in range(len(numbers)):
                if not visit[i]:
                    tmp = visit.copy()
                    tmp[i]=True
                    new_target.append([cur[0]+numbers[i],tmp])
        target = new_target
        d += 1

def solution(numbers):
    answer = 0
    for idx in range(1,len(numbers)+1):
        answer+=BFS(numbers,idx)
    return answer

# numbers = "17"
# numbers = "011"
numbers = '035728'
print(solution(numbers))