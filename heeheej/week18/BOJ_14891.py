# 톱니바퀴
# 114432kb, 140ms
# 주의 1: 회전시킬 방향 결정은 톱니바퀴 하나가 돌아가고 그 다음 맞닿은 극을 파악하는 게 아니라
# 회전하기 전 원래 상태 기준으로 극이 같은지 판별해야 한다.

import pprint
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

FRONT, REAR = 6, 2

arr = [deque(map(int, input().rstrip())) for _ in range(4)] # 큐 하나 당 톱니바퀴 하나
N = int(input())
for _ in range(N):
    k, d = map(int, input().split())
    k -= 1  # 인덱스 조정
    fronts = [arr[i][FRONT] for i in range(4)]
    rears = [arr[i][REAR] for i in range(4)]

    arr[k].rotate(d)   # 현재 톱니바퀴 먼저 회전
    nk, nd = k, d  # 초기화
    while nk > 0:   # 왼쪽방향 먼저 확인
        if rears[nk-1] == fronts[nk]:
            break
        nd *= -1    # 방향 반대
        nk -= 1     # 왼쪽 톱니바퀴로 이동
        arr[nk].rotate(nd)
    nk, nd = k, d  # 초기화

    while nk < 3:   # 오른쪽 방향 확인
        if rears[nk] == fronts[nk+1]:
            break
        nd *= -1
        nk += 1
        arr[nk].rotate(nd)

result = 0
for i in range(4):
    x = arr[i][0]
    if x == 1:  # S극이라면
        result += 2**i
print(result)