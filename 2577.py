# �Է� : �ڿ��� a,b,c / �� �� m / ����Ʈ li
# list.count(i)

a = int(input())
b = int(input())
c = int(input())
m = a * b * c
m_str = str(m)

li = list(map(int,str(m)))
for i in range(10) :
    print(li.count(i))