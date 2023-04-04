# 적록색약
# 117312kb, 196ms
# bfs
# 적록색약인 경우와 아닌 경우 나눠서 bfs를 짤 경우 중복되는 코드가 많아져서 그에 대한 고민이 필요했다.
# 적록색약인 경우를 위해 'G'를 'R'로 바꾼 2차원배열을 하나 더 만들어주고,
# firstColor, 배열, 방문배열을 파라미터로 넘기는 방식으로 중복되는 코드를 줄여보았다.

import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N = int(input())
_map = [list(input().rstrip()) for _ in range(N)]
newMap = [row[:] for row in _map]

# newMap에서는 녹색을 그냥 빨간색 취급하도록 한다.
for i in range(N):
    for j in range(N):
        if newMap[i][j] == 'G':
            newMap[i][j] = 'R'

visited1 = [[False]*N for _ in range(N)]    # 색약인 사람의 경우
visited2 = [[False]*N for _ in range(N)]    # 색약이 아닌 사람의 경우
cnt1, cnt2 = 0, 0   # cnt1: 색약인 경우, cnt2: 아닌 경우

def bfs(i, j, firstColor, arr, visited):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny] or arr[nx][ny] != firstColor:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            bfs(i, j, _map[i][j], _map, visited1)
            cnt1 += 1
        if not visited2[i][j]:
            bfs(i, j, newMap[i][j], newMap, visited2)
            cnt2 += 1

print(cnt1, cnt2)