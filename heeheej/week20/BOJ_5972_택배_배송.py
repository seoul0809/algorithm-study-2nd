# 택배 배송
# 126072kb, 352ms
# 다익스트라 (양방향 간선)

import sys
import heapq

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(1)

print(distance[N])