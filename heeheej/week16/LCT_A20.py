# 감시 피하기
# 117064kb, 208ms
# 그냥 반복문으로 풀거나 bfs로 풀 수 있었을 것 같다.
# dfs 연습하려고 굳이 dfs로 풀었는데 재귀의 늪에 또 빠져버렸다...
# 어느 부분에서 문제였는지 LCT_A20_2에 정리

import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
board = list()
xList = list()
tList = list()

for i in range(N):
    temp = list(map(str, input().split()))
    board.append(temp)
    for j in range(N):
        if temp[j] == 'X':
            xList.append((i, j))
        elif temp[j] == 'T':
            tList.append((i, j))

def dfs(depth, x, y, dir):
    global flag
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or ny < 0 or nx >= N or ny >= N or board[nx][ny] == 'O':
        flag = False
        return
    if board[nx][ny] == 'S':
        flag = True
        return
    dfs(depth + 1, nx, ny, dir)

def isCaughtByTeacher(x, y):
    for d in range(4):
        dfs(0, x, y, d)
        if flag:
            return True
    return False

combs = combinations(xList, 3)
for comb in combs:
    for i, j in comb:
        board[i][j] = 'O'

    flag = False
    for i, j in tList:
        if isCaughtByTeacher(i, j):
            flag = True
            break

    if not flag:
        print("YES")
        sys.exit()

    for i, j in comb:
        board[i][j] = 'X'

print("NO")
