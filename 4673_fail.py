# 10000�� ����Ʈ ���� �� �����ѹ� ����


li_num = list(range(1,10001))
li_new = []

# �� �ڸ� �̻��� �� ó��
def d(a) :  
  global new
  if a < 100 :
    ten = a // 10
    one = a % 10
    new = a + ten + one 
  elif a <= 100 and a < 1000 :
    hun = a // 100
    ten = a - (100 * hun) // 10
    one = a - (100 * hun + 10 * ten )
    new = hun + ten + one 
  elif a <= 1000 and a <= 10000 :
    tho = a // 10000
    hun = a - (1000 * tho) // 100
    ten = a - (100 * hun) // 10
    one = a - (1000 * tho + 100 * hun + 10 * ten )
    new = tho + hun + ten + one 
  return new

for i in li_num :
  sn = d(i)
  li_new.append(sn)
  if i not in li_new :
    print(i,'\n')
