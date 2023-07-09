# 특정 거리의 도시 찾기
# LCT A15 & BOJ 18352
# 예전에는 다익스트라로 풀었었는데 이번에는 BFS로 풀어봄
# 112ms, 160652kb
# 시작 도시를 방문처리 안해주는 실수함.. 주의하자

import sys
from collections import deque
import pprint

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)

result = list()

queue = deque()
queue.append(X)
visited = [-1]*(N+1)
visited[X] = 0
while queue:
    now = queue.popleft()
    for next in adj[now]:
        if visited[next] == -1:
            queue.append(next)
            visited[next] = visited[now] + 1
            if visited[next] == K:
                result.append(next)
        # pprint.pprint(locals())

result.sort()
if not result:
    result.append(-1)

for x in result:
    print(x)