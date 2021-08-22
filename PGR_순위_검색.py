#1:40

def find(A,x):
    left = 0
    right = len(A)-1
    if x<=A[0]:
        return 0
    if A[-1]<x:
        return -1
    while True:
        mid = (left+right)//2
        if A[mid]>=x and A[mid-1]<x:
            return mid
        if A[mid]>=x: 
            right = mid-1
        if A[mid]<x:
            left=mid+1

def solution(info, query):
    answer = []
    db = [[[[[] for _ in range(2)] for _ in range(2)] for _ in range(2)]for _ in range(3)]
    #개발언어 직군 경력 소울푸드
    for i in info:
        cur = i.split()
        idx = []
        if cur[0]=='cpp':
            idx.append(0)
        if cur[0]=='java':
            idx.append(1)
        if cur[0]=='python':
            idx.append(2)

        if cur[1]=='backend':
            idx.append(0)
        if cur[1]=='frontend':
            idx.append(1)

        if cur[2]=='junior':
            idx.append(0)
        if cur[2]=='senior':
            idx.append(1)

        if cur[3]=='chicken':
            idx.append(0)
        if cur[3]=='pizza':
            idx.append(1)
        # print(idx)
        db[idx[0]][idx[1]][idx[2]][idx[3]].append(int(cur[4]))\


    for a in [0,1,2]:
        for b in [0,1]:
            for c in [0,1]:
                for d in [0,1]:
                    db[a][b][c][d] = sorted(db[a][b][c][d])

    for q in query:
        cur = q.split('and')
        for x,y in enumerate(cur):
            cur[x]=y.strip()
        a,b = cur[-1].split()
        cur[-1]=a
        score = int(b)
        idx = [[] for _ in range(4)]
        if cur[0]=='-':
            idx[0]=[0,1,2]
        if cur[0]=='cpp':
            idx[0].append(0)
        if cur[0]=='java':
            idx[0].append(1)
        if cur[0]=='python':
            idx[0].append(2)

        if cur[1]=='-':
            idx[1]=[0,1]
        if cur[1]=='backend':
            idx[1].append(0)
        if cur[1]=='frontend':
            idx[1].append(1)

        if cur[2]=='-':
            idx[2]=[0,1]
        if cur[2]=='junior':
            idx[2].append(0)
        if cur[2]=='senior':
            idx[2].append(1)

        if cur[3]=='-':
            idx[3]=[0,1]
        if cur[3]=='chicken':
            idx[3].append(0)
        if cur[3]=='pizza':
            idx[3].append(1)
        sub = 0
        for a in idx[0]:
            for b in idx[1]:
                for c in idx[2]:
                    for d in idx[3]:
                        if db[a][b][c][d]:
                            x = find(db[a][b][c][d],score)
                            if x==-1:
                                continue
                            sub+=(len(db[a][b][c][d])-x)
        answer.append(sub)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))