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

# �����Ÿ� 1. ������ �ǹ�? / 2. 1�� �̻� return �Ϸ���? / 3. return�� �� ������ �Ǵ°ǰ�?