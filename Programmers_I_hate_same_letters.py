arr = list(map(int,input().split()))

def solution(arr):
  answer = []
  answer.append(arr[0]) # 0번 인덱스는 중복되지 않음, 무조건 추가 
  for i in range(1, len(arr)) :
    if arr[i] != arr[i-1] : # answer.append(arr[0]) 없으면 3부터
      answer.append(arr[i])
  return answer

print(solution(arr))