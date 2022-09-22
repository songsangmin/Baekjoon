count = int(input())		# 가로 개수 입력
arr = [0]   # 리스트 선언
result = set()   #결과 저장 및 중복제거 위한 Set  

for _ in range(count):
    arr.append(int(input())) # 두 번째 줄 입력

# 함수 선언
def Compare(first, second, number):
    first.add(number)			
    second.add(arr[number])	
    if arr[number] in first:		
        if first == second:		#  첫번째 줄 집합과 두번째 줄 집합이 같다면
            result.update(first)	# 결과 업데이트
            return True             # True 반환
        return False    #첫번째 줄 집합과 두번째 줄 집합이 같지 않을 시 False 반환
    return Compare(first, second, arr[number])	#  첫 번째에 arr[number]가 없다면 함수 실행

# 함수 실행
for i in range(1, count+1): #1부터 가로개수만큼
    if i not in result:			# 결과 안에 i가 없을 시
        Compare(set(), set(), i)

print(len(result)) #결과의 개수 출력
print(*sorted(list(result)), sep='\n') #오름차순