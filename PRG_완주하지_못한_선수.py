import sys

def solution(participant, completion):
    A = sorted(participant)
    B = sorted(completion)
    idx = 0
    while idx<len(B):
        if A[idx]!=B[idx]:
            return A[idx]
        idx += 1
    return A[-1]

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]
# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))