#시계수 찾기
def find_num(num):
    c_num = num
    for _ in range(3):
        num = (num % 1000) * 10 + num // 1000
        if c_num > num:
            c_num = num
    return c_num

#숫자 입력
c_num = find_num(int(''.join(input().split())))

i = 1111
cnt = 0
# 1111부터 c_num가지의 기계수 개수를 카운트
while(i<=c_num):
    if find_num(i) == i:
        cnt += 1
    i += 1

print(cnt)