#2745
import sys

N, B = sys.stdin.readline().rstrip('\n').split()
B = int(B)
ans = 0
for idx,val in enumerate(N[::-1]):
    if ord(val)>=65:
        val = ord(val) - 65 + 10
    else:
        val = int(val)
    ans += val * pow(B,idx)
print(ans)
