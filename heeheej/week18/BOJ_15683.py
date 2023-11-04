# 감시
# 118296kb, 408ms
# 주의: cctv가 없을 때 까지 고려

import pprint
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
arr = [[]
    , [[0], [1], [2], [3]]
    , [[0, 2], [1, 3]]
    , [[0, 1], [1, 2], [2, 3], [3, 0]]
    , [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
    , [[0, 1, 2, 3]]]

cnt = 0
result = float('inf')
N, M = map(int, input().split())
origin_board = [list(map(int, input().split())) for _ in range(N)]
cctvs = list()
for i in range(N):
    for j in range(M):
        if origin_board[i][j] == 0:
            cnt += 1
        elif 1 <= origin_board[i][j] <= 5:
            cctvs.append((i, j))
K = len(cctvs)

def watch(x, y, dir, board):
    remove_list = list()
    nx, ny = x, y
    while True:
        nx += dx[dir]
        ny += dy[dir]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny] == 6:
            break
        if board[nx][ny] == 0:
            board[nx][ny] = -1
            remove_list.append((nx, ny))
    return remove_list

def dfs(depth, board, total):   # depth: 몇번째 cctv인지, total: 사각지대 개수
    if depth == K:
        global result
        result = min(result, total)
        return

    x, y = cctvs[depth]
    n = board[x][y] # cctv 정보
    len1 = len(arr[n])
    for l in range(len1):
        len2 = len(arr[n][l])
        # 감시받는 영역을 -1로 표시
        temp_board = [row[:] for row in board]
        remove_list = list()
        for m in range(len2):
            remove_list.append(watch(x, y, arr[n][l][m], temp_board))
        # 표시 완료

        # 사각지대 개수 다시세기
        new_total = 0
        for a in range(N):
            for b in range(M):
                if temp_board[a][b] == 0:
                    new_total += 1

        # dfs 호출 (다음 cctv)
        dfs(depth+1, [row[:] for row in temp_board], new_total)

        # -1로 표시했던 부분 되돌리기
        for list1 in remove_list:
            for a, b in list1:
                board[a][b] = 0

result = cnt
if cctvs:
    dfs(0, origin_board, result)

print(result)