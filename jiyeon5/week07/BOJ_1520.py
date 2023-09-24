import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
dp=[[-1]*m for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(x,y):

    # 목적지에 도착했으면 1을 리턴하여 목적지까지 이동한 칸 모든 칸에 +1
    if x == n-1 and y == m-1:
        return 1

    if dp[x][y]==-1:
        dp[x][y]=0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[x][y]>arr[nx][ny]:
                    dp[x][y]+=dfs(nx,ny)

    return dp[x][y]

print(dfs(0,0))