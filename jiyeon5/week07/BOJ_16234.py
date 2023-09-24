from collections import deque

n,l,r=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
day=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y,index):
    units=[]
    units.append((x,y))
    q=deque([(x,y)])
    visited[x][y]=index
    sum=graph[x][y]
    count=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1:
                if l<=abs(graph[nx][ny]-graph[x][y])<=r:
                    q.append((nx,ny))
                    visited[nx][ny]=index
                    sum+=graph[nx][ny]
                    count+=1
                    units.append((nx,ny))

    for i,j in units:
        graph[i][j]=sum//count

while True:
    visited=[[-1]*n for _ in range(n)]
    index=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==-1:
                bfs(i,j,index)
                index+=1

    if index==n*n:
        break
    day+=1

print(day)