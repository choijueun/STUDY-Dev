# Lv1. 연립일차방정식의 해 계산기

def linearE(a, b, c, d, e, f):
    #print(str(a)+'x + '+str(b)+'y + '+str(c)+'= 0')
    #print(str(d)+'x + '+str(e)+'y + '+str(f)+'= 0')
    solutionY = (a*f - c*d)/(b*d - a*e)
    solutionX = -(c + b*solutionY)/a
    print('solution X:',solutionX)
    print('solution Y:',solutionY)
   
linearE(1,2,-3,4,5,-6)
linearE(1,1,-2,1,2,-3)

# 풀이 참고, 수정
from math import lcm
from fractions import Fraction as frac

def trsE(linearE):
    e = list(linearE.replace(' ',''))
    l = []
    eq = False
    for i, val in enumerate(e):
        try:
            if val == '=':
                eq = True
            elif e[i-1] == '-':
                l.append(-int(val))
            elif eq:
                l.append(-int(val))
            else:
                l.append(int(val))
        except:
            if val == '=':
                break
            else:
                pass
    return l
    
def lenearE2(inE1, inE2):
    e1 = trsE(inE1)
    e2 = trsE(inE2)

    A, B, C = e1
    a, b, c = e2
    
    if (A*b == a*B):
        if (A*c == a*C):
            print("해가 무수히 많습니다.")
        else:
            print("해가 존재하지 않습니다.")
    else:
        l=lcm(B,b)
        f1=int(l/B)
        f2=int(l/b)
        for i in range(3):
            e1[i]*=f1
            e2[i]*=f2
        e3=[]
        for j in range(3):
            e3.append(e1[j]-e2[j])
        x=frac(-e3[2], e3[0])
        y=(-A*x - C)/B
        print('x =',x,'y =',y)

lenearE2('1x + 1y = 2', '1x + 2y = 3')