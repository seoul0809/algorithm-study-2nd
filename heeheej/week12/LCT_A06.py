# 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i, v in enumerate(food_times):
        heapq.heappush(q, (v, i + 1))

    length = len(food_times)  # 남은 음식 개수
    sum_val = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간

    while sum_val + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_val += (now - previous) * length
        length -= 1  # 담 거은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_val) % length][1]