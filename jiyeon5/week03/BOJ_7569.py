'''
푼 시간 : 68분
성능 : 메모리 216944KB, 시간 3148ms (pypy)
주의할 점 :
    3차원 배열 [[] for _ in range(높이)] 로 초기화 : 입력시 행단위 list로 입력받기 때문
    탐색 시작점이 하나가 아닐 경우 배열 인덱스와 더불어 구하는 값을 갱신하는 로직 필요
'''

from collections import deque

# 상자 가로, 세로, 높이 입력 받기
m, n, h = map(int,input().split())
# 토마토의 정보를 담는 3차원 배열
tomato = [[] for _ in range(h)]
# 토마토 정보 입력 받기
for i in reversed(range(h)): # 가장 밑의 상자부터 입력되므로
    for j in range(n):
        tomato[i].append(list(map(int,input().split())))

# 상,하,좌,우,위,아래
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

# bfs 탐색
def bfs(x,y,z,d):
    queue = deque([(x,y,z,d)])

    # queue가 빌때까지 반복
    while queue:
        x, y, z, d = queue.popleft()

        # 6방향으로 탐색
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            nd = d + 1

            # 범위 내에 있을 때만 탐색 진행
            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                # 아직 토마토가 익지 않은 경우 또는 현재보다 익을 때까지 걸린 날이 더 크게 기록된 경우
                if tomato[nz][nx][ny] == 0 or tomato[nz][nx][ny] > nd:
                    # 토마토가 익은 날 저장 하며 큐에 저장
                    tomato[nz][nx][ny] = nd
                    queue.append((nx,ny,nz,nd))

for i in range(h):
    for j in range(n):
        for k in range(m):
            # 원래부터 익은 토마토를 만나면 bfs 실행
            if tomato[i][j][k] == 1:
                bfs(j,k,i,1)

# 토마토가 익을때까지 걸리는 최소 시간을 구하는 함수
def check():
    answer = -1
    for i in range(h):
        for j in range(n):
            for k in range(m):
                # 토마토가 모두 익지 않았으면 0 리턴
                if tomato[i][j][k] == 0:
                    return 0
                # 해당 토마토가 answer보다 크면 answer 갱신
                answer = max(answer, tomato[i][j][k])
    return answer

# 정답 출력
print(check()-1) # 익은토마토를 1으로 계산하여 날짜계산을 했으므로 -1하여 정답 구한다
