# p236: 06-1 구구단 만들기
def GuGu(n):
    result = []
    for i in range(1,10):
        result.append(n*i)
    return result

print(GuGu(2))


# p239: 06-2 3과 5의 배수 합하기
# http://projecteuler.net/archives
def sum35(n):
    sum = 0
    for i in range(1,n):
        if i%3 == 0 or i%5 == 0:
            sum += i
    return sum

rs = sum35(1000)
print(rs)

# p242: 06-3 게시판 페이징하기
def getTotalPage(total, unit):
    if total%unit == 0:
        return total//unit
    else:
        return total//unit +1

getTotalPage(10,10)

# p244: 06-4 간단한 메모장 만들기
import sys

option = sys.argv[1]
if option == '-a':
    texts = sys.argv[2:]
    f = open('memo.txt', 'a')
    f.write(' '.join(texts))
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt', 'r')
    memo = f.read()
    f.close()
    print(memo)

# p247 : 06-5 탭을 4개의 공백으로 바꾸기
import sys
src = sys.argv[1]
dst = sys.argv[2]

f = open(src, 'r')
text = f.read()
f.close()

f2 = open(dst, 'w')
f2.write(text.replace('\t', ' '*4))

# p250 : 06-6 하위 디렉터리 검색하기
import os
def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for name in filenames:
            full_filename = os.path.join(dirname, name)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass

search('C:\\Users\\최주은\\choijueun')

import os
for (path, dir, files) in os.walk('C:\\Users\\최주은\\choijueun'):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print('%s/%s' %(path, filename))