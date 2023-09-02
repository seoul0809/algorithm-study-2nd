# 럭키 스트레이트
# 113112kb, 108ms

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

str = list(input().rstrip())
arr = []
for x in str:
    arr.append(int(x))
half = len(str) // 2
if sum(arr[:half]) == sum(arr[half:]):
    print("LUCKY")
else:
    print("READY")