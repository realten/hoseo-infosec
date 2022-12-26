#자료형 공부

## 숫자형
def basic():
    print('integer - basic() start')
    n1 = 1          # 정수
    n2 = 0b10       # 2진수
    n3 = 0o10       # 8진수
    n4 = 0x10       # 16진수

    print('n1 - %d\nn2 - %d\nn3 - %d\nn4 - %d' % (n1, n2, n3, n4))


def operator():
    print('integer - exam1() start')
    print('더하기 => 1 + 2 = %d' % (1 + 2))    # 더하기
    print('빼기 => 2 - 1 = %d' % (2 - 1))     # 빼기
    print('곱하기 => 2 * 3 =%d' % (2 * 3))     # 곱하기
    print('제곱 => 2 ** 3 =%d' % (2 ** 3))    # 제곱
    print('나누기 => 4 / 2 =%d' % (4 / 2))     # 나누기
    print('나머지 => 4 / 3 =%d' % (4 / 3))     # 나머지
    print('몫 => 4 // 2 =%d' % (4 // 2))      # 몫


if __name__ == '__main__':
    basic()
    operator()
