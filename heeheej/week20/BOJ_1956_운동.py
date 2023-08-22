# 운동
# 117628kb, 1168ms
# 플로이드 워셜
# 단방향 그래프이므로
# a -> b -> a 사이클의 최소 도로 길이 == a -> b의 최소 도로 길이 + b -> a의 최소 도로 길이


import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float('inf')
v, e = map(int, input().split())
graph = [[INF]*(v+1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, v+1):
    graph[i][i] = 0

for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = INF
for i in range(1, v+1):
    for j in range(1, v+1):
        if i == j:
            continue
        if graph[i][j] != INF and graph[j][i] != INF:
            result = min(result, graph[i][j] + graph[j][i])

if result == INF:
    print(-1)
else:
    print(result)