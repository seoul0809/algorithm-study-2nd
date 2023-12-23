# 블록 이동하기
# bfs + 구현문제

from collections import deque

N = -1

def get_next_pos(cur, board):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    next_pos = list()
    pos = list(cur)
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    for i in range(4):
        nx1, ny1, nx2, ny2 = x1 + dx[i], y1 + dy[i], x2 + dx[i], y2 + dy[i]

        if board[nx1][ny1] == 1 or board[nx2][ny2] == 1:
            continue
        next_pos.append({(nx1, ny1), (nx2, ny2)})
        next_pos.append({(x2, y2), (nx2, ny2)})
        next_pos.append({(x1, y1), (nx1, ny1)})
    return next_pos

def bfs(x1, y1, x2, y2, board):
    visited = list()
    q = deque()
    q.append(({(1, 1), (1, 2)}, 0))   # x1, y1, x2, y2, 시간
    visited.append({(1, 1), (1, 2)})
    while q:
        pos, t = q.popleft()
        if (N-2, N-2) in pos:
            return t
        
        for next_pos in get_next_pos(pos, board):
            if next_pos in visited:
                continue
            q.append((next_pos, t + 1))
            visited.append(next_pos)

    return 0

def solution(board):
    global result
    global N
    N = len(board) + 2
    
    nboard = [[1]*N for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, N-1):
            nboard[i][j] = board[i-1][j-1]
    
    return bfs(1, 1, 1, 2, nboard)