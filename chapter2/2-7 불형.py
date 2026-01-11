# 불 (boolean)
a = True    #참
b = False   #거짓

# 비교 연산자
print(1 == 1)   #같은지
print(1 != 1)   #다른지
print(3 > 1)    #큰지
print(3 >= 1)   #크거나 같은지

# 변수로 비교
x=10
y=5
print(x > y)

# 논리 연산자
# and 연산자 : 양쪽 모두 참일때만 결과가 참
print(True and True) 
print(True and False)  
# or 연산자 : 한쪽이라도 참이면 결과가 참
print(True or False)
# not 연산자 : 참/거짓을 반대로 바꿈
print(not True)

# 변수로 비교
age = 20
money = 15000
# 나이가 19살 이상이고 소지금이 10000원 이상이면 참
print(age >= 19 and money >= 10000)
