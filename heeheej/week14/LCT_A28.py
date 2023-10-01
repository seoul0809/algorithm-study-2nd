# 고정점 찾기
# 이진탐색

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

left, right = 0, N-1
result = -1
while left <= right:
    mid = (left + right) // 2
    if mid > arr[mid]:
        left = mid + 1
    elif mid < arr[mid]:
        right = mid - 1
    else:
        result = mid
        break
print(result)
