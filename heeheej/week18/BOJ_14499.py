# 주사위 굴리기
# 구현 문제
# 114328kb, 128ms
'''
문제에서 말하는 주사위 전개도를 1차원 배열 dice = [0]*6 으로 표현
2번이 주사위 윗면이고 5번이 주사위 바닥면으로 고정
  0
1 2 3
  4
  5
주사위가 동, 서, 남, 북으로 이동할 때 (굴러갈때) 전개도 상에서 어떻게 바뀌는지 파악하고,
roll_dice 함수에서 처리해주도록 구현
'''
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dice = [0]*6
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

def roll_dice(d):
    global dice
    back, left, up, right, front, down = dice
    if d == 1:    # 동
        dice[1], dice[2], dice[3], dice[5] = down, left, up, right
    elif d == 2:  # 서
        dice[1], dice[2], dice[3], dice[5] = up, right, down, left
    elif d == 3:  # 북
        dice[0], dice[2], dice[4], dice[5] = up, front, down, back
    else:   # 남
        dice[0], dice[2], dice[4], dice[5] = down, back, up, front

nx, ny = x, y
for c in commands:
    nx += dx[c]
    ny += dy[c]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        nx -= dx[c]
        ny -= dy[c]
        continue

    roll_dice(c)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[2])
