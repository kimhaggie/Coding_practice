#14391
import sys

def sum_col(i,j,h,S):
    ans = ''
    for idx in range(i,i+h):
        ans+=S[idx][j]
    return ans

def func(i, j, S, visit, sub_ans, remain_num, N, M):
    if remain_num == 0:
        return sub_ans
    ans = 0
    #가로
    for w in range(1,M-j+1):
        if j+w == M:#마지막일 때
            flag = True
            for c in range(j,M):
                if visit[i][c]:
                    flag = False
                    break
            if not flag:
                break
            sub_ans += int(''.join(S[i][j:]))
            for x in range(j,M):
                visit[i][x] = True
            start_i = 0
            start_j = 0
            for b in range(M):
                for a in range(N):
                    if not visit[a][b]:
                        start_i = a
                        start_j = b
                        break
                if start_i!=0 or start_j!=0:
                    break
            result = func(start_i,start_j,S,visit,sub_ans,remain_num-w,N,M) 
            if ans < result:
                ans = result
            sub_ans -= int(''.join(S[i][j:]))
            for x in range(j,M):
                visit[i][x] = False
        else:
            flag = True
            for c in range(j,j+w):
                if visit[i][c]:
                    flag = False
                    break
            if not flag:
                break
            sub_ans += int(''.join(S[i][j:j+w]))
            for x in range(j,j+w):
                visit[i][x] = True
            start_i = 0
            start_j = 0
            for b in range(M):
                for a in range(N):
                    if not visit[a][b]:
                        start_i = a
                        start_j = b
                        break
                if start_i!=0 or start_j!=0:
                    break
            result = func(start_i,start_j,S,visit,sub_ans,remain_num-w,N,M) 
            if ans < result:
                ans = result
            sub_ans -= int(''.join(S[i][j:j+w]))
            for x in range(j,j+w):
                visit[i][x] = False
    #세로
    for h in range(2,N-i+1):
        if i+h == N:#마지막일 때
            flag = True
            for c in range(i,N):
                if visit[c][j]:
                    flag = False
                    break
            if not flag:
                break
            sub_ans += int(sum_col(i,j,h,S))
            for y in range(i,N):
                visit[y][j] = True
            start_i = 0
            start_j = 0
            for b in range(M):
                for a in range(N):
                    if not visit[a][b]:
                        start_i = a
                        start_j = b
                        break
                if start_i!=0 or start_j!=0:
                    break
            result = func(start_i,start_j,S,visit,sub_ans,remain_num-h,N,M) 
            if ans < result:
                ans = result
            sub_ans -= int(sum_col(i,j,h,S))
            for y in range(i,N):
                visit[y][j] = False
        else:
            flag = True
            for c in range(i,i+h):
                if visit[c][j]:
                    flag = False
                    break
            if not flag:
                break
            sub_ans += int(sum_col(i,j,h,S))
            for y in range(i,i+h):
                visit[y][j] = True
            start_i = 0
            start_j = 0
            for b in range(M):
                for a in range(N):
                    if not visit[a][b]:
                        start_i = a
                        start_j = b
                        break
                if start_i!=0 or start_j!=0:
                    break
            result = func(start_i,start_j,S,visit,sub_ans,remain_num-h,N,M) 
            if ans < result:
                ans = result
            sub_ans -= int(sum_col(i,j,h,S))
            for y in range(i,i+h):
                visit[y][j] = False

    return ans

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
S = []
for _ in range(N):
    S.append(list(sys.stdin.readline().rstrip('\n')))
visit = [[False for _ in range(M)] for _ in range(N)]
print(func(0,0,S,visit,0,N*M,N,M))