participant = list(map(str,input().split()))
completion = list(map(str,input().split()))

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

print(solution(participant, completion))

# 질문거리 1. 정렬의 의미? / 2. 1개 이상 return 하려면? / 3. return이 두 개여도 되는건가?