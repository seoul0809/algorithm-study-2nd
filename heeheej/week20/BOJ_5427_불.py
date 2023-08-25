# 불
# 229112kb, 872ms
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
T = int(input())

def fire_bfs(q):
    for _ in range(len(q)):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= H or ny >= W or board[nx][ny] != '.':
                continue
            q.append((nx, ny))
            board[nx][ny] = '*'

def move_bfs(q):
    is_moved = False
    for _ in range(len(q)):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= H or ny >= W:
                return visited[x][y] + 1
            if visited[nx][ny] != -1 or board[nx][ny] != '.':
                continue
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
            is_moved = True
    if not is_moved:
        return "IMPOSSIBLE"

for _ in range(T):
    W, H = map(int, input().split())
    board = list()
    queue = deque() # 상근이 이동 bfs에서 쓰는 큐
    fires = deque()      # 불의 위치들이 담긴 리스트
    visited = [[-1]*W for _ in range(H)]
    for i in range(H):
        temp = list(input().rstrip())
        for j in range(W):
            if temp[j] == '*':
                fires.append((i, j))
            elif temp[j] == '@':
                queue.append((i, j))
                temp[j] = '.'   # 빈공간으로 바꿔준다.
                visited[i][j] = 0
        board.append(temp)

    while True:
        fire_bfs(fires)
        result = move_bfs(queue)
        if result:
            print(result)
            break
