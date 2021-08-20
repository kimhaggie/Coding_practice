def solution(n, k, cmd):
    answer = ''
    last = n-1
    table = [[i-1,i+1]for i in range(n)]
    delete = []
    for c in cmd:
        if c[0]=='D':
            x = int(c[2:])
            for step in range(x):
                k=table[k][1]
        if c[0]=='U':
            x = int(c[2:])
            for step in range(x):
                k=table[k][0]
        if c=='C':
            if 0<=table[k][0]<n:
                table[table[k][0]][1]=table[k][1]
            if 0<=table[k][1]<n:
                table[table[k][1]][0]=table[k][0]
            delete.append(k)
            if k==last:
                last = table[k][0]
                k=table[k][0]
            else:
                k=table[k][1]
        if c=='Z':
            target = delete.pop()
            if target > last:
                last = target
            if 0<=table[target][0]<n:
                table[table[target][0]][1] = target
            if 0<=table[target][1]<n:
                table[table[target][1]][0] = target
    delete = set(delete)
    for idx in range(n):
        if idx in delete:
            answer+='X'
        else:
            answer+='O'
    return answer

n=8
k=2
cmd=	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n,k,cmd))