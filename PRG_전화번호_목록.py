import sys

def solution(phone_book):
    A = sorted(phone_book)
    for idx in range(len(A)-1):
        a = A[idx]
        b = A[idx+1]
        if len(a)<=len(b):
            if a==b[:len(a)]:
                return False
        else:
            if b==a[:len(b)]:
                return False
    return True

phone_book = ["119", "97674223", "1195524421"]
phone_book = ["123","456","789"]
phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))