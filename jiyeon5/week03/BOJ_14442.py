'''
푼 시간 : 108분
성능 : 메모리 339564KB, 시간 3916ms
주의할 점 :
    방문 체크를 위한 3차원 배열 [높이][세로][가로] : visited = [[[0]*가로 for _ in range(세로)] for _ in range(높이)]
    입출력 많을 땐 input = sys.stdin.readline, 사용할 때 마지막글자에 공백을 제거해줘야함 input().rstrip()
    3차원 배열을 사용해서 벽을 부순 횟수를 담고 방문처리
'''

from collections import deque
import sys
input = sys.stdin.readline

# n, m, k 입력받기
n, m, k = map(int, input().split())
# 맵 입력받기
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

# 이동할 수 있는 방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 방문 체크를 위한 3차원 배열 [벽부순횟수][세로][가로]
visited = [[[0]*m for _ in range(n)] for _ in range(k+1)]

# bfs 탐색
def bfs(x,y):
    queue = deque([(x,y,0)])
    visited[0][x][y] = 1

    while queue:
        x,y,wall = queue.popleft() # 세로, 가로, 벽 부순 횟수

        # 도착해야할 칸일경우 이동횟수를 반환
        if x==n-1 and y==m-1:
            return visited[wall][x][y]

        # 4방향을 돌면서 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵의 범위 안에 있을 때만 이동
            if 0<=nx<n and 0<=ny<m and visited[wall][nx][ny] == 0:
                # 이동할 수 있는 곳이고 방문한 적 없을 경우 이동
                if arr[nx][ny] == 0 and visited[wall][nx][ny] == 0:
                    visited[wall][nx][ny] = visited[wall][x][y] + 1 # 이동횟수+1
                    queue.append((nx,ny,wall))
                # 벽이고 방문한 적 없을 경우 최대 부실수 있는 벽보다 적게 부셨을 경우에만 이동
                elif arr[nx][ny]==1 and wall < k and visited[wall+1][nx][ny] == 0:
                    visited[wall+1][nx][ny] = visited[wall][x][y] + 1 # 이동횟수+1
                    queue.append((nx,ny,wall+1))

    # (n,m)칸에 도착이 불가능 할 경우 -1 리턴
    return -1

print(bfs(0,0))