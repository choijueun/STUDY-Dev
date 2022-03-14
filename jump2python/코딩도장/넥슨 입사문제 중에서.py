# Lv.2 제네레이터
'''
def d(n):
    number_list = list(str(n))
    
    result=int(n)
    for num in number_list:
        result += int(num)
    
    return result

d(91)

self_list = list(range(5000))
for num in range(5000):
    not_self = d(num)
    if not_self in self_list: self_list.remove(not_self)

sum(self_list)
'''

#풀이 참고, 수정
def d(n):
    return sum([int(num) for num in str(n)])+n

set_5000 = set(range(1,5000))               #1~5000 집합
set_self = { d(n) for n in range(1,5000) }  #self number 집합

sum(set_5000-set_self)