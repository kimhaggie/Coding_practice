#15분

def solution(new_id):
    answer = ''
    new_id = list(new_id)
    #1
    for i,v in enumerate(new_id):
        if ord('A')<=ord(v)<=ord('Z'):
            new_id[i] = chr(ord(v)-(ord('A')-ord('a')))
    #2
    tmp = []
    for i,v in enumerate(new_id):
        if ord('a')<=ord(v)<=ord('z'):
            tmp.append(v)
            continue
        if ord('0')<=ord(v)<=ord('9'):
            tmp.append(v)
            continue
        if v == '-' or v == '_' or v=='.':
            tmp.append(v)
            continue
    new_id = tmp
    #3
    tmp = []
    for i,v in enumerate(new_id):
        if not tmp:
            tmp.append(v)
        else:
            if tmp[-1] == '.' and v=='.':
                continue
            else:
                tmp.append(v)
    new_id=tmp
    #4
    tmp = []
    for i,v in enumerate(new_id):
        if not tmp:
            if v=='.':
                continue
            else:
                tmp.append(v)
        else:
            tmp.append(v)
    if tmp:
        while tmp[-1] == '.':
            tmp.pop()
    new_id = tmp
    #5
    if not new_id:
        new_id = ['a']
    #6
    if len(new_id)>=16:
        new_id = new_id[:15]
    if new_id:
        while new_id[-1] == '.':
            new_id.pop()
    #7
    if len(new_id)<=2:
        while len(new_id)<3:
            new_id.append(new_id[-1])
    return ''.join(new_id)

new_id = 	"=.="
print(solution(new_id))