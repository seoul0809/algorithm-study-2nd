'''
푼 시간 : 42분
성능 : 메모리 34132KB, 시간 1528ms
주의할 점 :
    2차원배열 선언 : [[0]*n for _ in range(n)]
'''

from collections import deque

# 테스트 케이스의 수 입력받기
t= int(input())

# 나이트가 이동할 수 있는 방향
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]

# bfs탐색
def bfs(x,y):
    queue = deque([(x,y)])

    while queue:
        x,y = queue.popleft()

        # 8방향을 돌면서 탐색 반복
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            # 체스판 위에 있을 때만 이동 진행
            if 0<=nx<I and 0<=ny<I:
                # 나이트가 이동하려는 칸일 경우 이동횟수를 입력한 후 리턴
                if arr[nx][ny] == -2:
                    arr[nx][ny] = arr[x][y]+1
                    return
                # 한번도 이동한 적 없을 경우 이동
                if arr[nx][ny] == -1:
                    arr[nx][ny] = arr[x][y]+1
                    queue.append((nx,ny))

# 테스트 케이스의 수만큼 반복
for _ in range(t):
    # 체스판 한변의 길이 입력받기
    I= int(input())
    # 체스판 -1로 초기 세팅
    arr = [[-1]*I for _ in range(I)]
    # 현재 나이트가 있는 칸 입력받고 0으로 세팅
    x, y = map(int, input().split())
    arr[x][y] = 0
    # 나이트가 이동하려는 칸 입력받고 -2로 세팅
    nx, ny = map(int, input().split())
    arr[nx][ny] = -2
    # bfs 탐색 진행
    bfs(x,y)
    # 정답 출력
    print(arr[nx][ny])
