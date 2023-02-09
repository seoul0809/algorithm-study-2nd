# 소문난 칠공주
# 576ms, 118036kb
# 5x5 배열에서 (x, y) 좌표(자리)를 7개 선택하는 조합을 만든다.
# 각 조합마다, bfs를 돌려 자리가 이어져있는지 확인한다.
# 이어져있는지 확인함과 동시에, 이어져있는 자리의 수를 cnt변수에 저장, 이다솜파인 학생의 수를 sCnt변수에 저장한다.
# cnt가 7이 되면, 이다솜파가 4명이상인지 확인하여 맞으면 true, 아니면 false를 리턴한다.
# 그 외 경우엔 false를 리턴한다.

import sys
from itertools import combinations
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

_map = [list(input().rstrip()) for _ in range(5)]
arr = list()

def bfs(arr):
    queue = deque()
    startX, startY = arr[0][0], arr[0][1]
    queue.append((startX, startY))
    isVisited[startX][startY] = True
    cnt, sCnt = 1, 0
    if _map[startX][startY] == 'S':
        sCnt += 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or isVisited[nx][ny]:
                continue
            if (nx, ny) not in arr:
                continue
            else:
                cnt += 1
            if _map[nx][ny] == 'S':
                sCnt += 1
            queue.append((nx, ny))
            isVisited[nx][ny] = True

            if cnt == 7:
                if sCnt >= 4:
                    return True
                else:
                    return False
    return False

for i in range(5):
    for j in range(5):
        arr.append((i, j))

combs = combinations(arr, 7)
result = 0
for comb in combs:
    isVisited = [[False] * 5 for _ in range(5)]
    if bfs(comb):
        result += 1
print(result)

