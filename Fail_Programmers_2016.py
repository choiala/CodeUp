#  b % 7 == 0 �� ��, Fri
#  b % 7 == 1 �� ��, Sat
#  b % 7 == 2 �� ��, Sun
#  b % 7 == 3 �� ��, Mon
#  b % 7 == 4 �� ��, Tue
#  b % 7 == 5 �� ��, Wed
#  b % 7 == 6 �� ��, Thu

# �����̶�� �ܼ��� ��� ��Ծ��?
# �Ŵ� 1���� �ݿ����ΰ� �ƴ�!!!!!!!!!

a, b = input().split()
b = int()

def solution(b) :
  if b % 7 == 0 :
    return "FRI"
  elif b % 7 == 1 :
    return "SAT"
  elif b % 7 == 2 :
    return "SUN"
  elif b % 7 == 3 :
    return "MON"
  elif b % 7 == 4 :
    return "Tue"
  elif b % 7 == 5 :
    return "WED"
  elif b % 7 == 6 :
    return "THU"

print(solution(b)