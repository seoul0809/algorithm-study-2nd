# 카드 정렬하기
# 276ms, 119060kb
# 우선순위 큐 (heapq), 그리디, 정렬
# 그리디: 매 상황에서 무조건 가장 작은 크기의 두 카드 묶음을 합치고 다시 리스트에 삽입하면 된다.
# 반례: 20, 30, 40, 45
# 20과 30 비교 => 50 (40, 45, 50)
# 40과 45 비교 => 85 (50, 85)
# 50과 85 비교 => 135
# result => 270

import sys, heapq

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
heap = [int(input().rstrip()) for _ in range(N)]
heap.sort()
result = 0
while len(heap) >= 2:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    sum = first + second
    heapq.heappush(heap, sum)
    result += sum
print(result)