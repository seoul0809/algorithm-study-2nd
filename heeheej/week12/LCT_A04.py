# 만들 수 없는 금액

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1
for x in arr:
    if x > target:
        break
    target += x
print(target)