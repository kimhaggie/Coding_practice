#10430
import sys

a,b,c = map(int,sys.stdin.readline().rstrip('\n').split(' '))
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)