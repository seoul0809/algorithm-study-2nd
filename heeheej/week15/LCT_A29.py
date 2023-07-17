# 공유기 설치 (BOJ 2110)
# 116560kb, 192ms
# 이진탐색
# mid ==> 가장 인접한 두 공유기 사이의 거리 (gap)
# mid를 조절해가며 C보다 많은 개수로 공유기를 설치할 수 있는지 확인한다.
# C보다 더 많이 설치할 수 있다면 gap을 늘린다.
# left의 초기값은 1이어야 한다. 교재가 틀린듯

import pprint
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

left = 1
right = arr[-1] - arr[0]
result = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 1 # 가장 인접한 두 공유기 사이의 거리가 mid일 때 세울 수 있는 공유기 수
    value = arr[0]
    for i in range(1, N):
        if arr[i] >= value + mid:
            value = arr[i]
            cnt += 1
    if cnt >= C:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)