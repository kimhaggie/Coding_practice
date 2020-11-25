#11653
num = int(input())
i = 2
while num!=1:
    if num%i == 0:
        num = num/i
        print(i)
    else:
        i += 1