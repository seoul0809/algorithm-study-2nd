# 청소년 상어
# 117352kb, 228ms
# 2차원 배열 복사할 때 쓰는 [row[:] for row in _map]를 습관적으로 썼는데,
# fishMap은 3차원 배열이라서 다른 값이 나온다.. 그냥 import copy, copy.deepcopy(arr) 로 가자

import pprint
import sys
import copy
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

fishMap = [[0]*4 for _ in range(4)]
result = 0
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        fishMap[i][j] = [temp[j*2], temp[j*2+1]]

def getPositionByFishNum(n, _map):
    for i in range(4):
        for j in range(4):
            if _map[i][j][0] == n:
                return i, j
    return -1, -1

def swap(nx, ny, fDir, n, _map):
    # n을 A, 이동할 위치에 있는 물고기를 B라 하자.
    # nx, ny: n번 물고기가 이동할 다음 위치 (기존 B의 위치)
    # fDir: n번 물고기의 방향

    if _map[nx][ny][0] == 0:  # 이동할 위치에 물고기가 존재하지 않을 때
        _map[nx][ny] = [n, fDir]
    else:
        ax, ay = getPositionByFishNum(n, _map)
        _map[ax][ay] = _map[nx][ny] # a의 위치에 b를 넣는다
        _map[nx][ny] = [n, fDir] # b의 위치에 a를 넣는다

def dfs(x, y, total, _map):
    # 종료조건 처리를 여기서 말고 아래에서 해주니까 테케 통과
    # if x < 0 or y < 0 or x >= 4 or y >= 4 or _map[x][y][0] == 0:
    #     global result
    #     print(f"result: {result}, total: {total}")
    #     result = max(result, total)
    #     return

    eatFish = _map[x][y][0] # 먹을 물고기 번호
    totalAdd = total + eatFish
    # 물고기 있으면 먹기
    nextDir = _map[x][y][1] # 상어 방향 변경
    _map[x][y][0] = 0   # 물고기 먹은걸로 처리

    for k in range(1, 17):
        fx, fy = getPositionByFishNum(k, _map)
        if fx == -1 and fy == -1: # 해당 번호의 물고기가 먹혔으면
            continue
        # 물고기 이동
        fDir = _map[fx][fy][1]
        for _ in range(8):
            nx = fx + dx[fDir]
            ny = fy + dy[fDir]
            if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                if not (nx, ny) == (x, y):  # 이동 가능하면 물고기 이동시키고 반복 종료
                    _map[fx][fy][1] = fDir
                    _map[fx][fy], _map[nx][ny] = _map[nx][ny], _map[fx][fy]
                    break
            # 이동 불가능하면 방향 이동
            fDir = fDir % 8 + 1  # 방향 이동
    # 상어 이동
    nx, ny = x, y
    while True:
        nx += dx[nextDir]
        ny += dy[nextDir]

        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            global result
            result = max(result, totalAdd)
            return
        if _map[nx][ny][0] > 0:
            newMap = copy.deepcopy(_map)
            # newMap = [row[:] for row in _map] # _map은 3차원 배열이라서 결과가 다르게 나옴!!
            dfs(nx, ny, totalAdd, newMap)

dfs(0, 0, 0, fishMap)
print(result)