# 연구소 2
# 117392kb, 228ms
# bfs, 빈칸이 없는 경우 예외처리

import sys
from itertools import combinations
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
board = []
available = []
wall_cnt = 0
for i in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)
    for j in range(N):
        if temp[j] == 2:
            available.append((i, j))
            board[i][j] = 0
        elif temp[j] == 1:
            wall_cnt += 1
            board[i][j] = -1

blank_cnt = N*N - wall_cnt - M
if blank_cnt == 0:
    print(0)
    sys.exit()
def bfs(arr, new_board):
    queue = deque(arr)
    for x, y in arr:
        new_board[x][y] = 1

    cnt = blank_cnt
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or new_board[nx][ny] != 0:
                continue
            queue.append((nx, ny))
            new_board[nx][ny] = new_board[x][y] + 1
            cnt -= 1
            if cnt == 0:
                return True
    else:
        return False

result = float('inf')
flag = False    # 모든 빈칸에 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없을 때 False
combs = combinations(available, M)
for comb in combs:
    new_board = [row[:] for row in board]
    if bfs(comb, new_board):
        time = 0
        for i in range(N):
            for j in range(N):
                time = max(time, new_board[i][j])
        result = min(result, time)
        flag = True
if flag:
    print(result - 1)
else:
    print(-1)