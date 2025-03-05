# 마법사 상어와 비바라기
# 113892kb, 504ms
# 구현 문제
# 문제에서 시키는대로 잘 구현한다..
# N행/열에서 1행/열로, 1행/열에서 N행/열로 넘어가기 때문에 mod 연산으로 값을 계산해준다
# 주의: 좌표가 1부터 N까지이므로 mod연산 후에 0이 되는 경우, N으로 바꿔줘야 함

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N, M = map(int, input().split())
board = [[0]*(N+1)]+[[0] + list(map(int, input().split())) for _ in range(N)]
cmds = [tuple(map(int, input().split())) for _ in range(M)]
clouds = [(N, 1), (N, 2), (N-1, 1), (N-1, 2)]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def count_water_basket(x, y):
    cnt = 0
    for i in range(2, 9, 2):    # 2, 4, 6, 8번 방향이 대각선 방향이다
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 1 or nx > N or ny < 1 or ny > N:
            continue
        if board[nx][ny] != 0:
            cnt += 1
    return cnt

for d, s in cmds:
    new_clouds = []
    # print(clouds)
    for x, y in clouds:
        nx = (x + dx[d]*s) % N
        ny = (y + dy[d]*s) % N
        if nx == 0:
            nx = N
        if ny == 0:
            ny = N

        # print(f"x, y: {x}, {y} / nx, ny: {nx}, {ny}")
        new_clouds.append((nx, ny))
    # print("new clouds")
    # print(new_clouds)
    for x, y in new_clouds:
        board[x][y] += 1
    for x, y in new_clouds:
        board[x][y] += count_water_basket(x, y)
    clouds = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            if (i, j) not in new_clouds and board[i][j] >= 2:
                clouds.append((i, j))
                board[i][j] -= 2

    # for i in range(1, N+1):
    #     print(board[i][1:])
    
result = 0
for i in range(1, N+1):
    result += sum(board[i])
print(result)