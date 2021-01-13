#2529
import sys

def func(a,start,m,ans,op):
    max_val = -1
    min_val = float('inf')
    if m == 0:
        return ''.join(map(str,ans))
    else:
        cur_op = op[len(op)-m]
        for idx in range(start,len(a)):
            if len(ans)!=0:
                if cur_op == '<' and ans[-1] >= a[idx]:
                    continue
                if cur_op == '>' and ans[-1] <= a[idx]:
                    continue
            ans.append(a[idx])
            b = a.copy()
            del b[idx]
            sub_ans = func(b,0,m-1,ans,op)
            if type(sub_ans) is str: #마지막 깊이에서 리턴되었을 때
                if min_val == float('inf') or int(sub_ans) < int(min_val):
                    min_val = sub_ans
                if int(max_val) < int(sub_ans):
                    max_val = sub_ans
            else: #[min_val,max_val]을 리턴했을 때
                if sub_ans[0] == float('inf'):
                    pass
                elif min_val == float('inf') or int(sub_ans[0]) < int(min_val):
                    min_val = sub_ans[0]
                if int(max_val) < int(sub_ans[1]):
                    max_val = sub_ans[1]
            ans.pop()
        return [min_val,max_val]

k = int(sys.stdin.readline().rstrip('\n'))
op = sys.stdin.readline().rstrip('\n').split(' ')
if '' in op:
    op.remove('')
a = list(range(10))
ans = []
m,M= func(a,0,k+1,ans,op)
print(M)
print(m)