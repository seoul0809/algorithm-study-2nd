# 수들의 합 2
# 124ms, 114488kb
# 수열 A[]의 원소는 30000을 넘지 않는 자연수! => 투포인터

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
inputs = list(map(int, input().split()))

left, right = 0, 0
result = 0
sum = 0
for left in range(N):
    while sum < M and right < N:
        sum += inputs[right]
        right += 1
    if sum == M:
        result += 1
    sum -= inputs[left]
print(result)