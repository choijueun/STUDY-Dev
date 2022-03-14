# Lv.1 정수 1부터 10,000까지 8이 몇 번 나오는가?
list_of_eight = []
for num in range(1,10000):
    list_of_eight += [n for n in str(num) if int(n) == 8]

print(len(list_of_eight))

print(str(list(range(1,10000))).count('8'))