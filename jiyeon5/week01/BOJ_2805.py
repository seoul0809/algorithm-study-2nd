'''
푼 시간 : 27분
성능 : 메모리 149780KB, 시간 4824ms
주의할 점 :
    input으로 입력받고 숫자는 int형으로 변환 해주기
'''


# 입력 데이터 개수로 인한 시간초과 방지하기 위해 라이브러리 추가
import sys

# N: 나무의 수, M: 상근이가 집으로 가져가려고 하는 나무의 길이 입력 받기
N, M = map(int,input().split())
# 나무의 높이 입력 받기
trees = list(map(int,sys.stdin.readline().split()))

start = 0
end = max(trees) # 나무들의 높이 중 최대값을 초기 끝점으로 세팅

# 절단하는 높이 (구해야하는 값)
cut = 0
# 이분탐색
while start <= end:
    mid = (start + end) // 2

    sum = 0
    # 절단 후 가져가는 나무 높이 확인
    for t in trees:
        if t > mid: # 가져갈 수 있는 나무가 있다면 sum에 추가
           sum += t - mid

    # 절단 후 가져가는 높이가 M보다 크다면 절단 높이 저장 후 절단 높이 올리기
    if sum >= M:
        cut = mid
        start = mid +1
    # 절단 후 가져가는 높이가 M보다 작다면 절단 높이 낮추기
    else:
        end = mid -1

# 절단 높이 최대값 출력
print(cut)