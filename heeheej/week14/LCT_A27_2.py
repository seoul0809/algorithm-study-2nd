# 정렬된 배열에서 특정 수의 개수 구하기
# 이진탐색, bisect 라이브러리 없이

import sys
from bisect import bisect_left, bisect_right

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N, x = map(int, input().split())
arr = list(map(int, input().split()))

def bi_left(arr, x):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            if mid == 0 or arr[mid-1] < x:
                return mid
            else:
                right = mid - 1
    return -1


def bi_right(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            if mid == len(arr)-1 or arr[mid + 1] > x:
                return mid
            else:
                left = mid + 1
    return -1

a = bi_left(arr, x)
b = bi_right(arr, x)
result = b - a
if result == 0:
    print(-1)
else:
    print(result)