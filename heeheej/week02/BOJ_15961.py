# 회전 초밥
# 슬라이딩 윈도우
# 964ms, 215580kb

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
inputs = [int(input()) for _ in range(N)]

sushi = dict()  # key: 초밥 종류, value: 해당 종류 초밥의 개수
                # len(sushi)가 곧 초밥의 가짓수가 된다.
sushi[c] = 1    # 보너스 초밥을 무조건 먼저 먹고 시작한다.
init = inputs[:k]
for x in init:    # 0부터 k-1번째 초밥에 대해 dict에 담기
    if x not in sushi:
        sushi[x] = 1
    else:
        sushi[x] += 1

inputs = inputs + inputs
result = len(sushi) # 초밥의 가짓수 초기값
for i in range(k, k+N-1):   # i는 윈도우의 마지막 원소!
    # 이전 윈도우의 첫번쨰 원소 빼주기
    sushi[inputs[i-k]] -= 1
    if sushi[inputs[i-k]] == 0:
        del sushi[inputs[i-k]]

    nextX = inputs[i]
    if nextX not in sushi:
        sushi[nextX] = 1
    else:
        sushi[nextX] += 1

    result = max(result, len(sushi))

print(result)