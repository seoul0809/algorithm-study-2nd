# 계란으로 계란치기
# 1436ms, 122228kb
# dfs(재귀) 이용

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
result = -1 # 최대로 깰 수 있는 계란
def dfs(depth):
    if depth == N:
        global result
        # 깨진 계란 개수 한번에 세기
        cnt = 0
        for x, y in info:
            if x <= 0:
                cnt += 1
        result = max(result, cnt)
        return

    if info[depth][0] <= 0:    # 손에 든 계란이 깨졌을 때는 치지 않고 넘어간다.
        dfs(depth + 1)
    else:
        flag = True # 모든 계란이 깨졌는지(깨지지 않은 다른 계란이 없는지) 여부
        for i in range(N):
            if depth != i and info[i][0] > 0:
                flag = False
                info[i][0] -= info[depth][1]
                info[depth][0] -= info[i][1]
                dfs(depth + 1)
                info[i][0] += info[depth][1]
                info[depth][0] += info[i][1]
        if flag:
            dfs(N)

dfs(0)
print(result)