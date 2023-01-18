'''
푼 시간 : 76분
성능 : 메모리 169624KB, 시간 1764ms (pypy)
주의할 점 :
    defaultdict를 사용하면 딕셔너리.setdefault(키,기본값) 설정을 하지 않아도 기본값 설정 가능
    del 을 사용해 딕셔너리 키값 제거
'''

from collections import defaultdict

# 벨트위 접시의 수, 초밥 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호 입력받기
n, d, k, c = map(int, input().split())
# 초밥 종류 입력받기
arr = [int(input()) for _ in range(n)]

# 회전초밥이므로 k만큼 더해준다, k이상부터는 배열을 0부터 탐색할때와 같음
arr += arr[0:k]

start = 0
end = 0
eat = defaultdict(int) # 먹은 초밥을 딕셔너리에 저장, defaultdict을 사용해 기본값 0으로 지정
max_eat = 0 # 초밥 가짓수의 최대값을 저장 (구해야하는 값)

# 쿠폰 초밥은 무조건 먹기
eat[c] += 1

# 처음 k 구간까지 먹기
while end < k :
    eat[arr[end]] += 1
    end += 1

# 슬라이딩 윈도우 적용해서 한칸씩 뒤로가며 k구간만큼씩 먹는 걸 반복
while end < n+k:
    max_eat = max(max_eat, len(eat))

    # 맨 왼쪽 초밥 제거
    eat[arr[start]] -= 1
    # start에 있던 초밥 다시 먹지 않을 걸로 표시하기
    if eat[arr[start]] == 0:
        del eat[arr[start]]

    # 초밥 먹으며 포인터 이동
    eat[arr[end]] += 1
    start += 1
    end += 1

print(max_eat)
