# 컨베이어 벨트 위의 로봇
# 120124kb, 708ms
# 구현 문제
# 처음엔 벨트를 [[내구도, 로봇이 있는지 여부], [내구도, 로봇이 있는지 여부] ...] 이런식으로 int, bool 2차원리스트 형태로 만들었는데,
# 내구도 따로 로봇여부 따로 해서 2개의 queue를 만들면 속도가 약 2배 빨라진다. (1420 -> 708ms)

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N, K = map(int, input().split())
belt = deque(map(int, input().split()))
isRobot = deque([False]*2*N)

def move_robots(belt, isRobot):
    for i in range(N-1, -1, -1):
        if isRobot[i] and (not isRobot[i+1] and belt[i+1] >= 1):
            isRobot[i] = False
            belt[i+1] -= 1
            if i + 1 != N - 1:
                isRobot[i+1] = True

def check_stop_condition(belt):
    cnt = 0
    for x in belt:
        if x == 0:
            cnt += 1
            if cnt >= K:
                return True
    else:
        return False

answer = 0
while True:
    answer += 1
    belt.rotate()
    isRobot.rotate()
    if isRobot[N-1]:    # 내리는 위치에 도달한 로봇 있으면 내린다
        isRobot[N-1] = False

    move_robots(belt, isRobot)
    if belt[0] != 0: # 올리는 위치에 내구도 1 이상이면 로봇 올린다
        belt[0] -= 1
        isRobot[0] = True
    
    if check_stop_condition(belt):
        break
print(answer)