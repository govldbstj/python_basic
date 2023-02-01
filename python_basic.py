print("hello world")

a = 2
b = 3.5
c = a+b
print(c)

print("python")
print('python')
print("""python""")
print('''python''')

apple = 3
print('I eat %d apples' %a)

print('%d'%a) #정수
print('%f'%a) #부동소수점수
print('%x'%a) #16진수

from math import *
tmp = 4.5 
tmp = round(tmp) #반올림 함수
print('%f' %tmp) #반올림 법칙 -> 정수부가 짝수면 .5단위가 버려짐
tmp = 3.5 
tmp = round(tmp)
print('%f' %tmp) #반올림 법칙 -> 정수부가 홀수면 .5단위가 버려짐

#formatting
k = 'world'
print('hello', k)
print('hello %s' %k)
print('hello {}'.format(k))
print(f'hello {k}') # python3 기준으로 속도가 가장 빠르다.

#문자열 관련 함수
name = 'yunseo'
print(name.count('e')) #e 개수 반환
print(name.find('o')) #0부터 시작하는 인덱스로, 5 반환
print(name.find('a')) #없을 때는 -1 반환

underbar = '_'
t = underbar.join('abcd')
print(t)

#upper -> 전체 대문자화
a = 'hi'
print(a.upper())

#lower -> 전체 소문자화
a = 'hi'
print(a.lower())

#strip -> 띄어쓰기 없게
a = ' h i '
print(a.strip())

#replace -> 특정 단어 대체
a = 'new world'
print(a.replace('new', 'old'))

#split -> parsing
a = 'a b c d'
print(a.split(' '))

#index slicing
a = [1, 2, 3]
print(a[0]) #1
print(a[0] + a[2]) #1+3
print(a[-1]) #3 뒤로가기도 가능

a = [1,2,3,['a','b','c']]
print(a[-1])
print(a[-1][0])

a = [1,2,3,4,5]
print(a[0:2]) # 0부터 2미만이므로, 0과 1인덱스에 해당하는 원소만 출력

#리스트 연산자
a = [1,2,3]
b = [4,5]
print(a+b) # 두 리스트 연결

a = [1,2,3]
print(a*3) # 값이 곱해진 것이 아니라 여러번 반복 출력됨

a[2] = 4 
print(a) # 월소 대체

a[1:2] = ['a','b','c']
print(a) # 원소 범위도 대체

a[1:3] = []
print(a) # 원소 범위로 대체 = 삭제

del(a[1])
print(a) # 원소 삭제

''' 리스트 내장함수 '''

#리스트에 값 추가 : append
a = [1,2,3]
a.append(4)
print(a)
a.append([5,6]) # 5,6을 원소로 삽입하고 싶다면 [] 뺄 것
print(a)

#리스트 정렬 : sort
a = [1,2,3,4]
a.sort()
print(a)

#리스트 뒤집기 : reverse
a.reverse()
print(a)

#리스트 내 위치 반환 : index
a = [1,2,3]
print(a.index(3))
# 없을 경우 오류 반환, 같은 기능을 하는 find 함수는 -1 반환

#리스트 중간 값 삽입 : insert
a.insert(0,4) # 0번 인덱스 자리에 4 삽입
print(a)
a.insert(3,5) # 3번 인덱스 자리에 5 삽입
print(a)

#리스트에서 원소 제거 : remove
a = [1,2,1,2]
a.remove(2) # 2번 인덱스 자리의 원소 제거
print(a)

#리스트의 마지막 값 꺼내는 pop
a = [1,2,3]
print(a.pop())
print(a) # a에서 마지막이 제거됨

#리스트 내부의 값을 세는 count
a = [1,2,3,1]
print(a.count(1))

#리스트를 확장하는 extend
a = [1,2,3]
a.extend([4,5])
print(a)

''' 튜플
-> 리스트와 유사하지만, 대괄호가 아닌 소괄호를 이용 () 
-> 슬라이싱과 인덱스는 동일하게 적용되지만, 값 변경/삭제는 불가능 
-> 즉, 값의 변경을 원하지 않을 때 (const처럼 사용하고 싶을 때) 사용 '''

