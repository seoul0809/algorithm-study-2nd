# 11-1 모험가 길드
# 그리디
# 공포도를 기준으로 오름차순으로 정렬하면 항상 최소한의 모함가의 수만 포함하여 그룹을 결성하게 되므로
# 최적의 해를 찾을 수 있다. => 그리디!

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = 0
cnt = 0

for n in arr:
    cnt += 1
    if cnt >= n:
        result += 1
        cnt = 0
print(result)