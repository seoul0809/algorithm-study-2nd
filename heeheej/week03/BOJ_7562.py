# 나이트의 이동
# bfs
# 이동 횟수를 visited 배열의 원소로 저장한다.

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [2, 1, -2, -1, 2, 1, -2, -1]
dy = [1, 2, 1, 2, -1, -2, -1, -2]

def bfs(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1))
    result = float('inf')
    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2:
            result = min(result, visited[x][y])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l or visited[nx][ny] != 0:
                continue

            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
    return result
T = int(input())
for _ in range(T):
    l = int(input())
    srcX, srcY = map(int, input().split())
    dstX, dstY = map(int, input().split())

    visited = [[0]*l for _ in range(l)]
    print(bfs(srcX, srcY, dstX, dstY))
