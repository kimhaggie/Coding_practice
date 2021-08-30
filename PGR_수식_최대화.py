from itertools import permutations

def calculate(x):
    stack = []
    for val in x:
        # print(stack)
        if val in ['+','-','*']:
            a = stack.pop()
            b = stack.pop()
            if val == '+':
                c=a+b
            elif val == '-':
                c=b-a
            else:
                c=a*b
            stack.append(c)
        else:
            stack.append(val)
    return stack[0]

def solution(expression):
    answer = 0
    exp = []
    tmp = ''
    for idx,val in enumerate(expression):
        if val in ['+','-','*']:
            exp.append(int(tmp))
            exp.append(val)
            tmp = ''
        else:
            tmp+=val
    exp.append(int(tmp))
    for case in permutations([1,2,3],3):
        order = dict()
        for idx,val in enumerate(case):
            if idx==0:
                order['+'] = val
            elif idx==1:
                order['-'] = val
            else:
                order['*'] = val
        # print(order)
        stack = []
        result = []
        for val in exp:
            # print(stack)
            if val in ['+','-','*']:
                while True:
                    if not stack:
                        stack.append(val)
                        break
                    top = stack[-1]
                    if order[top]>=order[val]:
                        result.append(top)
                        stack.pop()
                        continue
                    else:
                        stack.append(val)
                        break
            else:
                result.append(val)
        while stack:
            result.append(stack.pop())
        # print(result)
        tmp = abs(calculate(result))
        if answer < tmp:
            answer = tmp
    # print(exp)
    return answer

expression = "100-200*300-500+20"
print(solution(expression))