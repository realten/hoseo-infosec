# 자료형 공부

## Boolean - 참
def isTrue():
    return True


## Boolean - 참
def isFalse():
    return False


# 논리 여부 체크
def isNull(v):
    return bool(v)


# And 연산자
def andCalc():
    return True & False


# Or 연산자
def orCalc():
    return True | False


if __name__ == '__main__':
    print(isTrue())
    print(isFalse())
    print(f'''"python" is {isNull("python")}, "" is {isNull("")}''')  # 문자열
    print(f'''1 is {isNull(1)}, 0 is {isNull(0)}''')  # 숫자
    print(f'''[0, 1] is {isNull([0, 1])}, [] is {isNull([])}''')  # 리스트
    print(f'''(0 ,1) is {isNull((0, 1))}, () is {isNull(())}''')  # Tuple
    print(f'''%s is {isNull({"k": "v"})}, %s is {isNull({})}''' % ({'k : v'}, {}))  # Dictionary
    print(f'''None is {isNull(None)}''')  # None
    print(f'True & False is {andCalc()}')
    print(f'True | False is {orCalc()}')
