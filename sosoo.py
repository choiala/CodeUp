n = int(input())
list_n = list(map(int, input().split()))


# 1�� �ڱ� �ڽ����θ� ��������
def sosoo(a) :
  cnt = 0
  for i in range(len(list_n)) :
    for j in range(2, len(list_n)) :
      if a[i] % j != 0 :
        return False
      else :
        cnt =+ 1
        return cnt

print(sosoo(list_n))
