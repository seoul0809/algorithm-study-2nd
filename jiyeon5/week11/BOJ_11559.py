from collections import deque
import copy
puyo=[]

for _ in range(12):
    puyo.append(list(input()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bomb(graph,visited,x,y,color):
    q=deque([(x,y)])
    graph[x][y]='.'
    visited[x][y]=True
    cnt=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<12 and 0<=ny<6:
                if graph[nx][ny]==color:
                    q.append((nx,ny))
                    graph[nx][ny]='.'
                    cnt+=1
                    visited[nx][ny]=True

    if cnt>=4:
        return True #그대로
    else:
        return False #origin 사용

def down(graph,x,y):
    origin=graph[x][y]
    q=deque([(x,y)])
    graph[x][y]='.'

    while q:
        x,y=q.popleft()
        nx=x+1
        if 0<=nx<12 and graph[nx][y]=='.':
            q.append((nx,y))
            graph[x][y]='.'
    graph[x][y]=origin

cnt=0
flag=True
while flag:
    flag=False
    visited=[[False]*6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if puyo[i][j]!='.' and not visited[i][j]:
                origin=copy.deepcopy(puyo)
                tmp=bomb(puyo,visited,i,j,puyo[i][j])
                if tmp:
                    flag=True
                else:
                    puyo=origin

    for i in range(10,-1,-1):
        for j in range(6):
            if puyo[i][j]!='.':
                down(puyo,i,j)
    if flag: cnt+=1
print(cnt)