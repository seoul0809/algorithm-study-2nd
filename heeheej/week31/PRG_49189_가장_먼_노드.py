# 가장 먼 노드
# 프로그래머스 코딩테스트 고득점 kit > 그래프
# 다익스트라 이용해서 1번 노드로부터 다른 모든 노드까지의 최단거리 구하고, INF를 제외한 최대값 찾아서 그 개수를 구한다.
# 1287 (+7)

import heapq

def dijkstra(start, distance, graph):
    
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    M = -1   # 1번 노드에서 가장 멀리 떨어진 노드까지의 거리
    
    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue
        
        for nxt in graph[now]:
            cost = dis + 1
            if cost < distance[nxt]:
                heapq.heappush(q, (cost, nxt))
                distance[nxt] = cost
                M = max(M, cost)
                # print(q, distance)
    return M
    
def solution(n, edge):
    answer = 0
    
    INF = int(1e9)
    distance = [INF]*(n+1)
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    M = dijkstra(1, distance, graph)
    answer = distance.count(M)
    return answer