def cycle(start,food_times,k):
    total_len = 0 #남은 음식 수
    for food in food_times:
        if food>0:
            total_len+=1        
    x = k//total_len #바퀴수
    y = k%total_len #나머지
    new_k = 0 #남은 시간
    for idx, val in enumerate(food_times):
        if val>0:
            food_times[idx]-=x
        if food_times[idx]<0:
            new_k-=food_times[idx]
            food_times[idx]=0
    # print(food_times,start+y)
    new_start = start
    # print(new_k)
    # while food_times[new_start]<=0:
        # print(new_start)
        # new_start = (new_start+1)%len(food_times)
    # print(new_start)
    while y>0:
        if food_times[new_start]>0:
            food_times[new_start]-=1
            y-=1
        new_start = (new_start+1)%len(food_times)
    while food_times[new_start]<=0:
        new_start = (new_start+1)%len(food_times)
    return new_start, food_times, new_k

def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    new_start = 0
    new_k = k
    while True:
        new_start, food_times, new_k = cycle(new_start,food_times,new_k)
        if new_k == 0:
            return new_start+1

food_times = [3,1,2]
k = 6
print(solution(food_times, k))