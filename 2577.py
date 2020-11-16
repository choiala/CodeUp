# 입력 : 자연수 a,b,c / 곱 값 m / 리스트 li
# list.count(i)

a = int(input())
b = int(input())
c = int(input())
m = a * b * c
m_str = str(m)

li = list(map(int,str(m)))
for i in range(10) :
    print(li.count(i))