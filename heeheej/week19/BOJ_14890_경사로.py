# 경사로
# 115416kb, 124ms
# 구현 문제
# x축, y축 방향으로 각각 현재칸과 다음칸과의 높이차이를 담는 2차원 배열을 만든다.
# x축방향 (아래쪽 방향) N개 열을 대상으로  check 함수 시행
# check 함수 내에서 왼쪽부터 순서대로 아래 과정 시행
# 1. 다음칸과의 차이를 diff라 할 때, diff가 0이면 pass
# 2. diff의 절댓값이 2이면 해당 열은 지나갈 수 있는 길 X
# 3. diff가 1이면 경사로 세울 수 있는지 확인하기
#    -> 범위 벗어나거나, 높이가 달라지거나, 이미 경사로 세웠다면 지나갈 수 있는 길 X
# 4. 경사로 세울 수 있다고 판단했다면 경사로 세우는 작업
# 모든 과정을 통과했다면 x번째 열은 경사로를 세울 수 있는 길임
# 이를 y축 방향 (오른쪽 방향) N개 행을 대상으로도 시행

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
diff_y = [[0]*N for _ in range(N)]  # (오른쪽) y축 방향으로 현재 칸과 다음 칸과의 높이차이
diff_x = [[0]*N for _ in range(N)]  # (아래쪽) x축 방향으로 현재 칸과 다음 칸과의 높이차이
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N-1):
        now = board[i][j]
        diff_y[i][j] = board[i][j+1] - now

# 차이 구한 후, 역행렬 형태로 값이 들어가도록 함
for i in range(N-1):
    for j in range(N):
        now = board[i][j]
        diff_x[j][i] = board[i+1][j] - now

# def printArray(arr):
#     print("==================")
#     for i in range(N):
#         print(arr[i])

def check(x, diff):
    for j in range(N-1):
        val = diff[x][j]
        if val == 0:
            continue
        if abs(val) >= 2:
            return False
        elif val == 1:
            nj = j
            if visited[x][j]:
                return False
            for _ in range(L-1):
                nj -= 1
                if nj < 0 or diff[x][nj] != 0 or visited[x][nj]:
                    return False
            # 경사로 세우기
            nj = j
            for _ in range(L):
                visited[x][nj] = True
                nj -= 1
        elif val == -1:
            nj = j
            for _ in range(L-1):
                nj += 1
                if nj >= N-1 or diff[x][nj] != 0 or visited[x][nj]:
                    return False
            # 경사로 세우기
            nj = j
            for _ in range(L):
                nj += 1
                visited[x][nj] = True
    
    return True

result = 0
for i in range(N):
    if check(i, diff_x):
        result += 1

visited = [[False]*N for _ in range(N)] # 경사로 정보 초기화
for i in range(N):
    if check(i, diff_y):
        result += 1

print(result)