# 게임 맵 최단거리
# 백준 환경에서는 잘 안헷갈리는데 x축 y축을 혼동해버렸다. 왜지? 자알 생각하고 풀자.

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])  # 이거 헷갈리면 안돼...
    queue = deque()
    queue.append((0, 0))
    visited = [[-1] * M for _ in range(N)]  # 얘도....
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] != -1 or maps[nx][ny] == 0:
                continue
            if nx == N - 1 and ny == M - 1:
                return visited[x][y] + 1
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
    return -1