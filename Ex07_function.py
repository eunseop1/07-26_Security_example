def add_and_mul(a, b):
    return a + b, a * b
result = add_and_mul(3, 4)
print(type(result), result)

# 오버라이딩이 된다
def add_and_mul(a, b, c):
    return [a + b + c, a * b * c]
result = add_and_mul(3, 4, 5)
print(type(result), result)

def say_myself(name='무명', old=18, man = True):  #디폴트 값은 뒤에서 부터 지정해야만 한다
    #print("나의 이름은 %s입니다" %name)
    #print("나이는 %d살입니다" %old)
    print("나의 이름은 {0}입니다".format(name))
    print("나이는 {0}살입니다".format(old))
    if man:
        print("남자입니다")
    else:
        print("여자입니다")
    print()
say_myself('한사람', 34)
say_myself('두사람', 34, False)
say_myself('세사람')  # 이렇게만 하면 어떤 인수인지 모르기에 에러, 모든 인수에 기본값을 주거나 혹은 마지막에만 인수의 기본값을 줘야 한다
say_myself(man=False, name="네사람", old=22)
say_myself(22, "네사람")  # 이렇게 하면 나이는 22로 인식하고 네사람을 %d로 출력하려다 에러가 난다.

a = 1
def vartest(a):
    a = a + 1  # 함수안에서 선언한 변수는 함수내에서만 유효하다
    return a
b = vartest(a)
print(a)  # 1
print(b)  # 2

a = 5
def vartest():
    global a  #전역변수를 사용하겠다
    a = a + 1

vartest()
print(a)