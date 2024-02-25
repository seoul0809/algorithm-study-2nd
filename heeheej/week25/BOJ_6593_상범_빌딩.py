# 상범 빌딩
# 118008kb, 204ms
# 3차원 배열에 대해 bfs 돌린다.

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]

def bfs(sPos):
    x, y, z = sPos
    visited = [[[-1]*C for _ in range(R)] for _ in range(L)]
    q = deque()
    q.append((x, y, z))
    visited[x][y][z] = 0

    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= L or ny < 0 or ny >= R or nz < 0 or nz >= C or visited[nx][ny][nz] != -1:
                continue
            elif (nx, ny, nz) == ePos:
                return visited[x][y][z] + 1
            elif board[nx][ny][nz] == '#':
                continue
            
            q.append((nx, ny, nz))
            visited[nx][ny][nz] = visited[x][y][z] + 1
    return -1

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:    # 입력의 끝 (탈출조건)
        break
    sPos, ePos = (-1, -1, -1), (-1, -1, -1)
    
    board = []
    for i in range(L):
        temp = []
        for j in range(R):
            line = list(input().rstrip())
            temp.append(line)
            for k, x in enumerate(line):
                if x == 'S':
                    sPos = (i, j, k)
                elif x == 'E':
                    ePos = (i, j, k)
        board.append(temp)
        input()
    
    result = bfs(sPos)
    if result == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {result} minute(s).")
    
