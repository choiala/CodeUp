s = input()

def solution(s) : # 5�� �� 3 ��ȯ, 4�� �� 2,3 ��ȯ
  s_length = len(s)
  s_id = 0
  s_id2 = 0
  if s_length % 2 == 1 :
    s_id = s_length // 2
    return s[s_id]
  else :
#    print(s_length)
#    print(s_length // 2)
    s_id = (s_length // 2) - 1 # �� - 1 -> �ε����� 0���� �����ϴϱ�!!!
    s_id2 = s_id +1
    return s[s_id] + s[s_id2]

print(solution(s))


    
