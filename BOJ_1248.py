#1248
import sys

def func(a,start,m,ans,S):
    if m == 0:
        print(' '.join(map(str,ans)))
        return True
    else:
        for idx in range(start,len(a)):
            cur_val = a[idx]
            cur_idx = len(ans) #[a,b] -> 2
            poss = True
            ans.append(cur_val)
            cal = sum(ans)
            for i in range(0,cur_idx+1):
                if i>=1:
                    cal -= ans[i-1]
                if S[i][cur_idx]=='+' and cal <= 0:
                    poss=False
                    break
                if S[i][cur_idx]=='-' and cal >= 0:
                    poss=False
                    break
                if S[i][cur_idx]=='0' and cal != 0:
                    poss=False
                    break
            if poss:
                result = func(a,0,m-1,ans,S)
                if result:
                    return True
            ans.pop()

N = int(sys.stdin.readline().rstrip('\n'))
sign = list(sys.stdin.readline().rstrip('\n'))
S = [[None for _ in range(N)] for _ in range(N)]
step = 0
for i in range(N):
    for j in range(N):
        if i<=j:
            S[i][j] = sign[step]
            step += 1
a = list(range(-10,11))
a.reverse()
ans = []
func(a,0,N,ans,S)