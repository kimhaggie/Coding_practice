#11723
import sys

M = int(sys.stdin.readline().rstrip('\n'))
S = 0
for _ in range(M):
    command = sys.stdin.readline().rstrip('\n')
    if command == 'all':
        S = -1
    elif command == 'empty':
        S = 0
    else:
        command = command.split(' ')
        command[1] = int(command[1])
        if command[0] == 'add':
            S = S|(1<<command[1])
        elif command[0] == 'remove':
            S = S&~(1<<command[1])
        elif command[0] == 'check':
            if S&(1<<command[1])>0:
                sys.stdout.write('1\n')
            else:
                sys.stdout.write('0\n')
        elif command[0] == 'toggle':
            S = S^(1<<command[1])