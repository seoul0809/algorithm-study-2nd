# 거짓말
# 116ms, 114328kb
# union-find
# 핵심: 이미 지나간 파티에 새롭게 진실을 알게된 사람이 생길 수 있으므로 M번 반복한다

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
knowList = set(input().split()[1:])
arr = [set(input().split()[1:]) for _ in range(M)]

for _ in range(M):
    for party in arr:   # 이미 지나간 파티에 새롭게 진실을 알게된 사람이 생길 수 있으므로 상위에서 M번 반복한다.
        if party & knowList:  # 교집합이 있다면 (겹치는 원소가 있다면)
            knowList = knowList.union(party)

result = 0
for party in arr:
    if party & knowList:    # 교집합이 없다면 (겹치는 원소가 없다면)
        continue
    result += 1

print(result)