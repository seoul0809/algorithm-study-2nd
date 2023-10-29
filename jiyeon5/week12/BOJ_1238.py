import heapq
INF=int(1e9)
n,m,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,t=map(int,input().split())
    graph[a].append((b,t))
distances=[[INF]*(n+1) for _ in range(n+1)]
def dijkstra(start,distance):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist, now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for b,t in graph[now]:
            cost=dist+t
            if cost<distance[b]:
                distance[b]=cost
                heapq.heappush(q,(cost,b))


answer=-1
for i in range(1,n+1):
    dijkstra(i,distances[i])
for i in range(1,n+1):
    answer=max(answer,distances[i][x]+distances[x][i])
print(answer)