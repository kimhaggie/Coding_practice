#이분탐색
def check(n,times,mid):
    num = 0
    for x in times:
        num+=mid//x
    return num >= n

def solution(n, times):
    answer = 0

    left = 1
    right = n*min(times)
    mid = (left+right)//2

    while True:
        # print(left,mid,right)
        # if left == 28:
        #     return 0
        cur = check(n,times,mid)
        next_ = check(n,times,mid-1)
        # print(cur,next_)
        if cur and not next_:
            return mid
        if not cur:
            left=mid+1
            mid = (left+right)//2
        else:
            right=mid-1
            mid = (left+right)//2

n = 6
times = [7,10]
print(solution(n,times))