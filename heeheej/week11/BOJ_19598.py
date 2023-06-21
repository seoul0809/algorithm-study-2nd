# 최소 회의실 개수
# 126708kb, 492ms

import sys, heapq

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
time = [tuple(map(int, input().split())) for _ in range(N)]
time.sort()
q = []
heapq.heappush(q, time[0][1])   # 회의 시작 시간이 가장 빠른 회의가 끝나는 시간을 q라는 힙큐에 넣는다.
time.pop(0)
cnt = 1
for start, end in time:
    if q[0] <= start:
        heapq.heappop(q)
    else:
        cnt += 1
    heapq.heappush(q, end)

print(cnt)