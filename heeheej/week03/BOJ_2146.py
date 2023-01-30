# 다리 만들기
# bfs1: 각 섬을 구분하기 위해 각 섬 내에서 bfs하고 visited배열에 각 섬을 섬번호로 구분하여 표시
# bfs2: 특정 섬에서 나머지 다른 섬들로 이동하는 거리 중 최단거리를 구하기 위한 bfs, 이 때 출발섬이 아닌 섬에 도착했는지 체크해야한다.
# 344ms, 120356kb

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
_map = [list(map(int, input().split())) for _ in range(N)]
cnt = 1 # 섬 번호

def bfs1(sx, sy):
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = cnt # 섬 번호를 방문배열의 원소로 넣기!

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] != 0:
                continue
            if _map[nx][ny] == 1:
                visited[nx][ny] = cnt
                queue.append((nx, ny))

def bfs2():
    queue = deque()
    dist = [[-1]*N for _ in range(N)]   # 특정 섬에서 다른 섬으로 가는 이동하는데, 각 좌표에 현재까지 이동거리를 표시하며 나아간다.
    global result

    for i in range(N):
        for j in range(N):
            if visited[i][j] == cnt:
                queue.append((i, j))
                dist[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or dist[nx][ny] != -1:
                continue
            if visited[nx][ny] > 0 and not visited[nx][ny] == cnt:  # 다른 섬에 도착하면, 최솟값을 비교하여 더 최솟값이 나왔을 경우 갱신해준다.
                result = min(result, dist[x][y])
                return
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

result = float('inf')
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if _map[i][j] == 1 and visited[i][j] == 0:
            bfs1(i, j)
            cnt += 1

islandCnt = cnt - 1 # 총 섬의 개수
cnt = 1 # 첫번쨰 섬부터 bfs2를 시작한다!
for i in range(N):
    for j in range(N):
        if visited[i][j] == cnt:
            bfs2()
            cnt += 1

print(result)