# �Է� : n, 10���� ������ �տ� 0�� ���δ� (if��), ���� �ڸ��� ���� �ڸ��� ������ ����Ʈ?
# ��� : ����Ŭ�� ����, ���� ���� ���ƿ� ������ while ���� ����?
# ���̽� ���� �ʱ�ȭ... ����...

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