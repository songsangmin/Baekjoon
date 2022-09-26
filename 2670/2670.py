N = int(input()) #실수 개수 입력받기
array = list(float(input()) for _ in range(N)) #N 개수 만큼 실수 입력받기

for i in range(1, N):
    array[i] = max(array[i], array[i] * array[i - 1]) #최대곱 찾기

print('%0.3f' % max(array)) #소수점 셋째 자리까지 최댓값 출력