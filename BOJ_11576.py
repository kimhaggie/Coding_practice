#11576
import sys

A,B = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
n = int(sys.stdin.readline().rstrip('\n'))
L = list(sys.stdin.readline().rstrip('\n').split(' '))

ans = 0
for idx,val in enumerate(L[::-1]):
    val = int(val)
    ans +=  val * pow(A,idx)
result = []
if ans == 0:
    result.append(0)
else:
    while ans!=0:
        x = ans % B
        result.append(x)
        ans = ans // B
print(' '.join(map(str,result[::-1])))