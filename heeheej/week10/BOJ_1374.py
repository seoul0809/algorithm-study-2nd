# 강의실
# 127540kb, 460ms
# 힙큐 두 개 사용
# remain은 남은 강의(아직 강의실을 배정시키지 않은 강의)들을 시작시간 기준으로 항상 정렬해놓는 힙큐
# q는 각 강의실마다 마지막강의의 끝나는 시간이 저장되어있는 힙큐
# q에서 끝나는 시간이 가장 빠른 강의를 다음 강의의 시작시간과 비교해서 시간대가 맞으면 다음 강의의 강의실을 배정한다.

import sys
import heapq

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
remain = []   # (시작시간, 끝나는시간)
q = []      # 끝나는시간
for i in range(N):
    n, start, end = map(int, input().split())
    heapq.heappush(remain, (start, end))

# 일단 시작시간이 가장 빠른 강의를 배정시키고, q에 넣는다.
heapq.heappush(q, heapq.heappop(remain)[1])

while remain:   # 아직 배정시키지 않은 강의가 남아있는 한 반복한다.
    start, end = heapq.heappop(remain)  # 아직 배정시키지 않은 강의 중 시작시간이 가장 빠른 강의(a라 하자.)를 꺼낸다.
    # 강의실 별 마지막 강의들 중에서 끝나는 시간이 가장 빠른 강의(b라 하자.)가 꺼낸 강의(a)의 시작시간보다 작거나 같을 경우,
    # b가 사용하는 강의실의 마지막 강의는 b에서 a로 교체 된다. 따라서 q에서 b에 대한 정보를 빼준다.
    if q[0] <= start:
        heapq.heappop(q)
    # a가 b가 쓰는 강의실이 배정이 되었다면 a는 b가 사용하는 강의실의 마지막 강의로서,
    # a를 b가 쓰는 강의실에 배정할 수 없었다면 새 강의실을 배정하고 그 강의실의 처음이자 마지막 강의로서,
    # q에 a 강의의 끝나는 시간을 push한다.
    heapq.heappush(q, end)

# 강의실을 모두 배정시키고 나면, 각 강의실의 마지막 강의들만 남게 되고 q의 길이는 곧 강의실 개수가 된다.
print(len(q))