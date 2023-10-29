import heapq
INF=(int(1e9))
n,e=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2=map(int,input().split())

def dijkstra(start):
    q=[]
    distance=[INF]*(n+1)
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)
        if dist> distance[now]:
            continue
        for b,c in graph[now]:
            cost=dist+c
            if cost<distance[b]:
                distance[b]=cost
                heapq.heappush(q,(cost,b))

    return distance

one_dist=dijkstra(1)
v1_dist=dijkstra(v1)
v2_dist=dijkstra(v2)

ans1=one_dist[v1]+v1_dist[v2]+v2_dist[n]
ans2=one_dist[v2]+v2_dist[v1]+v1_dist[n]
answer=min(ans1,ans2)
if answer>=INF:
    print(-1)
else:
    print(answer)