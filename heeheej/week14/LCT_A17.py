# 경쟁적 전염 (BOJ 18405)
# 118264kb, 284ms
# bfs
# N<K인 경우도 존재하기 때문에 arr의 행의 개수는 (N+1)개가 아니라 (K+1)개여야 한다.

import pprint
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, K = map(int, input().split())
_map = [[0]*(N+1) for _ in range(N+1)]
arr = [deque() for _ in range(K+1)]
for i in range(1, N+1):
    temp = list(map(int, input().split()))
    for j in range(1, N+1):
        if temp[j-1] != 0:
            _map[i][j] = temp[j-1]
            arr[temp[j-1]].append((i, j))

S, X, Y = map(int, input().split())
for s in range(S):
    for k in range(1, K+1):
        length = len(arr[k])
        while length > 0:
            queue = arr[k]
            x, y = queue.popleft()
            length -= 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 1 or ny < 1 or nx > N or ny > N or _map[nx][ny] != 0:
                    continue
                queue.append((nx, ny))
                _map[nx][ny] = k

print(_map[X][Y])