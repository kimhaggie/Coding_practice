def valid(p):
    if p == '':
        return True
    stack = []
    for val in p:
        if val == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            else:
                if stack[-1]!='(':
                    return False
                else:
                    stack.pop()
    if stack:
        return False
    return True

def go(p):
    if p=='':
        return ''
    a=0
    b=0
    u=''
    v=''
    for idx, val in enumerate(p):
        if val=='(':
            a+=1
        if val==')':
            b+=1
        if a>0 and a==b:
            u = p[:idx+1]
            v = p[idx+1:]
            break
    flag = valid(u)
    if flag:
        return u+go(v)
    else:
        sub = '('+go(v)+')'
        reverse_u = ''
        for val in u[1:-1]:
            if val == '(':
                reverse_u+=')'
            else:
                reverse_u+='('
        sub+=reverse_u
        return sub

def solution(p):
    return go(p)

p = "(()())()"
p = ')('
p = "()))((()"	
p = ''
p = '()'
print(p[1:-1][::-1])
print(solution(p))