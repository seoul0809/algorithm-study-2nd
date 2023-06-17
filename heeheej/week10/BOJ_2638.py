# 치즈(골드3)
# https://www.acmicpc.net/problem/2638
# 125444kb, 480ms

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]

# 외부 공기를 -1로 바꾼다.
# 모눈종이의 맨 가장자리에는 치즈가 놓이지 않으므로, (0, 0)부터 bfs를 돌린다.
def fillOuterAir():
    queue = deque()
    queue.append((0, 0))
    _map[0][0] = -1
    visited2 = [[False] * M for _ in range(N)]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M or _map[nx][ny] == 1:
                continue
            if visited2[nx][ny]:
                continue
            _map[nx][ny] = -1
            queue.append((nx, ny))
            visited2[nx][ny] = True

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        touched = 0 # 외부공기와 닿은 변 개수
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if _map[nx][ny] == -1: # 외부 공기 닿았는지 체크
                touched += 1
            if not visited[nx][ny] and _map[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
        if touched >= 2 and (x, y) not in removeList:
            removeList.append((x, y))
fillOuterAir()

# 치즈의 개수 세기
cnt = 0
for i in range(1, N-1):
    for j in range(1, M-1):
        if _map[i][j] == 1:
            cnt += 1

time = 0
while cnt > 0:
    time += 1
    removeList = list()
    visited = [[False] * M for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if _map[i][j] == 1: # 치즈라면
                bfs(i, j)
    for x, y in removeList: # C로 표시된 모든 치즈 격자를 외부 공기로 바꾸기
        _map[x][y] = -1
        cnt -= 1
    fillOuterAir()
print(time)