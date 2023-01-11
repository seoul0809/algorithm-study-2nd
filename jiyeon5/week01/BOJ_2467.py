'''
푼 시간 : 1시간
성능 : 메모리 41968KB, 시간 428ms
주의할 점 :
    함수 내에서 전역변수 사용시 global로 재선언 하기
    print format 형식 익히기
'''


# 전체 용액의 수 입력받기
N = int(input())
# 용액의 특성값 입력받기
solutions = list(map(int,input().split()))

# 두 용액의 특성값 합을 최대값인 2000000000 으로 초기 세팅
answer = 2000000000
# 출력할 두 용액을 담을 배열 설정 (구해야하는 값)
ans_solution = [-1, -1]

# 이분탐색으로 두번째 용액값 구하는 함수
def binary_search(start, end, one):
    # 전역변수 answer 사용위해 global로 재선언
    global answer

    while start <= end:
        mid = (start + end) // 2

        # 새로만든 두 용액의 값이 저장된 두 용액의 값보다 작은 경우 업데이트
        mix = solutions[mid] + one
        if abs(mix) < abs(answer) : # 용액 값이 음수와 양수 둘다 가능하기 때문에 절대값을 취한다
            answer = mix
            ans_solution[0], ans_solution[1] = one, solutions[mid] # 첫번째 용액의 값과 두번째 용액의 값을 갱신

        # 섞은 용액의 값이 0보다 작으면 두번째 용액의 값이 더 커지는 쪽으로 탐색
        if mix < 0 :
            start = mid + 1
        # 섞은 용액의 값이 0보다 작으면 두번째 용액의 값이 더 커지는 쪽으로 탐색
        elif mix > 0:
            end = mid -1
        # 섞은 용액의 값이 0이면 탐색 종료
        else:
            return

# 두 용액 중 한 용액 one을 설정하고 나머지 용액을 solutions에서 이분탐색을 진행하며 특성값이 0에 가까운 용액을 찾는다
for i in range(N):
    # 두 용액 중 한 용액을 설정
    one = solutions[i]
    # 용액의 특성값은 정렬되어 있으므로 첫번째 용액으로 선택한 'one의 바로 뒤 인덱스'와 '전체 용액 수-1'을 start, end로 세팅
    start = i+1
    end = N - 1
    # 이분탐색 진행
    binary_search(start, end, one)

# 특성값을 오름차순으로 출력
ans_solution.sort()
print('{0} {1}'.format(ans_solution[0],ans_solution[1]))