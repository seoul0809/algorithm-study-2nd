# 세 용액

# 메모리: 114488KB, 시간: 156ms
# 투포인터
# 참고: https://velog.io/@nkw011/baekjoon-2473

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
inputs = list(map(int, input().split()))
inputs.sort()

first, second, third = 0, 0, 0
result = float('inf')
for i in range(N-2):
    lo, hi = i+1, N-1
    while lo < hi:
        temp = inputs[i] + inputs[lo] + inputs[hi]
        if abs(temp) < result:
            result = abs(temp)
            first, second, third = inputs[i], inputs[lo], inputs[hi]
            if temp == 0:
                print(first, second, third)
                exit(0)
        if temp < 0:
            lo += 1
        else:
            hi -= 1

print(first, second, third)