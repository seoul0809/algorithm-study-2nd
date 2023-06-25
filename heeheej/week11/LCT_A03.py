# 문자열 뒤집기
# 0에서 1로 뒤집히는 횟수와 1에서 0으로 뒤집히는 횟수를 세서,
# 더 작은 수를 답으로 출력

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

S = list(input().rstrip())
N = len(S)
cnt1, cnt2 = 0, 0   # cnt1: 0 -> 1 가는 경우, cnt2: 1 ->0
for i in range(N):
    x = int(S[i])

    if i == N-1:    # 마지막 숫자의 경우 따로 처리
        if x == 0:
            cnt1 += 1
        elif y == 1:
            cnt2 += 1
        break

    y = int(S[i+1])

    if x == 0 and y == 1:
        cnt1 += 1
    elif x == 1 and y == 0:
        cnt2 += 1
print(min(cnt1, cnt2))