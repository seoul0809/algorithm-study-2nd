# 아이템 줍기
# 프로그래머스 코딩테스트 고득점 kit > bfs/dfs
# 1206 (+9)
# 직사각형의 가로 혹은 세로가 1이거나, 변의 길이가 1인 ㄷ자모양 길을 지날 때 bfs가 원하는대로 작동 못한다.
# 좌표를 2배씩 해주면 해결할 수 있다!
# 테두리 표시
# 1. 먼저 모든 좌표를 -1로 초기화
# 2. 테두리가 아닌 내부는 0으로, 테두리는 1로 채움
# 3. 다른 직사각형 반복문 돌 때, 이미 0이면 다른 직사각형의 내부인 것이므로 아무것도 안해주고
#    다른 직사각형의 내부가 아니여서 0이 아닌 경우 테두리이므로 1로 표시

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    N = 50
    board = [[-1]*(2*N+2) for _ in range(2*N+2)]
    visited = [[-1]*(2*N+2) for _ in range(2*N+2)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 0
                elif board[i][j] != 0:  # 다른 직사각형의 내부가 아니면서 현재 직사각형의 테두리일 때 1로 채움
                    board[i][j] = 1
    
    def bfs():
        q = deque()
        q.append((2*characterX, 2*characterY))
        nonlocal visited
        visited[2*characterX][2*characterY] = 0

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= 0 or ny <= 0 or nx > 2*N or ny > 2*N or visited[nx][ny] != -1 or board[nx][ny] != 1:
                    continue

                if nx == 2*itemX and ny == 2*itemY:
                    return (visited[x][y] + 1)
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    
    answer = bfs() // 2
    return answer