# 자료형 공부

## 문자열
def basic():
    s1 = 'one'                  # 작은따옴표로 문자열 감싸기
    s2 = "two"                  # 큰따옴표로 문자열 감싸기
    s3 = '''I'm Iron Man'''     # 3개의 작은따옴표로 문자열 감싸기
    s4 = """I'll Be Back"""     # 3개의 큰따옴표로 문자열 감싸기

    print(f'{s1}\n{s2}\n{s3}\n{s4}')


def stringMultiple():
    s1 = "ba"
    s2 = "na"
    print(s1 + (s2 * 2))    # 문자열에 곱셈을 하면 그 수만큼 반복하여 출력한다.


def length():
    s1 = "Hello World"
    print("문자열 길이 - len(s1) = %d" % (len(s1)))


def index():
    s1 = "abcdefg" \
         "hijklmn" \
         "opqrstu" \
         "vwxyz"
    print("5번째 문자열 - s1[4] = %c" % (s1[4]))   # 배열은 0번부터 시작하므로 5번째는 s1[4]번째에 있다.
    print("7번째부터 10번째 문자열 - s1[7:10] = %s" % (s1[7:10]))
    print("5번째까지의 문자열 - s1[:5] = %s" % (s1[:5]))
    print("22번째부터의 문자열 - s1[21:] = %s" % (s1[21:]))


if __name__ == '__main__':
    basic()
    stringMultiple()
    length()
    index()
