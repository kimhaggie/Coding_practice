def check(a,b,start,end):
    # print(a,b,start,end)
    if start<=a and b<=end:
        # print(1)
        return True
    if start<=a and a<=end<=b:
        # print(2)
        return True
    if a<=start<=b and b<=end:
        # print(3)
        return True
    if a<=start<=b and a<=end<=b:
        # print(4)
        return True
    # print(0)
    return False

def solution(lines):
    answer = 0
    start = []
    end = []
    for l in lines:
        cur = l.split(' ')
        time = cur[1].split(':')
        # print(time)
        end_time = 60*60*int(time[0])+60*int(time[1])+float(time[2])
        T = float(cur[2].split('s')[0])
        start_time = round(end_time-T+0.001,3)
        start.append(start_time)
        end.append(end_time)
    # print(start)
    # print(end)
    for time in start:
        # import pdb;pdb.set_trace()
        # print(time)
        num=0
        a=round(time-1+0.001,3)
        b=time
        for s,e in zip(start,end):
            if check(a,b,s,e):
                num+=1
        if answer<num:
            answer=num
    return answer

lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]

print(solution(lines))