''' 딕셔너리
-> 키벨류 쌍으로 이루어짐 (json과 같은 형태), key를 통해 value를 얻어내는 방식으로 사용 가능
-> 중괄호를 이용해 생성할 수 있음. 또는 a[2] = 'b'의 형태로 추가 가능
-> del[1]로 삭제 가능 '''

''' 집합
-> 집합에 관련된 자료형
-> 중괄호
-> set을 이용해 생성, 중복 허용 x, 순서도 없음 '''

s1 = set([1,2,3])
print(s1)
s2 = set('Hello')
print(s2)

#집합의 연산

#교집합
s3 = s1&s2
print(s3)

#합집합
s3 = s1|s2
print(s3)

#차집합
s3 = s1-s2
print(s3)

#집합에 값 하나만 추가 : add
s1.add(5)
print(s1)

#집합에 값 여러개 추가 : update
s1.update([300,400,500])
print(s1)

#특정 값 제거 : remove
s1.remove(300)
print(s1)

''' 불리언
-> 참과 거짓을 분리
-> 어떤 문자라도 있을 경우 True
-> ""처럼 아무것도 없을 경우 False
-> 리스트 튜플 다 동일, 딕셔너리의 경우 키와 벨류 하나도 없으면 false
-> 숫자형이 아닌 경우 0이 아닌 숫자는 true, 0과 none은 false '''

''' 조건문
if - elif - else로 구성
비교 연산자 (> , < , <=, == 등), 논리연산자 (or, and, not) 사용 가능
값의 존재 여부도 확인 가능 (a in [list / tuple / string] -> true false로 반환)
'''

l = ['a', 'b', 'c', 'd']

if 'b' in l :
    print('존재합니다')
else:
    print('존재하지 않습니다')

# pass : 구현 내용이 미정이거나 아무것도 하고 싶지 않을 때 사용

for i in range(1, 100):
    if i > 50 :
        print(i)
    else : pass

''' 반복문
for, while 대표적 '''

a = 10

for i in range (1, a):
    a = a + 1
    print(a)

l = [1,2,3,4]

for i in l : 
    print(i)
    if i % 2 == 0:
        continue
    else:
        break


''' 함수
반복 방지, 가독성을 위해 사용 '''

# def: 함수 정의

def myFunc(*args):
    for arg in args:
        print(arg)

myFunc(10, 20, 'a') # args : 정해지지 않은 개수의 파라미터이므로 여러 개 가능

# global: 전역변수 사용

a = 1

def vartest():
    global a
    a = a + 1
    print(a)

vartest()
print(a)

''' 클래스
-> 파이썬의 객체지향적 특징
-> 내부에서 사용할 수 있는 함수를 포함하고, 클래스를 활용해 여러 가지 객체 생성 가능 '''

class Calculator:
    def __init__(self):
        self.result = 0
    # 메소드 : 클래스 내부에 정의된 함수 -> add
    def add(self, num):
        self.result += num
        return self.result

# 인스턴스 : 클래스를 통해 생성된 객체 -> cal1, cal2
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(5))

''' 사용하는 이유 : 똑같은 메소드를 가진 객체 생성이 가능 '''

''' 모듈
함수, 변수 또는 클래스를 모아놓은 파일, import로 호출 가능
특정 함수만 쓰고 싶을 때는 from math import pi 이렇게 pi만 가지고 올 수 있음
'''

''' 예외 처리
-> 파이썬 오류의 종류
1. 문법 오류 -> 코드 실행 전에 잡은 오류 / 2. 코드 실행 중 오류 -> 인덱스/ 파일탐색 불가 등 
-> try/catch문으로 예외 처리
'''

for i in range (0,11):
    try :
        print(i, 1/(10-i))
    except ZeroDivisionError as e:
        print(e)

''' 파이썬 내장 함수
abs() all() 등
파이썬 외장 함수
sys() pickle() os() time() random() threading()등
'''

