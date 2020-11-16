li = []
li2 = []

for i in range(10):
    n = int(input())
    li.append(n)

for i in range(len(li)):
    li2.append(li[i] % 42)
    
li2_set = set(li2)
print(len(li2_set))