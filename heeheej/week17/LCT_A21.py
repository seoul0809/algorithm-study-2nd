# 인구 이동 (BOJ 16234)
# 131856kb, 1580ms
# bfs 이용, bfs 한번 끝날 때 인구 이동시킨다.

import pprint
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
result = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    population = arr[x][y]
    cnt = 1
    unionList = list()
    unionList.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny]:
                continue

            val = abs(arr[x][y] - arr[nx][ny])
            if L <= val <= R:
                queue.append((nx, ny))
                unionList.append((nx, ny))
                population += arr[nx][ny]
                cnt += 1
                visited[nx][ny] = True
    newPopulation = population // cnt
    for i, j in unionList:
        arr[i][j] = newPopulation

    if cnt != 1:    # 국경선 열기 (인구이동 한번이라도 O)
        global flag
        flag = True

def check():
    global visited
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)

while True:
    flag = False # 인구이동여부
    check()
    if flag:
        result += 1
    else:
        break

print(result)