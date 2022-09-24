# x, y 좌표를 1이상 100이하로 설정
square = [[ 0 for _ in range(101)] for _ in range(101)]
#결과를 담을 변수 선언
result = 0 

for _ in range(4):
    # 왼쪽 아래 꼭짓점 오른쪽 위 꼭짓점 입력
    x1, y1, x2, y2 = map(int, input().split())

    #사각형 꼭짓점 부분 1로 변경
    for i in range(x1, x2):
        for j in range(y1, y2):
            square[i][j] = 1

for i in square:
    result += sum(i) # 결과에 면적 합 더함 

print(result)