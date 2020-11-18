n = int(input()) # 왜 안될까
cnt = 0

for i in range(1, n+1) :
  if i < 100 :
    cnt =+ 1
  else :
    x = list(map(int, str(i)))
  #    print(x)
    if x[0] - x[1] == x[1] - x[2] :
        cnt =+ 1
      
print(cnt)