# 현수막
# 117580kb, 188ms
# bfs

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]
visited = [[False]*N for _ in range(M)]

def bfs(x, y):
    global visited
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N or visited[nx][ny] or board[nx][ny] == 0:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True

result = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            result += 1
print(result)