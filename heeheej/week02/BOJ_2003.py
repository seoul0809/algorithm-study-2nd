# 수들의 합 2
# 240ms, 114488kb
# 수열 A[]의 원소는 30000을 넘지 않는 자연수! => 투포인터
# sum은 매 반복문마다 0부터 더해 계산할 필요 없이, left위치의 원소만큼 빼고, 다시 다음 반복문의 right위치의 원소만큼 더하면 된다!

import sys

sys.stdin = open("input.txt", "r")
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