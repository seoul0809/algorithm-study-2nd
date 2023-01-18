# 부분합
# 144ms, 128152kb

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N, S = map(int, input().split())
inputs = list(map(int, input().split()))

result = float('inf')
sum, left, right = 0, 0, 0

while True: # 한 iteration이 끝나고 나면 left부터 right-1번쨰까지 더한게 sum
    if sum >= S:
        result = min(result, right - left)  # right은 이미 1 앞서가있으므로 길이를 계산하기 위해 (left+right)에 +1해줄필요 X
        sum -= inputs[left]
        left += 1

    elif right == N:    # sum이 S이상이 아닌데 right가 N이면 right를 키울 수 없음 => 종료
        break
    else:
        sum += inputs[right]
        right += 1

if result == float('inf'):
    print(0)
else:
    print(result)