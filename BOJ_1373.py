#1373
import sys

binary = sys.stdin.readline().rstrip('\n')
n = len(binary)
ans = ''
for i in range(0,n,3):
    if n-i-3<=0:
        x = binary[0:n-i]
        dec = 0
        for idx,val in enumerate(x[::-1]):
            dec += int(val)*pow(2,idx)
        ans+=str(dec)
    else:
        x = binary[n-i-3:n-i]
        dec = 0
        for idx,val in enumerate(x[::-1]):
            dec += int(val)*pow(2,idx)
        ans+=str(dec)
print(ans[::-1])
