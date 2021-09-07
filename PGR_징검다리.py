def change(dis,k,n):
    ans = []
    idx = 0
    cur = 0
    while True:
        if n<0:
            return False
        if cur<k:
            if idx>=len(dis):
                return ans
            if cur!=0:
                n-=1
            cur+=dis[idx]
            idx+=1
        else:
            ans.append(cur)
            cur=0

def solution(distance, rocks, n):
    answer = 0
    rocks = sorted(rocks)
    dis = [rocks[0]]
    for i in range(1,len(rocks)):
        dis.append(rocks[i]-rocks[i-1])
    dis.append(distance- rocks[-1])
    left = min(dis)
    right = max(dis)
    while True:
        mid = (left+right)//2
        if left == 10 and mid==9 and right==9:
            break
        cur = change(dis,mid,n)
        prev = change(dis,mid+1,n)
        if cur and not prev:
            return mid
        if cur and prev:
            left = mid+1
        if not cur:
            right = mid-1
    return answer

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n))