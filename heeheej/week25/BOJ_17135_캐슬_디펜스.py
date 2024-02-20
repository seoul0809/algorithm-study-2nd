# 캐슬 디펜스
# 116732kb, 312ms
# 구현 문제
# 중첩된 반복문이 많을 때 -> 각 변수 초기화하는 것을 잊지말고, 초기화 위치도 잘 생각해주자
import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M, D = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(N)]
orig_enemies = []
for i in range(N):
    for j in range(M):
        if origin[i][j] == 1:
            orig_enemies.append((i, j))
orig_enemies.sort(key = lambda x : x[1])
enemy_cnt = len(orig_enemies)
visited = [False]*enemy_cnt
result = -1
INF = 1e9
combs = combinations([(N, i) for i in range(M)], 3)

for comb in combs:
    temp = [row[:] for row in origin]
    cnt = enemy_cnt
    visited = [False]*enemy_cnt
    enemies = [row[:] for row in orig_enemies]
    total_kill_cnt = 0  # 궁수의 공격으로 제거한 적의 수
    while cnt > 0:
        targets = []
        for x, y in comb:   # 궁수마다 반복
            dists = [INF]*enemy_cnt
            for i in range(enemy_cnt):
                if not visited[i]:
                    a, b = enemies[i]
                    dist = abs(x-a)+abs(y-b)
                    if dist <= D:
                        dists[i]= dist
            min_dist = min(dists)
            if min_dist != INF:
                for i, dist in enumerate(dists):
                    if dist == min_dist:
                        targets.append(i)
                        break
        kill_cnt = 0
        for i in targets:
            if not visited[i]:
                visited[i] = True
                x, y = enemies[i]
                temp[x][y] = 0
                kill_cnt += 1
        cnt -= kill_cnt
        total_kill_cnt += kill_cnt

        # 적 이동시키기
        for i, pos in enumerate(enemies):
            if not visited[i]:
                x, y = pos[0], pos[1]
                nx = x+1
                if nx >= N:
                    visited[i] = True
                    cnt -= 1
                    temp[x][y] = 0
                else:
                    enemies[i] = (nx, y)
                    temp[x][y] = 0
                    temp[nx][y] = 1
    result = max(result, total_kill_cnt)
print(result)