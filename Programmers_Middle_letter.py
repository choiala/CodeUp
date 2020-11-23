s = input()

def solution(s) : # 5일 땐 3 반환, 4일 땐 2,3 반환
  s_length = len(s)
  s_id = 0
  s_id2 = 0
  if s_length % 2 == 1 :
    s_id = s_length // 2
    return s[s_id]
  else :
#    print(s_length)
#    print(s_length // 2)
    s_id = (s_length // 2) - 1 # 왜 - 1 -> 인덱스라서 0부터 시작하니까!!!
    s_id2 = s_id +1
    return s[s_id] + s[s_id2]

print(solution(s))


    
