import sys

def solution(num): 
    num = list(map(str, num)) 
    num.sort(key = lambda x : x*3, reverse = True) 
    return str(int(''.join(num)))

numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]
print(solution(numbers))