# 뱀 (BOJ 3190)
# 116652kb, 164ms
# dfs -> RecursionError
# for문으로 고쳐서 성공

import sys
from collections import deque

def printArray(arr):
    for i in range(len(arr)):
        print(arr[i])

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
K = int(input())
_map = [[False]*(N+1) for _ in range(N+1)]    # 사과가 있으면 True
input1 = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())
queue2 = deque([tuple(input().split()) for _ in range(L)])

for a, b in input1:
    _map[a][b] = True

dx = [0, 1, 0, -1]
dy = [1, 0 , -1, 0]

def getDirection(nowDir, C):
    if C == 'L':    # 왼쪽
        nextDir = nowDir - 1
    else:   # 오른쪽
        nextDir = (nowDir + 1) % 4
    if nextDir == -1:
        nextDir = 3
    return nextDir

queue = deque()
queue.append((1, 1))
result = -1
time = 0
nx, ny = 1, 1
nextDir = 0
while True:
    if queue2 and time == int(queue2[0][0]):
        t, nextDirChar = queue2.popleft()
        nextDir = getDirection(nextDir, nextDirChar)

    nx += dx[nextDir]
    ny += dy[nextDir]
    if nx <= 0 or ny <= 0 or nx > N or ny > N or (nx, ny) in queue:
        result = time + 1
        break

    queue.append((nx, ny))
    if _map[nx][ny]:
        _map[nx][ny] = False
    else:
        queue.popleft()  # 꼬리 자르기
    time += 1

print(result)