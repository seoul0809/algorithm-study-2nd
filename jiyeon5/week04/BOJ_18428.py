from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(input().split())
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i,j))
        elif board[i][j] == 'X':
            spaces.append((i,j))

def watch(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    find =False

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        while 0<=nx<n and 0<=ny<n:
            if board[nx][ny]=='S':
                find = True
                break
            elif board[nx][ny]=='O':
                find = False
                break
            nx += dx[i]
            ny += dy[i]

        if find:
            return True

    return False

def check():
    for x,y  in teachers:
        if watch(x,y):
            return True
    return False

for col in combinations(spaces,3):
    for x,y in col:
        board[x][y]='O'

    if not check():
        print('YES')
        exit(0)

    for x,y in col:
        board[x][y]='X'

print('NO')