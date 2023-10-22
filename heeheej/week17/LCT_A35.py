# 못생긴 수
N = int(input())

dp = [0]*N  # 못생긴 수를 담기 위한 dp 배열
dp[0] = 1 # 첫번째 못생긴 수는 1

i2 = i3 = i5 = 0    # 2배, 3배, 5배를 위한 인덱스
next2, next3, next5 = 2, 3, 5   # 곱셈값 초기화

for l in range(1, N):
    dp[l] = min(next2, next3, next5)
    if dp[l] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if dp[l] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if dp[l] == next5:
        i5 += 1
        next5 = dp[i5] * 3
print(dp[N-1])