c = int(input()) # 테스트 케이스 갯수
for i in range(c) :
    student = list(map(int, input().split()))
    avg_student = sum(student[1:]) / student[0]
    cnt = 0
    for j in student[1:] :
        if j > avg_student :
            cnt =+ 1 
    print(round(cnt / student[0] * 100,3 ), "%")