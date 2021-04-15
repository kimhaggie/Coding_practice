import sys

def solution(numbers, target):
    answer = 0
    for i in range(1<<len(numbers)):
        cur = 0
        for j in range(len(numbers)):
            if i&(1<<j):
                cur+=numbers[j]
            else:
                cur-=numbers[j]
        if cur==target:
            print(bin(i),cur)
            answer+=1
    return answer

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))