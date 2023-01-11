# 공유기 설치

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, C = map(int, input().split())
pos = [int(input()) for _ in range(N)]
pos.sort()

lo, hi = 1, pos[-1]-pos[0]
result = -1

while lo <= hi:
    mid = (lo + hi) // 2
    current = pos[0]
    count = 1
    for i in range(N):
        if pos[i]-current >= mid:
            current = pos[i]
            count += 1

    if count >= C:
        lo = mid + 1
        result = mid
    else:
        hi = mid - 1

print(result)