#이번 문제는 어려워서 검색을 통해 찾아보았다.다시 한번 더 고민하고 공부 필요.
import re #정규표현식을 사용할 수 있는 내장 함수


N = input()
p = re.compile('(100+1+|01)+') #규칙 생성

m = p.fullmatch(p) #fullmatch 함수(문자열의 처음부터 끝까지 패턴에 일치되는 지를 확인해주는 함수)
                   #match 시 match 된 객체 반환 match 안될 시 None
    
if m:
    print("SUBMARINE")
else:
    print("NOISE")