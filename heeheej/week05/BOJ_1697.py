# 숨바꼭질
# 160ms, 117712kb
# bfs 이용

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

visited = [0]*100001

N, K = map(int, input().split())

queue = deque()
queue.append(N)

while queue:
    x = queue.popleft()

    if x == K:
        print(visited[x])
        break

    for nx in [x-1, x+1, x*2]:
        if 0 <= nx <= 100000 and visited[nx] == 0:
            visited[nx] = visited[x] + 1
            queue.append(nx)