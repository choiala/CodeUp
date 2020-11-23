#  b % 7 == 0 일 때, Fri
#  b % 7 == 1 일 때, Sat
#  b % 7 == 2 일 때, Sun
#  b % 7 == 3 일 때, Mon
#  b % 7 == 4 일 때, Tue
#  b % 7 == 5 일 때, Wed
#  b % 7 == 6 일 때, Thu

# 윤년이라는 단서는 어떻게 써먹어야?
# 매달 1일이 금요일인게 아님!!!!!!!!!

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