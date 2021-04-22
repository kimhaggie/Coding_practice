import sys

def clock(X):
    order = [6,3,0,7,4,1,8,5,2]
    return [X[i] for i in order]

def clock_U(front, up, right, down, left):
    order = [6,3,0,7,4,1,8,5,2]
    new_front = [front[i] for i in order]
    new_up = [i for i in up]
    new_up[:3] = left[:3]
    new_right = [i for i in right]
    new_right[:3] = up[:3]
    new_down = [i for i in down]
    new_down[:3] = right[:3]
    new_left = [i for i in left]
    new_left[:3] = down[:3]
    return [new_front,new_up,new_right,new_down,new_left]

def reverse_U(front, up, right, down, left):
    order = [2,5,8,1,4,7,0,3,6]
    new_front = [front[i] for i in order]
    new_up = [i for i in up]
    new_up[:3] = right[:3]
    new_right = [i for i in right]
    new_right[:3] = down[:3]
    new_down = [i for i in down]
    new_down[:3] = left[:3]
    new_left = [i for i in left]
    new_left[:3] = up[:3]
    return [new_front,new_up,new_right,new_down,new_left]

t = int(sys.stdin.readline().rstrip('\n'))
color = ['w','y','r','o','g','b']
for _ in range(t):
    #0위 1아래 2앞 3뒤 4왼 5오른
    cube = [[color[i] for _ in range(9)]for i in range(6)]
    n = int(sys.stdin.readline().rstrip('\n'))
    cmd = sys.stdin.readline().rstrip('\n').split()
    for x in cmd:
        if x == 'U+':
            cube[0],cube[3],cube[5],cube[2],cube[4] = clock_U(cube[0],cube[3],cube[5],cube[2],cube[4])
        if x == 'U-':
            cube[0],cube[3],cube[5],cube[2],cube[4] = reverse_U(cube[0],cube[3],cube[5],cube[2],cube[4])
        if x == 'D+':
            cube[1],cube[3],cube[4],cube[2],cube[5] = clock_U(cube[1],clock(clock(cube[3])),clock(clock(cube[4])),clock(clock(cube[2])),clock(clock(cube[5])))
            cube[3] = clock(clock(cube[3]))
            cube[4] = clock(clock(cube[4]))
            cube[2] = clock(clock(cube[2]))
            cube[5] = clock(clock(cube[5]))
        if x == 'D-':
            cube[1],cube[3],cube[4],cube[2],cube[5] = reverse_U(cube[1],clock(clock(cube[3])),clock(clock(cube[4])),clock(clock(cube[2])),clock(clock(cube[5])))
            cube[3] = clock(clock(cube[3]))
            cube[4] = clock(clock(cube[4]))
            cube[2] = clock(clock(cube[2]))
            cube[5] = clock(clock(cube[5]))
        if x == 'F+':
            cube[2],cube[0],cube[5],cube[1],cube[4] = clock_U(cube[2],clock(clock(cube[0])),clock(cube[5]),clock(clock(cube[1])),clock(clock(clock(cube[4]))))
            cube[0] = clock(clock(cube[0]))
            cube[5] = clock(clock(clock(cube[5])))
            cube[1] = clock(clock(cube[1]))
            cube[4] = clock(cube[4])
        if x == 'F-':
            cube[2],cube[0],cube[5],cube[1],cube[4] = reverse_U(cube[2],clock(clock(cube[0])),clock(cube[5]),clock(clock(cube[1])),clock(clock(clock(cube[4]))))
            cube[0] = clock(clock(cube[0]))
            cube[5] = clock(clock(clock(cube[5])))
            cube[1] = clock(clock(cube[1]))
            cube[4] = clock(cube[4])
        if x == 'B+': 
            cube[3],cube[0],cube[4],cube[1],cube[5] = clock_U(cube[3],cube[0],clock(cube[4]),cube[1],clock(clock(clock(cube[5]))))
            cube[4] = clock(clock(clock(cube[4])))
            cube[5] = clock(cube[5])
        if x == 'B-':
            cube[3],cube[0],cube[4],cube[1],cube[5] = reverse_U(cube[3],cube[0],clock(cube[4]),cube[1],clock(clock(clock(cube[5]))))
            cube[4] = clock(clock(clock(cube[4])))
            cube[5] = clock(cube[5])
        if x == 'L+':
            cube[4],cube[0],cube[2],cube[1],cube[3] = clock_U(cube[4],clock(cube[0]),clock(cube[2]),clock(clock(clock(cube[1]))),clock(clock(clock(cube[3]))))
            cube[0] = clock(clock(clock(cube[0])))
            cube[2] = clock(clock(clock(cube[2])))
            cube[1] = clock(cube[1])
            cube[3] = clock(cube[3])
        if x == 'L-':
            cube[4],cube[0],cube[2],cube[1],cube[3] = reverse_U(cube[4],clock(cube[0]),clock(cube[2]),clock(clock(clock(cube[1]))),clock(clock(clock(cube[3]))))
            cube[0] = clock(clock(clock(cube[0])))
            cube[2] = clock(clock(clock(cube[2])))
            cube[1] = clock(cube[1])
            cube[3] = clock(cube[3])
        if x == 'R+':
            cube[5],cube[0],cube[3],cube[1],cube[2] = clock_U(cube[5],clock(clock(clock(cube[0]))),clock(cube[3]),clock(cube[1]),clock(clock(clock(cube[2]))))
            cube[0] = clock(cube[0])
            cube[3] = clock(clock(clock(cube[3])))
            cube[1] = clock(clock(clock(cube[1])))
            cube[2] = clock(cube[2])
        if x == 'R-':
            cube[5],cube[0],cube[3],cube[1],cube[2] = reverse_U(cube[5],clock(clock(clock(cube[0]))),clock(cube[3]),clock(cube[1]),clock(clock(clock(cube[2]))))
            cube[0] = clock(cube[0])
            cube[3] = clock(clock(clock(cube[3])))
            cube[1] = clock(clock(clock(cube[1])))
            cube[2] = clock(cube[2])
    x = cube[0]
    for idx,val in enumerate(x):
        print(val,end='')
        if idx in [2,5,8]:
            print()