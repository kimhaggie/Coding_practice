#10819
import sys

def cal(a):
    A = 0
    for i in range(len(a)-1):
        A+=abs(a[i]-a[i+1])
    return A

def func(a,m):
    if m==1:
        ans.append(a[0])
        ans_n.append(cal(ans))
        ans.pop()
    for idx,val in enumerate(a):
        ans.append(a[idx])
        b = a.copy()
        b.remove(val)
        func(b,m-1)
        ans.pop()

n = int(sys.stdin.readline().rstrip('\n'))
a= list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
ans = []
ans_n = []
func(a,len(a))
print(max(ans_n))