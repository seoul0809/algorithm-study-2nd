'''
푼 시간 : 2시간
성능 : 메모리 115400KB, 시간 196ms
주의할 점 :
    python으로 제출 시 시간초과 -> pypy로 제출
'''


# 전체 용액의 수 입력받기
N = int(input())
# 용액의 특성값 입력받기
solutions = list(map(int,input().split()))

# 탐색을 사용하기 위해 용액 배열 정렬하기 O(NlogN)
solutions.sort()

# 세 용액의 특성값의 합을 최대값으로 초기 세팅
sum = 3_000_000_000
# 세 용액을 담을 배열을 설정 (구해야하는 값)
ans_solution = []

# 첫번째 용액을 고르고 나머지 두용액을 첫번째 용액 다음 용액부터 가장 끝 용액으로 설정한뒤 포인터를 이동하며 용액의 합이 0에 가장 가까운 값을 찾는다
for i in range(N-2):
    left = i+1 #왼쪽 포인터, 두번째 용액
    right = N-1 # 오른쪽 포인터, 세번째 용액
    while left < right:
        tmp = solutions[i] + solutions[left] + solutions[right]
        # 세 용액의 절대값 합이 가장 적은 값으로 sum과 배열을 업데이트
        if abs(tmp) < abs(sum) :
            sum = tmp
            ans_solution = [solutions[i], solutions[left], solutions[right]]

        #용액의 합이 0보다 작으면 더 큰 용액을 추가해야하므로 left 오른쪽으로 이동
        if tmp < 0:
            left += 1
        # 용액의 합이 0보다 크면 더 작은 용액을 추가해야하므로 right 왼쪽으로 이동
        elif tmp > 0:
            right -= 1
        # 0일 경우 최소값이므로 반복문 탈출
        else:
            break

# 용액의 값 오름차순으로 출력
print('{0} {1} {2}'.format(ans_solution[0], ans_solution[1], ans_solution[2]))