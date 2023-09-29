# 정렬된 배열에서 특정 수의 개수 구하기
# 이진탐색, bisect 라이브러리
# bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

import sys
from bisect import bisect_left, bisect_right

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N, x = map(int, input().split())
arr = list(map(int, input().split()))

a = bisect_left(arr, x)
b = bisect_right(arr, x)
result = b - a
if result == 0:
    print(-1)
else:
    print(result)