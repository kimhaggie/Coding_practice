#10:40

def change(x):
    h,m,s = map(int,x.split(':'))
    return h*60*60+m*60+s
def reverse(x):
    h = (x//60)//60
    x -= h*60*60
    m = x//60
    x -= m*60
    s = x
    h=str(h)
    m=str(m)
    s=str(s)
    if len(h)==1:
        h = '0'+h
    if len(m)==1:
        m = '0'+m
    if len(s)==1:
        s = '0'+s
    return ':'.join(map(str,[h,m,s]))

def solution(play_time, adv_time, logs):
    answer = ''
    play_time = change(play_time)
    adv_time = change(adv_time)
    time_table = [0 for _ in range(100*60*60)]
    for log in logs:
        start,end = log.split('-')
        start = change(start)
        end = change(end)
        for t in range(start,end):
            time_table[t]+=1
    
    total_time = sum(time_table[:adv_time])
    answer_time = sum(time_table[:adv_time])
    answer = 0
    start = 0
    end = adv_time
    while end<=play_time:
        total_time-=time_table[start]
        total_time+=time_table[end]
        start+=1
        end+=1
        if answer_time<total_time:
            answer = start
            answer_time = total_time
    return (reverse(answer))

# import heapq as heap

# def solution(play_time, adv_time, logs):
#     answer = ''
#     play_time = change(play_time)
#     adv_time = change(adv_time)
#     my_logs = []
#     for log in logs:
#         start,end = log.split('-')
#         start = change(start)
#         end = change(end)
#         heap.heappush(my_logs,[end,start])
#     sorted_time = sorted(my_logs)

#     tmp = my_logs.copy()
#     answer = 0
#     answer_time = 0
#     while True:
#         if not tmp:
#             break
#         end,start = heap.heappop(tmp)
#         if start<adv_time:
#             answer_time += min(adv_time-start,end-start)
#         else:
#             break
#     print(reverse(answer_time))
#     for end,_ in sorted_time:
#         start = end-adv_time
#         tmp = my_logs.copy()
#         while True:
#             if not tmp:
#                 break
#             cur_end,cur_start = heap.heappop(tmp)
#             if cur_end <= start:
#                 continue
            
#         pass

#     return answer

play_time = "02:03:55"	
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

play_time = "99:59:59"	
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]

play_time = "50:00:00"	
adv_time = "50:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

play_time = "50:00:00"	
adv_time = "10:00:00"
logs = ["00:00:00-08:21:49", "01:00:00-10:00:00", "09:59:59-42:51:45"]
print(solution(play_time,adv_time,logs))