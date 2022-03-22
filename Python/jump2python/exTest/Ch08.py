#-*- coding: utf-8 -*-

# p283: 08장 종합문제
# https://wikidocs.net/12769#08

# Q1 문자열 바꾸기
'#'.join('a:b:c:d'.split(':'))

# Q2 딕셔너리 값 추출하기
a = {'A':90, 'B':80}
a.get('C', 70)

# Q3 리스트 더하기와 extend 함수
a = [1,2,3]
# a = a + [4,5]
# a.extend([4,5])

# Q4 리스트 총합 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum([n for n in A if n>=50])

# Q5 피보나치 함수
def fibonacci(n):
    lis = []
    i = 0
    while i<14:
        lis.append(i) if i<2 else lis.append(lis[i-2]+lis[i-1])
        if lis[i] > n:
            del lis[i]
            break
        i += 1
    return lis

fibonacci(14)

def fibonacci2(n):
    if n==0: return 0
    elif n==1: return 1
    return fibonacci2(n-2)+fibonacci2(n-1)

# Q6 숫자의 총합 구하기
inputs = list(map(int, input("숫자는 콤마로 구분하여 입력한다: ").split(',')))
sum(inputs)

# Q7 한 줄 구구단
num = int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))
for i in range(1,10):
    print(num*i, end=' ')
    
# Q8 역순 저장
import os

from sqlalchemy import null
os.chdir(os.getcwd())

f = open('abc.txt', 'r')
txt_origin = f.read()
f.close()

txt_origin = txt_origin.split('\n')

txt_new = ''
for i in range(len(txt_origin)):
    if i != 0 : txt_new += '\n'
    txt_new += txt_origin[-(i+1)]

f = open('abc.txt', 'w')
f.write(txt_new)
f.close()

# Q9 평균값 구하기
f = open('sample.txt', 'r')
all_grades = f.read()
f.close

all_grades = list(map(int,all_grades.split('\n')))

f = open('result.txt', 'w', encoding="utf-8")
f.write('총합: '+str(sum(all_grades)))
f.write('\n')
f.write('평균: '+str(sum(all_grades)/len(all_grades)))
f.close()

# Q10 사칙연산 계산기
class Calculator:
    def __init__(self, input_list):
        self.input_list = input_list
    
    def sum(self):
        return sum(self.input_list)

    def avg(self):
        return sum(self.input_list)/len(self.input_list)
    
cal1 = Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()
cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()

# Q11 모듈 사용 방법

# Q12 오류와 예외 처리

# Q13 DashInsert 함수
import re

def DashInsert(num):
    num = str(num)
    #연속홀수
    num = re.sub('([13579])(?=[13579])', '\g<1>-', num)
    #연속짝수
    num = re.sub('([02468])(?=[02468])', '\g<1>*', num)
    
    return num

DashInsert(4546793)

# Q14 문자열 압축하기
def compress_string(input_str):
    _c = ''
    result = ''
    cnt = 0
    for s in input_str:
        if _c == s :
            cnt += 1
        else:
            _c = s
            if cnt: result += str(cnt)+_c
            else: result += _c
            cnt = 1
    if cnt:
        result += str(cnt)
    return result

print(compress_string('aaabbcccccca'))
            

# Q15 Duplicate Numbers
def DuplicateNumbers(input_str):
    for i in range(10):
        m = re.search(str(i)+'+', input_str)
        if not m or m.end()-m.start() != 1: 
            return False
    return True

DuplicateNumbers('123456789')

# Q16 모스 부호 해독
import re

MorseCode = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z'
}

def MorseToString(input_str):
    p = re.compile("(\S+)")
    result = ''
    
    list_word = input_str.split('  ')   #단어 단위로 분리
    for word in list_word:
        
        list_chr = word.split(' ')      #글자 단위로 분리
        for each_chr in list_chr:
            
            m = p.findall(each_chr)
            if not m: return 'Error'
            
            for result_chr in m:
                result += MorseCode[result_chr]
                
        result += ' '
    return result

HE_SLEEPS_EARLY = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'
print(MorseToString(HE_SLEEPS_EARLY))

# Q19 그루핑
def Last4Number(input_str):
    p = re.compile('(\d{3})[-](\d{4})[-](\d{4})', re.MULTILINE)
    m = p.sub('\g<1>-\g<2>-####', input_str)
    print(m)

s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

Last4Number(s)

# Q20 전방 탐색
def validEmail(input_email):
    p = re.compile('.*[@].*[.](?=com$|net$).*$')
    m = p.search(input_email)
    if m:
        print(m.group())
        return True
    return False

email_A = 'park@naver.com'
email_B = 'kim@daum.net'
email_C = 'lee@myhome.co.kr'
print(validEmail(email_A))
print(validEmail(email_B))
print(validEmail(email_C))