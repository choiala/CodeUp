n = int(input())
sc = list(map(int, input().split()))
M = max(sc)
new_sc = []

for i in range(n) :
    tmp_sc = (sc[i] / M * 100)
    new_sc.append(tmp_sc)

print(round(sum(new_sc) / len(new_sc),2))