# Lv2. 숫자 정렬
def sortOdd(inputList):
    try:
        chk = 0
        sortList1 = []  #홀수
        sortList2 = []  #짝수
        for num in inputList:
            if num%2 == 1:
                sortList1.append(num)
                chk += 1
            else:
                sortList2.append(num)
                chk -= 1
                
        if chk != 0:
            print("홀짝의 수가 같지 않습니다.")
            return
        
        sortList1.sort()
        sortList2.sort(reverse=True)
        
        result=[]
        for i in range(len(sortList1)):
            result.append(sortList1[i])
            result.append(sortList2[i])
        
        return result
    
    except:
        print('오류발생')
        
print(sortOdd([4,1,3,2,6,5]))


#풀이
inList = [4,1,3,2,6,5,8,11]

# odd = list(map(lambda x: x%2 == 1, inList))
# even = list(map(lambda x: x%2 == 0, inList))
odd = [int(num) for num in inList if num%2 == 1]
even = [int(num) for num in inList if num%2 == 0]

result = []
for i in range(len(odd)):
    result.append(sorted(odd)[i])
    result.append(sorted(even, reverse=True)[i])

print(result)