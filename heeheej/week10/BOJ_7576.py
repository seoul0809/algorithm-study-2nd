import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]

cnt = 0 # 익지 않은 토마토 개수
queue = deque()

def printArray():
    for k in range(N):
        print(_map[k])
    print(f"cnt: {cnt}")
def bfs():
    global cnt
    day = -1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or _map[nx][ny] != 0:
                continue
            _map[nx][ny] = _map[x][y] + 1
            cnt -= 1
            queue.append((nx, ny))
            day = max(day, _map[nx][ny])
            if cnt <= 0:
                return day-1
        # printArray()
    return -1
for i in range(N):
    for j in range(M):
        if _map[i][j] == 0:
            cnt += 1
        elif _map[i][j] == 1:
            queue.append((i, j))
if cnt == 0:
    print(0)
else:
    print(bfs())