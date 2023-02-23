# 마인크래프트
# 804ms, 117424kb
# 완전탐색.. 모든 높이가 다 가능성있다고 생각하고 다 돌려본다.

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M, B = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]
result = float('inf')
resultH = 0
for h in range(257):    # h는 기준이 되는 높이
    cnt1, cnt2 = 0, 0   # 인벤토리에서 꺼내야하는 블록개수, 제거하여 인벤토리에 넣을 블록개수
    for i in range(N):
        for j in range(M):
            if _map[i][j] < h:
                cnt1 += (h - _map[i][j])
            else:
                cnt2 += (_map[i][j] - h)

    if B + cnt2 < cnt1:
        continue
    time = cnt1+cnt2*2
    if result >= time:  # 같은 경우도 포함해줘야 같은 시간에서 가장 높은 높이가 result가 됨
        result = time
        resultH = h
print(result, resultH)