def solution(n, t, m, timetable):
    answer = ''
    time = []
    for val in timetable:
        val = val.split(':')
        time.append(60*int(val[0])+int(val[1]))
    time = sorted(time,reverse=True)
    bus = []
    #540
    start = 540
    bus= []
    crew = [[] for _ in range(n)]
    for i in range(n):
        bus.append(start+i*t)
        tmp = []
        while True:
            if not time:
                break
            cur = time[-1]
            if cur <= start+(i)*t and len(tmp)<m:
                tmp.append(cur)
                time.pop()
            else:
                break
        crew[i]=tmp
    if len(crew[-1])==m:
        answer = crew[-1][-1]-1
    else:
        answer = bus[-1]
    a = answer//60
    b = answer%60
    if a<10:
        a = '0'+str(a)
    else:
        a = str(a)
    if b<10:
        b = '0'+str(b)
    else:
        b = str(b)
    answer = str(a)+':'+str(b)
    return answer

n=2
t=1
m=4
timetable = ["08:00", "08:01", "08:02", "08:03"]
n=2
t=10
m=2
timetable = ["09:10", "09:09", "08:00"]
# n=1
# t=1
# m=5
# timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
# n=10
# t=60
# m=45
# timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
# n=2
# t=10
# m=3
# timetable = ["09:05","09:09","09:13"]
print(solution(n,t,m,timetable))