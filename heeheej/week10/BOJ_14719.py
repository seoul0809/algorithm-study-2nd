# 빗물
# 116360kb, 128ms
# 구현 문제

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
H, W = map(int, input().split())
height = list(map(int, input().split()))
_map = [[False]*W for _ in range(H)]
for i in range(W):
    h = height[i]
    for j in range(h):
        _map[j][i] = True

result = 0
for i in range(H):
    flag = False # 카운트 시작했는지 여부
    cnt = 0
    for j in range(W):
        if _map[i][j]:  # 블록이면
            if not flag:    # 빗물 카운트 시작 안했다면 시작해야함
                cnt = 0
                flag = True
            elif flag:  # 빗물 카운트 시작 이미 했는데 다시 블록을 만난 것이므로 지금까지 cnt를 결과에 반영
                result += cnt
                cnt = 0
        else:  # 블록이 아니면
            if flag:
                cnt += 1
print(result)