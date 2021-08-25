pos = {
    1:[0,3],
    2:[1,3],
    3:[2,3],
    4:[0,2],
    5:[1,2],
    6:[2,2],
    7:[0,1],
    8:[1,1],
    9:[2,1],
    0:[1,0]
}

def distance(x,y,a,b):
    return abs(x-a)+abs(y-b)

def solution(numbers, hand):
    answer = ''
    left_pos = [0,0]
    right_pos = [2,0]
    for x in numbers:
        # print(left_pos,right_pos,x)
        target_x = pos[x][0]
        target_y = pos[x][1]
        if x in [1,4,7]:
            left_pos = [target_x,target_y]
            answer+='L'
        elif x in [3,6,9]:
            right_pos = [target_x,target_y]
            answer+='R'
        else:
            d_left = distance(left_pos[0],left_pos[1],target_x,target_y)
            d_right = distance(right_pos[0],right_pos[1],target_x,target_y)
            # print(d_left,d_right)
            if d_left<d_right:
                left_pos = [target_x,target_y]
                answer+='L'
            elif d_left>d_right:
                right_pos = [target_x,target_y]
                answer+='R'
            else:
                if hand == 'left':
                    left_pos = [target_x,target_y]
                    answer+='L'
                else:
                    right_pos = [target_x,target_y]
                    answer+='R'


    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers,hand))