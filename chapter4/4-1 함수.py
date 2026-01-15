# 함수 만들기

# 두 수를 더하는 함수 
# def 함수이름(매개변수):
# 필요시 결과 리턴
def add(a, b):
    return a + b    

# 함수 사용하기
a = 3
b = 4
result = add(a, b) # 함수 호출
print(result) # 결과 출력

# 입력값 또는 결과값이 없을 수도 있음 

# 입력값 없고, 리턴값 있는 함수
def say():
    return 'Hi'

msg = say()
print(msg)

# 입력값 있고, 리턴값 없는 함수
def show_add(a, b):
    print(a, b, "의 합은:", a+b)

show_add(3, 4)

# 입력값 없고, 리턴값도 없는 함수
def show_hello():
    print('hello')

show_hello()
