arr = list(map(int,input().split()))

def solution(arr):
  answer = []
  answer.append(arr[0]) # 0�� �ε����� �ߺ����� ����, ������ �߰� 
  for i in range(1, len(arr)) :
    if arr[i] != arr[i-1] : # answer.append(arr[0]) ������ 3����
      answer.append(arr[i])
  return answer

print(solution(arr))