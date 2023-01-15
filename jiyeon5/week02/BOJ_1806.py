'''
푼 시간 : 20분
성능 : 메모리 41824KB, 시간 124ms
주의할 점 :
    두개의 값 비교하여 저장할 때 max(), min() 함수 사용
    1e9 ~= 1_000_000_000
'''

# N, S 입력받기
n, s = map(int,input().split())
# N짜리 수열 입력받기
arr = list(map(int, input().split()))

answer = 1e9 # 부분합이 S이상이 되는 것 중 가장 짤은 것의 길이, 초기엔 무한대 값으로 설정 (구해야하는 값)
end = 0 # 두번째 포인터
sum = 0 # 두개의 포인터 사이의 수들로 이루어진 부분합

# 모든 배열 값을 돌면서 부분합 계산 반복
for start in range(n): #첫번째 포인터
    # 포인터 사이 부분합이 S보다 작다면 두번째 포인터 오른쪽으로 이동
    while end < n and sum < s:
        sum += arr[end]
        end += 1
    # 부분합이 S보다 크거나 같다면 answer와 비교해서 부분합이 짧은 길이를 저장
    if sum >= s:
        tmp = end - start
        answer = min(answer, tmp)
    # 첫번째 포인터 오른쪽으로 이동
    sum -= arr[start]

# 정답 출력
print(answer if answer!=1e9 else 0) #합을 만드는 것이 불가능하다면 0을 출력
