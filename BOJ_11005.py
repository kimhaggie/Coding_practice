#11005
import sys

N,B = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
ans = ''
if N == 0:
    ans ='0'
while N!=0:
    x = N % B
    if x<10:
        ans += str(x)
    else:
        ans += chr(x-10+65)
    N = N // B
print(ans[::-1])