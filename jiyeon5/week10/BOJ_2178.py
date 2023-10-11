from collections import deque

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

q=deque([(0,0)])
while q:
    x,y=q.popleft()

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]==1 and not (nx==0 and ny==0):
                q.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1

print(graph[n-1][m-1])