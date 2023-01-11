'''
푼 시간 : 49분
성능 : 메모리 127600KB, 시간 288ms
주의할 점 :
    log(2)1,000,000,000 ~= 30
    시간복잡도 O() : 1억이 1초 정도
'''

# 집의 개수와 공유기의 개수 입력받기
N, C = map(int,input().split())
# 집의 좌표 입력받기
home_x = []
for _ in range(N):
    home_x.append(int(input()))

# 이진탐색을 위한 정렬
home_x.sort()

#공유기 설치시 거리차이의 최대값과 최소값을 구한다
max_distance = home_x[-1] - home_x[0]
min_distance = 1

while min_distance <= max_distance:
    mid = (min_distance + max_distance) // 2

    # mid값으로 공유기를 앞에서부터 설치
    pointer = home_x[0] # 마지막으로 설치한 집의 좌표
    count = 1 # 첫번째 집은 무조건 설치
    for x in range(1,N):
        # 마지막으로 설치한 집의 좌표와 최대거리보다 집의 좌표가 떨어져있으면 해당 집의 좌표에 공유기 설치
        if home_x[x] >= pointer + mid :
            pointer = home_x[x]
            count += 1

    # 설치한 공유기가 공유기의 개수보다 많으면 mid값을 커지게 하기위해 min_distance 변경, answer에 mid값 저장
    if count >= C:
        min_distance = mid + 1
        answer = mid # (구해야하는 값)
    # 설치한 공유기가 공유기의 개수보다 적으면 mid값을 줄어들게 하기위해 max_distance 변경
    else:
        max_distance = mid -1

# 정답 출력
print(answer)