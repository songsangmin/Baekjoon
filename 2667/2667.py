# line 수 입력
lines = int(input())

#행렬 만들기
graph = [list(map(int, input())) for _ in range(lines)]

num = []

#상하좌우 비교를 위한 선언
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0 #집 개수
number = 0 #단지 개수

def Compare(x,y):
    #가로 세로 범위를 넘어가거나 0보다 작을시 False 반환
    if x < 0 or x >= lines or y < 0 or y >= lines:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0 #탐색위치 0 변경 -> 이것 때문에 재탐색 안됨
        for i in range(4): 
            nx = x + dx[i] #좌우비교
            ny = y + dy[i] #상하비교
            Compare(nx, ny) #재귀호출
        return True
    return False

for i in range(lines):
    for j in range(lines):
        if Compare(i,j) == True:
            num.append(count)
            number += 1
            count = 0

num.sort() #정렬
print(number)
for i in range(len(num)):
    print(num[i])