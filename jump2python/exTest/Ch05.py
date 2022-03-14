https://wikidocs.net/12769#05

#Q1
class Calculator:                       #부모클래스: 더하기
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val
   
class UpgradeCalculator(Calculator):    #자식클래스: 빼기
    def minus(self, val):
        self.value -= val

cal1 = UpgradeCalculator()               #자식클래스 인스턴스 생성
cal1.add(10)
cal1.minus(7)

print(cal1.value)

#Q2
class MaxLimitCalculator(Calculator):   #자식클래스: 최대100
    def add(self, val):
        self.value += val
        if self.value > 100 :
            self.value = 100

cal2 = MaxLimitCalculator()             #자식클래스 인스턴스 생성
cal2.add(50)
cal2.add(60)
print(cal2.value)

#Q3
q3_1 = all([1,2,abs(-3)-3])
print(q3_1)                 #예상: False
print(chr(ord('a')) == 'a') #예상: True

#Q4
q4_list = list(filter(lambda x: x>0, [1, -2, 3, -5, 8, -3]))
print(q4_list)

#Q5
print(int(0xea))
#int('0xea', 16)

#Q6
q6_list = list(map(lambda x: x*3, [1, 2, 3, 4]))
print(q6_list)

#Q7
q7_list = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(q7_list))
print(min(q7_list))
print(max(q7_list)+min(q7_list))

#Q8
q8_float = round(17/3, 4)
print(q8_float)

#Q9
'''
argList = sys.args[1:] #sys.args[0]은 'myargv.py'
result = 0
for num in argList:
    result += num
print(result)
'''

#Q10
'''
import os
os.chdir('c:/Users/최주은/choijueun')
result = os.popen("dir")
print(result.read())
'''

#Q11
'''
import glob
glob.glob('c:/Users/최주은/choijueun/ngdaps/*.py')
'''

#Q12
import time
time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))

#Q13
import random
lottoList = list(range(1,45))
result1 = []
for i in range(6):
    num = random.choice(lottoList)
    result1.append(lottoList.pop(num))
print(result1)
'''
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
IndexError: pop index out of range
'''

import random
result2 = []
while len(result2)<6:
    num = random.randint(0,45)
    if num not in result2:
        result2.append(num)
print(result2)