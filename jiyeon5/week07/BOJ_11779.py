import heapq
INF=int(1e9)

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

start,destination=map(int,input().split())

q=[]
heapq.heappush(q,(0,[start]))
distance[start]=0
new_routes=[]

while q:
    dist,routes=heapq.heappop(q)
    now=routes[-1]
    if distance[now]<dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            new_route = routes + [i[0]]
            heapq.heappush(q, (cost, new_route))
            if i[0] == destination:
                save = new_route

if start == destination:
    print(0)
    print(start)
    print(start)
else:
    print(distance[destination])
    print(len(save))
    for s in save:
        print(s, end=' ')
