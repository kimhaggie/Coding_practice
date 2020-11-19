#1212
import sys

octa = sys.stdin.readline().rstrip('\n')
ans = ''
for idx,val in enumerate(octa):
    if idx==0:
        val = int(val)
        x=''
        if val==0:
            ans+='0'
        while val!=0:
            x+=str(val%2)
            val=val//2
        ans+=x[::-1]
    else:
        val = int(val)
        x = ''
        while val!=0:
            x+=str(val%2)
            val=val//2
        while len(x)!=3:
            x+='0'
        ans+=x[::-1]
print(ans)

