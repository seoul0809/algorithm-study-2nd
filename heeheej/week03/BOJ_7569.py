# 토마토
# 940ms, 227132kb
# 3차원 bfs!
# 2차원 bfs를 주로 풀었는데, 3차원으로 푸니까 재미있었다.
# 자꾸 dx, dy, dz에서 오타를 내서 오답을 낸다.. 주의하자! ㅜㅜ
# 방문 배열의 원소로 해당 좌표의 토마토가 익는데 며칠 걸렸는지 저장한다!
# cnt변수에 익지 않은 토마토 개수를 세어 저장하고,
# 익지 않은 토마토가 익을 때 cnt를 하나씩 줄였다.
# cnt가 0이 될 때 == 모든 토마토가 익었을 때 이므로 그 때 걸린 일수를 return해주었다.

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split())
tomatoes = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]

def bfs():
    cnt = 0 # 익지 않은 토마토 개수
    queue = deque()
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatoes[h][n][m] == 1:  # 익은 토마토는 큐에 넣는다. 방문 체크도 해준다.
                    queue.append((h, n, m))
                    visited[h][n][m] = 0
                elif tomatoes[h][n][m] == 0:    # 익지 않은 토마토라면, cnt를 1 증가시킴
                    cnt += 1
    if cnt == 0:
        return 0
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M \
                    or visited[nx][ny][nz] != -1:
                continue

            if tomatoes[nx][ny][nz] == 0:   # 익지 않은 토마토일때만 전진하여 토마토를 익게 처리한다!
                visited[nx][ny][nz] = visited[x][y][z] + 1  # 이전까지 걸린 일수 + 1 해준다.
                queue.append((nx, ny, nz))
                cnt -= 1
                if cnt == 0:    # 전진해서 모든 토마토가 익게된 경우, 걸린 일수를 바로 return한다!
                    return visited[nx][ny][nz]
    return -1

visited = [list([-1]*M for _ in range(N)) for _ in range(H)]    # 방문체크배열이고, 원소로 해당 좌표까지 며칠 걸렸는지 저장한다.

print(bfs())