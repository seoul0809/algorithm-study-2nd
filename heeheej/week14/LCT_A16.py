# 연구소
# 120332kb, 416ms
# bfs
# 1. 2차원 배열 입력받으면서 빈칸(0)인 곳 좌표를 blanks 리스트에 추가,
# 바이러스 있는 곳 좌표를 virus 리스트에 추가
# 2. blanks에서 3개 골라 1로 변경
# 3. 각 virus를 시작으로 bfs 돌린다.
# 4. 빈칸의 개수를 구한다 => 안전구역 개수

import sys
from collections import deque
from itertools import combinations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

blank = list()
virus = list()
_map = [[] for _ in range(N)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    temp[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if temp[nx][ny] != 0:
                continue
            queue.append((nx, ny))
            temp[nx][ny] = 1

for i in range(N):
    arr = list(map(int, input().split()))
    _map[i] = arr
    for j in range(M):
        if arr[j] == 0:
            blank.append((i, j))
        elif arr[j] == 2:
            virus.append((i, j))
result = -1
combs = list(combinations(blank, 3))
for comb in combs:
    temp = [row[:] for row in _map]
    # 벽 3개 세우기
    for i, j in comb:
        temp[i][j] = 1

    for i, j in virus:
        bfs(i, j)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                cnt += 1

    result = max(result, cnt)

print(result)