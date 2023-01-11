# 용액

# 메모리: 128124KB, 시간: 172ms
# 특성값은 정렬되어있다!
# 이진탐색

import sys

sys.stdin = open("input.txt", "r", encoding = "UTF-8")
input = sys.stdin.readline

N = int(input())
inputs = list(map(int, input().split()))

minSum = float('inf')   # 두 용액의 합 중 최솟값
resLo, resHi = 0, N-1

for i in range(N-1):
    target = inputs[i]
    lo, hi = i+1, N-1

    while lo <= hi:
        mid = (lo + hi) // 2
        temp = inputs[i] + inputs[mid]
        # print(f"i: {i}, lo: {lo}, hi: {hi}, mid: {mid}, temp: {temp}, inputs[i]: {inputs[i]}, inputs[mid]: {inputs[mid]}")
        if abs(temp) < minSum:
            resLo, resHi = i, mid
            minSum = abs(temp)
            # print(f"minSum: {minSum}")
            if temp == 0:
                break
        if temp < 0:
            lo = mid+1
        else:
            hi = mid-1

print(inputs[resLo], inputs[resHi])