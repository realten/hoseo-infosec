# 자료형 공부

## 빈 리스트 생성
def emptylist():
    return list()


## 리스트 인덱싱
def listindexing(i):
    list = ['a', 'b', 'c', 'd', 'e']
    return list[i]


## 리스트 슬라이싱
def listslicing(i, j):
    list = ['a', 'b', 'c', 'd', 'e']
    return list[i:j]


## 리스트 요소 추가
def listappend(c):
    list = ['a', 'b', 'c']
    list.append(c)
    return list


## 리스트 요소 삭제
def listremove(c):
    list = ['a', 'b', 'c']
    list.remove(c)
    return list


## 리스트 정렬
def listsort():
    list = ['b', 'e', 'a', 'c', 'd']
    list.sort()
    return list


## 리스트 리버스
def listreverse():
    list = ['a', 'b', 'c']
    list.reverse()
    return list


## 리스트 특정 값의 인덱스 반환
def listindex(c):
    list = ['a', 'b', 'c']
    try:
        idx = list.index(c)
    except:
        # 리스트에서 값을 찾지 못한 경우 오류 처리
        idx = -1
    return idx


## 리스트 특정 인덱스에 요소 삽입
def listinsert(i, c):
    list = ['a', 'b', 'c']
    list.insert(i, c)
    return list


## 리스트 특정 값 개수
def listcount(c):
    list = ['a', 'b', 'c', 'b', 'c']
    return list.count(c)


## 리스트 확장
def listextend(temp):
    list = ['a', 'b', 'c']
    list.extend(temp)
    return list


if __name__ == '__main__':
    print(emptylist())
    print(listindexing(0))          # list[0] 은 앞에서 첫 번째 값
    print(listindexing(-1))         # list[-1] 은 뒤에서 첫 번째 값
    print(listslicing(0, 2))        # list[1:3] 는 list[1] ~ list[3 - 1] 값 조회
    print(listappend('d'))          # list의 맨 마지막에 'd' 추가
    print(listremove('b'))          # list에서 첫 번째 나오는 'b' 제거
    print(listsort())               # list 정렬
    print(listreverse())            # list 리버스
    print(listindex('z'))           # list 인덱스
    print(listinsert(1, 'z'))       # list 특정 인덱스에 요소 삽입
    print(listcount('b'))           # list 특정 값 개수
    print(listextend(['d', 'e']))   # list 확장
