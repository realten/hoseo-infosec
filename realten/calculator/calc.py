from plus import *
from minus import *
from multiply import *
from divide import *


def execute():
    print(plus.calc(2, 5))
    print(minus.calc(5, 3))
    print(multiply.calc(3, 2))
    print(divide.calc(10, 2))


# calc.py를 실행하는 경우 자기 자신이 메인이기 때문에 아래 라인을 수행한다.
if __name__ == '__main__':
    execute()
