'''
푼 시간 : 7분
성능 : 메모리 31704KB, 시간 40ms
주의할 점 :
'''

# N, M을 입력받기
n, m = map(int, input().split())
# N개의 수로 된 수열을 입력받기
arr = list(map(int, input().split()))

count = 0 # 부분합의 갯수 (구해야하는 값)
sum = 0 # 부분합을 저장하는 변수
end = 0

# start를 차례로 증가시키며 반복
for start in range(n):
    # end를 차례로 증가시키기
    while end < n and sum < m:
        sum += arr[end]
        end += 1
    # 부분합이 m과 같을때 카운트 증가
    if sum == m:
        count += 1
    # start 포인트 이동
    sum -= arr[start]

print(count)