# 입력 : n, 10보다 작으면 앞에 0을 붙인다 (if문), 일의 자리와 십의 자리를 저장할 리스트?
# 출력 : 사이클의 길이, 원래 수로 돌아올 때까지 while 문을 돌려?
# 파이썬 변수 초기화... 뭘까...

n = int(input())
new = n
cnt = 1

while True :
    one = int(new) % 10
    ten = int(new) // 10
    new_new = one + ten 
    new = str(one) + str(new_new % 10)
    
    if int(new) == n :
        break
    else : 
        cnt += 1

print(cnt)