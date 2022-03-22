# 제곱 사이클
'''
def squareOnce(number):
    numList = list(str(number))
    
    sum = 0
    for num in numList:
        sum += int(num)**2
    
    return sum
   
def squareCycle(number):
    print('='*5,'시작','='*5)
    cnt = 1
    num = squareOnce(number)
    while num != number:
        cnt += 1
        if cnt == 100:
            print("100개 이상")
            return
        num = squareOnce(num)
    print(cnt)
    
   
squareCycle(4)
squareCycle(2)

'''
input_num = int(input('정수를 입력하세요: '))
num_list = list(str(input_num))

for i in range(1,101):
    sum = 0
    for num in num_list:
        sum += int(num)**2
    
    num_list = list(str(sum))
    
    if sum == input_num:
        print(i)
        break
    elif i == 100:
        print('100개 이상')